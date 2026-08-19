# An AI Chief Of Staff Needs Operating Memory, Not A Longer Prompt

A useful AI partner should be able to return tomorrow, recover the right context and keep the work moving. The founder should not have to rebuild the company inside every new chat.

That takes more than stored documents. A context window is not operating memory. Search is not understanding. A failure log is not learning.

Founder Chief of Staff is an open-source system for that larger job.

## Founders Do Not Work In One Thread

A customer call can change a relationship, a task, a product assumption and the company story at the same time. A deadline can change today's priorities. A correction can expose a rule that matters again next week.

Most AI assistants handle the message in front of them. The founder still has to remember which document, spreadsheet, decision and follow-up should change.

This project gives each kind of information one clear owner. Current focus belongs in the dashboard. Decisions belong in the decision queue. Relationships belong in the relationship system. Personal work belongs in the daily console. Failures and their remedies belong in the learning record.

The agent finds only the sources needed for the current task. It keeps their status and ownership visible. After verified work, it updates the systems that actually own the information.

## Memory Must Be Easy To Use

Files alone do not solve the problem. The agent must be able to find the right passage quickly without rereading the whole workspace.

The release builds a disposable SQLite search index from approved Markdown and JSON files. The original files remain the source of truth. The index returns a small set of excerpts and follows only declared relationships between them.

This saves context while keeping the reasoning inspectable.

## Corrections Must Change The Next Task

Writing a mistake into a register does not mean the system has learned.

When a failure can recur, it must become a rule. That rule needs a clear task trigger. It must be tested against bad and good examples. It must also enter the next relevant task before the work is released.

The system records whether the rule prevented the mistake, caught it before release, failed again or did not apply. This is a controlled learning loop. It is not a claim that the agent rewrites itself freely.

Version 0.3.1 applies that principle to the repository itself. The previous release had an external-writing standard, but the standard was not part of task-time retrieval or the release audit. Accurate but difficult public copy passed. The new release registers the rule, tests it and blocks publication when the public front door fails the reader check.

## The Founder Keeps Judgment

The agent can capture, reconcile, prepare, check and maintain. It cannot invent a material fact, deadline, owner, relationship or outcome.

The founder still owns judgment, risk, relationships and final calls. The purpose of the system is to remove the operating work around those decisions.

## What Ships

The repository includes:

- a founder-workspace generator;
- entry points for Codex, Claude Code and other agents;
- a local search and context runtime;
- task-specific failure rules;
- positive and negative test cases;
- a public-writing release gate;
- synthetic examples;
- one complete release command.

It contains no private founder data, customer work, live relationship records or credentials.

The fixed tests show that the declared mechanisms work on their fixtures. General live reliability still needs to be earned through repeated use.

The bet is simple: an AI agent becomes far more useful when it can recover the right company context, keep work connected and apply earlier lessons before the same mistake escapes again.
