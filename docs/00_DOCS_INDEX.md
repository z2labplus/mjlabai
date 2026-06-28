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
docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md
docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md
docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md
```

`docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`
records the post-P5 transition review after final P5 closure. It confirms that
P5 is closed for the current synthetic/local evaluation groundwork scope and
allows only a docs-only next task to define P6 data-system scope, entry criteria
and first task before implementation. It is not P6 implementation approval,
P7-P12 entry approval, data-ingestion evidence or model-strength evidence.

`docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
records the post-current-scope P6 transition review after final current-scope
P6 closure. It confirms that accepted current-scope P6 is closed only for the
synthetic/local minimal replay schema and project-authored fixture scope, that
full P6 remains open and that P7-P12 entry remains unapproved. It selects the
next docs-only task: define a full P6 closure roadmap and remaining scope
inventory after current-scope closure. It is transition-review evidence only,
not full P6 closure, P7-P12 entry approval, implementation approval, ingestion
evidence or model-strength evidence.

`docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md`
records the post-full-P6 transition review after final full P6 closure. It
confirms that full P6 is closed only for the documented P6 data-system scope
and selects the next docs-only task: define P7 scope, entry criteria and first
task before implementation. It is transition-review evidence only, not P7-P12
entry approval, P7 implementation approval, training approval, real-data
approval, parser / reader / ingestion approval or model-strength evidence.

`docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md`
records the post-current-scope P7 transition review after final current-scope
P7 closure. It confirms that P7 current scope is closed only for the exact
docs-only readiness chain plus accepted minimal synthetic/local feature-label
smoke implementation, that full P7 remains open and that broader P7
implementation and P8-P12 remain unapproved. It selects the next docs-only
task: define a full P7 closure roadmap and remaining scope inventory after
current-scope closure. It is transition-review evidence only, not full P7
closure, broader implementation approval, training approval, parser / reader /
ingestion approval, real-data approval, P8-P12 entry approval or
model-strength evidence.

## Supervised-policy files

```text
docs/03_supervised_policy/03_SUPERVISED_POLICY.md
docs/03_supervised_policy/03A_MODEL_ARCHITECTURE.md
docs/03_supervised_policy/03B_TRAINING_OBJECTIVES.md
docs/03_supervised_policy/03C_KEY_DECISION_HEADS.md
docs/03_supervised_policy/03D_OFFLINE_METRICS.md
docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md
docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md
docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md
docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md
docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md
docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md
docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md
docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md
docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md
docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md
docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md
docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md
docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md
docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md
docs/03_supervised_policy/03W_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_AFTER_CURRENT_SCOPE_CLOSURE.md
docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md
docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md
docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md
```

`docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
defines P7 supervised-learning scope, entry criteria, future exit criteria,
required inputs, risk review requirements, evidence requirements and the first
task candidate before implementation. It is docs-only P7 planning evidence:
P7 implementation, P7 first-task execution, training, parser, dataset reader,
ingestion, feature extraction, label generation, real Tenhou, real haifu,
external logs, platform data, model-output integration, CLI, self-play, league
and P8-P12 remain unapproved.

`docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
reviews the P7 scope, entry criteria and first-task definition before
implementation. It records that the review can close with no blocker and
selects `Define P7 supervised-learning data/source readiness inventory before
implementation` as the next docs-only P7 task. It is P7 review evidence only:
P7 implementation, P7 first-task execution, training, parser, dataset reader,
ingestion, feature extraction, label generation, real Tenhou, real haifu,
external logs, platform data, model-output integration, CLI, self-play, league
and P8-P12 remain unapproved.

`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
defines P7 supervised-learning data/source readiness inventory before
implementation. It records candidate source categories, readiness status
vocabulary, training-data readiness requirements, P6 source-rights consistency,
parser / reader / ingestion dependency status, feature / label readiness
status, risks and evidence requirements. It records that no source is currently
approved for P7 training, source ingestion, feature extraction or label
generation. It is inventory-definition evidence only, not source approval,
training-data approval, P7 implementation or P8-P12 entry approval.

`docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
reviews the P7 supervised-learning data/source readiness inventory before
implementation. It records that `03G` scope, source categories, no-approved-
training-source status, readiness vocabulary, training-data requirements, P6
source-rights consistency, parser / reader / ingestion status, feature / label
readiness status, risks, evidence requirements and governance synchronization
are sufficient for the current review gate. Review decision: `Review can
close.` It is review evidence only, not source approval, training-data
approval, P7 implementation, feature/label approval or P8-P12 entry approval.

`docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines P7 supervised-learning feature and label readiness boundaries before
implementation. It records candidate feature and label families, forbidden
feature / label scope, dependency order, leakage risks, evidence requirements
and readiness vocabulary. It is boundary-definition evidence only: it does not
approve feature extraction, label generation, parser, dataset reader,
ingestion, training, real data, model-output integration, P7 implementation or
P8-P12 entry.

`docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
reviews the P7 feature and label readiness boundary before implementation. It
records `Review can close` and confirms that `03I` scope, feature boundary,
label boundary, candidate families, forbidden scope, dependency map, risks,
evidence requirements, readiness vocabulary and governance synchronization are
sufficient for the current review gate. It is review evidence only, not P7
implementation, feature extraction, label generation, source approval,
training-data approval or P8-P12 entry approval.

`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
defines the P7 supervised-learning risk and evidence taxonomy before
implementation. It records P7 risk categories, evidence grades, current P7
evidence classification, future evidence requirements, evidence-to-claim
mapping, forbidden evidence interpretations, dependency order, governance
update requirements and P8-P12 non-entry boundaries. It is taxonomy-definition
evidence only, not P7 implementation, source approval, feature extraction,
label generation, training, model-strength evidence or P8-P12 entry approval.

`docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`
reviews the P7 supervised-learning risk and evidence taxonomy before
implementation. It records `Review can close` and confirms that `03K` scope,
risk taxonomy, evidence taxonomy, current evidence classification, future
evidence requirements, evidence-to-claim mapping, forbidden interpretations,
dependency map, governance update requirements, P8-P12 non-entry boundary,
governance synchronization and validation are sufficient for the current review
gate. It is review evidence only, not P7 implementation, source approval,
feature extraction, label generation, training, model-strength evidence or
P8-P12 entry approval.

`docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`
defines a docs-only proposal for a future minimal P7 synthetic/local
supervised fixture and feature-label smoke path before implementation. It
names only candidate future files, candidate fixture boundaries, candidate
feature / label smoke boundaries, future validation commands, approval
conditions, stop conditions and risks. It is proposal evidence only: no
fixture, tests, production code, data file, source approval, parser, dataset
reader, ingestion, feature extraction, label generation, training,
model-output integration, real data, self-play, league or P8-P12 entry is
approved.

`docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md`
reviews the `03M` proposal and records `Review can close` with no blocker. It
confirms the scope, candidate classes, exact candidate future files,
synthetic/local fixture boundary, feature / label smoke boundary, validation
distinction, future approval conditions, stop conditions, risks, evidence
grade and governance synchronization are sufficiently conservative. It is
proposal-review evidence only, not P7 implementation, fixture creation, tests,
production code, data-file creation, source approval, parser, dataset reader,
ingestion, feature extraction, label generation, training, model-output
integration, model-strength evidence or P8-P12 entry approval.

`docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
records the docs-only approval decision for the next minimal P7
synthetic/local supervised fixture and feature-label smoke implementation
task. Decision: `Approved for next minimal implementation task.` This approval
is narrow: it only permits the next `10_NEXT` item to be the exact minimal
synthetic/local smoke implementation task. It does not execute implementation,
create files, generate an implementation prompt, approve a training source,
approve parser / reader / ingestion, approve actual feature extraction,
approve actual label generation, approve real data or approve P8-P12.

Minimal P7 synthetic/local supervised feature-label smoke implementation
artifacts:

```text
src/mjlabai/supervised/feature_label_schema.py
tests/fixtures/supervised/synthetic_supervised_smoke.json
tests/supervised/test_feature_label_schema.py
tests/supervised/test_synthetic_supervised_fixture_schema.py
```

These artifacts implement only the exact `03O` synthetic/local smoke scope:
in-memory JSON-safe fixture validation, candidate feature/label family
validation, public-information-only placeholders, hidden/future information
rejection, unsafe provenance rejection and fixture smoke tests. They are not
source approval, training-data approval, parser / reader / ingestion, actual
feature extraction, actual label generation, supervised dataset construction,
training, model-output integration, CLI, real-data use, model-strength
evidence, LuckyJ `10.68` comparison or P8-P12 entry approval.

`docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`
reviews the exact minimal implementation and records `Review can close`. It
confirms that the `03O` file list was respected, the helper remains
standard-library-only and in-memory, the fixture remains project-authored
synthetic/local, tests cover the approved scope, guardrails are sufficient for
the current smoke boundary, validation passes and governance is synchronized.
It is P7 minimal synthetic/local feature-label smoke implementation review
evidence only, not broad P7 implementation, source approval, training-data
approval, parser / reader / ingestion, actual feature extraction, actual label
generation, supervised dataset construction, training, model architecture,
trainer, model-output integration, CLI, real-data use, model-strength
evidence, LuckyJ `10.68` comparison or P8-P12 entry approval.

`docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
records the current-scope acceptance decision for the exact minimal P7
synthetic/local supervised feature-label smoke implementation. Decision:
`Accepted as current-scope complete.` The accepted scope is limited to the
exact helper, fixture, smoke tests and direct docs/governance synchronization.
It accepts only JSON-safe synthetic/local smoke mapping validation, candidate
feature family validation, candidate label family validation,
public-information-only checks, hidden/future information rejection, unsafe
provenance / claim rejection and non-evidence guardrails. It does not accept
or approve broad P7 implementation, P7 training, source ingestion, parser /
reader / ingestion, actual feature extraction, actual label generation,
supervised dataset construction, model architecture, trainer, real data,
model-output integration, CLI, self-play, league, P8-P12 entry,
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate promotion.

`docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines the next P7 current-scope supervised-learning task after `03Q`
acceptance. It evaluates candidate docs-only next tasks and selects
`Define P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance`
so P7 does not continue indefinitely through readiness / schema churn. It is
next-task definition evidence only; it does not approve broad P7
implementation, training, source ingestion, parser / reader / ingestion,
actual feature extraction, actual label generation, real data, model-output
integration, CLI, self-play, league, P8-P12, model-strength evidence, LuckyJ
`10.68` comparison or candidate promotion.

`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
defines P7 current-scope closure criteria after minimal synthetic feature-label
smoke acceptance. It records accepted current-scope inventory, C1-C26 closure
criteria, exit readiness, remaining docs/review/closure items, deferred /
blocked / not accepted items, validation commands and P8-P12 non-entry
conditions. It is closure-criteria definition evidence only: it does not close
P7 current scope, approve broader P7 implementation, approve training, approve
source ingestion, approve parser / reader / ingestion, approve actual feature
extraction, approve actual label generation, approve real data, approve
model-output integration, approve self-play, approve league or approve
P8-P12.

`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`
reviews the `03S` P7 current-scope closure criteria. Review decision:
`Review can close.` It confirms that `03S` scope, accepted inventory, C1-C26
criteria, exit readiness, remaining docs/review/closure items, deferred /
blocked / not accepted classification, validation commands, governance
synchronization and P8-P12 non-entry conditions are sufficient and
conservative. It is closure-criteria review evidence only: it does not close
P7 current scope, approve broader P7 implementation, approve training, approve
source ingestion, approve parser / reader / ingestion, approve actual feature
extraction, approve actual label generation, approve real data, approve
model-output integration, approve self-play, approve league or approve
P8-P12.

`docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the P7 current-scope handoff and evidence index after the `03T`
closure-criteria review. It records a finalization-ready handoff summary, an
evidence index covering `03E`-`03U`, accepted minimal synthetic/local
feature-label smoke implementation artifacts, P6/P5 context and governance
docs, confirms evidence grade consistency and recommends `Run final P7
current-scope closure review gate` as the next docs-only task. It is handoff /
evidence-index finalization evidence only: it does not close P7 current scope,
approve broader P7 implementation, approve training, approve source ingestion,
approve parser / reader / ingestion, approve actual feature extraction,
approve actual label generation, approve real data, approve model-output
integration, approve self-play, approve league, approve P8-P12 or provide
model-strength evidence.

`docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md`
runs the final P7 current-scope closure review gate. Decision: `P7 current
scope can close` for the exact current scope only: docs-only supervised
learning readiness chain plus the accepted minimal synthetic/local supervised
feature-label smoke implementation. It is P7 final current-scope closure
review evidence only. It does not close full P7, approve broader P7
implementation, approve training, approve source ingestion, approve parser /
reader / ingestion, approve actual feature extraction, approve actual label
generation, approve real data, approve model-output integration, approve
self-play, approve league, approve P8-P12 or provide model-strength evidence.

`docs/03_supervised_policy/03W_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_AFTER_CURRENT_SCOPE_CLOSURE.md`
defines the full P7 closure roadmap and remaining scope inventory after
current-scope closure. It records that P7 current scope is closed only for the
exact docs-only readiness chain plus accepted minimal synthetic/local
feature-label smoke implementation, classifies full-P7 remaining items as
required / deferred / blocked / later-stage / out of scope, and selects a
docs-only roadmap review gate as the next task. It is roadmap/inventory
definition evidence only, not full P7 closure, broader implementation
approval, training approval, source approval, parser / reader / ingestion
approval, real-data approval, P8-P12 entry approval or model-strength
evidence.

`docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md`
reviews the `03W` full P7 closure roadmap and remaining scope inventory after
current-scope closure. It records `Review can close`, confirms that the scope,
current-scope closure context, remaining-scope classifications, docs-first
roadmap, validation commands, evidence grade and governance synchronization
are sufficient, and selects
`Define broader P7 scope, entry criteria and first task before implementation`
as the next docs-only task. It is review evidence only, not full P7 closure,
broader implementation approval, training approval, source approval, parser /
reader / ingestion approval, real-data approval, P8-P12 entry approval or
model-strength evidence.

`docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
defines broader P7 scope, entry criteria and first task before implementation.
It records broader P7 purpose, allowed docs-only scope, forbidden scope,
implementation entry criteria, required upstream artifacts, blocked /
deferred / later-stage / out-of-scope items, reasons not to implement or train
yet, reasons not to enter P8-P12, planning decision and evidence grade. It
selects `Review broader P7 scope, entry criteria and first task before
implementation` as the next docs-only review gate. It is definition evidence
only, not broader P7 implementation approval, training approval, source
approval, parser / reader / ingestion approval, actual feature extraction or
label generation approval, real-data approval, P8-P12 entry approval or
model-strength evidence.

`docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews the `03Y` broader P7 scope, entry criteria and first-task definition.
It records `Review can close`, confirms that the `03Y` scope, context,
allowed docs-only scope, forbidden scope, entry criteria, implementation entry
criteria, upstream artifacts, classifications, evidence grade and governance
synchronization are sufficient, and selects
`Define broader P7 data/source readiness and source approval boundary before implementation`
as the next docs-only task. It is review evidence only, not full P7 closure,
broader implementation approval, training approval, source approval, parser /
reader / ingestion approval, actual feature extraction or label generation
approval, real-data approval, P8-P12 entry approval or model-strength
evidence.

`docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines broader P7 data/source readiness and source-approval boundary before
implementation. It records current source status, source category inventory,
readiness / approval vocabulary, source-specific approval-record requirements,
source approval vs ingestion vs training approval distinctions, parser /
reader / ingestion dependency, feature / label dependency, risk controls,
evidence requirements, first task candidate, planning decision and evidence
grade. It selects `Review broader P7 data/source readiness and source approval
boundary before implementation` as the next docs-only review gate. It is
boundary-definition evidence only, not source approval, training-data
approval, source ingestion approval, parser / reader / ingestion approval,
actual feature extraction or label generation approval, real-data approval,
training approval, P8-P12 entry approval or model-strength evidence.

`docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews the `03AA` broader P7 data/source readiness and source-approval
boundary before implementation. It records `Review can close`, confirms that
the scope, purpose, source status, source-category inventory, readiness /
approval vocabulary, source-specific approval-record requirements, concept
separation, parser / reader / ingestion dependency, feature / label
dependency, risks, evidence requirements, first task candidate, planning
decision and governance synchronization are sufficient. It selects
`Define broader P7 parser, reader and ingestion boundary before implementation`
as the next docs-only task. It is review evidence only, not full P7 closure,
source approval, training-data approval, source ingestion approval, parser /
reader / ingestion implementation or approval, actual feature extraction,
label generation, training approval, real-data approval, P8-P12 entry approval
or model-strength evidence.

`docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines the broader P7 parser, reader and ingestion boundary before
implementation. It records current parser / reader / ingestion status,
concept definitions, dependency order, future candidate classes,
approval-record fields, allowed future implementation boundaries, forbidden
scope, stop conditions, risk controls, evidence requirements, the next review
gate, planning decision and evidence grade. It selects
`Review broader P7 parser, reader and ingestion boundary before implementation`
as the next docs-only task. It is boundary-definition evidence only, not parser
implementation, reader implementation, ingestion implementation, parser /
reader / ingestion approval, source ingestion approval, source approval,
training-data approval, broad file ingestion, CLI, real-data use, actual
feature extraction, label generation, training approval, P8-P12 entry approval
or model-strength evidence.

`docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
reviews the `03AC` broader P7 parser, reader and ingestion boundary before
implementation. It records `Review can close`, confirms that scope, purpose,
current parser / reader / ingestion status, concept definitions, dependency
map, candidate classes, future approval fields, allowed / forbidden boundary,
stop conditions, risk controls, evidence requirements, first task candidate,
planning decision, evidence grade and governance synchronization are
sufficient, and selects `Define broader P7 actual feature extraction and label
generation boundary before implementation` as the next docs-only task. It is
review evidence only, not parser implementation, reader implementation,
ingestion implementation, parser / reader / ingestion approval, source
ingestion approval, source approval, training-data approval, broad file
ingestion, CLI, real-data use, actual feature extraction, actual label
generation, supervised dataset construction, training approval, P8-P12 entry
approval or model-strength evidence.

`docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
defines the broader P7 actual feature extraction and label generation boundary
before implementation. It records feature / label vocabulary, current status,
dependency order, parser / reader / ingestion separation, synthetic/local smoke
non-training boundary, candidate feature and label families, future approval
fields, allowed / forbidden scope, stop conditions, risk controls, evidence
requirements, first task candidate, planning decision and evidence grade. It
is boundary-definition evidence only, not actual feature extraction
implementation, label generation implementation, feature / label approval,
source approval, source ingestion, parser / reader / ingestion approval,
supervised dataset construction, training, model architecture, real-data use,
P8-P12 entry or model-strength evidence.

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
docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md
docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md
docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md
docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md
docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md
docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md
docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md
docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md
docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md
docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md
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

`docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
defines P6 current-scope data-system closure criteria after minimal replay
schema acceptance. It records current accepted scope, minimum closure
criteria, an exit readiness checklist, required remaining current-scope items,
deferred items, P7-P12 non-entry conditions and the next review-gate task. It
is closure-criteria definition evidence only, not full P6 closure, not
current-scope P6 closure, not new implementation approval, not parser /
dataset-reader / ingestion / feature / label evidence, not real-data approval,
not model-strength evidence and not P7-P12 entry approval.
`docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
reviews the `02R` closure criteria. It records that `02R` scope is correct,
the C1-C25 criteria are sufficient, the exit readiness checklist is auditable,
remaining items and deferred items are correctly classified, P7-P12 non-entry
conditions are sufficient, governance is synchronized, validation passes and
the review can close with no blocker. It is closure-criteria review evidence
only, not full P6 closure, not current-scope P6 closure, not new
implementation approval and not P7-P12 entry approval.
`docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
runs the final P6 current-scope data-system closure review gate. It records
that current-scope P6 can close for the accepted synthetic/local minimal replay
schema and project-authored synthetic fixture scope only. It is final
current-scope closure review evidence only: full P6 is not closed, P7-P12
entry is not approved, and parser / dataset-reader / ingestion / feature /
label / real-data / model-output / CLI / training / self-play / league work
remains unapproved.

`docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
defines the full P6 closure roadmap and remaining scope inventory after
accepted current-scope closure. It classifies remaining items as required,
deferred, blocked, later-stage or explicitly out of scope; selects a docs-only
roadmap review gate as the next task; and keeps full P6 open, P7-P12
unapproved and implementation / real-data / parser / reader / ingestion /
feature / label work unapproved.

`docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
reviews the `02U` roadmap / inventory. It records that the review can close
with no blocker, confirms the classification and roadmap are conservative and
auditable, and selects a docs-only full P6 closure criteria definition as the
next task. It is review evidence only, not full P6 closure, P7-P12 entry
approval, implementation approval, real-data approval, ingestion evidence or
model-strength evidence.

`docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
defines full P6 closure criteria after the `02U` roadmap / inventory and `02V`
review. It records full-P6 closure scope, C1-C27 closure criteria, exit
readiness, required remaining closure items, deferred / blocked /
later-stage / out-of-scope classifications and P7-P12 non-entry conditions.
It is criteria-definition evidence only: full P6 remains open, P7-P12 entry is
not approved, and no implementation, parser, reader, ingestion, feature,
label, real-data or model-strength work is approved.

`docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
reviews the `02W` full P6 closure criteria. It records that the review can
close with no blocker, confirms that C1-C27 criteria and the exit readiness
checklist are conservative and auditable, and selects full P6 handoff /
evidence index finalization as the next docs-only task. It is criteria-review
evidence only, not full P6 closure, P7-P12 entry approval, implementation
approval, real-data approval, ingestion evidence or model-strength evidence.

`docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the full P6 handoff and evidence index after the `02X` criteria
review. It records a finalization-ready full P6 handoff summary, an evidence
index covering `02A`-`02X`, `12B` / `12C`, accepted implementation artifacts
and governance artifacts, evidence grade consistency, remaining required
full-P6 items and the next risk / source-rights consistency review scope. It
is handoff / evidence-index finalization evidence only: full P6 remains open,
P7-P12 entry remains unapproved, and no parser, dataset reader, ingestion,
feature extraction, label generation, real data, CLI, model-output
integration, training, self-play, league or model-strength claim is approved.

`docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
reviews full P6 risk-register and source-rights inventory consistency before
the final full P6 closure review. It confirms that source-rights inventory,
risk register, evidence index and governance docs consistently keep real
Tenhou, real haifu, external logs, platform data, accounts, parser / reader /
ingestion, feature extraction, label generation, CLI, model-output
integration, third-party artifacts, training, self-play, league and P7-P12
unapproved. The review can close with no risk/source-rights blocker for the
final full P6 closure review gate. It is not full P6 closure, not P7-P12
approval, not source approval and not model-strength evidence.

`docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
runs the final full P6 closure review gate. It records that full P6 can close
for the documented P6 data-system scope: docs/governance/source-rights
planning, accepted synthetic/local minimal replay schema and project-authored
synthetic fixture smoke implementation, and deferred/blocked/later-stage
inventory. It is not P7-P12 entry approval, not P7 first-task approval, not
new implementation approval, not real-data/source/ingestion approval and not
model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
candidate-promotion evidence.

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
