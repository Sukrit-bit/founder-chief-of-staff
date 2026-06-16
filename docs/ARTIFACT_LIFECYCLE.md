# Artifact Lifecycle

Founder Research OS works because important thinking does not stay trapped in chat.

Every meaningful input should become the right artifact, at the right level, with the right evidence label.

## Artifact Levels

| Level | Use For | Example |
|---|---|---|
| Project | The full operating system and current priorities. | Dashboard, working state, artifact index. |
| Theme | A broad market or arena. | Healthcare operations, climate adaptation, legal workflows. |
| Sub-arena | A narrower cluster inside a theme. | Claims processing, permitting, procurement. |
| Company hypothesis | A possible company direction. | Practice-area workflow layer. |
| Wedge | A first entry point. | Resubmission workflow, vendor review. |
| Workflow | A repeated job or work product. | Intake, checklist, review, report, escalation. |
| Evidence | Interview, pilot, usage, payment, or shadowing signal. | Pilot evidence note. |
| Source | Article, company, transcript, memo, or market signal. | Source note or case study. |

## Metadata Standard

Use this block for strategic artifacts:

```markdown
## Metadata

| Field | Value |
|---|---|
| Scope level | Project / Theme / Sub-arena / Company hypothesis / Wedge / Workflow / Evidence / Source |
| Evidence maturity | Raw signal / Structured observation / Pattern-backed / Problem candidate / Interview-backed / Experiment-backed / Pilot-backed / Decision-ready |
| Parent artifact | Path or `None` |
| Child artifacts | Paths or `None yet` |
| Decision status | Continue / Narrow / Experiment / Park / Pause / Kill / Not decision-bearing |
| Next evidence needed | Specific next evidence |
| Indexes updated | Dashboard / Working state / Artifact index / Decision queue / Pattern register / Other |
| Failure-mode check | None / Existing failure mode / New register entry |
```

The metadata block is not bureaucracy.

It tells the next agent where the artifact lives in the system.

## Lifecycle Pass

When an artifact changes strategy, scope, sequencing, positioning, or active context, run this pass:

1. Classify the artifact level.
2. Add or update the metadata block.
3. Define parent and child links.
4. Update the artifact index.
5. Update the dashboard if the current state changed.
6. Update the decision queue if judgment pressure changed.
7. Update the pattern register if a reusable signal emerged.
8. Preserve parked context explicitly.
9. Run the relevant audit or project check.

## Scope Guardrail

Do not let the current sprint become the whole project.

Say:

```text
This is the active wedge.
```

Do not say:

```text
This is the whole company.
```

Unless the evidence actually supports that decision.

## Evidence Guardrail

Do not inflate evidence.

Public research can support a pattern.

Interviews can support a problem.

Pilots can support a wedge.

Only tested assumptions should support a strategic decision.

## Completion Standard

An artifact is complete when a future session can answer:

1. What is this?
2. Why does it matter?
3. What evidence level does it have?
4. What decision does it pressure?
5. What should happen next?

