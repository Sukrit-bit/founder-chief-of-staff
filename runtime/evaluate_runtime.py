#!/usr/bin/env python3
"""Run the fixed public queryable-memory and learning casebook."""

from __future__ import annotations

import json
from pathlib import Path
import tempfile

from pcos_memory import MemoryRuntime, RUNTIME_DIR


CASEBOOK = RUNTIME_DIR / "benchmarks" / "public_casebook.json"


def main() -> int:
    cases = json.loads(CASEBOOK.read_text(encoding="utf-8"))
    findings: list[dict[str, object]] = []
    results: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="pcos-eval-") as directory:
        runtime = MemoryRuntime(Path(directory) / "memory.sqlite3")
        build = runtime.rebuild()

        for case in cases["retrieval_cases"]:
            hits = runtime.search(case["query"], limit=8)
            ids = [hit.source_id for hit in hits]
            top_five = set(ids[:5])
            missing_top = sorted(set(case["required_top_5"]) - top_five)
            missing_any = sorted(set(case["required_any"]) - set(ids))
            passed = not missing_top and not missing_any
            result = {
                "case_id": case["case_id"],
                "kind": "retrieval",
                "passed": passed,
                "source_ids": ids,
                "missing_top_5": missing_top,
                "missing_any": missing_any,
            }
            results.append(result)
            if not passed:
                findings.append(result)

        for case in cases.get("context_budget_cases", []):
            bundle = runtime.context_bundle(case["task"], limit=case.get("limit", 8))
            excerpt_characters = bundle["context_character_count"]
            returned_sources = len(bundle["sources"])
            passed = (
                excerpt_characters <= case["max_excerpt_characters"]
                and returned_sources <= case["max_returned_sources"]
                and set(case.get("required_source_ids", [])).issubset(
                    {item["source_id"] for item in bundle["sources"]}
                )
            )
            result = {
                "case_id": case["case_id"],
                "kind": "context_budget",
                "passed": passed,
                "excerpt_characters": excerpt_characters,
                "max_excerpt_characters": case["max_excerpt_characters"],
                "returned_sources": returned_sources,
                "max_returned_sources": case["max_returned_sources"],
            }
            results.append(result)
            if not passed:
                findings.append(result)

        for case in cases["control_cases"]:
            ids = [control["control_id"] for control in runtime.applicable_controls(case["task"])]
            missing = sorted(set(case["required_controls"]) - set(ids))
            passed = not missing
            result = {
                "case_id": case["case_id"],
                "kind": "control_selection",
                "passed": passed,
                "control_ids": ids,
                "missing": missing,
            }
            results.append(result)
            if not passed:
                findings.append(result)

        for case in cases["candidate_cases"]:
            evaluation = runtime.check_candidate(case["task"], case["candidate"])
            failed = {
                item["control_id"] for item in evaluation["controls_evaluated"] if not item["passed"]
            }
            missing_failed = sorted(set(case["required_failed_controls"]) - failed)
            passed = evaluation["passed"] == case["expected_pass"] and not missing_failed
            result = {
                "case_id": case["case_id"],
                "kind": "candidate_enforcement",
                "passed": passed,
                "expected_pass": case["expected_pass"],
                "actual_pass": evaluation["passed"],
                "failed_controls": sorted(failed),
                "missing_failed_controls": missing_failed,
            }
            results.append(result)
            if not passed:
                findings.append(result)

        selection_coverage = {
            control_id
            for case in cases["control_cases"]
            for control_id in case["required_controls"]
        }
        negative_coverage = {
            control_id
            for case in cases["candidate_cases"]
            if not case["expected_pass"]
            for control_id in case["required_failed_controls"]
        }
        positive_coverage: set[str] = set()
        for case in cases["candidate_cases"]:
            if case["expected_pass"]:
                positive_coverage.update(
                    control["control_id"]
                    for control in runtime.applicable_controls(case["task"])
                )

        active_controls = {
            control["control_id"] for control in runtime.controls if control.get("status") == "active"
        }
        control_health = {
            "case_id": "CONTROL-HEALTH",
            "kind": "control_health",
            "passed": True,
            "missing_selection_cases": sorted(active_controls - selection_coverage),
            "missing_negative_cases": sorted(active_controls - negative_coverage),
            "missing_positive_cases": sorted(active_controls - positive_coverage),
        }
        control_health["passed"] = not any(
            control_health[key]
            for key in ("missing_selection_cases", "missing_negative_cases", "missing_positive_cases")
        )
        results.append(control_health)
        if not control_health["passed"]:
            findings.append(control_health)

    summary = {
        "passed": not findings,
        "cases": len(results),
        "passed_cases": sum(1 for item in results if item["passed"]),
        "failed_cases": len(findings),
        "build": build,
        "findings": findings,
        "results": results,
        "proof_boundary": "Synthetic benchmark evidence only; this is not live behavioral proof.",
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
