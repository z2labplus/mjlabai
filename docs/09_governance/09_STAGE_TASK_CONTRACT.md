# 09_STAGE_TASK_CONTRACT

## Current stage

Project setup / rule-load verification.

## AI role

Rule follower + project documentation assistant.

## Stage goal

Verify that the AI has loaded project rules before any project execution begins.

## Inputs

- AGENTS.md
- docs/00_HANDOFF.md
- docs/00_DOCS_INDEX.md
- docs/10_next/10_NEXT.md

## Do

- Read the required project rules.
- State the current stage and current next task.
- State the north-star target.
- Wait for the user to enter the goal-and-benchmark stage after rule-load passes.

## Do not

- Do not write code.
- Do not create model/training scripts.
- Do not design a full architecture yet.
- Do not scrape data.
- Do not create Tenhou automation or integration.
- Do not modify files during the rule-load test.

## Task boundary

Only confirm rules and readiness until the rule-load test passes.

## Output files

None during rule-load test. After the user enters the next stage, update goal-and-benchmark files according to `10_NEXT.md`.

## Acceptance criteria

- AI can summarize the north-star target.
- AI can identify the current stage.
- AI can identify what is forbidden.
- AI can identify the first task in `docs/10_next/10_NEXT.md`.

## Document sync requirements

After any real task completes, update:

- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/00_HANDOFF.md`

## Only next step

Run rule-load verification, then create the goal-and-benchmark stage contract and first minimal benchmark-definition task.
