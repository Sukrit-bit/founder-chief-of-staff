# Protocol Change

Date: 2026-06-17
Changed artifact: Agent operating rule

## Trigger

The agent summarized a customer conversation without updating project state.

## Previous Behavior

The agent could answer well enough in chat and stop.

## New Rule

If a founder input changes project state, the agent must identify which durable artifact should change.

At minimum, it should check:

- current dashboard;
- current working state;
- artifact index;
- decision queue;
- pattern register;
- failure-mode register.

## Files That Would Change In A Real Workspace

- `00_Context/Current_Decision_Dashboard.md`
- `00_Context/Project_Artifact_Index.md`
- `06_Decision_Log/Active_Decision_Queue.md`
- `06_Decision_Log/Failure_Mode_Register.md`
- `01_Themes/[Theme]/Pattern_Register.md`
- `07_Source_Material/[Source_Note].md`

## Verification

The improved next run creates a source/evidence artifact, updates the decision queue, and names the next evidence needed.

