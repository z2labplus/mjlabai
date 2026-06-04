# 12B_POST_P5_TRANSITION_REVIEW

## Scope

This document records the post-P5 transition review after the final P5 closure
review gate.

P5 is closed for the current synthetic/local evaluation groundwork scope in:

```text
docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md
```

This transition review decides whether the project may begin a separate
docs-only task to define P6 scope, entry criteria and first task. It does not
execute P6.

This review does not:

- approve P6 implementation.
- approve P7-P12 entry.
- generate a P6 implementation prompt.
- add production code.
- add tests or fixtures.
- implement replay schema, dataset schema, feature extraction, label
  generation, file ingestion or data pipelines.
- implement metrics.
- change metric registry code, metric units, metric directions or registry
  definitions.
- change evidence taxonomy definitions.
- change promotion criteria.
- add CLI, broad file ingestion, latency measurement or fixed-position
  exact-match computation.
- add a legal-action checker, canonicalizer, broad evaluator or production
  evaluator logic.
- connect model output.
- call model APIs, OpenAI APIs, third-party binaries, Akochan `system.exe` or
  `libai.so`.
- read real Tenhou, real haifu, external logs, platform data or online account
  data.
- train, tune, self-play, run league or runner behavior.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game evidence,
  LuckyJ `10.68` comparison or candidate-promotion evidence.

## Review Questions

| question | review_answer | blocker | notes |
|---|---|---|---|
| Can P5 current synthetic/local evaluation groundwork be treated as closed? | yes | none | `05X` records that P5 can close for current scope. |
| Is the next step allowed to execute P6-P12 directly? | no | none | P5 closure is not P6 entry approval. |
| Is a separate transition review required before any P6 task? | yes | none | This document is that transition review. |
| Can the project start defining P6 scope, entry criteria and first task? | yes, as a docs-only task | none | The next task may define P6 scope/entry criteria/first task without implementing P6. |
| Can the next task implement replay schemas, data ingestion or pipelines? | no | none | Implementation must wait until P6 scope and entry criteria are explicitly approved. |
| Can the next task use real Tenhou, real haifu, external logs or platform data? | no | none | Data-source and compliance boundaries must be defined before any ingestion. |
| Can the next task train, tune, self-play or run league behavior? | no | none | Later stages require separate gates. |

## Post-P5 Transition Review Goal

The goal of this transition review is to prevent two failure modes:

1. P5 continuing indefinitely through more schema/review churn after it has met
   current-scope closure criteria.
2. P5 closure being mistaken for permission to jump directly into P6-P12
   implementation.

This review creates a narrow bridge:

```text
P5 closed for current scope
-> post-P5 transition review
-> docs-only P6 scope / entry criteria / first-task definition
-> later review before any P6 implementation
```

## Inputs Reviewed

- `AGENTS.md`.
- `README.md`.
- `docs/00_HANDOFF.md`.
- `docs/00_DOCS_INDEX.md`.
- `docs/10_next/10_NEXT.md`.
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`.
- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`.
- `docs/07_development_execution/07A_MILESTONES.md`.
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`.
- `docs/07_development_execution/07B_TASK_BACKLOG.md`.
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`.
- `docs/09_governance/09_EVIDENCE_LOG.md`.
- `docs/09_governance/09_RISK_REGISTER.md`.
- `docs/09_governance/09_CHANGELOG.md`.

## Output Boundary

This review allows exactly one next step:

```text
Define P6 data-system scope, entry criteria and first task before implementation.
```

That next task must be docs-only. It may define:

- P6 purpose and north-star connection.
- P6 allowed inputs.
- P6 forbidden inputs.
- P6 entry criteria.
- P6 exit criteria.
- P6 first task candidate.
- P6 risk review.
- P6 evidence requirements.
- P6 non-entry boundaries for P7-P12.

That next task must not implement:

- replay schema code.
- dataset readers.
- real haifu ingestion.
- Tenhou platform integration.
- external log ingestion.
- data pipelines.
- feature extraction.
- label generation.
- model-output integration.
- CLI or broad file ingestion.
- training, tuning, self-play, league or runner behavior.

## P6 Candidate Scope For Later Definition

The project roadmap names P6 as:

```text
Data system.
```

The roadmap goal is:

```text
Build replay, feature, label and quality pipelines for training and evaluation.
```

The roadmap gate is:

```text
Supervised training and offline evaluation datasets can be generated.
```

This transition review does not approve that implementation. It only approves
creating a P6 scope definition task.

The likely first P6 definition task should narrow P6 to documentation first:

- define replay/data-system scope.
- define legal and provenance guardrails.
- define synthetic/local starter boundary.
- define whether `docs/02_data_system/02B_REPLAY_SCHEMA.md` must be revised
  before any code.
- define what evidence is required before any real data or external log path.

## Forbidden Scope For The Next Task

The next task must explicitly forbid:

- training.
- tuning.
- self-play.
- league.
- runner or match harness behavior.
- real Tenhou.
- Tenhou account/session/platform automation.
- real haifu ingestion.
- external log ingestion.
- platform data ingestion.
- model-output integration.
- third-party binaries/artifacts.
- Akochan `system.exe`.
- `libai.so`.
- unknown model weights, `*.pth`, `*.pt`, checkpoints or snapshots.
- CLI.
- broad file ingestion.
- P7-P12.
- model-strength claims.
- Tenhou ranked claims.
- stable-dan ranked-game claims.
- LuckyJ `10.68` comparison claims.
- candidate-promotion claims.

## Evidence Grade

Current evidence grade:

```text
Post-P5 transition review evidence only.
```

This is not:

- P6 implementation approval.
- P7-P12 entry approval.
- production data-system evidence.
- replay schema implementation evidence.
- data-ingestion evidence.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.

## Transition Decision

```text
The project may start a docs-only task to define P6 data-system scope, entry
criteria and first task before implementation.
```

This is a limited planning approval. It does not approve P6 implementation.

## Next Task Recommendation

The next task should be:

```text
Define P6 data-system scope, entry criteria and first task before implementation.
```

That task must remain docs-only and must not implement data ingestion, replay
schema code, training, self-play, league, real Tenhou, model-output integration,
CLI, broad file ingestion or model-strength claims.

## Verification

Recommended validation:

```bash
git diff --check
```
