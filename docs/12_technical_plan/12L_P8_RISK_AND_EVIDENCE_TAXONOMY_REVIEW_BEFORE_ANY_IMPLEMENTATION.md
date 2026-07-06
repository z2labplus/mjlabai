# 12L_P8_RISK_AND_EVIDENCE_TAXONOMY_REVIEW_BEFORE_ANY_IMPLEMENTATION

## Scope

This document reviews:

```text
docs/12_technical_plan/12K_P8_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_ANY_IMPLEMENTATION.md
```

This is a docs-only P8 risk/evidence taxonomy review gate. It does not:

- approve P8 entry.
- approve P8 implementation.
- define or approve a P8 implementation prompt.
- approve a P8 first executable task.
- approve P9-P12 entry.
- add or modify production code.
- add or modify tests.
- add fixtures or data files.
- approve source approval or source ingestion.
- read real data, real Tenhou, real haifu, external logs or platform data.
- approve broad file ingestion or CLI.
- approve feature extraction, label generation or dataset construction.
- approve training, tuning, evaluation, self-play, league or RL execution.
- approve model-output integration.
- produce model-strength evidence.
- produce Tenhou ranked evidence.
- produce stable-dan evidence.
- produce LuckyJ `10.68` comparison.
- produce candidate-promotion evidence.

North-star relationship: this review helps the long-term Tenhou stable-dan
`> 10.68` target only by checking that future P8 work cannot overclaim
planning artifacts as training, self-play, model-strength or target-comparison
evidence.

## Reviewed Artifacts

Primary reviewed artifact:

- `docs/12_technical_plan/12K_P8_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_ANY_IMPLEMENTATION.md`

Context artifacts:

- `docs/12_technical_plan/12J_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_REVIEW.md`
- `docs/12_technical_plan/12I_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_AFTER_P8_P12_TRANSITION_SCOPE_REVIEW.md`
- `docs/12_technical_plan/12H_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_REVIEW.md`
- `docs/12_technical_plan/12G_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK.md`
- `docs/12_technical_plan/12F_POST_FULL_P7_TRANSITION_REVIEW.md`
- `docs/03_supervised_policy/03BL_FINAL_FULL_P7_CLOSURE_REVIEW.md`
- `docs/03_supervised_policy/03BK_P7_FULL_SCOPE_RISK_SOURCE_RIGHTS_AND_EVIDENCE_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
- `docs/03_supervised_policy/03BJ_P7_FULL_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_REVIEW_AFTER_CLOSURE_CRITERIA_REVIEW.md`
- `docs/03_supervised_policy/03BI_P7_FULL_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
- `docs/03_supervised_policy/03BH_FULL_P7_CLOSURE_CRITERIA_REVIEW_AFTER_PARSER_READER_SMOKE_EXTENSION_CURRENT_SCOPE_ACCEPTANCE.md`
- `docs/03_supervised_policy/03BG_FULL_P7_CLOSURE_CRITERIA_AFTER_PARSER_READER_SMOKE_EXTENSION_CURRENT_SCOPE_ACCEPTANCE.md`
- `docs/03_supervised_policy/03BE_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_EXTENSION_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
- `docs/03_supervised_policy/03BD_P7_PARSER_READER_SMOKE_EXTENSION_IMPLEMENTATION_REVIEW_AFTER_BLOCKER_FIX.md`
- `docs/03_supervised_policy/03AW_P7_FULL_SCOPE_EXPANSION_PLAN_AFTER_CURRENT_SCOPE_ACCEPTANCE.md`
- `docs/03_supervised_policy/03AX_P7_FULL_SCOPE_EXPANSION_PLAN_REVIEW_AFTER_CURRENT_SCOPE_ACCEPTANCE.md`
- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

Read-only implementation context:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`
- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`

## Full P7 / P8 Scope Recap Review

Review result: sufficient.

`12K` correctly records:

- Full P7 closed only for the documented P7 supervised-learning scope.
- `12F`, `12G` and `12H` established P8-P12 docs-only transition planning.
- `12I` defined P8 scope, entry criteria and the first planning task.
- `12J` reviewed `12I` and recorded `A. Review can close`.
- P8 remains docs-only planning.
- P8 entry remains unapproved.
- P8 implementation remains unapproved.
- P9-P12 remain unapproved.

No recap item implies P8 entry, P8 implementation, self-play, RL execution,
training, evaluation, real-data use, model-output integration or P9-P12 entry.

## P8 Non-Approval Baseline Review

Review result: sufficient.

`12K` explicitly records that the following remain unapproved or absent:

- P8 entry.
- P8 implementation.
- P8 first executable task.
- P8 implementation prompt.
- P9-P12 entry.
- self-play evidence.
- RL evidence.
- league evidence.
- training evidence.
- evaluation evidence.
- model-output evidence.
- model-strength evidence.
- real-data permission.
- source-ingestion permission.

This baseline is conservative and prevents taxonomy language from being read as
approval.

## Risk Taxonomy Review

Review result: sufficient.

`12K` defines R1-R20 and each row includes:

- `risk_id`
- `risk_name`
- `description`
- `current_status`
- `severity`
- `blocked_by`
- `required_controls`
- `evidence_required`
- `forbidden_current_action`
- `notes`

Reviewed risk families:

| risk_id | review |
|---|---|
| R1 | Scope / entry approval confusion is covered and blocked by review / later approval chain. |
| R2 | Implementation creep is covered and blocks code, tests, fixtures and data without approval. |
| R3 | Self-play / RL execution creep is covered and blocked by dependency map and approval. |
| R4 | Training / tuning creep is covered and blocked by training-data / training-run approvals. |
| R5 | Evaluation / benchmark creep is covered and blocks evaluation runner / benchmark work. |
| R6 | Model-output integration creep is covered and blocks model-output paths. |
| R7 | Model-strength overclaim is covered and blocks strength claims. |
| R8 | Source approval / source ingestion gap is covered. |
| R9 | Real-data / platform / account risk is covered. |
| R10 | Feature / label / dataset dependency ambiguity is covered. |
| R11 | Reward hacking / objective mismatch risk is covered as future RL risk. |
| R12 | Self-play collapse / overfitting risk is covered as future self-play risk. |
| R13 | Opponent-pool / league bias risk is covered and marked later-stage. |
| R14 | Reproducibility / stochasticity risk is covered. |
| R15 | Compute / resource escalation risk is covered. |
| R16 | Safety / governance / auditability mismatch is covered. |
| R17 | P9-P12 scope creep is covered. |
| R18 | Tenhou / stable-dan / LuckyJ / promotion overclaim is covered. |
| R19 | Third-party artifact / binary / model-weight risk is covered. |
| R20 | `10_NEXT` / governance drift is covered. |

No risk entry implies approval. No mitigation implies implementation. All
execution-like risks remain blocked, not started or unapproved. The taxonomy
remains planning evidence only.

## Evidence Taxonomy Review

Review result: sufficient.

`12K` defines E1-E25 and each row includes:

- `evidence_family_id`
- `name`
- `allowed_current_status`
- `future_use`
- `required_prerequisites`
- `cannot_support`
- `risk_controls`
- `notes`

Reviewed evidence families:

| evidence_family_id | review |
|---|---|
| E1 | Scope definition evidence is allowed and cannot support implementation or strength claims. |
| E2 | Scope review evidence is allowed and cannot support implementation or entry approval. |
| E3 | Risk/evidence taxonomy evidence is allowed now and cannot support implementation or strength claims. |
| E4 | Risk/evidence taxonomy review evidence is future-only until this review closes. |
| E5 | Dependency-map evidence is future-only and cannot grant execution permission. |
| E6 | Dependency-map review evidence is future-only and cannot grant implementation approval. |
| E7 | Approval-decision evidence is future-only and limited to exact next tasks. |
| E8 | Exact implementation evidence is future-only and requires approval. |
| E9 | Implementation review evidence is future-only and not acceptance by itself. |
| E10 | Test / validation evidence is limited and not strength evidence. |
| E11 | Source-rights evidence is future-only. |
| E12 | Source-ingestion evidence is future-only. |
| E13 | Training-data approval evidence is future-only. |
| E14 | Training-run evidence is future-only. |
| E15 | Self-play protocol evidence is future-only. |
| E16 | Self-play result evidence is future-only. |
| E17 | League protocol evidence is future-only and later-stage. |
| E18 | Evaluation protocol evidence is future-only. |
| E19 | Model-output integration evidence is future-only. |
| E20 | Model-strength evidence is future-only. |
| E21 | Tenhou ranked evidence is future-only. |
| E22 | Stable-dan evidence is future-only. |
| E23 | LuckyJ comparison evidence is future-only. |
| E24 | Candidate-promotion evidence is future-only. |
| E25 | Governance synchronization evidence is allowed but not technical merit or strength. |

Only docs-only planning grades are possible now. Self-play, RL, training,
evaluation, model-output, model-strength, Tenhou, stable-dan, LuckyJ and
promotion evidence do not exist now. Existing tests remain validation evidence,
not strength evidence.

## Evidence Grade Vocabulary Review

Review result: sufficient.

The vocabulary is clear and conservative:

- current `12K` grade is taxonomy definition evidence only.
- this `12L` review grade is taxonomy review evidence only.
- exact implementation evidence is not available now.
- self-play protocol/result evidence is not available now.
- evaluation/model-output/model-strength evidence is not available now.
- Tenhou/stable-dan/LuckyJ/candidate-promotion evidence is not available now.

No current evidence grade can support P8 entry, implementation, model strength,
Tenhou ranked results, stable dan, LuckyJ comparison or candidate promotion.

## Current Evidence Classification Review

Review result: sufficient.

`12K` correctly classifies current evidence:

- P7 closure evidence is historical prerequisite evidence only, not P8
  performance evidence.
- `12G` / `12H` are P8-P12 transition planning / review evidence only.
- `12I` / `12J` are P8 scope definition / review evidence only.
- `12K` is P8 risk/evidence taxonomy definition evidence only.
- accepted synthetic/local P7 smoke helpers are local guardrail validation
  evidence only.
- existing unit tests are validation evidence for exact synthetic/local code
  paths only.
- no current artifact is self-play evidence.
- no current artifact is RL evidence.
- no current artifact is model-strength evidence.
- no current artifact is Tenhou ranked evidence.
- no current artifact is stable-dan evidence.
- no current artifact is LuckyJ comparison.
- no current artifact is candidate-promotion evidence.

No blocker found.

## P8 Workstream Risk / Evidence Matrix Review

Review result: sufficient.

The matrix covers:

1. P8 scope / entry planning.
2. P8 risk/evidence taxonomy.
3. Self-play/RL dependency mapping.
4. Training dependency mapping.
5. Model-output dependency mapping.
6. Evaluation dependency mapping.
7. Real-data / source-rights dependency mapping.
8. League dependency boundary.
9. Model-strength evidence boundary.
10. P9-P12 non-entry boundary.
11. Governance / risk / evidence synchronization.

Each row records workstream, risk families, evidence required, current
evidence, current status, approval state, blocker, forbidden current scope and
next safe gate. The matrix correctly keeps self-play/RL, training, evaluation,
model-output, real-data/source, league, model-strength and P9-P12 work
unapproved.

## Model-Strength Evidence Boundary Review

Review result: sufficient.

`12K` explicitly states that no current artifact is model-strength evidence.
It requires future model-strength evidence to have:

- approved evaluation protocol.
- approved model-output path.
- approved sample definition.
- sufficient sample-size / uncertainty method.
- leakage controls.
- governance review.
- separate approval decision.

Synthetic/local smoke evidence and unit tests cannot be used as
model-strength evidence.

## Tenhou / Stable-Dan / LuckyJ / Promotion Boundary Review

Review result: sufficient.

`12K` explicitly states that no current artifact is:

- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison evidence.
- candidate-promotion evidence.

Future such evidence requires separate protocol, source approval, sample
definition, uncertainty method, leakage review and governance approval.

## Source / Real-Data / Platform Boundary Review

Review result: sufficient.

`12K` explicitly states that no current source is approved for P8 self-play,
RL, training, evaluation, real-data use or platform-data use.

Future source work requires:

- source-rights review.
- platform / privacy / account-policy review.
- source approval decision.
- ingestion boundary.
- validation protocol.
- evidence logging.

No current document authorizes real Tenhou, real haifu, external logs,
platform data, account/session/cookie/token handling or broad file ingestion.

## Self-Play / RL Boundary Review

Review result: sufficient.

`12K` explicitly states:

- no self-play is approved now.
- no RL execution is approved now.
- no opponent pool is approved now.
- no league is approved now.
- no training loop is approved now.

Future self-play/RL work requires:

- dependency map.
- risk/evidence review.
- source/model-output/evaluation boundary.
- approval decision.
- exact implementation scope.
- validation and review.

## Stop Conditions Review

Review result: sufficient.

`12K` requires stopping if any task:

- implies P8 entry approval.
- implies P8 implementation approval.
- generates an implementation prompt.
- runs training or tuning.
- runs self-play.
- runs league.
- uses real data.
- uses Tenhou / haifu / platform data.
- approves source ingestion.
- emits model-output integration.
- claims model strength.
- claims Tenhou / stable-dan / LuckyJ / promotion evidence.
- enters P9-P12.
- creates production code.
- creates tests, fixtures or data.
- downloads or uses unknown model artifacts.
- vendors third-party binaries.
- calls Akochan `system.exe`, `libai.so` or another third-party binary.
- changes `10_NEXT` to an implementation task without approval.

These stop conditions are sufficient for the current review gate.

## Candidate Next Directions Review

Review result: sufficient.

`12K` evaluates:

- Review P8 risk and evidence taxonomy before any implementation.
- Define P8 self-play / RL dependency map before any implementation.
- Define P8 training / model-output / evaluation dependency map.
- Prepare P8 entry approval decision.
- Draft P8 implementation proposal.
- Start P8 implementation.
- Start training / tuning.
- Start self-play / league.
- Start real-data / Tenhou work.
- Start model-output integration / model-strength evidence work.
- Define P9-P12 scope.

The selected next direction in `12K` was this review gate. Since this review
finds no blocker, the next safe task is:

```text
Define P8 self-play / reinforcement-learning dependency map before any implementation.
```

That next task must still be docs-only. It must not approve P8 entry, P8
implementation, a P8 implementation prompt, self-play execution, RL execution,
training, tuning, evaluation, league, source approval, source ingestion, real
data, model-output integration, model-strength evidence or P9-P12 entry.

## Governance Synchronization Review

Review result: sufficient after this update.

Synchronized documents:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

Governance now records:

- current stage is P8 self-play / RL dependency map definition before any
  implementation.
- Full P7 closed only for documented P7 supervised-learning scope.
- P8 risk/evidence taxonomy review can close.
- P8 entry remains unapproved.
- P8 implementation remains unapproved.
- P8 implementation prompt remains unapproved.
- P9-P12 remain unapproved.
- no source approval.
- no source ingestion.
- no real data.
- no training.
- no evaluation.
- no self-play.
- no league.
- no RL execution.
- no model-output integration.
- no model-strength evidence.
- next task is docs-only dependency-map definition.

## Validation Results

Required validation:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Results:

```text
git diff --check: passed.
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py: passed, 15 tests.
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py: passed, 11 tests.
python3 -m unittest tests/supervised/test_feature_label_schema.py: passed, 11 tests.
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py: passed, 1 test.
python3 -m unittest tests/data/test_replay_schema.py: passed, 7 tests.
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py: passed, 1 test.
```

## Review Decision

```text
A. Review can close.
```

Reasons:

- scope is correct.
- Full P7 / P8 recap is accurate.
- P8 non-approval baseline is explicit.
- risk taxonomy R1-R20 is complete and conservative.
- evidence taxonomy E1-E25 is complete and conservative.
- evidence grade vocabulary is safe.
- current evidence classification is correct.
- workstream risk/evidence matrix is sufficient.
- model-strength boundary is explicit.
- Tenhou / stable-dan / LuckyJ / promotion boundary is explicit.
- source / real-data / platform boundary is explicit.
- self-play / RL boundary is explicit.
- stop conditions are sufficient.
- candidate next directions are safe.
- governance is synchronized.
- validation is required and recorded.
- no blocker found.
- no overclaim found.

## Next Task Recommendation

The next first task should be:

```text
Define P8 self-play / reinforcement-learning dependency map before any implementation.
```

This next task must be docs-only dependency-map definition. It must not
approve P8 entry, approve P8 implementation, define or generate an
implementation prompt, execute self-play, execute RL, train, tune, evaluate,
run league, approve source work, ingest real data, integrate model output,
claim model strength or enter P9-P12.

## Evidence Grade

```text
P8 risk/evidence taxonomy review evidence only.
```

## Explicit Non-Evidence

This review is not:

- P8 entry approval.
- P8 implementation approval.
- a P8 implementation prompt.
- P8 first executable task approval.
- P9-P12 entry approval.
- training.
- tuning.
- evaluation.
- self-play.
- league.
- RL execution.
- source approval.
- source ingestion.
- real data.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
