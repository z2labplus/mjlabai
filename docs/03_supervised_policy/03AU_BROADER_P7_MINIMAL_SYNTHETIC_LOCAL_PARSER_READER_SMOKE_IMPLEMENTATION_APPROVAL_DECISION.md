# 03AU Broader P7 Minimal Synthetic/Local Parser-Reader Smoke Implementation Approval Decision

Date: 2026-06-30

## Scope

This document prepares and records the approval decision for the broader P7
minimal synthetic/local parser-reader smoke implementation candidate.

This is a docs-only approval-decision document. It does not execute
implementation, add production code, add tests, add fixtures, add data files,
modify implementation logic, approve broader P7 implementation, approve source
approval, approve source ingestion, approve broad parser / reader / ingestion,
approve actual feature extraction, approve actual label generation, approve
supervised dataset construction, approve split creation, approve leakage-test
implementation, approve training-data construction, approve training-data
approval, approve a training run, approve training, approve model architecture
or trainer implementation, approve checkpoint / weights creation, approve
evaluation implementation, approve model-output integration, create
model-strength evidence, create Tenhou ranked evidence, create stable-dan
ranked-game evidence, create LuckyJ `10.68` comparison evidence, create
candidate-promotion evidence, approve self-play, approve league or approve
P8-P12 entry.

North-star relationship: this decision supports the long-term Tenhou
stable-dan `> 10.68` target only by allowing one narrowly bounded
synthetic/local parser-reader smoke implementation to become auditable in a
later task. It is not model-strength evidence, Tenhou ranked evidence,
stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
candidate-promotion evidence.

## Reviewed Proposal Chain

Reviewed proposal chain:

- `03AQ` defined the broader P7 minimal implementation proposal boundary.
- `03AR` reviewed that proposal boundary and recorded `Review can close`.
- `03AS` drafted the project-authored synthetic/local parser-reader smoke
  proposal for later review only.
- `03AT` reviewed `03AS`, recorded `Review can close`, found no blocker and
  recommended this docs-only approval-decision preparation task.

Current task role:

- This document performs only the approval decision.
- It does not implement the decision.
- It does not create the future approved files.
- It does not create a new fixture.
- It does not generate or run the future test.

## Decision Options

| option | meaning | selected |
| --- | --- | ---: |
| Approved for next exact minimal implementation task. | A later exact `10_NEXT` implementation task may create only the exact approved files and scope. | yes |
| Deferred pending blocker or clarification. | Implementation remains closed and a docs-only blocker-resolution task is needed. | no |
| Rejected / not approved. | Implementation remains closed because the proposal is not acceptable. | no |

## Decision

```text
Approved for next exact minimal implementation task.
```

Exact approved future task:

```text
Implement broader P7 minimal synthetic/local parser-reader smoke only.
```

This approval is narrow. It approves only placing that exact implementation
task into `docs/10_next/10_NEXT.md` as the next first unchecked task. It does
not execute implementation in this task and does not approve broader P7
implementation.

This approval is not source approval, source ingestion approval, broad parser
/ reader / ingestion approval, actual feature extraction approval, actual label
generation approval, supervised dataset construction approval, split creation
approval, leakage-test implementation approval, training-data approval,
training-run approval, training approval, model architecture / trainer
approval, evaluation approval, model-output integration approval,
model-strength evidence approval, Tenhou evidence approval, stable-dan
evidence approval, LuckyJ `10.68` comparison approval, candidate promotion
approval, self-play approval, league approval or P8-P12 entry approval.

## Exact Approved Future Files

The next exact implementation task may create or modify only these
implementation files:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`

The next exact implementation task may also update directly related
docs/governance records only as needed to record implementation evidence,
validation, risks and the next task.

No new fixture or data file is approved by default. In particular,
`tests/fixtures/supervised/synthetic_parser_reader_smoke.json` is not approved
for creation by this decision. If a future implementation needs a new fixture
or any additional file, it must stop and require a separate approval or
approval amendment.

## Explicitly Excluded Files

The next implementation task must not modify these files unless a later
approval decision explicitly amends the exact scope:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`
- any real-data directory.
- any CLI file.
- any broad ingestion file.
- any model / trainer / dataloader / optimizer / loss / checkpoint / weight
  file.
- any evaluation / metric / runner / benchmark harness file.
- any P8-P12 file.
- any third-party source, binary, params or build artifact.
- any account / session / cookie / token file.
- `.env`, dotfiles or secret files.

## Allowed Future Inputs

The next exact implementation task may use only:

- project-authored synthetic/local in-memory mappings.
- the existing project-authored synthetic/local supervised fixture
  `tests/fixtures/supervised/synthetic_supervised_smoke.json` as read-only
  input if the exact implementation uses it.
- JSON-safe synthetic/local records.
- synthetic/local provenance and non-evidence guardrails.

Allowed inputs must not be broad filesystem paths and must not come from real
or external sources.

## Forbidden Future Inputs

The next exact implementation task must not use:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token data.
- hidden files / dotfiles.
- `.env` / secrets.
- arbitrary user-supplied paths.
- broad directories.
- model outputs.
- generated labels.
- human labels from real play.
- self-play outputs.
- league outputs.
- third-party binaries / weights / checkpoints / params.
- any source not explicitly approved.

## Allowed Future Outputs

The next exact implementation task may output only:

- in-memory normalized synthetic/local records.
- JSON-safe validation summaries.
- schema-safe smoke objects.
- provenance / guardrail flags.
- local unit-test pass/fail evidence.
- docs/governance evidence entries.

## Forbidden Future Outputs

The next exact implementation task must not output:

- feature tensors.
- labels.
- targets.
- supervised examples.
- train / validation / test splits.
- datasets.
- training data.
- model inputs.
- model outputs.
- evaluation results.
- model-strength evidence.
- Tenhou evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.

## Future Validation Commands

The future implementation task should run at least:

```bash
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

This approval-decision task must not run
`tests/supervised/test_synthetic_parser_reader_smoke.py`, because that future
test does not exist yet.

## Future Implementation Stop Conditions

The future implementation task must stop before commit if any of these occur:

- an unapproved file is needed.
- a new fixture or data file is needed.
- real data is needed.
- source approval is needed.
- source ingestion is needed.
- arbitrary-path reading is needed.
- CLI behavior is needed.
- broad ingestion behavior is needed.
- feature tensors are emitted.
- labels are emitted.
- targets are emitted.
- supervised examples are emitted.
- a dataset is constructed.
- a split is created.
- leakage checks are created.
- training behavior appears.
- model / trainer / checkpoint / weights behavior appears.
- evaluation / metric / runner / harness behavior appears.
- model-output integration appears.
- model-strength, Tenhou, stable-dan, LuckyJ or promotion claims appear.
- P8-P12 drift appears.
- validation fails.
- docs/governance cannot be updated consistently.

## Future Rollback Plan

If the future exact implementation expands scope or fails validation, rollback
must:

- revert the exact implementation commit.
- remove only approved new implementation files.
- preserve existing P6/P7 smoke artifacts.
- require no real-data deletion, because no real data may be used.
- update docs/governance to mark the task failed, reverted or blocked.
- stop if rollback would touch unrelated files.

## Risk Controls

| risk | control |
| --- | --- |
| Approval decision mistaken for implementation execution. | This document says implementation is not executed and sets implementation as the next task only. |
| Narrow approval mistaken for broader P7 implementation approval. | Approved files and scope are exact; broader P7 remains open and unapproved. |
| Synthetic/local parser-reader smoke mistaken for source ingestion. | Source approval, source ingestion, real data and broad ingestion remain forbidden. |
| Parser-reader smoke drifts into feature extraction. | Feature tensors, labels, targets and examples are forbidden outputs. |
| Reader output mistaken for labels or supervised examples. | Allowed output is limited to normalized synthetic/local records and validation summaries. |
| Candidate files mistaken for current edits. | The exact files are approved only for the next implementation task, not this decision task. |
| Future validation command mistaken for current test creation. | The future parser-reader smoke test is not run or created by this task. |
| Existing fixture read-only use drifts into fixture modification. | Existing supervised fixture is read-only if used; modification is explicitly excluded. |
| Real-data creep. | Real Tenhou, real haifu, external logs and platform data remain forbidden inputs. |
| CLI or broad ingestion creep. | CLI and broad file ingestion remain forbidden. |
| Model-output creep. | Model outputs remain forbidden inputs and outputs. |
| Dataset or training creep. | Dataset construction, split creation, training data and training remain forbidden. |
| Evaluation or strength creep. | Evaluation implementation and model-strength / Tenhou / LuckyJ claims remain forbidden. |
| P8-P12 creep. | P8-P12 entry remains unapproved. |
| Governance mismatch. | Handoff, index, `10_NEXT`, technical plan, evidence log, risk register, decision record, changelog, stage contract, milestones and backlog are synchronized. |

## Evidence Requirements

The approval-decision evidence fields are:

- approval_decision_id: `03AU`.
- reviewed_proposal:
  `docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`.
- reviewed_proposal_review:
  `docs/03_supervised_policy/03AT_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`.
- decision: `Approved for next exact minimal implementation task.`
- approved_future_task_name:
  `Implement broader P7 minimal synthetic/local parser-reader smoke only.`
- approved_exact_files:
  `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`,
  `tests/supervised/test_synthetic_parser_reader_smoke.py`.
- explicitly_excluded_files: listed above.
- allowed_inputs: listed above.
- forbidden_inputs: listed above.
- allowed_outputs: listed above.
- forbidden_outputs: listed above.
- validation_commands: listed above.
- stop_conditions: listed above.
- rollback_plan: listed above.
- risk_controls: listed above.
- evidence_grade:
  `Broader P7 minimal synthetic/local parser-reader smoke approval-decision evidence only.`
- evidence_log_reference: `docs/09_governance/09_EVIDENCE_LOG.md`.
- risk_register_reference: `docs/09_governance/09_RISK_REGISTER.md`.
- decision_record_reference: `docs/09_governance/09_DECISION_RECORD.md`.
- human / Web ChatGPT approval reference: the user-provided approval-decision
  prompt for this task.
- explicit_non_evidence_warning: listed below.

## Next Task

Because the decision is approved, the next first `10_NEXT` task should be:

```text
Implement broader P7 minimal synthetic/local parser-reader smoke only.
```

That task must remain limited to the exact approved future files and direct
docs/governance synchronization. It must not add a fixture or data file by
default, must not use real data, must not approve source or ingestion, must
not become broad parser / reader / ingestion, must not add CLI or broad file
ingestion, must not extract features, must not generate labels, must not
construct a dataset, must not create splits or leakage tests, must not train,
must not implement model / trainer / checkpoint / weights, must not implement
evaluation, must not integrate model output, must not self-play, must not run
league, must not enter P8-P12 and must not make model-strength claims.

## Planning Decision

```text
Approved for next exact minimal implementation task: Implement broader P7
minimal synthetic/local parser-reader smoke only. This approval is limited to
the exact synthetic/local parser-reader smoke scope and exact approved files.
It does not approve broader P7 implementation, source approval, source
ingestion, broad parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, split creation,
leakage-test implementation, training-data approval, training-run approval,
training, model architecture implementation, trainer implementation,
checkpoint, weights, evaluation implementation, model-output integration,
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ 10.68 comparison, candidate promotion, real data, self-play,
league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 minimal synthetic/local parser-reader smoke approval-decision evidence only.
```

## Explicit Non-Evidence

This approval decision is not:

- implementation execution.
- production code.
- tests.
- fixtures.
- data files.
- broader P7 implementation approval.
- source approval.
- source ingestion.
- broad parser / reader / ingestion approval.
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
