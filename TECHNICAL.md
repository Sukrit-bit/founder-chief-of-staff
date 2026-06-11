# TECHNICAL: Founder Research OS

## Overview

Founder Research OS is a file-native operating system for AI-assisted startup research.

The audience for this document is a builder who wants to understand the mechanics and tradeoffs behind the framework.

For product framing, start with [README.md](README.md) and [PRD.md](PRD.md).

## Engineering Decisions

### Decision 1: File-native state over chat-native state

Problem: chat is a weak memory substrate for multi-week founder research.

Attempt: rely on conversation continuity and summaries.

Learning: important distinctions get lost. Current focus gets mistaken for project identity. Session-end workflows can fire at the wrong time.

Decision: make state explicit in files:

- dashboard for current operating state;
- working state for full continuity;
- artifact index for navigation;
- decision queue for judgment pressure;
- evals and reviews for quality control.

Tradeoff: more files. Better auditability.

### Decision 2: Protocols before automation

Problem: automation without rules creates confident drift.

Attempt: let the agent infer what to update.

Learning: inference works until scope changes. Then the agent may update the wrong layer.

Decision: encode protocols first:

- agent contract;
- abstraction guardrails;
- evidence maturity ladder;
- artifact lifecycle;
- data-handling rules;
- session handoff rules;
- failure-mode register.

Tradeoff: more upfront structure. Better repeatability.

### Decision 3: Evals as operating artifacts

Problem: a research system can feel smart while making weak decisions.

Attempt: review outputs informally.

Learning: informal review catches prose problems but misses structural problems.

Decision: keep evals as first-class artifacts. Evals should produce remediation items, not just scores.

Tradeoff: more friction after major work. Better learning rate.

### Decision 4: Synthetic examples instead of real research examples

Problem: real founder research contains names, decisions, market context, and access paths that distract from the reusable method.

Attempt: remove names and publish a cleaned-up research trail.

Learning: cleanup is not enough. The framework needs examples designed for teaching.

Decision: ship the framework with synthetic examples.

Tradeoff: less emotional specificity. Cleaner adoption path.

## System Characteristics

Current framework:

- 4 root docs: README, PRD, TECHNICAL, PROMPT.
- 8 protocol docs.
- 8 reusable templates.
- 1 synthetic example loop.
- 1 visual explainer.
- 2 audit scripts: documentation quality and repo safety.
- 1 GitHub Actions workflow.

The system is optimized for judgment quality, not low-latency interaction.

Recommended thresholds:

- Every strategic artifact should have scope, maturity, parent, children, decision status, and next evidence.
- Every active hypothesis should have a decision queue row.
- Every repeated operating failure should update the failure-mode register.
- Every shared repo should pass the data-handling checklist.
- Every meaningful milestone should run the docs audit.
- Every shared repo should run the repo safety check.

## What Surprised Us

The hard part was not creating folders.

The hard part was preventing useful research from becoming a giant memory file. The dashboard/index/state split became necessary once the working state started carrying too many jobs.

The second surprise was that autonomy needs friction. The agent should act without waiting on routine maintenance, but it still needs bright lines around evidence quality, sensitive material, and session boundaries.

## Closing

Founder Research OS is not a note-taking template.

It is a decision system for founders working with AI agents. The core technical idea is simple: put the agent inside a workspace where state, evidence, protocols, evals, and failure modes are all inspectable files.
