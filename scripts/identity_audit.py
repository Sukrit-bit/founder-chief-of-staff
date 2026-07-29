#!/usr/bin/env python3
"""Block legacy project identity from the current public repository."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


LEGACY_PATTERNS = {
    "legacy_product_name": re.compile(r"founder\s+research\s+os", re.IGNORECASE),
    "legacy_repo_slug": re.compile(r"founder-research-os", re.IGNORECASE),
    "legacy_category": re.compile(r"research\s+operating\s+system", re.IGNORECASE),
    "legacy_short_category": re.compile(r"research\s+os", re.IGNORECASE),
}

TEXT_SUFFIXES = {".md", ".html", ".py", ".yml", ".yaml", ".svg", ".txt", ".json"}
SKIP_PATHS = {"scripts/identity_audit.py"}


def find_legacy_identity(text: str) -> list[str]:
    return [name for name, pattern in LEGACY_PATTERNS.items() if pattern.search(text)]


def self_test() -> list[str]:
    failures: list[str] = []
    if find_legacy_identity("Founder Chief of Staff coordinates company state and execution."):
        failures.append("positive identity fixture was incorrectly rejected")

    negative = find_legacy_identity("Clone founder-research-os and start Founder Research OS.")
    expected = {"legacy_product_name", "legacy_repo_slug"}
    if not expected.issubset(set(negative)):
        failures.append("negative identity fixture escaped the guard")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()

    failures = self_test()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: identity audit positive and negative self-tests")

    repo = pathlib.Path(args.repo).resolve()
    findings: list[str] = []
    for path in sorted(repo.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or path.suffix.lower() not in TEXT_SUFFIXES
        ):
            continue
        relative = path.relative_to(repo).as_posix()
        if relative in SKIP_PATHS:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in find_legacy_identity(line):
                findings.append(f"{relative}:{line_no}:{match}")

    if findings:
        for finding in findings:
            print(f"FAIL: {finding}")
        return 1

    print("PASS: no legacy project identity remains")
    return 0


if __name__ == "__main__":
    sys.exit(main())
