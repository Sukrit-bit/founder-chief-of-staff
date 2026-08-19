# TECHNICAL: Founder Chief of Staff

## Overview

Founder Chief of Staff is a file-native control layer for durable AI-assisted work. Version 0.3.0 adds a queryable-memory and bounded-learning runtime using Python and SQLite FTS5.

Start with [README.md](README.md) and [PRD.md](PRD.md).

## System Model

```text
registered canonical sources + authority metadata
                 |
                 v
       generated SQLite FTS index
                 |
        exact + full-text ranking
                 |
     bounded relationship expansion
                 |
        inspectable context bundle
                 |
      task-applicable controls
                 |
       candidate output checks
                 |
verified canonical update + typed learning outcome
```

## Engineering Decisions

### Canonical files, derived database

`runtime/source_manifest.json` registers sources, authority, status, and relationships. `runtime/memory.sqlite3` is generated and ignored by Git. `rebuild` deletes and recreates the index from the manifest. Search infrastructure therefore cannot silently become a second source of truth.

### Bounded hybrid retrieval without embeddings

Release one combines title and metadata signals, SQLite FTS5 ranking, and explicit relationship traversal. Context creation reports returned sources and character count. Limits are part of the interface, not a prompt suggestion.

Embeddings and an external graph database are deferred. They should be added only when a measured retrieval failure cannot be resolved through better source structure, vocabulary, or explicit relationships.

### Control selection before candidate enforcement

`runtime/control_registry.json` holds machine-testable controls with task triggers and candidate requirements or prohibitions. The runtime first determines which controls apply to the task, then checks the candidate only against that subset. This avoids treating every historical failure as relevant to every task.

### Typed learning evidence

`runtime/learning_events.json` records outcomes such as `prevented`, `caught_before_release`, `repeated`, and `not_applicable`. A log entry is evidence about the control, not permission for the system to rewrite its own policy.

### Explicit proof classes

The public release distinguishes structural evidence, synthetic evidence, and live evidence. The included evaluator provides structural and synthetic evidence only.

## Runtime Components

| Component | Responsibility |
|---|---|
| `source_manifest.json` | Registered sources, authority, status, relationships |
| `pcos_memory.py` | Parsing, indexing, retrieval, context assembly, controls |
| `cli.py` | Rebuild, search, context, control, candidate, and status commands |
| `control_registry.json` | Task triggers and candidate enforcement rules |
| `learning_events.json` | Typed observed outcomes |
| `benchmarks/public_casebook.json` | Fixed synthetic evaluation contract |
| `evaluate_runtime.py` | Retrieval, budget, control, and candidate evaluation |

## Commands

```bash
python3 runtime/cli.py rebuild
python3 runtime/cli.py search "operating memory"
python3 runtime/cli.py context "Prepare work after a repeated failure"
python3 runtime/cli.py controls "A correction was repeated"
python3 runtime/cli.py candidate "A correction was repeated" "The failure was logged, so it is learned."
python3 runtime/evaluate_runtime.py
```

## Evaluation Architecture

The release audit combines six gates: claim and migration contract; repository-wide narrative consistency; claim-to-evidence consistency; runnable retrieval, budget, control, and candidate cases; generated workspace, safety, identity, and link integrity; and visual plus cold-reader review evidence.

`python3 scripts/release_audit.py` is the single release command. A partial pass is not a release pass.

## Failure Handling

- Missing registered file: rebuild fails visibly.
- Invalid JSON or schema: command fails rather than ignoring the record.
- No retrieval match: return an empty or limited bundle; do not invent context.
- Candidate violates a selected control: return the failed control and message.
- Over-broad control: update trigger and add positive and negative regression cases.
- Stale derived index: run `rebuild`; do not edit the database directly.

## Security and Data Boundary

The public manifest includes only public repository files and synthetic fixtures. Common credential, secret, environment, and Git paths are excluded. This is a local reference implementation, not a tenant-isolated hosted service.

## Extensibility

Future adapters can ingest Docs, Sheets, Gmail, Calendar, or project systems into registered canonical sources. They should preserve authority, provenance, access boundaries, rebuildability, and proof classification. Connector availability alone is not a reason to ingest a source.

## Result

The architecture makes operating memory queryable without loading the entire workspace, and makes prior failures executable without claiming that an agent has autonomously learned merely because a note exists.
