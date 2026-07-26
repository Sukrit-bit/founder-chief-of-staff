# Automation Contracts

## Purpose

Recurring agent work should have a contract before it runs.

Without a contract, automation becomes confident drift.

An automation contract defines:

- when the agent runs;
- what it is allowed to read;
- what it is allowed to write;
- what it must not infer;
- when it must stop;
- how it verifies the result;
- what it reports.

## Contract Fields

| Field | Meaning |
|---|---|
| Name | Human-readable automation name |
| Schedule / Trigger | Time, event, or manual trigger |
| Purpose | The job in one sentence |
| Inputs | Files, sheets, folders, or sources the agent may read |
| Eligible Records | The exact rows, files, or states that can be processed |
| Allowed Writes | The exact destinations the agent may update |
| Prohibited Actions | Actions that require human approval |
| Deduplication Rule | How the agent avoids creating duplicate records |
| Inference Rule | What can be inferred and what must become a clarification item |
| Verification | How success is checked |
| Reporting Rule | What the founder should see, including no-report conditions |
| Failure / Stop Conditions | When the automation must stop instead of guessing |

## Good Automation Behavior

A good automation:

- processes only eligible inputs;
- preserves raw captures;
- checks canonical records before creating new ones;
- uses clarification status instead of inventing material facts;
- makes small, auditable writes;
- produces no noisy report when nothing changed;
- logs material updates and blockers.

## Bad Automation Behavior

A bad automation:

- reads everything because it can;
- writes to source-of-truth records from weak evidence;
- changes formulas or schema during a processing run;
- creates duplicate records;
- reports activity even when nothing happened;
- treats stale memory as current proof.

## Minimum Verification

Each run should answer:

1. What was eligible?
2. What changed?
3. What was skipped?
4. What needs clarification?
5. What verification passed?
6. What proof status should be used?

## Recommended Daily Stack

### Relationship Triage

- Process only eligible free-text inbox records.
- Preserve raw captures.
- Deduplicate against canonical people, organizations, opportunities, interactions, and introductions.
- Use clarification status instead of inferring material facts.

### Founder Daily Plan

- Reconcile new founder commitments and dates.
- Import CRM actions as read-only suggestions.
- Rank overdue, critical, near-term, strategic, and repeated carryover work.
- Append a concise plan history.

### Control Scan

- Check stale current-state dates, broken references, unresolved contradictions, and open proof windows.
- Apply only low-risk internal repairs allowed by the contract.
- Route external, destructive, sensitive, or strategic actions to a human gate.

These may run at different times. Each needs its own contract, write boundary, and verification.

Style check: external style applied.
