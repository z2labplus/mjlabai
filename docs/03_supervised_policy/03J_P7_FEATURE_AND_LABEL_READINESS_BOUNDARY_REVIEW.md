# 03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW

## Scope

This document reviews
`docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
before any P7 implementation.

This is a docs-only P7 feature and label readiness boundary review gate. It
does not implement P7, execute a P7 first task, approve feature extraction,
approve label generation, approve parser / dataset reader / ingestion,
approve a training data source, approve source ingestion, approve
model-output integration, approve CLI / broad ingestion, approve real Tenhou /
real haifu / external-log / platform-data use, approve self-play or league
behavior, approve P8-P12 entry, or create model-strength evidence.

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
| docs-only boundary | `03I` defines P7 feature and label readiness boundaries before implementation. | pass |
| no P7 implementation | `03I` explicitly does not approve implementation or first-task execution. | pass |
| no feature extraction approval | `03I` says no feature extraction implementation is approved. | pass |
| no label generation approval | `03I` says no label generation implementation is approved. | pass |
| no parser / reader / ingestion approval | `03I` keeps parser, dataset reader and ingestion as separate prerequisites. | pass |
| no source approval | `03I` requires source approval later and does not approve a training source. | pass |
| no model work | `03I` does not approve architecture, dataloader, optimizer, loss, trainer, checkpoint or model artifacts. | pass |
| no real data | `03I` keeps real Tenhou, real haifu, external logs and platform data unapproved. | pass |
| no later-stage entry | `03I` keeps self-play, league and P8-P12 unapproved. | pass |
| no strength claim | `03I` evidence grade is boundary definition evidence only. | pass |

Review finding:

```text
03I scope is correct.
```

## Feature Readiness Boundary Review

`03I` covers the required future feature extraction approval prerequisites:

- `source_id` and source category.
- source rights, privacy and platform terms.
- parser / reader / ingestion status.
- schema version and feature version.
- feature family list.
- public-information-only policy.
- hidden-information exclusion.
- future-information leakage policy.
- turn / action timing boundary.
- seat / round / score / hand / discard / call / riichi / dora visibility
  boundary.
- derived feature policy.
- raw vs derived storage policy.
- train / validation split leakage policy.
- validation command plan.
- evidence log and risk register update plan.
- human / Web ChatGPT approval.
- explicit first unchecked `docs/10_next/10_NEXT.md` implementation task.

Review finding:

```text
Feature readiness boundary is sufficient for a pre-implementation boundary.
No feature extraction implementation is approved.
```

## Label Readiness Boundary Review

`03I` covers the required future label generation approval prerequisites:

- label source policy.
- allowed candidate label types.
- forbidden label types.
- human-authored label boundary.
- generated label boundary.
- model-output label boundary.
- action imitation label boundary.
- value / reward target boundary.
- future outcome leakage policy.
- hidden-information leakage policy.
- train / test leakage policy.
- label provenance.
- label versioning through label version evidence requirements.
- label validation.
- label evidence and risk review.
- human / Web ChatGPT approval.
- explicit first unchecked `docs/10_next/10_NEXT.md` implementation task.

Review finding:

```text
Label readiness boundary is sufficient for a pre-implementation boundary.
No label generation implementation is approved.
```

## Candidate Feature Families Review

`03I` lists the required candidate feature families:

- round / honba / riichi-stick context.
- seat / dealer / turn index.
- visible hand tile counts.
- visible discard pond.
- visible calls / melds.
- visible dora indicators.
- score / placement context.
- legal action mask candidate.
- previous action context.
- synthetic-only provenance indicators.

Each row is candidate-only, marks implementation as not allowed now, and
records source dependency, hidden-information risk, leakage risk and required
conditions before implementation.

Review finding:

```text
Candidate feature families are safe as planning-only rows.
```

## Candidate Label Families Review

`03I` lists the required candidate label families:

- action imitation label.
- discard choice label.
- call / no-call label.
- riichi / no-riichi label.
- legal action target label.
- synthetic smoke label.
- future value / reward target.
- future ranking / placement target.
- generated pseudo-label.
- human-authored annotation label.

Each row is candidate-only, marks implementation as not allowed now, and
records source dependency, leakage risk and required conditions before
implementation. No label family is approved for generation.

Review finding:

```text
Candidate label families are safe as planning-only rows.
```

## Forbidden Feature / Label Scope Review

`03I` explicitly forbids:

- hidden opponent hands.
- wall order and unrevealed future draws.
- future discards, future calls and future riichi declarations.
- final score or final placement as a decision-time feature.
- information unavailable to the acting player.
- labels from unapproved real data.
- labels from model outputs before a model-output label policy exists.
- labels from self-play or league outputs before P8 / P10 approval.
- labels requiring parser, reader or ingestion before those are approved.
- labels implying training data approval without source approval.
- any feature or label from real Tenhou, real haifu, external logs or platform
  data before source-specific approval.
- account, session, cookie, token or online-platform private data.
- third-party binaries, weights, params, checkpoints or snapshots as feature
  or label sources without later lawful artifact review.

Review finding:

```text
Forbidden feature / label scope is strict enough for the current review gate.
```

## Dependency Map Review

`03I` requires this dependency order:

```text
data/source readiness inventory
-> source approval
-> parser / reader / ingestion boundary
-> replay schema
-> feature boundary
-> label boundary
-> train / validation split policy
-> leakage policy
-> evidence / risk update plan
-> future implementation proposal
-> approval decision
-> exact implementation task in docs/10_next/10_NEXT.md
```

The document states that if any dependency is missing, implementation remains
blocked.

Review finding:

```text
Dependency map is correct and conservative.
```

## Feature / Label Risk Review

`03I` covers the required feature and label risks:

- hidden-information leakage.
- future-information leakage.
- train/test leakage.
- labels from unapproved source.
- synthetic fixture mistaken as training source.
- docs context mistaken as data.
- generated labels mistaken as ground truth.
- model outputs used too early.
- feature extraction creeps into parser / ingestion.
- label generation creeps into training.
- P7 feature/label boundary mistaken for implementation approval.
- model-strength overclaim.
- P8/P10 stage creep.

Mitigations are conservative: require source approval, public-information-only
checks, hidden/future-info exclusion, split policy, evidence/risk updates,
review gates and explicit `10_NEXT` implementation tasks.

Review finding:

```text
Feature / label risks and mitigations are sufficient for this review gate.
```

## Evidence Requirements Review

`03I` requires future P7 feature / label evidence to record:

- `source_id`.
- schema version.
- feature version.
- label version.
- feature family.
- label family.
- public-information-only validation.
- hidden-information exclusion validation.
- future-information exclusion validation.
- train / validation split validation.
- provenance.
- validation commands.
- evidence log reference.
- risk register reference.
- known exclusions.
- explicit non-evidence warning.

The evidence grade in `03I` is:

```text
P7 feature and label readiness boundary definition evidence only.
```

Review finding:

```text
Evidence requirements are sufficient and conservative.
```

## Readiness Vocabulary Review

`03I` defines the required readiness vocabulary:

- `docs_boundary_defined`
- `not_approved_for_implementation`
- `blocked_by_missing_source_approval`
- `blocked_by_missing_parser_reader_ingestion`
- `blocked_by_missing_feature_boundary_review`
- `blocked_by_missing_label_boundary_review`
- `blocked_by_leakage_policy`
- `requires_human_web_chatgpt_approval`
- `implementation_allowed_only_after_explicit_10_NEXT_task`

`03I` states that none of these statuses means current feature extraction
approval or current label generation approval.

Review finding:

```text
Readiness vocabulary is safe and cannot be read as implementation approval.
```

## Governance Synchronization Review

Reviewed governance and tracking documents are consistent with `03I`:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/07_development_execution/07A_MILESTONES.md`

The synchronized state is:

- P7 implementation is not approved.
- P7 first-task execution is not approved.
- feature extraction is not approved.
- label generation is not approved.
- parser / reader / ingestion is not approved.
- training data source is not approved.
- source ingestion is not approved.
- P8-P12 entry is not approved.
- next task is docs-only.
- no model-strength claim is made.
- no real-data approval is made.
- no training approval is made.

Review finding:

```text
Governance synchronization is consistent.
```

## Validation Results

Required validation for this docs-only review:

```text
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Validation status is recorded in the task completion summary and governance
updates for this review.

Result:

```text
pass
```

## Review Decision

```text
Review can close.
```

No blocker was found. `03I` is sufficiently conservative and auditable for the
current P7 feature and label readiness boundary review gate.

## Next Task Recommendation

Recommended next task:

```text
Define P7 supervised-learning risk and evidence taxonomy before implementation.
```

Rationale:

- P7 has now defined and reviewed scope, data/source readiness and feature /
  label readiness boundaries.
- The next safest P7-only step is to define a P7 risk and evidence taxonomy so
  later proposals cannot confuse boundary docs, source approval, feature
  extraction, label generation, training, model-output integration or strength
  evidence.
- This next task must remain docs-only.
- It must not implement P7, approve P7 first-task execution, add production
  code, tests, fixtures, parser, dataset reader, ingestion, feature
  extraction, label generation, training, model-output integration, real data,
  CLI, self-play, league or P8-P12 work.

## Taxonomy Status

`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
defines the recommended P7 risk and evidence taxonomy. The next task is a
docs-only review of that taxonomy before any P7 implementation proposal.

That taxonomy definition does not approve P7 implementation, P7 first-task
execution, source approval, source ingestion, parser, dataset reader,
ingestion, feature extraction, label generation, training, real data,
model-output integration, CLI, self-play, league, model-strength claims or
P8-P12 entry.

## Evidence Grade

```text
P7 feature and label readiness boundary review evidence only.
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
