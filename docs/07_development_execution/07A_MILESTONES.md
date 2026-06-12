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
| P7 | Supervised policy model | Train a base strategy model from high-quality human play and key decisions | Model beats simple baselines in key offline scenarios and completes games | Data/source readiness inventory defined/reviewed; feature/label boundary defined/reviewed; risk/evidence taxonomy defined/reviewed; minimal synthetic/local supervised fixture proposal defined/reviewed in `03M`/`03N`; approval-decision preparation next; implementation unapproved |
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
reviews that proposal and records `Review can close`. The current next step is
docs-only approval-decision preparation for the minimal synthetic/local
supervised fixture and feature-label smoke implementation task.
No source is approved for P7 training, source ingestion, parser / reader /
ingestion, feature extraction or label generation. P7 implementation, P7
first-task execution and P8-P12 entry remain unapproved.
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
