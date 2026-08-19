#!/usr/bin/env python3
"""Audit the v0.3.0 public claim contract and narrative migration."""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "release-v0.3.1" / "claim_contract.json"
SURFACES = [
    "README.md", "PRD.md", "TECHNICAL.md", "index.html",
    "docs/MEMORY_AND_SYNTHESIS.md", "docs/CONTINUOUS_IMPROVEMENT_LOOP.md",
    "docs/PROOF_OF_OPERATION.md", "docs/LAUNCH_ESSAY.md",
    "docs/EXTERNAL_WRITING_STANDARD.md",
    "docs/WALKTHROUGH_SCRIPT.md", "visuals/operating-loop.html",
    "assets/social-card.svg"
]

def normalized(path: pathlib.Path) -> str:
    return re.sub(r"\s+", " ", path.read_text(encoding="utf-8", errors="ignore").lower())

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)

def main() -> int:
    if not CONTRACT.exists():
        fail("release claim contract is missing")
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    for item in contract["shipped_claims"]:
        if not item.get("evidence"):
            fail(f"{item['claim_id']} has no evidence")
        for evidence in item["evidence"]:
            if not (ROOT / evidence).exists():
                fail(f"{item['claim_id']} references missing evidence: {evidence}")
    for surface in SURFACES:
        if not (ROOT / surface).exists():
            fail(f"required public surface is missing: {surface}")
    texts = [normalized(ROOT / path) for path in SURFACES]
    combined = " ".join(texts)
    required = {
        "strategic outcome": "durable operating partner", "canonical memory": "canonical",
        "bounded retrieval": "bounded", "relationships": "relationship",
        "task-time controls": "task-time", "learning evidence": "learning evidence",
        "synthetic boundary": "synthetic", "live proof boundary": "live",
        "derived index boundary": "derived index",
        "external reader gate": "external writing"
    }
    missing = [label for label, phrase in required.items() if phrase not in combined]
    if missing:
        fail("narrative concepts missing: " + ", ".join(missing))
    prohibited = [
        r"proven autonomous learning", r"general live reliability (?:is|has been) proven",
        r"ships with (?:a )?vector database", r"ships with (?:a )?graph database",
        r"ships with gmail ingestion", r"sqlite (?:database|index) is (?:the )?source of truth"
    ]
    for pattern in prohibited:
        if any(re.search(pattern, text) for text in texts):
            fail(f"prohibited overclaim found: {pattern}")
    print(f"PASS: claim contract and {len(SURFACES)} narrative surfaces are aligned")
    return 0

if __name__ == "__main__":
    sys.exit(main())
