# Memory And Synthesis

## Purpose

The memory layer should help an agent recover current truth without pretending that chat history is reliable.

The synthesis layer should turn research into decisions without treating every company as a competitor verdict or every feature as roadmap scope.

## Queryable Operating Memory

Canonical memory is necessary but insufficient. If an agent must reread the whole workspace, it will waste context, flatten authority, and still miss relationships that make a fact meaningful.

Version 0.3.0 adds a derived retrieval layer with four rules:

1. canonical files remain authoritative;
2. the SQLite index can always be rebuilt;
3. retrieval returns a bounded context bundle with source IDs and authority;
4. relationship expansion follows explicit registered edges rather than resemblance alone.

The goal is not to remember everything. It is to recover the smallest reliable slice needed to move the current work forward without losing provenance or nuance.

```bash
python3 runtime/cli.py rebuild
python3 runtime/cli.py context "What should change after a repeated failure?"
```

## Memory Model

Use five distinct layers:

| Layer | Job | Example |
|---|---|---|
| State registry | Machine-readable authority and access map | Which file or Sheet owns CRM truth |
| Dashboard | Current focus and immediate pressure | The three decisions that matter now |
| Working state | Full current continuity | Current thesis, active paths, and blockers |
| Artifact index | Navigation | Where the current product brief lives |
| History and proof | Audit trail | Why a rule changed and how it was tested |

Chat is an input to this system. It is not one of these layers.

The generated SQLite database is also not one of these authority layers. It is a disposable access structure over them.

## State Registry Contract

Each registered system should declare:

- stable ID;
- purpose;
- location;
- authority level;
- read and write mode;
- current versus historical status;
- owner;
- update trigger;
- prohibited content or actions.

If two current authoritative sources conflict, create a contradiction record and block the affected conclusion.

## Evidence Contract

Keep these levels separate:

1. Raw signal.
2. Structured observation.
3. Repeated pattern.
4. Interview-backed problem.
5. Experiment-backed result.
6. Decision-ready evidence.

Better writing does not raise evidence maturity.

## Company-To-Capability Synthesis

For every company or product studied, record:

| Field | Question |
|---|---|
| Company | What was studied? |
| Target user | Who has the problem? |
| Problem | What costly or risky job remains unresolved? |
| Trigger | When does the need become urgent? |
| Workflow | What work happens from input to output? |
| Capability | What reusable product capability enables that work? |
| Mechanism | How does the product deliver it? |
| Proof | What source supports the claim? |
| Limitation | What has not been proved? |
| Transfer conditions | What would need to be true in our context? |
| Decision route | Build, integrate, bundle, compete, monitor, reject, or needs evidence |
| Destination | Which roadmap question, experiment, or decision should receive it? |

This prevents two failures:

- stopping at a competitor summary;
- turning an interesting feature into automatic scope.

## Synthesis Rules

- Analyze adjacent products, services, and workflows, not only direct competitors.
- Preserve multiple possible routes when the market is large.
- Separate the capability from the company's chosen market.
- State whether a lesson affects product, go-to-market, service delivery, trust, pricing, or architecture.
- Deduplicate capabilities before adding roadmap pressure.
- Keep the source case linked so a later decision can inspect the evidence.
- A competitor's existence does not decide whether to enter a space.

## Completion Standard

A future agent should be able to answer:

1. Which source is authoritative?
2. What is current and what is history?
3. What evidence supports the claim?
4. Which contradiction remains open?
5. Which transferable capability was extracted?
6. Which decision or experiment should use it?
7. How much context was retrieved, and why were those sources included?

Style check: external style applied.
