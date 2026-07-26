#!/usr/bin/env python3
"""Validate a generated Founder Chief of Staff workspace."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "PROMPT.md",
    "00_Context/Current_Decision_Dashboard.md",
    "00_Context/Current_Working_State.md",
    "00_Context/Project_Artifact_Index.md",
    "00_Context/Operating_Control_Map.md",
    "00_Context/State_Registry.json",
    "00_Context/Daily_Operating_Console.md",
    "06_Decision_Log/Active_Decision_Queue.md",
    "09_Automation/Automation_Registry.md",
    "09_Automation/Failure_Mode_Register.md",
    "09_Automation/Continuous_Improvement_Log.md",
    "09_Automation/Protocol_Change_Log.md",
    "09_Automation/Autonomy_Control_Ledger.json",
]

REQUIRED_CONTROL_FIELDS = {
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
}


def load_json(path: pathlib.Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", help="Generated workspace path")
    args = parser.parse_args()

    workspace = pathlib.Path(args.workspace).expanduser().resolve()
    failures: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (workspace / relative).exists():
            failures.append(f"missing required path: {relative}")

    registry_path = workspace / "00_Context" / "State_Registry.json"
    if registry_path.exists():
        try:
            registry = load_json(registry_path)
            systems = registry.get("systems")
            if not isinstance(systems, list) or not systems:
                failures.append("state registry must contain at least one system")
            else:
                for system in systems:
                    if not isinstance(system, dict):
                        failures.append("state registry system entries must be objects")
                        continue
                    for field in ("id", "purpose", "location", "authority", "access", "status"):
                        if not system.get(field):
                            failures.append(f"state registry entry missing field: {field}")
                    location = system.get("location")
                    if location and not (workspace / location).exists():
                        failures.append(f"state registry target does not exist: {location}")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            failures.append(f"invalid state registry: {exc}")

    ledger_path = workspace / "09_Automation" / "Autonomy_Control_Ledger.json"
    if ledger_path.exists():
        try:
            ledger = load_json(ledger_path)
            actual = set(ledger.get("required_fields", []))
            missing = sorted(REQUIRED_CONTROL_FIELDS - actual)
            if missing:
                failures.append(f"control ledger missing required fields: {', '.join(missing)}")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            failures.append(f"invalid control ledger: {exc}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: workspace controls are valid at {workspace}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
