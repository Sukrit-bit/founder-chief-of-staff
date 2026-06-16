# Templates

Use these files to create durable founder research artifacts.

The core flow is:

```text
source_note -> artifact_card -> pattern_register -> decision_queue -> experiment_plan -> continuous_improvement_entry
```

Start with:

- `artifact_card.md` for strategic artifact metadata and decision pressure.
- `source_note.md` for raw inputs.
- `pattern_register.md` for repeated signals.
- `decision_queue.md` for continue, narrow, experiment, park, pause, or kill calls.
- `experiment_plan.md` for the next evidence loop.
- `pilot_evidence.md` for live service, workflow, or concierge-learning loops.
- `continuous_improvement_entry.md` for logging what changed in the OS and why.
- `protocol_change.md` for rule or template changes caused by failures, evals, or repeated use.

Use the starter script to copy the templates into a fresh workspace:

```bash
python3 scripts/init_workspace.py ~/founder-research/my-next-idea
```
