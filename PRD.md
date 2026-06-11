# PRD: Founder Research OS

## The Problem

Founders gather signals faster than they make decisions.

They read markets, scan companies, talk to operators, test ideas, and collect strong opinions. The hard part is not note-taking. The hard part is converting those inputs into a clear view of what to continue, narrow, test, park, pause, or kill.

Most AI workflows help with one task. They summarize an article. They draft a memo. They answer a question. They do not carry a founder's research state across weeks of messy exploration.

## The Core Insight

An AI agent becomes more useful when the workspace gives it memory, protocols, evals, and autonomy boundaries.

The agent should not only answer. It should help run the research operating system.

That means every important input should move through a visible loop:

```text
input -> artifact -> pattern -> decision queue -> experiment -> evidence -> updated context
```

## Key Decisions And Why

### Decision 1: Make the repo the memory layer

The obvious approach is to keep using chat history. That fails because chat history is hard to audit, hard to search, and easy to lose across sessions.

The chosen approach is to make the project folder carry the live state. The dashboard, working state, artifact index, decision queue, and evals are all files.

The result is a workspace that can be resumed without asking the founder to reconstruct the last conversation.

### Decision 2: Separate evidence from conviction

The obvious approach is to turn strong market research into a thesis. That is dangerous. Public research can show patterns, but it does not prove buyer urgency.

The chosen approach is an evidence maturity ladder. Each artifact says whether it is raw, structured, pattern-backed, interview-backed, experiment-backed, or decision-ready.

The result is less false certainty.

### Decision 3: Force decision pressure

The obvious approach is to keep adding research. That feels productive but often avoids judgment.

The chosen approach is a decision queue. Every serious hypothesis needs a status and next evidence requirement.

The result is a system that asks, "What would make us continue, narrow, experiment, park, pause, or kill this?"

### Decision 4: Let the agent maintain the system

The obvious approach is to make the agent wait for every instruction. That creates hidden admin work for the founder.

The chosen approach is controlled autonomy. The agent can make low-risk maintenance updates, cross-reference artifacts, run checks, and log repeated failure modes.

The result is a system that improves when it breaks.

### Decision 5: Ship with synthetic examples

The obvious approach is to explain the framework with someone else's real research. That creates noise and risk.

The chosen approach is to make the framework complete on its own and use synthetic examples to show the loop.

The result is a repo that feels usable immediately. Users bring their own markets, sources, interviews, and decisions into their own workspace.

## The Output

A founder using this system gets:

- a landing page explaining the method;
- a dashboard for what matters now;
- a working state file for full continuity;
- an artifact index for navigation;
- source notes and case studies for research inputs;
- pattern registers for repeated signals;
- problem backlogs and experiment plans;
- a decision queue;
- operating reviews and failure-mode logs;
- reusable templates.
- a starter script for creating a new workspace.

## Architecture

The architecture is file-native:

```text
00_Context
01_Themes
03_Problem_Statements
04_Venture_Theses
05_Experiments
06_Decision_Log
07_Source_Material
09_Automation
templates
```

This repo compresses that into docs, templates, examples, and scripts.

See [TECHNICAL.md](TECHNICAL.md) for implementation details.

## Edge Cases

If the agent overclaims, the evidence ladder should force a lower maturity label.

If the founder changes scope, abstraction guardrails should prevent the current sprint from being mistaken for the whole project.

If the agent repeats a mistake, the failure-mode register should turn the correction into a protocol change.

If the team wants to share a repo or demo, the data-handling checklist should catch sensitive material before release.

## What's Next

The next version should prove repeatability with real users.

- Run 2 synthetic examples.
- Run 1 real local loop from source to experiment.
- Add a stronger data-handling checklist.
- Expand the starter script into a compact CLI.
- Add examples of evals catching bad work.

The quality bar is defined in [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md).

## How It Was Built

This framework was built from an operating system already used for founder research.

Codex helped turn the method into documentation, templates, a synthetic example, a visual explainer, and audit scripts.
