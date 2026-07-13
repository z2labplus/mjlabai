# 12N_P8_SELF_PLAY_RL_DEPENDENCY_MAP_REVIEW_BEFORE_ANY_IMPLEMENTATION

## Scope

This document reviews
`docs/12_technical_plan/12M_P8_SELF_PLAY_RL_DEPENDENCY_MAP_BEFORE_ANY_IMPLEMENTATION.md`.

This is a docs-only review gate. It does not approve P8 entry, P8
implementation, a P8 implementation prompt, a P8 first executable task,
P9-P12 entry, production code, tests, fixtures, data files, self-play, RL
execution, training, tuning, evaluation, league, source approval/ingestion,
real data, broad file ingestion, CLI, feature extraction, label generation,
dataset construction, model-output integration or any strength claim.

## Reviewed Artifacts

Primary artifact:

- `docs/12_technical_plan/12M_P8_SELF_PLAY_RL_DEPENDENCY_MAP_BEFORE_ANY_IMPLEMENTATION.md`

P8 planning context:

- `docs/12_technical_plan/12L_P8_RISK_AND_EVIDENCE_TAXONOMY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12K_P8_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12J_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_REVIEW.md`
- `docs/12_technical_plan/12I_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_AFTER_P8_P12_TRANSITION_SCOPE_REVIEW.md`
- `docs/12_technical_plan/12H_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_REVIEW.md`
- `docs/12_technical_plan/12G_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK.md`
- `docs/12_technical_plan/12F_POST_FULL_P7_TRANSITION_REVIEW.md`

Closure and governance context:

- `docs/03_supervised_policy/03BL_FINAL_FULL_P7_CLOSURE_REVIEW.md`
- P7 closure-preparation chain referenced by `03BL`.
- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- handoff, index, technical plan, `10_NEXT`, evidence, risk, decision,
  changelog, stage contract, milestones and backlog.
- accepted synthetic/local P6/P7 implementation artifacts, read-only.

## Review Checklist

| review area | result | finding |
|---|---|---|
| Scope | pass | `12M` is dependency-map definition only and grants no entry or execution permission. |
| Full P7 / P8 recap | pass | Closure and transition/taxonomy history is accurate and bounded. |
| Non-approval baseline | pass | P8 entry/implementation and every executable workstream remain unapproved. |
| Vocabulary | pass | Required, blocked, deferred, later-stage, out-of-scope, not-approved and planning-only are distinct. |
| D1-D18 | pass | Dependency families cover governance, protocol, objective, environment, model, data, run, evaluation, opponent, artifacts and later stages. |
| Dependency matrix | pass | Execution-like dependencies have `approved_now = no`; docs-only governance rows are explicitly limited. |
| RD1-RD12 | pass | Future prerequisites are complete and RD12 requires a separate approval decision. |
| Status classifications | pass | Blocked, deferred and later-stage lists are conservative and auditable. |
| Risk linkage | pass | D1-D18 collectively cover R1-R20; the focused table covers all required high-risk themes. |
| Evidence linkage | pass | E1-E25 remain separated by grade and E20-E24 are unavailable. |
| Model-output boundary | pass | Interface/schema/environment/evaluation/review/decision prerequisites are explicit. |
| Evaluation boundary | pass | Protocol, metrics, samples, leakage, uncertainty, review and decision are required. |
| Source / real-data boundary | pass | Rights, privacy, platform, approval, ingestion, validation and logging remain required. |
| Stop conditions | pass | Stage jumps, execution, real data, artifacts and overclaims require stopping. |
| Candidate directions | pass | Review is selected first; implementation/execution candidates are rejected or forbidden. |
| Governance synchronization | pass | Current task and non-approval posture are consistent across control documents. |

## Full P7 / P8 Risk-Taxonomy Recap Review

The recap passes:

- Full P7 is closed only for the documented P7 supervised-learning scope.
- `12F`-`12H` established and reviewed P8-P12 docs-only transition planning.
- `12I` defined P8 scope/entry criteria and `12J` reviewed it.
- `12K` defined R1-R20/E1-E25 and `12L` reviewed it.
- P8 remains docs-only planning; P8 entry and implementation remain
  unapproved; P9-P12 remain unapproved.

## P8 Self-Play / RL Non-Approval Baseline Review

The baseline passes. `12M` keeps unapproved:

- P8 entry, implementation, first executable task and implementation prompt.
- self-play, RL execution, training/tuning, evaluation, league and
  model-output integration.
- source approval/ingestion, real data and P9-P12.

It also correctly records that no self-play, RL, training, evaluation,
league, model-output or model-strength evidence and no real-data or
source-ingestion permission exist.

## Dependency Map Vocabulary Review

The vocabulary is safe:

- `required` means necessary later, not approved now.
- `blocked` requires separate resolution, review and approval.
- `deferred` means postponed, not approved.
- `later-stage` is outside current P8 scope.
- `out-of-scope` is forbidden now.
- `planning-only` permits documentation only.

Dependency definition cannot be interpreted as implementation permission.

## Dependency Families Review

D1-D18 pass. Each row supplies the required identifier, name, description,
status, downstream use, approval state, blocker, evidence, risk linkage, stop
condition and notes.

Coverage includes:

- D1-D2: reviewed P8 scope and taxonomy prerequisites.
- D3-D5: self-play protocol, RL objective/reward and environment/simulator.
- D6-D10: model output, training/tuning, evaluation, source/real data and
  feature/label/dataset.
- D11-D14: opponent pool, league/promotion, compute/reproducibility and
  checkpoints/artifacts.
- D15-D18: governance, P9-P12 separation, evidence-grade safety and
  third-party artifacts/binaries/weights.

No execution-like dependency is approved. D15 and D17 permit only active
docs-only governance and evidence-grade control, not implementation.

## Dependency Matrix Review

The matrix passes. Its `self_play`, `RL`, `training` and `evaluation` columns
are equivalent to the required-for relationship requested by the review.
Every execution-like row is blocked or later-stage with `approved_now = no`.
The only docs-only entries concern governance/evidence control and cannot
authorize implementation.

## Required Dependencies Review

RD1-RD12 pass. They require reviewed scope/taxonomy/map, separate protocol,
objective, environment, model-output, training, evaluation and source
boundaries, explicit `10_NEXT` authorization and a separate approval decision.

None of RD1-RD12 is approved by `12M`. RD12 prevents implementation without a
separate decision.

## Blocked Dependencies Review

The blocked list passes and includes source approval/ingestion, Tenhou/haifu,
external/platform/account data, training data/runs, model output, evaluation,
self-play, RL, league, strength evidence, P9-P12 and unknown third-party
artifacts.

## Deferred Dependencies Review

The deferred list passes. Self-play protocol, RL objective/reward,
environment/simulator, downstream dependency follow-ups, source-rights review
and the approval-decision path remain postponed and unapproved.

## Later-Stage / Out-of-Scope Dependencies Review

The classification passes. P9 search/risk, P10 league/mainline selection, P11
large-scale training, P12 Tenhou validation, promotion, ranked Tenhou,
stable-dan and LuckyJ comparison remain later-stage/out-of-scope.

## Self-Play / RL Risk Linkage Review

The D1-D18 table collectively maps all R1-R20 risks. The focused linkage table
also covers every required high-risk theme: reward hacking, collapse,
opponent/league bias, reproducibility, compute escalation, overclaim,
source/real-data risk, P9-P12 creep, external artifacts and governance drift.

## Evidence Linkage Review

The evidence linkage passes:

- E1-E4/E25 support reviewed planning context.
- this map is E5-style dependency-map definition evidence.
- E6 review evidence is created only by this review.
- E7-E24 remain unavailable for approval, implementation, source, training,
  self-play, league, evaluation, model output, strength, Tenhou, stable-dan,
  LuckyJ or promotion claims.

## Model-Output Dependency Boundary Review

Pass. No model-output integration is approved. Future work requires interface,
output-schema, environment, evaluation, risk/evidence review and exact
approval-decision boundaries.

## Evaluation Dependency Boundary Review

Pass. No evaluation implementation is approved. Future work requires protocol,
metric/sample definitions, leakage and uncertainty controls, governance review
and an exact approval decision.

## Source / Real-Data Dependency Boundary Review

Pass. No real data or source ingestion is approved. Future work requires
source-rights, privacy/platform/account-policy review, source approval,
ingestion boundary, validation protocol and evidence logging.

## Stop Conditions Review

The stop conditions pass. They stop on implied entry/implementation approval,
implementation prompts, execution, real/platform/account data, source or
model-output work, strength claims, P9-P12 jumps, code/tests/data, unknown
artifacts, third-party binaries and unauthorized `10_NEXT` implementation.

## Candidate Next Directions Review

The candidates are safe. A review is correctly selected before later boundary
definition. Implementation, training, self-play, real-data, model-output and
P9-P12 candidates are rejected or forbidden.

After this review, the narrowest safe next planning task is:

```text
Define P8 self-play protocol boundary before any implementation.
```

This orders protocol semantics before RL reward/objective semantics and keeps
all work docs-only. It does not approve or execute self-play.

## Governance Synchronization Review

Handoff, index, `10_NEXT`, technical plan, evidence log, risk register,
decision record, stage contract, changelog, milestones and backlog are aligned
to this review and the next docs-only protocol-boundary task.

## Validation Results

```text
git diff --check: passed
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py: passed, 15 tests
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py: passed, 11 tests
python3 -m unittest tests/supervised/test_feature_label_schema.py: passed, 11 tests
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py: passed, 1 test
python3 -m unittest tests/data/test_replay_schema.py: passed, 7 tests
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py: passed, 1 test
```

These are existing synthetic/local guardrail validation results only.

## Review Decision

```text
A. Review can close.
```

No blocker or overclaim was found.

## Next Task Recommendation

```text
Define P8 self-play protocol boundary before any implementation.
```

The next task must be docs-only. It must not approve P8 entry,
implementation, an implementation prompt or a first executable task; execute
self-play, RL, training, tuning, evaluation or league; approve source/real
data/model output; claim strength; or enter P9-P12.

## Evidence Grade

```text
P8 self-play / reinforcement-learning dependency map review evidence only.
```

## Explicit Non-Evidence

This review is not P8 entry/implementation approval, an implementation prompt,
P9-P12 approval, training, tuning, evaluation, self-play, league, RL
execution, source approval/ingestion, real Tenhou/haifu/external/platform data,
model-output integration, model-strength evidence, Tenhou ranked evidence,
stable-dan evidence, LuckyJ `10.68` comparison or candidate promotion.
