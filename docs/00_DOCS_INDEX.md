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
```

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

## Current rule

所有算法讨论都必须先定位其 funnel stage，再定义下一步最低成本实验。
