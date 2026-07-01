# 07A_MILESTONES

## North-star route

All project stages serve one target:

```text
Train a Japanese riichi mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum benchmark: above Tenhou 10 dan and stable dan > 10.68.
```

## P0-P12 roadmap

| Stage | Name | Goal | Gate | Status |
|---|---|---|---|---|
| P0 | Project docs and Codex rules | Make Codex load the project target, workflow and forbidden actions before execution | Rule-load test passes without file changes | Closing |
| P1 | North-star target and metrics | Lock Tenhou stable dan > LuckyJ 10.68 as the target and define Tenhou-oriented metrics | Target and metrics are documented in `01_goal_benchmark` | Mostly complete |
| P2 | Algorithm candidate table and racing funnel | Maintain Suphx / LuckyJ / Mortal / Archer / Akochan / Kanachan roles and funnel stages | Candidate roles and F0-F7 gates are documented | Mostly complete |
| P3 | Baseline reproducibility audit | Verify whether open baselines can install, run, infer and expose useful I/O locally | At least one baseline can perform stable local inference | Active |
| P4 | Unified mahjong environment and interface | Define shared state, legal actions, logs, replays and adapter contracts | Different candidates can run through the same interface | Future |
| P5 | Unified evaluation system | Compare all models with Tenhou-oriented metrics under one harness | Stable comparison of baselines and project models | Closed for current synthetic/local evaluation groundwork scope |
| P6 | Data system | Build replay, feature, label and quality pipelines for training and evaluation | Supervised training and offline evaluation datasets can be generated | Closed for documented P6 data-system scope only; parser / reader / ingestion / feature / label and real data remain unapproved |
| P7 | Supervised policy model | Train a base strategy model from high-quality human play and key decisions | Model beats simple baselines in key offline scenarios and completes games | Current scope closed only for docs-only readiness chain plus exact minimal synthetic/local feature-label smoke implementation in `03V`; broader scope / entry criteria reviewed in `03Z`; broader data/source readiness and source-approval boundary defined in `03AA` and reviewed in `03AB`; broader parser / reader / ingestion boundary defined in `03AC` and reviewed in `03AD`; broader actual feature extraction and label generation boundary defined in `03AE` and reviewed in `03AF`; broader supervised dataset construction / split / leakage boundary defined in `03AG` and reviewed in `03AH`; broader training-data approval / training-run boundary defined in `03AI` and reviewed in `03AJ`; broader model architecture / trainer planning boundary defined in `03AK` and reviewed in `03AL`; broader evaluation dependency / model-strength evidence boundary defined in `03AM` and reviewed in `03AN`; broader implementation readiness checklist defined in `03AO` and reviewed in `03AP`; broader minimal implementation proposal boundary defined in `03AQ` and reviewed in `03AR`; broader minimal implementation proposal drafted in `03AS` for review only and reviewed in `03AT`; exact broader P7 minimal synthetic/local parser-reader smoke implementation approved in `03AU` for two exact files only, implemented in those exact files, reviewed in `03AV` with `Review can close`, and accepted as current-scope complete on 2026-07-01 for that exact synthetic/local scope only; full P7 scope expansion plan defined in `03AW` and reviewed in `03AX`; P7 minimal implementation proposal drafted in `03AY` for review only and reviewed in `03AZ` with `Review can close`; current next is docs-only approval-decision preparation; full P7, broad implementation, evaluation implementation, metric implementation, evaluation runner, benchmark harness, strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ comparison, candidate promotion, training, training-data construction, training-data approval, training-run approval, training-run implementation, source approval, source ingestion, broad parser / reader / ingestion implementation, actual feature extraction, actual label generation, feature tensors, labels, examples, splits, supervised dataset construction, leakage-test implementation, model architecture / trainer implementation, dataloader / optimizer / loss implementation, checkpoints, weights, real data, model-output integration and P8-P12 remain unapproved |
| P8 | Self-play reinforcement learning | Optimize toward Tenhou pt EV, placement and stable-dan objectives | RL checkpoint beats supervised checkpoint in the unified league | Future |
| P9 | Search and risk model | Improve push/fold, deal-in risk, south-round rank control and oorasu decisions | Search-enhanced model beats non-search model in scenarios and league play | Future |
| P10 | Model league and mainline selection | Run long comparisons among baselines, SL, RL, search and historical best versions | A candidate reliably beats the current mainline with uncertainty reported | Future |
| P11 | Large-scale training and stability validation | Expand compute only after the route is justified by previous gates | Internal evaluation approaches or exceeds the LuckyJ 10.68 target line | Future |
| P12 | Tenhou target validation | Validate whether the system can exceed LuckyJ 10.68 under compliant conditions | Long-term stable dan, pt EV, rank metrics, latency and logs are verified | Final |

## Current position

```text
P0 / P1 / P2 are basically established.
P3 baseline reproducibility produced current Mortal/Akochan funnel evidence.
P5 evaluation groundwork is closed for the current synthetic/local scope.
Full P6 is closed only for the documented P6 data-system scope recorded in
`02AA`: docs/governance/source-rights planning, accepted synthetic/local
minimal replay schema and project-authored synthetic fixture smoke
implementation, and deferred/blocked/later-stage inventory.
`12D` completes the post-full-P6 transition review and selected the docs-only
P7 scope definition task. `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
defines P7 scope, entry criteria and the first task candidate before
implementation. `docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
reviews that definition and records `Review can close`.
`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
defines the P7 supervised-learning data/source readiness inventory, and
`docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
reviews that inventory and records `Review can close`.
`docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines the P7 feature and label readiness boundary.
`docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
reviews that boundary and records `Review can close`.
`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
defines the P7 supervised-learning risk and evidence taxonomy, and
`docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`
reviews that taxonomy and records `Review can close`.
`docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`
defines the docs-only proposal for a minimal P7 synthetic/local supervised
fixture and feature-label smoke path before implementation.
`docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md`
reviews that proposal and records `Review can close`.
`docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
records decision `Approved for next minimal implementation task.` The current
exact minimal synthetic/local supervised fixture and feature-label smoke
implementation is complete in the files named in `03O`, and
`docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`
reviews it with `Review can close`.
`docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
accepts it as current-scope complete only for the exact minimal synthetic/local
smoke scope. `docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines the next P7 current-scope supervised-learning task and selects
docs-only current-scope closure criteria definition as the next step.
`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines those criteria, exit readiness, remaining docs/review/closure items,
deferred / blocked / not accepted items and P8-P12 non-entry conditions. It
does not close P7 current scope; the next step is a docs-only criteria review
gate.
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
reviews those criteria and records `Review can close` with no blocker. It does
not close P7 current scope.
`docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the P7 current-scope handoff and evidence index with no separate
risk/evidence consistency blocker. It does not close P7 current scope; the
next step is a docs-only final current-scope closure review gate.
`docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md`
runs that final review gate and records that P7 current scope can close only
for the exact current scope: docs-only supervised-learning readiness chain plus
accepted minimal synthetic/local supervised feature-label smoke implementation.
Full P7, broader P7 implementation, training, source ingestion, parser /
reader / ingestion, actual feature extraction, actual label generation, real
data, model-output integration and P8-P12 remain unapproved. The next step is
a docs-only post-current-scope P7 transition review.
`docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md`
completes that transition review, confirms full P7 remains open and selects
docs-only full P7 closure roadmap / remaining-scope inventory definition as
the next step.
`docs/03_supervised_policy/03W_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_AFTER_CURRENT_SCOPE_CLOSURE.md`
defines that roadmap / inventory, classifies remaining full-P7 items as
required, deferred, blocked, later-stage or out of scope, and selects a
docs-only review gate next.
`docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md`
reviews that roadmap / inventory and records `Review can close` with no
blocker. The next step is a docs-only definition of broader P7 scope, entry
criteria and first task before implementation; it does not approve broader P7
implementation, training, source ingestion, parser / reader / ingestion,
actual feature extraction, actual label generation, real data, model-output
integration or P8-P12.
`docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
defines broader P7 scope, entry criteria and first task before implementation.
It records broader P7 purpose, implementation entry criteria, required upstream
artifacts, blocked / deferred / later-stage / out-of-scope items and the next
docs-only review gate. Full P7 remains open, and broader P7 implementation,
training, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, model architecture / trainer, real data,
model-output integration and P8-P12 remain unapproved.
`docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews `03Y` and records `Review can close` with no blocker. It confirms that
broader P7 scope, entry criteria and the first-task boundary are conservative
enough before implementation. The broader data/source readiness and
source-approval boundary has now been defined and reviewed. The broader
parser / reader / ingestion boundary has now been defined. The next step is
docs-only: `Review broader P7 parser, reader and ingestion boundary before
implementation`. It does not approve full P7 closure, broad implementation,
training, source approval, source ingestion, parser / reader / ingestion
implementation, actual feature extraction, actual label generation, real data,
model-output integration or P8-P12.
`docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines that broader P7 data/source readiness and source-approval boundary.
It records that no source is approved for P7 training, source ingestion,
actual feature extraction or actual label generation. It also separates
source readiness, source-specific approval, source ingestion approval,
feature extraction approval, label generation approval, training-data approval
and training-run approval.
`docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews that boundary, records `Review can close` and selects
`Define broader P7 parser, reader and ingestion boundary before implementation`
as the next docs-only task. It does not approve any source, source ingestion,
parser / reader / ingestion implementation, actual feature extraction, actual
label generation, training, real data, model-output integration or P8-P12.
`docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines broader P7 parser / reader / ingestion concepts, dependency order,
candidate classes, future approval-record fields, allowed and forbidden scope,
stop conditions, risk controls and evidence requirements. It selects
`Review broader P7 parser, reader and ingestion boundary before implementation`
as the next docs-only task. It does not approve parser, reader, ingestion,
source ingestion, broad file ingestion, CLI, source approval, actual feature
extraction, actual label generation, training, real data or P8-P12.
`docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews `03AC` and records `Review can close` with no blocker. It confirms
that the parser / reader / ingestion boundary is conservative enough for the
current gate and selects `Define broader P7 actual feature extraction and label
generation boundary before implementation` as the next docs-only task. It does
not approve parser, reader, ingestion, source ingestion, broad file ingestion,
CLI, source approval, actual feature extraction, actual label generation,
training, real data or P8-P12.
`docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines broader P7 actual feature extraction and label generation vocabulary,
current status, dependency order, candidate feature and label families,
future approval fields, allowed / forbidden scope, leakage controls, stop
conditions, risk controls and evidence requirements. It selects `Review
broader P7 actual feature extraction and label generation boundary before
implementation` as the next docs-only task. It does not approve actual feature
extraction, actual label generation, feature tensors, labels, targets,
examples, splits, supervised dataset construction, training, real data or
P8-P12.
`docs/03_supervised_policy/03AF_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews `03AE`, records `Review can close` with no blocker and selects
`Define broader P7 supervised dataset construction, split and leakage boundary
before implementation` as the next docs-only task. It does not approve actual
feature extraction, actual label generation, feature tensors, labels, targets,
examples, splits, supervised dataset construction, training, real data or
P8-P12.
`docs/03_supervised_policy/03AG_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines broader P7 supervised dataset construction, split and leakage boundary
before implementation.
`docs/03_supervised_policy/03AH_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews `03AG`, records `Review can close` with no blocker and selects
`Define broader P7 training-data approval and training-run boundary before
implementation` as the next docs-only task. It does not approve supervised
dataset construction, split creation, leakage-test implementation,
training-data construction, training-run approval, training, real data or
P8-P12.
`docs/03_supervised_policy/03AI_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines the broader P7 training-data approval and training-run boundary before
implementation and selects a docs-only review gate next. It does not approve
training data, training-data construction, a training run, training-run
implementation, training, model architecture / trainer, checkpoints, weights,
real data or P8-P12.
`docs/03_supervised_policy/03AJ_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews `03AI`, records `Review can close` with no blocker and selects
`Define broader P7 model architecture and trainer planning boundary before
implementation` as the next docs-only task. It does not approve model
architecture implementation, trainer implementation, dataloader / optimizer /
loss implementation, checkpoint / weights creation, training, real data or
P8-P12.
`docs/03_supervised_policy/03AK_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines the broader P7 model architecture and trainer planning boundary before
implementation and selects `Review broader P7 model architecture and trainer
planning boundary before implementation` as the next docs-only task. It does
not approve model architecture implementation, trainer implementation,
dataloader / optimizer / loss implementation, checkpoint / weights creation,
training-data approval, training-run approval, training, real data or P8-P12.
`docs/03_supervised_policy/03AL_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews that boundary, records `Review can close` with no blocker and selects
`Define broader P7 evaluation dependency and model-strength evidence boundary
before implementation` as the next docs-only task. It does not approve
evaluation implementation, model-strength evidence, Tenhou evidence,
stable-dan evidence, LuckyJ `10.68` comparison, candidate promotion, model
architecture implementation, trainer implementation, checkpoint / weights
creation, training, real data or P8-P12.
`docs/03_supervised_policy/03AM_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines the broader P7 evaluation dependency and model-strength evidence
boundary before implementation. It records current no-strength-evidence
status, evaluation and evidence vocabulary, dependency order, evaluation
dependency boundary, model-strength evidence boundary, Tenhou / stable-dan /
LuckyJ evidence prerequisites, future evidence-record fields, candidate
evidence classes, allowed and forbidden future scope, stop conditions, risk
controls, evidence requirements, planning decision and evidence grade. The
next step is a docs-only review gate. It does not approve evaluation
implementation, metric implementation, evaluation runner, benchmark harness,
model-output integration, model-strength evidence, Tenhou evidence,
stable-dan evidence, LuckyJ `10.68` comparison, candidate promotion,
training, real data or P8-P12.
`docs/03_supervised_policy/03AN_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews that boundary, records `Review can close` with no blocker and selects
`Define broader P7 implementation readiness checklist after boundary-chain
review` as the next docs-only task. It does not approve broader P7
implementation, evaluation implementation, metric implementation, evaluation
runner, benchmark harness, model-output integration, model-strength evidence,
Tenhou evidence, stable-dan evidence, LuckyJ `10.68` comparison, candidate
promotion, training, real data or P8-P12.
`docs/03_supervised_policy/03AO_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_AFTER_BOUNDARY_CHAIN_REVIEW.md`
defines that readiness checklist after the reviewed boundary chain, records
the candidate implementation class readiness matrix and required future
proposal / approval fields, and selects `Review broader P7 implementation
readiness checklist after boundary-chain review` as the next docs-only task.
It does not approve broader P7 implementation, production code, tests,
fixtures, data files, source approval, source ingestion, parser / reader /
ingestion, actual feature extraction, actual label generation, supervised
dataset construction, training, model / trainer implementation, evaluation
implementation, model-output integration, strength evidence, real data,
self-play, league or P8-P12.
`docs/03_supervised_policy/03AP_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW_AFTER_BOUNDARY_CHAIN_REVIEW.md`
reviews that readiness checklist, records `Review can close` with no blocker
and selects `Define broader P7 minimal implementation proposal boundary after
readiness checklist review` as the next docs-only task. It does not approve a
proposal, broader P7 implementation, source approval, source ingestion, parser
/ reader / ingestion, actual feature extraction, actual label generation,
supervised dataset construction, training, model / trainer implementation,
evaluation implementation, model-output integration, strength evidence, real
data, self-play, league or P8-P12.
`docs/03_supervised_policy/03AQ_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_AFTER_READINESS_CHECKLIST_REVIEW.md`
defines that minimal implementation proposal boundary after the readiness
checklist review, records lifecycle vocabulary, candidate proposal classes,
required sections, exact-scope requirements, forbidden scope, approval
separation, prerequisites, stop conditions, risk controls and evidence
requirements, and selects `Review broader P7 minimal implementation proposal
boundary after readiness checklist review` as the next docs-only task. It
does not approve a proposal, broader P7 implementation, source approval,
source ingestion, parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, training, model /
trainer implementation, evaluation implementation, model-output integration,
strength evidence, real data, self-play, league or P8-P12.
`docs/03_supervised_policy/03AR_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW_AFTER_READINESS_CHECKLIST_REVIEW.md`
reviews that proposal-boundary definition, records `Review can close` with no
blocker and selects `Draft broader P7 minimal implementation proposal for
review after proposal-boundary review` as the next docs-only task. It does not
approve a proposal, broader P7 implementation, source approval, source
ingestion, parser / reader / ingestion, actual feature extraction, actual
label generation, supervised dataset construction, training, model / trainer
implementation, evaluation implementation, model-output integration, strength
evidence, real data, self-play, league or P8-P12.
`docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`
drafts that proposal for review only. It selects a project-authored
synthetic/local parser-reader smoke proposal, names candidate future files as
not approved for editing, records allowed / forbidden inputs and outputs,
dependency status, validation command candidates, rollback, stop conditions,
risk controls, evidence requirements and approval separation, and selects
`Review broader P7 minimal implementation proposal before approval decision`
as the next docs-only task. It does not approve the proposal, broader P7
implementation, code, tests, fixtures, data files, source approval, ingestion,
parser / reader / ingestion, actual feature extraction, actual label
generation, dataset construction, training, model / trainer implementation,
evaluation implementation, model-output integration, strength evidence, real
data, self-play, league or P8-P12.
`docs/03_supervised_policy/03AT_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`
reviews that proposal, records `Review can close` with no blocker, and
selects `Prepare approval decision for broader P7 minimal synthetic/local
parser-reader smoke implementation` as the next docs-only task. It does not
approve the proposal, broader P7 implementation, code, tests, fixtures, data
files, source approval, ingestion, parser / reader / ingestion, actual
feature extraction, actual label generation, dataset construction, training,
model / trainer implementation, evaluation implementation, model-output
integration, strength evidence, real data, self-play, league or P8-P12.
`docs/03_supervised_policy/03AU_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
records `Approved for next exact minimal implementation task` for `Implement
broader P7 minimal synthetic/local parser-reader smoke only`. The approval is
limited to `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`,
`tests/supervised/test_synthetic_parser_reader_smoke.py` and direct
docs/governance synchronization; no new fixture/data file is approved by
default, and broad P7 implementation, source approval, source ingestion,
broad parser / reader / ingestion, actual feature extraction, actual label
generation, dataset construction, training, model / trainer implementation,
evaluation implementation, model-output integration, strength evidence, real
data, self-play, league and P8-P12 remain unapproved.
No source is approved for P7 training, source ingestion, parser / reader /
ingestion, actual feature extraction or actual label generation. Broad P7
implementation, training and P8-P12 entry remain unapproved.
```

The exact minimal P6 replay schema and project-authored synthetic fixture
implementation approved in
`docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
is complete in the named files only and reviewed in
`docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md`
with no blocker. It is accepted as current-scope complete in
`docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`.
`docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
selects current-scope closure criteria as the next docs-only P6 step, and
`docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
defines those criteria without closing full P6 or current-scope P6.
`docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
reviews those criteria with no blocker. The next step is a docs-only final
current-scope closure review gate. `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
records that current-scope P6 can close for the accepted synthetic/local
minimal replay schema and project-authored synthetic fixture scope only. Full
P6 remains open, and P7-P12 remains unapproved.
`docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
completes the post-current-scope transition review and selects the next
docs-only task: define a full P6 closure roadmap and remaining scope inventory.
`docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
defines that roadmap / inventory and selects a docs-only review gate.
`docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
reviews the roadmap / inventory with no blocker and selects the next docs-only
task: define full P6 closure criteria after roadmap and remaining scope review.
`docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
defines those criteria, exit readiness, required remaining closure items,
deferred / blocked / later-stage / out-of-scope classifications and P7-P12
non-entry conditions.
`docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
reviews those criteria with no blocker and selects full P6 handoff / evidence
index finalization as the next docs-only task.
`docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes that handoff / evidence index and selects a docs-only risk register
and source-rights inventory consistency review before final closure review.
`docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
reviews that risk / source-rights consistency with no blocker for the final
full P6 closure review gate. `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
records that full P6 can close for the documented P6 data-system scope only.
`docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md` completes the
post-full-P6 transition review and selected the docs-only P7 scope definition
task. `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
now defines that scope and recommends a docs-only review gate next. This must
not expand into parser, dataset reader, data ingestion, feature extraction,
label generation, training, self-play, league, real Tenhou, external-log
ingestion, P7 implementation, P8-P12 work or model-strength claims.

## Guardrail

Do not train, tune, build Tenhou integration, scrape data or start self-play before the relevant stage and `docs/10_next/10_NEXT.md` explicitly allow it.
