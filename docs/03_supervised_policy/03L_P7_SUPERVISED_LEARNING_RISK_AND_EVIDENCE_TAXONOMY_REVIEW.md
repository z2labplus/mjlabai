# 03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW

## Scope

This document reviews
`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
before any P7 implementation.

This is a docs-only P7 risk and evidence taxonomy review gate. It does not
implement P7, execute a P7 first task, approve a training data source, approve
source ingestion, approve parser / dataset reader / ingestion, approve feature
extraction, approve label generation, approve supervised dataset construction,
approve model architecture / dataloader / optimizer / loss / trainer /
checkpoint work, approve model-output integration, approve CLI / broad
ingestion, approve real Tenhou / real haifu / external-log / platform-data
use, approve self-play or league behavior, approve P8-P12 entry, or create
model-strength evidence.

## Reviewed Artifacts

Primary P7 artifacts:

- `AGENTS.md`
- `README.md`
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md`
- `docs/03_supervised_policy/03_SUPERVISED_POLICY.md`
- `docs/03_supervised_policy/03A_MODEL_ARCHITECTURE.md`
- `docs/03_supervised_policy/03B_TRAINING_OBJECTIVES.md`
- `docs/03_supervised_policy/03C_KEY_DECISION_HEADS.md`
- `docs/03_supervised_policy/03D_OFFLINE_METRICS.md`
- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
- `docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
- `docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
- `docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`

P6 / data-system closure context:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`

P5 / evaluation context:

- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md`

Read-only implementation context:

- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Governance and tracking:

- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

All `03A`-`03D` context files exist. No context replacement document was
needed.

## Scope Review

| review_item | finding | status |
|---|---|---|
| docs-only taxonomy | `03K` defines P7 supervised-learning risk and evidence taxonomy before implementation. | pass |
| no P7 implementation | `03K` explicitly does not approve implementation or first-task execution. | pass |
| no source approval | `03K` keeps source approval and training-data approval separate from readiness evidence. | pass |
| no parser / reader / ingestion approval | `03K` keeps parser, dataset reader, ingestion, CLI and broad ingestion unapproved. | pass |
| no feature / label approval | `03K` keeps feature extraction and label generation unapproved. | pass |
| no model work | `03K` keeps architecture, dataloader, optimizer, loss, trainer, checkpoint and model artifacts unapproved. | pass |
| no real data | `03K` keeps real Tenhou, real haifu, external logs and platform data unapproved. | pass |
| no later-stage entry | `03K` keeps self-play, league and P8-P12 unapproved. | pass |
| no strength claim | `03K` classifies itself as taxonomy-definition evidence only. | pass |

Review finding:

```text
03K scope is correct.
```

## Risk Taxonomy Review

`03K` covers the required P7 risk categories:

- scope / stage creep risk.
- source approval risk.
- training-data approval risk.
- parser / reader / ingestion creep risk.
- feature extraction approval ambiguity risk.
- label generation approval ambiguity risk.
- hidden-information leakage risk.
- future-information leakage risk.
- train / validation / test leakage risk.
- model-output integration too early risk.
- real-data / platform-data leakage risk.
- account / cookie / token risk.
- third-party binary / weights / params risk.
- training-before-approval risk.
- model artifact provenance risk.
- metric / evidence overclaim risk.
- model-strength overclaim risk.
- LuckyJ / Tenhou / stable-dan comparison overclaim risk.
- P8/P10/P12 stage creep risk.
- candidate promotion overclaim risk.

Each row includes `risk_category`, `risk_description`, `current_status`,
`mitigation`, `required_before_implementation`, `owner_doc_or_followup`,
`blocker_if_unresolved` and `notes`.

Review finding:

```text
Risk taxonomy is sufficient and conservative for the current review gate.
```

## Evidence Taxonomy Review

`03K` defines the required evidence types / grades:

- docs-only P7 scope evidence.
- data/source readiness evidence.
- feature/label readiness boundary evidence.
- risk/evidence taxonomy evidence.
- future proposal evidence.
- future approval-decision evidence.
- future synthetic/local smoke implementation evidence.
- future feature/label schema smoke evidence.
- future training-run engineering evidence.
- future offline evaluation evidence.
- future model-strength evidence candidate.
- future Tenhou validation evidence candidate.

Each row includes `evidence_type`, `allowed_interpretation`,
`forbidden_interpretation`, `implementation_allowed`, `training_allowed`,
`model_strength_claim_allowed`, `P8_P12_entry_allowed`,
`required_supporting_artifacts` and `notes`.

Review finding:

```text
Evidence taxonomy is sufficient and keeps interpretation boundaries clear.
```

## Current P7 Evidence Classification Review

`03K` classifies the current P7 evidence chain correctly:

- `03E`: docs-only scope / entry criteria / first-task definition evidence.
- `03F`: docs-only scope review evidence.
- `03G`: data/source readiness inventory evidence.
- `03H`: data/source readiness inventory review evidence.
- `03I`: feature/label readiness boundary definition evidence.
- `03J`: feature/label readiness boundary review evidence.
- `03K`: risk/evidence taxonomy definition evidence.

The classification explicitly says the current P7 evidence is not P7
implementation evidence, training evidence, source approval evidence, feature
extraction evidence, label generation evidence, model-strength evidence,
Tenhou evidence, LuckyJ comparison evidence or candidate promotion evidence.

Review finding:

```text
Current P7 evidence classification is accurate.
```

## Future Evidence Requirements Review

`03K` defines future evidence fields for later implementation, training or
evaluation tasks:

- `source_id`.
- source approval status.
- source rights / license / terms.
- parser / reader version.
- ingestion version.
- schema version.
- feature version.
- label version.
- training dataset id.
- train / validation / test split policy.
- leakage checks.
- model architecture id.
- training config id.
- random seed.
- dependency versions.
- hardware / runtime if relevant.
- validation commands.
- metric outputs.
- evaluation envelope.
- artifact checksum.
- failure modes.
- known exclusions.
- explicit non-evidence warning.

Review finding:

```text
Future P7 evidence requirements are sufficient for pre-implementation governance.
```

## Evidence-To-Claim Mapping Review

`03K` safely maps evidence to claims:

- docs-only boundary evidence supports only boundary / planning claims.
- source readiness evidence supports only readiness inventory claims.
- source approval evidence supports source-use claims only after separate
  approval.
- synthetic smoke evidence supports only engineering smoke claims.
- training run evidence supports only training-run engineering claims.
- offline evaluation evidence may support offline performance claims only if
  metrics and protocol are approved.
- model league evidence may support relative model comparison only if P10 is
  approved.
- Tenhou validation evidence can support Tenhou ranked claims only under P12.
- LuckyJ comparison requires an explicit comparison protocol, data, sample size
  and stage approval.

Review finding:

```text
Evidence-to-claim mapping is safe and blocks overclaiming.
```

## Forbidden Evidence Interpretations Review

`03K` explicitly forbids:

- docs evidence interpreted as model strength.
- P6 synthetic fixture interpreted as training data approval.
- P7 data/source readiness interpreted as source approval.
- feature/label boundary interpreted as implementation approval.
- risk taxonomy interpreted as approval decision.
- smoke tests interpreted as model performance.
- offline metric planning interpreted as actual offline performance.
- training logs interpreted as Tenhou strength.
- self-play wins interpreted as Tenhou strength without P10 / P12.
- current P7 artifacts interpreted as LuckyJ `10.68` comparison or candidate
  promotion.

Review finding:

```text
Forbidden evidence interpretations are strict enough for the current P7 gate.
```

## Risk / Evidence Dependency Map Review

`03K` defines the dependency order:

```text
P7 scope / entry criteria
-> data/source readiness
-> feature/label readiness
-> risk/evidence taxonomy
-> implementation proposal
-> proposal review
-> approval decision
-> exact minimal implementation
-> implementation review
-> evidence/risk update
-> future training / evaluation gates
```

It also states that if any predecessor is missing, ambiguous or rejected, later
implementation must remain blocked or deferred.

Review finding:

```text
Risk / evidence dependency map is correct and conservative.
```

## Evidence Log / Risk Register Update Requirements Review

`03K` requires future P7 tasks to keep these governance files synchronized:

- `docs/09_governance/09_EVIDENCE_LOG.md`.
- `docs/09_governance/09_RISK_REGISTER.md`.
- `docs/09_governance/09_DECISION_RECORD.md`.
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`.
- `docs/10_next/10_NEXT.md`.
- `docs/00_HANDOFF.md`.

Review finding:

```text
Governance update requirements are sufficient.
```

## P8-P12 Non-Entry Boundary Review

`03K` explicitly keeps later stages unapproved:

- no P8 reinforcement learning.
- no P9 search / risk model implementation.
- no P10 model league.
- no P11 large-scale training.
- no P12 Tenhou validation.

It also states that future P7 closure does not automatically approve P8-P12
and that each later stage needs a separate transition review, scope
definition, entry criteria, risk review, evidence taxonomy and first-task
approval.

Review finding:

```text
P8-P12 non-entry boundary is sufficient.
```

## Governance Synchronization Review

The following governance docs were reviewed and synchronized:

- `docs/00_HANDOFF.md`.
- `docs/00_DOCS_INDEX.md`.
- `docs/10_next/10_NEXT.md`.
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`.
- `docs/09_governance/09_EVIDENCE_LOG.md`.
- `docs/09_governance/09_RISK_REGISTER.md`.
- `docs/09_governance/09_CHANGELOG.md`.
- `docs/09_governance/09_DECISION_RECORD.md`.
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`.
- `docs/07_development_execution/07B_TASK_BACKLOG.md`.
- `docs/07_development_execution/07A_MILESTONES.md`.

Governance synchronization confirms:

- P7 implementation is still not approved.
- P7 first-task execution is still not approved.
- training data source is still not approved.
- source ingestion is still not approved.
- parser / reader / ingestion is still not approved.
- feature extraction is still not approved.
- label generation is still not approved.
- P8-P12 is still unapproved.
- the next task is a docs-only follow-up.
- no model-strength claim is made.
- no real-data approval exists.
- no training approval exists.

Special check:

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md now points to the current next docs-only P7 follow-up and no longer treats the old taxonomy definition task as pending.
```

Review finding:

```text
Governance synchronization is consistent.
```

## Validation Results

Validation commands:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Result:

```text
pass
```

## Review Decision

```text
Review can close.
```

No blocker was found. `03K` is sufficiently conservative, complete and
auditable for the current P7 supervised-learning risk and evidence taxonomy
review gate.

## Next Task Recommendation

Recommended next task:

```text
Define minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation.
```

This next task must be a docs-only proposal definition. It must not implement
P7, approve P7 first-task execution, create fixtures, add tests, add production
code, construct a supervised dataset, approve a source, approve source
ingestion, approve parser / dataset reader / ingestion, implement feature
extraction, implement label generation, train, tune, self-play, run league,
read real Tenhou / real haifu / external logs / platform data, add CLI /
broad ingestion, integrate model outputs, approve model-strength claims or
enter P8-P12.

## Evidence Grade

```text
P7 supervised-learning risk and evidence taxonomy review evidence only.
```

## Explicit Non-Evidence

This review is not:

- P7 implementation.
- P7 first-task execution.
- P8-P12 entry approval.
- training.
- tuning.
- self-play.
- league.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- parser.
- dataset reader.
- data ingestion.
- feature extraction implementation.
- label generation implementation.
- source approval.
- training-data approval.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
