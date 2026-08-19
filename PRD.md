# PRD: Founder Chief of Staff

## The Problem

Founders work across product, customers, hiring, fundraising, partnerships, research, and execution. The record is spread across documents, spreadsheets, repositories, messages, and meetings. General AI agents can help with individual tasks, but their usefulness collapses when they cannot recover what matters across time.

The failure has three layers:

1. Important facts may exist, but the agent cannot tell which source is authoritative.
2. Search can return text, but not necessarily the smallest useful context or the relationships that explain it.
3. Corrections can be logged, but remain passive and fail to change the next same-class task.

The founder repeatedly restates context, stale claims resurface, token use grows, and “learning” becomes a list of mistakes rather than improved behavior.

## The Core Insight

The useful unit is not a conversation. It is a durable founder-agent operating relationship.

That relationship requires both queryable operating memory—canonical sources, explicit authority, relationships, and bounded retrieval—and bounded learning—failures converted into applicable controls, pre-release checks, and same-class evidence.

Memory without retrieval becomes an archive. Retrieval without authority becomes plausible noise. A failure registry without enforcement does not improve behavior.

## User and Job

The primary user is a founder who wants an AI agent to carry meaningful work forward without surrendering judgment or repeatedly re-explaining the company.

> Recover the right operating context, help move the work forward, preserve what changed, and make an earlier correction relevant before the same mistake escapes again.

## The Product Contract

For a material task, the system should:

1. identify the canonical sources and their authority;
2. retrieve a bounded set of relevant passages;
3. expand only through explicit useful relationships;
4. surface contradictions and uncertainty rather than blending them away;
5. select failure controls applicable to this task;
6. evaluate candidate work before release;
7. write verified changes back to the owning operating sources;
8. record whether a control prevented, caught, repeated, or did not apply.

## Release-One Scope

Version 0.3.0 delivers a public, local reference implementation:

- JSON source and relationship registry;
- Markdown/JSON ingestion into a derived SQLite FTS index;
- bounded retrieval with provenance and context-size reporting;
- task-time control selection;
- candidate-output enforcement;
- typed learning-event records;
- fixed synthetic evaluation cases and a one-command release audit.

It sits beneath the existing founder workspace. Dashboard, working state, decision queue, research and capability records, relationship systems, daily plan, automation contracts, and improvement records remain canonical operating surfaces.

## Key Decisions

### Start with an inspectable local architecture

SQLite FTS and explicit graph edges are sufficient to validate authority-aware retrieval and bounded learning. A vector database, external graph store, and managed orchestration layer are deferred until observed retrieval failures justify them.

### Keep canonical and derived state separate

The index can always be rebuilt. It never silently becomes the authority.

### Make proof boundaries visible

The public evaluator proves behavior only on its declared synthetic casebook. Live longitudinal improvement requires operating evidence across repeated real tasks and remains unproved here.

### Preserve founder judgment

The system can prepare decisions, enforce controls, and maintain low-risk internal state. External publication, consequential commitments, and unsupported strategy remain human-gated.

## The Output

A successful release produces:

- a compact context bundle rather than a workspace dump;
- source IDs, authority, and relationships for inspection;
- applicable controls before the answer is released;
- a pass/fail candidate evaluation with reasons;
- learning evidence that can be queried later;
- an operating update that survives the chat session.

## Success Measures

Release-one measures are deterministic: expected authoritative sources rank correctly; context stays within a declared budget; expected controls are selected; unsafe candidates fail and bounded candidates pass; public claims, links, generated workspace checks, and safety checks pass together.

Future live measures include reduced founder restatement, fewer repeated same-class failures, lower context cost for equivalent work, and higher successful carry-forward across sessions. These are target outcomes, not current public claims.

## Edge Cases

- Two sources disagree: preserve both and require clarification.
- A source is historical: retrieve it only with historical status intact.
- A failure control fires too broadly: narrow its trigger and add a regression case.
- No relevant source exists: say so; do not fill the gap from chat confidence.
- A task needs private data: keep private sources outside the public corpus.
- A benchmark passes: report synthetic evidence, not general reliability.

## Architecture

See [TECHNICAL.md](TECHNICAL.md). The causal chain is source registry → derived index → bounded context → applicable controls → candidate enforcement → verified operating update → typed learning evidence.

## What's Next

After real-task evidence identifies clear gaps: relationship-aware ranking improvements, richer contradiction handling, incremental rebuilds, optional embeddings, connector ingestion, and proof-window reporting. None should precede evidence that release one is insufficient.

## How It Was Built

The release was migrated through an explicit claim contract and six-gate audit covering narrative consistency, evidence boundaries, runnable behavior, safety and links, visuals, and cold-reader comprehension. See [docs/EVALS.md](docs/EVALS.md) and [docs/releases/v0.3.0-evaluation.md](docs/releases/v0.3.0-evaluation.md).
