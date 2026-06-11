# Quality Bar

## What This Repo Should Signal

This repo should signal founder judgment, not prompt enthusiasm.

The reader should understand three things within 90 seconds:

1. The system helps a founder make startup decisions.
2. The agent works inside a structured operating system.
3. The public repo protects private research edge.

## What Counts As Good

- Clear operating loop.
- Sharp evidence labels.
- Public/private boundary.
- Decision queue.
- Synthetic examples.
- Evals that produce remediation.
- Scripts that catch obvious drift.

## What Counts As Weak

- Long notes without decisions.
- A folder structure with no loop.
- Generic AI language.
- Claims without examples.
- Public examples that leak private research.
- A repo that looks like a prompt pack.

## Pre-Publish Gate

Before public release:

```bash
python3 scripts/doc_audit.py --repo . --strict
python3 scripts/public_leak_scan.py --repo .
```

Then ask:

```text
Would a serious founder, operator, investor, or AI builder understand why this exists?
Would publishing this reduce any private startup edge?
Does the repo show a method, not just a claim?
```

