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
| P4 | Unified mahjong environment and interface | Define shared state, legal actions, logs, replays and adapter contracts | Different candidates can run through the same interface | Active prerequisite: synthetic transition is review-closed in `04I`; pinned MahJax integration is review-closed in `04K`; exact 256-cap JIT single-round rollout plus global-seat-score review fix is implemented with 314 tests passing and exact review next; no full conformance/shared candidate adapter yet |
| P5 | Unified evaluation system | Compare all models with Tenhou-oriented metrics under one harness | Stable comparison of baselines and project models | Closed for current synthetic/local evaluation groundwork scope |
| P6 | Data system | Build replay, feature, label and quality pipelines for training and evaluation | Supervised training and offline evaluation datasets can be generated | Closed for documented P6 data-system scope only; parser / reader / ingestion / feature / label and real data remain unapproved |
| P7 | Supervised policy model | Train a base strategy model from high-quality human play and key decisions | Model beats simple baselines in key offline scenarios and completes games | Current scope closed only for docs-only readiness chain plus exact minimal synthetic/local feature-label smoke implementation in `03V`; broader scope / entry criteria reviewed in `03Z`; broader data/source readiness and source-approval boundary defined in `03AA` and reviewed in `03AB`; broader parser / reader / ingestion boundary defined in `03AC` and reviewed in `03AD`; broader actual feature extraction and label generation boundary defined in `03AE` and reviewed in `03AF`; broader supervised dataset construction / split / leakage boundary defined in `03AG` and reviewed in `03AH`; broader training-data approval / training-run boundary defined in `03AI` and reviewed in `03AJ`; broader model architecture / trainer planning boundary defined in `03AK` and reviewed in `03AL`; broader evaluation dependency / model-strength evidence boundary defined in `03AM` and reviewed in `03AN`; broader implementation readiness checklist defined in `03AO` and reviewed in `03AP`; broader minimal implementation proposal boundary defined in `03AQ` and reviewed in `03AR`; broader minimal implementation proposal drafted in `03AS` for review only and reviewed in `03AT`; exact broader P7 minimal synthetic/local parser-reader smoke implementation approved in `03AU` for two exact files only, implemented in those exact files, reviewed in `03AV` with `Review can close`, and accepted as current-scope complete on 2026-07-01 for that exact synthetic/local scope only; full P7 scope expansion plan defined in `03AW` and reviewed in `03AX`; P7 minimal implementation proposal drafted in `03AY` for review only and reviewed in `03AZ` with `Review can close`; approval decision recorded in `03BA` as `Approved for next exact minimal implementation task`, limited to `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`, `tests/supervised/test_synthetic_parser_reader_smoke_extension.py` and direct docs/governance synchronization; exact extension implementation is now added in those approved files only; `03BB` reviewed it and recorded `Review cannot close because blockers exist` due to missing explicit top-level `bytes`, `bytearray` and `Mapping` rejection test coverage; `03BC` approved only the next exact test-only blocker-resolution task in `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`; that exact test-only blocker fix is now complete with only explicit top-level `bytes`, `bytearray` and `Mapping` rejection tests added in the approved test file; `03BD` reran the implementation review after blocker fix and recorded `Review can close`; `03BE` accepted the exact parser-reader smoke extension implementation as current-scope complete only for the exact `03BA` / `03BC` scope; `03BF` selected full P7 closure criteria definition as the next docs-only planning step after that acceptance; `03BG` defined full P7 closure criteria without closing full P7; `03BH` reviewed those criteria and recorded `Review can close`; `03BI` finalized the full-scope handoff and evidence index after closure criteria review; `03BJ` reviewed that handoff/evidence index and recorded `Review can close`; `03BK` reviewed full-scope risk, source-rights and evidence consistency and found no blocker; `03BL` ran final full P7 closure review and recorded that full P7 can close only for the documented supervised-learning scope; `12F` completed post-full-P7 transition review and found no blocker for defining P8-P12 docs-only scope / entry criteria / first planning task; `12G` defined that transition scope, entry criteria and first planning task and selected a docs-only review gate as the next task; `12H` reviewed `12G`, recorded `A. Review can close`, and selected P8 scope / entry criteria / first planning task definition as the next docs-only task; broad implementation, evaluation implementation, metric implementation, evaluation runner, benchmark harness, strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ comparison, candidate promotion, training, training-data construction, training-data approval, training-run approval, training-run implementation, source approval, source ingestion, broad parser / reader / ingestion implementation, actual feature extraction, actual label generation, feature tensors, labels, examples, splits, supervised dataset construction, leakage-test implementation, model architecture / trainer implementation, dataloader / optimizer / loss implementation, checkpoints, weights, real data, model-output integration and P8-P12 remain unapproved |
| P8 | Self-play reinforcement learning | Optimize toward Tenhou pt EV, placement and stable-dan objectives | RL checkpoint beats supervised checkpoint in the unified league | Exact two-policy interaction is accepted; further wrappers are deferred while the selected MahJax P4 environment path is integrated and reviewed; no production self-play or model-strength claim approved |
| P9 | Search and risk model | Improve push/fold, deal-in risk, south-round rank control and oorasu decisions | Search-enhanced model beats non-search model in scenarios and league play | Future |
| P10 | Model league and mainline selection | Run long comparisons among baselines, SL, RL, search and historical best versions | A candidate reliably beats the current mainline with uncertainty reported | Future |
| P11 | Large-scale training and stability validation | Expand compute only after the route is justified by previous gates | Internal evaluation approaches or exceeds the LuckyJ 10.68 target line | Future |
| P12 | Tenhou target validation | Validate whether the system can exceed LuckyJ 10.68 under compliant conditions | Long-term stable dan, pt EV, rank metrics, latency and logs are verified | Final |

## 2026-07-18 P8 Two-Step Acceptance And Interleaved Trace Approval Update

## 2026-07-18 P8 One-Step Acceptance And Bounded Sequence Approval Update

- `12AU` accepts the exact review-closed one-step closed loop as current-scope
  complete.
- Directly approved one exact 1-through-4-step sequence with reviewed helper
  reuse, model continuity and globally unique candidate-transition IDs.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, environment/episode, replay, self-play, persistence, production
  evaluation, real data, broad P8 or P9-P12 work was added by this decision.

## 2026-07-18 P8 Bounded Policy-Improvement Sequence Implementation Update

- Added the exact `12AU`-approved sequence module, package exports and 10
  focused tests.
- Enforced 1-through-4 exact steps, reviewed one-step helper reuse, direct model
  continuity, global IDs, indexed chained errors and immutable output.
- Full explicit repository run reports 267 tests OK with two environment-gated
  skips; compile/diff checks and independent 1/2/4-step probes pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No general environment/episode, replay, self-play, persistence, production
  evaluation, real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Bounded Sequence Review Closure Update

- Added `12AV`; decision after one exact blocker fix: `A. Review can close.`
- Initial two-traversal conformance blocker was fixed in `8897793`; source now
  has one explicit bounded step loop and AST regression coverage.
- All 267 explicit tests are OK with two environment-gated skips; compile/diff
  checks and independent 1/2/4-step probes pass.
- Next: accept/reject current scope and directly approve/defer one exact
  bounded two-policy alternating interaction, with no sibling boundary.
- No general environment/episode, production self-play/evaluation, real data,
  strength claim, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Bounded Sequence Acceptance And Two-Policy Approval Update

- `12AW` accepts the exact review-closed bounded single-policy sequence as
  current-scope complete.
- Directly approved exactly two synthetic/local policy models and two/four
  A/B alternating turns with independent continuity and global IDs.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, environment/episode/outcome, replay, production self-play/
  evaluation, real data, broad P8 or P9-P12 work was added by this decision.

## 2026-07-18 P8 Two-Policy Interaction Implementation Update

- Added the exact `12AW`-approved interaction module, package exports and 12
  focused tests.
- Enforced two participants, two/four A/B turns, reviewed helper reuse,
  actor-only updates, independent model lineage and global IDs.
- Full explicit repository run reports 279 tests OK with two environment-gated
  skips; compile/diff checks and independent probes pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No environment/episode/outcome, replay, production self-play/evaluation,
  real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Two-Policy Interaction Review Closure Update

- Added `12AX`; decision: `A. Review can close.`
- Confirmed exact participants/turns, A/B alternation, actor-only updates,
  independent model lineage, helper reuse, global IDs and frozen output.
- All 279 explicit tests are OK with two environment-gated skips; compile/diff
  checks and independent probes pass; no blocker exists.
- Next: accept/reject current scope and resolve the P4-owned environment
  prerequisite. Another synthetic interaction wrapper is forbidden.
- No environment/episode/outcome, production self-play/evaluation, real data,
  strength claim, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Acceptance And P4 Environment Activation Update

- Accepted the exact review-closed P8 two-policy interaction only for its
  synthetic/local scope and banned another interaction wrapper.
- Confirmed no environment package/state/transition exists; `04A` remains
  planned and `12S`/`12T` are docs-only boundaries.
- Activated P4 and directly approved the exact `04H` single-transition,
  four-seat, strict-`dahai` synthetic/local contract smoke.
- Zero mandatory gates remain before code; direct P4 implementation is next.
- No general engine, multi-step episode, production self-play/evaluation, real
  data, Tenhou, broad P8 or P9-P12 work was added by this decision.

## 2026-07-18 P4 Synthetic Environment Transition Implementation Update

- Added the exact `04H`-approved environment package, transition module and 12
  focused tests.
- Enforced four-seat identity, two strict `dahai` legal actions, authoritative
  match selection and immutable terminal state progression.
- Full explicit repository run reports 291 tests OK with two environment-gated
  skips; compile/diff checks and independent all-seat/action probes pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No full rules/scoring engine, hand/hidden-state/RNG, multi-step episode,
  self-play, real data, Tenhou, broad P8 or P9-P12 work was added.

## 2026-07-18 P4 Synthetic Environment Transition Review Closure Update

- Added `04I`; decision: `A. Review can close.`
- Confirmed exact strict-action authority, state/provenance validation,
  deterministic event and immutable terminal post-state.
- All 291 explicit tests are OK with two environment-gated skips; compile/diff
  checks and independent all-seat/action probes pass; no blocker exists.
- Next: accept/reject current scope and select/reject one proven local riichi
  environment integration path. Another authored wrapper is forbidden.
- No full engine, episode, self-play, real data, Tenhou, strength claim, broad
  P8 or P9-P12 work was added.

## 2026-07-18 P8 Two-Step Acceptance And Interleaved Trace Approval Update

- `12AG` accepts the exact review-closed two-step scope as current-scope
  complete.
- Directly approved one fixed four-record A/B/A/B interleaved two-key trace
  that verifies independent value continuity through the base helper.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, replay buffer, environment, self-play, model, training/evaluation,
  real data, broad P8 or P9-P12 work was added by this decision.

## 2026-07-18 P8 Interleaved Policy-Update Trace Implementation Update

- Added the exact `12AG`-approved trace module, package exports and 11 focused
  tests.
- Enforced exact four-record A/B/A/B ordering, two independent keys, source
  and ID constraints, per-key continuity, immutable output and error chaining.
- Reused the reviewed single-step helper for all four calculations; 79 total
  approved tests pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No variable batch, replay buffer, environment, self-play, model, production
  training/evaluation, real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Interleaved Policy-Update Trace Review Closure Update

- Added `12AH`; decision: `A. Review can close.`
- Confirmed exact `12AG` file/API/input/order/continuity/helper-reuse/error-
  chain/output/export/warning and forbidden-scope compliance.
- All 79 approved tests, compile/diff checks and independent probes pass; no
  blocker or production code/test change was required.
- Next: current-scope acceptance plus direct approval of one exact executable
  P8 task, with no sibling proposal or boundary.

## 2026-07-18 P8 Interleaved Trace Acceptance And Policy-Table Approval Update

- `12AI` accepts the exact review-closed interleaved trace as current-scope
  complete.
- Directly approved one fixed two-key in-memory policy-value table update smoke
  that reuses the reviewed trace helper.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, persistence, replay buffer, environment, self-play, model,
  training/evaluation, real data, broad P8 or P9-P12 work was added by this
  decision.

## 2026-07-18 P8 Fixed Policy-Value Table Update Implementation Update

- Added the exact `12AI`-approved table module, package exports and 11 focused
  tests.
- Bound one exact frozen two-entry A/B table to the reviewed trace keys and
  initial values, called the trace helper once and returned normalized finals.
- All 90 approved tests pass; compile and diff checks pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No mutable/dynamic table, persistence, trainer, environment, self-play,
  model, production training/evaluation, real data, broad P8 or P9-P12 work
  was added.

## 2026-07-18 P8 Fixed Policy-Value Table Review Closure Update

- Added `12AJ`; decision: `A. Review can close.`
- Confirmed exact `12AI` file/API/input/key/value/helper-reuse/error-chain/
  output/export/warning and forbidden-scope compliance.
- All 90 approved tests, compile/diff checks and independent probes pass; no
  blocker or production code/test change was required.
- Next: current-scope acceptance plus direct approval of one exact executable
  P8 task, with no sibling proposal or boundary.

## 2026-07-18 P8 Fixed Table Acceptance And Two-Pass Approval Update

- `12AK` accepts the exact review-closed fixed table update as current-scope
  complete.
- Directly approved one fixed two-pass table-update sequence that reuses the
  reviewed table helper twice and carries intermediate table state.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, variable epoch/trainer, persistence, environment, self-play, model,
  training/evaluation, real data, broad P8 or P9-P12 work was added by this
  decision.

## 2026-07-18 P8 Fixed Two-Pass Table Sequence Implementation Update

- Added the exact `12AK`-approved sequence module, package exports and 11
  focused tests.
- Called the reviewed table helper exactly twice, carried pass 1 finals into
  pass 2 and rejected duplicate IDs across all eight records.
- All 101 approved tests pass; compile and diff checks pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No third pass, variable epoch/trainer, persistence, environment, self-play,
  model, production training/evaluation, real data, broad P8 or P9-P12 work
  was added.

## 2026-07-18 P8 Fixed Two-Pass Sequence Review Closure Update

- Added `12AL`; decision: `A. Review can close.`
- Confirmed exact two-pass helper reuse, continuity, identity, frozen output,
  errors, exports, warnings and 101 passing tests; no blocker was found.
- Next: directly approve or defer one bounded synthetic/local tabular trainer.
- A third fixed-pass wrapper and sibling boundary are forbidden.

## 2026-07-18 P8 Two-Pass Acceptance And Bounded Trainer Approval Update

- `12AM` accepts the review-closed fixed two-pass scope as current-scope
  complete.
- Directly approved the first loop-based synthetic/local tabular trainer with
  an exact 1-through-8 pass bound and reviewed helper reuse.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, model/network, optimizer, environment, self-play, persistence,
  real data, production evaluation, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Bounded Tabular Trainer Implementation Update

- Added the exact `12AM`-approved trainer module, package exports and 11
  focused tests.
- Enforced an exact tuple of 1 through 8 ordered passes, one reviewed table-
  helper call per pass, state continuity, global ID uniqueness, frozen history
  and pass-indexed chained errors.
- All 112 approved tests pass; compile and diff checks pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No unbounded loop, environment, self-play, model/network, optimizer,
  production evaluation, real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Bounded Tabular Trainer Review Closure Update

- Added `12AN`; decision: `A. Review can close.`
- Confirmed exact pass bound, helper reuse, continuity, identity, frozen
  output, errors, exports, warnings and 112 passing tests; no blocker found.
- Next: current-scope acceptance plus direct approval or deferment of one exact
  materially progressive executable P8 task.
- A sibling trainer wrapper and another boundary chain are forbidden.

## 2026-07-18 P8 Bounded Trainer Acceptance And Linear Model Approval Update

- `12AO` accepts the review-closed bounded trainer as current-scope complete.
- Directly approved a fixed two-feature/two-action linear Q model training
  smoke over four synthetic/local transitions and at most eight epochs.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, environment, replay, self-play, generic optimizer, persistence,
  real data, production evaluation, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Linear Action-Value Model Training Implementation Update

- Added the exact `12AO`-approved model-training module, package exports and 13
  focused tests.
- Trained a fixed two-feature/two-action linear Q model over four safe
  transitions for 1 through 8 deterministic epochs using exact TD updates.
- All 125 approved tests pass; compile and diff checks pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No environment, replay, self-play, generic optimizer, tensor framework,
  persistence/checkpoint, real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Linear Model Training Review Closure Update

- Added `12AP`; decision: `A. Review can close.`
- Confirmed exact model/input shapes, provenance, epoch cap, TD formulas,
  selected-action updates, diagnostics, errors and 125 passing tests.
- Next: current-scope acceptance plus direct approval or deferment of one exact
  inference/greedy-decision executable P8 task.
- Another training wrapper and sibling boundary are forbidden.

## 2026-07-18 P8 Linear Model Acceptance And Greedy Decision Approval Update

- `12AQ` accepts the review-closed linear model training as current-scope
  complete.
- Directly approved deterministic inference and greedy decisions over one
  frozen model and exactly three synthetic/local probes.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, environment/gameplay, replay, self-play, model loading,
  persistence, real data, production evaluation, broad P8 or P9-P12 work was
  added.

## 2026-07-18 P8 Linear Greedy Decision Implementation Update

- Added the exact `12AQ`-approved decision module, package exports and 11
  focused tests.
- Reused reviewed helpers to compute two values for exactly three safe probes
  and applied the lower-index tie rule.
- All 136 approved tests pass; compile and diff checks pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No environment/gameplay, self-play, stochastic selection, model loading,
  persistence, real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Linear Greedy Decision Review Closure Update

- Added `12AR`; decision: `A. Review can close.`
- Confirmed exact model/probes/provenance, helper calls, action values, tie
  behavior, diagnostics, errors and 136 passing tests.
- Next: current-scope acceptance plus direct approval or deferment of one exact
  one-step policy-improvement closed-loop P8 task.
- Another inference wrapper and sibling boundary are forbidden.

## 2026-07-18 P8 Greedy Decision Acceptance And Closed-Loop Approval Update

- `12AS` accepts the review-closed greedy-decision diagnostic as current-scope
  complete.
- Directly approved one before decision, one action-selected transition batch,
  one reviewed training epoch and one after decision.
- Zero mandatory gates remain before code; direct implementation is next.
- No code, general environment/episode, replay, self-play, model loading,
  persistence, real data, production evaluation, broad P8 or P9-P12 work was
  added.

## 2026-07-18 P8 One-Step Policy Improvement Implementation Update

- Added the exact `12AS`-approved closed-loop module, package exports and 10
  focused tests.
- Validated both action-indexed batches, ran reviewed decision/train/decision
  helpers and trained only the controlled-action-selected batch for one epoch.
- All 146 approved tests pass; compile and diff checks pass.
- Next: one exact implementation review, with no sibling boundary/proposal.
- No general environment/episode, replay, self-play, persistence, real data,
  broad P8 or P9-P12 work was added.

## 2026-07-18 P8 One-Step Policy Improvement Review Closure Update

- Added `12AT`; decision: `A. Review can close.`
- Confirmed candidate validation, both action paths, helper order, model
  lineage, selected IDs, stage errors and 146 passing tests.
- Next: current-scope acceptance plus direct bounded sequence approval or
  deferment.
- Another fixed one-step wrapper and sibling boundary are forbidden.

## 2026-07-18 P8 Two-Step Policy-Update Smoke Review Closure Update

- Added `12AF`; decision: `A. Review can close.`
- Confirmed every exact `12AE` requirement, 68 passing tests and additional
  in-memory adversarial probes; no blocker or code/test fix was found.
- Next: current-scope acceptance plus direct approval of one next executable
  P8 task, with no sibling boundary.
- No production code, test, self-play, model, training/evaluation, real data,
  broad P8 or P9-P12 work was added in the review.

## 2026-07-18 P8 Two-Step Policy-Update Smoke Implementation Update

- Added the exact `12AE`-approved sequence module, package exports and focused
  tests.
- Reused the reviewed single-step helper and enforced exact two-step ordering,
  identity, distinct IDs, continuity, immutable output and error chaining.
- 10 sequence, 12 base and 46 regression tests pass; exact review is next.
- No environment, episode, self-play, model, production training/evaluation,
  real data, broad P8 or P9-P12 work was added.

## 2026-07-18 P8 Current-Scope Acceptance And Next Task Approval Update

- `12AE` accepts the review-closed single-record smoke as current-scope
  complete for its exact synthetic/local numerical scope.
- Directly approved one exact two-step chained update smoke that reuses the
  single-step helper and verifies ordered value continuity.
- Zero mandatory gates remain before that code; direct implementation is next.
- No code, environment, episode, self-play, model, training/evaluation, real
  data, broad P8 or P9-P12 work was added by this decision.

## 2026-07-18 P8 Policy-Update Smoke Re-review Closure Update

- Updated existing `12AD`; decision: `A. Review can close after blocker fix.`
- Confirmed exception normalization, unchanged API/formula/scope and 58 passing
  tests.
- Next: current-scope acceptance plus one exact executable-task decision.
- No new review document, sibling boundary or broad P8/P9-P12 work.

## 2026-07-18 P8 Numeric-Conversion Blocker Fix Update

- Normalized float-conversion overflow to the approved validation exception.
- Added the exact `10**10000` regression test; all 58 tests pass.
- Next: re-review in existing `12AD`, with no new planning document.
- No formula/API/scope expansion, training, self-play, model or P9-P12 work.

## 2026-07-18 P8 Minimal Policy-Update Smoke Implementation Review Update

- Added `12AD`; decision: `B. Review cannot close because blockers exist.`
- Formula/API/scope checks and 57 approved tests pass.
- An adversarial finite `Real` exposes raw `OverflowError` during float
  conversion; the next task is one exact source/test fix.
- No broad P8, training, self-play, model, real-data or P9-P12 work is approved.

## 2026-07-18 P8 Minimal Policy-Update Smoke Implementation Milestone Update

- Added the exact `12AC`-approved `mjlabai.rl` module and focused unit test.
- Implemented one deterministic single-record terminal/non-terminal tabular
  action-value update with strict numerical and synthetic/local validation.
- Validation passed 11 focused tests, 46 approved regression tests and
  `git diff --check`.
- Next: review this exact implementation, with no sibling boundary.
- This is not an environment, self-play, model, production training/evaluation
  system, strength result, broad P8 entry or P9-P12 work.

## 2026-07-18 P8 Minimal Policy-Update Smoke Approval Milestone Update

- Added `12AC_P8_MINIMAL_SYNTHETIC_LOCAL_POLICY_UPDATE_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`.
- Decision: `Approved for next exact minimal implementation task.`
- Approved one deterministic standard-library single-record tabular action-
  value update and three exact source/test files only.
- Recorded exact P8-E15 human transition authorization for this task.
- Next: implement the exact smoke directly; no additional docs gate.
- No code, tests, fixtures, data, model/artifact use, self-play, production
  training/evaluation, real data, strength claim, broad P8 or P9-P12 work was
  added in this approval task.

## 2026-07-18 P8 Provenance-Manifest Boundary Review Milestone Update

- Added `12AB_P8_MODEL_ARTIFACT_PROVENANCE_MANIFEST_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`.
- Review decision: `A. Review can close.`
- Found no genuine blocker and left `12AA` unchanged.
- Applied the anti-overdocumentation exit: one exact approval decision remains
  before a deterministic CPU-only synthetic/local policy-update smoke.
- Next: decide whether to approve that exact minimal implementation.
- No code, tests, fixtures, data, artifact/model use, training, evaluation,
  self-play/RL/league, real-data work, strength claim or P9-P12 work was added
  or approved.

## 2026-07-15 P8 Model / Artifact Provenance Manifest Boundary Milestone Update

- Added `12AA_P8_MODEL_ARTIFACT_PROVENANCE_MANIFEST_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`.
- Defined three-layer logical/content/manifest identity, authority separation,
  ten unapproved artifact classes, components, derivation and acyclic lineage,
  lifecycle, freeze/thaw/revocation, verification/attestation, compatibility,
  eligibility, reproducibility, candidate fields and PM-E1 through PM-E15.
- Deferred content identity/hash/canonicalization, serialization/storage,
  signature/attestation authority, package composition, retention/revocation
  implementation and third-party/remote artifact use.
- Planning decision: `P8 model / artifact provenance manifest boundary is
  defined before any implementation.`
- Next: review the provenance-manifest boundary, docs-only.
- No P8 entry/implementation, manifest/schema/loader/validator/artifact, model
  loading, training/evaluation/inference, self-play/RL/league, source/real-data
  work, strength evidence or P9-P12 work was added or approved.

## 2026-07-15 P8 Training / Evaluation Model-Use Boundary Review Milestone Update

- Added `12Z_P8_TRAINING_EVALUATION_MODEL_USE_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`.
- Review decision: `A. Review can close.`
- Confirmed mutable/frozen separation, identity/lineage, update/freeze,
  use/leakage, eligibility/failure/reproducibility, TU-E1 through TU-E15 and
  stop-condition boundaries are sufficient for this gate.
- Preserved non-blocking future notes for content identity/attestation, update
  atomicity, freeze finalization/revocation, data-use lineage, recurrent reset,
  eligibility-transition authority and reproducibility verification.
- `12Y` was not modified.
- Next: define the P8 model/artifact provenance-manifest boundary, docs-only.
- No P8 entry/implementation, manifest/schema/loader/artifact, model loading,
  training/evaluation/inference, self-play/RL/league, source/real-data work,
  strength evidence or P9-P12 work was added or approved.

## 2026-07-14 P8 Training / Evaluation Model-Use Boundary Milestone Update

`12Y` defines the P8 training/evaluation model-use boundary before any
implementation. It separates mutable training and frozen evaluation policy
uses; binds artifact/update/freeze/lineage identity; separates training,
validation, checkpoint selection and holdout; and records tuning leakage,
eligibility, failure, reproducibility, ten unapproved candidate use classes,
candidate fields, TU-E1 through TU-E15 and stop conditions.

The next docs-only task is `Review P8 training / evaluation model-use boundary
before any implementation`.

This milestone update does not approve P8 entry/implementation, an
implementation prompt, training data/run, model/checkpoint/weight loading or
creation, training/tuning/evaluation/checkpoint selection, inference,
model-output integration, environment/self-play/RL/league, source/real-data
work, model-strength evidence or P9-P12 entry.

## 2026-07-14 P8 Model-Output Interface Dependency Boundary Review Milestone Update

`12X` reviews the P8 model-output interface dependency boundary in `12W` and
records `A. Review can close.` It confirms scope/non-approval, authority and
identity separation, all ten candidate classes, request/observation/legal-set
binding, candidate action/numeric/status semantics, failure/retry/fallback,
state/batching isolation, reproducibility, evidence boundaries, MO-E1 through
MO-E15 and stop conditions.

Non-blocking future notes cover request/response finalization, action
vocabulary/selection/RNG, timing/latency, fallback identity, numeric semantics,
recurrent-state identity, batching reproducibility and remote privacy/
redaction. `12W` was not modified.

The next docs-only task is `Define P8 training / evaluation model-use boundary
before any implementation`.

This milestone update does not approve P8 entry, P8 implementation, an
implementation prompt, a schema/API/adapter, model/checkpoint/weight loading,
inference/action generation, training/evaluation execution, environment/self-
play/RL/league, source/real-data/remote-model work, model-strength evidence or
P9-P12 entry.

## 2026-07-14 P8 Model-Output Interface Dependency Boundary Milestone Update

`12W` now defines the P8 model-output interface dependency boundary before any
implementation. It separates environment/protocol/interface/model/reward/
evaluation authority; records ten unapproved candidate interface classes;
defines model/policy/artifact identity, request/observation/legal-action
handoff, candidate action/score/value/status, timeout/stale/duplicate/retry/
fallback, recurrent/session/batching/concurrency and reproducibility
boundaries; and records candidate fields, MO-E1 through MO-E15 and stop
conditions.

The next docs-only task is `Review P8 model-output interface dependency
boundary before any implementation`.

This milestone update does not approve P8 entry, P8 implementation, an
implementation prompt, a schema/API/adapter, model/checkpoint/weight loading,
inference/action generation, environment/self-play/RL/training/evaluation/
league, source/real-data/remote-model work, model-strength evidence or P9-P12
entry.

## 2026-07-07 P8 Planning Milestone Update

`12I` now defines P8 scope, P8-E1 through P8-E15 entry criteria, non-entry
conditions, a P8 workstream inventory, risk controls, evidence requirements
and the next docs-only review gate after the reviewed P8-P12 transition-scope
document in `12H`.

This milestone update does not approve P8 entry, P8 implementation,
self-play, reinforcement-learning execution, training, evaluation, league,
source approval, source ingestion, real data, model-output integration,
model-strength evidence or P9-P12 entry.

## 2026-07-07 P8 Scope Review Milestone Update

`12J` now reviews the `12I` P8 scope, entry criteria and first planning task
definition and records `A. Review can close.` The next docs-only task is
`Define P8 risk and evidence taxonomy before any implementation`.

This milestone update does not approve P8 entry, P8 implementation, an
implementation prompt, self-play, reinforcement-learning execution, training,
evaluation, league, source approval, source ingestion, real data,
model-output integration, model-strength evidence or P9-P12 entry.

## 2026-07-07 P8 Risk/Evidence Taxonomy Milestone Update

`12K` now defines the P8 risk and evidence taxonomy before any
implementation. It records R1-R20 risk families, E1-E25 evidence families,
evidence-grade vocabulary, current evidence classification, a P8 workstream
risk/evidence matrix, model-strength / Tenhou / stable-dan / LuckyJ /
promotion boundaries, source / real-data / platform boundaries, self-play / RL
boundaries, stop conditions and candidate next directions.

The next docs-only task is `Review P8 risk and evidence taxonomy before any
implementation`.

This milestone update does not approve P8 entry, P8 implementation, an
implementation prompt, self-play, reinforcement-learning execution, training,
evaluation, league, source approval, source ingestion, real data,
model-output integration, model-strength evidence or P9-P12 entry.

## 2026-07-07 P8 Risk/Evidence Taxonomy Review Milestone Update

`12L` now reviews the `12K` P8 risk and evidence taxonomy and records
`A. Review can close.` The review confirms the scope, Full P7 / P8 recap,
P8 non-approval baseline, R1-R20 risk taxonomy, E1-E25 evidence taxonomy,
evidence-grade vocabulary, current evidence classification, P8 workstream
risk/evidence matrix, model-strength / Tenhou / stable-dan / LuckyJ /
promotion boundaries, source / real-data / platform boundaries, self-play / RL
boundaries, stop conditions and candidate next directions.

The next docs-only task is `Define P8 self-play / reinforcement-learning
dependency map before any implementation`.

This milestone update does not approve P8 entry, P8 implementation, an
implementation prompt, self-play, reinforcement-learning execution, training,
evaluation, league, source approval, source ingestion, real data,
model-output integration, model-strength evidence or P9-P12 entry.

## 2026-07-13 P8 Self-Play / RL Dependency Map Milestone Update

`12M` defines the P8 self-play / reinforcement-learning dependency map before
any implementation. It records D1-D18 dependency families, RD1-RD12 required
dependencies, blocked / deferred / later-stage dependencies, R1-R20 and
E1-E25 linkage, model-output / evaluation / source-real-data boundaries, stop
conditions and candidate next directions.

The next docs-only task is `Review P8 self-play / reinforcement-learning
dependency map before any implementation`.

This milestone update is dependency-map definition evidence only. It does not
approve P8 entry, P8 implementation, an implementation prompt, self-play, RL
execution, training, evaluation, league, source approval/ingestion, real data,
model-output integration, model-strength evidence or P9-P12 entry.

## 2026-07-13 P8 Self-Play / RL Dependency Map Review Milestone Update

`12N` reviews the `12M` P8 self-play / reinforcement-learning dependency map
and records `A. Review can close.` The review confirms the non-approval
baseline, vocabulary, D1-D18, matrix, RD1-RD12, dependency classifications,
R1-R20/E1-E25 linkage, key boundaries, stop conditions and candidate next
directions.

The next docs-only task is `Define P8 self-play protocol boundary before any
implementation`.

This milestone update is dependency-map review evidence only. It does not
approve P8 entry/implementation, self-play, RL execution, training,
evaluation, league, source/real-data work, model-output integration,
model-strength evidence or P9-P12 entry.

## 2026-07-13 P8 Self-Play Protocol Boundary Milestone Update

`12O` defines the P8 self-play protocol boundary before any implementation.
It records protocol vocabulary and classes, participant/artifact identity,
episode lifecycle, information/action boundaries, reproducibility,
termination/abort handling, candidate manifest fields, training/evaluation
separation, downstream dependency boundaries, SP-E1 through SP-E15, stop
conditions and candidate next directions.

The next docs-only task is `Review P8 self-play protocol boundary before any
implementation`.

This milestone update is protocol-boundary definition evidence only. It does
not approve P8 entry/implementation, self-play, RL, training, evaluation,
league, source/real-data work, model-output integration, model-strength
evidence or P9-P12 entry.

## 2026-07-13 P8 Self-Play Protocol Boundary Review Milestone Update

`12P` reviews the `12O` P8 self-play protocol boundary and records
`A. Review can close.` It confirms scope, non-approval baseline, vocabulary,
candidate classes, identity, lifecycle, information/action, reproducibility,
termination, candidate manifest, training/evaluation separation, downstream
boundaries, SP-E1 through SP-E15 and stop conditions.

The review records future notes for scoped P8 runner/environment wording,
cross-episode policy updates, seat/retry selection bias and candidate manifest
refinements. The next docs-only task is `Define P8 RL objective / reward
specification boundary before any implementation`.

This milestone update is protocol-boundary review evidence only. It does not
approve P8 entry/implementation, reward implementation, self-play, RL,
training, evaluation, league, source/real-data work, model-output integration,
strength evidence or P9-P12 entry.

## 2026-07-14 P8 RL Objective / Reward Boundary Milestone Update

`12Q` defines the P8 RL objective / reward specification boundary before any
implementation. It separates raw outcome, reward, objective/loss, training
diagnostics, evaluation metrics and strength evidence; evaluates only
unselected/non-executable candidate families; and records source/timing,
failure/retry, bias, reward-hacking, scaling, credit-assignment, dependency,
OR-E1 through OR-E15 and stop-condition boundaries.

The next docs-only task is `Review P8 RL objective / reward specification
boundary before any implementation`.

This milestone update is boundary-definition evidence only. It does not
approve P8 entry/implementation, reward/loss implementation, RL algorithm
selection, self-play/RL/training/evaluation/league, source/real-data work,
model-output integration, strength evidence or P9-P12 entry.

## 2026-07-14 P8 RL Objective / Reward Boundary Review Milestone Update

`12R` reviews the `12Q` P8 RL objective / reward specification boundary and
records `A. Review can close.` It confirms concept separation, candidate-family
non-selection, source/timing/provenance, failure/retry/bias, anti-hacking,
scaling, credit, algorithm/loss, training/evaluation, evidence, dependency,
OR-E1 through OR-E15 and stop-condition boundaries.

The review records non-blocking future notes for evaluation-only metric
classification, explicit upstream-version linkage, retry lineage and
environment authority. The next docs-only task is `Define P8 environment /
simulator boundary before any implementation`.

This milestone update is boundary-review evidence only. It does not approve
P8 entry/implementation, reward/RL selection or implementation,
environment/simulator/runner implementation, self-play/RL/training/evaluation/
league, source/real-data/model-output work, strength evidence or P9-P12 entry.

## 2026-07-14 P8 Environment / Simulator Boundary Milestone Update

`12S` defines the P8 environment / simulator authority boundary before any
implementation. It separates environment, simulator, participant, protocol,
reward and evaluation authority and defines state, reset, transition,
legality, observation, RNG/seed/seat, terminal/raw outcome, failure/retry/
resource, concurrency/isolation, invariant, version/provenance, manifest and
dependency boundaries.

All candidate environment classes remain unapproved and non-executable.
ENV-E1 through ENV-E15 retain separate review, approval and exact `10_NEXT`
gates. The next docs-only task is `Review P8 environment / simulator boundary
before any implementation`.

This milestone update is boundary-definition evidence only. It does not
approve P8 entry/implementation, environment/simulator/runner implementation,
transition/episode/self-play/RL/training/evaluation/league, source/real-data/
model-output work, strength evidence or P9-P12 entry.

## 2026-07-14 P8 Environment / Simulator Boundary Review Milestone Update

`12T` reviews the `12S` P8 environment / simulator authority boundary and
records `A. Review can close.` It confirms authority separation,
candidate-class non-selection, state/reset/transition/legality/observation/
RNG/seat/outcome/failure/concurrency/invariant/version/manifest/dependency/
evidence boundaries, ENV-E1 through ENV-E15 and stop conditions.

The review preserves non-blocking future notes for simulator conformance,
reset/retry identity, transition atomicity/idempotency, RNG substreams,
concurrent event ordering/partial failure and manifest provenance. `12S` was
not modified. The next docs-only task is `Define P8 raw-outcome and
environment-provenance boundary before any implementation`.

This milestone update is boundary-review evidence only. It does not approve
P8 entry/implementation, a raw-outcome schema, environment/simulator/runner
implementation, transition/episode/self-play/RL/training/evaluation/league,
source/real-data/model-output work, strength evidence or P9-P12 entry.

## 2026-07-14 P8 Raw-Outcome / Environment-Provenance Boundary Milestone Update

`12U` defines the P8 raw-outcome / environment-provenance boundary before any
implementation. It defines immutable authority lineage from protocol and
environment through transition, terminal state and raw outcome; outcome
status/finalization; correction/supersession; retry/duplicate/failure;
completeness/integrity; participant/artifact/RNG/seed/seat/resource
provenance; candidate fields; and raw-outcome separation from reward,
evaluation and evidence use.

All candidate fields remain non-schema, unapproved and non-executable.
RO-E1 through RO-E15 retain separate review, approval and exact `10_NEXT`
gates. The next docs-only task is `Review P8 raw-outcome and
environment-provenance boundary before any implementation`.

This milestone update is boundary-definition evidence only. It does not
approve P8 entry/implementation, a schema/parser/reader/ingestion path,
environment/simulator/runner/outcome implementation, transition/episode/
self-play/RL/training/evaluation/league, source/real-data/model-output work,
strength evidence or P9-P12 entry.

## 2026-07-14 P8 Raw-Outcome / Environment-Provenance Boundary Review Milestone Update

`12V` reviews the `12U` P8 raw-outcome / environment-provenance boundary and
records `A. Review can close.` It confirms authority and attempt lineage,
canonical outcome status, finalization/immutability, correction/supersession,
simulator conformance, retry/duplicate/failure, completeness/integrity,
participant/artifact/RNG/seat/resource provenance, candidate fields,
reward/evaluation/use separation, RO-E1 through RO-E15 and stop conditions.

The review preserves non-blocking future notes for parent-attempt identity,
atomic/idempotent unique finalization, acyclic supersession, payload content
identity, separate finalization/correction authority and privacy/redaction
classification. `12U` was not modified. The next docs-only task is `Define P8
model-output interface dependency boundary before any implementation`.

This milestone update is boundary-review evidence only. It does not approve
P8 entry/implementation, a schema/parser/database, environment/outcome or
model-output implementation, model/checkpoint loading, inference/action
generation, transition/episode/self-play/RL/training/evaluation/league,
source/real-data work, strength evidence or P9-P12 entry.

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
