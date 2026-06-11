# Contributing To Founder Research OS

Founder Research OS is not a prompt pack.

It is an operating system for helping founders turn market signals into evidence-backed startup decisions.

Contributions should make that loop sharper:

```text
input -> artifact -> pattern -> decision queue -> experiment -> evidence -> updated context
```

If a change does not improve memory, evidence quality, decision pressure, data handling, or repeatability, it probably does not belong here.

## Good Contributions

- Better templates that help a founder capture a real research artifact.
- Stronger eval rubrics that catch weak reasoning or overclaiming.
- Cleaner synthetic examples that show the loop without exposing sensitive work.
- Data-handling checks that reduce release risk.
- Small scripts that make the OS easier to run and audit.
- Documentation that helps founders make continue, narrow, experiment, park, pause, or kill decisions.

## Strong PRs

Strong PRs usually do one of these:

- move an idea from vague synthesis toward a decision;
- make evidence maturity clearer;
- make sensitive-material handling safer;
- make the agent's operating rules more enforceable;
- improve an example so another founder can copy the method.

## Not In Scope

- Dumps of sensitive customer, interview, or company material.
- Prompt collections without an operating loop.
- Generic note-taking templates.
- Claims that public research equals customer validation.
- Examples that include real conversations or access paths.
- Broad productivity-system features that do not improve founder research decisions.

## Quality Bar

Before opening a pull request:

```bash
python3 scripts/doc_audit.py --repo .
python3 scripts/repo_safety_check.py --repo .
```

Then ask:

```text
Does this help a founder make a better decision?
Does this preserve the difference between signal, pattern, validation, and conviction?
Could this be shared without exposing sensitive customer, interview, or company material?
```

The repo should stay decision-focused and safe to share.
