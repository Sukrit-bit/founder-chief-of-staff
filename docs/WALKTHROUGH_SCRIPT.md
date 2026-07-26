# Historical v0.1 Walkthrough Script

> This script records the original research-focused release. The current project is **Founder Chief of Staff**. Start with [README.md](../README.md).

Use this for a 3-5 minute demo of Founder Research OS.

## Goal

Show the core loop quickly:

```text
messy input
-> durable artifact
-> decision pressure
-> eval
-> failure log
-> protocol/template change
-> better future run
```

The message:

```text
Founder Research OS automates decision preparation.
It preserves founder judgment.
```

## Demo Flow

### 1. Open With The Problem

Say:

```text
Most founders do not have an information problem.
They have a decision problem.

AI can summarize more information.
But founder discovery needs memory, evidence labels, decision pressure, and a way to improve when the workflow breaks.
```

Show:

- `README.md`
- `index.html`

### 2. Show The Operating Loop

Say:

```text
Every meaningful input should become project memory.
The agent should not stop at a summary.
It should create or update the artifact, pattern register, decision queue, and working state.
```

Show:

- `docs/OPERATING_LOOP.md`
- `docs/WORKING_WITH_AGENT.md`
- `docs/ARTIFACT_LIFECYCLE.md`

### 3. Show The Self-Improving Loop

Say:

```text
The second loop is the important one.
When the agent fails, the OS should improve.

A bad run becomes an eval.
The eval becomes a failure log.
The failure log becomes a protocol or template change.
The next run is better.
```

Show:

- `docs/CONTINUOUS_IMPROVEMENT_LOOP.md`
- `examples/synthetic-self-improving-loop/bad_agent_output.md`
- `examples/synthetic-self-improving-loop/protocol_change.md`
- `examples/synthetic-self-improving-loop/improved_next_run.md`

### 4. Show The Starter Workspace

Run:

```bash
python3 scripts/init_workspace.py /tmp/founder-research-demo --name "Demo Workspace"
```

Say:

```text
The starter workspace creates the operating files on day one:
dashboard, working state, artifact index, decision queue, failure register, continuous-improvement log, and protocol-change log.
```

Show:

- `/tmp/founder-research-demo/00_Context/Current_Decision_Dashboard.md`
- `/tmp/founder-research-demo/06_Decision_Log/Active_Decision_Queue.md`
- `/tmp/founder-research-demo/09_Automation/Continuous_Improvement_Log.md`
- `/tmp/founder-research-demo/09_Automation/Protocol_Change_Log.md`

### 5. Close With The Boundary

Say:

```text
The founder still owns judgment.

The agent prepares decisions.
The system preserves memory.
The failure logs improve future runs.

That is the difference between using AI as a chat window and using AI inside a founder operating system.
```

## Questions To Ask Viewers

Ask:

1. What do you think this is?
2. Would you use this for your own founder research?
3. Is the self-improving loop clear?
4. What feels too heavy?
5. What would make this more useful?
