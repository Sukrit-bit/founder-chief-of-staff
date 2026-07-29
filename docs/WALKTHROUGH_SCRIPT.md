# Founder Chief Of Staff Walkthrough

Use this for a 3-5 minute demonstration.

## 1. State The Problem

```text
A founder update rarely changes one thing.
It can change a relationship, task, decision, and company state at once.
Most AI assistants answer the message and leave those systems stale.
```

Show `README.md` and the live landing page.

## 2. Show The Operating Contract

```text
Chat is input, not authority.
The state registry and control map tell the agent which system owns each fact and what it may change.
```

Show:

- `docs/OPERATING_CONTROL_MAP.md`
- `docs/MEMORY_AND_SYNTHESIS.md`
- `AGENTS.md`

## 3. Run The Public Proof

```bash
python3 scripts/release_audit.py
```

Explain:

```text
The positive founder-event fixture must reconcile CRM, personal execution,
current state, and the decision queue.

The negative fixture must be blocked when it invents a rejection,
response date, or outreach.
```

Show:

- `evals/founder-event-reconciliation/contract.json`
- `evals/founder-event-reconciliation/valid-plan.json`
- `evals/founder-event-reconciliation/invalid-plan.json`
- `docs/PROOF_OF_OPERATION.md`

## 4. Show Structural Improvement

```text
When a failure can recur, fixing one answer is insufficient.
The shared control changes, positive and negative tests run,
and the remedy stays under observation.
```

Show:

- `docs/CONTINUOUS_IMPROVEMENT_LOOP.md`
- `examples/synthetic-self-improving-loop/protocol_change.md`
- `examples/synthetic-self-improving-loop/improved_next_run.md`

## 5. Generate A Workspace

```bash
python3 scripts/init_workspace.py /tmp/founder-chief-of-staff-demo --name "Demo Company"
python3 scripts/workspace_audit.py /tmp/founder-chief-of-staff-demo
```

Show the generated state registry, dashboard, working state, decision queue, daily console, and automation controls.

## Close

```text
The founder keeps judgment.
The agent owns capture, reconciliation, decision preparation,
verification, and low-risk system maintenance.
```

Style check: external style applied.
