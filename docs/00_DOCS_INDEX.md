# 00_DOCS_INDEX

This file explains where each project document lives.

- `00_HANDOFF.md`: project card, current stage, current status and handoff summary.
- `01_goal_benchmark`: north-star target, LuckyJ baseline, Tenhou metrics, success criteria, algorithm selection principles.
- `02_data_system`: replay data, schema, features, labels and data quality.
- `03_supervised_policy`: supervised learning model, objectives and offline metrics.
- `04_rl_selfplay`: self-play environment, reward design, RL promotion rules, algorithm candidate routes, candidate table and racing funnel.
- `05_evaluation`: benchmark suite, stable dan estimation, algorithm ranking protocol, racing-funnel evaluation and regression tests.
- `06_engine_inference`: state parser, policy service, search, risk model, imperfect-information search and latency.
- `07_development_execution`: milestones, backlog, Codex workflow, algorithm discovery workflow, racing-funnel execution task and completion audit.
- `08_experiment_analysis`: experiment log, model cards, algorithm candidate cards, failure cases and weekly review.
- `09_governance`: evidence, changelog, risk, compliance, glossary and stage contract.
- `10_next`: the only next task.
- `12_technical_plan`: current technical execution plan; technical plan is the active execution charter, while papers are future summaries.

## Critical governance files

```text
docs/09_governance/09_STAGE_TASK_CONTRACT.md
docs/09_governance/09_CHANGELOG.md
docs/09_governance/09_EVIDENCE_LOG.md
docs/09_governance/09_RISK_REGISTER.md
docs/09_governance/09_PLATFORM_COMPLIANCE.md
docs/09_governance/09_UPDATE_PROTOCOL.md
docs/09_governance/09_DECISION_RECORD.md
docs/10_next/10_NEXT.md
```

## Technical plan files

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md
```

`docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`
records the post-P5 transition review after final P5 closure. It confirms that
P5 is closed for the current synthetic/local evaluation groundwork scope and
allows only a docs-only next task to define P6 data-system scope, entry criteria
and first task before implementation. It is not P6 implementation approval,
P7-P12 entry approval, data-ingestion evidence or model-strength evidence.

## Data-system files

```text
docs/02_data_system/02A_DATA_SOURCES.md
docs/02_data_system/02B_REPLAY_SCHEMA.md
docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md
docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md
docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md
docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md
docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md
docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md
docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md
docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md
docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md
docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md
docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md
docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md
docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md
docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md
docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md
```

`docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
defines P6 data-system scope, entry criteria, future exit criteria and the
first next task before implementation. It is docs-only planning evidence: P6
implementation, replay schema code, data ingestion, real Tenhou, real haifu,
external logs, platform data, CLI, model-output integration, training,
self-play, league, runner behavior and P7-P12 remain unapproved.

`docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source
provenance and rights inventory before replay schema implementation. It records
inventory fields, approval-status vocabulary, source-category approvals,
required-before-ingestion checks, future evidence requirements, rights /
provenance risks and replay-schema implementation boundaries. It is docs-only
inventory-definition evidence, not ingestion approval, replay schema
implementation, model-strength evidence or LuckyJ comparison evidence.

`docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema
documentation boundary after the source inventory review. It records allowed
and forbidden field-family planning, source-inventory dependencies,
raw-vs-derived storage boundaries, validation expectations, future
implementation entry criteria and replay-schema risks. It is docs-only boundary
definition evidence, not replay schema implementation, ingestion approval,
source approval, P6 implementation approval, model-strength evidence or LuckyJ
comparison evidence.

`docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
reviews the P6 data-source provenance and rights inventory. It records that the
review can close with no blocker and that the inventory is sufficient as a
pre-ingestion boundary before replay schema documentation work. P6
implementation, replay schema implementation and data ingestion remain closed.
It is review evidence only, not source approval, ingestion evidence,
model-strength evidence or LuckyJ comparison evidence.

`docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
reviews the P6 replay schema documentation boundary before implementation. It
records that the review can close with no blocker, but replay schema
implementation, P6 implementation, data ingestion, dataset readers, feature
extraction, label generation, real Tenhou / real haifu / external-log /
platform-data access and P7-P12 remain closed. It is review evidence only, not
schema implementation, source approval, ingestion evidence, model-strength
evidence or LuckyJ comparison evidence.

`docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
defines the P6 synthetic/local replay fixture boundary before schema
implementation. It records allowed and forbidden fixture-boundary scope,
source-inventory dependency, replay-schema dependency, future shape families,
future implementation entry criteria, validation expectations and risks. It is
docs-only boundary definition evidence, not fixture implementation, replay
schema implementation, ingestion approval, dataset-reader approval,
feature/label generation, model-strength evidence or LuckyJ comparison
evidence.

`docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
reviews the P6 synthetic/local replay fixture boundary before schema
implementation. It records that the review can close with no blocker, while
fixture implementation, replay schema implementation, data ingestion, dataset
readers, parsers, feature extraction, label generation and P7-P12 remain
closed. It is review evidence only, not fixture implementation, schema
implementation, source approval, ingestion evidence, model-strength evidence or
LuckyJ comparison evidence.

`docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
defines the P6 replay schema and fixture implementation readiness checklist
before code. It lists candidate implementation classes, required prerequisites,
decision vocabulary, dependency map, P7-P12 non-entry boundaries and readiness
risks. It is checklist-definition evidence only, not replay schema
implementation, fixture implementation, data ingestion, parser/dataset-reader
approval, feature/label generation, source approval, model-strength evidence or
LuckyJ comparison evidence.

`docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
reviews the P6 replay schema and fixture implementation readiness checklist
before code. It records that the review can close with no blocker, while P6
implementation, replay schema implementation, fixture implementation, data
ingestion, parser/dataset-reader work, feature extraction, label generation and
P7-P12 remain closed. It is checklist-review evidence only, not implementation
approval, source approval, ingestion evidence, model-strength evidence or
LuckyJ comparison evidence.

`docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
defines the P6 replay schema and synthetic fixture implementation proposal
boundary before code. It records candidate proposal classes, required proposal
sections, allowed and forbidden proposal scope, source/fixture constraints,
minimal schema/fixture/test candidate boundaries, future approval conditions,
proposal decision vocabulary, P7-P12 non-entry boundaries and proposal risks.
It is proposal-boundary definition evidence only, not P6 implementation
approval, replay schema implementation, fixture implementation, test
implementation, ingestion evidence, source approval, model-strength evidence
or LuckyJ comparison evidence.

`docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
reviews the P6 replay schema and synthetic fixture implementation proposal
boundary before code. It records that the review can close with no blocker,
while P6 implementation, replay schema implementation, fixture implementation,
tests, ingestion, parser/dataset-reader work, feature extraction, label
generation and P7-P12 remain closed. It is proposal-boundary review evidence
only, not implementation approval, source approval, ingestion evidence,
model-strength evidence or LuckyJ comparison evidence.

`docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
prepares the P6 minimal replay schema and synthetic fixture implementation
proposal for review before code. It names candidate future files and strict
scope, validation, evidence, risk, rollback and stop-condition boundaries. It
does not create replay schema code, fixture files, tests, parser, dataset
reader, ingestion, feature extraction or label generation, and it is not
implementation approval, source approval, model-strength evidence or LuckyJ
comparison evidence.

`docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
reviews that minimal proposal before code. It records that the proposal review
can close with no blocker and that the proposal is sufficiently bounded for a
later approval-decision task, while P6 implementation, replay schema
implementation, fixture implementation, tests, ingestion, parser /
dataset-reader work, feature extraction, label generation and P7-P12 remain
closed. It is proposal-review evidence only, not implementation approval,
source approval, ingestion evidence, model-strength evidence or LuckyJ
comparison evidence.

`docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
prepares the approval decision after the `02M` review. It approves only the
next exact minimal implementation task, limited to the named replay schema
module, one project-authored synthetic/local fixture, two minimal tests and
governance synchronization. It does not execute implementation and does not
approve real Tenhou, real haifu, external logs, platform data, parser /
dataset-reader work, ingestion, feature extraction, label generation, CLI,
model-output integration, training, self-play, league or P7-P12.

The exact minimal P6 replay schema and project-authored synthetic fixture
implementation approved by `02N` is now present in:

```text
src/mjlabai/data/replay_schema.py
tests/fixtures/data/synthetic_replay_smoke.json
tests/data/test_replay_schema.py
tests/data/test_synthetic_replay_fixture_schema.py
```

These are P6 synthetic/local replay schema smoke implementation artifacts
only. They are not parser, dataset reader, ingestion, feature extraction,
label generation, real Tenhou, real haifu, external-log, platform-data,
training, self-play, league, stable-dan, LuckyJ `10.68` or model-strength
evidence.

`docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md`
reviews the exact minimal implementation created after `02N`. It records that
the exact implementation files were respected, the replay schema module remains
standard-library-only and in-memory, the fixture remains project-authored
synthetic/local, the two tests remain minimal and local, validation passed and
the review can close. It is implementation-review evidence only, not parser,
dataset-reader, ingestion, feature, label, real-data, model-output, training,
league, LuckyJ comparison, candidate-promotion or P7-P12 evidence.

`docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
decides that the exact minimal replay schema module, project-authored
synthetic/local fixture, two minimal local tests and directly related
governance synchronization are accepted as current-scope complete. This is
current-scope acceptance decision evidence only. It is not full P6 closure,
not new implementation approval, not parser / dataset-reader / ingestion /
feature / label evidence, not real-data approval, not model-strength evidence
and not P7-P12 entry approval.

`docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
defines the next P6 current-scope data-system task after the `02P` acceptance
decision. It reviews candidate docs-only next tasks and selects
`Define P6 current-scope data-system closure criteria after minimal replay
schema acceptance` as the next first task. It is task-definition evidence only,
not implementation approval, not full P6 closure and not P7-P12 entry approval.

## Algorithm discovery and racing-funnel files

```text
docs/01_goal_benchmark/01G_ALGORITHM_SELECTION_PRINCIPLES.md
docs/04_rl_selfplay/04E_ALGORITHM_CANDIDATE_ROUTES.md
docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md
docs/04_rl_selfplay/04G_ALGORITHM_RACING_FUNNEL.md
docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md
docs/05_evaluation/05F_ALGORITHM_SELECTION_BENCHMARK.md
docs/05_evaluation/05G_RACING_FUNNEL_EVALUATION.md
docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md
docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md
docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md
docs/05_evaluation/05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION.md
docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md
docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md
docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md
docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md
docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md
docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md
docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md
docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md
docs/07_development_execution/07E_ALGORITHM_DISCOVERY_WORKFLOW.md
docs/07_development_execution/07F_ALGORITHM_TABLE_BUILD_TASK.md
docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md
docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md
docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md
docs/08_experiment_analysis/08F_ALGORITHM_CANDIDATE_CARD.md
```

`docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md`
is the P5 legal-action synthetic evaluator coverage review. It records current
synthetic-only `dahai` + strict coverage and is not model-strength evidence,
Tenhou ranked evidence or LuckyJ comparison evidence.

`docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md`
is the P5 tiny benchmark harness boundary definition. It is docs-only planning
for future synthetic/local diagnostics and is not harness implementation,
model-strength evidence, Tenhou ranked evidence or LuckyJ comparison evidence.

`tests/fixtures/eval/tiny_benchmark_harness_smoke.json` and
`tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py` are the P5
tiny benchmark harness synthetic fixture schema smoke coverage. They validate
fixture shape, guardrails, safety flags and future diagnostic metric names only;
they do not implement a harness, measure latency, calculate fixed-position
exact-match, read real data or provide strength evidence.

`docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md`
is the P5 tiny benchmark fixture schema smoke coverage review. It records that
the fixture schema is sufficient as a front-door input boundary for a future
P5-only synthetic/local tiny benchmark harness implementation task. It is
docs-only and not model-strength evidence, Tenhou evidence, stable-dan evidence
or LuckyJ comparison evidence.

`docs/05_evaluation/05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION.md`
records the P5 tiny benchmark harness implementation for the project-authored
synthetic fixture only. The implementation validates and summarizes the fixed
synthetic fixture and can emit an `OfflineEvaluationResultEnvelope`; it does not
measure latency, compute fixed-position exact-match, connect model output,
read real data, add CLI/file ingestion or provide strength evidence.

`docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md`
reviews the P5 tiny benchmark harness implementation and records that it can
close for the current project-authored synthetic/local fixture scope. It is
docs-only review evidence, not model-strength evidence, Tenhou evidence,
stable-dan evidence or LuckyJ comparison evidence.

`docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md`
reviews whether the current offline result envelope coverage is sufficient for
synthetic tiny benchmark diagnostics. It records that `tiny_benchmark_harness`,
`wrapper_smoke_success`, `sample_size = 1`, all-false safety flags,
synthetic/local warnings and evidence references are sufficient for the current
fixture scope. It is docs-only review evidence, not model-strength evidence,
Tenhou evidence, stable-dan evidence or LuckyJ comparison evidence.

`docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md`
reviews metric registry consistency across stable-dan, legal-action and tiny
benchmark diagnostics. It records that metric names, units, directions,
current status, source notes and evidence grades are consistent for the current
P5 scope. It is docs-only review evidence, not metric implementation,
registry-code change, model-strength evidence or LuckyJ comparison evidence.

`docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md`
reviews P5 synthetic/local evidence taxonomy and promotion guardrails across
stable-dan, legal-action, tiny benchmark, offline envelope and metric registry
artifacts. It records that current evidence labels and non-evidence warnings are
consistent, and recommends defining P5 closure criteria next. It is docs-only
review evidence, not a promotion criteria change or model-strength evidence.

`docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md`
defines P5 evaluation groundwork closure criteria and an exit readiness
checklist. It records that P5 is near closure but remains open until reviewed.
It is docs-only specification evidence, not P5 closure itself, P6-P12 entry
approval or model-strength evidence.

`docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md`
reviews the P5 closure criteria and exit readiness checklist. It records that
the criteria review can close with no blocker, but P5 remains open pending
final P5 handoff/evidence index finalization and a later final closure review.
It is docs-only review evidence, not P5 closure itself, P6-P12 entry approval
or model-strength evidence.

`docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md`
finalizes the P5 handoff and evidence index for the final closure review gate.
It records a finalization-ready P5 handoff summary, a P5 evidence index,
deferred items and governance synchronization status. P5 remains open until the
final closure review gate. It is docs-only finalization evidence, not P5
closure itself, P6-P12 entry approval or model-strength evidence.

`docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
is the final P5 closure review gate. It records that P5 can close for the
current synthetic/local evaluation groundwork scope. This is not P6-P12 entry
approval, not P6 first-task approval and not model-strength evidence.

## Current rule

所有算法讨论都必须先定位其 funnel stage，再定义下一步最低成本实验。
