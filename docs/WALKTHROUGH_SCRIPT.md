# Founder Chief Of Staff Walkthrough

Use this for a three-to-five-minute demonstration.

## Start With The Founder Problem

Say:

```text
A founder update rarely changes one thing.
It can change a relationship, a task, a decision and the company state at once.
Most AI assistants answer the message and leave the surrounding systems stale.
```

Show the README and landing page.

## Show How The Agent Finds The Right Context

Say:

```text
Chat is input. It is not the company record.
The source list tells the agent where each important fact belongs.
The local search index finds only the context needed for the current task.
```

Show:

- `docs/OPERATING_CONTROL_MAP.md`
- `docs/MEMORY_AND_SYNTHESIS.md`
- `AGENTS.md`

Run:

```bash
python3 runtime/cli.py rebuild
python3 runtime/cli.py context "How should a repeated failure change the next answer?"
```

Point out the source names, ownership information and limited excerpts.

## Run The Public Proof

Run:

```bash
python3 scripts/release_audit.py
```

Explain:

```text
The release audit checks the product, the public claims and the public writing.
It includes both good and bad examples.
It must reject invented facts, passive failure logging and hard-to-read public copy.
```

Show:

- `docs/EXTERNAL_WRITING_STANDARD.md`
- `evals/release-v0.3.1/external_style_contract.json`
- `runtime/benchmarks/public_casebook.json`
- `docs/PROOF_OF_OPERATION.md`
- `docs/releases/v0.3.1-evaluation.md`

## Show How A Correction Changes The System

Say:

```text
Fixing one answer is not enough when the same mistake can happen again.
The system records the failure, adds a task trigger and tests a bad and good example.
The next relevant task receives that rule before the work is released.
```

Show:

- `docs/CONTINUOUS_IMPROVEMENT_LOOP.md`
- `examples/synthetic-self-improving-loop/protocol_change.md`
- `examples/synthetic-self-improving-loop/improved_next_run.md`

## Generate A Workspace

Run:

```bash
python3 scripts/init_workspace.py /tmp/founder-chief-of-staff-demo --name "Demo Company"
python3 scripts/workspace_audit.py /tmp/founder-chief-of-staff-demo
```

Show the state registry, dashboard, working state, decision queue, daily console and automation controls.

## Close

Say:

```text
The founder keeps judgment, relationships and final calls.
The agent keeps the surrounding operating system current and applies earlier lessons before release.
```
