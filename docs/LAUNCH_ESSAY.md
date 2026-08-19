# An AI Chief Of Staff Needs Operating Memory, Not A Longer Prompt

The practical promise is simple: a general AI agent should be able to return tomorrow, recover the right context, and help move the work forward without the founder rebuilding the world in every session.

That requires more than storing documents. A context window is not operating memory. Search is not understanding. A failure log is not learning.

Founder Chief of Staff combines canonical operating sources with bounded, relationship-aware retrieval and task-time learning controls. It brings the smallest useful slice of the company into the task, keeps source authority visible, and checks whether earlier failure modes are being repeated before candidate work is released.

Founders do not work in one workflow.

A customer call changes a relationship, a task, a product assumption, and the current company narrative at the same time. A new deadline changes today's plan. A correction may expose a rule that can fail again. Research may affect a roadmap decision, but it is not automatically scope.

Most AI assistants handle the message in front of them. The founder is still left to remember which spreadsheet, document, decision, and follow-up should change.

Founder Chief of Staff is an open-source operating harness for that larger job.

## Chat Is Input, Not Memory

The system gives each kind of state one named owner:

- current focus lives in a decision dashboard;
- continuity lives in current working state;
- unresolved judgment lives in a decision queue;
- relationships and opportunities live in a CRM;
- personal execution lives in a daily console;
- authority and access live in a state registry;
- failures and structural remedies live in control and proof logs.

The agent reads only the current context required for the task. When a material founder event arrives, it identifies every affected system, applies only permitted changes, and reads them back before closing.

Version 0.3.0 makes that selective recovery runnable. Registered sources are compiled into a disposable SQLite full-text index. The agent retrieves bounded excerpts, expands through explicit relationships, and retains provenance. Canonical documents remain authoritative.

## The Founder Keeps Judgment

The agent can capture, reconcile, synthesize, prepare, check, and maintain.

It cannot invent a material fact, deadline, owner, relationship, or outcome. External communication, publication, destructive work, and strategic commitments remain human-gated.

The goal is not to automate the founder. It is to remove the system work surrounding founder judgment.

## Corrections Must Change The System

A self-improving agent cannot merely remember that it was wrong.

When a failure can recur, the system finds the shared control, changes the rule or code, runs a positive test and a negative test, records proof status, and watches the next qualifying events. A clean fixture proves only the tested behavior.

The new runtime also makes the control available at task time and evaluates candidate output against it. Outcomes are recorded as prevented, caught before release, repeated, or not applicable. This is bounded learning, not a claim that the agent autonomously rewrites itself.

## Research Is One Module

Company and market research remain important, but they are one input to the Chief of Staff.

The synthesis layer extracts problems, workflows, capabilities, evidence, limitations, and transfer conditions. It can recommend build, integrate, bundle, compete, monitor, reject, or collect more evidence. A competitor's existence is evidence, never a ceiling.

## What Ships

The repository contains:

- a founder-workspace generator;
- Codex, Claude Code, and portable agent entry points;
- state, routing, execution, automation, and correction contracts;
- synthetic end-to-end examples;
- positive and negative reconciliation evals;
- safety, identity, documentation, and workspace audits;
- a one-command release check.
- a local queryable-memory and candidate-control runtime;
- fixed retrieval, context-budget, control-selection, and enforcement benchmarks.

It contains no private founder data, customer work, relationship records, or credentials.

The bet is straightforward: a general AI agent becomes materially more useful when company state, ownership, boundaries, and verification are explicit.

The public benchmark is synthetic evidence. Live general reliability remains to be proved through repeated operating use.

Style check: external style applied.
