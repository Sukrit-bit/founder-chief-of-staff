#!/usr/bin/env python3
"""Command-line interface for Founder Chief of Staff queryable memory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from pcos_memory import MemoryError, MemoryRuntime, format_hits


def emit(value, as_json: bool) -> None:
    if as_json:
        print(json.dumps(value, indent=2, ensure_ascii=False))
    else:
        print(value)


def main() -> int:
    parser = argparse.ArgumentParser(description="Canonical memory and bounded-learning runtime")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("rebuild", help="Rebuild the derived SQLite index")
    sub.add_parser("drift", help="Report source/index drift")

    query = sub.add_parser("query", help="Retrieve source-backed context")
    query.add_argument("query")
    query.add_argument("--limit", type=int, default=8)
    query.add_argument("--family")
    query.add_argument("--portfolio")
    query.add_argument("--json", action="store_true")

    context = sub.add_parser("context", help="Build a task context and control bundle")
    context.add_argument("task")
    context.add_argument("--limit", type=int, default=8)
    context.add_argument("--json", action="store_true")

    check = sub.add_parser("check-candidate", help="Apply relevant deterministic controls")
    check.add_argument("--task", required=True)
    candidate = check.add_mutually_exclusive_group(required=True)
    candidate.add_argument("--candidate")
    candidate.add_argument("--candidate-file", type=Path)
    check.add_argument("--json", action="store_true")

    record = sub.add_parser("record-outcome", help="Record a typed control outcome")
    record.add_argument("--event-id", required=True)
    record.add_argument("--task-id", required=True)
    record.add_argument("--control-id", required=True)
    record.add_argument("--outcome", required=True)
    record.add_argument("--evidence", required=True)
    record.add_argument("--correction-chain-id")

    args = parser.parse_args()
    try:
        runtime = MemoryRuntime()
        if args.command == "rebuild":
            emit(runtime.rebuild(), True)
        elif args.command == "drift":
            drift = runtime.drift()
            emit({"passed": not drift, "findings": drift}, True)
            return 0 if not drift else 1
        elif args.command == "query":
            hits = runtime.search(
                args.query, limit=args.limit, family=args.family, portfolio=args.portfolio
            )
            emit([hit.as_dict() for hit in hits] if args.json else format_hits(hits), args.json)
        elif args.command == "context":
            bundle = runtime.context_bundle(args.task, limit=args.limit)
            if args.json:
                emit(bundle, True)
            else:
                print(format_hits([runtime_hit(item) for item in bundle["sources"]]))
                print("\nApplicable controls:")
                for control in bundle["applicable_controls"]:
                    print(f"- {control['control_id']}: {control['title']} [{control['risk_tier']}]")
                print("\nImplicated systems: " + ", ".join(bundle["implicated_systems"]))
        elif args.command == "check-candidate":
            candidate_text = args.candidate
            if args.candidate_file:
                candidate_text = args.candidate_file.read_text(encoding="utf-8")
            result = runtime.check_candidate(args.task, candidate_text)
            emit(result, args.json or True)
            return 0 if result["passed"] else 1
        elif args.command == "record-outcome":
            event = runtime.record_outcome(
                event_id=args.event_id,
                task_id=args.task_id,
                control_id=args.control_id,
                outcome=args.outcome,
                evidence=args.evidence,
                correction_chain_id=args.correction_chain_id,
            )
            emit(event, True)
        return 0
    except (MemoryError, OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2


def runtime_hit(item):
    from pcos_memory import SearchHit
    return SearchHit(**item)


if __name__ == "__main__":
    sys.exit(main())
