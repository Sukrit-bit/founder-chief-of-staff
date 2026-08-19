# Queryable Memory And Bounded Learning Runtime

This public runtime demonstrates the two capabilities that make the Founder Chief of Staff more than a collection of files and prompts:

1. **Queryable operating memory:** retrieve a bounded, source-backed slice of the workspace while preserving authority, lifecycle, relationships and review triggers.
2. **Bounded learning:** retrieve prior failure controls for the current task and evaluate the actual candidate output before release.

The SQLite index is derived and rebuildable. Markdown and JSON sources remain authoritative.

```bash
python3 runtime/cli.py rebuild
python3 runtime/cli.py query "What did we decide about operating memory?"
python3 runtime/cli.py context "Explain how a logged failure becomes learning" --json
python3 runtime/evaluate_runtime.py
```

The included sources and cases are synthetic or public. The runtime does not include private founder data, external connectors, a vector database or a self-modifying policy engine.
