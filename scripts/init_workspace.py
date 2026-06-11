#!/usr/bin/env python3
"""Create a starter Founder Research OS workspace."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import shutil
import sys


ROOT_DIRS = [
    "00_Context",
    "01_Themes",
    "03_Problem_Statements",
    "04_Venture_Theses",
    "05_Experiments",
    "06_Decision_Log",
    "07_Source_Material",
    "09_Automation",
    "templates",
]


TEMPLATE_FILES = [
    "source_note.md",
    "pattern_register.md",
    "decision_queue.md",
    "experiment_plan.md",
    "problem_statement.md",
    "company_case_study.md",
    "operating_review.md",
    "session_handoff.md",
]


def write_if_missing(path: pathlib.Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def copy_templates(repo: pathlib.Path, target: pathlib.Path) -> list[pathlib.Path]:
    copied: list[pathlib.Path] = []
    source_dir = repo / "templates"
    dest_dir = target / "templates"
    for name in TEMPLATE_FILES:
        source = source_dir / name
        dest = dest_dir / name
        if source.exists() and not dest.exists():
            shutil.copy2(source, dest)
            copied.append(dest)
    return copied


def current_state(project_name: str, today: str) -> str:
    return f"""# Current Working State

Last updated: {today}
Project: {project_name}

## Current Read

This workspace is the durable memory layer for founder research.

Use it to move from market signals to evidence-backed startup decisions.

## Active Questions

- What market, workflow, or user pain is being explored?
- What evidence exists?
- What evidence is missing?
- What decision should this research pressure next?

## Active Decision Queue

See `../06_Decision_Log/Active_Decision_Queue.md`.

## Next Best Actions

1. Add the first source note in `../07_Source_Material/`.
2. Update a theme in `../01_Themes/`.
3. Add or update a decision queue row.
4. Decide whether the next step is continue, narrow, experiment, park, pause, or kill.
"""


def decision_queue(today: str) -> str:
    return f"""# Active Decision Queue

Last updated: {today}

| Priority | Decision Item | Evidence Maturity | Current Decision | Next Evidence Needed | Next Artifact |
|---:|---|---|---|---|---|
| 1 | First research theme | Raw signal | Continue | First source note and pattern scan | `../07_Source_Material/` |

## Decision Options

- Continue
- Narrow
- Experiment
- Park
- Pause
- Kill
"""


def readme(project_name: str) -> str:
    return f"""# {project_name}

This is a Founder Research OS workspace.

The goal is to turn founder curiosity into evidence-backed startup decisions.

## Operating Loop

```text
input -> artifact -> pattern -> decision queue -> experiment -> evidence -> updated context
```

## Start Here

1. Read `00_Context/Current_Working_State.md`.
2. Add source material in `07_Source_Material/`.
3. Create or update theme notes in `01_Themes/`.
4. Keep `06_Decision_Log/Active_Decision_Queue.md` current.
5. Use templates from `templates/`.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Founder Research OS starter workspace.")
    parser.add_argument("target", help="Path for the new workspace")
    parser.add_argument("--name", help="Project name. Defaults to the target folder name.")
    args = parser.parse_args()

    repo = pathlib.Path(__file__).resolve().parents[1]
    target = pathlib.Path(args.target).expanduser().resolve()
    project_name = args.name or target.name.replace("-", " ").replace("_", " ").title()
    today = dt.date.today().isoformat()

    target.mkdir(parents=True, exist_ok=True)
    created_dirs = []
    for dirname in ROOT_DIRS:
        path = target / dirname
        if not path.exists():
            path.mkdir(parents=True)
            created_dirs.append(path)

    created_files = []
    if write_if_missing(target / "README.md", readme(project_name)):
        created_files.append(target / "README.md")
    if write_if_missing(target / "00_Context" / "Current_Working_State.md", current_state(project_name, today)):
        created_files.append(target / "00_Context" / "Current_Working_State.md")
    if write_if_missing(target / "06_Decision_Log" / "Active_Decision_Queue.md", decision_queue(today)):
        created_files.append(target / "06_Decision_Log" / "Active_Decision_Queue.md")

    copied = copy_templates(repo, target)

    print(f"Created Founder Research OS workspace: {target}")
    print(f"Project name: {project_name}")
    print(f"Directories created: {len(created_dirs)}")
    print(f"Files created: {len(created_files)}")
    print(f"Templates copied: {len(copied)}")
    print("\nStart here:")
    print(f"  {target / '00_Context' / 'Current_Working_State.md'}")
    print(f"  {target / '06_Decision_Log' / 'Active_Decision_Queue.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
