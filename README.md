# Founder Chief of Staff

Turn a general AI agent into a durable operating partner—one that can recover the right context efficiently, carry work forward, and use previous failures to improve future work.

![Founder Chief of Staff social card](assets/social-card.svg)

## Why This Exists

Founders do not need another assistant that starts from zero in every session. They need work to survive context windows, decisions to remain connected to evidence, and corrections to change what happens next.

> A context window is not operating memory. Search is not understanding. A failure log is not learning.

Founder Chief of Staff combines a canonical operating record with selective, relationship-aware retrieval and enforceable learning controls. The result is a smaller, better context bundle for the task at hand—and a system that can test whether an earlier mistake is being repeated before an answer is released.

## What Is Shipped

Version 0.3.0 adds a runnable public reference implementation for:

- registering authoritative sources and their relationships;
- compiling them into a local SQLite full-text index;
- retrieving a bounded context bundle with source provenance;
- selecting controls relevant to the current task;
- checking candidate output before release;
- recording learning outcomes without claiming live improvement prematurely;
- evaluating retrieval, context budget, control selection, and candidate enforcement with fixed synthetic cases.

The repository also includes the founder operating workspace generator, state and automation contracts, Codex and Claude Code entry points, and synthetic end-to-end examples.

It does **not** include a hosted agent, private founder data, vector retrieval, a graph database, Gmail or Calendar ingestion, or self-modifying policy. The included benchmark is synthetic evidence, not proof of general live reliability.

## Try It

```bash
python3 runtime/cli.py rebuild
python3 runtime/cli.py context "How should a repeated failure change the next answer?"
python3 runtime/evaluate_runtime.py
python3 scripts/release_audit.py
```

To generate the broader operating workspace:

```bash
python3 scripts/init_workspace.py my-founder-os
python3 scripts/workspace_audit.py my-founder-os
```

## What It Does

```text
authoritative operating sources
        ↓
bounded retrieval + explicit relationships
        ↓
task context + applicable controls
        ↓
decision support or candidate work
        ↓
pre-release enforcement + verified updates
        ↓
learning evidence for the next same-class task
```

This is how memory becomes useful work. The system does not load the entire workspace or trust the latest chat. It finds the smallest useful slice, preserves source authority and uncertainty, and brings relevant failure controls into the task itself.

## Product Decisions

### Canonical sources remain the authority

The SQLite database is a derived index, not a new source of truth. Rebuild it from registered files whenever canonical sources change.

### Retrieval is bounded and inspectable

Release one uses exact-title signals, SQLite full-text search, relationship expansion, and explicit limits. Every returned excerpt retains its source ID and authority metadata. Vector search may become useful later; it is not necessary to validate the product contract now.

### Learning must alter task-time behavior

A failure is not considered learned because it was written down. It must become an applicable control, be evaluated against candidate work, and accumulate same-class evidence such as `prevented`, `caught_before_release`, `repeated`, or `not_applicable`.

### Proof language is part of the product

Structural capability, synthetic benchmark evidence, and live operating evidence are kept separate. A green benchmark shows that the public mechanism works on fixed cases. It does not prove that every future agent response will be correct.

## Documentation

- [PRD.md](PRD.md) — product problem, user contract, release scope, and outcomes.
- [TECHNICAL.md](TECHNICAL.md) — source registry, derived index, retrieval, controls, and evaluation architecture.
- [runtime/README.md](runtime/README.md) — runnable commands and proof boundary.
- [docs/MEMORY_AND_SYNTHESIS.md](docs/MEMORY_AND_SYNTHESIS.md) — canonical memory and selective retrieval.
- [docs/CONTINUOUS_IMPROVEMENT_LOOP.md](docs/CONTINUOUS_IMPROVEMENT_LOOP.md) — bounded learning from correction to evidence.
- [docs/PROOF_OF_OPERATION.md](docs/PROOF_OF_OPERATION.md) — claim-to-evidence map.
- [docs/EVALS.md](docs/EVALS.md) — release evaluation strategy.
- [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md), and [PROMPT.md](PROMPT.md) — agent entry points.
- [Live landing page](https://sukrit-bit.github.io/founder-chief-of-staff/) — public front door.

## Daily Rhythm

The generated workspace supports company state, decisions, capability intelligence, relationships, daily execution, automations, and continuous improvement. The new runtime is the retrieval and learning layer underneath those jobs; it is not a replacement for their canonical artifacts.

## Architecture

The public implementation is deliberately file-native and local-first: Markdown and JSON sources, a generated SQLite index, Python standard-library tooling, deterministic fixtures, and no external service requirement.

See [TECHNICAL.md](TECHNICAL.md) and the [v0.3.0 evaluation report](docs/releases/v0.3.0-evaluation.md).

## Result

An agent can recover the right operating context without rereading the whole workspace and can use prior corrections as task-time controls rather than passive reminders.

## Install

Clone the repository and run the commands above with Python 3. No package install is required.

## Built With

Python, SQLite FTS5, Markdown, JSON, HTML, and deterministic release checks.

## License

[MIT](LICENSE)
