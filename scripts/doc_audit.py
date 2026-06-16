#!/usr/bin/env python3
"""Audit Founder Research OS docs."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


ROOT_FILES = ["README.md", "PRD.md", "TECHNICAL.md", "PROMPT.md"]
LAUNCH_FILES = [
    "index.html",
    "assets/social-card.svg",
    "assets/social-card.png",
    "docs/WORKING_WITH_AGENT.md",
    "docs/ARTIFACT_LIFECYCLE.md",
    "docs/CONTINUOUS_IMPROVEMENT_LOOP.md",
    "docs/LAUNCH_ESSAY.md",
    "docs/LAUNCH_ESSAY.html",
    "scripts/init_workspace.py",
    "examples/synthetic-municipal-permitting/example_journey.md",
    "examples/synthetic-ai-services-pilot/README.md",
    "examples/synthetic-ai-services-pilot/pilot_evidence.md",
    "examples/synthetic-self-improving-loop/README.md",
    "examples/synthetic-self-improving-loop/improved_next_run.md",
    "templates/artifact_card.md",
    "templates/continuous_improvement_entry.md",
    "templates/pilot_evidence.md",
    "templates/protocol_change.md",
]

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


def check_launch_surface(repo: pathlib.Path) -> list[tuple[str, str]]:
    results = []
    for name in LAUNCH_FILES:
        path = repo / name
        if path.exists():
            results.append(result("PASS", f"{name} exists"))
        else:
            results.append(result("FAIL", f"{name} is missing"))

    index = repo / "index.html"
    if index.exists():
        text = normalize(read(index))
        required = ["founder research", "decision pressure", "github", "start in three commands"]
        missing = [term for term in required if term not in text]
        if missing:
            results.append(result("WARN", f"landing page missing launch signals: {', '.join(missing)}"))
        else:
            results.append(result("PASS", "landing page has launch positioning and start path"))

    readme = repo / "README.md"
    if readme.exists():
        text = normalize(read(readme))
        required = ["sukrit-bit.github.io/founder-research-os", "scripts/init_workspace.py", "assets/social-card.svg"]
        missing = [term for term in required if term not in text]
        if missing:
            results.append(result("WARN", f"README missing launch-surface references: {', '.join(missing)}"))
        else:
            results.append(result("PASS", "README points to landing page, starter script, and social card"))

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


def check_framework_completeness(repo: pathlib.Path) -> list[tuple[str, str]]:
    text = "\n".join(read(path) for path in repo.rglob("*.md"))
    normalized = normalize(text)
    required = [
        "synthetic",
        "decision queue",
        "evidence maturity",
        "data handling",
        "founder-agent",
        "artifact lifecycle",
        "public credibility",
        "continuous improvement",
        "protocol change",
        "decision preparation",
    ]
    missing = [term for term in required if term not in normalized]
    if not missing:
        return [result("PASS", "framework completeness signals appear in docs")]
    return [result("WARN", f"framework completeness signals missing: {', '.join(missing)}")]


def check_starter_workspace(repo: pathlib.Path) -> list[tuple[str, str]]:
    script = repo / "scripts" / "init_workspace.py"
    if not script.exists():
        return []

    text = normalize(read(script))
    required = [
        "current_decision_dashboard.md",
        "current_working_state.md",
        "project_artifact_index.md",
        "active_decision_queue.md",
        "failure_mode_register.md",
        "continuous_improvement_log.md",
        "protocol_change_log.md",
        "artifact_card.md",
        "continuous_improvement_entry.md",
        "pilot_evidence.md",
        "protocol_change.md",
    ]
    missing = [term for term in required if term not in text]
    if missing:
        return [result("FAIL", f"starter workspace missing core operating outputs: {', '.join(missing)}")]
    return [result("PASS", "starter workspace creates core operating outputs")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).resolve()
    checks: list[tuple[str, str]] = []
    checks.extend(check_file_exists(repo))
    checks.extend(check_launch_surface(repo))
    checks.extend(check_section_hints(repo / "README.md", "README", README_HINTS))
    checks.extend(check_section_hints(repo / "PRD.md", "PRD", PRD_HINTS))
    checks.extend(check_links(repo))
    checks.extend(check_banned(repo))
    checks.extend(check_framework_completeness(repo))
    checks.extend(check_starter_workspace(repo))

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
