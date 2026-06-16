# Failure Mode Register Update

Date: 2026-06-17

## New Failure Mode

| Failure | Symptom | Cause | Prevention |
|---|---|---|---|
| Summary without system update | Agent summarizes a meaningful input but does not update durable project state. | The agent treats the answer as the deliverable instead of treating the workspace as the deliverable. | If input changes project state, create or update the artifact, decision queue, artifact index, and any relevant pattern register. |

## Why This Matters

The founder should not need to ask:

```text
Did you log this?
```

The OS should preserve useful signals by default.

