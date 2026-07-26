# Relationship And Execution Stack

## Purpose

Founders need relationship memory and personal execution, but those systems should not become one spreadsheet.

The relationship stack owns people and opportunities. The execution stack owns what the founder should do.

## Relationship System

Recommended canonical records:

| Record | Purpose |
|---|---|
| People | One record per person |
| Organizations | One record per organization |
| Opportunity threads | Commercial, design-partner, investor, advisor, or hiring path |
| Interactions | Calls, messages, meetings, and material updates |
| Introductions | Connector, target, owner, and status |

A free-text inbox should let users capture messy updates. A scheduled triage can structure eligible rows.

### Triage Rules

- Preserve the raw capture.
- Process only eligible statuses.
- Check canonical records before creating anything.
- Deduplicate by stable ID, source, person, organization, owner, date, and thread.
- Do not infer a material relationship, commitment, owner, or date.
- Use clarification status when information is missing.
- Do not change formulas or schema during a processing run.
- If nothing is eligible, make no writes and produce no report.

## Personal Execution System

Recommended views:

| View | Purpose |
|---|---|
| Dashboard / Today | Ranked plan, overdue work, waiting items, and carryovers |
| Quick Capture | Messy task inbox |
| Tasks | Canonical personal task list |
| CRM Suggestions | Read-only next actions derived from relationship records |
| Daily Plans | Morning-plan history |
| Picklists | Controlled status, priority, effort, depth, and source values |

Minimal task fields:

```text
Task ID, Task, Workstream, Source Type, Source Link or ID, Owner,
Status, Priority, Due Date, Planned Date, Effort, Depth,
Next Action, Waiting On, Carryover Count, Last Updated, Notes
```

## Handoff Contract

The v0 handoff is one-way:

```text
CRM next action -> CRM suggestion -> founder accepts or ignores -> personal task
```

The personal console does not change CRM relationship or opportunity truth.

Deduplicate a suggestion against canonical tasks using source ID, owner, action, and due date.

## Morning Plan

Rank:

1. Overdue and due-today work.
2. Critical work with a concrete next action.
3. Near-term relationship follow-ups.
4. Strategic work tied to an active decision.
5. Repeated carryovers.
6. Quick wins after the important work is visible.

The founder should be able to understand the day in under two minutes.

## Boundaries

- Do not store client work or sensitive legal analysis in a CRM or personal task tracker.
- Do not make the task tracker the source of truth for relationship facts.
- Do not send outreach or schedule meetings without approval.
- Do not add metrics until they answer a real operating question.
- Keep waiting items visible; do not convert them into false active work.

Style check: external style applied.
