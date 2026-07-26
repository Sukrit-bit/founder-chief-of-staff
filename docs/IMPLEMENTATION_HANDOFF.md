# Implementation Handoff

## Purpose

Founder Chief of Staff can feed a product repo without becoming the product repo.

Use implementation handoffs when strategy, discovery, or workflow design needs to become buildable work for a coding agent or engineering team.

The handoff should be narrow, current, and versioned.

## Core Pattern

```text
research OS
-> implementation handoff brief
-> product repo
-> build artifact
-> product evidence
-> updated decision queue
```

The product repo should not be forced to read the whole research archive.

## What Goes Into A Handoff

| Section | Purpose |
|---|---|
| Product intent | What user problem the build serves |
| Current decision | What has already been decided |
| Source artifacts | Which research artifacts support the brief |
| User flow | What the user should be able to do |
| Architecture constraints | Boundaries the implementation should preserve |
| Non-goals | What should not be built yet |
| Data and confidentiality | What may and may not enter the product repo |
| Acceptance checks | How the build should be verified |
| Open questions | What still needs founder or user judgment |

## Agent Coordination Options

Use the lightest bridge that solves the problem:

| Option | Use when | Shape |
|---|---|---|
| Checked-in handoff doc | The product repo needs stable context | Add `docs/implementation_handoff.md` or similar |
| Project instructions | The coding agent needs persistent build rules | Use the repo's agent instruction file |
| Imported context file | A coding agent supports imports from another file | Import the handoff explicitly rather than loading the whole workspace |
| Project-scoped tool connection | The build agent needs live data from another system | Use a shared, bounded tool or MCP configuration |
| Issue or PR handoff | Work should happen through code review | Create an issue or PR with the handoff as the body |

## Guardrails

- Do not expose private research, customer details, credentials, or sensitive access paths.
- Do not let the coding agent infer product strategy from old notes.
- Do not let the research OS edit the product repo silently.
- Do not let build output become validation until users or evidence support it.

## Completion Standard

A good handoff lets a coding agent answer:

1. What should I build?
2. Why does it matter?
3. What must I preserve?
4. What must I avoid?
5. How do I know it works?
6. What should I ask before proceeding?
