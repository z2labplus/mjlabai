# 00_HANDOFF

## Project card

Project name: MjLabAI Tenhou Mahjong AI

North-star target:

```text
Train a Japanese Mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum target: Tenhou stable dan > 10.68.
```

## Current status

The project documentation now includes:

- North-star goal and LuckyJ benchmark.
- Tenhou-oriented success metrics.
- Data, supervised policy, self-play RL, evaluation, inference and governance structure.
- Algorithm candidate table for Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer.
- Algorithm ranking protocol.
- v0.4 racing-funnel mechanism for staged algorithm selection.
- P0-P12 project roadmap from rule setup through LuckyJ 10.68 validation.
- v0.1 technical execution plan: technical-plan-first execution, paper-as-future-summary.

Current stage interpretation:

```text
P0 / P1 / P2 are basically established.
P3 baseline reproducibility audit produced current Mortal/Akochan funnel evidence.
Current active stage is post-current-scope P7 supervised learning transition
review planning after final current-scope closure:
the exact `03O` minimal synthetic/local supervised fixture and feature-label
smoke task has been implemented in `src/mjlabai/supervised/feature_label_schema.py`,
`tests/fixtures/supervised/synthetic_supervised_smoke.json`,
`tests/supervised/test_feature_label_schema.py` and
`tests/supervised/test_synthetic_supervised_fixture_schema.py`. The
implementation validates only in-memory JSON-safe synthetic/local smoke
mappings, candidate feature/label family names, public-information-only
placeholders and provenance / non-evidence guardrails. It does not approve
parser / reader / ingestion, actual feature extraction, actual label
generation, training, model-output integration, real data or P8-P12 entry.
`docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`
reviews that exact implementation and records `Review can close`.
`docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
records `Accepted as current-scope complete` for the exact minimal
synthetic/local smoke scope only.
`docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines the next P7 current-scope supervised-learning task and selects
docs-only P7 current-scope closure criteria definition to avoid indefinite
readiness / schema churn.
`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines those current-scope closure criteria, C1-C26, exit readiness,
remaining docs/review/closure items, deferred / blocked / not accepted items,
validation commands and P8-P12 non-entry conditions. It does not close P7
current scope.
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
reviews those criteria and records `Review can close` with no blocker. It does
not close P7 current scope.
`docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the P7 current-scope handoff and evidence index after `03T`,
confirms no separate risk/evidence consistency review is needed before final
current-scope closure review, and recommends `Run final P7 current-scope
closure review gate` as the next docs-only task. It does not close P7 current
scope, close full P7, approve broader P7 implementation, approve training,
approve source ingestion, approve parser / reader / ingestion, approve actual
feature extraction, approve actual label generation, approve real data,
approve model-output integration or approve P8-P12.
`docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md`
runs that final gate and records `P7 current scope can close` only for the
exact current scope: docs-only supervised-learning readiness chain plus the
accepted minimal synthetic/local supervised feature-label smoke
implementation. Full P7 is not closed. Broader P7 implementation, training,
training data source approval, source ingestion, parser / reader / ingestion,
actual feature extraction, actual label generation, supervised dataset
construction, model architecture / trainer, real data, model-output
integration, self-play, league and P8-P12 remain unapproved. The next task is
`Run post-current-scope P7 transition review before defining any broader P7
implementation or P8 task`.
`docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md`
completes that post-current-scope transition review. It confirms that P7
current scope is closed only for the exact current scope, full P7 remains
open, broader P7 implementation and P8-P12 remain unapproved, and the next
task is `Define full P7 closure roadmap and remaining scope inventory after
current-scope closure`. That next task is docs-only roadmap / inventory
definition and must not add production code, tests, fixtures, data files,
parser / reader / ingestion, actual feature extraction, actual label
generation, supervised dataset construction, training, model architecture,
model-output integration, real data, self-play, league or P8-P12 work.
`docs/03_supervised_policy/03W_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_AFTER_CURRENT_SCOPE_CLOSURE.md`
now defines that full P7 roadmap and remaining scope inventory. It classifies
remaining items as required, deferred, blocked, later-stage or out of scope and
keeps full P7 open. The next task is `Review full P7 closure roadmap and
remaining scope inventory after current-scope closure`, a docs-only review
gate that still must not approve broader P7 implementation, training, source
ingestion, parser / reader / ingestion, actual feature extraction, actual
label generation, model architecture / trainer, real data, model-output
integration, self-play, league or P8-P12.
`docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md`
reviews that roadmap / inventory and records `Review can close` with no
blocker. It confirms that the `03W` scope, current-scope closure context,
remaining-scope classification, docs-first roadmap, validation commands,
evidence grade and governance synchronization are sufficient. Full P7 remains
open. The next task is `Define broader P7 scope, entry criteria and first task
before implementation`, and it is still docs-only: no broader P7
implementation, training, source ingestion, parser / reader / ingestion,
actual feature extraction, actual label generation, supervised dataset
construction, model architecture / trainer, real data, model-output
integration, self-play, league or P8-P12 is approved.
`docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
defines that broader P7 scope / entry / first-task boundary. It records
broader P7 purpose, allowed docs-only scope, forbidden scope, implementation
entry criteria, required upstream artifacts, blocked / deferred / later-stage
/ out-of-scope items, why broader implementation and training remain
unapproved, why P8-P12 remain closed, and the evidence grade. Full P7 remains
open. The next task is `Review broader P7 scope, entry criteria and first task
before implementation`, and it is still docs-only: no broader P7
implementation, training, source ingestion, parser / reader / ingestion,
actual feature extraction, actual label generation, supervised dataset
construction, model architecture / trainer, real data, model-output
integration, self-play, league or P8-P12 is approved.
The active project work has just closed P5 evaluation groundwork for the
current synthetic/local scope.
Mortal F1 runnable-baseline path is paused because no lawful, verifiable and usable trained model artifact is currently available.
Akochan F1 is Conditional Pass after successful Ubuntu GitHub Actions build/minimal-run evidence, with license and local macOS build limits still open.
Akochan F2 task definition is complete.
Minimal Akochan F2 wrapper skeleton is implemented and passes fake-executable smoke tests.
Akochan F2 fixed-sample real-exe wrapper validation has passed: workflow run `26629344590` at commit `29f5e1ed19407d169f85524e05438ac8938d2dc2` built `ai_src/libai.so`, root `libai.so` and `system.exe`; fake wrapper tests passed 14 tests; real `legal_action` and real `mjai_log` wrapper tests both passed.
This is fixed-sample wrapper/integration evidence only. It is not Akochan strength evidence, not mjlabai strength evidence, and not authorization for broad adapter work, self-play, match, training or Tenhou integration.
The project has completed the final P5 closure review for the current
synthetic/local evaluation groundwork scope. The deterministic Tenhou
stable-dan calculator from room-specific formulas is implemented and tested.
The stable-dan bootstrap confidence interval is implemented and tested with percentile empirical multinomial resampling.
The stable-dan threshold comparison helper is implemented and tested with LuckyJ stable dan `10.68` as the default target line.
The stable-dan reporting schema and minimum sample-size guardrails are implemented and tested.
The placement-count aggregation helper is implemented and tested for offline stable-dan evaluation inputs.
The CLI-free stable-dan evaluation report smoke fixture is implemented and tested from synthetic placement inputs.
The stable-dan evaluation API documentation is added with example usage from synthetic placements.
The stable-dan evaluation groundwork subtrack is complete for the current P5 scope.
The P5 offline evaluation metric registry and result envelope schema are implemented and documented.
The offline evaluation envelope smoke test now verifies that a synthetic stable-dan report can be represented as an `OfflineEvaluationResultEnvelope`.
The P5 legal-action / invalid-action metric specification is defined in `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`.
The P5 action canonicalization schema for legal-action metric fixtures is defined in `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`.
The synthetic legal-action metric fixture schema smoke test is implemented in `tests/eval/test_legal_action_fixture_schema_smoke.py` against `tests/fixtures/eval/legal_action_metric_smoke.json`; it validates fixture shape only and does not calculate legal/invalid rates or implement an evaluator.
The P5 legal-action metric synthetic evaluator boundary is defined in `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`: future implementation may use only project-authored synthetic/local fixtures, current `dahai` scope and strict matching; it must preserve explicit count/rate denominator rules and all-false safety flags, and must not use real Tenhou, real haifu, external logs, platform data, model code, third-party binaries, training, self-play or league paths.
The P5 synthetic legal-action metric evaluator is implemented for the project-authored fixture only in `src/mjlabai/eval/legal_action_metric.py`, with tests in `tests/eval/test_legal_action_metric.py`. The fixture now includes an explicit synthetic `parse_failure` record that keeps `action_type = "dahai"` and uses `tsumogiri: null` only to exercise the current strict parse-failure branch. It computes the current synthetic fixture as `legal=1`, `invalid=1`, `missing=1`, `parse_failure=1`, `skipped=1`, `evaluated=4`, and rates `1/4`, `1/4`, `1/4`, `1/4`. It also maps the result into `OfflineEvaluationResultEnvelope` with all safety flags false and synthetic-only warnings. `docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md` records that this minimum outcome coverage is complete only for the current P5 synthetic-only `dahai` + strict scope. This is legality diagnostic infrastructure only, not a broad evaluator, canonicalizer, legal-action checker, CLI, league, runner, model-output path, Tenhou integration or strength evidence.
`docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md` defines the P5 tiny benchmark harness boundary before implementation. It is docs-only: future legal-action rate, latency and fixed-position diagnostics may use only synthetic/local inputs and compatible `OfflineEvaluationResultEnvelope` records.
`tests/fixtures/eval/tiny_benchmark_harness_smoke.json` and `tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py` add a P5 tiny benchmark harness synthetic fixture schema smoke test. The fixture is project-authored synthetic/local only and describes legal-action diagnostic shape, latency diagnostic plan shape and fixed-position synthetic decision shape without implementing a harness, measuring latency, calculating fixed-position exact-match, calling model code or reading real Tenhou / real haifu / external logs / platform data. It is not model-strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.
`docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md` reviews that fixture schema smoke coverage and records that it is complete only for the current P5 schema-only synthetic/local boundary. The fixture schema is sufficient as a front-door input boundary for a future P5-only tiny benchmark harness implementation task, but no harness implementation, production code, tests, fixtures, latency measurement, model-output integration, real-data path, CLI, league, runner or P6-P12 work was added by the review gate.
`src/mjlabai/eval/tiny_benchmark_harness.py` implements the P5 tiny benchmark harness for the project-authored synthetic fixture only, with tests in `tests/eval/test_tiny_benchmark_harness.py`. The harness loads only `tests/fixtures/eval/tiny_benchmark_harness_smoke.json`, validates and summarizes its legal-action diagnostic shape, latency plan shape and fixed-position synthetic record shape, and can emit an `OfflineEvaluationResultEnvelope` with `evaluation_type = "tiny_benchmark_harness"`, `wrapper_smoke_success = true`, `sample_size = 1`, all safety flags false and synthetic/local warnings. It does not measure latency, calculate legal-action metrics inside the harness, compute fixed-position exact-match, connect model output, add CLI/file ingestion, read real Tenhou / real haifu / external logs / platform data, or provide model-strength, stable-dan or LuckyJ `10.68` evidence.
`docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md` reviews the P5 tiny benchmark harness implementation and records that it can close for the current project-authored synthetic/local fixture scope with no blocker. The evidence grade remains P5 synthetic/local tiny benchmark harness implementation review evidence only.
`docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md` reviews the P5 offline result envelope coverage for synthetic tiny benchmark diagnostics. It records that the current envelope can represent the diagnostic with `evaluation_type = "tiny_benchmark_harness"`, `wrapper_smoke_success = true`, `sample_size = 1`, `latency_ms = None`, all-false safety flags, synthetic/local warnings and evidence references. No blocker was found, and the evidence grade remains P5 synthetic/local offline envelope coverage review evidence only.
`docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md` reviews P5 metric registry consistency across stable-dan, legal-action and tiny benchmark diagnostics. It records that current registry names, units, directions, status/source notes and evidence grades are consistent for the current P5 scope. It also records that future tiny benchmark names such as latency percentiles and fixed-position exact-match remain fixture planning names, not current registered/emitted metrics. No blocker was found, and no registry code, production code, tests or fixtures were changed by the review.
`docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md` reviews P5 synthetic/local evidence taxonomy and promotion guardrails. It records that evidence labels, non-evidence warnings, promotion/ranking guardrails and stage-boundary wording are consistent across the current P5 stable-dan, legal-action, tiny benchmark, offline envelope and metric registry artifacts. No blocker was found, and no promotion criteria, taxonomy definitions, production code, tests or fixtures were changed by the review.
`docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md` defines P5 evaluation groundwork closure criteria and an exit readiness checklist. It records the current P5 scope, current-scope complete subtracks, required remaining P5 items, deferred items and non-entry conditions for P6-P12. P5 is near closure, but it remains open until a closure review gate confirms readiness.
`docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md` reviews the P5 closure criteria and exit readiness checklist. The review found no blocker: the `05U` scope is correct, the current P5 subtrack inventory is complete enough for finalization, closure criteria are sufficient, the exit readiness checklist is executable, deferred items are correctly classified and P6-P12 non-entry conditions are sufficient. The closure criteria review can close, but P5 remains open pending final P5 handoff/evidence index finalization and a later final closure review.
`docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md` finalizes the P5 handoff and evidence index for final closure review. It records a finalization-ready handoff summary, a P5 evidence index, required remaining items, deferred items and governance synchronization status. No blocker was found. P5 handoff and evidence index are finalized for final closure review, but P5 remains open until the final closure review gate.
`docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md` is the final P5 closure review gate. It records that all P5 closure criteria pass, no blocker was found, required remaining P5 items have narrowed to closure decision recording, deferred later-stage items do not block current P5 closure, and required validation tests were rerun. P5 is closed for the current synthetic/local evaluation groundwork scope.
P5 closure does not approve P6-P12 entry, P6 data-system work, training, self-play, league, real Tenhou, model-output integration, CLI, broad ingestion, latency measurement, fixed-position exact-match, metric implementation, registry code changes, promotion criteria changes or model-strength claims.
`docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` records the post-P5 transition review. It confirms that P5 is closed for the current synthetic/local evaluation groundwork scope and that the project may start only a docs-only task to define P6 data-system scope, entry criteria and first task before implementation.
`docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P6 data-system scope, entry criteria, future exit criteria and first next task before implementation. It records that P6 exists to make future replay, feature, label and data-quality work lawful, reproducible and auditable before any supervised learning, RL, search, league or LuckyJ validation work begins. This is docs-only planning evidence: no replay schema code, data ingestion, feature extraction, label generation, dataset reader, CLI, model-output integration, real Tenhou, real haifu, external-log ingestion, platform-data ingestion, training, self-play, league, runner behavior, P7-P12 work or model-strength claim was added. P6 implementation remains closed until a later explicit implementation boundary is approved.
`docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source provenance and rights inventory before replay schema implementation. It records inventory fields, approval-status vocabulary, source-category approvals, required-before-ingestion checks, future evidence requirements, rights/provenance risks and replay-schema implementation boundaries. Project-authored synthetic/local fixtures and repository docs may be used only in their current docs/smoke context; real Tenhou, real haifu, external logs, platform data, accounts, third-party binaries, model weights, model outputs, self-play outputs and league outputs remain unapproved. This inventory is docs-only definition evidence, not ingestion approval, replay schema implementation, P6 implementation approval, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` reviews that inventory before replay schema implementation. The review found no blocker and can close, but P6 implementation, replay schema implementation, source ingestion, feature extraction, label generation and P7-P12 remain closed. This is P6 inventory review evidence only, not source approval, ingestion approval, data-system implementation approval, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema documentation boundary after source inventory review. It records allowed documentation scope, forbidden scope, source-inventory dependencies, replay field families, validation expectations, future implementation entry criteria and replay-schema risks. This is P6 replay schema documentation boundary definition evidence only: P6 implementation, replay schema implementation, source ingestion, feature extraction, label generation and P7-P12 remain closed.
`docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` reviews the P6 replay schema documentation boundary before implementation. The review found no blocker and can close, but P6 implementation, replay schema implementation, source ingestion, data ingestion, dataset readers, feature extraction, label generation and P7-P12 remain closed. This is P6 replay schema documentation boundary review evidence only, not source approval, ingestion approval, schema implementation, data-system implementation approval, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md` defines the P6 synthetic/local replay fixture boundary before schema implementation. It records project-authored and repo-local fixture requirements, allowed and forbidden fixture-boundary scope, source/provenance dependencies, replay field-family alignment, future shape families, future implementation entry criteria, validation expectations and fixture risks. This is docs-only boundary definition evidence: fixture implementation, replay schema implementation, data ingestion, dataset readers, feature extraction, label generation and P7-P12 remain closed.
`docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md` reviews the P6 synthetic/local replay fixture boundary and records that the review can close with no blocker, but fixture implementation remains closed. P6 implementation, replay schema implementation, replay fixture implementation, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md` defines the P6 replay schema and fixture implementation readiness checklist before code. It records candidate implementation classes, replay schema code readiness, synthetic/local replay fixture readiness, parser/dataset reader readiness, feature/label readiness, data-ingestion readiness, decision vocabulary, dependency map, P7-P12 non-entry boundaries and risks. This is checklist-definition evidence only: P6 implementation, replay schema implementation, fixture implementation, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md` reviews the P6 replay schema and fixture implementation readiness checklist before code. The review found no blocker and can close, but P6 implementation, replay schema implementation, fixture implementation, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md` defines the P6 replay schema and synthetic fixture implementation proposal boundary before code. It records how any future implementation proposal must state candidate class, scope, non-goals, source inventory dependency, replay schema boundary dependency, synthetic fixture boundary dependency, readiness status, allowed/forbidden files, allowed/forbidden code changes, fixture/test policy, validation commands, evidence/risk update plans, rollback plan, blockers, human/Web ChatGPT approval requirements, P7-P12 non-entry and non-evidence warnings. This is proposal-boundary definition evidence only: P6 implementation, replay schema implementation, fixture implementation, tests, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md` reviews that proposal boundary with no blocker. The review can close, but P6 implementation, replay schema implementation, fixture implementation, tests, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved. This is proposal-boundary review evidence only, not implementation approval, source approval, ingestion evidence, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md` prepares the P6 minimal replay schema and synthetic fixture implementation proposal for review before code. It names candidate future files (`src/mjlabai/data/replay_schema.py`, `tests/fixtures/data/synthetic_replay_smoke.json`, `tests/data/test_replay_schema.py`, `tests/data/test_synthetic_replay_fixture_schema.py`) and defines strict scope, validation, evidence, risk, rollback, stop-condition and human/Web ChatGPT approval boundaries. This is proposal-drafting evidence only: P6 implementation, replay schema implementation, fixture implementation, tests, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md` reviews that proposal before code. The review found no blocker: `02L` scope is correct, candidate implementation classes and proposed file candidates are sufficient and conservative, the minimal replay schema code / synthetic fixture / validation test candidate boundaries are narrow enough for a later approval-decision task, and review can close. This is proposal-review evidence only: P6 implementation, replay schema implementation, fixture implementation, tests, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` prepared the approval decision for the minimal P6 replay schema and project-authored synthetic fixture implementation task. The decision was `Approved for next minimal implementation task`, but only for the exact task and exact files named in `02N`: `src/mjlabai/data/replay_schema.py`, `tests/fixtures/data/synthetic_replay_smoke.json`, `tests/data/test_replay_schema.py` and `tests/data/test_synthetic_replay_fixture_schema.py`, plus directly related docs/governance synchronization.
The minimal P6 replay schema and project-authored synthetic fixture implementation is now complete in those exact files. The helper validates in-memory replay fixture / record mappings, project-authored synthetic provenance, no-real-data / no-account-id / no-model-output / no-training-use guardrails and JSON-safe content. `tests/fixtures/data/synthetic_replay_smoke.json` is project-authored synthetic/local only and is not Tenhou data, real haifu, external log, platform data, model output, training data, model-strength evidence or LuckyJ `10.68` comparison. Local validation passed `git diff --check`, `python3 -m unittest tests/data/test_replay_schema.py` and `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`. No parser, dataset reader, ingestion, feature extraction, label generation, CLI, broad file ingestion, model-output integration, real Tenhou, real haifu, external logs, platform data, training, self-play, league, P7-P12 or model-strength claim was added.
`docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md` reviews that exact implementation. It confirms the exact implementation files were respected, the replay schema module remains standard-library-only and in-memory, the fixture remains project-authored synthetic/local, both tests remain minimal/local, validation passed and the review can close with no blocker. This is implementation-review evidence only, not data ingestion, parser, dataset reader, feature extraction, label generation, real-data approval, model-output integration, training, self-play, league, LuckyJ comparison, candidate promotion or P7-P12 entry approval.
`docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md` accepts that exact minimal replay schema module, project-authored synthetic/local fixture, two minimal local tests and directly related governance synchronization as current-scope complete. This is not full P6 closure, not new implementation approval, not parser / reader / ingestion / feature / label evidence, not real-data approval, not model-output integration, not training, self-play, league, LuckyJ comparison, candidate promotion or P7-P12 entry approval.
`docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` defines the next P6 current-scope data-system task after that acceptance. It reviews candidate docs-only tasks and selects `Define P6 current-scope data-system closure criteria after minimal replay schema acceptance` because the project should avoid extending P6 indefinitely now that the minimal replay schema / synthetic fixture scope is accepted.
`docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` defines the P6 current-scope data-system closure criteria after minimal replay schema acceptance. It records the accepted current scope, minimum closure criteria, exit readiness checklist, required remaining items, deferred items, P7-P12 non-entry conditions and the next review gate. It is closure-criteria definition evidence only: it does not close full P6, does not close current-scope P6, does not approve new implementation and does not approve P7-P12 entry.
`docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` reviews the `02R` closure criteria and finds no blocker. The review confirms `02R` scope is correct, closure criteria are sufficient, the exit readiness checklist is auditable, required remaining items are correctly narrowed, deferred items are correctly excluded from current-scope closure, P7-P12 non-entry conditions are sufficient and validation passes. This is closure-criteria review evidence only: it does not close full P6, does not close current-scope P6, does not approve new implementation and does not approve P7-P12 entry.
`docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md` runs the final P6 current-scope data-system closure review gate. It records that current-scope P6 can close for the accepted synthetic/local minimal replay schema and project-authored synthetic fixture scope only. Full P6 is not closed, P7-P12 entry is not approved and parser / reader / ingestion / feature / label / real-data / model-output / CLI / training / self-play / league work remains unapproved.
`docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md` completes the post-current-scope P6 transition review. It confirms that accepted current-scope P6 is closed only for the synthetic/local minimal scope, full P6 remains open and P7-P12 remain unapproved. The next project task is docs-only: define a full P6 closure roadmap and remaining scope inventory after current-scope closure. It must not add production code, tests, fixtures, data files, parser / reader / ingestion behavior, feature / label behavior, model output, CLI, broad ingestion, third-party artifact, overclaim or P7-P12 drift.
`docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md` defines the full P6 closure roadmap and remaining scope inventory after accepted current-scope closure. It classifies remaining P6 items as required, deferred, blocked, later-stage or explicitly out of scope; identifies docs-only closure criteria / review / evidence / risk / final closure gates as the required path; and keeps full P6 open, P7-P12 unapproved, and implementation / real-data / parser / reader / ingestion / feature / label work unapproved. The next task is a docs-only review of this roadmap / inventory.
`docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md` reviews the `02U` roadmap / inventory with no blocker. It confirms that `02U` scope is correct, the accepted current-scope closed chain is complete, the remaining inventory classification is reasonable, the roadmap is conservative and docs-only, required / deferred / blocked / later-stage / out-of-scope classifications are safe, P7-P12 non-entry boundaries are sufficient and governance is synchronized. The review can close, but it does not close full P6, approve P7-P12 entry, approve implementation, approve real data or create model-strength evidence. The next task is a docs-only full P6 closure criteria definition.
`docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md` defines full P6 closure criteria after the roadmap / inventory and review. It records full-P6 closure scope, C1-C27 closure criteria, an exit readiness checklist, required remaining full-P6 closure items, deferred items, blocked items, later-stage / out-of-scope items and P7-P12 non-entry conditions. This is criteria-definition evidence only: full P6 remains open, P7-P12 entry remains unapproved, and parser / dataset reader / ingestion / feature extraction / label generation / real-data / model-output / CLI / training / self-play / league work remains unapproved. The next task is a docs-only review of these full P6 closure criteria.
`docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md` reviews the `02W` full P6 closure criteria with no blocker. It confirms that the `02W` scope is correct, C1-C27 are sufficient and conservative, exit readiness is auditable, required remaining items are docs/review/closure-only, deferred / blocked / later-stage / out-of-scope classifications are safe, P7-P12 non-entry conditions are sufficient and governance is synchronized. This is criteria-review evidence only: full P6 remains open, P7-P12 entry remains unapproved, and parser / dataset reader / ingestion / feature extraction / label generation / real-data / model-output / CLI / training / self-play / league work remains unapproved. It selected docs-only full P6 handoff and evidence index finalization as the next task.
`docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md` finalizes the full P6 handoff and evidence index after `02X`. It records a finalization-ready full P6 handoff summary, an evidence index covering the P6 planning/review chain, accepted minimal implementation artifacts, validation and governance artifacts, evidence grade consistency, remaining required full-P6 items and the next risk / source-rights review scope. This is handoff / evidence-index finalization evidence only: full P6 remains open, P7-P12 entry remains unapproved, and parser / dataset reader / ingestion / feature extraction / label generation / real-data / model-output / CLI / training / self-play / league work remains unapproved. The next task is docs-only risk register and source-rights inventory consistency review before final closure review.
`docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md` reviews full P6 risk-register and source-rights inventory consistency before final closure review. It confirms that the source-rights inventory, risk register, evidence index and governance docs consistently keep real Tenhou, real haifu, external logs, platform data, accounts, third-party artifacts, parser / reader / ingestion, feature extraction, label generation, CLI, model-output integration, training, self-play, league and P7-P12 unapproved. Review decision: `Review can close; no risk/source-rights blocker for final full P6 closure review.` This is risk/source-rights consistency review evidence only: it does not close full P6, approve P7-P12 entry, approve source ingestion, approve real data, approve parser / reader / ingestion / feature / label work, approve CLI or model-output integration, or provide model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or candidate-promotion evidence. The next task is the docs-only final full P6 closure review gate.
`docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md` runs the final full P6 closure review gate and records the decision `Full P6 can close` for the documented P6 data-system scope: docs/governance/source-rights planning, accepted synthetic/local minimal replay schema and project-authored synthetic fixture smoke implementation, and deferred/blocked/later-stage inventory. Full P6 closure does not approve P7-P12 entry, a P7 first task, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, source-specific real-data approval, model-output integration, CLI, training, tuning, self-play, league, model-strength claims, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison or candidate promotion. The next task is a docs-only post-full-P6 transition review before defining any P7 task.
`docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md` completes the post-full-P6 transition review. It confirms that full P6 is closed only for the documented P6 data-system scope and selects `Define P7 scope, entry criteria and first task before implementation` as the next docs-only task. This is transition-review evidence only: it does not approve P7 implementation, P7 first-task execution, P8-P12 entry, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, training, tuning, self-play, league, model-strength claims, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison or candidate promotion.
`docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P7 supervised-learning scope, entry criteria and the first task candidate before implementation. It records P7 purpose, north-star relationship, allowed docs-only scope, forbidden scope, implementation entry criteria, exit criteria draft, required inputs, risk review requirements, evidence requirements and P8-P12 non-entry boundaries. It recommends `Review P7 scope, entry criteria and first task before implementation` as the next docs-only review gate. This is P7 scope / entry criteria / first-task definition evidence only; it does not approve P7 implementation, P7 first-task execution, training, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, self-play, league, P8-P12 entry, model-strength claims, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison or candidate promotion.
`docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md` reviews `03E` and records the decision `Review can close`. The P7 scope definition is sufficient to move to the next docs-only P7 readiness task, but it still does not approve P7 implementation, P7 first-task execution, training, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, self-play, league, P8-P12 entry or model-strength claims. The next P7 task is `Define P7 supervised-learning data/source readiness inventory before implementation`.
`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md` defines the P7 supervised-learning data/source readiness inventory before implementation. It records that no source is currently approved for P7 training, source ingestion, parser / reader / ingestion, feature extraction or label generation. It classifies candidate categories including the P6 project-authored synthetic/local fixture, repository docs, future synthetic SL fixtures, future approved real replay sources, real Tenhou / ranked logs, real haifu / external logs, platform data / online account data, model outputs / self-play / league outputs, third-party references, third-party binaries / weights / params / checkpoints, human-authored labels and generated labels. This is inventory-definition evidence only, not source approval, training-data approval, P7 implementation, model-strength evidence or P8-P12 entry approval.
`docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md` reviews `03G` and records the decision `Review can close`. The review confirms that `03G` scope, candidate categories, current `None` approved-for-training status, readiness vocabulary, training-data requirements, P6 source-rights consistency, parser / reader / ingestion dependency status, feature / label readiness status, risks, evidence requirements and governance synchronization are sufficient for the current P7 review gate. This is inventory-review evidence only; it does not approve P7 implementation, P7 first-task execution, training data source, source ingestion, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, self-play, league, P8-P12 entry or model-strength claims. The next task is `Define P7 feature and label readiness boundary before implementation`.
`docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md` defines P7 feature and label readiness boundaries before implementation. It records candidate feature families, candidate label families, forbidden feature / label scope, the dependency map, leakage risks, evidence requirements, readiness vocabulary and the planning decision that the boundary is defined. This is boundary-definition evidence only; it does not approve feature extraction, label generation, parser, dataset reader, ingestion, training, real data, model-output integration, P7 implementation or P8-P12 entry. The next task is `Review P7 feature and label readiness boundary before implementation`.
`docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md` reviews `03I` and records the decision `Review can close`. The review confirms that `03I` scope, feature readiness boundary, label readiness boundary, candidate feature families, candidate label families, forbidden scope, dependency map, risks, evidence requirements, readiness vocabulary, governance synchronization and validation are sufficient for the current P7 review gate. This is boundary-review evidence only; it does not approve P7 implementation, P7 first-task execution, training data source, source ingestion, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, self-play, league, P8-P12 entry or model-strength claims. That review selected `Define P7 supervised-learning risk and evidence taxonomy before implementation` as its follow-up.
`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md` defines the P7 supervised-learning risk and evidence taxonomy before implementation. It records scope/stage creep, source approval, training-data approval, parser/reader/ingestion, feature/label ambiguity, leakage, model-output, real-data, artifact, training-before-approval, evidence-overclaim, LuckyJ/Tenhou/stable-dan and P8/P10/P12 risks; it also defines evidence grades, current P7 evidence classification, future evidence fields, evidence-to-claim mapping, forbidden evidence interpretations, dependency order and governance update requirements. This is taxonomy-definition evidence only; it does not approve P7 implementation, P7 first-task execution, source approval, source ingestion, parser, dataset reader, ingestion, feature extraction, label generation, training, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, self-play, league, P8-P12 entry or model-strength claims. Its follow-up review task was completed in `03L`.
`docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md` reviews `03K` and records the decision `Review can close`. The review confirms that `03K` scope, risk taxonomy, evidence taxonomy, current P7 evidence classification, future evidence requirements, evidence-to-claim mapping, forbidden interpretations, dependency map, evidence / risk governance update requirements, P8-P12 non-entry boundary, governance synchronization and validation are sufficient for the current P7 review gate. This is taxonomy-review evidence only; it does not approve P7 implementation, P7 first-task execution, training data source, source ingestion, parser, dataset reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs, platform data, model-output integration, CLI, self-play, league, P8-P12 entry or model-strength claims. It selected `Define minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation`, which is now defined in `03M`.
`docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md` defines the minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation. It identifies exact candidate future files only, synthetic/local fixture boundaries, feature / label smoke boundaries, future validation commands, approval conditions, stop conditions and risks. This is proposal evidence only: no fixture, tests, production code, data files, source approval, parser, dataset reader, ingestion, feature extraction, label generation, training, model-output integration, real data, self-play, league or P8-P12 entry is approved. It selected `Review minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation`, which is now complete in `03N`.
`docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md` reviews the `03M` proposal and records `Review can close` with no blocker. It confirms the scope, minimal candidate classes, exact candidate future files, synthetic/local fixture boundary, feature / label smoke boundary, validation-command distinction, future approval conditions, stop conditions, risks, evidence grade and governance synchronization are sufficient. This is proposal-review evidence only: it does not approve P7 implementation, P7 first-task execution, fixture creation, tests, production code, data files, source approval, parser, dataset reader, ingestion, feature extraction, label generation, training, model-output integration, real data, self-play, league or P8-P12 entry. Its follow-up approval decision is now recorded in `03O`.
`docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md` records the docs-only approval decision. Decision: `Approved for next minimal implementation task.` The exact allowed implementation files are `src/mjlabai/supervised/feature_label_schema.py`, `tests/fixtures/supervised/synthetic_supervised_smoke.json`, `tests/supervised/test_feature_label_schema.py` and `tests/supervised/test_synthetic_supervised_fixture_schema.py`, plus directly related docs/governance updates only. This is approval-decision evidence only: it does not execute implementation, create files, generate an implementation prompt, approve source ingestion, approve parser, dataset reader, ingestion, actual feature extraction, actual label generation, training, real data, self-play, league or P8-P12 entry. The next task is `Implement minimal P7 synthetic/local supervised fixture and feature-label smoke only`.
The exact minimal P7 synthetic/local supervised fixture and feature-label smoke
implementation is complete in `src/mjlabai/supervised/feature_label_schema.py`,
`tests/fixtures/supervised/synthetic_supervised_smoke.json`,
`tests/supervised/test_feature_label_schema.py` and
`tests/supervised/test_synthetic_supervised_fixture_schema.py`. It validates
only JSON-safe synthetic/local smoke mappings, candidate feature families,
candidate label families, public-information-only placeholders, absence of
hidden/future information fields, all-false non-evidence flags and rejection
of training-use approval, source-approval, real-data, model-output, self-play
and league provenance.
`docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`
reviews the implementation and records `Review can close` with no blocker.
`docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
accepts it as current-scope complete only for the exact minimal
synthetic/local feature-label smoke scope.
`docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines the next P7 current-scope supervised-learning task and selects
docs-only current-scope closure criteria definition.
`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines those criteria, exit readiness, remaining docs/review/closure items,
deferred / blocked / not accepted items and P8-P12 non-entry conditions.
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
reviews `03S` and records `Review can close`.
`docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the P7 current-scope handoff and evidence index, records
conservative evidence-grade consistency and recommends the final P7
current-scope closure review gate next. `03V` now records that P7 current
scope can close only for the exact current scope. This remains non-evidence
for P7 broad implementation, training-data approval, source approval, parser,
dataset reader, ingestion, actual feature extraction, actual label generation,
supervised dataset construction, training, model architecture, trainer,
model-output integration, real data, CLI, self-play, league, P8-P12 entry,
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence. The next
task is `Define full P7 closure roadmap and remaining scope inventory after
current-scope closure`.
```

## Current methodology

The project uses a strict local Codex workflow:

```text
1. Load rules first.
2. Execute only the first unchecked task in docs/10_next/10_NEXT.md.
3. Do not skip stages.
4. Do not train or modify code unless the current task explicitly asks for it.
5. After each real task, update changelog, evidence/risk notes when needed, handoff and 10_NEXT.
```

Current execution charter:

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
```

Role split:

- Web ChatGPT Pro: solution design, research, review and decision support.
- Local Codex App: code, tests and documentation landing.
- Git + docs: only source of truth.

## Algorithm selection stance

Current interpretation:

```text
Do not fully train every candidate algorithm.
Use a racing funnel:
F0 candidate registration
F1 reproducibility audit
F2 interface/legal-action adapter
F3 offline scenario evaluation
F4 small self-play league
F5 medium promotion league
F6 mainline candidate gate
F7 LuckyJ target validation
```

Roles:

- LuckyJ: final benchmark target, not implementation seed.
- Suphx: main methodology blueprint, split into reproducible modules.
- Mortal: paused as a runnable baseline; retained as source-code, mjai-interface, methodology and engineering reference.
- Archer: high-potential Tenhou baseline candidate requiring verification.
- Akochan: secondary baseline/reviewer candidate; F1 Conditional Pass on Ubuntu GitHub Actions; F2 fixed-sample wrapper validation passed through real-exe workflow run `26629344590`. It remains an interface/reviewer candidate, not a strength baseline. Any broader evaluator/reviewer integration must be a separate task with license boundary review.
- Kanachan: data/model architecture reference; not direct Tenhou baseline until adapted.

Main technical route:

```text
Suphx-style SL + RL
+ Tenhou stable dan / pt EV reward
+ ACH-inspired policy improvement
+ risk model / search
+ baseline racing funnel
```

LuckyJ remains the target benchmark, not a direct full-reproduction object.

## Current next task

See:

```text
docs/10_next/10_NEXT.md
```

Latest Mortal F1 audit summary:

- GitHub connector could inspect `Equim-chan/Mortal` at commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- License is AGPL-3.0-or-later for code.
- Official inference path is mjai/Docker-oriented and requires a separate trained model artifact.
- System DNS still cannot resolve GitHub domains, but Mortal source tarball was obtained through `codeload.github.com` with explicit host resolution and checksum `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`.
- Normal `git clone` still failed; local `rustc`, `cargo`, `docker`, `conda` and PyTorch were not available.
- Official gist evidence says there is currently no plan to release trained model parameters.
- Minimal inference sample was not run; Mortal must remain at F1 Reproduce blocked.
- Current project decision: because there is no lawful, verifiable and usable Mortal trained model artifact, Mortal is paused as a runnable baseline.
- Do not use unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Mortal remains useful as source-code, mjai-interface, methodology and engineering reference.

Current expected direction:

```text
Review broader P7 scope, entry criteria and first task before implementation.
The broader-P7 scope / entry / first-task review must be docs-only. It must
not add production code, tests, fixtures, data files, parser, dataset reader,
ingestion, actual feature extraction, actual label generation, supervised
dataset construction, training, tuning, self-play, league, runner behavior,
real Tenhou, real haifu, external logs, platform data, model-output
integration, CLI, broad file ingestion, P8-P12 work or model-strength claims.
```

Latest Akochan F1 audit summary:

- GitHub repository `critter-mj/akochan` is public and inspectable.
- Clone URL: `https://github.com/critter-mj/akochan.git`.
- Default branch: `master`.
- Audited commit: `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Normal `git clone` failed because local DNS could not resolve `github.com`; clone with explicit `http.curloptResolve` succeeded in `/tmp/mjlabai_akochan_audit_20260529_084246`.
- License is a custom Japanese usage agreement, not a standard OSI license. Private research audit is allowed, but redistribution, AI-part modification, commercial use and public release are restricted and need review/permission.
- Build path is C++11 Makefile-based: build `ai_src` into `libai.so`, then root into `system.exe`.
- Dependencies include g++/clang++, OpenMP, Boost.System/Boost.Asio, pthread on Linux, Homebrew LLVM/Boost on macOS and repository-included `params/` text files.
- No external neural-network `*.pth`/`*.pt`/checkpoint/snapshot artifact was detected; 709 text parameter files are included under `params/`.
- Source exposes promising `mjai_log`, `stats_mjai`, `game_server`, `legal_action`, `legal_action_log_all`, `pipe`, `pipe_detailed` and `mjai_client` entry points.
- Local macOS ARM build failed: MacOS Makefile expects `/opt/homebrew/opt/llvm/bin/clang++`; Linux Makefile is incompatible with this macOS target due `/proc/cpuinfo`, `-mcmodel=medium` and `-fopenmp`.
- `mjai` CLI was not installed.
- No `system.exe` was produced, so minimal run was not executed.
- F1 conclusion: Blocked.

Latest Akochan F1 blocker-resolution attempt:

- Docker is not installed: `docker: command not found`.
- Host is macOS 26.2 / Darwin 25.2.0 on arm64.
- `/usr/bin/g++`, `/usr/bin/clang++` and `/usr/bin/make` exist, but `g++`/`clang++` are Apple clang 21.0.0.
- Homebrew exists, but usable Boost, LLVM and OpenMP/libomp files were not present under the expected `/opt/homebrew/opt/*` paths.
- Akochan was cloned outside the repository to `/tmp/mjlabai_akochan_build_audit` and checked out at `53188a0b926fbab38177f88c3cd87d554cf412af`.
- `make -f Makefile_MacOS` in `ai_src` failed because `/opt/homebrew/opt/llvm/bin/clang++` was missing.
- `make -f Makefile_Linux` in `ai_src` failed because `/proc/cpuinfo` is absent on macOS and Apple clang rejected `-mcmodel=medium` and `-fopenmp`.
- Root Makefile attempts failed for the same missing LLVM / unsupported OpenMP reasons.
- No `libai.so` or `system.exe` was generated, so no minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample was run.
- F1 conclusion remains: Blocked.

GitHub Actions support added:

- Added `.github/workflows/akochan-f1-build-audit.yml`.
- Workflow name: `Akochan F1 Build Audit`.
- Trigger: manual `workflow_dispatch` only.
- Inputs:
  - `akochan_commit`, default `53188a0b926fbab38177f88c3cd87d554cf412af`.
  - `run_minimal_samples`, default `true`.
- Runner: `ubuntu-latest`.
- The workflow installs Ubuntu build dependencies inside the temporary runner, clones `critter-mj/akochan` into the runner temp directory, checks out the requested commit, attempts `cd ai_src && make -f Makefile_Linux` and then `make -f Makefile_Linux` at the root.
- If `system.exe` is generated and `run_minimal_samples` is true, it runs only minimal non-training samples: `legal_action` and `mjai_log haifu_log_sample.json 0 2`.
- The workflow does not upload third-party source, `system.exe`, binaries or build artifacts.
- This workflow support entry was superseded by successful run `26617347785`, which moved Akochan to F1 Conditional Pass.

First GitHub Actions run review:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26615920289`.
- Result: failed during GitHub workflow validation before any Ubuntu runner build started.
- Cause: `.github/workflows/akochan-f1-build-audit.yml` used `runner.temp` inside job-level `env`, which GitHub did not accept at lines 27 and 28.
- Local fix: `AKOCHAN_DIR` and `SUMMARY_FILE` are now configured in a runtime shell step via `$GITHUB_ENV`; the final summary step has a fallback if the summary file was not created.
- Evidence impact: no `system.exe`, `legal_action` or `mjai_log` evidence was produced by the failed run. Akochan remains F1 Blocked.

Corrected GitHub Actions run review:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26617347785`.
- Commit: `b6b69e08fd009052cb3bbd16c779ac6e2139591b`.
- Result: success on `ubuntu-latest`.
- Generated: `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Minimal samples:
  - `legal_action`: success; emitted legal `dahai` JSON actions.
  - `mjai_log haifu_log_sample.json 0 2`: success; emitted parsed mjai/log JSON output.
- Guardrails: no training, tuning, self-play, Tenhou connection, adapter work, artifact upload or third-party vendoring.
- New risk note: GitHub emitted a Node.js 20 deprecation warning for `actions/checkout@v4`; this is workflow maintenance risk, not an Akochan F1 blocker.
- F1 conclusion: Conditional Pass. Akochan can move to F2 task definition, but custom license limits and Ubuntu-only build evidence must remain documented.

Akochan F2 task definition:

- Added `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`.
- Defined Akochan roles for F2: legal-action checker, mjai/log reviewer and baseline/reviewer candidate.
- Defined the interface boundary: Akochan source, `system.exe`, `libai.so`, `params/` and third-party build artifacts must not enter this repository.
- Future wrapper should call an external path or a GitHub Actions temporary build path.
- Defined draft mapping for mjai events: `start_game`, `start_kyoku`, `tsumo`, `dahai`, `chi`, `pon`, `kan`, `reach`, `hora`, `ryukyoku`, `end_kyoku`.
- Defined draft normalized internal action schema for `legal_action` outputs.
- Defined mandatory audit-log fields: tool name, external repo/commit, build environment, command, input/output hashes, exit code, stdout/stderr summaries, elapsed time and flags proving no training/self-play/Tenhou command was run.
- Reaffirmed license guardrails: private/internal audit only; no source modification, redistribution, commercial use or public release without review/permission.
- No adapter code was written in the F2 definition task.

Akochan F2 wrapper skeleton:

- Added a minimal Python package under `src/mjlabai`.
- Implemented `AkochanWrapper.run_legal_action(input_json)` and `AkochanWrapper.run_mjai_log(log_path, actor=0, mode=2)`.
- The wrapper accepts a real external `system.exe` path only through an explicit constructor argument or `AKOCHAN_SYSTEM_EXE`.
- The wrapper exposes only the two fixed subcommands: `legal_action` and `mjai_log`; it does not provide free-form command execution.
- Added audit-log dataclasses with required fields: tool name, external repo/commit, build environment, command, input/output hashes, exit code, stdout/stderr summaries, elapsed time and explicit no-training/no-self-play/no-Tenhou flags.
- Added a synthetic fixed `legal_action` fixture and a tiny synthetic mjai-log fixture.
- Added `tests/fixtures/akochan/fake_system_exe.py` as a test substitute only. It is not Akochan and is not model-strength evidence.
- Local smoke test `python3 -m unittest tests/adapters/test_akochan_wrapper.py` passed 14 tests after the allowlisted mixed stdout parser fix.
- No Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary, unknown model artifact or build artifact was stored in this repository.

Akochan F2 fixed-sample real-exe wrapper validation closeout:

- Workflow: `Akochan F2 Wrapper Real Exe Audit`.
- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26629344590`.
- Commit: `29f5e1ed19407d169f85524e05438ac8938d2dc2`.
- Commit message: `Support Akochan mixed stdout parsing`.
- Result: success.
- Job result: success.
- Successful evidence:
  - Ubuntu runner built `ai_src/libai.so`.
  - Ubuntu runner built root `libai.so`.
  - Ubuntu runner built `system.exe`.
  - Fake wrapper tests passed 14 tests.
  - Real `system.exe legal_action` wrapper test passed.
  - Real `system.exe mjai_log` wrapper test passed.
  - Allowlisted mixed stdout parser was verified by the real workflow.
- Guardrails:
  - No training.
  - No tuning.
  - No self-play, match or league command.
  - No real Tenhou connection.
  - No Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary or build artifact was stored or uploaded.
- Interpretation:
  - Akochan status is F1 Conditional Pass plus F2 fixed-sample wrapper validation passed.
  - This is not playing-strength evidence.
  - This does not make Akochan a mainline baseline or prove mjlabai strength.
  - Akochan custom license still restricts modification, redistribution, commercial use and public release.
  - GitHub Actions reported a Node.js 20 deprecation warning; this is workflow maintenance risk and does not affect the F2 validation result.

Akochan F2 real executable validation path:

- Added `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`.
- Workflow name: `Akochan F2 Wrapper Real Exe Audit`.
- Trigger: manual `workflow_dispatch` only.
- Input:
  - `akochan_commit`, default `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Runner: `ubuntu-latest`.
- The workflow checks out mjlabai, installs Ubuntu build dependencies, clones `critter-mj/akochan` into the runner temporary directory, checks out the fixed commit, builds `ai_src/libai.so`, root `libai.so` and `system.exe`, installs mjlabai with `python -m pip install -e .`, then runs both fake wrapper tests and real-executable wrapper tests.
- Added `tests/adapters/test_akochan_wrapper_real_exe.py`.
- Real-executable tests skip locally unless `AKOCHAN_SYSTEM_EXE` is set. The `mjai_log` test also requires `AKOCHAN_MJAI_LOG_SAMPLE`.
- Local validation:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed after the allowlisted mixed stdout parser fix.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped, as expected without a real external executable.
- The wrapper parser now supports single JSON values, JSON Lines, concatenated JSON values, pretty-printed multi-record JSON streams and mixed stdout with the single allowlisted status line `calculating review`.
- The parser preserves `raw_stdout`, exposes `parsed_records`, records `parse_warnings` and `skipped_non_json_lines`, and rejects unknown non-JSON lines or partial parses.
- First workflow run `26621536548` was run and reviewed; it failed only at the real `mjai_log` wrapper test because `system.exe` could not load `setup_mjai.json` from the current working directory.
- Working-directory fix has been implemented locally:
  - `AkochanWrapper` supports explicit `working_dir`, then `AKOCHAN_WORKING_DIR`, then defaults to `Path(system_exe).resolve().parent`.
  - `_run_subcommand` passes `cwd=self.working_dir` to `subprocess.run`.
  - `AkochanAuditLog` records `working_dir`.
  - Fake tests verify default, explicit and environment-variable working-directory behavior.
  - The workflow now exports `AKOCHAN_WORKING_DIR=${AKOCHAN_DIR}` before real-exe tests.
- The workflow does not upload artifacts; any Akochan clone/build output remains in the temporary GitHub runner.

First Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26621536548`.
- Commit: `7d58f969367d3e51c57d859dbfb9433f1ca898a1`.
- Result: failure.
- Successful evidence:
  - Akochan source cloned at `53188a0b926fbab38177f88c3cd87d554cf412af`.
  - `ai_src/libai.so`, root `libai.so` and `system.exe` built successfully.
  - Fake wrapper smoke tests passed.
  - Real `legal_action` wrapper test passed.
- Failed evidence:
  - Real `mjai_log` wrapper test failed.
- Failure detail:
  - `AkochanWrapperError: Akochan command failed with exit code -6: error:load_json_from_file setup_mjai.json`.
  - `system.exe` asserted while loading `setup_mjai.json`.
- Interpretation:
  - The wrapper called external `system.exe` from the mjlabai checkout working directory.
  - Akochan expects runtime config files such as `setup_mjai.json` to be visible from the process working directory.
  - Next fix should set the subprocess working directory to the executable directory or an explicitly provided external working directory.
- Evidence status:
  - This is real `legal_action` wrapper compatibility evidence.
  - This is not successful real `mjai_log` wrapper compatibility evidence.
  - This is not strength evidence.

Akochan F2 working-directory fix:

- Wrapper behavior:
  - Constructor priority is explicit `working_dir`, then `AKOCHAN_WORKING_DIR`, then `Path(system_exe).resolve().parent`.
  - Missing or non-directory working directories fail with a clear error.
  - The external subprocess is launched with `cwd=self.working_dir`.
  - Audit logs include the actual `working_dir`.
- Test behavior:
  - `fake_system_exe.py` now requires a synthetic `fake_setup_mjai.json` in cwd for `mjai_log`, proving the cwd boundary is exercised.
  - Local fake tests passed 8 tests.
  - Local real-exe tests skipped 2 tests as expected without real Akochan.
- Current evidence gap:
  - Workflow run `26623247276` confirmed `AKOCHAN_WORKING_DIR` removes the `setup_mjai.json` failure.
  - The first parser blocker was improved locally, but workflow run `26628128871` exposed the known `calculating review` status line.

Second Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26623247276`.
- Commit: `0ddb28575ddd1b624cad34b20d6dc6b79303963c`.
- Result: failure.
- Successful evidence:
  - Akochan source cloned at `53188a0b926fbab38177f88c3cd87d554cf412af`.
  - `ai_src/libai.so`, root `libai.so` and `system.exe` built successfully.
  - Fake wrapper smoke tests passed 8 tests.
  - `AKOCHAN_SYSTEM_EXE`, `AKOCHAN_WORKING_DIR` and `AKOCHAN_MJAI_LOG_SAMPLE` were configured.
  - Real `legal_action` wrapper test passed.
  - Real `mjai_log` no longer failed on `setup_mjai.json`.
- Failed evidence:
  - Real `mjai_log` wrapper test failed while parsing stdout.
- Failure detail:
  - `AkochanOutputParseError: Akochan stdout was not parseable JSON or JSON Lines: Extra data: line 2 column 1`.
- Interpretation:
  - The cwd/runtime-file blocker is mitigated.
  - The next issue is understanding and parsing the real multi-record `mjai_log` stdout shape while preserving raw output and bounded summaries.
- Evidence status:
  - This is real `legal_action` compatibility evidence and cwd-fix evidence.
  - This is not successful real `mjai_log` wrapper compatibility evidence.
  - This is not strength evidence.

Akochan F2 strict JSON stream parser fix:

- Parser behavior:
  - single JSON value returns that value with `parsed_records=[value]`;
  - JSON Lines and concatenated/pretty multi-record JSON streams return `parsed_json=records` and `parsed_records=records`;
  - any non-whitespace non-JSON residue fails instead of being accepted as a partial parse.
- Diagnostics:
  - parse failures include bounded stdout summary, stdout SHA256, failure position and parsed-record count.
- Local tests:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 12 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Current evidence gap:
  - Workflow run `26628128871` must be interpreted before real `mjai_log` compatibility can be closed.

Third Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26628128871`.
- Commit: `9f51aff1ab403e8053ab71fe1db7587bf7af01cf`.
- Result: failure.
- Successful evidence:
  - Ubuntu runner built `ai_src/libai.so`, root `libai.so` and `system.exe`.
  - Fake wrapper tests passed 12 tests.
  - Real `legal_action` wrapper test passed.
  - Real `mjai_log` launched with `AKOCHAN_WORKING_DIR` and produced parseable JSON records before the status line.
- Failed evidence:
  - Real `mjai_log` wrapper test failed on mixed stdout containing JSON records, then `calculating review`, then JSON review output.
- Interpretation:
  - Strict JSON stream support is not enough for real `mjai_log`.
  - The parser may skip only the exact known status line `calculating review`, record that skip, and continue strict JSON stream parsing.
  - Unknown non-JSON lines and partial parses must remain failures.

Akochan F2 allowlisted mixed stdout parser fix:

- Parser behavior:
  - single JSON value returns that value with `parsed_records=[value]`;
  - JSON Lines and concatenated/pretty multi-record JSON streams return `parsed_json=records` and `parsed_records=records`;
  - mixed stdout may skip only the exact non-JSON status line `calculating review`;
  - `skipped_non_json_lines` records skipped allowlisted lines;
  - unknown non-JSON residue and partial parses still fail.
- Diagnostics:
  - parse failures include bounded stdout summary, stdout SHA256, failure position, parsed-record count and skipped-status-line count.
- Local tests:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Real workflow validation:
  - Workflow run `26629344590` verified real `legal_action` and real `mjai_log` wrapper tests both pass after allowlisted mixed stdout parser support.

Fourth Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26629344590`.
- Commit: `29f5e1ed19407d169f85524e05438ac8938d2dc2`.
- Result: success.
- Successful evidence:
  - Ubuntu runner built `ai_src/libai.so`.
  - Ubuntu runner built root `libai.so`.
  - Ubuntu runner built `system.exe`.
  - Fake wrapper tests passed 14 tests.
  - Real `legal_action` wrapper test passed.
  - Real `mjai_log` wrapper test passed.
- Interpretation:
  - Akochan F2 fixed-sample real-exe wrapper validation is complete.
  - This is fixed-sample integration evidence only, not strength evidence.
  - Further evaluator/reviewer integration must be a separate scoped task with license guardrails.

## Do not forget

- The final metric is not loss.
- The final metric is not action prediction accuracy.
- The final metric is Tenhou-like strength: stable dan, pt EV, average placement and fourth-place control.
- No candidate can be promoted without evidence and a rollback path.
- Current next work is a docs-only post-full-P6 transition review before
  defining any P7 task. Full P6 is closed only for the documented P6
  data-system scope, and that closure is not P7-P12 entry approval. Do not
  implement fixture files, tests, replay schema code, parser, dataset reader,
  ingestion, feature extraction, label generation, CLI, model-output
  integration, train, tune, self-play, league, connect to real Tenhou or treat
  closure as model-strength evidence.
- Technical decisions from Web ChatGPT Pro must be written into Git + docs before becoming project facts.
