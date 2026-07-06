# 03BG_FULL_P7_CLOSURE_CRITERIA_AFTER_PARSER_READER_SMOKE_EXTENSION_CURRENT_SCOPE_ACCEPTANCE

## Scope

This document defines full P7 closure criteria after `03BE` accepted the exact
P7 minimal synthetic/local parser-reader smoke extension implementation as
current-scope complete and `03BF` selected closure-criteria definition as the
next full-scope planning step.

This is a docs-only full P7 closure-criteria definition. It is not:

- full P7 closure.
- broader P7 implementation approval.
- production code.
- tests.
- fixtures.
- data files.
- source approval.
- source ingestion.
- parser / reader / ingestion implementation.
- broad file ingestion.
- CLI.
- arbitrary path reading.
- actual feature extraction.
- actual label generation.
- feature tensors.
- labels.
- targets.
- supervised examples.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- training-data approval.
- training-run approval.
- training.
- tuning.
- model architecture / trainer implementation.
- dataloader / optimizer / loss implementation.
- checkpoint / weights / snapshot creation.
- evaluation implementation.
- metric implementation.
- evaluation runner.
- benchmark harness.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- real data.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token handling.
- self-play.
- league.
- P8-P12 entry.

North-star relationship: full P7 closure criteria support the long-term Tenhou
stable-dan `> 10.68` target only by defining what must be true before the
supervised-learning stage can be considered closed. This document is not
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## Current Accepted P7 Current Scope

The currently accepted P7 current-scope items are:

- docs-only supervised-learning readiness / boundary / proposal / review /
  approval / acceptance chain.
- exact minimal synthetic/local supervised feature-label smoke implementation
  accepted in `03Q`.
- exact broader P7 minimal synthetic/local parser-reader smoke implementation
  accepted as current-scope complete after `03AV`.
- exact P7 minimal synthetic/local parser-reader smoke extension
  implementation accepted in `03BE`.
- exact `03BC` test-only blocker fix for top-level `bytes`, top-level
  `bytearray` and top-level `Mapping` rejection.
- validation evidence for those exact scopes.
- direct docs / governance synchronization for those exact scopes.

The accepted implementation surface is synthetic/local only:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

This accepted scope does not approve source approval, real data, source
ingestion, broad parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, training,
evaluation, model-output integration, self-play, league or P8-P12.

## Current Full P7 Open Scope

Full P7 remains open. The following ranges are not complete and remain
unapproved:

- source approval / data rights.
- source ingestion.
- broad parser / reader / ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split / leakage implementation.
- training-data approval.
- training-data construction.
- training-run approval.
- training.
- model architecture / trainer implementation.
- dataloader / optimizer / loss implementation.
- checkpoint / weights / snapshot creation.
- evaluation implementation.
- metric implementation.
- evaluation runner.
- benchmark harness.
- model-output integration.
- model-strength evidence.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token handling.
- self-play.
- league.
- P8-P12.

## Why Current Scope Does Not Close Full P7

Current-scope artifacts are synthetic/local smoke and docs/governance
evidence. They validate guardrails, schema hygiene, narrow in-memory helper
boundaries and non-evidence warnings.

They do not prove:

- source readiness.
- real-data rights or lawful allowed use.
- ingestion correctness.
- broad parser / reader correctness.
- actual feature extraction correctness.
- actual label generation correctness.
- supervised dataset quality.
- split or leakage controls.
- training-data readiness.
- model / trainer readiness.
- evaluation readiness.
- model-output readiness.
- model quality or policy strength.

Therefore current-scope smoke artifacts can support auditability, but they
cannot by themselves close full P7.

## Why Full P7 Cannot Close Now

Full P7 cannot close now because major full-scope workstreams remain
unapproved, blocked or deferred. No source is approved for P7 training or
ingestion, no broad ingestion exists, no actual features or labels are
produced, no supervised dataset or split exists, no training data is approved,
no training run is approved, no model/trainer work exists, no model outputs
exist and no evaluation or model-strength evidence exists.

Closing full P7 now would incorrectly treat synthetic/local smoke guardrails
as complete supervised-learning readiness.

## Why P8-P12 Cannot Start Now

P8-P12 require upstream supervised/data/evaluation evidence that does not
exist yet. Current P7 evidence does not include approved training data, a
trained supervised model, model outputs, evaluation results, self-play
readiness, league readiness, Tenhou ranked evidence, stable-dan ranked-game
evidence or LuckyJ `10.68` comparison evidence.

P8-P12 entry remains blocked until full P7 closure and a separate post-full-P7
transition review define later-stage scope, entry criteria, risks and first
task approval.

## Closure Criteria Vocabulary

| status | meaning |
|---|---|
| pass | The criterion is satisfied for the documented scope, but pass does not imply implementation approval beyond that scope. |
| not pass | The criterion is required for full P7 closure and is not currently satisfied. |
| deferred | The item is known and intentionally delayed; deferred does not mean approved. |
| blocked | The item cannot proceed until a named upstream approval, review or artifact exists. |
| later-stage | The item belongs to a later project phase and must not be used as P7 closure evidence. |
| out-of-scope | The item is outside current full P7 closure criteria and requires a separate stage/task. |
| not applicable to current scope | The item does not apply to the accepted synthetic/local current-scope artifacts. |

Synthetic/local smoke pass is not full P7 pass. Docs-only review pass is not
implementation approval.

## Workstream Closure Criteria Matrix

| workstream | closure criterion | current status | required evidence | current evidence | status | blocker | notes |
|---|---|---|---|---|---|---|---|
| Source approval / data rights | Source posture is explicit and either approved for a named future use or explicitly deferred/blocked. | no source approved | source approval record, rights/allowed-use evidence, storage/privacy notes | `03AA` / `03AB` boundary and review only | not pass | source-specific approval missing | Closure may record not approved only if future closure intentionally excludes real/source data. |
| Source ingestion | Ingestion status is explicit and not overclaimed. | not approved | ingestion approval, exact files, input boundary, validation plan | boundary docs only | not pass | source approval missing | Current parser-reader smoke is not ingestion. |
| Broad parser / reader / ingestion | Broad parser/reader status is explicit and exact approved scope exists if included. | not approved | proposal, review, approval decision, implementation review | synthetic/local smoke only | not pass | no source/ingestion approval | No broad file ingestion, CLI or arbitrary path reading exists. |
| Actual feature extraction | Feature extraction status is explicit and not overclaimed. | not approved | feature schema, leakage controls, implementation/review if included | `03AE` / `03AF` boundary only | not pass | parser/source approval missing | Current smoke emits no feature tensors/examples. |
| Actual label generation | Label generation status is explicit and not overclaimed. | not approved | label taxonomy, public-info policy, provenance, implementation/review if included | boundary docs only | not pass | parser/source approval missing | Current labels are smoke placeholders/guardrails only. |
| Supervised dataset construction | Dataset status is explicit and not overclaimed. | not approved | dataset schema, manifest, provenance, approval/review if included | `03AG` / `03AH` boundary only | not pass | feature/label approval missing | No dataset files, examples or manifests are approved. |
| Split / leakage controls | Split/leakage status is explicit and not overclaimed. | not approved | split policy, leakage tests, review evidence | boundary docs only | not pass | dataset approval missing | Hidden/future info controls are smoke guardrails, not dataset leakage suite. |
| Training-data approval | Training-data status is explicit and separate from dataset construction. | not approved | training-data approval record, source/dataset/leakage evidence | `03AI` / `03AJ` boundary only | not pass | dataset/split evidence missing | No training data is approved. |
| Training-run approval | Training-run status is explicit and separate from training data. | not approved | run approval, command plan, artifact policy | boundary docs only | not pass | training-data approval missing | No trainer commands or artifact creation are approved. |
| Training execution | Training status is explicit and not overclaimed. | not approved / not run | approved run logs, reproducibility metadata, artifact policy | none | not pass | training-run approval missing | No training/tuning was run. |
| Model architecture / trainer | Model/trainer status is explicit. | not approved | model/trainer proposal, approval, tests/review if included | `03AK` / `03AL` boundary only | not pass | training-data/run prerequisites missing | No dataloader, optimizer, loss or trainer implementation exists. |
| Checkpoint / weights / artifacts | Artifact status is explicit. | not approved | artifact policy, approved creation/load path, provenance | none | not pass | model/training approval missing | No checkpoint, weights or snapshot creation/loading is approved. |
| Evaluation implementation | Evaluation status is explicit. | not approved | evaluation protocol, implementation approval, review evidence | `03AM` / `03AN` boundary only | not pass | model-output/eval prerequisites missing | P5 patterns may inform future docs only. |
| Model-output integration | Model-output status is explicit. | blocked | output schema, model artifact policy, evaluation dependency review | none | blocked | no model/trainer/evaluation prerequisites | No model outputs exist or are approved. |
| Model-strength evidence | Strength-evidence status is explicit and conservative. | absent | approved evaluation, sample-size/uncertainty evidence, governance review | none | blocked | no model/evaluation output | No Tenhou, stable-dan or LuckyJ evidence exists. |
| Real Tenhou / real haifu / external logs / platform data | Real/external data status is explicit. | blocked | lawful source approval, privacy/platform/account review, storage policy | none | blocked | source-specific compliance review missing | No real/external/platform data is approved. |
| Governance / risk / evidence / decision records | Governance records are synchronized. | active | handoff, index, next, evidence, risk, decisions, changelog, stage contract, milestones, backlog, technical plan | current docs and this task | pass for criteria definition after sync | none | Must be reviewed separately. |
| Current synthetic/local smoke artifacts | Accepted exact current-scope artifacts are indexed and bounded. | accepted for exact current scope | acceptance docs, exact file list, validation evidence | `03Q`, `03AV`, `03BE`, implementation/tests | pass for current scope only | none | This is not full P7 closure by itself. |
| Self-play / league | Later-stage status is explicit. | later-stage | post-P7/P8-P10 transition reviews | none | later-stage | full P7 not closed | Not P7 closure evidence. |
| P8-P12 transition boundary | Later-stage entry is explicitly blocked. | not approved | full P7 closure, transition review, scope/entry criteria | none | later-stage | full P7 not closed | No P8-P12 task may start now. |

## Required Closure Criteria

Full P7 future closure requires these criteria to be explicitly satisfied or,
where allowed, explicitly deferred/blocked with conservative non-closure
wording:

- C1. Accepted current-scope smoke artifacts are indexed and bounded.
- C2. Source/data-rights posture is explicit.
- C3. Source approval status is either approved with evidence or explicitly
  deferred/blocked.
- C4. Source ingestion status is explicit and not overclaimed.
- C5. Broad parser / reader / ingestion status is explicit and not
  overclaimed.
- C6. Actual feature extraction status is explicit and not overclaimed.
- C7. Actual label generation status is explicit and not overclaimed.
- C8. Supervised dataset construction status is explicit and not overclaimed.
- C9. Split / leakage status is explicit and not overclaimed.
- C10. Training-data approval status is explicit.
- C11. Training-run status is explicit.
- C12. Training execution status is explicit.
- C13. Model architecture / trainer status is explicit.
- C14. Checkpoint / weights / artifact status is explicit.
- C15. Evaluation implementation and model-output status are explicit.
- C16. Model-strength evidence status is explicit and conservatively graded.
- C17. Real-data / platform-data / account-risk status is explicit.
- C18. P8-P12 non-entry status is explicit.
- C19. Governance docs are synchronized.
- C20. Validation commands pass.
- C21. Evidence grade is conservative.
- C22. Non-evidence boundaries are explicit.
- C23. Any deferred/blocked/later-stage item is auditable and not mistaken for
  approval.
- C24. A separate full P7 closure review gate reviews these criteria before
  any final closure decision.

## Exit Readiness Checklist

Before a future full P7 closure review, the project must confirm:

- all accepted current-scope artifacts are listed.
- all full-scope required/deferred/blocked/later-stage items are listed.
- no implicit source approval exists.
- no implicit ingestion approval exists.
- no implicit feature/label approval exists.
- no implicit dataset/training approval exists.
- no implicit evaluation/model-strength claim exists.
- source and real/external data status is explicit.
- training-data and training-run status is explicit.
- model/trainer/artifact status is explicit.
- evaluation/model-output/strength-evidence status is explicit.
- P8-P12 remains blocked unless a separate transition review exists.
- validation commands pass.
- governance docs are synchronized.
- risk register is synchronized.
- decision record is synchronized.
- evidence log is synchronized.
- handoff, docs index, backlog, milestones and technical plan are synchronized.
- no unresolved blocker contradicts closure.

## Required Remaining Items

The following items remain required before full P7 can close, unless a future
review explicitly records a conservative closure decision that excludes them
from full P7 closure scope:

- source/data-rights posture review.
- source approval or explicit deferred/blocked source decision.
- source ingestion status review.
- broad parser / reader / ingestion status review.
- actual feature extraction status review.
- actual label generation status review.
- supervised dataset construction status review.
- split / leakage status review.
- training-data approval status review.
- training-run status review.
- model architecture / trainer status review.
- evaluation / model-output / strength-evidence status review.
- final full P7 handoff / evidence index.
- final full P7 closure review gate.
- post-full-P7 transition review before any later-stage task.

## Deferred Items

Deferred items remain unapproved:

- source-specific approval process.
- any approved-source reader.
- any approved-source feature extractor.
- any approved-source label generator.
- dataset manifest builder.
- split/leakage validator.
- training-data manifest validator.
- model/trainer config validator.
- evaluation evidence envelope validator.
- additional synthetic/local implementation proposal loops.

Deferred does not mean approved.

## Blocked Items

Blocked items include:

- real Tenhou / real haifu / external logs / platform data, blocked until
  source-rights, platform, privacy, storage and account-policy review.
- source ingestion, blocked until source approval.
- broad parser / reader / ingestion, blocked until source/ingestion approval.
- actual feature extraction, blocked until source/parser/feature approval.
- actual label generation, blocked until source/parser/label approval.
- supervised dataset construction, blocked until feature/label approval.
- split/leakage implementation, blocked until dataset schema/split policy.
- training, blocked until training-data and training-run approval.
- evaluation, blocked until model/output/protocol approval.
- model-strength evidence, blocked until approved evaluation with sufficient
  evidence and uncertainty.
- model-output integration, blocked until model/trainer/evaluation
  prerequisites exist.

## Later-Stage / Out-of-Scope Items

Later-stage / out-of-scope for this P7 closure-criteria definition:

- self-play.
- league.
- reinforcement learning.
- P8-P12.
- Tenhou ranked validation.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

These items cannot be used as current full P7 closure evidence and require
separate later transition reviews.

## Evidence Requirements

Future full P7 closure evidence records should include:

- `evidence_id`
- `workstream`
- `status`
- `accepted_artifacts`
- `source_approval_status`
- `ingestion_status`
- `feature_label_status`
- `dataset_status`
- `training_status`
- `model_status`
- `evaluation_status`
- `model_output_status`
- `strength_evidence_status`
- `validation_commands`
- `evidence_grade`
- `risk_register_reference`
- `decision_record_reference`
- `known_exclusions`
- `explicit_non_evidence_warning`

## Non-Closure Evidence

The following are not full P7 closure evidence by themselves:

- synthetic/local smoke alone.
- unit tests alone.
- docs-only review alone.
- parser-reader smoke alone.
- parser-reader smoke extension alone.
- validation pass alone.
- source planning without approval.
- training planning without training data.
- model planning without model implementation/training/evaluation.
- P5 closure evidence.
- P6 closure evidence.
- P8/P9/P10/P11/P12 planning.

## P8-P12 Non-Entry Conditions

Do not enter P8-P12 unless all of the following exist:

- full P7 closure.
- post-full-P7 transition review.
- P8-P12 scope definition.
- entry criteria.
- risk/evidence review.
- first task approval.

Any missing item blocks P8-P12 entry.

## Governance Synchronization Requirements

This task must synchronize:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Planning Decision

```text
Full P7 closure criteria are defined after parser-reader smoke extension
current-scope acceptance.
```

This task does not close full P7 and does not approve broader P7
implementation, source approval, source ingestion, broad parser / reader /
ingestion, actual feature extraction, actual label generation, supervised
dataset construction, split creation, leakage-test implementation,
training-data approval, training-run approval, training, model architecture /
trainer implementation, checkpoint / weights, evaluation implementation,
model-output integration, model-strength evidence, real data, self-play,
league or P8-P12 entry.

## Evidence Grade

```text
Full P7 closure criteria definition evidence only.
```

## Explicit Non-Evidence

This closure-criteria definition is not:

- full P7 closure.
- broader P7 implementation approval.
- source approval.
- source ingestion.
- broad parser / reader / ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- training-data approval.
- training-run approval.
- training.
- model architecture.
- trainer.
- checkpoint.
- weights.
- evaluation implementation.
- metric implementation.
- evaluation runner.
- benchmark harness.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- real data.
- self-play.
- league.
- P8-P12 entry approval.

## First Task Candidate

If no blocker is found, the new first unchecked task in `10_NEXT` should be:

```text
Review full P7 closure criteria after parser-reader smoke extension current-scope acceptance.
```

The task must explicitly remain:

- docs-only review gate.
- not full P7 closure.
- not implementation.
- not source approval.
- not source ingestion.
- not broad parser / reader / ingestion.
- not feature extraction.
- not label generation.
- not dataset construction.
- not training.
- not evaluation.
- not model-output integration.
- not model-strength evidence.
- not real data.
- not self-play.
- not league.
- not P8-P12.
