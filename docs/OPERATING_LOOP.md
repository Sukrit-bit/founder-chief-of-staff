# Operating Loop

## Purpose

The operating loop prevents founder updates from remaining trapped in chat.

```text
founder event
-> evidence and eligibility check
-> affected canonical systems
-> bounded writes
-> read-back verification
-> concise founder view
```

Research and discovery use a nested loop:

```text
source -> structured observation -> pattern -> decision -> experiment -> evidence
```

The improvement loop sits behind it:

```text
bad run or new learning -> eval -> failure register -> protocol/template change -> better next run
```

## Loop Stages

| Stage | Meaning | Output |
|---|---|---|
| Event | Update, commitment, correction, relationship change, research signal, or decision. | Supported facts and uncertainties. |
| Routing | Resolve which canonical systems own the change. | Affected-system checklist. |
| Writes | Apply only allowed, deduplicated changes. | Updated state, CRM, tasks, evidence, or controls. |
| Verification | Read back every material write and run relevant checks. | Verified result or explicit failure. |
| Founder view | Surface priorities, blockers, decisions, and clarification needs. | Concise operating update. |
| Improvement | Classify recurring failures and change the shared control. | Tested structural remedy. |

## Operating Rule

Do not let a material event stop at summary.

Every meaningful input should answer:

1. What changed, and what remains uncertain?
2. Which systems are authoritative for the change?
3. What decision or action does it affect?
4. What may not be inferred?
5. What was written and read back?
6. Did this expose a shared-control failure?

## Visual

Open [../visuals/operating-loop.html](../visuals/operating-loop.html) for the visual map.
