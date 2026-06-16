# Pilot Evidence: Engagement 01

Date: 2026-06-17
Evidence maturity before pilot: Problem candidate
Decision this should support: Continue / Narrow / Experiment / Park / Kill

## Pilot Context

Synthetic customer: mid-market SaaS company.

Service sold: vendor-risk review.

Channel: partner introduction.

Team: founder plus one domain expert.

## Workflow Map

```text
request
-> vendor questionnaire
-> missing-info list
-> risk register
-> expert review
-> client report
-> remediation tracker
```

## What The System Did

- Converted raw questionnaire answers into a structured fact matrix.
- Flagged missing facts.
- Drafted a first-pass risk register.
- Created a client-facing report outline.
- Proposed remediation owners.

## What Humans Reviewed

- Risk severity.
- Legal or compliance interpretation.
- Final recommendation language.
- Escalation items.

## Evidence

| Signal | Evidence | Strength |
|---|---|---|
| Workflow repeatability | Intake, missing-info, risk register, and report steps appear reusable. | Medium |
| Time saved or quality improved | First report draft took less manual assembly, but expert review still dominated. | Medium |
| Buyer or user pull | Client asked whether this could run quarterly. | Medium |
| Follow-on demand | Remediation tracking became a natural next step. | Medium |
| Productizable module | Fact matrix and missing-info generator look reusable. | Strong |

## Path Scoring

| Path | Score | Evidence |
|---|---:|---|
| AI-native services firm | 2 | Buyer trusted expert-led delivery. |
| Consultant software | 2 | Internal workflow looked reusable. |
| Buyer-facing program manager | 1 | Quarterly use was suggested but not proven. |
| Combined loop | 2 | Software plus expert escalation felt plausible. |

## Decision

Decision: experiment again.

Next change: build the missing-info generator and remediation tracker before Engagement 02.

