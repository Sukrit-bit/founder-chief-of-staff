#!/usr/bin/env python3
"""Run the complete public-release verification suite."""

from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    print(f"\n$ {' '.join(args)}")
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    run(sys.executable, "scripts/doc_audit.py", "--repo", ".", "--strict")
    run(sys.executable, "scripts/repo_safety_check.py", "--repo", ".")
    run(sys.executable, "scripts/eval_scenarios.py")

    with tempfile.TemporaryDirectory(prefix="founder-chief-of-staff-") as temp_dir:
        workspace = pathlib.Path(temp_dir) / "workspace"
        run(sys.executable, "scripts/init_workspace.py", str(workspace))
        run(sys.executable, "scripts/workspace_audit.py", str(workspace))

    print("\nPASS: public release checks completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
