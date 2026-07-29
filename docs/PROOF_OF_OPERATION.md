# Proof Of Operation

This page separates what the repository proves directly from what depends on an AI agent, connected tools, or a private founder workspace.

## Public Proof

| Capability | Public evidence | Proof status |
|---|---|---|
| Create a canonical founder workspace | `scripts/init_workspace.py` generates the state registry, current state, decision queue, execution boundaries, automation controls, and templates | Runnable |
| Validate workspace integrity | `scripts/workspace_audit.py` checks required controls, JSON validity, registered targets, and correction-ledger fields | Runnable |
| Prevent common publication leaks | `scripts/repo_safety_check.py` scans publishable files for common secret and confidentiality markers | Runnable, bounded |
| Route a founder event across systems | `evals/founder-event-reconciliation/` tests the required CRM, execution, state, and decision routes | Synthetic fixture pass |
| Block invented outcomes and deadlines | The negative fixture must fail when it treats silence as rejection, invents a response date, or claims outreach | Synthetic negative pass |
| Start Codex, Claude Code, or another agent | `AGENTS.md`, `CLAUDE.md`, and `PROMPT.md` provide native and portable operating contracts | Inspectable |
| Verify a release | `scripts/release_audit.py` runs documentation, safety, scenario, generation, and workspace checks together | Runnable |

Run the complete proof:

```bash
python3 scripts/release_audit.py
```

## Agent-Dependent Behavior

The repository is an operating harness, not a hosted agent service. The AI runtime is supplied by Codex, Claude Code, Hermes, or another capable agent.

The agent is responsible for:

- interpreting a messy founder update;
- selecting the minimum current context;
- proposing the affected systems;
- writing only through configured connectors and permissions;
- reading changes back;
- escalating unsupported or strategic decisions.

The public evals test the contracts around that behavior. They do not prove that every model will follow them perfectly.

## Private Operating Evidence

The framework is used in a private founder workspace for relationship triage, daily planning, company-state reconciliation, research synthesis, and correction control. That workspace is intentionally not included because it contains company strategy, relationships, and operating data.

The public repository exposes the schemas, contracts, synthetic cases, and verification methods needed to inspect or reproduce the method without publishing that private state.

## Claim Boundaries

- `Runnable` means the code can be executed from this repository.
- `Synthetic fixture pass` means a deterministic public case passes.
- `Inspectable` means the contract is present and reviewable, but execution depends on an agent.
- Private use is not independent external validation.
- A clean eval proves the tested behavior, not permanent immunity from failure.

Style check: external style applied.
