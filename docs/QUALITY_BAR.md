# Quality Bar

## What This Repo Should Signal

This repo should signal founder judgment, not prompt enthusiasm.

The reader should understand three things within 90 seconds:

1. The system helps a founder make startup decisions.
2. The agent works inside a structured operating system.
3. The repo is complete enough to use with their own research context.
4. The public surface reflects strong product judgment, not only documentation completeness.
5. The working style is clear without private chat context.
6. The self-improving loop is obvious: evals and failures change future behavior.

## What Counts As Good

- Clear operating loop.
- Sharp evidence labels.
- Synthetic examples.
- Decision queue.
- Evals that produce remediation.
- Continuous-improvement logs that explain what changed and why.
- Protocol or template changes caused by real failures.
- Scripts that catch obvious drift.
- Data-handling checks.
- A clear founder-agent collaboration model.
- A starter workspace that creates the actual operating files.
- A landing page that makes the idea clear before someone reaches the file tree.
- A starter path that makes the system usable.

## What Counts As Weak

- Long notes without decisions.
- A folder structure with no loop.
- Generic AI language.
- Claims without examples.
- Examples that expose sensitive customer, interview, or company material.
- A repo that looks like a prompt pack.
- A launch surface that looks like internal cleanup work.
- A repo that makes the author look organized but not worth meeting.
- Failure logs that do not change future behavior.

## Release Gate

Before sharing a repo or demo:

```bash
python3 scripts/doc_audit.py --repo . --strict
python3 scripts/repo_safety_check.py --repo .
```

Then ask:

```text
Would a serious founder, operator, investor, or AI builder understand why this exists?
Could this be shared without exposing sensitive material?
Does the repo show a method, not just a claim?
Does the first public screen make the artifact feel finished?
Would a strong founder, builder, or investor want to talk to the person who made this?
Can someone see how the OS improves after a bad run?
```
