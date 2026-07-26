#!/usr/bin/env python3
"""Create a starter Founder Chief of Staff workspace."""

from __future__ import annotations

import argparse
import datetime as dt
import json
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
    "08_Execution",
    "09_Automation",
    "templates",
]


TEMPLATE_FILES = [
    "artifact_card.md",
    "continuous_improvement_entry.md",
    "source_note.md",
    "pattern_register.md",
    "decision_queue.md",
    "experiment_plan.md",
    "pilot_evidence.md",
    "protocol_change.md",
    "problem_statement.md",
    "company_case_study.md",
    "operating_review.md",
    "session_handoff.md",
    "daily_operating_console.md",
    "automation_contract.md",
    "implementation_handoff.md",
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

This workspace is the durable operating layer for the founder and AI Chief of Staff.

Use it to keep current state, decisions, relationships, execution, research, and controls aligned.

## Active Questions

- What market, workflow, or user pain is being explored?
- What evidence exists?
- What evidence is missing?
- What decision should this research pressure next?

## Active Decision Queue

See `../06_Decision_Log/Active_Decision_Queue.md`.

## Artifact Index

See `Project_Artifact_Index.md`.

## Operating Control Map

See `Operating_Control_Map.md`.

## Dashboard

See `Current_Decision_Dashboard.md`.

## Daily Operating Console

See `Daily_Operating_Console.md`.

## Continuous Improvement

See `../09_Automation/Continuous_Improvement_Log.md`.

## Next Best Actions

1. Add the first source note in `../07_Source_Material/`.
2. Update a theme in `../01_Themes/`.
3. Add or update a decision queue row.
4. Decide whether the next step is continue, narrow, experiment, park, pause, or kill.
"""


def dashboard(project_name: str, today: str) -> str:
    return f"""# Current Decision Dashboard

Last updated: {today}
Project: {project_name}

## Current Focus

Define the first market, workflow, user pain, or company hypothesis under exploration.

## Current Decision Pressure

| Priority | Decision | Current Status | Next Evidence Needed | Owner |
|---:|---|---|---|---|
| 1 | Choose first research theme | Continue | First source note and first pattern scan | Founder |

## Active Paths

| Path | Evidence Maturity | Current Read | Next Action |
|---|---|---|---|
| First theme | Raw signal | Not enough evidence yet | Create source note |

## Parked Context

- None yet.

## Next Best Actions

1. Capture one real input as a source note.
2. Convert the strongest repeated signal into a pattern row.
3. Update the decision queue with the decision being pressured.
"""


def artifact_index(today: str) -> str:
    return f"""# Project Artifact Index

Last updated: {today}

Use this index so the founder and agent can restart from the workspace without reconstructing chat history.

## Core Operating Files

| Artifact | Purpose | Status |
|---|---|---|
| `Current_Decision_Dashboard.md` | Current focus and decision pressure | Active |
| `Current_Working_State.md` | Full continuity state | Active |
| `Operating_Control_Map.md` | Which files own which jobs | Active |
| `Daily_Operating_Console.md` | Today's execution cockpit | Active |
| `../06_Decision_Log/Active_Decision_Queue.md` | Decisions that need founder judgment | Active |
| `../09_Automation/Automation_Registry.md` | Scheduled or recurring agent workflows | Active |
| `../09_Automation/Failure_Mode_Register.md` | Repeated mistakes and protocol fixes | Active |
| `../09_Automation/Continuous_Improvement_Log.md` | What changed in the OS and why | Active |
| `../09_Automation/Protocol_Change_Log.md` | Protocol and template changes | Active |

## Research Artifacts

| Artifact | Scope Level | Evidence Maturity | Decision Status |
|---|---|---|---|
| None yet | Source | Raw signal | Not decision-bearing |

## Maintenance Rule

When a new strategic artifact is created, add it here.
"""


def operating_control_map(today: str) -> str:
    return f"""# Operating Control Map

Last updated: {today}

Use this file to decide what to read and update. Do not load the whole workspace by default.

## Read Order

1. `Current_Decision_Dashboard.md`
2. `State_Registry.json`
3. `Current_Working_State.md`
4. `Project_Artifact_Index.md`
5. `../06_Decision_Log/Active_Decision_Queue.md`
6. The task-specific canonical source.

## Source-Of-Truth Map

| Need | Source of truth | Update when |
|---|---|---|
| Current focus | Current decision dashboard | Priorities or active bets change |
| Full continuity | Current working state | The project phase, thesis, or active evidence changes |
| Authority and access | State registry | A canonical system or boundary changes |
| Navigation | Project artifact index | A current artifact or active work path is added |
| Founder judgment | Active decision queue | A hypothesis needs continue, narrow, experiment, park, pause, or kill pressure |
| Daily execution | Daily operating console | Today's plan, waiting items, or carryovers change |
| Repeated mistakes | Failure-mode register | The same operating mistake appears twice or creates material risk |
| Scheduled work | Automation registry | A recurring workflow is added or changed |
| System changes | Continuous-improvement log | The OS changes because of correction, eval, or new workflow |
| Rule changes | Protocol-change log | A protocol, template, prompt, or automation contract changes |
| Structural repair proof | Autonomy-control ledger | A structural repair is opened, tested, or closed |

## Boundary Rules

- The dashboard is not a history file.
- The working state is not an artifact index.
- The decision queue is not a task manager.
- The daily console is not the source of truth for research evidence.
- Implementation handoffs should be narrow and safe to share with a build repo.
"""


def state_registry(today: str) -> str:
    payload = {
        "schema_version": "1.0",
        "last_updated": today,
        "systems": [
            {
                "id": "current-dashboard",
                "purpose": "Current focus and decision pressure",
                "location": "00_Context/Current_Decision_Dashboard.md",
                "authority": "canonical",
                "access": "read_write",
                "status": "current",
                "owner": "founder",
                "update_trigger": "Priorities or active bets change",
            },
            {
                "id": "working-state",
                "purpose": "Full current continuity",
                "location": "00_Context/Current_Working_State.md",
                "authority": "canonical",
                "access": "read_write",
                "status": "current",
                "owner": "founder",
                "update_trigger": "Phase, thesis, evidence, or blockers change",
            },
            {
                "id": "decision-queue",
                "purpose": "Founder decisions requiring preparation",
                "location": "06_Decision_Log/Active_Decision_Queue.md",
                "authority": "canonical",
                "access": "read_write",
                "status": "current",
                "owner": "founder",
                "update_trigger": "A strategic call needs preparation",
            },
            {
                "id": "daily-console",
                "purpose": "Founder execution view",
                "location": "00_Context/Daily_Operating_Console.md",
                "authority": "canonical",
                "access": "read_write",
                "status": "current",
                "owner": "founder",
                "update_trigger": "Commitments, dates, blockers, or carryovers change",
            },
            {
                "id": "automation-controls",
                "purpose": "Recurring workflows and structural repair proof",
                "location": "09_Automation",
                "authority": "canonical",
                "access": "read_write",
                "status": "current",
                "owner": "agent",
                "update_trigger": "An automation or control changes",
            },
        ],
        "global_boundaries": [
            "Do not infer material facts, owners, dates, or relationships",
            "External publication, outreach, destructive actions, and strategic commitments are human-gated",
            "Do not store credentials, client work, private notes, or confidential strategy in public paths",
        ],
        "open_contradictions": [],
    }
    return json.dumps(payload, indent=2) + "\n"


def daily_operating_console(today: str) -> str:
    return f"""# Daily Operating Console

Last updated: {today}

Use this file for execution. Keep strategic evidence in the research OS.

## Today

| Rank | Task | Workstream | Priority | Effort | Depth | Next Action |
|---:|---|---|---|---|---|---|
| 1 | Capture first real source note | Research | P1 | 30 min | Medium | Pick one source and use `templates/source_note.md` |

## Waiting

| Task | Waiting On | Follow-Up Date |
|---|---|---|
| None yet |  |  |

## Carryovers

| Task | Carryover Count | Decision Needed |
|---|---:|---|
| None yet | 0 |  |
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


def failure_mode_register(today: str) -> str:
    return f"""# Failure Mode Register

Last updated: {today}

Use this file when the founder or agent notices a repeated operating failure.

| Failure Mode | Example Trigger | Protocol Fix | Status |
|---|---|---|---|
| Summary without system update | Agent summarizes a source but does not create or update an artifact | Create/update artifact, index, and decision queue when input changes project state | Active guardrail |
| Evidence inflation | Public research is treated as validation | Apply evidence maturity label before recommending a decision | Active guardrail |
| Scope collapse | Current wedge is described as the whole company | Name active wedge, parent theme, and parked paths separately | Active guardrail |

## Add New Failures Here

| Date | Failure Mode | What Happened | Fix Added |
|---|---|---|---|
| {today} | None yet | Starter workspace created | None |
"""


def continuous_improvement_log(today: str) -> str:
    return f"""# Continuous Improvement Log

Last updated: {today}

Use this file when the workspace improves because of an eval, correction, repeated failure, or new workflow.

## Operating Rule

The OS should get better because work happened.

```text
failure or new learning -> eval -> failure log -> protocol/template update -> better next run
```

## Entries

| Date | Trigger | Change Made | Why It Matters | Verification |
|---|---|---|---|---|
| {today} | Starter workspace created | Continuous-improvement log initialized | Future changes have a place to be explained | Workspace includes core operating files |
"""


def protocol_change_log(today: str) -> str:
    return f"""# Protocol Change Log

Last updated: {today}

Use this file when a protocol, template, prompt, or operating rule changes.

## Entries

| Date | Trigger | Protocol Or Template Changed | New Rule | Verification |
|---|---|---|---|---|
| {today} | Starter workspace created | Initial protocol set | Meaningful inputs should create artifacts and decision pressure | Starter workspace created |
"""


def automation_registry(today: str) -> str:
    return f"""# Automation Registry

Last updated: {today}

Use this file to track recurring or scheduled agent workflows.

Each automation should have a contract before it runs.

## Automations

| Name | Trigger | Purpose | Allowed Writes | Verification | Status |
|---|---|---|---|---|---|
| None yet |  |  |  |  | Not started |

## Contract Rule

Every automation should define:

- eligible inputs;
- allowed writes;
- prohibited actions;
- deduplication rule;
- inference rule;
- verification;
- reporting rule;
- stop conditions.
"""


def autonomy_control_ledger(today: str) -> str:
    payload = {
        "schema_version": "1.0",
        "last_updated": today,
        "controls": [],
        "required_fields": [
            "control_id",
            "failure_class",
            "repair_class",
            "controlling_surface",
            "blast_radius",
            "change",
            "rollback",
            "positive_test",
            "negative_test",
            "proof_status",
            "observation_window",
        ],
        "proof_statuses": [
            "fixture_pass",
            "live_pass",
            "observation_open",
            "human_gated",
        ],
    }
    return json.dumps(payload, indent=2) + "\n"


def readme(project_name: str) -> str:
    return f"""# {project_name}

This is a Founder Chief of Staff workspace.

The goal is to keep company memory, decision preparation, relationships, execution, research, and operating controls aligned.

## Operating Loop

```text
input -> artifact -> pattern -> decision queue -> experiment -> evidence -> updated context
```

```text
failure -> eval -> failure log -> protocol/template update -> better next run
```

## Start Here

1. Read `00_Context/Current_Decision_Dashboard.md`.
2. Read `00_Context/State_Registry.json`.
3. Read `00_Context/Current_Working_State.md`.
4. Read `00_Context/Operating_Control_Map.md`.
5. Use `00_Context/Daily_Operating_Console.md` for today's execution.
6. Add source material in `07_Source_Material/`.
7. Create or update theme notes in `01_Themes/`.
8. Keep `06_Decision_Log/Active_Decision_Queue.md` current.
9. Keep `00_Context/Project_Artifact_Index.md` current.
10. Use `09_Automation/Automation_Registry.md` for recurring agent workflows.
11. Use `09_Automation/Continuous_Improvement_Log.md` when the OS changes.
12. Use `09_Automation/Autonomy_Control_Ledger.json` for structural repair proof.
13. Use templates from `templates/`.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Founder Chief of Staff starter workspace.")
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
    for agent_file in ("AGENTS.md", "CLAUDE.md", "PROMPT.md"):
        source = repo / agent_file
        destination = target / agent_file
        if source.exists() and not destination.exists():
            shutil.copy2(source, destination)
            created_files.append(destination)
    if write_if_missing(target / "00_Context" / "Current_Decision_Dashboard.md", dashboard(project_name, today)):
        created_files.append(target / "00_Context" / "Current_Decision_Dashboard.md")
    if write_if_missing(target / "00_Context" / "Current_Working_State.md", current_state(project_name, today)):
        created_files.append(target / "00_Context" / "Current_Working_State.md")
    if write_if_missing(target / "00_Context" / "Project_Artifact_Index.md", artifact_index(today)):
        created_files.append(target / "00_Context" / "Project_Artifact_Index.md")
    if write_if_missing(target / "00_Context" / "Operating_Control_Map.md", operating_control_map(today)):
        created_files.append(target / "00_Context" / "Operating_Control_Map.md")
    if write_if_missing(target / "00_Context" / "State_Registry.json", state_registry(today)):
        created_files.append(target / "00_Context" / "State_Registry.json")
    if write_if_missing(target / "00_Context" / "Daily_Operating_Console.md", daily_operating_console(today)):
        created_files.append(target / "00_Context" / "Daily_Operating_Console.md")
    if write_if_missing(target / "06_Decision_Log" / "Active_Decision_Queue.md", decision_queue(today)):
        created_files.append(target / "06_Decision_Log" / "Active_Decision_Queue.md")
    if write_if_missing(target / "09_Automation" / "Automation_Registry.md", automation_registry(today)):
        created_files.append(target / "09_Automation" / "Automation_Registry.md")
    if write_if_missing(target / "09_Automation" / "Failure_Mode_Register.md", failure_mode_register(today)):
        created_files.append(target / "09_Automation" / "Failure_Mode_Register.md")
    if write_if_missing(target / "09_Automation" / "Continuous_Improvement_Log.md", continuous_improvement_log(today)):
        created_files.append(target / "09_Automation" / "Continuous_Improvement_Log.md")
    if write_if_missing(target / "09_Automation" / "Protocol_Change_Log.md", protocol_change_log(today)):
        created_files.append(target / "09_Automation" / "Protocol_Change_Log.md")
    if write_if_missing(target / "09_Automation" / "Autonomy_Control_Ledger.json", autonomy_control_ledger(today)):
        created_files.append(target / "09_Automation" / "Autonomy_Control_Ledger.json")

    copied = copy_templates(repo, target)

    print(f"Created Founder Chief of Staff workspace: {target}")
    print(f"Project name: {project_name}")
    print(f"Directories created: {len(created_dirs)}")
    print(f"Files created: {len(created_files)}")
    print(f"Templates copied: {len(copied)}")
    print("\nStart here:")
    print(f"  {target / '00_Context' / 'Current_Decision_Dashboard.md'}")
    print(f"  {target / '00_Context' / 'Current_Working_State.md'}")
    print(f"  {target / '00_Context' / 'State_Registry.json'}")
    print(f"  {target / '00_Context' / 'Operating_Control_Map.md'}")
    print(f"  {target / '00_Context' / 'Daily_Operating_Console.md'}")
    print(f"  {target / '06_Decision_Log' / 'Active_Decision_Queue.md'}")
    print(f"  {target / '09_Automation' / 'Continuous_Improvement_Log.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
