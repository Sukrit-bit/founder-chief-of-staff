#!/usr/bin/env python3
"""Block public releases whose front-door writing fails the external style contract."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "evals" / "release-v0.3.1" / "external_style_contract.json"


class VisibleHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"style", "script", "svg", "pre"}:
            self.skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"style", "script", "svg", "pre"} and self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip and data.strip():
            self.parts.append(data.strip())


def visible_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() == ".html":
        parser = VisibleHTML()
        parser.feed(raw)
        return "\n\n".join(parser.parts)
    if path.suffix.lower() == ".svg":
        root = ET.fromstring(raw)
        return "\n".join(part.strip() for part in root.itertext() if part.strip())
    raw = re.sub(r"```.*?```", " ", raw, flags=re.S)
    raw = re.sub(r"`([^`]+)`", r"\1", raw)
    raw = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", raw)
    raw = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", raw)
    raw = re.sub(r"^#{1,6}\s+(.+)$", r"\1.\n", raw, flags=re.M)
    raw = re.sub(r"^\s*[-*]\s+(.+?)[;.]?\s*$", r"\1.\n", raw, flags=re.M)
    return raw


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w'-]+\b", text)


def sentences(text: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", part.strip())
        for part in re.split(r"(?<=[.!?])\s+|\n+", text.strip())
        if words(part)
    ]


def paragraphs(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", part.strip()) for part in re.split(r"\n\s*\n", text) if words(part)]


def inspect_text(text: str, surface: dict, contract: dict) -> list[str]:
    findings: list[str] = []
    lowered = text.lower()
    for phrase in contract["forbidden_phrases"]:
        if phrase.lower() in lowered:
            findings.append(f"forbidden phrase present: {phrase}")

    text_words = words(text)
    window = " ".join(text_words[: surface["front_window_words"]]).lower()
    dense_hits = [term for term in contract["dense_terms"] if term.lower() in window]
    if len(dense_hits) > surface["max_dense_terms"]:
        findings.append(
            "front-door language exceeds dense-term budget: " + ", ".join(dense_hits)
        )

    sentence_lengths = [len(words(sentence)) for sentence in sentences(text)]
    if sentence_lengths:
        average = sum(sentence_lengths) / len(sentence_lengths)
        if average > surface["max_average_sentence_words"]:
            findings.append(
                f"average sentence length {average:.1f} exceeds {surface['max_average_sentence_words']} words"
            )
        longest = max(sentence_lengths)
        if longest > surface["max_sentence_words"]:
            findings.append(
                f"longest sentence has {longest} words; limit is {surface['max_sentence_words']}"
            )

    long_paragraphs = [len(words(part)) for part in paragraphs(text) if len(words(part)) > surface["max_paragraph_words"]]
    if long_paragraphs:
        findings.append(
            f"paragraph length exceeds {surface['max_paragraph_words']} words: max {max(long_paragraphs)}"
        )
    return findings


def self_test(contract: dict) -> list[str]:
    fixture = {
        "front_window_words": 120,
        "max_dense_terms": 1,
        "max_average_sentence_words": 24,
        "max_sentence_words": 42,
        "max_paragraph_words": 120,
    }
    invalid = (
        "Founder Chief of Staff combines canonical operating sources with bounded retrieval, "
        "source provenance, task-time controls and candidate enforcement. "
        "Style check: external style applied."
    )
    valid = (
        "Founder Chief of Staff helps an AI agent find the right company context and keep work moving. "
        "It also checks whether the agent is about to repeat a known mistake."
    )
    failures: list[str] = []
    if not inspect_text(invalid, fixture, contract):
        failures.append("negative fixture was not rejected")
    if inspect_text(valid, fixture, contract):
        failures.append("positive fixture was rejected")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    args = parser.parse_args()
    repo = args.repo.resolve()
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    failures = self_test(contract)
    if failures:
        print("FAIL: external-style evaluator self-test")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PASS: external-style evaluator rejects the old failure and accepts the plain-language fixture")

    surface_failures = 0
    for surface in contract["surfaces"]:
        path = repo / surface["path"]
        if not path.is_file():
            print(f"FAIL: missing external surface: {surface['path']}")
            surface_failures += 1
            continue
        findings = inspect_text(visible_text(path), surface, contract)
        if findings:
            surface_failures += 1
            print(f"FAIL: {surface['path']} ({surface['audience']})")
            for finding in findings:
                print(f"- {finding}")
        else:
            print(f"PASS: {surface['path']} ({surface['audience']})")

    if surface_failures:
        print(f"FAIL: {surface_failures} external surface(s) need revision")
        return 1
    print("PASS: all declared external surfaces meet the mechanical style contract")
    print("NOTE: the versioned release report must still record the manual 15/45/90-second reader review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
