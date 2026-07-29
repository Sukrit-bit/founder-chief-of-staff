#!/usr/bin/env python3
"""Run deterministic positive and negative evals for public agent scenarios."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys


def load_json(path: pathlib.Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def validate(contract: dict, candidate: dict) -> list[str]:
    failures: list[str] = []

    required_systems = set(contract.get("required_systems", []))
    actual_systems = set(candidate.get("systems_updated", []))
    for system in sorted(required_systems - actual_systems):
        failures.append(f"missing_system:{system}")

    expected_states = contract.get("required_states", {})
    actual_states = candidate.get("states", {})
    for field, expected in expected_states.items():
        if actual_states.get(field) != expected:
            failures.append(f"wrong_state:{field}")

    actual_claims = set(candidate.get("claims", []))
    for claim in contract.get("forbidden_claims", []):
        if claim in actual_claims:
            failures.append(f"forbidden_claim:{claim}")

    if not candidate.get("verification"):
        failures.append("missing_verification")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--eval-dir",
        default="evals/founder-event-reconciliation",
        help="Directory containing contract.json and candidate fixtures",
    )
    args = parser.parse_args()

    eval_dir = pathlib.Path(args.eval_dir).resolve()
    contract = load_json(eval_dir / "contract.json")
    valid = load_json(eval_dir / "valid-plan.json")
    invalid = load_json(eval_dir / "invalid-plan.json")

    valid_failures = validate(contract, valid)
    if valid_failures:
        print(f"FAIL: positive fixture rejected: {', '.join(valid_failures)}")
        return 1
    print("PASS: positive fixture reconciles every required system without inference")

    invalid_failures = validate(contract, invalid)
    required_negative_signals = {
        "missing_system:current_state",
        "missing_system:decision_queue",
        "wrong_state:relationship_status",
        "wrong_state:founder_task_status",
        "forbidden_claim:investor_rejected",
        "forbidden_claim:response_date_known",
        "forbidden_claim:outreach_sent",
        "missing_verification",
    }
    missing_signals = sorted(required_negative_signals - set(invalid_failures))
    if missing_signals:
        print(f"FAIL: negative fixture escaped controls: {', '.join(missing_signals)}")
        return 1
    print("PASS: negative fixture is blocked for incomplete routing and invented facts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
