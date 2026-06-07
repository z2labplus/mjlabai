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
| P6 | Data system | Build replay, feature, label and quality pipelines for training and evaluation | Supervised training and offline evaluation datasets can be generated | Closed for accepted synthetic/local minimal replay schema and project-authored fixture current scope only; full P6 remains open |
| P7 | Supervised policy model | Train a base strategy model from high-quality human play and key decisions | Model beats simple baselines in key offline scenarios and completes games | Future |
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
The project is in P6 data-system docs-only full-closure criteria review
after the exact approved replay schema / synthetic fixture implementation was
implemented, reviewed, accepted as current-scope complete, closed for the
accepted synthetic/local minimal scope only, reviewed in a post-current-scope
transition gate, inventoried in `02U` and reviewed in `02V` with no blocker.
`02W` now defines full P6 closure criteria; the next step is a docs-only
review of those criteria.
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
The next docs-only criteria review must not expand into parser, dataset
reader, data ingestion, feature extraction, label generation, training,
self-play, league, real Tenhou, external-log ingestion or P7-P12 work.

## Guardrail

Do not train, tune, build Tenhou integration, scrape data or start self-play before the relevant stage and `docs/10_next/10_NEXT.md` explicitly allow it.
