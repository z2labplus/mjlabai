# 03BC_P7_PARSER_READER_SMOKE_EXTENSION_REVIEW_BLOCKER_RESOLUTION_APPROVAL_DECISION

## Scope

This document prepares and records the approval decision for resolving the
P7 parser-reader smoke extension review blocker found in `03BB`.

This task is docs-only approval-decision preparation. It is not:

- blocker fix execution.
- test modification.
- production code modification.
- fixture creation.
- data-file creation.
- source approval.
- source ingestion.
- parser / reader / ingestion implementation.
- feature extraction.
- label generation.
- dataset construction.
- training.
- evaluation.
- model-output integration.
- model-strength evidence.
- P8-P12 entry.

North-star relationship: this decision supports the long-term Tenhou stable-dan
`> 10.68` target only by keeping the P7 synthetic/local parser-reader smoke
extension review path auditable before any future supervised-learning work can
depend on it. It is not model-strength evidence, Tenhou ranked evidence,
stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
candidate-promotion evidence.

## Reviewed Blocker

`03BB` reviewed the exact `03BA` implementation files:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

`03BB` recorded:

```text
Review cannot close because blockers exist.
```

The blocker is:

- missing explicit top-level `bytes` rejection test.
- missing explicit top-level `bytearray` rejection test.
- missing explicit top-level `Mapping` rejection-as-records-collection test.

Clarifications:

- The implementation logic already contains these guards.
- Existing validation commands pass.
- The blocker is a review-prompt coverage completeness blocker.
- The blocker is not implementation scope drift.
- The blocker is not a production-code defect.
- The blocker does not show source approval, source ingestion, broad parser /
  reader / ingestion, feature extraction, label generation, dataset
  construction, training, evaluation, model-output integration, real-data use
  or P8-P12 drift.

## Decision Options

| option | meaning | selected |
| --- | --- | ---: |
| Approved for next exact test-only blocker-resolution task. | A later exact `10_NEXT` task may add only the missing explicit rejection tests. | yes |
| Deferred pending blocker or clarification. | No blocker-resolution implementation is approved; a docs-only clarification task is needed. | no |
| Rejected / not approved. | No blocker-resolution implementation is approved. | no |

## Decision

```text
Approved for next exact test-only blocker-resolution task.
```

This approval is not implementation execution.

This approval is not production-code approval.

This approval is not broader P7 implementation approval.

This approval is not full P7 closure.

This approval is not source approval.

This approval is not source ingestion.

This approval is not feature extraction.

This approval is not label generation.

This approval is not dataset construction.

This approval is not training.

This approval is not evaluation.

This approval is not model-output integration.

This approval is not P8-P12 entry.

## Approved Future Task If Approved

Exact approved future task:

```text
Add explicit P7 parser-reader smoke extension rejection tests only.
```

The future task must be limited to resolving the exact `03BB` test coverage
blocker. It may not become production-code work, fixture work, source work,
ingestion work, feature/label work, dataset work, training work, evaluation
work, model-output work or P8-P12 work.

## Exact Approved Future File If Approved

Only this future file is approved:

- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

No production code file is approved by default.

No fixture or data file is approved by default.

No docs beyond direct governance synchronization are approved by default.

If the future test-only change reveals that production code needs modification,
the future task must stop and create a separate approval path.

## Allowed Future Test Additions If Approved

The next exact task may add only explicit coverage for:

1. top-level `bytes` input is rejected.
2. top-level `bytearray` input is rejected.
3. top-level `Mapping` as records collection is rejected.

Allowed implementation style:

- use the existing `unittest` style.
- call the existing public extension API.
- assert `SyntheticParserReaderSmokeExtensionError` or collected error
  messages.
- add no new fixtures.
- use no real data.
- read no filesystem paths.
- use no external logs.
- use no platform data.

## Forbidden Future Edits If Approved

The next exact task must not:

- modify `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`.
- modify `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`.
- modify `src/mjlabai/supervised/feature_label_schema.py`.
- modify any fixture.
- add fixtures.
- add data files.
- read real data.
- add CLI.
- implement ingestion.
- add feature extraction.
- add label generation.
- build datasets.
- train.
- evaluate.
- integrate model output.
- enter P8-P12.

## Future Validation Commands If Approved

The future exact test-only blocker fix must run:

```bash
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Current Validation Commands

This approval-decision task uses only existing validation commands and does not
modify tests to change coverage:

```bash
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Future Stop Conditions

The future exact blocker fix must stop if:

- any production code change is needed.
- any fixture or data file is needed.
- any real or external data is needed.
- the test-only change requires source approval or ingestion.
- the test-only change requires feature extraction, label generation, dataset
  construction, training, evaluation or model-output integration.
- the test-only change expands into broad parser / reader / ingestion.
- validation fails.
- governance synchronization cannot remain consistent.

## Rollback Plan

If the future exact blocker fix needs rollback:

- revert the exact future test-only blocker-resolution commit.
- remove only added or changed test assertions in
  `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`.
- preserve the production extension module.
- preserve existing fixtures and data files.
- update governance if the fix is reverted.
- stop if rollback would touch unrelated files.

## Risk Controls

| Risk | Control |
| --- | --- |
| Approval decision is mistaken for test modification. | This document states that no blocker fix is executed in this task. |
| Test-only approval is mistaken for production-code approval. | Exact approved future file excludes all production code. |
| Blocker fix expands beyond three missing explicit tests. | Allowed future additions list exactly three cases. |
| Fixture or data creep occurs. | Fixtures and data files are explicitly forbidden. |
| Real-data creep occurs. | Real data, Tenhou, haifu, external logs and platform data remain forbidden. |
| Source ingestion creep occurs. | Source approval, source ingestion and broad parser / reader / ingestion remain unapproved. |
| Feature / label / dataset / training / evaluation creep occurs. | These workstreams remain explicitly forbidden. |
| Model-output or model-strength overclaim occurs. | Evidence grade is approval-decision evidence only with non-evidence warnings. |
| P8-P12 creep occurs. | P8-P12 remain unapproved and later-stage. |
| Governance mismatch occurs. | `10_NEXT`, handoff, evidence, risks, decisions, stage contract, milestones and backlog are synchronized. |

## Evidence Grade

```text
P7 parser-reader smoke extension review blocker-resolution approval-decision evidence only.
```

Explicit non-evidence:

- not blocker fix execution.
- not production code.
- not fixture.
- not data file.
- not source approval.
- not source ingestion.
- not feature extraction.
- not label generation.
- not dataset construction.
- not training.
- not evaluation.
- not model-output integration.
- not model-strength evidence.
- not P8-P12 evidence.

## Approval Separation

Lifecycle:

1. `03BB` identified the blocker.
2. This task records the blocker-resolution approval decision.
3. Because the decision is approved, the next exact task may add only the
   explicit test coverage listed above.
4. After that, a separate implementation review rerun is required.
5. Only after review can close may current-scope acceptance be considered.

This task executes only step 2.

This task does not execute step 3.

## Next Task

Because the decision is approved, the new first task in
`docs/10_next/10_NEXT.md` is:

```text
Add explicit P7 parser-reader smoke extension rejection tests only.
```

The next task must remain exact test-only blocker resolution:

- only approved file:
  `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`
- no production code.
- no fixtures.
- no data files.
- no real data.
- no source approval.
- no source ingestion.
- no broad parser / reader / ingestion.
- no feature extraction.
- no label generation.
- no dataset construction.
- no training.
- no evaluation.
- no model-output integration.
- no model-strength evidence.
- no self-play.
- no league.
- no P8-P12.
