# TECHNICAL: Founder Chief of Staff

## Overview

Founder Chief of Staff is a file-native control layer for AI-assisted company building. It can coordinate connected Sheets, documents, repositories, and automations, but no connector becomes the source of truth merely because the agent can access it.

Start with [README.md](README.md) and [PRD.md](PRD.md).

## System Model

```text
founder or external event
        |
        v
eligibility and evidence check
        |
        v
operating control map -> state registry -> implicated canonical systems
        |                                  |
        |                                  +-> decisions
        |                                  +-> relationships
        |                                  +-> tasks
        |                                  +-> research and capabilities
        v
bounded writes -> read-back verification -> proof or clarification status
```

## Engineering Decisions

### 1. File-native control, tool-native data

Markdown and JSON make the control system inspectable and portable. Live CRM or task records may remain in Sheets. Product delivery status may remain in another repository. The state registry records authority, access mode, and update triggers.

Tradeoff: the agent must route carefully. Benefit: one tool outage or chat reset does not redefine truth.

### 2. Registry plus control map

The state registry is machine-readable. The control map is human-readable. Together they answer:

- what is authoritative;
- what is current versus historical;
- what is read-only;
- what can be updated automatically;
- what requires a human decision;
- what must never be opened or published.

### 3. Event-to-system reconciliation

The agent classifies a founder update as a fact change, commitment, decision, relationship event, research signal, correction, or combination. It then resolves every implicated route before closing the turn.

This prevents the common failure where chat is correct but the CRM, task list, and working state remain stale.

### 4. Evidence and contradiction gates

Material claims carry a source, evidence level, and proof status. When two current sources disagree, the agent records a contradiction and blocks closure of the affected claim.

This does not eliminate hallucinations. It makes unsupported claims and unresolved conflicts observable.

### 5. Capability intelligence

Company research enters as evidence, not scope. A normalized capability record contains:

```text
problem -> user -> trigger -> workflow -> capability -> proof
-> limitation -> transfer conditions -> Inkstone-style decision
```

The final field is generic in a new workspace: build, integrate, bundle, compete, monitor, reject, or needs evidence.

### 6. One-way operational handoffs

CRM actions may create suggestions in the personal execution console. The console does not silently update CRM opportunity truth. Product strategy may create an implementation brief. The coding agent does not silently rewrite strategy.

### 7. Automation as a contract

Each recurring job defines:

- trigger and purpose;
- allowed inputs and eligible states;
- allowed writes;
- prohibited actions;
- inference and deduplication rules;
- stop conditions;
- verification;
- reporting behavior.

No eligible input means no write. No material change can mean no report.

### 8. Structural correction controller

Correction handling has three routes:

| Route | Use | Required proof |
|---|---|---|
| Local | One output is wrong and cannot recur through a shared control | Correct output and read-back |
| Bounded structural | Shared prompt, protocol, schema, or automation can reproduce the failure | Control change, rollback path, positive and negative tests |
| Human gate | External, destructive, sensitive, or strategic decision | Explicit founder approval |

A proof window tracks whether the same failure class returns. A clean test proves the control works on the fixture; it does not prove the system can never fail.

## Generated Workspace

The starter creates:

- current dashboard, working state, artifact index, control map, and JSON state registry;
- decision queue and operating reviews;
- relationship and personal-execution boundaries;
- automation registry and contracts;
- failure, continuous-improvement, protocol-change, and autonomy-control logs;
- reusable templates.

## Verification

Repository checks:

```bash
python3 scripts/doc_audit.py --repo .
python3 scripts/repo_safety_check.py --repo .
```

Generated workspace check:

```bash
python3 scripts/init_workspace.py /tmp/founder-chief-of-staff-demo
python3 scripts/workspace_audit.py /tmp/founder-chief-of-staff-demo
```

The workspace audit checks required control files, JSON validity, state-registry targets, and required automation-control fields.

## Security And Privacy Boundaries

- Keep credentials and environment files outside publishable paths.
- Keep client and customer work in restricted systems.
- Give agents the minimum read and write scope needed for the route.
- Treat external publication and outreach as human-gated.
- Use synthetic examples in the public repository.
- Run the safety check before a commit intended for sharing.

## Tradeoffs

The system adds operating discipline. That is worthwhile only if each artifact has one clear job.

Avoid adding a new document when an existing canonical surface can own the information. Add a new control only when it prevents a real failure, removes recurring work, or defines a distinct source of truth.

## Closing

The technical claim is narrow: a general agent becomes more reliable as a founder's Chief of Staff when state, ownership, evidence, write boundaries, corrections, and verification are explicit and inspectable.

Style check: external style applied.
