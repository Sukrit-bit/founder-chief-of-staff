#!/usr/bin/env python3
"""Scan the public export for common public-safety mistakes."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


PUBLIC_SAFETY_TERMS = [
    "CONFIDENTIAL:",
    "DO NOT SHARE",
    "BEGIN PRIVATE",
    "REAL CUSTOMER",
    "INTERVIEW TRANSCRIPT",
    "TOKEN=",
    "API_KEY",
    "PASSWORD=",
    "sk-proj-",
    "sk-live-",
    "ghp_",
    "gho_",
]


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).resolve()
    findings: list[tuple[str, int, str]] = []

    for path in sorted(repo.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".html", ".py", ".yml", ".yaml"}:
            continue

        relative = path.relative_to(repo).as_posix()
        if relative == "scripts/public_leak_scan.py":
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, line in enumerate(text.splitlines(), start=1):
            line_norm = normalize(line)
            for term in PUBLIC_SAFETY_TERMS:
                if normalize(term) in line_norm:
                    findings.append((relative, line_no, term))

    if findings:
        print("Potential public-safety issue found:")
        for relative, line_no, term in findings:
            print(f"[FAIL] {relative}:{line_no} matched '{term}'")
        return 1

    print("PASS: no common public-safety terms found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
