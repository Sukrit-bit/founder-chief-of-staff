# Daily Operating Console

## Purpose

The daily operating console is the founder's execution cockpit.

It is the execution view inside the Founder Chief of Staff. It does not replace the decision queue, CRM, evidence, or experiments.

The job is simple:

```text
messy commitments -> canonical tasks -> ranked daily plan -> carryover learning
```

## Why It Exists

Founder work gets messy quickly:

- market research;
- product decisions;
- customer calls;
- advisor follow-ups;
- build tasks;
- investor prep;
- service delivery;
- personal commitments to collaborators.

Canonical company systems preserve judgment and evidence. The daily console preserves execution.

Do not merge those jobs.

## Recommended Tabs Or Files

| Surface | Purpose |
|---|---|
| Dashboard / Today | Today's ranked plan, overdue items, waiting items, and carryovers |
| Quick Capture | Messy free-text task inbox |
| Tasks | Canonical task list |
| CRM Suggestions | Read-only suggested actions from the relationship system |
| Daily Plans | Historical log of morning plans |
| Picklists | Status, priority, effort, depth, source, workstream |

This can live in a spreadsheet, task database, or markdown files. The key is the workflow, not the tool.

## Minimal Task Fields

| Field | Why it matters |
|---|---|
| Task ID | Deduplication and durable reference |
| Task | Human-readable action |
| Workstream | Prevents mixed work from becoming noise |
| Source Type | Manual, CRM, decision queue, product sprint, meeting |
| Source Link / ID | Lets the task trace back to the source |
| Owner | Prevents implied ownership |
| Status | Inbox, Active, Today, Waiting, Done, Deferred, Dropped |
| Priority | P0 today, P1 this week, P2 soon, P3 parked |
| Due Date | Time pressure |
| Planned Date | Today's plan without pretending everything is due |
| Effort | Helps create a realistic day |
| Depth | Deep work, medium work, shallow work |
| Next Action | Forces execution clarity |
| Waiting On | Makes blockers visible |
| Carryover Count | Prevents repeated deferral from disappearing |

## Ranking Rule

Rank the daily plan in this order:

1. Overdue and due-today work.
2. P0/P1 work with a concrete next action.
3. Follow-ups with near-term dates.
4. Strategic work tied to active decision pressure.
5. Carryovers that repeated more than once.
6. Quick wins only after the important work is visible.

## CRM Handoff

CRM remains the source of truth for relationships and opportunity threads.

The daily console may import a CRM next action as a suggestion. It should deduplicate by source ID, action, owner, and due date. Accepting a suggestion creates or updates a personal task. It does not write back to the CRM in v0.

## Guardrails

- Do not store sensitive customer or client material in a personal task tracker.
- Do not let a task tracker become the research source of truth.
- Do not let a task tracker become the CRM source of truth.
- Do not over-measure in v0. Start with visibility before metrics.
- Review carryovers honestly. A repeated carryover is a decision signal.
