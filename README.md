# Founder Chief of Staff

Give an AI agent the memory and discipline to keep important founder work moving.

![Founder Chief of Staff social card](assets/social-card.svg)

## Why This Exists

Founders do not work in one thread. A customer conversation can change a relationship, a task, a product assumption and the company story at the same time.

Most AI assistants answer the message in front of them. The founder still has to remember what else changed, where the real record lives and which earlier mistake must not happen again.

Founder Chief of Staff gives an agent a durable way to carry that work forward.

> A context window is not operating memory. Search is not understanding. A failure log is not learning.

## What It Does

The system helps an agent:

- find the right company information without loading the whole workspace;
- show which source owns each important fact;
- follow useful links between decisions, work and evidence;
- bring earlier failure rules into the current task;
- check work before it is released;
- record whether the rule actually helped.

The founder keeps judgment, relationships and final decisions. The agent handles the surrounding system work.

## What Shipped

Version 0.3.1 includes a runnable local reference built with Python and SQLite. It reads approved Markdown and JSON files, builds a disposable search index and returns a small source-backed context bundle for the task.

It also selects relevant rules before release. Version 0.3.1 adds a public-writing rule and a release check that can reject accurate but hard-to-read copy. The check rejects the old failure where an internal style label appeared even though the writing had not been properly evaluated.

The fixed public casebook now tests retrieval, context limits, rule selection and both rejected and accepted work. These are synthetic tests. They do not prove that every future response will be correct.

## Product Decisions

### The original files remain the source of truth

The SQLite database exists only to make the files easy to search. Delete it and rebuild it at any time. It never becomes a competing record.

### Bring in only the context the task needs

More context is not automatically better. The system returns a limited set of excerpts and keeps their source, status and relationships visible.

### A recorded failure is not yet learning

A recurring failure must become a rule that applies to a future task. The system then checks the work and records whether the mistake was prevented, caught or repeated.

### Proof must stay honest

A green fixture proves the declared fixture. Live reliability requires repeated real use and remains unproved here.

## How It Works: Architecture

```text
named sources of truth
        ↓
find the smallest useful context
        ↓
bring in relevant failure rules
        ↓
prepare the work
        ↓
check it before release
        ↓
write verified changes back
        ↓
record what happened
```

“Canonical state” in the deeper documentation means the named source that owns a fact. The search index helps the agent find that source; it does not replace it.

## Results

- One command runs the complete release audit.
- The fixed runtime casebook includes positive and negative checks.
- The repository contains no private founder, customer or relationship data.
- The public front door now has its own external-writing test.
- The landing page has been checked at desktop and narrow widths.

These results show that the public mechanism works on declared tests. They are not a claim of general live reliability.

## Install And Use

```bash
git clone https://github.com/Sukrit-bit/founder-chief-of-staff.git
cd founder-chief-of-staff
python3 runtime/cli.py rebuild
python3 runtime/cli.py context "How should a repeated failure change the next answer?"
python3 runtime/evaluate_runtime.py
python3 scripts/release_audit.py
```

No package installation is required.

To generate the broader founder workspace:

```bash
python3 scripts/init_workspace.py my-founder-os
python3 scripts/workspace_audit.py my-founder-os
```

## Daily Rhythm

The generated workspace separates current priorities, working state, decisions, relationships, personal execution, automation and failure controls. The runtime helps the agent recover the right slice of those systems for the task at hand.

## Documentation

- [PRD.md](PRD.md) explains the product problem and decisions.
- [TECHNICAL.md](TECHNICAL.md) explains the implementation and trade-offs.
- [Memory and synthesis](docs/MEMORY_AND_SYNTHESIS.md) explains source-backed retrieval.
- [Continuous improvement](docs/CONTINUOUS_IMPROVEMENT_LOOP.md) explains how corrections become rules and evidence.
- [External writing standard](docs/EXTERNAL_WRITING_STANDARD.md) explains the new public-release gate.
- [Proof of operation](docs/PROOF_OF_OPERATION.md) maps claims to evidence.
- [Evaluation strategy](docs/EVALS.md) explains every release check.
- [Live landing page](https://sukrit-bit.github.io/founder-chief-of-staff/) is the public front door.

## What's Next

Run a cold-user installation test. Then collect real retrieval misses and repeated-task outcomes. Add more architecture only when those observations show a clear need.

## Built With

Python, SQLite FTS5, Markdown, JSON, HTML and deterministic release checks.

AI tools accelerated implementation. The product framing, operating model, evidence boundaries, evaluation design and release decisions remain founder-owned.

## License

[MIT](LICENSE)
