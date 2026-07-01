# 12A_TECHNICAL_PLAN_v0.1

## Purpose

本文件是当前项目执行总纲。

项目从这一版开始采用：

```text
技术方案优先，论文未来总结。
```

含义：

- 技术方案用于指导当前阶段、任务拆分、实验选择、代码落地和评测闭环。
- 论文不是当前执行主线；论文是未来当路线、证据、评测和结论足够稳定之后的成果总结。
- 任何代码、实验、baseline、训练或评测都必须先能说明它如何服务北极星目标。

North-star target:

```text
Train a Japanese riichi mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum benchmark: above Tenhou 10 dan and stable dan > 10.68.
```

## Current Stage

当前项目处于：

```text
P7 minimal synthetic/local parser-reader smoke extension implementation review
gate.
The exact `03BA`-approved extension is now implemented in
`src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py` and tested
in `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`.
The extension accepts only already-loaded in-memory project-authored
synthetic/local smoke records, delegates each record to the existing
parser-reader smoke validation path, rejects top-level and per-record
path-like inputs, rejects empty record sequences, aggregates JSON-safe
manifest guardrail summaries and emits no feature tensors, labels, targets,
supervised examples, datasets, splits, model input, model output, evaluation
result or model-strength fields. No fixture/data file, existing parser-reader
smoke logic, feature-label schema, replay schema, source approval, source
ingestion, broad parser / reader / ingestion, CLI, actual feature extraction,
actual label generation, supervised dataset construction, split creation,
leakage-test implementation, training data, training, model architecture /
trainer implementation, evaluation implementation, metric implementation,
evaluation runner, benchmark harness, model-output integration, real data,
self-play, league or P8-P12 work was added. The next task is `Review P7
minimal synthetic/local parser-reader smoke extension implementation`.

Earlier context:
The exact `03AU`-approved implementation added
`src/mjlabai/supervised/synthetic_parser_reader_smoke.py` and
`tests/supervised/test_synthetic_parser_reader_smoke.py`. The helper accepts
only already-loaded in-memory project-authored synthetic/local feature-label
smoke mappings, delegates guardrail validation to `feature_label_schema`,
rejects path-like inputs, real-data flags, model-output flags, source-approval
claims, hidden/future information and non-JSON-safe values, and returns only a
JSON-safe guardrail summary. It emits no feature tensors, labels, targets,
supervised examples, datasets, splits, model input, model output, evaluation
result or model-strength fields.
`docs/03_supervised_policy/03AV_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_REVIEW.md`
reviews the exact implementation, records `Review can close`, confirms
validation passed and finds no blocker. The 2026-07-01 current-scope
acceptance decision is `ACCEPTED as current-scope complete` for that exact
synthetic/local parser-reader smoke scope only.
`docs/03_supervised_policy/03AW_P7_FULL_SCOPE_EXPANSION_PLAN_AFTER_CURRENT_SCOPE_ACCEPTANCE.md`
now defines the full P7 expansion plan: accepted scope, non-approved scope,
workstream inventory, expansion sequence, candidate future implementation
classes, deferred / blocked / later-stage inventory, risk controls, evidence
requirements and full P7 closure preparation. `03AW` is planning evidence
only and does not approve source approval, ingestion, feature extraction,
label generation, dataset construction, training, evaluation, real data,
model-output integration, self-play, league or P8-P12.
`docs/03_supervised_policy/03AX_P7_FULL_SCOPE_EXPANSION_PLAN_REVIEW_AFTER_CURRENT_SCOPE_ACCEPTANCE.md`
reviews `03AW`, records `Review can close`, and keeps every implementation
and evidence boundary unapproved.
`docs/03_supervised_policy/03AY_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_AFTER_FULL_SCOPE_REVIEW.md`
drafts a P7 minimal implementation proposal for a project-authored
synthetic/local parser-reader smoke extension candidate. It records exact
goals, non-goals, candidate future files, input/output boundaries, dependency
status, validation commands, rollback, stop conditions, risk controls,
evidence grade and approval separation. It is proposal draft evidence only
and does not approve the proposal, implementation, source approval, source
ingestion, feature extraction, label generation, dataset construction,
training, evaluation, real data or P8-P12.
`docs/03_supervised_policy/03AZ_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`
reviews `03AY`, records `Review can close`, and confirms that the proposal is
clear enough for a separate approval-decision preparation task. `03AZ` does
not approve the proposal, approve implementation, generate implementation,
add code, add tests, add fixtures, add data files, approve source approval,
approve ingestion, approve feature extraction, approve label generation,
approve dataset construction, approve training, approve evaluation, approve
model-output integration, approve real data or approve P8-P12. The next task
was `Prepare approval decision for P7 minimal synthetic/local parser-reader
smoke extension implementation`. `03BA` records that approval decision:
`Approved for next exact minimal implementation task.` It approves only the
future task `Implement P7 minimal synthetic/local parser-reader smoke
extension only`, only
`src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`,
`tests/supervised/test_synthetic_parser_reader_smoke_extension.py` and direct
docs/governance synchronization. It does not execute implementation, approve
broader P7 implementation, source approval, source ingestion, broad parser /
reader / ingestion, actual feature extraction, actual label generation,
dataset construction, training, evaluation, model-output integration, real
data, self-play, league or P8-P12. The next task is `Implement P7 minimal
synthetic/local parser-reader smoke extension only`.
P5 evaluation foundation is closed for the current synthetic/local scope.
General P6 data-system implementation is not open; the exact minimal replay
schema and project-authored synthetic fixture task approved by `02N` is
implemented, reviewed with no blocker and accepted as current-scope complete in
`02P`; `02Q` selected a docs-only current-scope closure-criteria task, `02R`
defined those criteria, `02S` reviewed them with no blocker and `02T` closed
the accepted current-scope P6 synthetic/local minimal replay schema and
project-authored synthetic fixture scope only. `02AA` closes full P6 only for
the documented P6 data-system scope: docs/governance/source-rights planning,
accepted synthetic/local minimal replay schema and project-authored synthetic
fixture smoke implementation, and deferred/blocked/later-stage inventory.
P7 current scope is closed only for the exact docs-only readiness chain plus
the accepted minimal synthetic/local supervised feature-label smoke
implementation reviewed in `03P`, accepted in `03Q`, bounded by `03S`/`03T`,
finalized in `03U`, and closed for current scope in `03V`. Full P7 remains
open. P7 broad implementation remains unapproved beyond the exact `03O`
minimal synthetic/local smoke task; P8-P12 entry remains unapproved. `12E`
completes the post-current-scope P7 transition review and selects the next
docs-only task: define a full P7 closure roadmap and remaining scope inventory
after current-scope closure. `03W` defines that roadmap and inventory,
classifies full-P7 remaining items as required / deferred / blocked /
later-stage / out of scope, and selects a docs-only roadmap review gate next.
`03X` reviews that roadmap / inventory with no blocker and records `Review can
close`. The follow-up was docs-only broader P7 scope, entry criteria and
first-task definition before implementation. `03Y` defines that broader P7 scope,
entry criteria and first task before implementation. It records required
implementation entry criteria, required upstream artifacts, blocked /
deferred / later-stage / out-of-scope items, reasons not to implement or
train yet, and reasons not to enter P8-P12. `03Z` reviews `03Y`, records
`Review can close` and selects the next docs-only task: define broader P7
data/source readiness and source-approval boundary before implementation.
`03AA` defines that broader P7 data/source readiness and source-approval
boundary and selects a docs-only review gate next. `03AB` reviews that boundary
and records `Review can close`; it selects `Define broader P7 parser, reader
and ingestion boundary before implementation` as the next docs-only task.
`03AC` defines that boundary and selects a docs-only review gate next. `03AD`
reviews that boundary, records `Review can close` with no blocker and selects
`Define broader P7 actual feature extraction and label generation boundary
before implementation` as the next docs-only task. `03AE` defines that
feature / label boundary and selects a docs-only review gate next. `03AF`
reviews that boundary, records `Review can close` with no blocker and selects
`Define broader P7 supervised dataset construction, split and leakage boundary
before implementation` as the next docs-only task. `03AG` defines that
dataset / split / leakage boundary and selects a docs-only review gate next.
`03AH` reviews `03AG`, records `Review can close` with no blocker and selects
`Define broader P7 training-data approval and training-run boundary before
implementation` as the next docs-only task. `03AI` defines that
training-data approval / training-run boundary and selects a docs-only review
gate next. `03AJ` reviews `03AI`, records `Review can close` with no blocker
and selects `Define broader P7 model architecture and trainer planning
boundary before implementation` as the next docs-only task. `03AK` defines
that model architecture / trainer planning boundary and selects a docs-only
review gate next. `03AL` reviews `03AK`, records `Review can close` with no
blocker and selects `Define broader P7 evaluation dependency and
model-strength evidence boundary before implementation` as the next docs-only
task. `03AM` defines that evaluation dependency / model-strength evidence
boundary and selects a docs-only review gate next. `03AN` reviews `03AM`,
records `Review can close` with no blocker and selects `Define broader P7
implementation readiness checklist after boundary-chain review` as the next
docs-only task. `03AO` defines that readiness checklist, summarizes the
reviewed boundary chain from `03Y` through `03AN`, defines readiness status
vocabulary, required upstream artifacts, candidate implementation class
statuses, future proposal fields, future approval-decision fields, stop
conditions, risk controls, evidence requirements and records that no broader
P7 implementation class is approved now. The next task is `Review broader P7
implementation readiness checklist after boundary-chain review`. `03AP`
reviews `03AO`, records `Review can close` with no blocker, and selects
`Define broader P7 minimal implementation proposal boundary after readiness
checklist review` as the next docs-only task. That next task may define a
future proposal boundary only; it does not approve a proposal or
implementation. `03AQ` defines that proposal boundary, including proposal
lifecycle vocabulary, candidate proposal classes, required proposal sections,
exact-scope requirements, forbidden proposal scope, approval-decision
separation, approval prerequisites, stop conditions, risk controls and
evidence requirements. The next task is `Review broader P7 minimal
implementation proposal boundary after readiness checklist review`. `03AR`
reviews that proposal-boundary definition, records `Review can close` with no
blocker and selects `Draft broader P7 minimal implementation proposal for
review after proposal-boundary review` as the next docs-only task. `03AS`
drafts that proposal for later review, selects `Project-authored
synthetic/local parser-reader smoke proposal` as the most conservative
proposal-boundary-eligible candidate and records that the proposal is drafted
but not approved. The next task is `Review broader P7 minimal implementation
proposal before approval decision`. `03AT` reviews that proposal, records
`Review can close` with no blocker and selects `Prepare approval decision for
broader P7 minimal synthetic/local parser-reader smoke implementation` as the
next docs-only task. `03AU` records that approval decision: `Approved for next
exact minimal implementation task.` The approved next task is limited to
`Implement broader P7 minimal synthetic/local parser-reader smoke only` and
the exact files `src/mjlabai/supervised/synthetic_parser_reader_smoke.py` and
`tests/supervised/test_synthetic_parser_reader_smoke.py`, plus direct
docs/governance synchronization.
None of `03Y`, `03Z`, `03AA`, `03AB`, `03AC`, `03AD`, `03AE`, `03AF`, `03AG`,
`03AH`, `03AI`, `03AJ`, `03AK`, `03AL`, `03AM`, `03AN`, `03AO`, `03AP`,
`03AQ`, `03AR`, `03AS` or `03AT` approves an implementation. `03AU` approves
only the next exact synthetic/local parser-reader smoke task and exact files;
it does not approve broad P7 implementation, training, source approval, source
ingestion, broad parser / reader / ingestion implementation, actual feature
extraction, actual label generation, feature tensors, labels, targets,
examples, splits, supervised dataset construction, leakage-test
implementation, training-data construction, training-run approval, model
architecture / trainer implementation, dataloader / optimizer / loss
implementation, checkpoint / weights creation, evaluation implementation,
model-strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ
comparison, real data, model-output integration, self-play, league or P8-P12.
Mortal = F1 paused as runnable baseline / ReferenceOnly.
Akochan = F1 Conditional Pass; F2 fixed-sample real-exe wrapper validation passed in workflow run `26629344590`; not strength evidence.
Tenhou stable-dan calculator = deterministic point estimate implemented and tested.
Tenhou stable-dan bootstrap CI = percentile empirical multinomial bootstrap implemented and tested.
Tenhou stable-dan threshold helper = LuckyJ 10.68 lower-bound comparison implemented and tested.
Tenhou stable-dan reporting schema = minimum sample-size guardrails and report schema implemented and tested.
Tenhou stable-dan placement aggregation = offline placement-count helper implemented and tested.
Tenhou stable-dan report smoke fixture = CLI-free synthetic placement fixture implemented and tested.
Tenhou stable-dan evaluation API docs = synthetic placement example added.
Tenhou stable-dan evaluation groundwork = complete for current P5 scope.
P5 offline evaluation metric registry and result envelope schema = implemented/tested.
Offline evaluation envelope smoke fixture = synthetic stable-dan envelope smoke test implemented.
P5 legal-action / invalid-action metric specification = defined.
P5 action canonicalization schema for legal-action metric fixtures = defined.
Synthetic legal-action metric fixture schema smoke test = implemented.
P5 legal-action metric synthetic evaluator boundary = defined.
P5 overall = closed for the current synthetic/local evaluation groundwork scope.
P5 synthetic legal-action evaluator = implemented for project-authored fixture only.
P5 synthetic parse-failure fixture coverage = implemented.
P5 legal-action synthetic evaluator coverage review = complete for current synthetic-only dahai + strict scope.
P5 tiny benchmark harness boundary = defined before implementation.
P5 tiny benchmark harness synthetic fixture schema smoke test = implemented.
P5 tiny benchmark fixture schema coverage review = complete.
P5 tiny benchmark harness = implemented for project-authored synthetic fixture only.
P5 tiny benchmark harness implementation review = complete.
P5 offline envelope coverage review for synthetic tiny benchmark diagnostics = complete.
P5 metric registry consistency review across stable-dan, legal-action and tiny benchmark diagnostics = complete.
P5 synthetic/local evidence taxonomy and promotion guardrails review = complete.
P5 evaluation groundwork closure criteria and exit readiness checklist = defined.
P5 evaluation groundwork closure criteria and exit readiness checklist review = complete; no blocker found.
P5 handoff and evidence index finalization = complete; no blocker found.
P5 final closure review gate = complete; P5 can close for current synthetic/local evaluation groundwork scope.
Post-P5 transition review = complete.
P6 data-system scope / entry criteria / first task definition = complete as docs-only planning.
P6 data-source provenance and rights inventory = defined and reviewed before replay schema implementation; no blocker found.
P6 replay schema documentation boundary = defined after source inventory review; implementation remains closed.
P6 replay schema documentation boundary review = complete; no blocker found; implementation remains closed.
P6 synthetic/local replay fixture boundary = defined before schema implementation; fixture implementation remains closed.
P6 synthetic/local replay fixture boundary review = complete; no blocker found; fixture implementation remains closed.
P6 replay schema and fixture implementation readiness checklist = defined before code; implementation remains closed.
P6 replay schema and fixture implementation readiness checklist review = complete; no blocker found; implementation remains closed.
P6 replay schema and synthetic fixture implementation proposal boundary = defined before code; implementation remains closed.
P6 replay schema and synthetic fixture implementation proposal boundary review = complete; no blocker found; implementation remains closed.
P6 minimal replay schema and synthetic fixture implementation proposal = prepared for review before code; implementation remains closed.
P6 minimal replay schema and synthetic fixture implementation proposal review = complete; no blocker found; implementation remains closed.
P6 minimal replay schema and synthetic fixture implementation approval decision = complete.
P6 minimal replay schema and project-authored synthetic fixture implementation = complete in exact approved files only.
P6 minimal replay schema and project-authored synthetic fixture implementation review = complete; no blocker found.
P6 minimal replay schema and project-authored synthetic fixture current-scope acceptance decision = complete; accepted as current-scope complete.
P6 next current-scope data-system task definition = complete; selected a docs-only closure-criteria task.
P6 current-scope data-system closure criteria = defined after minimal replay schema acceptance.
P6 current-scope data-system closure criteria review = complete; no blocker found.
P6 final current-scope data-system closure review = complete; accepted current-scope closed.
P6 post-current-scope transition review = complete; full P6 remains open and
P7-P12 remains unapproved.
P6 full closure roadmap and remaining scope inventory = defined in `02U`;
full P6 remains open and P7-P12 remains unapproved.
P6 full closure roadmap and remaining scope inventory review = complete in
`02V`; review can close with no blocker.
P6 full closure criteria after roadmap and remaining scope review = defined in
`02W`; full P6 remains open and P7-P12 remains unapproved.
P6 full closure criteria review after roadmap and remaining scope review =
complete in `02X`; review can close with no blocker.
P6 full handoff and evidence index finalization after closure criteria review =
complete in `02Y`; full P6 remains open and P7-P12 remains unapproved.
P6 full risk register and source-rights inventory consistency review before
final closure = complete in `02Z`; review can close with no blocker for final
full P6 closure review.
Final full P6 closure review = complete in `02AA`; Full P6 can close for the
documented P6 data-system scope only.
Post-full-P6 transition review = complete in `12D`; the next task may define
P7 scope, entry criteria and first task as docs-only planning before
implementation.
P7 scope, entry criteria and first task = defined in
`docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` as
docs-only planning before implementation.
P7 scope, entry criteria and first task review = complete in
`docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`;
review can close with no blocker.
P7 supervised-learning data/source readiness inventory = defined in
`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`;
no source is currently approved for P7 training, source ingestion, parser /
reader / ingestion, feature extraction or label generation.
P7 supervised-learning data/source readiness inventory review = complete in
`docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`;
review can close with no blocker.
P7 feature and label readiness boundary = defined in
`docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`;
feature extraction, label generation, parser, dataset reader, ingestion,
training, real data and model-output integration remain unapproved.
P7 feature and label readiness boundary review = complete in
`docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`;
review can close with no blocker.
P7 supervised-learning risk and evidence taxonomy = defined in
`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`;
P7 implementation, source approval, feature extraction, label generation,
training, model-strength claims and P8-P12 entry remain unapproved.
P7 supervised-learning risk and evidence taxonomy review = complete in
`docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`;
review can close with no blocker. The next task is proposal definition only,
not implementation.
P7 minimal synthetic/local supervised fixture and feature-label smoke proposal =
defined in
`docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`;
candidate files are named for future review only and are not created. Fixture
creation, tests, production code, data files, source approval, parser / reader
/ ingestion, feature extraction, label generation, training, model-output
integration, real data, self-play, league and P8-P12 entry remain unapproved.
P7 minimal synthetic/local supervised fixture and feature-label smoke proposal
review = complete in
`docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md`;
review can close with no blocker. Implementation, fixture creation, tests,
production code, data files, source approval, parser / reader / ingestion,
feature extraction, label generation, training, model-output integration, real
data, self-play, league and P8-P12 entry remain unapproved.
P7 minimal synthetic/local supervised fixture and feature-label smoke
implementation approval decision = complete in
`docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`;
decision: `Approved for next minimal implementation task.` The approval is
limited to the exact next implementation task and exact files named in `03O`.
It does not execute implementation, approve parser / reader / ingestion,
approve actual feature extraction, approve actual label generation, approve
training, approve model-output integration, approve real data or approve
P8-P12 entry.
P7 minimal synthetic/local supervised fixture and feature-label smoke
implementation = complete in
`src/mjlabai/supervised/feature_label_schema.py`,
`tests/fixtures/supervised/synthetic_supervised_smoke.json`,
`tests/supervised/test_feature_label_schema.py` and
`tests/supervised/test_synthetic_supervised_fixture_schema.py`; it validates
only JSON-safe synthetic/local smoke mappings, candidate feature/label
families, public-information-only placeholders, absent hidden/future
information guardrails, all-false non-evidence flags and unsafe provenance
rejection.
P7 minimal synthetic/local supervised fixture and feature-label smoke
implementation review = complete in
`docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`;
review can close with no blocker. It does not approve broad P7 implementation,
source approval, parser / reader / ingestion, actual feature extraction,
actual label generation, training, real data, model-output integration or
P8-P12 entry.
P7 minimal synthetic/local supervised feature-label smoke current-scope
acceptance decision = complete in
`docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`;
decision `Accepted as current-scope complete` for the exact minimal
synthetic/local smoke scope only. It does not approve broad P7 implementation,
training, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, real data, model-output integration or
P8-P12 entry.
P7 next current-scope supervised-learning task definition = complete in
`docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`;
selected docs-only current-scope closure criteria definition to avoid endless
readiness / schema churn. It does not approve broad P7 implementation,
training, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, real data, model-output integration or
P8-P12 entry.
P7 current-scope closure criteria = defined in
`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`;
defines accepted current-scope inventory, C1-C26 criteria, exit readiness,
remaining docs/review/closure items, deferred / blocked / not accepted items,
validation commands and P8-P12 non-entry conditions. It does not close P7
current scope or approve broad P7 implementation, training, source ingestion,
parser / reader / ingestion, actual feature extraction, actual label
generation, real data, model-output integration or P8-P12 entry.
P7 current-scope closure criteria review = complete in
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`;
review decision `Review can close`. It does not close P7 current scope or
approve broad P7 implementation, training, source ingestion, parser / reader /
ingestion, actual feature extraction, actual label generation, real data,
model-output integration or P8-P12 entry.
P7 current-scope handoff and evidence index finalization = complete in
`docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`;
it finalizes the P7 current-scope handoff and evidence index, records no
risk/evidence consistency blocker and recommends the final current-scope
closure review gate. It does not close P7 current scope or approve broad P7
implementation, training, source ingestion, parser / reader / ingestion,
actual feature extraction, actual label generation, real data, model-output
integration or P8-P12 entry.
P7 final current-scope closure review = complete in
`docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md`;
decision `P7 current scope can close` for the exact current scope only:
docs-only supervised-learning readiness chain plus the accepted minimal
synthetic/local supervised feature-label smoke implementation. This does not
close full P7 or approve broad P7 implementation, training, source ingestion,
parser / reader / ingestion, actual feature extraction, actual label
generation, model architecture / trainer, real data, model-output integration
or P8-P12 entry.
P7 post-current-scope transition review = complete in
`docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md`;
full P7 remains open and the next task is docs-only full P7 closure roadmap /
remaining-scope inventory.
P7 full closure roadmap and remaining scope inventory = defined in
`docs/03_supervised_policy/03W_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_AFTER_CURRENT_SCOPE_CLOSURE.md`;
full P7 remains open.
P7 full closure roadmap and remaining scope inventory review = complete in
`docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md`;
review can close with no blocker.
Broader P7 scope / entry criteria / first task = defined in
`docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
and reviewed in
`docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 data/source readiness and source-approval boundary = defined in
`docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
and reviewed in
`docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 parser / reader / ingestion boundary = defined in
`docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`;
reviewed in
`docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 actual feature extraction and label generation boundary = defined
in `docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
and reviewed in
`docs/03_supervised_policy/03AF_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 supervised dataset construction, split and leakage boundary =
defined in
`docs/03_supervised_policy/03AG_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
Broader P7 supervised dataset construction, split and leakage boundary review =
complete in
`docs/03_supervised_policy/03AH_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 training-data approval and training-run boundary = defined in
`docs/03_supervised_policy/03AI_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_BEFORE_IMPLEMENTATION.md`;
no training data is approved, no training run is approved and the next task is
a docs-only review gate.
Broader P7 training-data approval and training-run boundary review = complete
in
`docs/03_supervised_policy/03AJ_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 model architecture and trainer planning boundary = defined in
`docs/03_supervised_policy/03AK_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_BEFORE_IMPLEMENTATION.md`;
no model architecture, trainer, dataloader, optimizer, loss, checkpoint,
weights, training data, training run or training is approved.
Broader P7 model architecture and trainer planning boundary review = complete
in
`docs/03_supervised_policy/03AL_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 evaluation dependency and model-strength evidence boundary =
defined in
`docs/03_supervised_policy/03AM_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_BEFORE_IMPLEMENTATION.md`;
no evaluation implementation, metric implementation, evaluation runner,
benchmark harness, model-output integration, model-strength evidence, Tenhou
evidence, stable-dan evidence, LuckyJ comparison or candidate promotion is
approved.
Broader P7 evaluation dependency and model-strength evidence boundary review =
complete in
`docs/03_supervised_policy/03AN_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`;
review can close with no blocker.
Broader P7 implementation readiness checklist = defined in
`docs/03_supervised_policy/03AO_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_AFTER_BOUNDARY_CHAIN_REVIEW.md`;
no broader P7 implementation class is approved and the next task is a docs-only
review gate.
Broader P7 implementation readiness checklist review = complete in
`docs/03_supervised_policy/03AP_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW_AFTER_BOUNDARY_CHAIN_REVIEW.md`;
review can close with no blocker, and the next task is a docs-only minimal
implementation proposal-boundary definition.
Broader P7 minimal implementation proposal boundary = defined in
`docs/03_supervised_policy/03AQ_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_AFTER_READINESS_CHECKLIST_REVIEW.md`;
no proposal or broader P7 implementation is approved, and the next task is a
docs-only proposal-boundary review gate.
Broader P7 minimal implementation proposal-boundary review = complete in
`docs/03_supervised_policy/03AR_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW_AFTER_READINESS_CHECKLIST_REVIEW.md`;
review can close with no blocker, and the next task is docs-only proposal
drafting for later review.
Broader P7 minimal implementation proposal draft = complete in
`docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`;
proposal is drafted for review only, not approved, and the next task is
docs-only proposal review before approval decision.
Broader P7 minimal implementation proposal review = complete in
`docs/03_supervised_policy/03AT_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`;
review can close with no blocker and the next task is docs-only
approval-decision preparation for the synthetic/local parser-reader smoke
candidate.
Broader P7 minimal synthetic/local parser-reader smoke approval decision =
complete in
`docs/03_supervised_policy/03AU_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`;
approved only the next exact implementation task and exact two implementation
files, with no fixture/data file by default.
Broader P7 minimal synthetic/local parser-reader smoke implementation =
complete in the exact approved files only; implementation review complete in
`03AV` with `Review can close`; the 2026-07-01 current-scope acceptance
decision is `ACCEPTED as current-scope complete` for that exact
synthetic/local parser-reader smoke scope only.
P7 full scope expansion plan = defined in `03AW` and reviewed in `03AX`;
review can close with no blocker.
P7 minimal implementation proposal = drafted in `03AY` for review only;
proposal and implementation remain unapproved.
P7 minimal implementation proposal review = complete in `03AZ`; review can
close with no blocker and the next task is docs-only approval-decision
preparation.
P7 minimal synthetic/local parser-reader smoke extension approval decision =
complete in `03BA`; approved only the next exact implementation task and exact
two future files, with no fixture/data file by default.
P7 minimal synthetic/local parser-reader smoke extension implementation =
complete in exact approved files only; no fixture/data file, real data,
source ingestion, feature extraction, label generation, dataset construction,
training, evaluation, model-output integration, self-play, league or P8-P12
was added.
P7 broad implementation = not approved.
P8-P12 entry = not approved.
P6 implementation = closed except for separately approved future tasks.
Next = review P7 minimal synthetic/local parser-reader smoke extension
implementation.
```

本技术方案不改变当前阶段，不允许跳过 Mortal/Akochan/Archer 等 baseline 的 F1/F2 复现与接口审计。

## Role Split

### Web ChatGPT Pro

网页端 ChatGPT Pro 负责高层方案与研究判断：

- 技术方案设计。
- 外部资料调研。
- 候选算法评审。
- 实验路线评审。
- 风险与合规判断。
- 关键技术决策。
- 论文结构和未来成果总结。

网页端输出不能直接替代项目事实。任何网页端结论都必须落到 Git + docs 后，才成为项目事实来源。

### Local Codex App

本地 Codex App 负责本地执行与落地：

- 读取项目规则。
- 执行 `docs/10_next/10_NEXT.md` 的第一项任务。
- 修改代码。
- 运行测试。
- 做本地可复现审计。
- 更新文档。
- 记录 evidence、risk、changelog 和 next。

Codex 不负责跳阶段，不负责无证据声称模型更强，不负责绕过平台规则。

## Source of Truth

唯一事实来源是：

```text
Git + docs
```

具体规则：

- Git worktree 中的文档和代码是当前项目状态。
- 网页端 ChatGPT Pro 的结论只有被 Codex 写入 docs 后才生效。
- 口头讨论、聊天记录、外部网页摘要不能单独作为项目事实。
- 每个技术决策必须写入对应 primary doc，并同步 handoff / changelog / next。
- 外部证据必须进入 `docs/09_governance/09_EVIDENCE_LOG.md`。
- 新风险必须进入 `docs/09_governance/09_RISK_REGISTER.md`。

## Main Technical Route

当前主路线是组合路线，不是单论文完整复现路线：

```text
Suphx-style SL + RL
+ Tenhou stable dan / pt EV reward
+ ACH-inspired policy improvement
+ risk model / search
+ baseline racing funnel
```

解释：

- Suphx-style SL + RL: 使用监督学习建立基础策略，再用自我对弈强化学习提升长期 Tenhou-like 指标。
- Tenhou stable dan / pt EV reward: 奖励与评测必须围绕稳定段位、Tenhou pt EV、平均顺位和四位率控制。
- ACH-inspired policy improvement: 借鉴 Actor-Critic Hedge / regret-minimization-inspired policy improvement 思路，但不得假设可直接迁移到四人 Tenhou。
- risk model / search: 把押引、危险牌、南场避四、Oorasu 排名判断作为后续增强重点。
- baseline racing funnel: Mortal / Archer / Akochan / Kanachan 等候选必须按 F0-F7 漏斗逐级验证。

## LuckyJ Position

LuckyJ 是目标基准，不是直接完整复现对象。

项目对 LuckyJ 的使用方式：

- 固定最低目标线：Tenhou stable dan > 10.68。
- 收集公开指标，定义验收条件。
- 不假设能得到 LuckyJ 实现细节、训练数据、权重或平台流程。
- 不为了复现 LuckyJ 而跳过本地评测、baseline、数据系统和合规边界。

## Execution Rule

Codex 每次只执行：

```text
docs/10_next/10_NEXT.md 的第一项未完成任务。
```

如果网页端或用户提出新方向，先判断它属于哪个阶段、哪个 primary doc、是否应成为新的 `10_NEXT`。不能把新想法直接变成训练、平台接入或大规模实验。

## Update Rule

每次真实任务完成后必须更新：

- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

如果任务产生技术决策，还必须更新：

- `docs/09_governance/09_DECISION_RECORD.md`

如果任务产生代码或实验结果，还必须记录：

- 使用的 commit / version / config。
- 数据来源与许可。
- 模型权重来源、版本、usage constraints 和 checksum。
- 评测规则、样本量、指标和失败案例。

## Current Non-Goals

当前不做：

- 不写训练代码。
- 不下载模型。
- 不接入真实 Tenhou。
- 不创建平台自动化、抓取、账号工具、规避或反检测逻辑。
- 不声称模型超过任何 baseline。
- 不把 LuckyJ 当作可直接复现对象。
- 不跳过 baseline racing funnel。
- 不使用来路不明的 model weights、`*.pth`、`*.pt`、`checkpoint` 或 `snapshot` 文件。
- 不把第三方源码 vendor/copy 进本仓库。
- 不超过 Akochan F2 fixed-sample wrapper 边界；不保存第三方源码、二进制、`params/` 或未知 artifact。

## Current Next Task

当前 `10_NEXT` 的下一步是：

```text
Review P7 minimal synthetic/local parser-reader smoke extension implementation.
```

`docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
accepts the exact minimal synthetic/local smoke implementation as
current-scope complete only.
`docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
selected docs-only current-scope closure criteria definition as the next P7
task. `docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines accepted current-scope inventory, closure criteria, deferred /
blocked / not accepted items, an exit readiness checklist, validation commands
and P8-P12 non-entry conditions. `docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
reviews those criteria and records `Review can close`.
`docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the current-scope handoff and evidence index.
`docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md`
runs the final current-scope closure review gate and records `P7 current scope
can close` for the exact current scope only.
`docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md`
completes the post-current-scope transition review and selects docs-only full
P7 closure roadmap / remaining-scope inventory as the next task. `03W` now
defines that roadmap / inventory and selects a docs-only review gate next.
`docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md`
reviews that roadmap / inventory and records `Review can close` with no
blocker. `03Y` now defines broader P7 scope / entry criteria / first task
before implementation, and `03Z` reviews it with no blocker. `03AA` defines
broader P7 data/source readiness and source-approval boundary before
implementation. `03AB` reviews it, records `Review can close`, and selects a
docs-only parser / reader / ingestion boundary definition next. `03AC` defines
that boundary and selects a docs-only review gate next. `03AD` reviews it,
records `Review can close`, and selects a docs-only actual feature extraction
and label generation boundary definition next. `03AE` defines that boundary
and selects a docs-only review gate next. `03AF` reviews that boundary, records
`Review can close`, and selects a docs-only supervised dataset construction /
split / leakage boundary definition next. `03AG` defines that boundary and
selects a docs-only review gate. `03AH` reviews it, records `Review can close`
and selects this docs-only training-data approval / training-run boundary
definition next. `03AI` defines that boundary and selects a docs-only review
gate next. `03AJ` reviews it, records `Review can close`, and selects a
docs-only model architecture / trainer planning boundary definition next.
`03AK` defines that boundary and selects a docs-only review gate next. `03AL`
reviews it, records `Review can close`, and selects a docs-only evaluation
dependency / model-strength evidence boundary definition next. `03AM` defines
that boundary and selects a docs-only review gate next. `03AN` reviews it,
records `Review can close`, and selects a broader P7 implementation readiness
checklist definition next. `03AO` defines that checklist and selects a
docs-only readiness checklist review gate. `03AP` reviews that checklist,
records `Review can close`, and selects a docs-only minimal implementation
proposal-boundary definition next. `03AQ` defines that proposal boundary and
selects a docs-only proposal-boundary review gate next. `03AR` reviews that
proposal boundary, records `Review can close`, and selects a docs-only
proposal drafting task next. `03AS` drafts that proposal for review only and
does not approve it. `03AT` reviews that proposal and records `Review can
close`. `03AU` approves only the next exact synthetic/local parser-reader
smoke implementation task and exact two implementation files. The next task
must not add fixtures, data files, source approval, source ingestion approval,
real data reads, broad parser implementation, dataset reader implementation,
ingestion implementation, actual feature extraction, actual label generation,
feature tensors, labels, examples, splits, supervised dataset construction,
leakage-test implementation, training-data construction, training-data
approval, training-run approval, training-run implementation, training, model
architecture implementation, trainer implementation, dataloader, optimizer,
loss, checkpoint, weights, evaluation implementation, model-strength evidence,
Tenhou evidence, stable-dan evidence, LuckyJ comparison, candidate promotion,
real Tenhou, real haifu, external logs, platform data, model-output
integration, CLI, broad file ingestion, self-play, league, P8-P12 work or
model-strength claims.

The exact P6 implementation approved by `02N` is complete and reviewed in
`docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md`
with no blocker and accepted as current-scope complete in
`docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`.
`docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
selected a docs-only closure-criteria definition as the next bounded P6
data-system task. `docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
now defines those criteria and selects a docs-only review gate as the next
task. `docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
reviews those criteria with no blocker and selects a docs-only final
current-scope closure review gate as the next task. It does not close full P6,
close current-scope P6 or approve real Tenhou, real haifu, external logs,
platform data, parser, dataset reader, data ingestion, feature extraction,
label generation, CLI, model-output integration, training, self-play, league
or P7-P12. `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
now records that current-scope P6 can close for the accepted synthetic/local
minimal replay schema and project-authored synthetic fixture scope only. Full
P6 remains open; P7-P12, real data, parser, dataset reader, ingestion, feature
extraction, label generation, model-output integration, CLI, training,
self-play and league remain unapproved.

`docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
records that the post-current-scope P6 transition review is complete. It
selects a docs-only full P6 closure roadmap and remaining scope inventory as
the next task; `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
now defines that roadmap / inventory and selects a docs-only review gate as the
next task. `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
reviews that roadmap / inventory with no blocker and selects a docs-only full
P6 closure criteria definition as the next task. This does not approve
implementation, real data, parser, dataset reader, ingestion, feature
extraction, label generation or P7-P12.
`docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
defines the full P6 closure criteria, exit readiness checklist, required
remaining full-P6 closure items, deferred / blocked / later-stage /
out-of-scope classifications and P7-P12 non-entry conditions. It does not
close full P6, approve P7-P12, approve implementation, real data, parser,
dataset reader, ingestion, feature extraction or label generation. The next
task is a docs-only review of those criteria.
`docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
reviews those criteria with no blocker and selects full P6 handoff / evidence
index finalization as the next docs-only task. It does not close full P6,
approve P7-P12, approve implementation, real data, parser, dataset reader,
ingestion, feature extraction or label generation.
`docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the full P6 handoff and evidence index after the criteria review. It
records the handoff summary, P6 evidence index, evidence grade consistency,
remaining required full-P6 items and next risk / source-rights review scope.
It does not close full P6, approve P7-P12, approve implementation, real data,
parser, dataset reader, ingestion, feature extraction or label generation.
`docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
reviews the risk register and source-rights inventory consistency before final
closure review. It finds no risk/source-rights blocker for the final full P6
closure review gate. It does not close full P6, approve P7-P12, approve source
ingestion, approve real data, approve parser, dataset reader, ingestion,
feature extraction or label generation.
`docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
records that full P6 can close for the documented P6 data-system scope only:
docs/governance/source-rights planning, accepted synthetic/local minimal
replay schema and project-authored synthetic fixture smoke implementation, and
deferred/blocked/later-stage inventory. It is not P7-P12 entry approval, not
P7 first-task approval and not new implementation approval.
`docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md` records that the
post-full-P6 transition review is complete and selected the docs-only P7 scope
definition task. `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
now defines P7 scope, entry criteria and the first task candidate before
implementation. This is not P7 implementation, not P7 first-task execution and
not P8-P12 entry approval.

 The stable-dan calculator now supports four-player general/ippan, upper/joukyu, expert/tokujou and phoenix/houou room formulas, records placement counts/rates and raises `StableDanUndefinedError` when `fourth_count == 0`. The bootstrap CI uses percentile empirical multinomial resampling, reports successful/undefined resamples and refuses to fabricate infinite stable dan. The threshold helper uses LuckyJ stable dan `10.68` by default and only returns `clear_pass` when bootstrap lower bound exceeds the threshold with acceptable undefined rate. The reporting schema separates `clears_threshold` from `can_enter_threshold_review` so low-sample reports cannot become project-level LuckyJ claims. The placement aggregation helper converts only explicit offline placement values and whitelisted aliases into first/second/third/fourth counts; it rejects zero-based, ambiguous, bool, float and unknown inputs. The smoke fixture verifies the CLI-free path from synthetic placements through report serialization without Tenhou data or model-strength claims. The API documentation explains this usage path and its guardrails. `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md` records stable-dan evaluation groundwork as complete for current P5 scope while keeping P5 overall open at that time. `src/mjlabai/eval/offline_result.py` and `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md` define the P5 offline metric registry and result envelope schema. `tests/eval/test_offline_envelope_smoke.py` verifies that a synthetic stable-dan report can be represented in the envelope. `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md` defines legal-action and invalid-action metric denominators, parse/missing/skipped handling, canonical matching principles, envelope mapping and the synthetic evaluator boundary before implementation. `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md` defines canonical action fields, current minimum `dahai` fixture scope, strict matching, future relaxed matching boundary and legal-action fixture shape. `tests/fixtures/eval/legal_action_metric_smoke.json` and `tests/eval/test_legal_action_fixture_schema_smoke.py` validate a synthetic-only legal-action fixture shape, now including `parse_failure` coverage. `src/mjlabai/eval/legal_action_metric.py` and `tests/eval/test_legal_action_metric.py` implement and test a narrow synthetic-only evaluator for that fixture, producing counts/rates and an offline envelope without CLI, broad ingestion, canonicalizer, rule engine, model code, training, self-play, league or Tenhou integration. `docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md` records that the current fixture covers `legal`, `invalid`, `missing_action`, `parse_failure` and `skipped_no_legal_actions`, and that the legal-action synthetic evaluator minimum outcome coverage is complete only for the current P5 synthetic-only `dahai` + strict scope. `docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md` defines the future tiny benchmark harness boundary for legal-action rate, latency and fixed-position diagnostics before implementation. `tests/fixtures/eval/tiny_benchmark_harness_smoke.json` and `tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py` validate the synthetic/local fixture shape for that boundary without implementing a harness, measuring latency, calculating fixed-position exact-match or reading real data. `docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md` records that the fixture schema is sufficient as the front-door input boundary for a future P5-only tiny benchmark harness implementation. `src/mjlabai/eval/tiny_benchmark_harness.py` now implements only that project-authored synthetic/local harness boundary and can emit an offline envelope without latency measurement, fixed-position exact-match, model-output integration, CLI, real data or strength claims. `docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md` records that this implementation review can close for the current fixture scope with no blocker. `docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md` records that the existing offline envelope coverage is sufficient for the synthetic tiny benchmark diagnostic scope with `wrapper_smoke_success`, `sample_size = 1`, `latency_ms = None`, all-false safety flags, synthetic/local warnings and evidence references. `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md` records that current P5 metric registry names, units, directions, statuses and evidence grades are consistent across stable-dan, legal-action and tiny benchmark diagnostics with no blocker. `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md` records that current P5 synthetic/local evidence labels, non-evidence warnings, promotion/ranking guardrails and stage-boundary wording are consistent with no blocker. `docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md` defines P5 closure criteria and an exit readiness checklist. `docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md` reviews those criteria and finds no blocker. `docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md` finalizes the P5 handoff and evidence index for final closure review and finds no blocker. `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md` records that all closure criteria pass, no blocker remains, and P5 can close for the current synthetic/local evaluation groundwork scope. `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` records that the project may start a docs-only task to define P6 data-system scope, entry criteria and first task before implementation. `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P6 data-system purpose, allowed/forbidden inputs, entry criteria, future implementation entry criteria, future exit criteria, provenance/rights/compliance requirements, evidence requirements, risks, P7-P12 non-entry boundaries and the first next task. `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 source provenance/rights inventory, source categories, approval vocabulary, pre-ingestion checklist, future evidence requirements and rights/provenance risks before replay schema implementation. `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` reviews that inventory and finds no blocker, while keeping broad P6 implementation and data ingestion closed. `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema documentation boundary after source inventory review, and `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` reviews it with no blocker. `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md` defines the P6 synthetic/local replay fixture boundary before schema implementation. `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md` reviews that boundary with no blocker. `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md` defines the replay schema and fixture implementation readiness checklist before code. `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md` reviews that checklist with no blocker. These remain metric infrastructure, specification, implementation, review, finalization, closure-review, transition-review and P6 planning evidence only, not strength evidence. `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md` defines the proposal boundary that any future replay schema or synthetic fixture implementation proposal must satisfy before code. `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md` reviews that proposal boundary with no blocker. `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md` prepares the minimal implementation proposal for review before code. `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md` reviews it with no blocker. `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` approved only the exact minimal implementation task. That task is now implemented in the approved files and reviewed in `02O` with no blocker before any further P6 work. It does not approve broad P6 implementation, real data, parser / reader / ingestion work, feature extraction, label generation, CLI, model-output integration, training, self-play, league, P7-P12 or model-strength claims.

`docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
prepares the current minimal proposal, and
`docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
reviews it with no blocker while keeping implementation closed.
`docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
approved only the exact minimal implementation task. That implementation is
now complete, reviewed and accepted as current-scope complete in the named
minimal replay schema module, project-authored synthetic/local fixture and two
minimal tests; `02Q` selects current-scope closure criteria as the next docs-only
P6 task, `02R` defines those criteria, `02S` reviews them with no blocker and
`02T` closes the accepted current-scope only. All parser, dataset reader, ingestion, feature
extraction, label generation, real-data, CLI, model-output, training,
self-play, league and P7-P12 work remains unapproved.

Mortal runnable baseline 已暂停，因为当前没有合法、可校验、可使用的 trained model artifact。Mortal 仍保留为源码、mjai 接口、方法论和工程参考。除非未来先补齐 artifact 来源、version/tag、usage constraints 和 checksum 并重新打开 F1，否则不进入 Mortal F2 adapter。

Akochan F1 审计已完成，当前结论为 Conditional Pass：仓库公开且 JSON/mjai/log/legal-action 入口有价值，未发现外部神经网络权重需求；修正后的 GitHub Actions Ubuntu workflow run `26617347785` 成功生成 `libai.so` 和 `system.exe`，并跑通最小 `legal_action` 与 `mjai_log haifu_log_sample.json 0 2` 样例。

Conditional 的原因：Akochan license 是 custom Japanese usage agreement，修改、再分发、商业或公开发布仍需要复审/许可；本机 macOS build 仍未通过，当前可复现证据来自 Ubuntu GitHub Actions runner。

F2 task definition 已写入 `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`。最小 wrapper skeleton 已实现，并通过 fake executable smoke tests；该 fake executable 只是测试替身，不是真实 Akochan，也不是强度证据。

真实 external `system.exe` 验证路径已新增：`.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` 会在临时 Ubuntu runner 中构建 Akochan，并用 `tests/adapters/test_akochan_wrapper_real_exe.py` 调用真实 runner-temp `system.exe`。

首个 workflow run `26621536548` 已复审：构建、fake wrapper tests 和真实 `legal_action` wrapper test 通过；真实 `mjai_log` wrapper test 失败，因为 Akochan 运行时需要从 process working directory 读取 `setup_mjai.json`。

本地 wrapper cwd 边界已修复：`AkochanWrapper` 支持显式 `working_dir`、`AKOCHAN_WORKING_DIR` 和默认 `Path(system_exe).resolve().parent`；`subprocess.run` 使用 `cwd=self.working_dir`；audit log 记录 `working_dir`。workflow run `26623247276` 证明 `setup_mjai.json` blocker 已消失，真实 `legal_action` 继续通过，但真实 `mjai_log` stdout 触发 `JSONDecodeError: Extra data`。workflow run `26628128871` 进一步证明 strict JSON stream parser 能解析前段 JSON records，但真实 stdout 还包含白名单状态行 `calculating review` 和后续 JSON review output。本地 parser 已支持 single JSON、JSON Lines、concatenated JSON values、pretty-printed multi-record JSON stream，以及只跳过 exactly `calculating review` 的 allowlisted mixed stdout；unknown non-JSON line 和 partial parse 仍必须失败。workflow run `26629344590` 已成功验证该路径：Ubuntu runner 成功构建 `ai_src/libai.so`、root `libai.so` 和 `system.exe`，fake wrapper tests 14 tests passed，real `legal_action` 和 real `mjai_log` 均通过。该证据只说明 fixed-sample wrapper/integration 可行，不是 Akochan 或 mjlabai 强度证据。下一步只允许 implement P5 synthetic legal-action metric evaluator for project-authored fixture only；仍然不训练、不调参、不自我对弈、不跑 league、不接入 Tenhou、不 vendor 或上传第三方源码、二进制、`params/` 或未知 artifact。
