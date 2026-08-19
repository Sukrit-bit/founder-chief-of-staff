#!/usr/bin/env python3
"""Queryable operating-memory and bounded-learning runtime."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sqlite3
from typing import Any, Iterable


RUNTIME_DIR = Path(__file__).resolve().parent
ROOT = RUNTIME_DIR.parent
MANIFEST_PATH = RUNTIME_DIR / "source_manifest.json"
CONTROL_PATH = RUNTIME_DIR / "control_registry.json"
LEARNING_PATH = RUNTIME_DIR / "learning_events.json"
DB_PATH = RUNTIME_DIR / ".runtime" / "professional_chief_of_staff.sqlite3"
PROHIBITED_PARTS = {".git", ".env", "secrets", "credentials", "private"}
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "by", "do", "does",
    "for", "from", "how", "i", "in", "is", "it", "me", "of", "on", "or",
    "our", "that", "the", "this", "to", "was", "we", "were", "what", "where",
    "which", "who", "why", "with", "you"
}


class MemoryError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise MemoryError(f"missing JSON source: {path}") from exc
    except json.JSONDecodeError as exc:
        raise MemoryError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise MemoryError(f"JSON root must be an object: {path}")
    return value


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_tokens(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]{1,}", text.lower())
    return list(dict.fromkeys(word for word in words if word not in STOPWORDS))


def markdown_chunks(text: str) -> list[tuple[str, str]]:
    chunks: list[tuple[str, str]] = []
    heading = "Document"
    body: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            if any(part.strip() for part in body):
                chunks.append((heading, "\n".join(body).strip()))
            heading = match.group(2).strip()
            body = []
        else:
            body.append(line)
    if any(part.strip() for part in body):
        chunks.append((heading, "\n".join(body).strip()))
    return chunks or [("Document", text.strip())]


def json_chunks(value: dict[str, Any]) -> list[tuple[str, str]]:
    chunks: list[tuple[str, str]] = []
    for key, item in value.items():
        chunks.append((str(key), json.dumps(item, indent=2, ensure_ascii=False, sort_keys=True)))
    return chunks or [("Document", "{}")]


def source_chunks(path: Path, text: str) -> list[tuple[str, str]]:
    if path.suffix.lower() == ".json":
        return json_chunks(json.loads(text))
    return markdown_chunks(text)


def validate_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    if manifest.get("schema_version") != 1:
        raise MemoryError("source manifest schema_version must be 1")
    sources = manifest.get("sources")
    if not isinstance(sources, list) or not sources:
        raise MemoryError("source manifest requires a non-empty sources list")
    required = {
        "source_id", "title", "path", "family", "portfolio", "authority",
        "lifecycle", "system_id", "tags", "review_trigger"
    }
    seen: set[str] = set()
    for source in sources:
        if not isinstance(source, dict):
            raise MemoryError("every source must be an object")
        missing = required - set(source)
        if missing:
            raise MemoryError(f"source missing fields {sorted(missing)}: {source}")
        source_id = source["source_id"]
        if source_id in seen:
            raise MemoryError(f"duplicate source_id: {source_id}")
        seen.add(source_id)
        relative = Path(source["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise MemoryError(f"source path must be repository-relative: {relative}")
        resolved = (ROOT / relative).resolve()
        if ROOT.resolve() not in resolved.parents:
            raise MemoryError(f"source escapes repository: {relative}")
        if PROHIBITED_PARTS.intersection({part.lower() for part in relative.parts}):
            raise MemoryError(f"source is prohibited: {relative}")
        if not resolved.is_file():
            raise MemoryError(f"registered source does not exist: {relative}")
        if not isinstance(source["tags"], list) or not all(isinstance(x, str) for x in source["tags"]):
            raise MemoryError(f"source tags must be strings: {source_id}")
    relationships = manifest.get("relationships", [])
    if not isinstance(relationships, list):
        raise MemoryError("relationships must be a list")
    for relationship in relationships:
        if relationship.get("from") not in seen or relationship.get("to") not in seen:
            raise MemoryError(f"relationship points to unknown source: {relationship}")
        if not relationship.get("type"):
            raise MemoryError(f"relationship has no type: {relationship}")
    return sources


def validate_controls(registry: dict[str, Any], source_ids: set[str]) -> list[dict[str, Any]]:
    if registry.get("schema_version") != 1:
        raise MemoryError("control registry schema_version must be 1")
    controls = registry.get("controls")
    if not isinstance(controls, list) or not controls:
        raise MemoryError("control registry requires controls")
    seen: set[str] = set()
    for control in controls:
        cid = control.get("control_id")
        if not cid or cid in seen:
            raise MemoryError(f"missing or duplicate control_id: {cid}")
        seen.add(cid)
        if control.get("risk_tier") not in {"safe_auto", "bounded_operational", "human_gate"}:
            raise MemoryError(f"invalid risk_tier for {cid}")
        for source_id in control.get("source_ids", []):
            if source_id not in source_ids:
                raise MemoryError(f"{cid} points to unknown source {source_id}")
        for field in (
            "task_trigger_regex", "claim_regex", "evidence_regex",
            "required_context_regex", "forbidden_candidate_regex", "allowed_override_regex"
        ):
            if control.get(field):
                try:
                    re.compile(control[field])
                except re.error as exc:
                    raise MemoryError(f"invalid {field} for {cid}: {exc}") from exc
    return controls


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE sources (
  source_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  path TEXT NOT NULL UNIQUE,
  family TEXT NOT NULL,
  portfolio TEXT NOT NULL,
  authority TEXT NOT NULL,
  lifecycle TEXT NOT NULL,
  system_id TEXT NOT NULL,
  review_trigger TEXT NOT NULL,
  tags_json TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  modified_at TEXT NOT NULL,
  indexed_at TEXT NOT NULL
);
CREATE TABLE chunks (
  chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_id TEXT NOT NULL REFERENCES sources(source_id) ON DELETE CASCADE,
  ordinal INTEGER NOT NULL,
  heading TEXT NOT NULL,
  body TEXT NOT NULL,
  UNIQUE(source_id, ordinal)
);
CREATE VIRTUAL TABLE chunks_fts USING fts5(
  source_id UNINDEXED,
  heading,
  body,
  tokenize='porter unicode61 remove_diacritics 2'
);
CREATE TABLE relationships (
  from_source TEXT NOT NULL REFERENCES sources(source_id),
  to_source TEXT NOT NULL REFERENCES sources(source_id),
  relationship_type TEXT NOT NULL,
  PRIMARY KEY(from_source, to_source, relationship_type)
);
CREATE TABLE controls (
  control_id TEXT PRIMARY KEY,
  failure_class TEXT NOT NULL,
  title TEXT NOT NULL,
  risk_tier TEXT NOT NULL,
  status TEXT NOT NULL,
  definition_json TEXT NOT NULL
);
"""


@dataclass
class SearchHit:
    source_id: str
    title: str
    path: str
    family: str
    portfolio: str
    authority: str
    lifecycle: str
    system_id: str
    review_trigger: str
    score: float
    heading: str
    excerpt: str
    relationship: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


class MemoryRuntime:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.manifest = load_json(MANIFEST_PATH)
        self.sources = validate_manifest(self.manifest)
        self.source_map = {item["source_id"]: item for item in self.sources}
        self.control_registry = load_json(CONTROL_PATH)
        self.controls = validate_controls(self.control_registry, set(self.source_map))

    def rebuild(self) -> dict[str, Any]:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.db_path.with_suffix(".tmp")
        if temp.exists():
            temp.unlink()
        connection = sqlite3.connect(temp)
        try:
            connection.executescript(SCHEMA)
            indexed_at = utc_now()
            chunk_count = 0
            for source in self.sources:
                path = ROOT / source["path"]
                text = path.read_text(encoding="utf-8")
                digest = sha256(text.encode("utf-8")).hexdigest()
                modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).replace(microsecond=0).isoformat()
                connection.execute(
                    "INSERT INTO sources VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        source["source_id"], source["title"], source["path"], source["family"],
                        source["portfolio"], source["authority"], source["lifecycle"],
                        source["system_id"], source["review_trigger"],
                        json.dumps(source["tags"], ensure_ascii=False), digest, modified, indexed_at
                    ),
                )
                for ordinal, (heading, body) in enumerate(source_chunks(path, text), start=1):
                    connection.execute(
                        "INSERT INTO chunks(source_id, ordinal, heading, body) VALUES (?, ?, ?, ?)",
                        (source["source_id"], ordinal, heading, body),
                    )
                    connection.execute(
                        "INSERT INTO chunks_fts(source_id, heading, body) VALUES (?, ?, ?)",
                        (source["source_id"], heading, body),
                    )
                    chunk_count += 1
            for relationship in self.manifest.get("relationships", []):
                connection.execute(
                    "INSERT INTO relationships VALUES (?, ?, ?)",
                    (relationship["from"], relationship["to"], relationship["type"]),
                )
            for control in self.controls:
                connection.execute(
                    "INSERT INTO controls VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        control["control_id"], control["failure_class"], control["title"],
                        control["risk_tier"], control["status"], json.dumps(control, ensure_ascii=False)
                    ),
                )
            connection.execute("INSERT INTO metadata VALUES ('schema_version', '1')")
            connection.execute("INSERT INTO metadata VALUES ('built_at', ?)", (indexed_at,))
            connection.commit()
        finally:
            connection.close()
        os.replace(temp, self.db_path)
        database_label = (
            str(self.db_path.relative_to(ROOT))
            if self.db_path.is_relative_to(ROOT)
            else str(self.db_path)
        )
        return {
            "status": "rebuilt",
            "database": database_label,
            "sources": len(self.sources),
            "chunks": chunk_count,
            "relationships": len(self.manifest.get("relationships", [])),
            "controls": len(self.controls),
        }

    def connect(self) -> sqlite3.Connection:
        if not self.db_path.is_file():
            self.rebuild()
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def drift(self) -> list[dict[str, str]]:
        if not self.db_path.is_file():
            return [{"source_id": "DATABASE", "state": "missing"}]
        findings: list[dict[str, str]] = []
        with self.connect() as connection:
            rows = {row["source_id"]: row for row in connection.execute("SELECT source_id, path, content_hash FROM sources")}
        for source in self.sources:
            row = rows.get(source["source_id"])
            if row is None:
                findings.append({"source_id": source["source_id"], "state": "not_indexed"})
                continue
            current = sha256((ROOT / source["path"]).read_bytes()).hexdigest()
            if current != row["content_hash"]:
                findings.append({"source_id": source["source_id"], "state": "stale_index"})
        for source_id in set(rows) - set(self.source_map):
            findings.append({"source_id": source_id, "state": "unregistered_index_entry"})
        return findings

    def _metadata_score(self, source: dict[str, Any], query: str, tokens: list[str]) -> float:
        lowered = query.lower()
        score = 0.0
        if source["source_id"].lower() in lowered:
            score += 60
        if source["title"].lower() in lowered:
            score += 45
        title = source["title"].lower()
        tags = " ".join(source["tags"]).lower()
        haystack = " ".join([
            title, source["family"], source["portfolio"],
            source["authority"], source["review_trigger"], tags
        ]).lower()
        for token in tokens:
            if token in title:
                score += 12
            elif token in tags:
                score += 8
            elif token in haystack:
                score += 3
        if source["lifecycle"] == "current":
            score += 1
        return score

    def search(
        self,
        query: str,
        *,
        limit: int = 8,
        family: str | None = None,
        portfolio: str | None = None,
        expand_relationships: bool = True,
    ) -> list[SearchHit]:
        tokens = normalize_tokens(query)
        scores: dict[str, float] = {}
        excerpts: dict[str, tuple[str, str]] = {}
        for source in self.sources:
            if family and source["family"] != family:
                continue
            if portfolio and source["portfolio"].lower() != portfolio.lower():
                continue
            scores[source["source_id"]] = self._metadata_score(source, query, tokens)
        if tokens:
            fts_query = " OR ".join(f'"{token.replace(chr(34), "")}"' for token in tokens[:18])
            fts_bonus: dict[str, float] = {}
            with self.connect() as connection:
                try:
                    rows = connection.execute(
                        "SELECT source_id, heading, body, bm25(chunks_fts) AS rank "
                        "FROM chunks_fts WHERE chunks_fts MATCH ? ORDER BY rank LIMIT 120",
                        (fts_query,),
                    ).fetchall()
                except sqlite3.OperationalError:
                    rows = []
            for row in rows:
                source_id = row["source_id"]
                if source_id not in scores:
                    continue
                rank_score = 22.0 / (1.0 + abs(float(row["rank"])))
                # A document with many generic matches must not outrank a more
                # relevant authority merely because it has more chunks. Keep
                # the best matching chunk as the source-level lexical signal.
                fts_bonus[source_id] = max(fts_bonus.get(source_id, 0.0), rank_score)
                if source_id not in excerpts:
                    clean = re.sub(r"\s+", " ", row["body"]).strip()
                    excerpts[source_id] = (row["heading"], clean[:420])
            for source_id, bonus in fts_bonus.items():
                scores[source_id] += bonus

        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        relationship_notes: dict[str, str] = {}
        if expand_relationships and ranked:
            seeds = [source_id for source_id, score in ranked[:3] if score > 0]
            if seeds:
                placeholders = ",".join("?" for _ in seeds)
                with self.connect() as connection:
                    rows = connection.execute(
                        f"SELECT * FROM relationships WHERE from_source IN ({placeholders}) OR to_source IN ({placeholders})",
                        (*seeds, *seeds),
                    ).fetchall()
                for row in rows:
                    if row["from_source"] in seeds:
                        neighbor = row["to_source"]
                        note = f"{row['relationship_type']} from {row['from_source']}"
                    else:
                        neighbor = row["from_source"]
                        note = f"{row['relationship_type']} to {row['to_source']}"
                    if neighbor in scores:
                        scores[neighbor] += 9
                        relationship_notes[neighbor] = note
                ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))

        hits: list[SearchHit] = []
        for source_id, score in ranked:
            if score <= 0:
                continue
            source = self.source_map[source_id]
            heading, excerpt = excerpts.get(source_id, ("Source metadata", source["review_trigger"]))
            hits.append(SearchHit(
                source_id=source_id,
                title=source["title"],
                path=source["path"],
                family=source["family"],
                portfolio=source["portfolio"],
                authority=source["authority"],
                lifecycle=source["lifecycle"],
                system_id=source["system_id"],
                review_trigger=source["review_trigger"],
                score=round(score, 3),
                heading=heading,
                excerpt=excerpt,
                relationship=relationship_notes.get(source_id),
            ))
            if len(hits) >= limit:
                break
        return hits

    def applicable_controls(self, task: str) -> list[dict[str, Any]]:
        applicable = []
        for control in self.controls:
            if control.get("status") != "active":
                continue
            if re.search(control["task_trigger_regex"], task):
                applicable.append(control)
        return applicable

    def context_bundle(self, task: str, *, limit: int = 8) -> dict[str, Any]:
        hits = self.search(task, limit=limit)
        controls = self.applicable_controls(task)
        control_sources = {
            source_id for control in controls for source_id in control.get("source_ids", [])
        }
        present = {hit.source_id for hit in hits}
        for source_id in control_sources - present:
            source = self.source_map[source_id]
            hits.append(SearchHit(
                source_id=source_id,
                title=source["title"],
                path=source["path"],
                family=source["family"],
                portfolio=source["portfolio"],
                authority=source["authority"],
                lifecycle=source["lifecycle"],
                system_id=source["system_id"],
                review_trigger=source["review_trigger"],
                score=0.0,
                heading="Applicable control source",
                excerpt="Included because an applicable prior control points to this canonical source.",
                relationship="control source",
            ))
        return {
            "task": task,
            "index_drift": self.drift(),
            "sources": [hit.as_dict() for hit in hits],
            "applicable_controls": [
                {
                    "control_id": control["control_id"],
                    "failure_class": control["failure_class"],
                    "title": control["title"],
                    "risk_tier": control["risk_tier"],
                    "source_ids": control["source_ids"],
                }
                for control in controls
            ],
            "implicated_systems": sorted({hit.system_id for hit in hits}),
            "context_character_count": sum(len(hit.excerpt) for hit in hits),
            "registered_source_count": len(self.sources),
            "authority_rule": "Use each source only for the facts it owns; retrieval does not change canonical state or prove completion.",
        }

    def check_candidate(self, task: str, candidate: str) -> dict[str, Any]:
        results: list[dict[str, Any]] = []
        for control in self.applicable_controls(task):
            passed = True
            reasons: list[str] = []
            claim = bool(control.get("claim_regex") and re.search(control["claim_regex"], candidate))
            if claim and control.get("evidence_regex") and not re.search(control["evidence_regex"], candidate):
                passed = False
                reasons.append(control["failure_message"])
            if control.get("required_context_regex") and not re.search(control["required_context_regex"], candidate):
                passed = False
                reasons.append(control["failure_message"])
            if control.get("forbidden_candidate_regex") and re.search(control["forbidden_candidate_regex"], candidate):
                allowed = bool(control.get("allowed_override_regex") and re.search(control["allowed_override_regex"], candidate))
                if not allowed:
                    passed = False
                    reasons.append(control["failure_message"])
            results.append({
                "control_id": control["control_id"],
                "failure_class": control["failure_class"],
                "risk_tier": control["risk_tier"],
                "passed": passed,
                "reasons": list(dict.fromkeys(reasons)),
            })
        return {
            "task": task,
            "passed": all(result["passed"] for result in results),
            "controls_evaluated": results,
            "note": "Deterministic candidate checks are enforcement evidence, not live same-class proof.",
        }

    def record_outcome(
        self,
        *,
        event_id: str,
        task_id: str,
        control_id: str,
        outcome: str,
        evidence: str,
        correction_chain_id: str | None = None,
    ) -> dict[str, Any]:
        data = load_json(LEARNING_PATH)
        allowed = set(data.get("allowed_outcomes", []))
        if outcome not in allowed:
            raise MemoryError(f"invalid outcome {outcome}; expected one of {sorted(allowed)}")
        control = next((item for item in self.controls if item["control_id"] == control_id), None)
        if control is None:
            raise MemoryError(f"unknown control_id: {control_id}")
        if not event_id or not task_id or not evidence.strip():
            raise MemoryError("event_id, task_id and evidence are required")
        if any(event.get("event_id") == event_id for event in data.get("events", [])):
            raise MemoryError(f"duplicate event_id: {event_id}")
        if outcome == "repeated" and not correction_chain_id:
            raise MemoryError("repeated outcomes require correction_chain_id")
        event = {
            "event_id": event_id,
            "task_id": task_id,
            "failure_class": control["failure_class"],
            "correction_chain_id": correction_chain_id,
            "control_id": control_id,
            "outcome": outcome,
            "evidence": evidence.strip(),
            "occurred_at": utc_now(),
        }
        data.setdefault("events", []).append(event)
        temp = LEARNING_PATH.with_suffix(".tmp")
        temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        os.replace(temp, LEARNING_PATH)
        return event


def format_hits(hits: Iterable[SearchHit]) -> str:
    lines: list[str] = []
    for index, hit in enumerate(hits, start=1):
        lines.append(f"{index}. {hit.title} [{hit.source_id}] — {hit.authority}")
        lines.append(f"   {hit.path} | {hit.heading} | score {hit.score}")
        if hit.relationship:
            lines.append(f"   relationship: {hit.relationship}")
        lines.append(f"   {hit.excerpt}")
    return "\n".join(lines)
