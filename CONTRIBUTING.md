# Contributing

Founder Research OS is a public method scaffold.

Contributions should improve the method without turning the repo into a generic productivity system.

## Good Contributions

- Better templates.
- Stronger eval rubrics.
- Cleaner synthetic examples.
- Redaction and export checks.
- Small scripts that improve repeatability.
- Documentation that helps founders make better decisions.

## Not In Scope

- Private research dumps.
- Prompt collections without an operating loop.
- Generic note-taking templates.
- Claims that public research equals customer validation.
- Examples that include real private conversations or access paths.

## Quality Bar

Before opening a pull request:

```bash
python3 scripts/doc_audit.py --repo .
python3 scripts/public_leak_scan.py --repo .
```

The repo should stay public-safe.

