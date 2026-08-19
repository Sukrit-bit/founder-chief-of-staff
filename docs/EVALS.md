# Release Evaluation Strategy

## Purpose

The release audit answers two different questions:

1. Does the repository implement what it claims?
2. Can a serious cold reader understand why the work matters without being misled about its maturity?

A release is not ready because the code runs, the prose reads well, or one benchmark is green. All gates must pass together.

## Release Contract

Every material release has a machine-readable claim contract under `evals/release-<version>/claim_contract.json`. It defines:

- the central public claim;
- the causal product spine;
- distinctions that must survive every surface;
- shipped claims and their evidence;
- prohibited overclaims;
- deliberately deferred capabilities;
- the release stop rule.

The contract is the migration authority. It prevents a repo-wide rewrite from turning into a collection of individually plausible but mutually inconsistent pages.

## The Six Gates

### Gate One — Claim and migration contract

Check that the contract is valid, every evidence path exists, and each shipped claim has inspectable support. No public surface may imply a prohibited or deferred capability is shipped.

Failure means: stop the release and correct either the claim or the implementation.

### Gate Two — Repository-wide narrative consistency

Scan the README, PRD, technical document, agent entry points, landing page, visuals, launch essay, proof document, examples, release notes, and social card.

The following spine must remain intact:

```text
canonical sources
→ bounded relationship-aware retrieval
→ task context and applicable controls
→ decision support or candidate work
→ pre-release enforcement and verified updates
→ same-class learning evidence
```

Search for stale counts, obsolete positioning, conflicting terminology, and tactical descriptions that erase the strategic outcome.

Failure means: repair every implicated surface, not only the first mismatch.

### Gate Three — Claim and evidence consistency

Map every important external claim to one of three evidence classes:

- structural: the mechanism or contract exists;
- synthetic: declared fixtures pass;
- live: repeated real operating evidence exists.

Synthetic success must never be described as proof of general live reliability. Deferred capabilities must remain described as deferred.

Failure means: narrow the language, add evidence, or remove the claim.

### Gate Four — Runnable product behavior

Run fixed cases for:

- source retrieval and ranking;
- context character and source budgets;
- task-time control selection;
- unsafe candidate rejection;
- bounded candidate acceptance.

Both positive and negative cases are required. The public casebook is fixed before the final run so the benchmark cannot be rewritten merely to match the implementation.

Failure means: repair the runtime or the declared contract, add a regression case, and rerun the whole gate.

### Gate Five — Generated product, safety, identity, and link integrity

Run the existing document, repository-safety, identity, synthetic-scenario, workspace-generation, and workspace-audit checks. Validate internal links and referenced files.

Failure means: fix the broken artifact or path and rerun from the top-level release command.

### Gate Six — Visual and 90-second reviewer test

Inspect the landing page, operating-loop visual, and social card at desktop and narrow widths. Then apply a cold-reader test:

- Within 15 seconds: can the reader state the outcome for a founder?
- Within 45 seconds: can the reader explain memory plus retrieval plus learning?
- Within 90 seconds: can the reader distinguish shipped evidence from future ambition?

Check hierarchy, overflow, contrast, legibility, and whether implementation detail overwhelms the product story.

Failure means: revise the relevant surface and re-inspect it. Visual review is recorded evidence; it is not implied by a code pass.

## Single Release Command

```bash
python3 scripts/release_audit.py
```

The command must execute the machine-testable parts of all gates. Human visual evidence and the cold-reader findings are recorded in the versioned report under `docs/releases/`.

## Remediation Rule

An eval finding is incomplete until it records:

1. what failed;
2. why it mattered;
3. which controlling artifact changed;
4. which regression check was added or rerun;
5. the final evidence class.

The founder must not be used as the first evaluation layer for a public release. The release candidate should already have survived the contract, adversarial claims check, runnable tests, and visual review.

## Versioned Evidence

Each release report records:

- the exact release and commit candidate;
- before-and-after product claims;
- commands and results;
- benchmark counts and context limits;
- visual inspection details;
- findings and repairs;
- remaining limitations;
- final release decision.

For this migration, see [v0.3.0 evaluation](releases/v0.3.0-evaluation.md).
