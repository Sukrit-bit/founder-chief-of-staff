# Continuous Improvement Loop

## Purpose

A self-improving agent must do more than remember that it made a mistake.

The system improves only when a correction changes the control that produced the failure and the change is tested.

## Trigger Signals

Run this loop when:

- the founder corrects reasoning, priority, scope, or a factual claim;
- the agent fixes an instance but the failure class can recur;
- a validator or automation fails;
- two current artifacts contradict each other;
- the same manual intervention appears twice;
- a new workflow exposes a missing control;
- a public claim exceeds its evidence.

## Required Route

```text
1. Correct the immediate output
2. Name the failure class
3. Find the controlling route
4. Inspect the blast radius
5. Choose local, bounded structural, or human-gated repair
6. Change the control
7. Run a positive test
8. Run a negative test
9. Read back the affected state
10. Record proof status and observation window
```

## Repair Classes

| Class | Example | Remedy |
|---|---|---|
| Local | One date was transcribed incorrectly | Correct and read back the record |
| Bounded structural | Priority logic repeatedly overweights brand or revenue | Change scoring contract and test contrasting fixtures |
| Human gate | Publishing, outreach, deletion, or a strategic commitment | Prepare options and wait for approval |

## Structural Remedy Standard

A structural remedy must identify:

- the shared control that allowed the failure;
- every active route that uses that control;
- the smallest enforceable change;
- a rollback path;
- a positive fixture that should pass;
- a negative fixture that should fail or stop;
- the proof status after testing;
- the window in which recurrence will be watched.

Updating only the failure log is not a structural remedy.

## Proof Language

Use bounded proof statements:

- `Fixture pass`: the control worked on the tested case.
- `Live pass`: the control worked during a qualifying live event.
- `Observation open`: the repair is active but recurrence has not been tested enough.
- `Human-gated`: the remaining decision requires the founder.

Do not say a remedy makes failure impossible.

## Example

Weak response:

```text
The agent gives an overconfident competitor recommendation.
The founder corrects it.
The agent apologizes and edits the answer.
```

Structural response:

```text
The agent gives an overconfident competitor recommendation.
The founder corrects it.
The system names the failure: competitor-as-ceiling reasoning.
The research protocol changes: company evidence must route through capability synthesis.
A positive test preserves a transferable capability.
A negative test blocks an unsupported market-exit recommendation.
The control enters a live observation window.
```

## Required Logs

| Log | Purpose |
|---|---|
| Failure-mode register | The failure class and recurrence risk |
| Continuous-improvement log | What changed and why |
| Protocol-change log | The exact rule, template, prompt, schema, test, or code change |
| Autonomy-control ledger | Repair class, verification, rollback, proof status, and observation window |

## Completion Standard

The loop closes only when:

1. the immediate issue is corrected;
2. the right controlling surface changed;
3. related routes were inspected;
4. positive and negative checks passed;
5. unresolved human decisions are explicit;
6. proof language matches the evidence.

Style check: external style applied.
