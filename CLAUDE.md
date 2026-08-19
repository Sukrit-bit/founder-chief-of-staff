# Claude Code Instructions

This workspace uses Claude Code as a founder-operations agent, not only as a coding agent.

Read `AGENTS.md` first. In this public template repository, continue with `docs/OPERATING_CONTROL_MAP.md`. In a generated founder workspace, continue with `00_Context/Operating_Control_Map.md` and `00_Context/State_Registry.json`.

Follow the same canonical-state, reconciliation, evidence, correction, automation, and privacy contracts defined in `AGENTS.md`. Use `PROMPT.md` for the full portable specification.

Use the queryable-memory runtime when present. Retrieve bounded source-aware context, treat SQLite as derived, apply relevant failure controls before release, and keep synthetic benchmark evidence distinct from live proof.

For external writing, read `docs/EXTERNAL_WRITING_STANDARD.md` and run `python3 scripts/external_style_audit.py` before release. A narrative or style label does not prove readability.

For GitHub publication, create the GitHub Release after pushing the tag and run `scripts/post_publish_audit.py`. A pushed tag alone is not a published release.

When implementation happens in a separate product repository, consume a narrow implementation handoff. Do not infer product scope from private founder notes or broad research folders.
