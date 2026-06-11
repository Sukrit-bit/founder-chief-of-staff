# Founder Research OS

An AI-native operating system for turning messy market curiosity into evidence-backed startup decisions.

This repo shows the method, not a private founder's live startup research.

Most AI founder workflows stop at summaries. This one keeps pushing toward decisions.

## What It Does

Founder Research OS gives an AI agent a structured workspace so it can operate as a research assistant, decision OS, and chief-of-staff layer for a founder.

It turns this:

```text
article, company, conversation, hunch
```

into this:

```text
source note -> pattern -> problem candidate -> decision queue -> experiment -> updated state
```

Start here:

- [PRD.md](PRD.md) explains the product case.
- [TECHNICAL.md](TECHNICAL.md) explains the operating architecture.
- [PROMPT.md](PROMPT.md) contains the public agent spec.
- [docs/LAUNCH_NOTE.md](docs/LAUNCH_NOTE.md) gives the short public narrative.
- [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md) defines the release bar.
- [docs/OPERATING_LOOP.md](docs/OPERATING_LOOP.md) shows the loop.
- [visuals/operating-loop.html](visuals/operating-loop.html) gives a visual map.
- [examples/synthetic-municipal-permitting](examples/synthetic-municipal-permitting) shows one synthetic loop.

## Product Decisions That Matter

1. The workspace is the memory layer.

   Chat is useful for thinking. The repo is where durable state lives.

2. Evidence has levels.

   Public research, repeated patterns, interviews, experiments, and decisions should not be treated as the same thing.

3. The system keeps a decision queue.

   Good research is not enough. The project must force continue, narrow, experiment, park, pause, or kill calls.

4. The agent is allowed to maintain the system.

   If the agent finds a low-risk operating fix, it should implement it and cross-reference it.

5. Public work is separated from private edge.

   The reusable method can be shared. Live theses, access paths, interview notes, and founder right-to-win stay private.

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

This first public export turns 1 private operating method into 39 public-safe files, with 1 clear outcome: a founder can move from loose signal to decision pressure without relying on chat memory.

The human outcome is faster founder judgment: fewer loose notes, fewer forgotten insights, and fewer ideas sitting in the vague middle between "interesting" and "worth testing."

## Setup

Clone the repo and read the docs in this order:

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

Run the public leak scan:

```bash
python3 scripts/public_leak_scan.py --repo .
```

Use the templates:

```bash
templates/source_note.md
templates/pattern_register.md
templates/decision_queue.md
templates/experiment_plan.md
```

## Next

The next milestone is proof, not polish.

- Add one more synthetic example outside municipal permitting.
- Add a redaction/export checklist for private teams.
- Add a small CLI that creates a new theme folder from templates.
- Add a public walkthrough video or short essay.
- Test the system with another founder and record where it breaks.

## Public Safety

This repo is designed as a public export.

It should not contain live startup theses, private interview notes, customer names, access paths, or proprietary research synthesis.

The leak scan is intentionally simple. It is not a substitute for judgment, but it catches obvious mistakes before publication.

## Built With

This scaffold was built with Codex as the implementation partner.

The human role was product judgment: defining the operating model, confidentiality boundary, public positioning, and quality bar. The AI role was scaffolding the repo, drafting docs, preserving cross-references, and running checks.
