# 09_CHANGELOG

## 2026-07-01 - v3.11

- Decided whether the broader P7 minimal synthetic/local parser-reader smoke
  implementation can be accepted as current-scope complete.
- Decision:
  `ACCEPTED as current-scope complete.`
- Accepted scope:
  - `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
  - `tests/supervised/test_synthetic_parser_reader_smoke.py`
  - existing supervised smoke schema integration used read-only.
  - existing replay/schema tests used read-only for validation.
- Acceptance reason:
  - implementation strictly follows the exact `03AU` scope.
  - `03AV` records `Review can close`.
  - no real-data leakage, ingestion behavior, feature extraction, label
    generation, dataset construction, training or evaluation behavior was
    found.
  - no scope drift into broad parser / reader / ingestion was found.
  - no unapproved file modification was found.
  - validation passed.
  - no model-strength, evidence or ranking leakage was found.
- New `10_NEXT` first item:
  `Define P7 full scope expansion plan (docs-only, no implementation).`
- This is broader P7 minimal synthetic/local parser-reader smoke
  current-scope acceptance evidence only.
- No production code, tests, fixtures, data files, implementation logic
  changes, source approval, source ingestion, broad parser / reader /
  ingestion, CLI, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture / trainer implementation, evaluation implementation,
  metric implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-07-01 - v3.10

- Reviewed the exact broader P7 minimal synthetic/local parser-reader smoke
  implementation.
- Added:
  - `docs/03_supervised_policy/03AV_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_REVIEW.md`
- Reviewed:
  - `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
  - `tests/supervised/test_synthetic_parser_reader_smoke.py`
  - `03AU`, `03AS`, `03AT` and related governance / support artifacts.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Decide whether broader P7 minimal synthetic/local parser-reader smoke implementation can be accepted as current-scope complete.`
- This is broader P7 minimal synthetic/local parser-reader smoke
  implementation review evidence only.
- No production code, tests, fixtures, data files, implementation logic
  changes, source approval, source ingestion, broad parser / reader /
  ingestion, CLI, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture / trainer implementation, evaluation implementation,
  metric implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.09

- Implemented the exact broader P7 minimal synthetic/local parser-reader smoke
  task approved by `03AU`.
- Added:
  - `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
  - `tests/supervised/test_synthetic_parser_reader_smoke.py`
- The helper accepts only already-loaded in-memory project-authored
  synthetic/local feature-label smoke mappings and delegates guardrail
  validation to `feature_label_schema`.
- The helper rejects path-like inputs, real-data flags, model-output flags,
  source-approval claims, hidden/future information and non-JSON-safe values.
- The returned summary is JSON-safe and intentionally excludes feature
  tensors, labels, targets, supervised examples, datasets, splits, model
  input, model output, evaluation results and model-strength fields.
- New `10_NEXT` first item:
  `Review broader P7 minimal synthetic/local parser-reader smoke implementation.`
- This is broader P7 exact minimal synthetic/local parser-reader smoke
  implementation evidence only.
- No fixture/data file, real data, source approval, source ingestion, broad
  parser / reader / ingestion, CLI, actual feature extraction, actual label
  generation, supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture / trainer implementation, evaluation implementation,
  metric implementation, evaluation runner, benchmark harness, model-output
  integration, self-play, league, P8-P12 work or model-strength evidence was
  added.

## 2026-06-30 - v3.08

- Prepared the approval decision for broader P7 minimal synthetic/local
  parser-reader smoke implementation.
- Added
  `docs/03_supervised_policy/03AU_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`.
- Decision:
  `Approved for next exact minimal implementation task.`
- Approved next task:
  `Implement broader P7 minimal synthetic/local parser-reader smoke only.`
- Approved future files only:
  - `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
  - `tests/supervised/test_synthetic_parser_reader_smoke.py`
- No new fixture or data file is approved by default.
- New `10_NEXT` first item:
  `Implement broader P7 minimal synthetic/local parser-reader smoke only.`
- This is broader P7 minimal synthetic/local parser-reader smoke
  approval-decision evidence only.
- No implementation was executed in this task.
- No broader P7 implementation, source approval, source ingestion, broad
  parser / reader / ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.07

- Reviewed broader P7 minimal implementation proposal before approval
  decision.
- Added
  `docs/03_supervised_policy/03AT_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`.
- Reviewed `03AS` scope, proposal summary, candidate class and current status,
  exact goal, exact non-goals, candidate future exact files, explicitly
  excluded files, allowed / forbidden inputs, allowed / forbidden outputs,
  dependency status, candidate validation commands, rollback plan, stop
  conditions, risk controls, evidence requirements, approval separation,
  current proposal decision, first task candidate, planning decision, evidence
  grade and governance synchronization.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Prepare approval decision for broader P7 minimal synthetic/local parser-reader smoke implementation.`
- This is broader P7 minimal implementation proposal review evidence only.
- No minimal implementation proposal was approved.
- No broader P7 implementation, production code, tests, fixtures, data files,
  source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.06

- Drafted broader P7 minimal implementation proposal for review after
  proposal-boundary review.
- Added
  `docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`.
- Selected `Project-authored synthetic/local parser-reader smoke proposal` as
  the most conservative proposal-boundary-eligible candidate.
- Recorded exact scope, proposal summary, candidate class, current status,
  exact goal, exact non-goals, candidate future exact files, explicitly
  excluded files, allowed / forbidden inputs, allowed / forbidden outputs,
  dependency status, candidate future validation commands, rollback plan, stop
  conditions, risk controls, evidence requirements, approval separation,
  current proposal decision, first task candidate, planning decision, evidence
  grade and explicit non-evidence warnings.
- Current proposal decision:
  `The proposal is drafted for review, but not approved.`
- New `10_NEXT` first item:
  `Review broader P7 minimal implementation proposal before approval decision.`
- This is broader P7 minimal implementation proposal draft evidence only.
- No minimal implementation proposal was approved.
- No broader P7 implementation, production code, tests, fixtures, data files,
  source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.05

- Reviewed broader P7 minimal implementation proposal boundary after readiness
  checklist review.
- Added
  `docs/03_supervised_policy/03AR_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW_AFTER_READINESS_CHECKLIST_REVIEW.md`.
- Confirmed that `03AQ` scope, purpose, proposal lifecycle vocabulary,
  candidate proposal classes, minimal proposal required sections, exact-scope
  requirements, forbidden proposal scope, approval-decision separation,
  approval prerequisites, stop conditions, risk controls, evidence
  requirements, current proposal-boundary decision, first task candidate,
  planning decision, evidence grade and governance synchronization are
  sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Draft broader P7 minimal implementation proposal for review after proposal-boundary review.`
- This is broader P7 minimal implementation proposal-boundary review evidence
  only.
- No minimal implementation proposal was approved.
- No broader P7 implementation, production code, tests, fixtures, data files,
  source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.04

- Defined broader P7 minimal implementation proposal boundary after readiness
  checklist review.
- Added
  `docs/03_supervised_policy/03AQ_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_AFTER_READINESS_CHECKLIST_REVIEW.md`.
- Recorded proposal lifecycle vocabulary, candidate proposal classes, minimal
  proposal required sections, exact-scope requirements, forbidden proposal
  scope, future approval-decision separation, approval prerequisites, stop
  conditions, risk controls, evidence requirements, current proposal-boundary
  decision, first task candidate, planning decision and evidence grade.
- Current proposal-boundary decision:
  `Broader P7 minimal implementation proposal boundary is defined, but no proposal is approved and no broader P7 implementation is approved.`
- New `10_NEXT` first item:
  `Review broader P7 minimal implementation proposal boundary after readiness checklist review.`
- This is broader P7 minimal implementation proposal-boundary definition
  evidence only.
- No minimal implementation proposal was approved.
- No broader P7 implementation, production code, tests, fixtures, data files,
  source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.03

- Reviewed broader P7 implementation readiness checklist after boundary-chain
  review.
- Added
  `docs/03_supervised_policy/03AP_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW_AFTER_BOUNDARY_CHAIN_REVIEW.md`.
- Confirmed that `03AO` scope, purpose, boundary-chain coverage, readiness
  status vocabulary, required upstream artifact checklist, candidate
  implementation class matrix, future implementation proposal fields, future
  approval-decision fields, stop conditions, risk controls, evidence
  requirements, readiness decision vocabulary, current readiness decision,
  first task candidate, planning decision, governance synchronization and
  evidence grade are sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 minimal implementation proposal boundary after readiness checklist review.`
- This is broader P7 implementation readiness checklist review evidence only.
- No minimal implementation proposal was approved.
- No broader P7 implementation, production code, tests, fixtures, data files,
  source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.02

- Defined broader P7 implementation readiness checklist after boundary-chain
  review.
- Added
  `docs/03_supervised_policy/03AO_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_AFTER_BOUNDARY_CHAIN_REVIEW.md`.
- Summarized the reviewed broader P7 boundary chain from `03Y` through `03AN`
  and recorded readiness status vocabulary, required upstream artifacts,
  candidate implementation class readiness matrix, future implementation
  proposal fields, future approval-decision fields, stop conditions, risk
  controls, evidence requirements, current readiness decision, first task
  candidate, planning decision and evidence grade.
- Current readiness decision:
  `Boundary chain is reviewed enough to define an implementation readiness checklist, but no broader P7 implementation class is approved.`
- New `10_NEXT` first item:
  `Review broader P7 implementation readiness checklist after boundary-chain review.`
- This is broader P7 implementation readiness checklist definition evidence
  only.
- No broader P7 implementation, production code, tests, fixtures, data files,
  source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v3.01

- Reviewed broader P7 evaluation dependency and model-strength evidence
  boundary before implementation.
- Added
  `docs/03_supervised_policy/03AN_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AM` scope, purpose, current no-strength-evidence status,
  concept definitions, dependency map, evaluation dependency boundary,
  model-strength evidence boundary, Tenhou / stable-dan / LuckyJ evidence
  boundary, future evidence-record fields, candidate evaluation / evidence
  classes, allowed future boundary, forbidden scope, stop conditions, risk
  controls, evidence requirements, first task candidate, planning decision,
  evidence grade and governance synchronization are sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 implementation readiness checklist after boundary-chain review.`
- This is broader P7 evaluation dependency and model-strength evidence
  boundary review evidence only.
- No broader P7 implementation, evaluation implementation, metric
  implementation, evaluation runner, benchmark harness, model-output
  integration, model-strength evidence, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison, candidate-promotion
  evidence, source approval, source ingestion, parser / reader / ingestion
  implementation, actual feature extraction, actual label generation,
  supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training-run approval, training,
  model architecture implementation, trainer implementation, dataloader,
  optimizer, loss, checkpoint, weights, production code, tests, fixtures, data
  files, real Tenhou, real haifu, external logs, platform data, self-play,
  league or P8-P12 work was added.

## 2026-06-30 - v3.00

- Defined broader P7 evaluation dependency and model-strength evidence
  boundary before implementation.
- Added
  `docs/03_supervised_policy/03AM_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded current no-strength-evidence status, evaluation and evidence
  vocabulary, dependency order, evaluation dependency boundary,
  model-strength evidence boundary, Tenhou / stable-dan / LuckyJ evidence
  boundary, future evidence-record fields, candidate evidence classes, allowed
  future boundary, forbidden scope, stop conditions, risk controls, evidence
  requirements, first task candidate, planning decision and evidence grade.
- New `10_NEXT` first item:
  `Review broader P7 evaluation dependency and model-strength evidence boundary before implementation.`
- This is broader P7 evaluation dependency and model-strength evidence
  boundary definition evidence only.
- No evaluation implementation, metric implementation, evaluation runner,
  benchmark harness, model-output integration, model-strength evidence,
  Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68`
  comparison, candidate-promotion evidence, source approval, source
  ingestion, parser / reader / ingestion implementation, actual feature
  extraction, actual label generation, supervised dataset construction,
  training-data approval, training-run approval, training, model architecture
  implementation, trainer implementation, dataloader, optimizer, loss,
  checkpoint, weights, production code, tests, fixtures, data files, real
  Tenhou, real haifu, external logs, platform data, self-play, league or
  P8-P12 work was added.

## 2026-06-30 - v2.99

- Reviewed broader P7 model architecture and trainer planning boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AL_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AK` scope, purpose, current no-model / no-trainer status,
  concept definitions, dependency map, model architecture planning boundary,
  trainer planning boundary, future approval record fields, candidate model /
  trainer classes, allowed future boundary, forbidden scope, stop conditions,
  risk controls, evidence requirements, first task candidate, planning
  decision, evidence grade and governance synchronization are sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 evaluation dependency and model-strength evidence boundary before implementation.`
- This is broader P7 model architecture and trainer planning boundary review
  evidence only.
- No model architecture, model config, encoder, policy head, value head,
  auxiliary head, decision head, dataloader, optimizer, loss, trainer,
  training loop, checkpoint, weights, snapshot, model artifact, training-data
  approval, training-data construction, training-run approval, training,
  source approval, source ingestion, parser / reader / ingestion
  implementation, feature extraction, label generation, supervised dataset
  construction, split creation, leakage-test implementation, evaluation
  implementation, production code, tests, fixtures, data files, real Tenhou,
  real haifu, external logs, platform data, model-output integration,
  self-play, league, P8-P12 work or model-strength claim was added.

## 2026-06-29 - v2.98

- Defined broader P7 model architecture and trainer planning boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AK_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded current no-model / no-trainer / no-training status, concept
  definitions, dependency order, model architecture planning boundary, trainer
  planning boundary, future approval-record fields, candidate model / trainer
  classes, allowed and forbidden future scope, stop conditions, risk controls,
  evidence requirements, first task candidate, planning decision and evidence
  grade.
- New `10_NEXT` first item:
  `Review broader P7 model architecture and trainer planning boundary before implementation.`
- This is broader P7 model architecture and trainer planning boundary
  definition evidence only.
- No model architecture, model config, encoder, policy head, value head,
  auxiliary head, decision head, dataloader, optimizer, loss, trainer,
  training loop, checkpoint, weights, snapshot, model artifact, training-data
  approval, training-data construction, training-run approval, training,
  source approval, source ingestion, parser / reader / ingestion
  implementation, feature extraction, label generation, supervised dataset
  construction, split creation, leakage-test implementation, production code,
  tests, fixtures, data files, real Tenhou, real haifu, external logs,
  platform data, model-output integration, self-play, league, P8-P12 work or
  model-strength claim was added.

## 2026-06-29 - v2.97

- Reviewed broader P7 training-data approval and training-run boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AJ_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AI` scope, purpose, current no-training-data /
  no-training-run status, concept definitions, dependency order,
  training-data approval boundary, training-run boundary, future approval
  record fields, candidate classes, allowed future boundary, forbidden scope,
  stop conditions, risk controls, evidence requirements, first task candidate,
  planning decision, evidence grade and governance synchronization are
  sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 model architecture and trainer planning boundary before implementation.`
- This is broader P7 training-data approval and training-run boundary review
  evidence only.
- No training data was approved or constructed. No training run was approved,
  implemented or executed. No model architecture, trainer, dataloader,
  optimizer, loss, checkpoint, weights, source approval, source ingestion,
  parser / reader / ingestion implementation, feature extraction, label
  generation, supervised dataset construction, split creation, leakage-test
  implementation, production code, implementation logic, tests, fixtures, data
  files, real Tenhou, real haifu, external logs, platform data, model-output
  integration, self-play, league, P8-P12 work or model-strength claim was
  added.

## 2026-06-29 - v2.96

- Defined broader P7 training-data approval and training-run boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AI_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded training-data approval vocabulary, training-run vocabulary,
  dependency order, current no-training-data / no-training-run status, approval
  prerequisites, future approval-record fields, candidate classes, allowed and
  forbidden future boundary, stop conditions, risk controls, evidence
  requirements, first task candidate, planning decision and evidence grade.
- New `10_NEXT` first item:
  `Review broader P7 training-data approval and training-run boundary before implementation.`
- This is broader P7 training-data approval and training-run boundary
  definition evidence only.
- No training data was approved or constructed. No training run was approved,
  implemented or executed. No source approval, source ingestion, parser /
  reader / ingestion implementation, feature extraction, label generation,
  supervised dataset construction, split creation, leakage-test implementation,
  model architecture, trainer, checkpoint, weights, production code, tests,
  fixtures, data files, real Tenhou, real haifu, external logs, platform data,
  model-output integration, self-play, league, P8-P12 work or model-strength
  claim was added.

## 2026-06-28 - v2.95

- Reviewed broader P7 supervised dataset construction, split and leakage
  boundary before implementation.
- Added
  `docs/03_supervised_policy/03AH_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AG` scope, non-approval wording, purpose, current
  no-dataset / no-split / no-leakage status, concept definitions, dependency
  map, dataset construction boundary, split boundary, leakage boundary, future
  approval-record fields, candidate classes, allowed future boundary,
  forbidden scope, stop conditions, risk controls, evidence requirements,
  first task candidate, planning decision, evidence grade and governance
  synchronization are sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 training-data approval and training-run boundary before implementation.`
- This is broader P7 supervised dataset construction, split and leakage
  boundary review evidence only.
- No supervised dataset construction, split creation, leakage-test
  implementation, training-data construction, training-data approval,
  training-run approval, training, source approval, source ingestion, parser /
  reader / ingestion implementation, production code, implementation logic,
  tests, fixtures, data files, actual feature extraction, actual label
  generation, feature tensors, labels, targets, examples, model architecture,
  trainer, model-output integration, real Tenhou, real haifu, external logs,
  platform data, self-play, league, P8-P12 work or model-strength claim was
  added.

## 2026-06-28 - v2.94

- Defined broader P7 supervised dataset construction, split and leakage
  boundary before implementation.
- Added
  `docs/03_supervised_policy/03AG_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded current no-dataset / no-split / no-leakage-implementation status,
  concept definitions, dependency order, dataset construction boundary, split
  boundary, leakage boundary, future approval-record fields, candidate dataset
  / split / leakage classes, allowed future implementation boundary, forbidden
  scope, stop conditions, risk controls, evidence requirements, first task
  candidate, planning decision and evidence grade.
- New `10_NEXT` first item:
  `Review broader P7 supervised dataset construction, split and leakage boundary before implementation.`
- This is broader P7 supervised dataset construction, split and leakage
  boundary definition evidence only.
- No supervised dataset construction, split creation, leakage-test
  implementation, training-data approval, training, source approval, source
  ingestion, parser / reader / ingestion implementation, production code,
  implementation logic, tests, fixtures, data files, actual feature
  extraction, actual label generation, feature tensors, labels, targets,
  examples, model architecture, trainer, model-output integration, real
  Tenhou, real haifu, external logs, platform data, self-play, league,
  P8-P12 work or model-strength claim was added.

## 2026-06-28 - v2.93

- Reviewed broader P7 actual feature extraction and label generation boundary
  before implementation.
- Added
  `docs/03_supervised_policy/03AF_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AE` scope, purpose, current feature / label status,
  concept definitions, dependency map, parser / reader / ingestion separation,
  synthetic/local smoke boundary, candidate feature families, candidate label
  families, feature rules, label rules, approval-record fields, allowed future
  boundary, forbidden scope, stop conditions, risk controls, evidence
  requirements, first task candidate, planning decision, evidence grade and
  governance synchronization are sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 supervised dataset construction, split and leakage boundary before implementation.`
- This is broader P7 actual feature extraction and label generation boundary
  review evidence only.
- No source approval, training-data approval, source ingestion, parser /
  reader / ingestion implementation or approval, broad file ingestion, CLI,
  production code, implementation logic, tests, fixtures, data files, actual
  feature extraction, actual label generation, feature tensors, labels,
  targets, examples, splits, supervised dataset construction,
  leakage-test implementation, training, model architecture, trainer,
  model-output integration, real Tenhou, real haifu, external logs, platform
  data, self-play, league, P8-P12 work or model-strength claim was added.

## 2026-06-28 - v2.92

- Defined broader P7 actual feature extraction and label generation boundary
  before implementation.
- Added
  `docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded feature / label vocabulary, current feature / label status,
  dependency order, parser / reader / ingestion separation, synthetic/local
  smoke non-training boundary, candidate feature families, candidate label
  families, feature boundary rules, label boundary rules, future approval
  fields, allowed / forbidden scope, stop conditions, risk controls, evidence
  requirements, first task candidate, planning decision and evidence grade.
- New `10_NEXT` first item:
  `Review broader P7 actual feature extraction and label generation boundary before implementation.`
- This is broader P7 actual feature extraction and label generation boundary
  definition evidence only.
- No source approval, training-data approval, source ingestion, parser /
  reader / ingestion implementation or approval, broad file ingestion, CLI,
  production code, implementation logic, tests, fixtures, data files, actual
  feature extraction, actual label generation, feature tensors, labels,
  targets, examples, splits, supervised dataset construction, training, model
  architecture, trainer, model-output integration, real Tenhou, real haifu,
  external logs, platform data, self-play, league, P8-P12 work or
  model-strength claim was added.

## 2026-06-28 - v2.91

- Reviewed broader P7 parser, reader and ingestion boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AC` scope, purpose, current parser / reader / ingestion
  status, concept definitions, dependency map, candidate classes, future
  approval fields, allowed / forbidden scope, stop conditions, risk controls,
  evidence requirements, first task candidate, planning decision, evidence
  grade and governance synchronization are sufficient.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 actual feature extraction and label generation boundary before implementation.`
- This is broader P7 parser, reader and ingestion boundary review evidence
  only.
- No parser approval, reader approval, ingestion approval, source ingestion
  approval, source approval, training-data approval, broad file ingestion, CLI,
  production code, implementation logic, tests, fixtures, data files, actual
  feature extraction, actual label generation, supervised dataset
  construction, training, model architecture, trainer, model-output
  integration, real Tenhou, real haifu, external logs, platform data,
  self-play, league, P8-P12 work or model-strength claim was added.

## 2026-06-26 - v2.90

- Defined broader P7 parser, reader and ingestion boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded scope, purpose, current parser / reader / ingestion status,
  concept definitions, boundary dependency map, future candidate classes,
  future approval-record fields, allowed future implementation boundary,
  forbidden parser / reader / ingestion scope, stop conditions, risk controls,
  evidence requirements, first task candidate, planning decision and evidence
  grade.
- New `10_NEXT` first item:
  `Review broader P7 parser, reader and ingestion boundary before implementation.`
- This is broader P7 parser, reader and ingestion boundary definition evidence
  only.
- No parser approval, reader approval, ingestion approval, source ingestion
  approval, source approval, training-data approval, broad file ingestion, CLI,
  production code, implementation logic, tests, fixtures, data files, actual
  feature extraction, actual label generation, supervised dataset construction,
  training, model architecture, trainer, model-output integration, real
  Tenhou, real haifu, external logs, platform data, self-play, league,
  P8-P12 work or model-strength claim was added.

## 2026-06-25 - v2.89

- Reviewed broader P7 data/source readiness and source approval boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03AA` scope, purpose, current source status, source category
  inventory, readiness / approval vocabulary, source-specific approval-record
  requirements, concept separation, parser / reader / ingestion dependency,
  feature / label dependency, risk controls, evidence requirements, first task
  candidate, planning decision, governance synchronization and evidence grade
  are sufficient for the current review gate.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 parser, reader and ingestion boundary before implementation.`
- This is broader P7 data/source readiness and source-approval boundary review
  evidence only.
- No source approval, training-data approval, source ingestion approval,
  parser / reader / ingestion implementation or approval, broad file ingestion,
  CLI, production code, implementation logic, tests, fixtures, data files,
  actual feature extraction, actual label generation, supervised dataset
  construction, training, model architecture, trainer, model-output
  integration, real Tenhou, real haifu, external logs, platform data,
  self-play, league, P8-P12 work or model-strength claim was added.

## 2026-06-25 - v2.88

- Defined broader P7 data/source readiness and source approval boundary before
  implementation.
- Added
  `docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- Recorded current source status, source category inventory, readiness /
  approval vocabulary, source-specific approval record requirements, source
  approval vs source ingestion vs training approval distinctions, parser /
  reader / ingestion dependency boundary, feature / label dependency boundary,
  smoke fixture non-training-source boundary, risk controls, evidence
  requirements, first task candidate, planning decision and evidence grade.
- Confirmed that no source is approved for P7 training, source ingestion,
  actual feature extraction or actual label generation.
- New `10_NEXT` first item:
  `Review broader P7 data/source readiness and source approval boundary before implementation.`
- This is broader P7 data/source readiness and source-approval boundary
  definition evidence only.
- No source approval, training-data approval, source ingestion, production
  code, implementation logic, tests, fixtures, data files, parser, dataset
  reader, ingestion, actual feature extraction, actual label generation,
  supervised dataset construction, training, model architecture, trainer,
  model-output integration, CLI, real Tenhou, real haifu, external logs,
  platform data, self-play, league, P8-P12 work or model-strength claim was
  added.

## 2026-06-25 - v2.87

- Reviewed broader P7 scope, entry criteria and first task before
  implementation.
- Added
  `docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`.
- Confirmed that `03Y` scope, current context, allowed docs-only scope,
  forbidden scope, broader entry criteria, implementation entry criteria,
  required upstream artifacts, blocked / deferred / later-stage / out-of-scope
  classifications, first task candidate, no-implementation reasoning,
  no-training reasoning, P8-P12 non-entry reasoning, planning decision and
  evidence grade are sufficient for the current review gate.
- Review decision:
  `Review can close.`
- Full P7 remains open.
- New `10_NEXT` first item:
  `Define broader P7 data/source readiness and source approval boundary before implementation.`
- This is broader P7 scope / entry criteria / first-task review evidence only.
- No production code, implementation logic, tests, fixtures, data files,
  source approval, source ingestion, parser, dataset reader, ingestion, actual
  feature extraction, actual label generation, supervised dataset
  construction, training, model architecture, trainer, model-output
  integration, CLI, real Tenhou, real haifu, external logs, platform data,
  self-play, league, P8-P12 work or model-strength claim was added.

## 2026-06-25 - v2.86

- Defined broader P7 scope, entry criteria and first task before
  implementation.
- Added
  `docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`.
- Recorded broader P7 purpose, current context, allowed docs-only scope,
  forbidden scope, implementation entry criteria, required upstream artifacts,
  blocked / deferred / later-stage / out-of-scope items, first task candidate,
  reasons not to start broader implementation, reasons not to train, reasons
  not to enter P8-P12, planning decision and evidence grade.
- Confirmed that P7 current scope is closed only for exact current scope and
  full P7 remains open.
- New `10_NEXT` first item:
  `Review broader P7 scope, entry criteria and first task before implementation.`
- This is broader P7 scope / entry criteria / first-task definition evidence
  only.
- No production code, implementation logic, tests, fixtures, data files,
  parser, dataset reader, ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, training, model architecture,
  trainer, model-output integration, CLI, real Tenhou, real haifu, external
  logs, platform data, self-play, league, P8-P12 work or model-strength claim
  was added.

## 2026-06-25 - v2.85

- Reviewed the full P7 closure roadmap and remaining scope inventory after
  current-scope closure.
- Added
  `docs/03_supervised_policy/03X_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW_AFTER_CURRENT_SCOPE_CLOSURE.md`.
- Confirmed that `03W` scope is correct and does not close full P7 or approve
  broader P7 implementation.
- Confirmed that P7 current scope is closed only for the exact docs-only
  readiness chain plus accepted minimal synthetic/local feature-label smoke
  implementation.
- Confirmed that full P7 remains open.
- Confirmed that the `03W` remaining-scope inventory covers required,
  deferred, blocked, later-stage and out-of-scope items with safe
  classifications.
- Confirmed that the `03W` roadmap is conservative, docs-first and does not
  authorize direct implementation.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define broader P7 scope, entry criteria and first task before implementation.`
- This is full P7 closure roadmap and remaining scope inventory review
  evidence only.
- No production code, implementation logic, tests, fixtures, data files,
  parser, dataset reader, ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, training, model architecture,
  trainer, model-output integration, CLI, real Tenhou, real haifu, external
  logs, platform data, self-play, league, P8-P12 work or model-strength claim
  was added.

## 2026-06-12 - v2.84

- Defined the full P7 closure roadmap and remaining scope inventory after
  current-scope closure.
- Added
  `docs/03_supervised_policy/03W_FULL_P7_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_AFTER_CURRENT_SCOPE_CLOSURE.md`.
- Recorded the exact P7 current-scope closure boundary.
- Classified full-P7 remaining items as required, deferred, blocked,
  later-stage or out of scope.
- Defined a conservative docs-first roadmap toward full P7 closure.
- Confirmed that full P7 remains open.
- Confirmed that broader P7 implementation, training, source ingestion,
  parser / reader / ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, model architecture / trainer,
  real data, model-output integration, self-play, league and P8-P12 remain
  unapproved.
- New `10_NEXT` first item:
  `Review full P7 closure roadmap and remaining scope inventory after current-scope closure.`
- This is full P7 closure roadmap and remaining scope inventory definition
  evidence only.
- No production code, implementation logic, tests, fixtures, data files,
  parser, dataset reader, ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, training, model architecture,
  trainer, model-output integration, CLI, real Tenhou, real haifu, external
  logs, platform data, self-play, league, P8-P12 work or model-strength claim
  was added.

## 2026-06-12 - v2.83

- Ran the post-current-scope P7 transition review before defining any broader
  P7 implementation or P8 task.
- Added `docs/12_technical_plan/12E_POST_CURRENT_SCOPE_P7_TRANSITION_REVIEW.md`.
- Confirmed that P7 current scope is closed only for the exact docs-only
  readiness chain plus accepted minimal synthetic/local supervised
  feature-label smoke implementation.
- Confirmed that full P7 remains open.
- Confirmed that broader P7 implementation, training, training data source
  approval, source ingestion, parser / reader / ingestion, actual feature
  extraction, actual label generation, supervised dataset construction, model
  architecture / trainer, real data, model-output integration, self-play,
  league and P8-P12 remain unapproved.
- Reviewed candidate next directions and selected:
  `Define full P7 closure roadmap and remaining scope inventory after current-scope closure.`
- This is post-current-scope P7 transition review evidence only.
- No production code, implementation logic, tests, fixtures, data files,
  parser, dataset reader, ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, training, model architecture,
  trainer, model-output integration, CLI, real Tenhou, real haifu, external
  logs, platform data, self-play, league, P8-P12 work or model-strength claim
  was added.

## 2026-06-12 - v2.82

- Ran the final P7 current-scope closure review gate.
- Added `docs/03_supervised_policy/03V_FINAL_P7_CURRENT_SCOPE_CLOSURE_REVIEW.md`.
- Reviewed the full `03E`-`03U` P7 current-scope chain, accepted minimal
  synthetic/local feature-label smoke implementation artifacts, P6/P5 context
  and governance synchronization.
- Confirmed C1-C26 final status: all pass for current-scope closure.
- Closure decision:
  `P7 current scope can close.`
- Closed scope is exact and narrow: docs-only supervised-learning readiness
  chain plus accepted minimal synthetic/local supervised feature-label smoke
  implementation.
- New `10_NEXT` first item:
  `Run post-current-scope P7 transition review before defining any broader P7 implementation or P8 task.`
- This is P7 final current-scope closure review evidence only.
- Full P7 is not closed.
- Broad P7 implementation, training, source ingestion, parser / reader /
  ingestion, actual feature extraction, actual label generation, supervised
  dataset construction, model architecture, trainer, model-output integration,
  real data, CLI, self-play, league and P8-P12 remain unapproved.
- No production code, implementation logic, tests, fixtures, data files, replay
  schema code, parser, dataset reader, ingestion, actual feature extraction,
  actual label generation, supervised dataset construction, training, tuning,
  self-play, league, runner behavior, model architecture, trainer, dataloader,
  optimizer, loss, checkpoint, weights, model-output integration, CLI, broad
  file ingestion, real Tenhou, real haifu, external logs, platform data,
  third-party binary call, latency measurement, fixed-position exact-match,
  metric implementation, registry code change, promotion criteria change,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 - v2.81

- Finalized P7 current-scope handoff and evidence index after closure
  criteria review.
- Added
  `docs/03_supervised_policy/03U_P7_CURRENT_SCOPE_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`.
- Recorded a finalization-ready P7 current-scope handoff summary.
- Built an evidence index covering `03E`-`03U`, accepted minimal
  synthetic/local feature-label smoke artifacts, P6/P5 context and governance
  docs.
- Confirmed evidence grade consistency and found no separate risk/evidence
  consistency blocker before final current-scope closure review.
- New `10_NEXT` first item:
  `Run final P7 current-scope closure review gate.`
- This is P7 current-scope handoff and evidence-index finalization evidence
  only.
- P7 current scope is not closed by this finalization.
- Broad P7 implementation, training, source ingestion, parser / reader /
  ingestion, actual feature extraction, actual label generation, supervised
  dataset construction, model architecture, trainer, model-output integration,
  real data, CLI, self-play, league and P8-P12 remain unapproved.
- No production code, implementation logic, tests, fixtures, data files, replay
  schema code, parser, dataset reader, ingestion, actual feature extraction,
  actual label generation, supervised dataset construction, training, tuning,
  self-play, league, runner behavior, model architecture, trainer, dataloader,
  optimizer, loss, checkpoint, weights, model-output integration, CLI, broad
  file ingestion, real Tenhou, real haifu, external logs, platform data,
  third-party binary call, latency measurement, fixed-position exact-match,
  metric implementation, registry code change, promotion criteria change,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 - v2.80

- Reviewed P7 current-scope closure criteria after minimal synthetic
  feature-label smoke acceptance.
- Added
  `docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
- Review decision:
  `Review can close.`
- Confirmed that `03S` scope, accepted current-scope inventory, C1-C26
  closure criteria, exit readiness checklist, required remaining
  docs/review/closure items, deferred / blocked / not accepted classifications,
  P8-P12 non-entry conditions, validation commands and governance
  synchronization are sufficient, conservative and auditable.
- New `10_NEXT` first item:
  `Finalize P7 current-scope handoff and evidence index after closure criteria review.`
- This is P7 current-scope closure criteria review evidence only.
- P7 current scope is not closed by this review.
- Broad P7 implementation, training, source ingestion, parser / reader /
  ingestion, actual feature extraction, actual label generation, supervised
  dataset construction, model architecture, trainer, model-output integration,
  real data, CLI, self-play, league and P8-P12 remain unapproved.
- No production code, implementation logic, tests, fixtures, data files, replay
  schema code, parser, dataset reader, ingestion, actual feature extraction,
  actual label generation, supervised dataset construction, training, tuning,
  self-play, league, runner behavior, model architecture, trainer, dataloader,
  optimizer, loss, checkpoint, weights, model-output integration, CLI, broad
  file ingestion, real Tenhou, real haifu, external logs, platform data,
  third-party binary call, latency measurement, fixed-position exact-match,
  metric implementation, registry code change, promotion criteria change,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 - v2.79

- Defined P7 current-scope closure criteria after minimal synthetic
  feature-label smoke acceptance.
- Added
  `docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
- Recorded accepted current-scope P7 inventory, C1-C26 closure criteria, exit
  readiness checklist, required remaining docs/review/closure items, deferred /
  blocked / not accepted items, P8-P12 non-entry conditions, validation
  commands, planning decision, next task recommendation and evidence grade.
- New `10_NEXT` first item:
  `Review P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.`
- This is P7 current-scope closure criteria definition evidence only.
- P7 current scope is not closed by this task.
- Broad P7 implementation, training, source ingestion, parser / reader /
  ingestion, actual feature extraction, actual label generation, supervised
  dataset construction, model architecture, trainer, model-output integration,
  real data, CLI, self-play, league and P8-P12 remain unapproved.
- No production code, implementation logic, tests, fixtures, data files, replay
  schema code, parser, dataset reader, ingestion, actual feature extraction,
  actual label generation, supervised dataset construction, training, tuning,
  self-play, league, runner behavior, model architecture, trainer, dataloader,
  optimizer, loss, checkpoint, weights, model-output integration, CLI, broad
  file ingestion, real Tenhou, real haifu, external logs, platform data,
  third-party binary call, latency measurement, fixed-position exact-match,
  metric implementation, registry code change, promotion criteria change,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 - v2.78

- Defined the next P7 current-scope supervised-learning task after minimal
  synthetic feature-label smoke acceptance.
- Added
  `docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
- Evaluated candidate next tasks:
  - current-scope closure criteria.
  - another readiness boundary.
  - another minimal implementation proposal.
  - blocker / transition review.
  - deferred human / Web ChatGPT decision.
- Recommended next task:
  `Define P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.`
- Rationale:
  P7 docs-only readiness chain plus one exact minimal synthetic/local smoke
  implementation has been accepted, so the next safe step is to define
  current-scope closure criteria and avoid endless readiness / schema churn.
- New `10_NEXT` first item:
  `Define P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.`
- This is P7 next current-scope supervised-learning task definition evidence
  only.
- No production code, implementation logic, tests, fixtures, data files,
  replay schema code, parser, dataset reader, ingestion, actual feature
  extraction, actual label generation, supervised dataset construction,
  training, tuning, self-play, league, runner behavior, model architecture,
  trainer, dataloader, optimizer, loss, checkpoint, weights, model-output
  integration, CLI, broad file ingestion, real Tenhou, real haifu, external
  logs, platform data, third-party binary call, latency measurement,
  fixed-position exact-match, metric implementation, registry code change,
  promotion criteria change, P8-P12 work or model-strength claim was added.

## 2026-06-12 - v2.77

- Decided whether the minimal P7 synthetic/local supervised fixture and
  feature-label smoke implementation can be accepted as current-scope
  complete.
- Added
  `docs/03_supervised_policy/03Q_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FEATURE_LABEL_SMOKE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`.
- Acceptance decision:
  `Accepted as current-scope complete.`
- Accepted scope is limited to the exact helper, project-authored
  synthetic/local fixture, smoke tests and direct docs / governance
  synchronization approved by `03O` and reviewed by `03P`.
- Accepted behavior is only JSON-safe synthetic/local smoke mapping
  validation, candidate feature family validation, candidate label family
  validation, public-information-only placeholder checks, hidden / future
  information rejection, unsafe provenance / unsafe claim rejection and
  non-evidence guardrails.
- New `10_NEXT` first item:
  `Define next P7 current-scope supervised-learning task after minimal synthetic feature-label smoke acceptance.`
- This is P7 minimal synthetic/local supervised feature-label smoke
  current-scope acceptance decision evidence only.
- No production code, implementation logic, tests, fixtures, data files,
  replay schema code, parser, dataset reader, ingestion, actual feature
  extraction, actual label generation, supervised dataset construction,
  training, tuning, self-play, league, runner behavior, model architecture,
  trainer, dataloader, optimizer, loss, checkpoint, weights, model-output
  integration, CLI, broad file ingestion, real Tenhou, real haifu, external
  logs, platform data, third-party binary call, latency measurement,
  fixed-position exact-match, metric implementation, registry code change,
  promotion criteria change, P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.76

- Reviewed the minimal P7 synthetic/local supervised fixture and feature-label
  smoke implementation.
- Added
  `docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`.
- Review decision:
  `Review can close.`
- The review confirms:
  - the exact `03O` allowed implementation file list was respected.
  - `src/mjlabai/supervised/feature_label_schema.py` remains
    standard-library-only and validates only in-memory synthetic/local smoke
    mappings and guardrails.
  - `tests/fixtures/supervised/synthetic_supervised_smoke.json` remains
    project-authored synthetic/local only, not Tenhou data, not real haifu, not
    external log, not platform data, not model output, not training data, not
    model-strength evidence, not LuckyJ `10.68` comparison and not
    candidate-promotion evidence.
  - supervised tests cover only the approved smoke scope.
  - validation passes.
  - governance is synchronized.
- New `10_NEXT` first item:
  `Decide whether minimal P7 synthetic/local supervised fixture and feature-label smoke implementation can be accepted as current-scope complete.`
- This is P7 minimal synthetic/local supervised feature-label smoke
  implementation review evidence only.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, actual feature extraction, actual label
  generation, supervised dataset construction, training, tuning, self-play,
  league, runner behavior, model architecture, trainer, dataloader, optimizer,
  loss, checkpoint, weights, model-output integration, CLI, broad file
  ingestion, real Tenhou, real haifu, external logs, platform data,
  third-party binary call, latency measurement, fixed-position exact-match,
  metric implementation, registry code change, promotion criteria change,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.75

- Implemented the minimal P7 synthetic/local supervised fixture and
  feature-label smoke task approved by `03O`.
- Added exact approved implementation files:
  - `src/mjlabai/supervised/feature_label_schema.py`
  - `tests/fixtures/supervised/synthetic_supervised_smoke.json`
  - `tests/supervised/test_feature_label_schema.py`
  - `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- The helper validates only:
  - in-memory JSON-safe synthetic/local smoke mappings.
  - project-authored synthetic/local provenance.
  - candidate feature family names.
  - candidate label family names.
  - public-information-only placeholder fields.
  - absent hidden/future information guardrails.
  - all-false non-evidence flags.
  - rejection of training-use approval, source approval, real data,
    model-output, self-play and league provenance.
- The fixture is project-authored synthetic/local only and explicitly not
  Tenhou data, not real haifu, not external log, not platform data, not model
  output, not training data, not model-strength evidence, not LuckyJ `10.68`
  comparison and not candidate-promotion evidence.
- New `10_NEXT` first item:
  `Review minimal P7 synthetic/local supervised fixture and feature-label smoke implementation.`
- This is P7 minimal synthetic/local supervised feature-label smoke
  implementation evidence only.
- No files outside the exact `03O` implementation list and direct
  docs/governance synchronization were added or modified.
- No replay schema code, P6 synthetic replay fixture, existing P6 tests,
  parser, dataset reader, data ingestion, actual feature extraction, actual
  label generation, supervised dataset construction, training, tuning,
  self-play, league, runner behavior, model architecture, trainer, dataloader,
  optimizer, loss, checkpoint, weights, model-output integration, CLI, broad
  file ingestion, real Tenhou, real haifu, external logs, platform data,
  OpenAI / LLM / model API call, Akochan `system.exe`, `libai.so`,
  third-party binary call, latency measurement, fixed-position exact-match,
  metric implementation, registry code change, promotion criteria change,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.74

- Prepared the approval decision for the minimal P7 synthetic/local supervised
  fixture and feature-label smoke implementation task.
- Added
  `docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`.
- Decision:
  `Approved for next minimal implementation task.`
- Exact approved implementation files for the next task:
  - `src/mjlabai/supervised/feature_label_schema.py`
  - `tests/fixtures/supervised/synthetic_supervised_smoke.json`
  - `tests/supervised/test_feature_label_schema.py`
  - `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- Directly related docs / governance updates are allowed only as necessary to
  record implementation evidence, validation, risks and the next task.
- New `10_NEXT` first item:
  `Implement minimal P7 synthetic/local supervised fixture and feature-label smoke only.`
- This is P7 implementation approval-decision evidence only.
- The decision does not execute implementation, create fixture files, add
  tests, add production code, add data files, generate an implementation
  prompt, approve parser / reader / ingestion, approve actual feature
  extraction, approve actual label generation, approve supervised dataset
  construction, approve training, approve model-output integration, approve
  real data, approve self-play, approve league or approve P8-P12 entry.
- No implementation files, tests, fixtures, data files, parser, dataset reader,
  ingestion, actual feature extraction, actual label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P8-P12 work or
  model-strength claim was added.

## 2026-06-12 — v2.73

- Reviewed the minimal P7 synthetic/local supervised fixture and feature-label
  smoke proposal before implementation.
- Added
  `docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md`.
- The review confirms:
  - `03M` scope is docs-only and correctly bounded before implementation.
  - minimal future implementation candidate classes are narrow and
    synthetic/local.
  - candidate exact files are safe and remain candidate paths only.
  - synthetic/local fixture boundary is sufficient.
  - feature / label smoke boundary is sufficient and does not imply feature
    extraction or label generation approval.
  - current vs future validation commands are clearly distinguished.
  - future implementation approval conditions and stop conditions are
    sufficient.
  - proposal risks and mitigations are sufficient.
  - evidence grade and non-evidence warnings are conservative.
  - governance synchronization is consistent.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Prepare approval decision for minimal P7 synthetic/local supervised fixture and feature-label smoke implementation task.`
- This is P7 minimal synthetic/local supervised fixture and feature-label smoke
  proposal review evidence only.
- P7 implementation, P7 first-task execution, fixture creation, tests,
  production code, data files, source approval, parser, dataset reader,
  ingestion, feature extraction, label generation, supervised dataset
  construction, training, model-output integration, real Tenhou, real haifu,
  external logs, platform data, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.72

- Defined a minimal P7 synthetic/local supervised fixture and feature-label
  smoke proposal before implementation.
- Added
  `docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`.
- The proposal records:
  - scope and purpose.
  - minimal future implementation candidate classes.
  - exact candidate future files:
    `src/mjlabai/supervised/feature_label_schema.py`,
    `tests/fixtures/supervised/synthetic_supervised_smoke.json`,
    `tests/supervised/test_feature_label_schema.py` and
    `tests/supervised/test_synthetic_supervised_fixture_schema.py`.
  - synthetic/local fixture boundaries.
  - feature / label smoke boundaries.
  - future validation commands.
  - future implementation approval conditions.
  - stop conditions.
  - proposal risks.
  - evidence grade and explicit non-evidence boundaries.
- Planning decision:
  `A minimal P7 synthetic/local supervised fixture and feature-label smoke proposal is defined before implementation. This does not approve P7 implementation, fixture creation, tests, production code, data files, feature extraction, label generation, parser, dataset reader, ingestion, training, model-output integration, real data, self-play, league or P8-P12 entry.`
- New `10_NEXT` first item:
  `Review minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation.`
- This is P7 minimal synthetic/local supervised fixture and feature-label smoke
  proposal evidence only.
- P7 implementation, fixture creation, tests, production code, data files,
  source approval, parser, dataset reader, ingestion, feature extraction,
  label generation, supervised dataset construction, training,
  model-output integration, real Tenhou, real haifu, external logs, platform
  data, self-play, league and P8-P12 remain unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.71

- Reviewed P7 supervised-learning risk and evidence taxonomy before
  implementation.
- Added
  `docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`.
- The review confirms:
  - `03K` scope is docs-only and correctly bounded before implementation.
  - risk taxonomy coverage is sufficient for the current P7 review gate.
  - evidence taxonomy and evidence-to-claim mapping are conservative.
  - current P7 evidence classification remains planning / review evidence
    only.
  - future evidence requirements do not approve source ingestion, feature
    extraction, label generation or training.
  - forbidden evidence interpretations prevent model-strength, Tenhou ranked,
    stable-dan ranked-game, LuckyJ `10.68` and candidate-promotion overclaims.
  - risk / evidence dependency order is auditable.
  - governance synchronization requirements are clear.
  - P8-P12 remain outside this task.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation.`
- This is P7 supervised-learning risk and evidence taxonomy review evidence
  only.
- P7 implementation, P7 first-task execution, training data source, source
  ingestion, parser, dataset reader, ingestion, feature extraction, label
  generation, real Tenhou, real haifu, external logs, platform data,
  model-output integration, CLI, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.70

- Defined P7 supervised-learning risk and evidence taxonomy before
  implementation.
- Added
  `docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`.
- The taxonomy records:
  - P7 risk categories for scope/stage creep, source approval, training-data
    approval, parser / reader / ingestion creep, feature/label approval
    ambiguity, hidden-information leakage, future-information leakage,
    train/validation/test leakage, early model-output integration, real-data
    and platform-data leakage, account/cookie/token risk, third-party
    binaries/weights/params, training-before-approval, model-artifact
    provenance, evidence overclaiming, model-strength overclaiming,
    LuckyJ/Tenhou/stable-dan overclaiming, P8/P10/P12 creep and candidate
    promotion overclaiming.
  - P7 evidence grades from docs-only scope evidence through future Tenhou
    validation evidence candidates.
  - current P7 evidence classification for `03E` through `03K`.
  - future P7 evidence fields.
  - evidence-to-claim mapping.
  - forbidden evidence interpretations.
  - risk/evidence dependency order.
  - governance update requirements.
  - P8-P12 non-entry boundaries.
- Planning decision:
  `P7 supervised-learning risk and evidence taxonomy is defined before implementation. This does not approve P7 implementation, P7 first-task execution, training, source ingestion, parser, dataset reader, feature extraction, label generation, real data, model-output integration, self-play, league, model-strength claims or P8-P12 entry.`
- New `10_NEXT` first item:
  `Review P7 supervised-learning risk and evidence taxonomy before implementation.`
- This is P7 supervised-learning risk and evidence taxonomy definition
  evidence only.
- P7 implementation, P7 first-task execution, training data source, source
  ingestion, parser, dataset reader, ingestion, feature extraction, label
  generation, real Tenhou, real haifu, external logs, platform data,
  model-output integration, CLI, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.69

- Reviewed P7 feature and label readiness boundary before implementation.
- Added
  `docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`.
- The review confirms:
  - `03I` scope is correct.
  - feature readiness boundary is sufficient for the current pre-implementation gate.
  - label readiness boundary is sufficient for the current pre-implementation gate.
  - candidate feature families are planning-only and not approved for implementation.
  - candidate label families are planning-only and not approved for generation.
  - forbidden feature / label scope is strict enough.
  - dependency map is correct and conservative.
  - feature / label risks and mitigations are sufficient.
  - evidence requirements are sufficient and conservative.
  - readiness vocabulary is safe and cannot be read as approval.
  - governance synchronization is consistent.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define P7 supervised-learning risk and evidence taxonomy before implementation.`
- This is P7 feature and label readiness boundary review evidence only.
- P7 implementation, P7 first-task execution, training data source, source
  ingestion, parser, dataset reader, ingestion, feature extraction, label
  generation, real Tenhou, real haifu, external logs, platform data,
  model-output integration, CLI, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.68

- Defined P7 feature and label readiness boundary before implementation.
- Added
  `docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`.
- The boundary records:
  - future feature readiness requirements.
  - future label readiness requirements.
  - candidate feature families.
  - candidate label families.
  - forbidden feature / label scope.
  - dependency map before any implementation.
  - hidden-information, future-information and train/test leakage risks.
  - evidence requirements.
  - readiness vocabulary.
  - planning decision.
- Planning decision:
  `P7 feature and label readiness boundary is defined before implementation. This does not approve P7 implementation, feature extraction, label generation, parser, dataset reader, ingestion, training, real data, model-output integration, self-play, league or P8-P12 entry.`
- New `10_NEXT` first item:
  `Review P7 feature and label readiness boundary before implementation.`
- This is P7 feature and label readiness boundary definition evidence only.
- P7 implementation, P7 first-task execution, training data source, source
  ingestion, parser, dataset reader, ingestion, feature extraction, label
  generation, real Tenhou, real haifu, external logs, platform data,
  model-output integration, CLI, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-12 — v2.67

- Reviewed P7 supervised-learning data/source readiness inventory before
  implementation.
- Added
  `docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`.
- The review confirms:
  - `03G` scope is correct.
  - candidate data/source categories are complete enough for the current gate.
  - current approved P7 training source remains `None.`
  - readiness status vocabulary is conservative and does not imply approval.
  - training-data readiness requirements are sufficient.
  - P6 source-rights consistency is clear.
  - parser / reader / ingestion remain unapproved.
  - feature extraction / label generation remain unapproved.
  - data/source risks and evidence requirements are sufficient.
  - governance synchronization is consistent.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define P7 feature and label readiness boundary before implementation.`
- This is P7 supervised-learning data/source readiness inventory review
  evidence only.
- P7 implementation, P7 first-task execution, training data source, source
  ingestion, parser, dataset reader, ingestion, feature extraction, label
  generation, real Tenhou, real haifu, external logs, platform data,
  model-output integration, CLI, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-08 — v2.66

- Defined P7 supervised-learning data/source readiness inventory before
  implementation.
- Added
  `docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`.
- The inventory records:
  - P7 data/source candidate categories.
  - current source status and blockers.
  - readiness status vocabulary.
  - training-data readiness requirements.
  - source-rights consistency with P6.
  - parser / reader / ingestion dependency status.
  - feature / label readiness status.
  - P7 data/source risks.
  - future evidence requirements.
  - planning decision and next review gate.
- Current approved P7 training source:
  `None.`
- New `10_NEXT` first item:
  `Review P7 supervised-learning data/source readiness inventory before implementation.`
- This is P7 supervised-learning data/source readiness inventory definition
  evidence only.
- P7 implementation, P7 first-task execution, training, training data source,
  source ingestion, parser, dataset reader, feature extraction, label
  generation, real Tenhou, real haifu, external logs, platform data,
  model-output integration, CLI, self-play, league and P8-P12 remain
  unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-08 — v2.65

- Reviewed P7 supervised-learning scope, entry criteria and first task before
  implementation.
- Added
  `docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`.
- The review confirms:
  - `03E` is a docs-only P7 scope / entry criteria / first-task definition.
  - post-full-P6 context is accurate.
  - allowed docs-only scope is sufficient.
  - forbidden scope is strict enough.
  - entry criteria distinguish definition from satisfaction.
  - exit criteria are future-only.
  - required inputs are honestly marked incomplete where appropriate.
  - risk and evidence requirements are sufficient for the current boundary.
  - P8-P12 remain closed.
  - no blocker was found.
- Review decision:
  `Review can close.`
- New `10_NEXT` first item:
  `Define P7 supervised-learning data/source readiness inventory before implementation.`
- This is P7 scope / entry criteria / first-task review evidence only.
- P7 implementation, P7 first-task execution, training, parser, dataset
  reader, ingestion, feature extraction, label generation, real Tenhou, real
  haifu, external logs, platform data, model-output integration, CLI,
  self-play, league and P8-P12 remain unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-08 — v2.64

- Defined P7 supervised-learning scope, entry criteria and first task before
  implementation.
- Added `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`.
- The document records:
  - post-full-P6 context.
  - P7 purpose and north-star relationship.
  - allowed docs-only scope.
  - forbidden scope.
  - entry criteria before implementation.
  - exit criteria draft.
  - required inputs and current status.
  - risk review requirements.
  - evidence requirements.
  - P8-P12 non-entry boundary.
  - first task candidate:
    `Review P7 scope, entry criteria and first task before implementation.`
- New `10_NEXT` first item:
  `Review P7 scope, entry criteria and first task before implementation.`
- This is P7 scope / entry criteria / first-task definition evidence only.
- P7 implementation, P7 first-task execution, training, parser, dataset
  reader, ingestion, feature extraction, label generation, real Tenhou, real
  haifu, external logs, platform data, model-output integration, CLI,
  self-play, league and P8-P12 remain unapproved.
- No production code, tests, fixtures, data files, replay schema code, parser,
  dataset reader, ingestion, feature extraction, label generation, CLI, broad
  file ingestion, model-output integration, real Tenhou, real haifu, external
  logs, platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-07 — v2.63

- Completed the post-full-P6 transition review before defining any P7 task.
- Added `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md`.
- The review confirms:
  - full P6 is closed only for the documented P6 data-system scope.
  - P7-P12 remain unapproved.
  - P7 implementation and P7 first-task execution remain unapproved.
  - the next task may define P7 scope, entry criteria and first task as
    docs-only planning before implementation.
- Decision:
  `Yes, define P7 scope / entry criteria / first task as docs-only next task.`
- New `10_NEXT` first item:
  `Define P7 scope, entry criteria and first task before implementation.`
- This transition review is not P7 implementation approval, P8-P12 entry
  approval, parser / reader / ingestion approval, feature / label approval,
  real-data approval, model-output integration approval or model-strength
  evidence.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7 implementation,
  P8-P12 work or model-strength claim was added.

## 2026-06-07 — v2.62

- Ran the final full P6 closure review gate.
- Added `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`.
- The review confirms:
  - the full P6 review chain from `02A` through `02Z` is complete.
  - C1-C27 final full P6 closure criteria pass.
  - `02Y` finalized handoff / evidence index.
  - `02Z` found no risk/source-rights blocker.
  - required validation commands passed.
  - governance documents are synchronized.
  - no unresolved blocker remains.
- Decision:
  `Full P6 can close`.
- Accepted closure boundary:
  docs/governance/source-rights planning, accepted synthetic/local minimal
  replay schema and project-authored synthetic fixture smoke implementation,
  and deferred/blocked/later-stage inventory.
- New `10_NEXT` first item:
  `Run post-full-P6 transition review before defining any P7 task.`
- Full P6 closure is not P7-P12 entry approval and is not P7 first-task
  approval.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, P7-P12 work or
  model-strength claim was added.

## 2026-06-07 — v2.61

- Reviewed full P6 risk register and source-rights inventory consistency
  before final closure review.
- Added
  `docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`.
- The review confirms:
  - source-rights inventory status remains consistent across `02A`, `02D` and
    the full-P6 closure chain.
  - risk register coverage remains sufficient for overclaim, stage drift,
    implementation drift, source-rights, platform/account and third-party
    artifact risks.
  - blocked real Tenhou, real haifu, external logs, platform data, account /
    session / cookie / token data and third-party artifact categories remain
    blocked.
  - deferred parser, dataset reader, ingestion, feature extraction, label
    generation, CLI and model-output integration remain unapproved.
  - no risk/source-rights blocker was found for the final full P6 closure
    review gate.
  - review decision:
    `Review can close; no risk/source-rights blocker for final full P6 closure review.`
- New `10_NEXT` first item:
  `Run final full P6 closure review gate.`
- Full P6 remains open until that later final closure review explicitly passes.
- P7-P12 entry remains unapproved.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.60

- Finalized full P6 handoff and evidence index after closure criteria review.
- Added
  `docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`.
- The finalization records:
  - a full-P6 handoff finalization summary.
  - a P6 evidence index covering P6 planning / boundary / review artifacts,
    accepted implementation artifacts, validation and governance artifacts.
  - evidence grade consistency across accepted current-scope evidence and
    roadmap / criteria / review / finalization evidence.
  - remaining required full-P6 items.
  - deferred, blocked, later-stage and out-of-scope summaries.
  - next risk / source-rights consistency review scope.
  - planning decision and evidence grade.
- New `10_NEXT` first item:
  `Review full P6 risk register and source-rights inventory consistency before final closure review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  metric implementation, registry code change, promotion criteria change,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.59

- Reviewed full P6 closure criteria after roadmap and remaining scope review.
- Added
  `docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`.
- The review confirms:
  - `02W` scope is correct.
  - full-P6 closure scope is reasonable.
  - C1-C27 criteria are sufficient, conservative and auditable.
  - exit readiness checklist is auditable.
  - required remaining items are docs/review/closure-only.
  - deferred, blocked, later-stage and out-of-scope classifications are safe.
  - P7-P12 non-entry conditions are sufficient.
  - governance synchronization is consistent.
  - validation passed.
  - review decision: `Review can close`.
- New `10_NEXT` first item:
  `Finalize full P6 handoff and evidence index after closure criteria review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.58

- Defined full P6 closure criteria after roadmap and remaining scope review.
- Added
  `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`.
- The criteria definition records:
  - full-P6 closure scope and explicit excluded scope.
  - C1-C27 full-P6 closure criteria.
  - full-P6 exit readiness checklist.
  - required remaining full-P6 closure items.
  - deferred items, blocked items and later-stage / out-of-scope items.
  - P7-P12 non-entry conditions.
  - planning decision and evidence grade.
- New `10_NEXT` first item:
  `Review full P6 closure criteria after roadmap and remaining scope review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.57

- Reviewed the full P6 closure roadmap and remaining scope inventory after
  accepted current-scope closure.
- Added
  `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`.
- The review confirms:
  - `02U` scope is correct.
  - accepted current-scope closed artifacts are complete.
  - remaining scope inventory classification is reasonable.
  - the full P6 closure roadmap is conservative and docs-only.
  - required, deferred, blocked, later-stage and out-of-scope classifications
    are safe.
  - P7-P12 non-entry boundary is sufficient.
  - governance synchronization is consistent.
  - validation passed.
  - review decision: `Review can close`.
- New `10_NEXT` first item:
  `Define full P6 closure criteria after roadmap and remaining scope review.`
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.56

- Defined the full P6 closure roadmap and remaining scope inventory after
  accepted current-scope closure.
- Added
  `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`.
- The roadmap / inventory records:
  - accepted current-scope P6 is closed only for the synthetic/local minimal
    replay schema and project-authored fixture scope.
  - full P6 remains open.
  - P7-P12 entry remains unapproved.
  - remaining P6 items are classified as required, deferred, blocked,
    later-stage or explicitly out of scope.
  - required full-P6 closure path is docs-only: roadmap review, closure
    criteria definition / review, handoff / evidence finalization, risk /
    source-rights consistency review and final full-P6 closure review.
  - blocked/deferred items include real data, parser, dataset reader,
    ingestion, feature extraction, label generation, model-output integration,
    CLI and later-stage training / self-play / league work.
  - the selected next task is:
    `Review full P6 closure roadmap and remaining scope inventory after
    current-scope closure`.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, decision record, evidence log, risk register and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.55

- Completed the post-current-scope P6 transition review.
- Added
  `docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`.
- The transition review records:
  - P5 is closed only for the current synthetic/local evaluation groundwork
    scope.
  - accepted current-scope P6 is closed only for the synthetic/local minimal
    replay schema and project-authored fixture scope.
  - full P6 remains open.
  - P7-P12 entry remains unapproved.
  - candidate next directions were reviewed.
  - the selected next task is:
    `Define full P6 closure roadmap and remaining scope inventory after
    current-scope closure`.
  - the selected next task is docs-only.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, decision record, evidence log, risk register and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.54

- Ran the final P6 current-scope data-system closure review gate.
- Added
  `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`.
- The final closure review records:
  - review chain completeness from P6 scope/source inventory through minimal
    implementation, acceptance, closure criteria and closure criteria review.
  - closure criteria final review passed with no blocker.
  - validation passed.
  - governance synchronization is complete.
  - decision:
    `Current-scope P6 can close`.
  - accepted boundary: only the accepted synthetic/local minimal replay schema
    and project-authored synthetic fixture scope.
  - full P6 is not closed.
  - P7-P12 entry is not approved.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, decision record, evidence log, risk register and `10_NEXT`.
- New `10_NEXT` first item:
  `Run post-current-scope P6 transition review before defining any next-stage
  data-system or P7 task.`
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.53

- Reviewed P6 current-scope data-system closure criteria after minimal replay
  schema acceptance.
- Added
  `docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`.
- The review confirms:
  - `02R` scope is correct.
  - current accepted / not accepted scope is accurate.
  - C1-C25 closure criteria are sufficient, conservative and auditable.
  - exit readiness checklist is auditable and keeps final closure review as
    `not_ready`.
  - required remaining items are docs/review/closure items only.
  - deferred items are correctly not required for current-scope closure.
  - P7-P12 non-entry conditions are sufficient.
  - governance synchronization is consistent.
  - validation passed.
  - review decision: `Review can close`.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register and `10_NEXT`.
- New `10_NEXT` first item:
  `Run final P6 current-scope data-system closure review gate`.
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  current-scope P6 closure, P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.52

- Defined P6 current-scope data-system closure criteria after minimal replay
  schema acceptance.
- Added
  `docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`.
- The closure-criteria definition records:
  - current accepted scope from `02P`.
  - the `02Q` next-task selection context.
  - minimum P6 current-scope closure criteria.
  - exit readiness checklist.
  - required remaining current-scope P6 items before closure.
  - deferred items that are not required for current-scope closure.
  - P7-P12 non-entry conditions.
  - the decision that current-scope P6 cannot be closed by this task.
  - next task:
    `Review P6 current-scope data-system closure criteria after minimal replay
    schema acceptance.`
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register and `10_NEXT`.
- New `10_NEXT` first item:
  `Review P6 current-scope data-system closure criteria after minimal replay
  schema acceptance.`
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  current-scope P6 closure, P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.51

- Defined the next P6 current-scope data-system task after minimal replay schema
  acceptance.
- Added
  `docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`.
- The task-definition gate records:
  - accepted current scope from `02P`: exact minimal replay schema module,
    project-authored synthetic/local fixture, two minimal local tests and
    directly related governance synchronization.
  - candidate next docs-only tasks and their risks.
  - selected next task:
    `Define P6 current-scope data-system closure criteria after minimal replay
    schema acceptance.`
  - allowed scope, forbidden scope, validation commands and stop conditions for
    that next task.
  - evidence grade: P6 next current-scope data-system task definition after
    minimal replay schema acceptance evidence only.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register and `10_NEXT`.
- New `10_NEXT` first item:
  `Define P6 current-scope data-system closure criteria after minimal replay
  schema acceptance.`
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, full P6 closure,
  P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.50

- Accepted the minimal P6 replay schema and project-authored synthetic fixture
  implementation as current-scope complete.
- Added
  `docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`.
- The acceptance decision records:
  - decision: `Accepted as current-scope complete`.
  - accepted scope: the exact minimal replay schema module,
    project-authored synthetic/local fixture, two minimal local tests and
    directly related governance synchronization.
  - non-acceptance: full P6 closure, additional replay schema expansion,
    additional fixtures/tests, parser, dataset reader, data ingestion, feature
    extraction, label generation, real data, CLI, model-output integration,
    training, self-play, league, LuckyJ `10.68` comparison, candidate promotion
    and P7-P12 entry remain unapproved.
  - evidence grade: P6 minimal replay schema and project-authored synthetic
    fixture current-scope acceptance decision evidence only.
  - validation passed:
    `git diff --check`,
    `python3 -m unittest tests/data/test_replay_schema.py` and
    `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register and `10_NEXT`.
- New `10_NEXT` first item:
  `Define next P6 current-scope data-system task after minimal replay schema
  acceptance.`
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, P7-P12 work or
  model-strength claim was added.

## 2026-06-07 — v2.49

- Reviewed the minimal P6 replay schema and project-authored synthetic fixture
  implementation.
- Added
  `docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md`.
- The review confirms:
  - the exact implementation files from `02N` were respected.
  - no other code, test, fixture or data file was added or modified by the
    implementation commit.
  - `src/mjlabai/data/replay_schema.py` remains standard-library-only,
    in-memory and minimal.
  - `tests/fixtures/data/synthetic_replay_smoke.json` remains
    project-authored synthetic/local only.
  - `tests/data/test_replay_schema.py` and
    `tests/data/test_synthetic_replay_fixture_schema.py` remain minimal/local.
  - validation passed:
    `git diff --check`,
    `python3 -m unittest tests/data/test_replay_schema.py` and
    `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`.
  - governance synchronization is sufficient.
  - review can close with no blocker.
- New `10_NEXT` first item:
  `Decide whether minimal P6 replay schema and synthetic fixture
  implementation can be accepted as current-scope complete.`
- No production code, tests, fixtures, replay schema code, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, broad file
  ingestion, model-output integration, real Tenhou, real haifu, external logs,
  platform data, OpenAI / LLM / model API call, third-party binary call,
  training, tuning, self-play, league, runner behavior, P7-P12 work or
  model-strength claim was added.

## 2026-06-07 — v2.48

- Implemented the exact minimal P6 replay schema and project-authored
  synthetic fixture task approved by `02N`.
- Added `src/mjlabai/data/replay_schema.py`.
  - Provides constant schema/source-category names.
  - Provides `validate_replay_record(...)`,
    `validate_replay_fixture(...)`, `assert_valid_replay_fixture(...)` and
    `is_project_authored_synthetic_fixture(...)`.
  - Validates in-memory mappings only.
  - Checks project-authored synthetic provenance, required top-level and
    record keys, no-real-data / no-account-id / no-model-output /
    no-training-use guardrails and JSON-safe content.
  - Does not read files, parse real logs, implement ingestion, extract
    features, generate labels, add CLI or touch model-output paths.
- Added `tests/fixtures/data/synthetic_replay_smoke.json`.
  - Project-authored synthetic/local only.
  - Not Tenhou data, not real haifu, not external log, not platform data, not
    model output, not training data, not model-strength evidence and not
    LuckyJ `10.68` comparison.
- Added `tests/data/test_replay_schema.py` and
  `tests/data/test_synthetic_replay_fixture_schema.py`.
- Local validation passed:
  - `git diff --check`
  - `python3 -m unittest tests/data/test_replay_schema.py`
  - `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register and `10_NEXT`.
- New `10_NEXT` first item:
  `Review minimal P6 replay schema and project-authored synthetic fixture
  implementation.`
- No parser, dataset reader, ingestion, feature extraction, label generation,
  CLI, broad file ingestion, model-output integration, real Tenhou, real
  haifu, external logs, platform data, OpenAI / LLM / model API call,
  third-party binary call, training, tuning, self-play, league, runner
  behavior, P7-P12 work or model-strength claim was added.

## 2026-06-07 — v2.47

- Prepared the approval decision for the minimal P6 replay schema and
  project-authored synthetic fixture implementation task.
- Added
  `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`.
- The approval decision records:
  - purpose and limits of the docs-only approval gate.
  - approval options A / B / C.
  - approval criteria review across `02A` through `02M`.
  - decision: `Approved for next minimal implementation task`.
  - exact allowed implementation files:
    `src/mjlabai/data/replay_schema.py`,
    `tests/fixtures/data/synthetic_replay_smoke.json`,
    `tests/data/test_replay_schema.py` and
    `tests/data/test_synthetic_replay_fixture_schema.py`.
  - exact allowed future scope: one minimal replay schema module, one
    project-authored synthetic/local fixture, two minimal tests and directly
    related docs/governance synchronization.
  - forbidden future expansion: real Tenhou, real haifu, external logs,
    platform data, parser, dataset reader, ingestion, feature extraction,
    label generation, CLI, model-output integration, training, self-play,
    league, P7-P12 and model-strength claims.
  - future validation commands:
    `git diff --check`,
    `python3 -m unittest tests/data/test_replay_schema.py` and
    `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`.
  - rollback and stop conditions.
- Updated `02L`, `02M`, handoff, docs index, stage contract, milestones,
  backlog, technical plan, evidence log, risk register, decision record and
  `10_NEXT`.
- No production code, tests, fixtures, replay schema code, synthetic replay
  fixture, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, OpenAI / LLM / model API call, third-party binary
  call, training, tuning, self-play, league, runner behavior, P7-P12 work or
  model-strength claim was added.

## 2026-06-07 — v2.46

- Reviewed the P6 minimal replay schema and synthetic fixture implementation
  proposal before code.
- Added
  `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`.
- The review confirms:
  - `02L` scope is correct.
  - candidate implementation classes are sufficient and conservative.
  - proposed file candidates are clear and remain candidate paths only.
  - minimal replay schema code, synthetic/local fixture and validation test
    candidate boundaries are narrow enough for a later approval-decision task.
  - allowed future minimal scope is conservative.
  - forbidden future expansion, rollback plan and stop conditions are
    sufficient.
  - human / Web ChatGPT approval requirement is clear.
  - P7-P12 non-entry boundary is sufficient.
  - governance docs are synchronized.
- Decision:
  - review can close.
  - no blocker was found.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - replay fixture implementation remains closed.
  - tests, data ingestion, dataset readers, parsers, feature extraction and
    label generation remain closed.
  - the next task is `Prepare approval decision for minimal P6 replay schema
    and synthetic fixture implementation task.`
- Evidence grade:
  - P6 minimal replay schema and synthetic fixture implementation proposal
    review evidence only.
- Updated `02A`, `02B`, `02F`, `02H`, `02J`, `02L`, handoff, docs index,
  stage contract, milestones, backlog, technical plan, evidence log, risk
  register, decision record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, OpenAI / LLM / model API call, third-party binary
  call, training, tuning, self-play, league, runner behavior, P7-P12 work or
  model-strength claim was added.

## 2026-06-07 — v2.45

- Prepared the P6 minimal replay schema and synthetic fixture implementation
  proposal for review before code.
- Added
  `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`.
- The proposal draft records:
  - target stage: `P6 data system / docs-only proposal drafting`.
  - candidate implementation classes for minimal replay schema code,
    project-authored synthetic/local replay fixture, minimal schema validation
    test, minimal fixture validation test and evidence/risk/docs
    synchronization.
  - proposed future file candidates:
    `src/mjlabai/data/replay_schema.py`,
    `tests/fixtures/data/synthetic_replay_smoke.json`,
    `tests/data/test_replay_schema.py` and
    `tests/data/test_synthetic_replay_fixture_schema.py`.
  - minimal replay schema code candidate boundary.
  - minimal synthetic/local fixture candidate boundary.
  - minimal validation test candidate boundary.
  - allowed future minimal implementation scope if later approved.
  - forbidden future expansion.
  - future validation command candidates.
  - evidence / risk / docs update plan.
  - rollback plan and stop conditions.
  - human / Web ChatGPT approval requirement.
  - P7-P12 non-entry boundary.
- Decision:
  - P6 minimal replay schema and synthetic fixture implementation proposal is
    prepared for review before code.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - fixture implementation remains closed.
  - tests, data ingestion, dataset readers, parsers, feature extraction and
    label generation remain closed.
  - the next task is `Review P6 minimal replay schema and synthetic fixture
    implementation proposal before code.`
- Evidence grade:
  - P6 minimal replay schema and synthetic fixture implementation proposal
    drafting evidence only.
- Updated `02A`, `02B`, `02F`, `02H`, `02J`, `02K`, handoff, docs index,
  stage contract, milestones, backlog, technical plan, evidence log, risk
  register, decision record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, OpenAI / LLM / model API call, third-party binary
  call, training, tuning, self-play, league, runner behavior, P7-P12 work or
  model-strength claim was added.

## 2026-06-06 — v2.44

- Reviewed the P6 replay schema and synthetic fixture implementation proposal
  boundary before code.
- Added
  `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`.
- The review confirms:
  - `02J` scope is correct.
  - candidate proposal classes are sufficient and conservative.
  - required future proposal sections are sufficient.
  - allowed and forbidden proposal boundaries are strict enough.
  - source and fixture constraints are sufficient.
  - minimal replay schema and synthetic fixture candidate boundaries remain
    proposal-only.
  - test and validation proposal boundaries remain proposal-only.
  - future implementation approval conditions are sufficient.
  - proposal decision vocabulary is safe.
  - P7-P12 non-entry boundary is sufficient.
  - governance docs are synchronized.
- Decision:
  - review can close.
  - no blocker was found.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - replay fixture implementation remains closed.
  - tests, data ingestion, dataset readers, parsers, feature extraction and
    label generation remain closed.
  - the next task is `Prepare P6 minimal replay schema and synthetic fixture
    implementation proposal for review before code.`
- Evidence grade:
  - P6 replay schema and synthetic fixture implementation proposal boundary
    review evidence only.
- Updated `02A`, `02B`, `02F`, `02I`, `02J`, handoff, docs index, stage
  contract, milestones, backlog, technical plan, evidence log, risk register,
  decision record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.43

- Defined the P6 replay schema and synthetic fixture implementation proposal
  boundary before code.
- Added
  `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`.
- The proposal boundary records:
  - candidate proposal classes for minimal replay schema code,
    project-authored synthetic/local replay fixture, validation tests, deferred
    parser / dataset reader, deferred feature extraction / label generation,
    deferred data ingestion and blocked real/external/platform source
    integration.
  - required sections for any future implementation proposal.
  - allowed and forbidden proposal scope.
  - source and fixture constraints.
  - minimal replay schema code candidate boundary.
  - minimal synthetic/local fixture candidate boundary.
  - test and validation proposal boundary.
  - future implementation approval conditions.
  - proposal decision vocabulary.
  - P7-P12 non-entry boundary.
  - proposal boundary risks.
- Decision:
  - the proposal boundary is defined for review before code.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - replay fixture implementation remains closed.
  - tests, data ingestion, dataset readers, parsers, feature extraction and
    label generation remain closed.
  - the next task is `Review P6 replay schema and synthetic fixture
    implementation proposal boundary before code.`
- Evidence grade:
  - P6 replay schema and synthetic fixture implementation proposal boundary
    definition evidence only.
- Updated `02A`, `02B`, `02F`, `02H`, `02I`, handoff, docs index, stage
  contract, milestones, backlog, technical plan, evidence log, risk register,
  decision record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.42

- Reviewed the P6 replay schema and fixture implementation readiness checklist
  before code.
- Added
  `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`.
- The review confirms:
  - `02H` scope is correct.
  - candidate implementation classes are sufficient and conservative.
  - replay schema code readiness criteria are sufficient and remain
    `not_ready_for_implementation`.
  - synthetic/local replay fixture readiness criteria are sufficient and remain
    `not_ready_for_implementation`.
  - parser / dataset reader readiness remains deferred and not approved.
  - feature extraction / label generation readiness remains deferred and not
    approved.
  - data ingestion readiness remains deferred and not approved.
  - readiness decision vocabulary is safe and does not imply implementation
    approval.
  - cross-artifact dependency map is complete for current P6 docs-only
    planning.
  - P7-P12 non-entry boundary is sufficient.
  - readiness risks and mitigations are sufficient.
  - governance docs are synchronized.
- Decision:
  - review can close.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - replay fixture implementation remains closed.
  - data ingestion, dataset readers, parsers, feature extraction and label
    generation remain closed.
  - the next task is `Define P6 replay schema and synthetic fixture
    implementation proposal boundary before code.`
- Evidence grade:
  - P6 replay schema and fixture implementation readiness checklist review
    evidence only.
- Updated `02A`, `02B`, `02F`, `02H`, handoff, docs index, stage contract,
  milestones, backlog, technical plan, evidence log, risk register, decision
  record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.41

- Defined the P6 replay schema and fixture implementation readiness checklist
  before code.
- Added
  `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`.
- The checklist records:
  - candidate implementation classes for replay schema code, synthetic/local
    fixture files, schema/fixture validation tests, parsers, dataset readers,
    feature extraction, label generation, data ingestion, real/external source
    integration, CLI / broad ingestion, model-output integration and later-stage
    work.
  - replay schema code readiness criteria.
  - synthetic/local replay fixture readiness criteria.
  - parser / dataset reader readiness criteria.
  - feature extraction / label generation readiness criteria.
  - data-ingestion readiness criteria.
  - readiness decision vocabulary.
  - cross-artifact dependency map.
  - P7-P12 non-entry boundary.
  - readiness risks.
- Decision:
  - the readiness checklist is defined for review before code.
  - no candidate implementation class is approved by the checklist definition.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - replay fixture implementation remains closed.
  - data ingestion, dataset readers, parsers, feature extraction and label
    generation remain closed.
  - the next task is `Review P6 replay schema and fixture implementation
    readiness checklist before code.`
- Evidence grade:
  - P6 replay schema and fixture implementation readiness checklist definition
    evidence only.
- Updated `02A`, `02B`, `02F`, handoff, docs index, stage contract,
  milestones, backlog, technical plan, evidence log, risk register, decision
  record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.40

- Reviewed the P6 synthetic/local replay fixture boundary before schema
  implementation.
- Added
  `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`.
- The review confirms:
  - `02F` scope is correct.
  - allowed fixture boundary is sufficient.
  - forbidden fixture boundary is strict enough.
  - source-inventory dependency on `02A` / `02D` is clear.
  - replay-schema boundary dependency on `02B` / `02E` is clear.
  - future fixture shape families are sufficient and safe as documentation
    boundaries only.
  - future implementation entry criteria and validation expectations are
    sufficient.
  - synthetic/local fixture risks and governance synchronization have no
    blocker.
- Decision:
  - review can close.
  - fixture implementation remains unapproved.
  - replay schema implementation remains unapproved.
  - P6 implementation remains closed.
  - data ingestion, dataset readers, parsers, feature extraction and label
    generation remain closed.
  - the next task is `Define P6 replay schema and fixture implementation
    readiness checklist before code.`
- Evidence grade:
  - P6 synthetic/local replay fixture boundary review evidence only.
- Updated `02A`, `02B`, `02F`, handoff, docs index, stage contract,
  milestones, backlog, technical plan, evidence log, risk register, decision
  record and `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.39

- Defined the P6 synthetic/local replay fixture boundary before schema
  implementation.
- Added
  `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`.
- The document records:
  - fixture boundary purpose.
  - allowed project-authored / repo-local / small smoke-only fixture boundary.
  - forbidden real Tenhou, real haifu, external-log, platform-data, model-output,
    training, self-play, league and P7-P12 fixture interpretations.
  - source-inventory dependency on `02A` / `02D`.
  - replay-schema boundary dependency on `02B` / `02E`.
  - future fixture shape families.
  - future fixture implementation entry criteria.
  - future validation expectations.
  - synthetic/local fixture risks.
  - planning decision and next-task recommendation.
- Decision:
  - P6 synthetic/local replay fixture boundary is defined for review.
  - fixture implementation remains unapproved.
  - replay schema implementation remains unapproved.
  - P6 implementation remains closed.
  - data ingestion, dataset readers, feature extraction and label generation
    remain closed.
  - the next task is `Review P6 synthetic/local replay fixture boundary before
    schema implementation.`
- Evidence grade:
  - P6 synthetic/local replay fixture boundary definition evidence only.
- Updated `02A`, `02B`, handoff, docs index, stage contract, milestones,
  backlog, technical plan, evidence log, risk register, decision record and
  `10_NEXT`.
- No production code, tests, fixtures, synthetic replay fixture, replay schema
  code, dataclass / pydantic / JSON schema, parser, dataset reader, feature
  extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.38

- Reviewed the P6 replay schema documentation boundary before implementation.
- Added
  `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`.
- The review confirms:
  - `02B` scope is correct for P6 replay schema documentation boundary review.
  - allowed documentation scope is sufficient.
  - forbidden implementation, ingestion, real-data and later-stage scope is
    strict enough.
  - source inventory dependencies on `02A` / `02D` are clear.
  - replay field-family draft is sufficient and safe as documentation-boundary
    planning only.
  - validation expectations and future implementation entry criteria are
    sufficient to prevent premature implementation.
  - replay-schema risks and governance synchronization have no blocker.
- Decision:
  - review can close.
  - replay schema implementation remains closed.
  - P6 implementation remains closed.
  - data ingestion, dataset readers, feature extraction and label generation
    remain closed.
  - the next task is `Define P6 synthetic/local replay fixture boundary before
    schema implementation.`
- Evidence grade:
  - P6 replay schema documentation boundary review evidence only.
- Updated `02B`, handoff, docs index, stage contract, milestones, backlog,
  technical plan, evidence log, risk register, decision record and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, dataclass /
  pydantic / JSON schema, parser, dataset reader, feature extraction, label
  generation, data ingestion, CLI, broad ingestion, model-output integration,
  real Tenhou, real haifu, external-log ingestion, platform-data ingestion,
  third-party binary call, training, tuning, self-play, league, runner
  behavior, P7-P12 work or model-strength claim was added.

## 2026-06-06 — v2.37

- Defined the P6 replay schema documentation boundary after source inventory
  review.
- Updated `docs/02_data_system/02B_REPLAY_SCHEMA.md` from a placeholder into a
  docs-only boundary document.
- The document records:
  - allowed replay schema documentation scope.
  - forbidden implementation, ingestion and real-data scope.
  - source-inventory dependencies.
  - replay field-family draft.
  - validation expectations before future implementation.
  - future implementation entry criteria.
  - replay-schema risks.
  - planning decision and next-task recommendation.
- Decision:
  - P6 replay schema documentation boundary is defined for review.
  - replay schema implementation remains unapproved.
  - P6 implementation remains closed.
  - data ingestion, feature extraction and label generation remain closed.
  - the next task is `Review P6 replay schema documentation boundary before
    implementation.`
- Evidence grade:
  - P6 replay schema documentation boundary definition evidence only.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register, decision record and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, dataset reader,
  feature extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-06 — v2.36

- Reviewed the P6 data-source provenance and rights inventory before replay
  schema implementation.
- Added
  `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`.
- The review confirms:
  - `02A` scope is documentation-only and pre-ingestion.
  - the inventory field schema is sufficient as a future source-record
    boundary.
  - the approval-status vocabulary is conservative.
  - project-authored synthetic/local fixtures and repository docs remain
    limited to their current docs/smoke/review contexts.
  - real Tenhou, real haifu, external logs, platform data, accounts,
    third-party binaries, unknown weights, model outputs, self-play outputs
    and league outputs remain unapproved or blocked.
  - the required-before-ingestion checklist and future evidence requirements
    are sufficient for the current pre-schema review gate.
  - no rights/provenance blocker was found.
- Decision:
  - the P6 source inventory review can close.
  - P6 implementation remains closed.
  - replay schema implementation remains closed.
  - data ingestion remains closed.
  - the next task is `Define P6 replay schema documentation boundary after
    source inventory review.`
- Evidence grade:
  - P6 data-source provenance and rights inventory review evidence only.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register, decision record and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, dataset reader,
  feature extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-05 — v2.35

- Defined P6 data-source provenance and rights inventory before replay schema
  implementation.
- Updated `docs/02_data_system/02A_DATA_SOURCES.md` from a placeholder source
  table into the P6 source inventory control document.
- The document records:
  - inventory field schema.
  - approval-status vocabulary.
  - source-category inventory.
  - required-before-ingestion checklist.
  - future source evidence requirements.
  - rights / provenance risk review.
  - replay schema implementation boundary.
  - planning decision and next task recommendation.
- Decision:
  - P6 data-source provenance and rights inventory is defined for review.
  - P6 implementation remains closed.
  - the next task is `Review P6 data-source provenance and rights inventory
    before replay schema implementation.`
- Evidence grade:
  - P6 data-source provenance and rights inventory definition evidence only.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register, decision record and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, dataset reader,
  feature extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-05 — v2.34

- Defined P6 data-system scope, entry criteria and first task before
  implementation.
- Added
  `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`.
- The document records:
  - P6 purpose and north-star relationship.
  - allowed and forbidden P6 planning scope.
  - allowed and forbidden future inputs.
  - P6 docs-only entry criteria.
  - future P6 implementation entry criteria.
  - future P6 exit criteria.
  - provenance, rights and compliance requirements.
  - evidence requirements.
  - risk review.
  - P7-P12 non-entry boundaries.
  - first next task candidate.
- Decision:
  - P6 data-system scope is defined for planning only.
  - P6 implementation remains closed.
  - the next task is `Define P6 data-source provenance and rights inventory
    before replay schema implementation.`
- Evidence grade:
  - P6 data-system scope definition evidence only.
- Updated handoff, docs index, stage contract, milestones, backlog, technical
  plan, evidence log, risk register, decision record and `10_NEXT`.
- No production code, tests, fixtures, replay schema code, dataset reader,
  feature extraction, label generation, data ingestion, CLI, broad ingestion,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, third-party binary call, training, tuning,
  self-play, league, runner behavior, P7-P12 work or model-strength claim was
  added.

## 2026-06-04 — v2.33

- Completed the post-P5 transition review.
- Added `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`.
- Transition decision:
  - P5 remains closed for the current synthetic/local evaluation groundwork
    scope.
  - P5 closure is not P6 implementation approval.
  - the project may start a docs-only task to define P6 data-system scope,
    entry criteria and first task before implementation.
- The review records:
  - transition-review goal, inputs, output boundary and forbidden scope.
  - P6 candidate scope is data system, but implementation is not approved.
  - the next task must define P6 scope / entry criteria / first task before any
    replay schema code, data ingestion or pipeline work.
- Evidence grade:
  - post-P5 transition review evidence only.
- Updated handoff, docs index, stage contract, backlog, technical plan,
  evidence log, risk register, decision record and `10_NEXT`.
- Set the next task to `Define P6 data-system scope, entry criteria and first
  task before implementation.`
- No production code, tests, fixtures, replay schema code, dataset reader,
  feature extraction, label generation, CLI, broad ingestion, model-output
  integration, real Tenhou, real haifu, external-log ingestion, platform-data
  ingestion, third-party binary call, training, tuning, self-play, league,
  runner behavior, P7-P12 work or model-strength claim was added.

## 2026-06-04 — v2.32

- Ran the final P5 closure review gate.
- Added `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`.
- Closure decision:
  - P5 can close.
  - P5 is closed for the current synthetic/local evaluation groundwork scope.
  - no closure blocker was found.
- The review records:
  - all closure criteria pass.
  - current-scope P5 subtracks are complete for synthetic/local evaluation
    groundwork.
  - the P5 evidence index is sufficient for the closure decision.
  - required remaining P5 items narrowed to closure decision recording.
  - deferred later-stage items do not block P5 closure.
  - P6-P12 non-entry conditions remain active.
- Evidence grade:
  - P5 final closure review evidence only.
- Updated handoff, docs index, stage contract, backlog, technical plan,
  evidence log, risk register and `10_NEXT`.
- Set the next task to `Await separate post-P5 transition review before
  defining any P6 task.`
- P5 closure is not P6-P12 entry approval and does not approve P6 first task,
  P6 data-system work, production evaluator expansion, metric implementation,
  registry code changes, promotion criteria changes, CLI, broad ingestion,
  latency measurement, fixed-position exact-match computation, model-output
  integration, legal-action checker, canonicalizer, broad evaluator, league,
  runner, training, tuning, self-play, Tenhou connection, external-data reader
  or model-strength claims.

## 2026-06-04 — v2.31

- Finalized the P5 handoff and evidence index before final closure review.
- Added
  `docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md`.
- Finalization contents:
  - finalization-ready P5 handoff summary.
  - P5 evidence index across stable-dan, offline envelope, legal-action, tiny
    benchmark, cross-cutting reviews and governance artifacts.
  - required remaining P5 items.
  - deferred item table.
  - governance synchronization summary.
- Assessment:
  - P5 handoff and evidence index are finalized for final closure review.
  - P5 remains open until the final closure review gate.
  - no finalization blocker was found.
  - P5 must not enter P6-P12 yet.
- Evidence grade:
  - P5 handoff and evidence index finalization evidence only.
- Updated handoff, docs index, stage contract, backlog, technical plan,
  evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Run final P5 closure review gate.`
- No P5 closure, P6-P12 entry approval, production code, tests, fixtures,
  metric implementation, registry code changes, evidence taxonomy definition
  changes, promotion criteria changes, CLI, broad ingestion, latency
  measurement, fixed-position exact-match computation, model-output
  integration, legal-action checker, canonicalizer, broad evaluator, league,
  runner, training, tuning, self-play, Tenhou connection or external-data
  reader was added.

## 2026-06-04 — v2.30

- Reviewed P5 evaluation groundwork closure criteria and the exit readiness
  checklist.
- Added
  `docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md`.
- Review findings:
  - `05U` scope is correct.
  - current P5 subtrack inventory is complete enough for finalization.
  - P5 closure criteria are sufficient.
  - the exit readiness checklist is executable.
  - required remaining P5 items are correctly limited to review/finalization.
  - deferred items are correctly classified.
  - P6-P12 non-entry conditions are sufficient.
  - no closure-criteria blocker was found.
- Review conclusion:
  - closure criteria review can close.
  - P5 remains open pending final P5 handoff/evidence index finalization and a
    later final closure review.
  - P5 must not enter P6-P12 yet.
- Evidence grade:
  - P5 evaluation groundwork closure criteria and exit readiness review
    evidence only.
- Updated handoff, docs index, stage contract, backlog, technical plan,
  evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Finalize P5 handoff and evidence index before
  final closure review.`
- No P5 closure, P6-P12 entry approval, production code, tests, fixtures,
  metric implementation, registry code changes, evidence taxonomy definition
  changes, promotion criteria changes, CLI, broad ingestion, latency
  measurement, fixed-position exact-match computation, model-output
  integration, legal-action checker, canonicalizer, broad evaluator, league,
  runner, training, tuning, self-play, Tenhou connection or external-data
  reader was added.

## 2026-06-04 — v2.29

- Defined P5 evaluation groundwork closure criteria and an exit readiness
  checklist.
- Added
  `docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md`.
- The specification records:
  - current P5 scope.
  - current-scope complete, near-complete and incomplete subtracks.
  - minimum P5 closure criteria.
  - exit readiness checklist.
  - required remaining P5 items.
  - deferred items and non-entry conditions for P6-P12.
- Assessment:
  - P5 closure criteria are defined, but P5 remains open until reviewed.
  - P5 is near closure.
  - P5 must not enter P6-P12 yet.
- Evidence grade:
  - P5 evaluation groundwork closure criteria and exit readiness specification
    evidence only.
- Updated handoff, docs index, stage contract, backlog, technical plan,
  evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Review P5 evaluation groundwork closure
  criteria and exit readiness checklist.`
- No P5 closure, P6-P12 entry approval, production code, tests, fixtures,
  metric implementation, registry code changes, evidence taxonomy definition
  changes, promotion criteria changes, CLI, broad ingestion, latency
  measurement, fixed-position exact-match computation, model-output
  integration, legal-action checker, canonicalizer, broad evaluator, league,
  runner, training, tuning, self-play, Tenhou connection or external-data
  reader was added.

## 2026-06-04 — v2.28

- Reviewed P5 synthetic/local evaluation evidence taxonomy and promotion
  guardrails.
- Added
  `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md`.
- The review records that current evidence labels, non-evidence warnings,
  promotion/ranking guardrails, LuckyJ / Tenhou / stable-dan claim boundaries
  and stage-boundary wording are consistent across the current P5 stable-dan,
  legal-action, tiny benchmark, offline envelope and metric registry artifacts.
- No blocker was found.
- Evidence grade:
  - P5 synthetic/local evidence taxonomy and promotion guardrails review
    evidence only.
- Follow-up:
  - P5 has many completed subtracks and should not continue indefinitely
    through more schema/review churn.
  - The next P5-only task is to define evaluation groundwork closure criteria
    and an exit readiness checklist.
- Updated handoff, docs index, 05F, 05J, 05S, stage contract, backlog,
  technical plan, evidence log, risk register and `10_NEXT`.
- No production code, tests, fixtures, metric implementation, registry code
  changes, evidence taxonomy definition changes, promotion criteria changes,
  CLI, broad ingestion, latency measurement, fixed-position exact-match
  computation, model-output integration, legal-action checker, canonicalizer,
  broad evaluator, league, runner, training, tuning, self-play, Tenhou
  connection, external-data reader or P6-P12 work was added.

## 2026-05-30 — v2.27

- Reviewed P5 metric registry consistency across stable-dan, legal-action and
  tiny benchmark diagnostics.
- Added `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md`.
- The review records that current registry names, units, directions, current
  statuses/source notes and evidence grades are consistent for the current P5
  scope across:
  - stable-dan synthetic report metrics.
  - synthetic legal-action count/rate metrics.
  - synthetic tiny benchmark diagnostic metric `wrapper_smoke_success`.
- No blocker was found.
- Non-blocking follow-up:
  - tiny benchmark fixture names such as latency percentiles and
    fixed-position exact-match remain future planning names, not current
    registered/emitted metrics.
- Evidence grade:
  - P5 synthetic/local metric registry consistency review evidence only.
- Updated handoff, docs index, 05F, 05J, 05R, stage contract, backlog,
  technical plan, evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Review P5 synthetic/local evaluation evidence
  taxonomy and promotion guardrails.`
- No production code, tests, fixtures, metric implementation, registry code
  changes, CLI, broad ingestion, latency measurement, fixed-position exact-match
  computation, model-output integration, legal-action checker, canonicalizer,
  broad evaluator, league, runner, training, tuning, self-play, Tenhou
  connection, external-data reader or P6-P12 work was added.

## 2026-05-30 — v2.26

- Reviewed the P5 offline evaluation result envelope coverage for synthetic tiny
  benchmark diagnostics.
- Added
  `docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md`.
- The review records that the current `OfflineEvaluationResultEnvelope` coverage
  is sufficient for the current project-authored synthetic/local tiny benchmark
  diagnostic scope:
  - `evaluation_type = "tiny_benchmark_harness"`.
  - `wrapper_smoke_success = true`.
  - `sample_size = 1`.
  - `latency_ms = None`.
  - all safety flags false.
  - synthetic/local warnings.
  - evidence references to the fixture, tests and P5 boundary/review docs.
- No blocker was found for representing the current tiny benchmark diagnostic in
  the offline envelope.
- Evidence grade:
  - P5 synthetic/local offline envelope coverage review evidence only.
- Updated handoff, docs index, 05F, 05J, 05P, 05Q, stage contract, backlog,
  technical plan, evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Review P5 metric registry consistency across
  stable-dan, legal-action and tiny benchmark diagnostics.`
- No production code, tests, fixtures, envelope schema code, metric registry
  code, CLI, broad ingestion, latency measurement, fixed-position exact-match
  computation, model-output integration, legal-action checker, canonicalizer,
  broad evaluator, league, runner, training, tuning, self-play, Tenhou
  connection, external-data reader or P6-P12 work was added.

## 2026-05-30 — v2.25

- Reviewed the P5 tiny benchmark harness implementation.
- Added `docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md`.
- The review records that:
  - the harness loads only the fixed project-authored synthetic/local fixture.
  - `run_project_tiny_benchmark_harness()` has no arbitrary path parameter.
  - no CLI, directory scan, glob, broad file ingestion, model-output path, real
    Tenhou / real haifu / external-log / platform-data path, third-party binary
    call or model/API call was found.
  - the envelope remains P5-only with `evaluation_type =
    "tiny_benchmark_harness"`, `wrapper_smoke_success = true`, `sample_size =
    1`, all safety flags false and `latency_ms = None`.
  - tests cover fixed fixture loading, deterministic result, no arbitrary path,
    envelope fields, all-false safety flags, measured-latency rejection and
    JSON serialization.
- Review conclusion:
  - current implementation can close for the project-authored synthetic/local
    fixture scope.
  - no blocker was found.
- Evidence grade:
  - P5 synthetic/local tiny benchmark harness implementation review evidence
    only.
- Updated handoff, docs index, stage contract, backlog, technical plan,
  evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Review P5 offline evaluation result envelope
  coverage for synthetic tiny benchmark diagnostics.`
- No production code, tests, fixtures, CLI, broad ingestion, latency measurement,
  fixed-position exact-match computation, model-output integration, legal-action
  checker, canonicalizer, broad evaluator, league, runner, training, tuning,
  self-play, Tenhou connection, external-data reader or P6-P12 work was added.

## 2026-05-30 — v2.24

- Implemented the P5 tiny benchmark harness for the project-authored synthetic
  fixture only.
- Added `src/mjlabai/eval/tiny_benchmark_harness.py`.
- Added exports in `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_tiny_benchmark_harness.py`.
- Added `docs/05_evaluation/05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION.md`.
- The harness:
  - loads only `tests/fixtures/eval/tiny_benchmark_harness_smoke.json`.
  - validates and summarizes legal-action diagnostic shape, latency plan shape
    and fixed-position synthetic record shape.
  - records deterministic `smoke_success = true` and
    `fixed_position_record_count = 1`.
  - can wrap the result in `OfflineEvaluationResultEnvelope` with
    `evaluation_type = "tiny_benchmark_harness"`,
    `wrapper_smoke_success = true`, `sample_size = 1`, all safety flags false
    and synthetic/local warnings.
- The harness does not measure latency, calculate legal-action metrics inside
  the harness, compute fixed-position exact-match, connect model output, add
  CLI/file ingestion, read real Tenhou / real haifu / external logs / platform
  data, call third-party binaries, train, tune, self-play, run league/runner
  behavior or enter P6-P12.
- Evidence grade remains P5 synthetic/local engineering diagnostic evidence
  only, not model-strength, Tenhou, stable-dan, LuckyJ `10.68`, policy-quality
  or candidate-promotion evidence.
- Updated handoff, docs index, 05J, 05N, 05O, stage contract, backlog,
  technical plan, evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Review P5 tiny benchmark harness
  implementation and define next P5-only evaluation task.`

## 2026-05-30 — v2.23

- Reviewed the P5 tiny benchmark harness synthetic fixture schema smoke coverage.
- Added `docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md`.
- The review records that:
  - `tests/fixtures/eval/tiny_benchmark_harness_smoke.json` satisfies the current P5 synthetic/local input boundary.
  - `tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py` validates shape, guardrails, all-false safety flags and future diagnostic metric names only.
  - the fixture schema is sufficient as a front-door input boundary for a future P5-only tiny benchmark harness implementation task.
- The review preserves the evidence grade:
  - P5 synthetic/local fixture schema smoke evidence only.
- The review states this is not benchmark harness implementation, latency measurement, legal-action metric computation, fixed-position exact-match computation, model-output integration, model-strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.
- Updated handoff, docs index, 05F, 05J, 05K, 05L, 05M, 05N, stage contract, backlog, technical plan, evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Implement P5 tiny benchmark harness for project-authored synthetic fixture only.`
- No production code, tests, fixtures, benchmark harness implementation, latency measurement code, evaluator logic changes, canonicalizer, broad evaluator, legal-action checker, CLI, file ingestion, league, runner, model-output path, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_metric.py`: 6 tests passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 16 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.

## 2026-05-30 — v2.22

- Added the P5 tiny benchmark harness synthetic fixture schema smoke test.
- Added `tests/fixtures/eval/tiny_benchmark_harness_smoke.json`.
- Added `tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py`.
- The fixture is project-authored synthetic/local only and records:
  - legal-action diagnostic input shape.
  - latency diagnostic plan shape.
  - fixed-position synthetic decision diagnostic shape.
  - all-false intended safety flags.
  - warnings that the fixture is not Tenhou data, not a real haifu, not an external log, not model output, not model-strength evidence, not LuckyJ `10.68` comparison and not candidate-promotion evidence.
- The schema smoke test validates fixture shape, safety flags, warnings, future diagnostic metric names, the synthetic legal-action fixture reference, latency plan fields and strict `dahai` fixed-position action shape.
- The schema smoke test does not implement a benchmark harness, calculate legal-action metrics, measure latency, calculate fixed-position exact-match, call model code, call evaluator code, add CLI/file ingestion or read real Tenhou / real haifu / external logs / platform data.
- Updated handoff, docs index, 05F, 05J, 05K, 05L, 05N, stage contract, backlog, technical plan, evidence log, risk register and `10_NEXT`.
- Set the next P5-only task to `Review P5 tiny benchmark harness synthetic fixture schema smoke coverage and define next P5-only task.`
- No production code, benchmark harness implementation, latency measurement code, evaluator logic changes, canonicalizer, broad evaluator, legal-action checker, CLI, file ingestion, league, runner, model-output path, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_metric.py`: 6 tests passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 16 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.

## 2026-05-30 — v2.21

- Defined the P5 tiny benchmark harness boundary before implementation.
- Added `docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md`.
- The boundary allows only future synthetic/local diagnostic inputs:
  - project-authored synthetic fixtures.
  - repo-local synthetic/local fixtures.
  - in-memory fixture mappings.
  - fixed synthetic decision records.
- The boundary forbids real Tenhou, real haifu, external logs, platform data,
  online accounts, platform automation, third-party binaries, Akochan
  `system.exe`, `libai.so`, unknown model weights, model-output integration,
  training, tuning, self-play, league, runner, CLI, broad file ingestion and
  P6-P12 work.
- Future diagnostic metric categories are limited to legal-action rate,
  latency and fixed-position decision diagnostics. They are not strength
  evidence, Tenhou ranked evidence, stable-dan evidence, policy-quality
  evidence, candidate-promotion evidence or LuckyJ `10.68` comparison.
- Added cross-references from:
  - `docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md`.
  - `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`.
  - `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`.
  - `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`.
  - `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`.
- Updated handoff, docs index, stage contract, backlog, technical plan and
  `10_NEXT`.
- Set the next P5-only task to `Add P5 tiny benchmark harness synthetic fixture
  schema smoke test.`
- No production code, tests, fixtures, evaluator logic, canonicalizer, broad
  evaluator, legal-action checker, benchmark harness implementation, CLI, file
  ingestion, league, runner, model-output path, training, tuning, self-play,
  Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`:
    1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_metric.py`: 6 tests
    passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 16 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test
    passed.

## 2026-05-30 — v2.20

- Reviewed the P5 legal-action synthetic evaluator coverage.
- Added `docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md`.
- The review records that current minimum outcome coverage is complete only for the P5 synthetic-only `dahai` + strict scope:
  - `legal`.
  - `invalid`.
  - `missing_action`.
  - `parse_failure`.
  - `skipped_no_legal_actions`.
- Current fixture counts/rates remain:
  - `total_record_count = 5`.
  - `evaluated_decision_count = 4`.
  - `legal_action_count = 1`.
  - `invalid_action_count = 1`.
  - `missing_action_count = 1`.
  - `parse_failure_count = 1`.
  - `skipped_count = 1`.
  - `legal_action_rate = 1/4`.
  - `invalid_action_rate = 1/4`.
  - `missing_action_rate = 1/4`.
  - `parse_failure_rate = 1/4`.
- Updated `docs/00_DOCS_INDEX.md` to include the review document.
- Added cross-references from:
  - `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`.
  - `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`.
  - `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`.
  - `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`.
- Updated handoff, stage contract, backlog, technical plan and `10_NEXT`.
- Set the next P5-only task to `Define P5 tiny benchmark harness boundary for legal-action rate, latency and fixed-position decisions before implementation.`
- No production code, evaluator logic, canonicalizer, broad evaluator, legal-action checker, CLI, benchmark harness implementation, file ingestion, league, runner, model code, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_metric.py`: 6 tests passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 16 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.

## 2026-05-30 — v2.19

- Added explicit P5 synthetic parse-failure coverage to the project-authored legal-action metric fixture.
- Updated `tests/fixtures/eval/legal_action_metric_smoke.json` with a fifth synthetic record:
  - `expected_future_outcome = "parse_failure"`.
  - `proposed_action` remains in the current `dahai` fixture shape.
  - `proposed_action.tsumogiri = null` intentionally exercises the strict evaluator parse-failure branch.
  - `legal_actions` remains a non-empty valid strict `dahai` action list.
- Updated `tests/eval/test_legal_action_fixture_schema_smoke.py` so schema smoke coverage includes:
  - `legal`.
  - `invalid`.
  - `missing_action`.
  - `parse_failure`.
  - `skipped_no_legal_actions`.
- Updated `tests/eval/test_legal_action_metric.py` expected project-fixture counts and envelope metrics:
  - `total_record_count = 5`.
  - `legal_action_count = 1`.
  - `invalid_action_count = 1`.
  - `missing_action_count = 1`.
  - `parse_failure_count = 1`.
  - `skipped_count = 1`.
  - `evaluated_decision_count = 4`.
  - `legal_action_rate = 1/4`.
  - `invalid_action_rate = 1/4`.
  - `missing_action_rate = 1/4`.
  - `parse_failure_rate = 1/4`.
- Updated P5 docs and governance records to state that the parse-failure case is branch coverage only:
  - not an expansion beyond `dahai` + strict matching.
  - not support for unknown/null `tsumogiri` in canonical matching.
  - not model-strength evidence.
  - not Tenhou evidence.
  - not a LuckyJ 10.68 comparison.
- No canonicalizer, broad evaluator, legal-action checker, CLI, file ingestion, league, runner, model code, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_metric.py`: 6 tests passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 16 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.
- Set the next P5-only task to `Review P5 legal-action synthetic evaluator coverage and define next P5-only evaluation task.`

## 2026-05-29 — v2.18

- Implemented the P5 synthetic legal-action metric evaluator for the project-authored fixture only.
- Added `src/mjlabai/eval/legal_action_metric.py`.
- Added exports in `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_legal_action_metric.py`.
- Updated `src/mjlabai/eval/offline_result.py` registry definitions for implemented synthetic legal-action count/rate metrics:
  - `evaluated_decision_count`.
  - `legal_action_count`.
  - `invalid_action_count`.
  - `missing_action_count`.
  - `parse_failure_count`.
  - `skipped_count`.
  - `missing_action_rate`.
  - `parse_failure_rate`.
- The evaluator accepts an in-memory fixture mapping only; it does not add CLI or file-ingestion support.
- Current supported scope remains:
  - project-authored synthetic fixture only.
  - strict `dahai` matching only.
  - actor/action_type/tile/tsumogiri comparison only.
  - `raw_action`, metadata and `action_id` ignored for equality.
- Current fixture result:
  - `legal_action_count = 1`.
  - `invalid_action_count = 1`.
  - `missing_action_count = 1`.
  - `parse_failure_count = 0`.
  - `skipped_count = 1`.
  - `evaluated_decision_count = 3`.
  - `legal_action_rate = 1/3`.
  - `invalid_action_rate = 1/3`.
  - `missing_action_rate = 1/3`.
  - `parse_failure_rate = 0.0`.
- Added envelope helper `build_synthetic_legal_action_metric_envelope(...)` with all-false safety flags and synthetic-only warnings.
- Added decision record `DR-0025`.
- Tests confirm `expected_future_outcome` labels are not used for computation.
- No broad evaluator, canonicalizer, legal-action checker, CLI, file ingestion, league, runner, model code, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_legal_action_metric.py`: 6 tests passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 16 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.
- Set the next P5-only task to `Add P5 synthetic parse-failure legal-action fixture case and evaluator smoke coverage.`

## 2026-05-29 — v2.17

- Defined the P5 legal-action metric synthetic evaluator boundary before implementation.
- Updated `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md` with a new boundary section.
- Added decision record `DR-0024`.
- Added cross-references from:
  - `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`.
  - `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`.
  - `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`.
- Boundary allows only:
  - project-authored synthetic/local fixtures.
  - default fixture `tests/fixtures/eval/legal_action_metric_smoke.json`.
  - P5 offline evaluation context.
  - current `dahai` scope.
  - current strict matching mode.
- Boundary forbids:
  - real Tenhou data.
  - real haifu.
  - platform data.
  - online accounts.
  - external logs.
  - Akochan real executable or third-party binaries.
  - model output, model inference, model training or model weights.
  - self-play, league, match runner or Tenhou connector.
- Recorded minimum future count/rate boundary:
  - `legal_action_count`.
  - `invalid_action_count`.
  - `missing_action_count`.
  - `parse_failure_count`.
  - `skipped_count`.
  - `evaluated_decision_count`.
  - `legal_action_rate`.
  - `invalid_action_rate`.
  - `missing_action_rate`.
  - `parse_failure_rate`.
- Recorded invariant:
  - `evaluated_decision_count = legal_action_count + invalid_action_count + parse_failure_count + missing_action_count`.
- Recorded that `expected_future_outcome` labels are not evaluator output, model predictions, strength evidence or LuckyJ comparison evidence.
- No evaluator, canonicalizer, legal-action checker, production code, CLI, file ingestion, league harness, match runner, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_offline_result.py`: 15 tests passed.
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.
- Set the next P5-only task to `Implement P5 synthetic legal-action metric evaluator for project-authored fixture only.`

## 2026-05-29 — v2.16

- Added a synthetic legal-action metric fixture schema smoke test.
- Added `tests/fixtures/eval/legal_action_metric_smoke.json`.
- Added `tests/eval/test_legal_action_fixture_schema_smoke.py`.
- Fixture labels cover future outcome examples:
  - `legal`.
  - `invalid`.
  - `missing_action`.
  - `skipped_no_legal_actions`.
- The fixture is project-authored synthetic-only data:
  - not Tenhou data.
  - not a real haifu.
  - not an external log.
  - not model output.
  - not model-strength evidence.
- The smoke test validates:
  - fixture top-level schema fields.
  - strict matching mode.
  - record-level required fields.
  - actor range.
  - canonical `dahai` action shape.
  - `raw_action` preservation.
  - source-note guardrails.
  - required future outcome labels.
- The smoke test does not calculate `legal_action_rate` or `invalid_action_rate`.
- No canonical equality, canonicalizer, evaluator, legal-action checker, Python production schema, CLI, league harness, match runner, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py`: 1 test passed.
  - `git diff --check`: passed.
- Set the next P5-only task to `Define P5 legal-action metric synthetic evaluator boundary before implementation.`

## 2026-05-29 — v2.15

- Defined the P5 action canonicalization schema for legal-action metric fixtures.
- Added `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`.
- Updated `docs/00_DOCS_INDEX.md` to include the new schema document.
- Defined canonical action fields:
  - `schema_version`.
  - `action_id`.
  - `actor`.
  - `action_type`.
  - `tile`.
  - `tsumogiri`.
  - `called_tile`.
  - `consumed_tiles`.
  - `target`.
  - `source`.
  - `reach_declared`.
  - `kan_type`.
  - `raw_action`.
  - `metadata`.
- Recorded current minimum fixture scope:
  - `current_minimum_supported_action_type = dahai`.
- Defined strict `dahai` matching:
  - actor must match.
  - action type must match.
  - tile must match.
  - known `tsumogiri` must match.
  - unknown/null `tsumogiri` must not be guessed.
  - `raw_action` and `metadata` are ignored for equality.
- Documented future `relaxed_discard_tile` mode as a non-default, not-yet-implemented mode that must be recorded in result envelopes if ever used.
- Defined minimum legal-action fixture shape for `proposed_action` and `legal_actions`.
- Recorded edge cases for reach, chi/pon, kan, hora/ryukyoku, red fives and tile notation mismatch.
- No canonicalizer, evaluator, legal-action checker, Python schema/dataclass, CLI, league harness, match runner, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
- Set the next P5-only task to `Add synthetic legal-action metric fixture schema smoke test.`

## 2026-05-29 — v2.14

- Defined the P5 legal-action and invalid-action metric specification.
- Added `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`.
- Updated `docs/00_DOCS_INDEX.md` to include the new specification.
- Defined core decision-record terminology:
  - `decision_id`.
  - actor.
  - observation / state reference.
  - `legal_actions`.
  - `proposed_action`.
  - model/tool id.
  - ruleset, room and context metadata.
- Defined denominator and count rules:
  - `evaluated_decision_count`.
  - `legal_action_count`.
  - `invalid_action_count`.
  - `parse_failure_count`.
  - `missing_action_count`.
  - `skipped_count`.
- Defined rates for legal actions, invalid actions, parse failures and missing actions.
- Recorded that `evaluated_decision_count == 0` makes rates undefined and must not produce fabricated `0` or `1` values.
- Defined recommended outcome categories:
  - `legal`.
  - `invalid`.
  - `parse_failure`.
  - `missing_action`.
  - `skipped_no_legal_actions`.
  - `skipped_not_decision`.
  - `skipped_actor_mismatch`.
  - `skipped_not_evaluable`.
- Documented canonical matching principles for `dahai`, reach, chi/pon/kan and future hora/ryukyoku handling.
- Documented result-envelope mapping for future legal-action metrics.
- No evaluator, legal-action checker, canonicalizer implementation, CLI, league harness, match runner, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Validation:
  - `git diff --check`: passed.
- Set the next P5-only task to `Define P5 action canonicalization schema for legal-action metric fixtures.`

## 2026-05-29 — v2.13

- Added offline evaluation envelope smoke fixture for a synthetic stable-dan report.
- Added `tests/eval/test_offline_envelope_smoke.py`.
- The smoke test starts from `tests/fixtures/eval/stable_dan_placements_smoke.json`.
- The smoke chain covers:
  - `aggregate_placement_records(...)`.
  - `bootstrap_stable_dan_ci(...)`.
  - `compare_stable_dan_to_threshold(...)`.
  - `build_stable_dan_evaluation_report(...)`.
  - `OfflineEvaluationResultEnvelope(...)`.
  - `envelope.to_dict()`.
  - `json.dumps(...)`.
- The envelope includes stable-dan point estimate, CI lower/upper, threshold outcome and sample-size status metrics.
- The envelope records reproducibility metadata, all-false safety flags, synthetic / not-strength-evidence warnings and evidence references.
- No conversion helper was added; the smoke test constructs the envelope directly to keep scope minimal.
- No CLI, league harness, match runner, training, tuning, self-play, Tenhou connection, external-log reader or platform-data reader was added.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_offline_envelope_smoke.py`: 1 test passed.
- Set the next P5-only task to `Define P5 legal-action and invalid-action metric specification.`

## 2026-05-29 — v2.12

- Defined P5 offline evaluation metric registry and result envelope schema.
- Added `src/mjlabai/eval/offline_result.py`.
- Exported offline result schema APIs from `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_offline_result.py`.
- Added `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`.
- Registered metric names:
  - `stable_dan_point_estimate`
  - `stable_dan_ci_lower`
  - `stable_dan_ci_upper`
  - `stable_dan_threshold_outcome`
  - `stable_dan_sample_size_status`
  - `legal_action_rate`
  - `invalid_action_rate`
  - `command_exit_code`
  - `latency_ms`
  - `parse_success_rate`
  - `wrapper_smoke_success`
- Added schema dataclasses for metric values, confidence intervals, command status summaries, reproducibility metadata, safety flags and offline result envelopes.
- Confirmed the schema records results only; it does not run commands, read external data, train models, self-play, run league or connect to Tenhou.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_offline_result.py`: 15 tests passed.
- Set the next P5-only task to `Add offline evaluation envelope smoke fixture for synthetic stable-dan report.`

## 2026-05-29 — v2.11

- Reviewed P5 stable-dan evaluation groundwork completion.
- Added `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md`.
- Marked stable-dan evaluation groundwork as complete for the current P5 scope.
- Explicitly kept P5 overall open.
- Recorded current stable-dan completion basis:
  - deterministic stable-dan calculator.
  - bootstrap confidence interval.
  - LuckyJ `10.68` threshold comparison helper.
  - sample-size guardrails and report schema.
  - placement-count aggregation helper.
  - CLI-free synthetic smoke fixture.
  - stable-dan evaluation API documentation.
- Recorded current limits: no model-strength evidence, no real Tenhou ranked result, no real model game samples, no league harness, no replay parser, no real Tenhou data and no final LuckyJ proof.
- Set the next P5-only task to `Define P5 offline evaluation metric registry and result envelope schema.`
- No code, tests, CLI, file ingestion path, league harness, match runner, training, self-play, Tenhou connection or external-data reader was added.

## 2026-05-29 — v2.10

- Added stable-dan evaluation API documentation.
- Added `docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md`.
- Updated `docs/00_DOCS_INDEX.md` to include the new API document.
- Documented the synthetic fixture:
  - `tests/fixtures/eval/stable_dan_placements_smoke.json`.
  - 100 synthetic records with `first=30`, `second=30`, `third=20`, `fourth=20`.
  - Not Tenhou data, not real haifu, not external log and not model result.
- Documented the API-only flow:
  - `aggregate_placement_records(...)`.
  - `bootstrap_stable_dan_ci(...)`.
  - `compare_stable_dan_to_threshold(...)`.
  - `build_stable_dan_evaluation_report(...)`.
  - `StableDanEvaluationReport.to_dict()`.
- Documented key report fields and sample-size / threshold / claim guardrails.
- Clarified that the current report schema does not include `model_name`, `dataset_name`, `evaluation_context` or caller notes; those must remain outside the report until a future schema task extends it.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan_report_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_placement_counts.py`: 18 tests passed.
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- No code, CLI, file ingestion path, league harness, match runner, training, self-play, Tenhou connection or external-data reader was added.
- Set the next task to `Review P5 stable-dan evaluation groundwork completion and define the next P5-only evaluation task.`

## 2026-05-29 — v2.9

- Added CLI-free stable-dan evaluation report smoke fixture from placement inputs.
- Added `tests/fixtures/eval/stable_dan_placements_smoke.json`.
  - Project-authored synthetic fixture only.
  - 100 records: `first=30`, `second=30`, `third=20`, `fourth=20`.
  - Not Tenhou data, not an external haifu/log, not a league result and not a model result.
- Added `tests/eval/test_stable_dan_report_smoke.py`.
- Smoke path verifies:
  - `aggregate_placement_records(...)`.
  - deterministic phoenix stable dan point estimate `11.5`.
  - `bootstrap_stable_dan_ci(...)`.
  - `compare_stable_dan_to_threshold(...)`.
  - `build_stable_dan_evaluation_report(...)`.
  - `StableDanEvaluationReport.to_dict()` JSON serialization.
- The smoke report can be reported under current sample-size guardrails but cannot enter threshold review because `total_games=100` is below the project-internal threshold-review minimum of `1000`.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan_report_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_placement_counts.py`: 18 tests passed.
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- No CLI, file ingestion path, league harness, match runner, training, self-play, Tenhou connection or external-data reader was added.
- Set the next task to `Add stable-dan evaluation API documentation with example usage from synthetic placements.`

## 2026-05-29 — v2.8

- Added placement-count aggregation helper for stable-dan evaluation inputs.
- Added `src/mjlabai/eval/placement_counts.py` with:
  - `StableDanPlacementCounts`.
  - `aggregate_placement_counts(...)`.
  - `aggregate_placement_records(...)`.
  - `calculate_stable_dan_from_placements(...)`.
- Exported placement aggregation APIs from `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_placement_counts.py`.
- Supported placement inputs are only explicit `1`/`2`/`3`/`4` values and whitelisted aliases: `"1"`, `"2"`, `"3"`, `"4"`, `"first"`, `"second"`, `"third"`, `"fourth"`, `"1st"`, `"2nd"`, `"3rd"` and `"4th"`.
- Invalid, ambiguous, zero-based, bool, float and unknown placement inputs now fail explicitly instead of being silently normalized.
- `to_stable_dan_kwargs()` can feed the existing deterministic stable-dan calculator without reading files, running league code or touching Tenhou.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_placement_counts.py`: 18 tests passed.
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This remains offline evaluation input infrastructure only, not training, self-play, league execution, real Tenhou integration or model-strength evidence.
- Set the next task to `Add CLI-free stable-dan evaluation report smoke fixture from placement inputs.`

## 2026-05-29 — v2.7

- Added minimum sample-size guardrails and stable-dan evaluation report schema.
- Extended `src/mjlabai/eval/stable_dan.py` with:
  - `DEFAULT_MIN_TOTAL_GAMES_FOR_STABLE_DAN_REPORT = 100`.
  - `DEFAULT_MIN_FOURTH_COUNT_FOR_STABLE_DAN_REPORT = 10`.
  - `DEFAULT_MIN_TOTAL_GAMES_FOR_THRESHOLD_REVIEW = 1000`.
  - `DEFAULT_MIN_FOURTH_COUNT_FOR_THRESHOLD_REVIEW = 50`.
  - `DEFAULT_MAX_UNDEFINED_RATE_FOR_STABLE_DAN_REPORT = 0.05`.
  - `StableDanSampleSizeAssessment`.
  - `StableDanEvaluationReport`.
  - `assess_stable_dan_sample_size(...)`.
  - `build_stable_dan_evaluation_report(...)`.
- Report schema includes placement counts/rates, point estimate, bootstrap CI, threshold outcome, sample-size assessment, notes and source note.
- `StableDanEvaluationReport.to_dict()` returns a JSON-serializable dictionary.
- Documented that sample-size defaults are project-internal governance guardrails, not Tenhou official standards or proof of strength.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This remains evaluation statistics infrastructure only, not training, self-play, league execution, real Tenhou integration or model-strength evidence.
- Set the next task to `Add placement-count aggregation helper for stable-dan evaluation inputs.`

## 2026-05-29 — v2.6

- Added a stable-dan threshold comparison helper for the LuckyJ 10.68 target line.
- Extended `src/mjlabai/eval/stable_dan.py` with:
  - `LUCKYJ_STABLE_DAN_THRESHOLD = 10.68`.
  - `StableDanThresholdComparison`.
  - `compare_stable_dan_to_threshold(...)`.
  - `bootstrap_and_compare_stable_dan_threshold(...)`.
- Clear pass now requires `bootstrap_result.lower_bound > threshold` and `undefined_rate <= max_undefined_rate`.
- If point estimate exceeds the threshold but bootstrap lower bound does not, the outcome is `point_estimate_only` and `clears_threshold=False`.
- If undefined bootstrap resample rate is too high, the outcome is `unreliable` and `clears_threshold=False`.
- Added threshold comparison tests for clear pass, point-estimate-only, clear fail, inconclusive, unreliable, custom threshold, invalid inputs and the bootstrap-and-compare helper.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 32 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This is evaluation statistics infrastructure only, not model-strength evidence, training, self-play, league execution or Tenhou integration.
- Set the next task to `Add minimum sample-size and reporting schema for stable-dan evaluation results.`

## 2026-05-29 — v2.5

- Added bootstrap confidence intervals for the Tenhou stable-dan estimate.
- Extended `src/mjlabai/eval/stable_dan.py` with:
  - `bootstrap_stable_dan_ci(...)`.
  - `StableDanBootstrapResult`.
  - `StableDanBootstrapUndefinedError`.
- Implemented percentile empirical multinomial bootstrap over observed placement counts using Python standard library only.
- Bootstrap output records point estimate, confidence level, lower bound, upper bound, bootstrap count, successful resamples, undefined resamples, undefined rate, method, seed, quantile method and source note.
- Undefined bootstrap resamples with zero fourth-place count are skipped and counted; they are not converted into infinite stable dan.
- If every bootstrap resample is undefined, the API raises `StableDanBootstrapUndefinedError`.
- Updated `tests/eval/test_stable_dan.py` to cover reproducible seeded bootstrap, undefined-resample accounting, validation errors and non-infinite bounds.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 21 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This is evaluation statistics infrastructure only, not model-strength evidence, training, self-play, league execution or Tenhou integration.
- Set the next task to `Add stable-dan threshold comparison helper for LuckyJ 10.68 using bootstrap lower bound.`

## 2026-05-29 — v2.4

- Implemented the Tenhou stable-dan calculator as the next P5 evaluation-foundation task.
- Added `src/mjlabai/eval/stable_dan.py` and `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_stable_dan.py`.
- Implemented deterministic four-player room-specific formulas for:
  - general / ippan: first=20, second=10.
  - upper / joukyu: first=40, second=10.
  - expert / tokujou: first=50, second=20.
  - phoenix / houou: first=60, second=30.
- Added `StableDanResult`, `StableDanUndefinedError`, `calculate_stable_dan(...)` and `placement_rates(...)`.
- Recorded placement counts, placement rates, total games, formula name, formula weights and source note in calculator output.
- `fourth_count == 0` now raises `StableDanUndefinedError`; the calculator does not fabricate infinite strength.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 9 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This is deterministic metric infrastructure only, not a training result, league result, self-play result or Tenhou connection.
- Set the next task to `Add bootstrap confidence interval for stable-dan estimate.`

## 2026-05-29 — v2.3

- Closed the Akochan F2 fixed-sample real-exe wrapper validation task.
- Recorded GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` run `26629344590`.
- Run `26629344590` executed at commit `29f5e1ed19407d169f85524e05438ac8938d2dc2` with commit message `Support Akochan mixed stdout parsing`.
- Workflow result and job result were both success.
- Confirmed Ubuntu runner built `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Confirmed fake wrapper tests passed 14 tests.
- Confirmed real external `system.exe legal_action` wrapper test passed.
- Confirmed real external `system.exe mjai_log` wrapper test passed.
- Confirmed allowlisted mixed stdout parser passed real workflow validation.
- Recorded that this is fixed-sample wrapper/integration evidence only, not Akochan strength evidence and not mjlabai strength evidence.
- Recorded that no training, tuning, self-play, match, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.
- Recorded that Akochan custom license remains a blocker for modification, redistribution, commercial use or public release without review/permission.
- Recorded GitHub Actions Node.js 20 deprecation warning as workflow maintenance risk, not an F2 validation blocker.
- Set the next task to `Implement Tenhou stable-dan calculator from room-specific formulas.`

## 2026-05-29 — v2.2

- Fixed the Akochan F2 real-exe `mjai_log` mixed stdout parser blocker exposed by workflow run `26628128871`.
- The parser now supports:
  - single JSON values,
  - JSON Lines,
  - concatenated JSON values/objects,
  - pretty-printed multi-record JSON streams,
  - mixed stdout that contains the single allowlisted non-JSON status line `calculating review`.
- Added `skipped_non_json_lines` to `AkochanCommandResult`.
- Parser diagnostics now include bounded stdout summary, stdout SHA256, failure position, parsed-record count and skipped-status-line count.
- Unknown non-JSON lines and partial parses still raise `AkochanOutputParseError`; the only skipped non-JSON line is exactly `calculating review`.
- Fake executable tests now simulate JSON records + `calculating review` + JSON review output, plus an unknown status line that must fail.
- Local validation passed:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Set the next task to rerun the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review real `legal_action` / `mjai_log` results after allowlisted mixed stdout parser support.
- No training, tuning, self-play, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.

## 2026-05-29 — v2.1

- Fixed the Akochan F2 real-exe `mjai_log` stdout parser blocker exposed by workflow run `26623247276`.
- `AkochanWrapper` now parses:
  - single JSON values,
  - JSON Lines,
  - concatenated JSON values/objects,
  - pretty-printed multi-record JSON streams.
- Added `parsed_records` to `AkochanCommandResult` while preserving `parsed_json` compatibility: one record returns the record, multiple records return the records list.
- Parser diagnostics now include bounded stdout summary, stdout SHA256, failure position and parsed-record count.
- Parser does not accept partial parses: non-whitespace non-JSON residue raises `AkochanOutputParseError`.
- Fake executable tests now simulate JSON Lines, concatenated JSON objects, pretty-printed multi-record JSON streams and invalid mixed stdout.
- Local validation passed:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 12 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Set the next task to rerun the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review real `legal_action` / `mjai_log` results.
- No training, tuning, self-play, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.

## 2026-05-29 — v2.0

- Reran manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit`.
- Run `26623247276` executed at commit `0ddb28575ddd1b624cad34b20d6dc6b79303963c`.
- Confirmed Ubuntu build still generated `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Confirmed fake wrapper smoke tests passed 8 tests in the workflow.
- Confirmed workflow exported `AKOCHAN_SYSTEM_EXE`, `AKOCHAN_WORKING_DIR` and `AKOCHAN_MJAI_LOG_SAMPLE` before real-exe tests.
- Confirmed real `legal_action` wrapper test passed.
- Confirmed the previous `setup_mjai.json` cwd failure is gone for real `mjai_log`.
- Recorded the new blocker: real `mjai_log` stdout reaches the wrapper, but parsing fails with `JSONDecodeError: Extra data` / `AkochanOutputParseError`.
- Set the next task to fix real `mjai_log` stdout parsing/diagnostics, then rerun the workflow.
- Reaffirmed that this is interface/runtime evidence only, not strength evidence, and no third-party source, binary, params or build artifact was uploaded.

## 2026-05-29 — v1.9

- Fixed the Akochan F2 wrapper working-directory boundary exposed by workflow run `26621536548`.
- `AkochanWrapper` now resolves the runtime cwd by priority: explicit `working_dir`, `AKOCHAN_WORKING_DIR`, then `Path(system_exe).resolve().parent`.
- `_run_subcommand` now launches the external executable with `cwd=self.working_dir`.
- `AkochanAuditLog` now records `working_dir`.
- Updated fake executable tests so `mjai_log` requires a synthetic cwd runtime marker, proving cwd handling is exercised.
- Updated the real-exe workflow to export `AKOCHAN_SYSTEM_EXE`, `AKOCHAN_WORKING_DIR` and `AKOCHAN_MJAI_LOG_SAMPLE` before running real wrapper tests.
- Local validation passed:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 8 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Set the next task to rerun the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review whether real `legal_action` and `mjai_log` both pass with `AKOCHAN_WORKING_DIR` set.
- No training, tuning, self-play, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.

## 2026-05-29 — v1.8

- Triggered manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit`.
- Run `26621536548` executed at commit `7d58f969367d3e51c57d859dbfb9433f1ca898a1`.
- Confirmed the workflow built Akochan successfully in the temporary Ubuntu runner: `ai_src/libai.so`, root `libai.so` and `system.exe` were generated.
- Confirmed fake wrapper smoke tests passed in the workflow.
- Confirmed real `legal_action` wrapper test passed against the Ubuntu-built `system.exe`.
- Recorded real `mjai_log` wrapper test failure: `system.exe` could not load `setup_mjai.json` because the wrapper launched it from the mjlabai checkout working directory.
- Set the next task to fix the real-exe cwd/runtime boundary, then rerun the workflow.
- Reaffirmed that this is interface/runtime evidence only, not strength evidence, and no third-party source, binary, params or build artifact was uploaded.

## 2026-05-29 — v1.7

- Added `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`.
- The new workflow is manual `workflow_dispatch` only and builds Akochan at commit `53188a0b926fbab38177f88c3cd87d554cf412af` inside a temporary `ubuntu-latest` GitHub runner.
- The workflow sets `AKOCHAN_SYSTEM_EXE` to the runner-temp `system.exe` and `AKOCHAN_MJAI_LOG_SAMPLE` to the runner-temp `haifu_log_sample.json`, then runs mjlabai wrapper tests against the real external executable.
- Added `tests/adapters/test_akochan_wrapper_real_exe.py` with default skip behavior when `AKOCHAN_SYSTEM_EXE` is absent; `mjai_log` also skips when `AKOCHAN_MJAI_LOG_SAMPLE` is absent.
- Updated the wrapper stdout parser to accept either one JSON document or newline-delimited JSON objects.
- Verified local fake tests with `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 4 tests passed.
- Verified local real-exe tests with `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without a real external executable.
- Confirmed the new workflow/test path does not upload or store Akochan source, `system.exe`, `libai.so`, `params/`, third-party binaries or build artifacts.
- Set the next task to manually run `Akochan F2 Wrapper Real Exe Audit` and review whether the wrapper succeeds against the real Ubuntu-built `system.exe`.

## 2026-05-29 — v1.6

- Implemented the minimal Akochan F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples.
- Added minimal Python package structure under `src/mjlabai` and project metadata in `pyproject.toml`.
- Added `AkochanWrapper.run_legal_action(input_json)` and `AkochanWrapper.run_mjai_log(log_path, actor=0, mode=2)`.
- Added audit-log dataclasses that record external repo/commit, build environment, command, input/output hashes, exit code, stdout/stderr summaries, elapsed time and explicit no-training/no-self-play/no-Tenhou flags.
- Added synthetic test fixtures and `tests/fixtures/akochan/fake_system_exe.py` as a test substitute only; it is not Akochan and is not strength evidence.
- Added unit/smoke tests for JSON parsing, `dahai` normalization, audit logs, environment-variable executable path support and non-JSON stdout failure handling.
- Verified `python3 -m unittest tests/adapters/test_akochan_wrapper.py` passed 4 tests.
- Confirmed no Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary, unknown model artifact or build artifact was stored in this repository.
- Set the next task to run the wrapper against a real GitHub Actions Ubuntu-built external `system.exe` for fixed samples without uploading third-party binaries or artifacts.

## 2026-05-29 — v1.5

- Added `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`.
- Defined the Akochan F2 interface/legal-action adapter task without writing adapter code.
- Documented Akochan's F2 roles: legal-action checker, mjai/log reviewer and baseline/reviewer candidate.
- Defined wrapper-only boundaries: no Akochan source, `system.exe`, `libai.so`, `params/`, third-party binaries or build artifacts may enter this repository.
- Added draft mjai event mapping, normalized action schema, audit-log schema, F2 acceptance criteria and F2 failure conditions.
- Reaffirmed custom-license guardrails: private/internal audit only until license review or permission clears broader use.
- Set the next task to implement a minimal Akochan F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples under no-vendor, no-training and no-Tenhou constraints.
- Updated next, handoff, docs index, evidence, risk, candidate-table, backlog, stage-contract, technical-plan and decision docs.

## 2026-05-29 — v1.4

- Triggered the corrected manual GitHub Actions workflow `Akochan F1 Build Audit`.
- Run `26617347785` succeeded at commit `b6b69e08fd009052cb3bbd16c779ac6e2139591b`.
- Confirmed Ubuntu build generated `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Confirmed both minimal non-training samples succeeded: `legal_action` and `mjai_log haifu_log_sample.json 0 2`.
- Upgraded Akochan F1 from Blocked to Conditional Pass, limited to Ubuntu GitHub Actions evidence and subject to custom-license restrictions.
- Set the next task to define the Akochan F2 interface/legal-action adapter task; no adapter code was written.
- Recorded the GitHub Actions Node.js 20 deprecation warning for `actions/checkout@v4` as workflow maintenance risk.
- Updated next, handoff, evidence, risk, candidate-table, audit, backlog, stage-contract, technical-plan and decision docs.

## 2026-05-29 — v1.3

- Reviewed the first `Akochan F1 Build Audit` GitHub Actions run.
- Confirmed run `26615920289` failed during GitHub workflow validation before any Ubuntu build/minimal sample started.
- Fixed `.github/workflows/akochan-f1-build-audit.yml` by moving `AKOCHAN_DIR` and `SUMMARY_FILE` path setup out of job-level `env` and into a shell step that writes to `$GITHUB_ENV`.
- Added a fallback in the final summary step so validation/setup failures still produce a clear GitHub step summary when possible.
- Akochan remains F1 Blocked because the failed run produced no `system.exe`, `legal_action` or `mjai_log` evidence.
- Updated next, handoff, evidence, risk, audit and backlog docs.

## 2026-05-29 — v1.2

- Added manual GitHub Actions workflow `.github/workflows/akochan-f1-build-audit.yml`.
- The workflow provides an Ubuntu `workflow_dispatch` build-audit path for Akochan F1 without changing local machine dependencies.
- The workflow clones `critter-mj/akochan` at commit `53188a0b926fbab38177f88c3cd87d554cf412af` into the runner temp directory, installs build dependencies inside the temporary Ubuntu runner, attempts the Linux Makefile builds and runs only minimal non-training samples if `system.exe` is produced.
- The workflow does not train, tune, self-play, connect to Tenhou, write an adapter, enter F2, upload third-party source, upload binaries or publish artifacts.
- Akochan remains F1 Blocked until a manual workflow run succeeds and its build/minimal-run evidence is reviewed.
- Updated next, handoff, evidence, risk, audit and backlog docs.

## 2026-05-29 — v1.1

- Attempted to resolve the Akochan F1 build/toolchain blocker without training, tuning, self-play, Tenhou access, adapter work or third-party vendoring.
- Confirmed Docker is unavailable on the local machine.
- Re-cloned `critter-mj/akochan` outside the repository at fixed commit `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Confirmed local macOS ARM has Apple clang and make, but no usable Homebrew LLVM/Boost/OpenMP files.
- Retried official `ai_src` and root MacOS/Linux Makefile paths; all failed before producing `libai.so` or `system.exe`.
- No minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample was run because `system.exe` was not generated.
- Kept Akochan at F1 Blocked and narrowed the next task to providing a supported Docker Linux or verified local LLVM/Boost/OpenMP build environment.

## 2026-05-29 — v1.0

- Completed the Akochan F1 reproducibility audit as the next baseline path.
- Added `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`.
- Recorded `critter-mj/akochan` repository metadata, audited commit, custom license terms, dependency/build path, artifact needs, minimal-run entry points and I/O/logging fit.
- Confirmed Akochan does not appear to need external neural-network weights, but relies on repository-included text parameters under `params/`.
- Attempted local build in the external temporary clone only; macOS ARM build is blocked by missing/incompatible LLVM/OpenMP/Boost toolchain and Linux Makefile incompatibility.
- Set Akochan F1 conclusion to Blocked and kept Akochan out of F2.
- Updated next-task, handoff, evidence, risk, candidate-table, development-backlog, stage-contract, technical-plan and decision docs.

## 2026-05-29 — v0.9

- Completed the Mortal F1 continuation decision.
- Paused Mortal as a runnable baseline because no lawful, verifiable and usable trained model artifact is currently available.
- Recorded that unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files must not be used.
- Kept Mortal as a source-code, mjai-interface, methodology and engineering reference.
- Moved the next baseline F1 path to Akochan reproducibility audit without starting the Akochan audit in this task.
- Updated next-task, handoff, decision, risk, stage-contract, technical-plan, candidate-table, development-backlog and candidate-role docs.

## 2026-05-29 — v0.8

- Added `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` as the current technical execution charter.
- Shifted the project framing from internal-paper-first to technical-plan-first; papers are future outcome summaries.
- Clarified Web ChatGPT Pro vs local Codex App responsibilities.
- Reaffirmed Git + docs as the only source of truth.
- Recorded the current main route: Suphx-style SL+RL, Tenhou stable dan / pt EV reward, ACH-inspired policy improvement, risk model/search and baseline racing funnel.
- Clarified that LuckyJ is the target benchmark, not a direct full-reproduction object.
- Added `docs/09_governance/09_DECISION_RECORD.md` and recorded DR-0001.
- Updated docs index, handoff, next, evidence and risk notes.

## 2026-05-28 — v0.7

- Attempted to resolve Mortal F1 local reproducibility blockers without training, tuning, self-play or Tenhou integration.
- Retrieved and checksummed Mortal source tarball for commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2` through explicit host resolution.
- Confirmed normal system DNS and normal `git clone` are still unreliable.
- Confirmed Python 3.12 is available, but PyTorch is missing; Rust/Cargo and Docker remain unavailable.
- Recorded that Homebrew Rust metadata lookup is blocked by `formulae.brew.sh` DNS failure.
- Retrieved and checksummed the README-linked model-release gist metadata; recorded that official trained model parameters are not currently planned for public release.
- Left Mortal at F1 Reproduce blocked and updated `10_NEXT.md` to require a lawful trained model artifact decision before further Mortal runnable-baseline work.
- Updated development backlog so the blocker-resolution task is blocked on model artifact availability and the continuation decision is the planned next task.

## 2026-05-28 — v0.6

- Completed Mortal F1 initial reproducibility audit without training, tuning, self-play or Tenhou integration.
- Recorded that Mortal source/docs are inspectable through the GitHub connector at commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- Recorded Mortal code license, dependency/build path, Docker/mjai inference path, input/output notes and logging metadata.
- Recorded local blockers: GitHub DNS failure, missing Rust/Cargo, missing Docker/conda/torch and missing model artifact.
- Kept Mortal at F1 Reproduce blocked and updated `10_NEXT.md` to resolve blockers before any F2 adapter work.
- Updated development backlog statuses and added the Mortal F1 blocker-resolution task.
- Updated the stage task contract from rule-load verification to P3 baseline reproducibility audit.

## 2026-05-28 — v0.5

- Added the P0-P12 project roadmap to `07A_MILESTONES.md`.
- Clarified that P0/P1/P2 are basically established and the project is preparing to enter P3 baseline reproducibility audit.
- Updated handoff and next task so Mortal F1 reproducibility audit is the current execution step.
- Replaced the stale `templates/prompts/09_ALGORITHM_RACING_FUNNEL.md` reference with `docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md`.
- Recorded the stale template-path issue as a mitigated documentation risk.

## 2026-05-28 — v0.4

- Added racing-funnel mechanism for algorithm selection.
- Clarified that the project will not fully train every candidate algorithm before comparison.
- Added staged funnel: F0 registration, F1 reproducibility, F2 adapter/legal-action, F3 offline scenarios, F4 small league, F5 medium league, F6 mainline candidate, F7 LuckyJ validation.
- Clarified roles of LuckyJ, Suphx, Mortal, Archer, Akochan and Kanachan.
- Added racing-funnel evaluation metrics and promotion gates.
- Added local Codex prompt for applying the racing funnel.
- Added racing-funnel gate checklist.
- Updated docs index, handoff, risk register and next task.

## 2026-05-28 — v0.3

- Added concrete algorithm candidate table for Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer.
- Added scoring rubric for candidate selection.
- Added algorithm ranking protocol with evaluation ladder and stable-dan uncertainty requirement.
- Added local Codex prompt for building the candidate table.
- Added algorithm ranking gate checklist.
- Updated handoff, docs index and next task.

## 2026-05-28 — v0.2

- Added algorithm selection principles.
- Added algorithm candidate routes: Suphx-style, LuckyJ-inspired, open-source baseline, evaluation-first, search+risk.
- Added imperfect-information search document.
- Added algorithm discovery workflow for local Codex execution.
- Added algorithm candidate card template.
- Added algorithm discovery prompts and algorithm gate checklist.
- Updated `10_NEXT.md` to make algorithm candidate table the next post-rule-load task.
- Updated evidence log with initial sources for LuckyJ, Suphx, ACH, Mortal, Akochan, Kanachan and Archer.

## 2026-05-28 — v0.1

- Initial documentation package created.
