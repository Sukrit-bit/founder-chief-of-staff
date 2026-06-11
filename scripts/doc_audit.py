#!/usr/bin/env python3
"""Audit public Founder Research OS docs."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


ROOT_FILES = ["README.md", "PRD.md", "TECHNICAL.md", "PROMPT.md"]

README_HINTS = [
    "what it does",
    "product decision",
    "how it works",
    "result",
    "setup",
    "next",
    "built with",
]

PRD_HINTS = [
    "the problem",
    "the core insight",
    "key decisions",
    "the output",
    "architecture",
    "edge cases",
    "what's next",
    "how it was built",
]

BANNED_PHRASES = [
    "game-changer",
    "paradigm shift",
    "leveraging ai",
    "the landscape of",
    "harnessing the power",
    "important to note",
    "in today's rapidly",
]


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def headings(text: str) -> list[str]:
    return [normalize(line.lstrip("# ")) for line in text.splitlines() if line.startswith("##")]


def result(level: str, message: str) -> tuple[str, str]:
    return level, message


def check_file_exists(repo: pathlib.Path) -> list[tuple[str, str]]:
    results = []
    for name in ROOT_FILES:
        path = repo / name
        if path.exists():
            results.append(result("PASS", f"{name} exists"))
        else:
            results.append(result("FAIL", f"{name} is missing"))
    return results


def check_section_hints(path: pathlib.Path, label: str, hints: list[str]) -> list[tuple[str, str]]:
    if not path.exists():
        return []
    found = headings(read(path))
    results = []
    for hint in hints:
        if any(hint in heading for heading in found):
            results.append(result("PASS", f"{label} has section for '{hint}'"))
        else:
            results.append(result("WARN", f"{label} missing section for '{hint}'"))
    return results


def check_links(repo: pathlib.Path) -> list[tuple[str, str]]:
    readme = repo / "README.md"
    prd = repo / "PRD.md"
    technical = repo / "TECHNICAL.md"
    results = []

    if readme.exists():
        text = normalize(read(readme))
        if "prd.md" in text and "technical.md" in text:
            results.append(result("PASS", "README links to PRD and TECHNICAL"))
        else:
            results.append(result("WARN", "README should link to PRD.md and TECHNICAL.md"))

    if prd.exists():
        text = normalize(read(prd))
        if "technical.md" in text:
            results.append(result("PASS", "PRD links to TECHNICAL"))
        else:
            results.append(result("WARN", "PRD should link to TECHNICAL.md"))

    if technical.exists():
        text = normalize(read(technical))
        if "readme.md" in text and "prd.md" in text:
            results.append(result("PASS", "TECHNICAL links back to README and PRD"))
        else:
            results.append(result("WARN", "TECHNICAL should link back to README.md and PRD.md"))

    return results


def check_banned(repo: pathlib.Path) -> list[tuple[str, str]]:
    results = []
    for name in ROOT_FILES:
        path = repo / name
        if not path.exists():
            continue
        text = normalize(read(path))
        matches = [phrase for phrase in BANNED_PHRASES if phrase in text]
        if matches:
            results.append(result("WARN", f"{name} contains banned phrase(s): {', '.join(matches)}"))
        else:
            results.append(result("PASS", f"{name} has no banned phrase matches"))
    return results


def check_public_boundary(repo: pathlib.Path) -> list[tuple[str, str]]:
    text = "\n".join(read(path) for path in repo.rglob("*.md"))
    normalized = normalize(text)
    if "synthetic" in normalized and "redaction" in normalized and "private" in normalized:
        return [result("PASS", "public/private boundary appears in docs")]
    return [result("WARN", "public/private boundary should be clearer")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).resolve()
    checks: list[tuple[str, str]] = []
    checks.extend(check_file_exists(repo))
    checks.extend(check_section_hints(repo / "README.md", "README", README_HINTS))
    checks.extend(check_section_hints(repo / "PRD.md", "PRD", PRD_HINTS))
    checks.extend(check_links(repo))
    checks.extend(check_banned(repo))
    checks.extend(check_public_boundary(repo))

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for level, message in checks:
        counts[level] += 1
        print(f"[{level}] {message}")

    print("\nSummary:")
    for level in ["PASS", "WARN", "FAIL"]:
        print(f"  {level}: {counts[level]}")

    if counts["FAIL"]:
        return 1
    if args.strict and counts["WARN"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

