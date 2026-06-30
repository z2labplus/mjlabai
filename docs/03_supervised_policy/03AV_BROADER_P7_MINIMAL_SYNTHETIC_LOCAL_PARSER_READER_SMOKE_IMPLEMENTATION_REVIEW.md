# 03AV Broader P7 Minimal Synthetic/Local Parser-Reader Smoke Implementation Review

Date: 2026-07-01

## Scope

This document reviews the exact broader P7 minimal synthetic/local
parser-reader smoke implementation approved by `03AU`.

This is a docs-only implementation review gate. It does not add production
code, modify implementation logic, add tests, add fixtures, add data files,
approve broader P7 implementation, approve source approval, approve source
ingestion, approve broad parser / reader / ingestion, approve actual feature
extraction, approve actual label generation, approve supervised dataset
construction, approve split creation, approve leakage-test implementation,
approve training data, approve a training run, approve training, approve model
architecture or trainer implementation, approve evaluation implementation,
approve model-output integration, create model-strength evidence, create
Tenhou ranked evidence, create stable-dan ranked-game evidence, create LuckyJ
`10.68` comparison evidence, create candidate-promotion evidence, approve
self-play, approve league or approve P8-P12 entry.

North-star relationship: this review supports the long-term Tenhou stable-dan
`> 10.68` target only by checking that a small synthetic/local P7 guardrail
implementation stayed inside its approved scope. It is not model-strength
evidence, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ
`10.68` comparison or candidate-promotion evidence.

## Reviewed Artifacts

Reviewed approval and proposal artifacts:

- `docs/03_supervised_policy/03AU_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
- `docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`
- `docs/03_supervised_policy/03AT_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`

Reviewed implementation artifacts:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`

Reviewed support artifacts for context only:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Reviewed governance artifacts:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Exact File Scope Review

`03AU` approved only these implementation files:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`

Review findings:

- The implementation used exactly the approved implementation files.
- Direct docs/governance synchronization was added.
- No new fixture was added.
- No new data file was added.
- Existing supervised and data fixtures were not modified.
- Existing support implementation files were not modified.
- No unrelated implementation files were modified.

Review verdict: exact file scope respected.

## Module Review

Reviewed module:

```text
src/mjlabai/supervised/synthetic_parser_reader_smoke.py
```

Findings:

- The module uses the Python standard library plus the approved import from
  `feature_label_schema`.
- It accepts only already-loaded in-memory `Mapping` inputs.
- It rejects string path inputs.
- It rejects `PathLike` inputs.
- It rejects `bytes` and `bytearray` path-like inputs.
- It delegates guardrail validation to `collect_feature_label_smoke_errors`
  and `validate_feature_label_smoke_mapping`.
- It raises `SyntheticParserReaderSmokeError` for invalid smoke mappings.
- It returns a JSON-safe smoke summary.
- It does not read files.
- It does not read directories.
- It does not expose CLI behavior.
- It does not implement broad ingestion.
- It does not use real data.
- It does not accept model output.
- It does not allow source-approval claims through the delegated validation.
- It does not allow hidden or future information through the delegated
  validation.
- It does not emit feature tensors.
- It does not emit labels or targets.
- It does not emit supervised examples.
- It does not emit datasets or splits.
- It does not emit model inputs or model outputs.
- It does not emit evaluation results.
- It does not emit model-strength evidence.

Review verdict: module scope is safe for the exact synthetic/local smoke
implementation.

## Test Review

Reviewed test:

```text
tests/supervised/test_synthetic_parser_reader_smoke.py
```

Findings:

- Valid in-memory mapping passes.
- The existing project-authored synthetic/local supervised fixture is used
  read-only by the test harness.
- `real_data=True` is rejected.
- `model_output=True` is rejected.
- `source_approval="approved"` is rejected.
- `hidden_information` is rejected.
- `future_information` is rejected.
- String and path-like parser inputs are rejected.
- Forbidden output keys are absent from the returned summary.
- Non-evidence flags remain false.
- Non-JSON-safe mappings are rejected.
- The test file does not create new fixtures.
- The test file does not modify fixtures.
- The test file does not perform broad file ingestion.
- The test file does not expose CLI behavior.
- The test file does not run training.
- The test file does not invoke model or evaluation logic.
- The test file does not read real Tenhou, real haifu, external logs,
  platform data or account/session/cookie/token inputs.

Review verdict: test scope is safe for the exact synthetic/local smoke
implementation.

## Input Boundary Review

Allowed inputs remain limited to:

- in-memory project-authored synthetic/local mappings.
- the existing project-authored synthetic/local supervised fixture used
  read-only by tests.
- JSON-safe synthetic/local record content.

Forbidden inputs remain rejected or out of scope:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account/session/cookie/token data.
- arbitrary parser paths.
- broad directories.
- model outputs.
- generated labels.
- human labels from real play.
- self-play outputs.
- league outputs.
- third-party binaries, weights, params or checkpoints.
- unapproved source data.

Review verdict: input boundary is safe.

## Output Boundary Review

The parser-reader smoke helper returns only smoke-level guardrail fields,
including:

- record type and version.
- input fixture id and schema version.
- reader / parser smoke kinds.
- provenance flags.
- public-information and hidden/future-information guardrails.
- feature-family, label-family and warning counts.
- non-evidence guardrail summary.

The output does not contain:

- `feature_tensor`
- `features`
- `labels`
- `targets`
- `supervised_examples`
- `splits`
- `dataset`
- `training_data`
- `model_input`
- `model_output`
- `evaluation_result`
- `model_strength`

The output is not training data, not a dataset, not model input and not
evidence of model strength.

Review verdict: output boundary is safe.

## Non-Evidence Review

This implementation is only:

```text
Broader P7 minimal synthetic/local parser-reader smoke implementation evidence.
```

It is not:

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
- model architecture / trainer implementation.
- evaluation implementation.
- model-output integration.
- model-strength evidence.
- Tenhou evidence.
- stable-dan evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- P8-P12 entry approval.

Review verdict: evidence grade and claim boundaries are safe.

## Validation Results

Validation commands for this review:

```bash
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Validation result:

```text
All listed commands passed.
```

The review did not run real-data commands, Tenhou commands, training, tuning,
self-play, league, model-output integration, evaluation implementation,
model-strength evidence commands, LuckyJ comparison commands, Akochan
`system.exe`, `libai.so`, third-party binaries or unknown model artifacts.

## Governance Synchronization Review

Governance synchronization is sufficient after this review:

- `docs/00_HANDOFF.md` records the current review-gate status.
- `docs/00_DOCS_INDEX.md` lists this review document.
- `docs/10_next/10_NEXT.md` records this review as complete and sets the next
  docs-only acceptance decision task.
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` records the review-gate
  decision and next task.
- `docs/09_governance/09_EVIDENCE_LOG.md` records the implementation review
  evidence grade.
- `docs/09_governance/09_RISK_REGISTER.md` records remaining overclaim and
  scope-drift risks.
- `docs/09_governance/09_CHANGELOG.md` records this review.
- `docs/09_governance/09_DECISION_RECORD.md` records the review decision.
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md` records the updated current
  stage and next task.
- `docs/07_development_execution/07A_MILESTONES.md` records current P7 status.
- `docs/07_development_execution/07B_TASK_BACKLOG.md` records the review gate
  as complete and the acceptance decision as the next task.

Review verdict: governance synchronization is complete for this review gate.

## Review Decision

```text
Review can close.
```

Rationale:

- Exact file scope was respected.
- No extra implementation files were added.
- No fixture or data file was added.
- Module scope is safe.
- Test scope is safe.
- Input and output boundaries are safe.
- Non-evidence boundaries are safe.
- Validation passed.
- Governance is synchronized.
- No blocker was found.
- No overclaim was found.

## Next Task Recommendation

Recommended next first task:

```text
Decide whether broader P7 minimal synthetic/local parser-reader smoke implementation can be accepted as current-scope complete.
```

The next task must remain docs-only. It must not be treated as full P7 closure,
broader P7 implementation approval, source approval, source ingestion, broad
parser / reader / ingestion approval, actual feature extraction approval,
actual label generation approval, supervised dataset construction approval,
training-data approval, training-run approval, training approval, model /
trainer approval, evaluation approval, model-output integration approval,
model-strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ `10.68`
comparison, candidate-promotion evidence, self-play, league or P8-P12 entry.

## Evidence Grade

```text
Broader P7 minimal synthetic/local parser-reader smoke implementation review evidence only.
```

## Explicit Non-Evidence

This review is not:

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
- candidate promotion evidence.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- self-play.
- league.
- P8-P12 entry approval.
