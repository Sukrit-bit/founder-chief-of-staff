#!/usr/bin/env python3
"""Verify that a pushed tag is also visible as the latest GitHub Release."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class PublicationState:
    expected_commit: str
    local_tag_commit: str
    remote_tag_commit: str
    release_tag: str | None
    release_draft: bool | None
    release_prerelease: bool | None
    latest_tag: str | None


def failures_for(state: PublicationState, tag: str) -> list[str]:
    failures: list[str] = []
    if state.local_tag_commit != state.expected_commit:
        failures.append("local tag does not resolve to the expected commit")
    if state.remote_tag_commit != state.expected_commit:
        failures.append("remote tag does not resolve to the expected commit")
    if state.release_tag != tag:
        failures.append("GitHub Release object is missing or points to another tag")
    if state.release_draft:
        failures.append("GitHub Release is still a draft")
    if state.release_prerelease:
        failures.append("GitHub Release is marked as a prerelease")
    if state.latest_tag != tag:
        failures.append("GitHub does not expose this tag as the latest release")
    return failures


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def remote_tag_commit(tag: str) -> str:
    output = run("git", "ls-remote", "origin", f"refs/tags/{tag}^{{}}", f"refs/tags/{tag}")
    rows = [line.split() for line in output.splitlines() if line.strip()]
    peeled = next((sha for sha, ref in rows if ref.endswith("^{}")), None)
    direct = next((sha for sha, ref in rows if ref == f"refs/tags/{tag}"), None)
    if not peeled and not direct:
        raise RuntimeError(f"remote tag not found: {tag}")
    return peeled or direct or ""


def live_state(repo: str, tag: str, expected_commit: str) -> PublicationState:
    local = run("git", "rev-list", "-n", "1", tag)
    release = json.loads(
        run(
            "gh",
            "release",
            "view",
            tag,
            "--repo",
            repo,
            "--json",
            "tagName,isDraft,isPrerelease",
        )
    )
    latest = json.loads(run("gh", "api", f"repos/{repo}/releases/latest"))
    return PublicationState(
        expected_commit=expected_commit,
        local_tag_commit=local,
        remote_tag_commit=remote_tag_commit(tag),
        release_tag=release.get("tagName"),
        release_draft=release.get("isDraft"),
        release_prerelease=release.get("isPrerelease"),
        latest_tag=latest.get("tag_name"),
    )


def self_test() -> int:
    good = PublicationState("abc", "abc", "abc", "v1", False, False, "v1")
    bad = PublicationState("abc", "abc", "abc", None, None, None, "v0")
    if failures_for(good, "v1"):
        print("FAIL: positive publication fixture was rejected")
        return 1
    bad_failures = failures_for(bad, "v1")
    required = {
        "GitHub Release object is missing or points to another tag",
        "GitHub does not expose this tag as the latest release",
    }
    if not required.issubset(set(bad_failures)):
        print("FAIL: negative fixture did not reproduce the missing-release failure")
        return 1
    print("PASS: post-publication evaluator accepts a complete release and rejects a tag-only publication")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", help="GitHub owner/repository")
    parser.add_argument("--tag", help="Release tag")
    parser.add_argument("--expected-commit", help="Full expected commit SHA")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.repo or not args.tag:
        parser.error("--repo and --tag are required unless --self-test is used")

    expected = args.expected_commit or run("git", "rev-list", "-n", "1", args.tag)
    try:
        state = live_state(args.repo, args.tag, expected)
    except (subprocess.CalledProcessError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"FAIL: could not verify published release: {exc}")
        return 1

    failures = failures_for(state, args.tag)
    if failures:
        print("FAIL: GitHub publication is incomplete")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "PASS: commit, local tag, remote tag, GitHub Release object and latest-release state agree "
        f"for {args.tag} ({expected})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
