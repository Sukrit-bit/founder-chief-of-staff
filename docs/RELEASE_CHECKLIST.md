# Release Checklist

Run:

```bash
python3 scripts/release_audit.py
```

The release is not ready unless all of these are true:

| Check | Requirement |
|---|---|
| Identity | Product name, repository slug, metadata, URLs, and current docs say Founder Chief of Staff |
| Ninety-second scan | A cold reader understands the job before studying the architecture |
| External writing | The declared public surfaces pass `scripts/external_style_audit.py`; the internal style marker is absent |
| Evaluator self-test | The external-style evaluator rejects the old marker-plus-jargon fixture and accepts the plain-language fixture |
| Runnable proof | Workspace generation, integrity checks, and positive and negative event evals pass |
| Claim boundaries | Runnable, synthetic, agent-dependent, and private evidence remain distinct |
| Agent entry | Codex, Claude Code, and portable instructions agree on role and boundaries |
| Canonical state | Registry, control map, dashboard, working state, decisions, CRM, and tasks have distinct jobs |
| Automation | Every recurring workflow defines inputs, writes, inference limits, stop conditions, and verification |
| Correction control | A systemic remedy requires a shared-control change, positive test, negative test, and proof status |
| Data handling | No client work, private relationships, credentials, or confidential company context are published |
| Responsive surface | Landing page has no horizontal overflow on desktop or mobile |
| External proof | CI and Pages deployment pass for the exact published commit |

## Positioning

```text
Founder Chief of Staff gives an AI agent the memory and discipline to keep
important founder work moving without repeating known mistakes.
```

Do not reduce it to:

```text
AI notes, a prompt pack, or a market-research folder.
```
