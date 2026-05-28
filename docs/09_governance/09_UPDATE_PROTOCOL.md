# 09_UPDATE_PROTOCOL

## Purpose

Ensure every discussion updates the correct documents.

## Mapping

| Discussion type | Update files |
|---|---|
| Project goal / benchmark | `01_goal_benchmark/*`, `00_HANDOFF.md`, `09_CHANGELOG.md` |
| Data source / schema | `02_data_system/*`, `09_EVIDENCE_LOG.md`, `09_RISK_REGISTER.md` |
| Supervised model | `03_supervised_policy/*`, `08B_MODEL_CARD.md` |
| RL / self-play | `04_rl_selfplay/*`, `08A_EXPERIMENT_LOG.md` |
| Evaluation / benchmark | `05_evaluation/*`, `09_EVIDENCE_LOG.md` |
| Inference / engine | `06_engine_inference/*`, `07B_TASK_BACKLOG.md` |
| Development task | `07_development_execution/*`, `10_NEXT.md` |
| Experiment result | `08_experiment_analysis/*`, `05_evaluation/*` |
| Risk / compliance | `09_governance/*` |

## Always update after a real task

```text
docs/10_next/10_NEXT.md
docs/09_governance/09_CHANGELOG.md
docs/00_HANDOFF.md
```

## Rule

If a discussion produces a decision, it must be written into exactly one primary stage file and then reflected in handoff/changelog/next.
