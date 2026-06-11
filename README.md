# Founder Research OS

Founders do not have an information problem. They have a decision problem.

Founder Research OS is an open-source workspace for turning messy market curiosity into evidence-backed startup decisions with AI agents.

![Founder Research OS social card](assets/social-card.svg)

## What It Does

Founder Research OS gives an AI agent a structured workspace so it can operate as a research assistant, decision OS, and chief-of-staff layer for a founder.

It turns this:

```text
article, company, conversation, hunch
```

into this:

```text
source note -> pattern -> problem candidate -> decision queue -> experiment -> evidence -> updated state
```

Start here:

- [Live landing page](https://sukrit-bit.github.io/founder-research-os/) is the public front door.
- [Use this template](https://github.com/new?template_name=founder-research-os&template_owner=Sukrit-bit) to create your own workspace.
- [PRD.md](PRD.md) explains the product case.
- [TECHNICAL.md](TECHNICAL.md) explains the operating architecture.
- [PROMPT.md](PROMPT.md) contains the agent spec.
- [docs/LAUNCH_ESSAY.md](docs/LAUNCH_ESSAY.md) explains the core idea.
- [docs/LAUNCH_NOTE.md](docs/LAUNCH_NOTE.md) gives the short launch narrative.
- [docs/LAUNCH_THREAD.md](docs/LAUNCH_THREAD.md) gives launch copy for X or LinkedIn.
- [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md) defines the release bar.
- [docs/DATA_HANDLING.md](docs/DATA_HANDLING.md) defines how to handle real workspace material.
- [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md) defines the release checklist.
- [docs/OPERATING_LOOP.md](docs/OPERATING_LOOP.md) shows the loop.
- [visuals/operating-loop.html](visuals/operating-loop.html) gives a visual map.
- [examples/synthetic-municipal-permitting](examples/synthetic-municipal-permitting) shows one complete synthetic loop.

## Product Decisions That Matter

1. The workspace is the memory layer.

   Chat is useful for thinking. The repo is where durable state lives.

2. Evidence has levels.

   Public research, repeated patterns, interviews, experiments, and decisions should not be treated as the same thing.

3. The system keeps a decision queue.

   Good research is not enough. The project must force continue, narrow, experiment, park, pause, or kill calls.

4. The agent is allowed to maintain the system.

   If the agent finds a low-risk operating fix, it should implement it and cross-reference it.

5. Examples are synthetic by default.

   The repo should feel complete out of the box. Users bring their own markets, sources, interviews, and decisions into their own workspace.

## How It Works

The core loop is simple:

```text
input -> artifact -> pattern -> decision queue -> experiment -> evidence -> updated context
```

The project uses five layers:

- Dashboard: what matters now.
- Working state: canonical full context.
- Artifact index: where files live.
- Decision queue: what needs judgment.
- Evals and failure modes: how the system improves.

## Results

This repository ships a complete v0.1 framework with 1 clear outcome: a founder can move from loose signal to decision pressure without relying on chat memory.

The human outcome is faster founder judgment: fewer loose notes, fewer forgotten insights, and fewer ideas sitting in the vague middle between "interesting" and "worth testing."

## Setup

Create a starter workspace:

```bash
git clone https://github.com/Sukrit-bit/founder-research-os.git
cd founder-research-os
python3 scripts/init_workspace.py ~/founder-research/my-next-idea
```

Then read the docs in this order:

```bash
README.md
PRD.md
TECHNICAL.md
PROMPT.md
docs/OPERATING_LOOP.md
examples/synthetic-municipal-permitting/README.md
```

Run the documentation audit:

```bash
python3 scripts/doc_audit.py --repo .
```

Run the repo safety check:

```bash
python3 scripts/repo_safety_check.py --repo .
```

Use the templates:

```bash
templates/source_note.md
templates/pattern_register.md
templates/decision_queue.md
templates/experiment_plan.md
```

## Next

The next milestone is repeatability with real users.

- Add one more synthetic example outside municipal permitting.
- Expand the starter script into a small CLI.
- Add a walkthrough video or short essay.
- Test the system with another founder and record where it breaks.

## Data Handling

The repo ships with synthetic examples.

When using it for real work, keep sensitive customer, interview, credential, and company material in your own controlled workspace.

The safety check is intentionally simple. It is not a substitute for judgment, but it catches common mistakes before a repo is shared.

## Built With

This framework was built with Codex as the implementation partner.

The human role was product judgment: defining the operating model, release standard, and quality bar. The AI role was scaffolding the repo, drafting docs, preserving cross-references, and running checks.
