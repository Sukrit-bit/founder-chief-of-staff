#!/usr/bin/env python3
"""Verify local Markdown links and referenced files."""

from __future__ import annotations
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

def main() -> int:
    failures: list[str] = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in LINK.findall(path.read_text(encoding="utf-8", errors="ignore")):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{path.relative_to(ROOT)} escapes repository: {target}")
                continue
            if not resolved.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {target}")
    if failures:
        print("FAIL: broken local links")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"PASS: {checked} local Markdown links resolve")
    return 0

if __name__ == "__main__":
    sys.exit(main())
