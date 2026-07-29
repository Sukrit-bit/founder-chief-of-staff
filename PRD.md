# PRD: Founder Chief of Staff

## The Problem

An early-stage founder works across product, customers, hiring, fundraising, partnerships, research, and daily execution. Important facts arrive through calls, messages, documents, spreadsheets, and half-formed thoughts.

General AI assistants can help with each task, but they usually fail at the longer job:

- carrying authoritative state across weeks;
- knowing which document owns which fact;
- reconciling one update across every affected system;
- separating evidence from conviction;
- turning company research into product choices;
- connecting relationship follow-ups to daily work;
- learning structurally from a correction.

The result is repeated explanation, stale priorities, contradictory documents, and an agent that sounds informed without reliably running the founder's operating system.

## The Core Insight

The useful unit is not a conversation. It is a founder-agent operating relationship with inspectable state, clear ownership, bounded autonomy, and verification.

The founder owns judgment, taste, relationships, risk, and final calls. The agent owns capture, reconciliation, synthesis, cross-references, decision preparation, daily planning, checks, and system maintenance.

```text
founder event
-> canonical reconciliation
-> decision and execution effects
-> verified writes
-> concise founder view
```

When the system fails:

```text
signal
-> failure classification
-> blast-radius check
-> structural remedy
-> positive and negative tests
-> proof window
```

## Key Decisions

### 1. Use canonical state, not chat memory

Chat context is useful but not authoritative. The workspace keeps a registry of current sources of truth, their owners, update triggers, and access boundaries.

### 2. Route state by job

Current focus, full continuity, decisions, relationships, personal execution, research evidence, and automation controls have different owners. The operating control map defines the route and prevents a single memory document from becoming a dump.

### 3. Reconcile events across systems

A material founder update can change a relationship, a task, a decision, and current state at once. The agent identifies every implicated canonical system before it replies.

### 4. Prepare decisions without taking them

The system turns evidence into options, assumptions, tradeoffs, and next tests. It does not silently promote a hypothesis, assign ownership, invent a deadline, or make a founder-level strategic call.

### 5. Turn market research into capability intelligence

Company analysis is decomposed into the problem solved, user, workflow, capability, proof, limitation, and transfer conditions. The result can inform build, integrate, bundle, compete, monitor, or reject decisions. Competitor presence is evidence, never a ceiling.

### 6. Keep CRM and personal execution distinct

The relationship system owns people, organizations, opportunities, interactions, and introductions. The personal console owns the founder's tasks. CRM actions can flow into the console as suggestions; v0 has no automatic writeback.

### 7. Contract every recurring automation

Scheduled work must specify eligible inputs, allowed writes, prohibited actions, inference rules, deduplication, stop conditions, verification, and reporting behavior.

### 8. Treat corrections as system failures when warranted

A local answer correction is enough only for a local mistake. A recurring or high-risk failure must change the controlling prompt, protocol, schema, test, or code path and stay under a proof window.

### 9. Hand implementation context to coding agents narrowly

A coding agent receives product intent, current decisions, constraints, non-goals, acceptance checks, and source links through an implementation handoff. It does not need confidential founder or customer context.

### 10. Ship synthetic examples

The public repository demonstrates the method without exposing private research, company strategy, customer work, credentials, or live relationships.

## The Output

A founder gets:

- a current decision dashboard;
- a canonical working state;
- a source-of-truth registry;
- a compact artifact index and control map;
- evidence and capability records;
- an active decision queue;
- a relationship CRM contract;
- a personal daily operating console;
- bounded automation contracts;
- failure, protocol-change, and proof logs;
- implementation handoffs for separate coding agents;
- audits for documentation, workspace integrity, and public safety.

## Architecture

The system is file-native at its control layer:

```text
00_Context          current state, registry, routing, navigation
01_Themes           patterns and capability intelligence
03_Problem_Statements
04_Venture_Theses
05_Experiments
06_Decision_Log
07_Source_Material
08_Execution        CRM and personal-console contracts or exports
09_Automation       contracts, failures, protocol changes, proof
templates
```

Live operational data may sit in Sheets or databases. The control layer records which external system is authoritative and what the agent may read or write.

See [TECHNICAL.md](TECHNICAL.md) for implementation details.

## Edge Cases

- If sources conflict, record the contradiction and stop the affected closure.
- If evidence is weak, lower the maturity label instead of improving the prose.
- If a deadline or owner is missing, create a clarification need instead of inferring it.
- If a CRM action is already a task, update or link it instead of creating a duplicate.
- If a correction affects a class of behavior, inspect every route that can reproduce it.
- If an automation has no eligible input, make no writes and produce no noisy report.
- If a product build needs context, create a narrow handoff instead of exposing the whole workspace.
- If a public artifact depends on private proof, replace it with a synthetic example or a bounded claim.

## Results

The system is working when:

- a founder can resume without reconstructing prior chats;
- material updates reach every affected canonical surface;
- decisions show their evidence and remaining assumptions;
- CRM and daily execution remain linked without source-of-truth confusion;
- repeated mistakes produce tested controls;
- an external reader can understand the framework without private context.

## What's Next

- Test the generated workspace with founders other than its creator.
- Measure duplicate reduction, stale-state detection, and time-to-daily-plan.
- Add connector-specific adapters without weakening the canonical-state contract.
- Publish more synthetic proof cases for corrections, contradictions, and capability synthesis.

## How It Was Built

The framework expanded through sustained use from decision support into a broader Founder Chief of Staff. The design decisions come from real operating failures: stale state, superficial corrections, inflated evidence, duplicated trackers, and context handed to the wrong agent.

Style check: external style applied.
