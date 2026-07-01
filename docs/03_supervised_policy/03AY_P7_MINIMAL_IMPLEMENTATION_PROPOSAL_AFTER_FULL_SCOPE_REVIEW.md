# 03AY_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_AFTER_FULL_SCOPE_REVIEW

## Scope

This document drafts a P7 minimal implementation proposal after the P7 full
scope expansion plan review in `03AX`.

This task only drafts a proposal. It is not:

- proposal approval.
- implementation approval.
- implementation execution.
- production code.
- tests.
- fixtures.
- data files.
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

## Proposal Summary

Chosen candidate class:

```text
Project-authored synthetic/local parser-reader smoke extension proposal
```

This is the safest next P7 proposal because it stays close to the accepted
synthetic/local parser-reader smoke current scope, requires no real data,
requires no source approval, reads no external source, emits no feature or
label payload, and can be specified as a future exact implementation task with
two candidate files only.

The candidate is synthetic/local only because future inputs would be limited
to already-loaded project-authored synthetic/local in-memory records or
explicitly approved existing project-authored synthetic/local fixtures. It
does not require real data, Tenhou logs, haifu, platform data, account data,
source ingestion or broad file ingestion.

This proposal does not approve implementation. It must be reviewed later, and
any implementation must require a separate approval decision before it can be
placed in `docs/10_next/10_NEXT.md` as an exact implementation task.

## Candidate Class And Status

```text
candidate_class:
Project-authored synthetic/local parser-reader smoke extension proposal

current_status:
proposal draft only

approved_now:
No

execution_allowed_now:
No

proposal_review_required:
Yes

approval_decision_required:
Yes

implementation_task_required:
Yes, only after separate approval decision and exact 10_NEXT implementation task.
```

## Exact Goal

Future exact goal, if later reviewed and approved:

- define a tiny synthetic/local-only parser-reader smoke extension candidate.
- use only project-authored synthetic/local artifacts.
- accept only already-loaded in-memory synthetic/local records unless an
  existing project-authored synthetic/local fixture is explicitly approved for
  read-only test use in a later approval decision.
- produce only a JSON-safe smoke summary, normalized synthetic/local record
  summary or manifest-style validation summary.
- preserve provenance and guardrail flags.
- never emit feature tensors, labels, targets, supervised examples, splits,
  datasets, training data, model input, model output, evaluation result or
  evidence claims.

## Exact Non-Goals

The proposal explicitly excludes:

- no source approval.
- no source ingestion.
- no real data.
- no real Tenhou.
- no real haifu.
- no external logs.
- no platform data.
- no account / session / cookie / token.
- no arbitrary path reading.
- no broad file ingestion.
- no CLI.
- no feature extraction.
- no label generation.
- no feature tensors.
- no labels.
- no targets.
- no supervised examples.
- no dataset.
- no splits.
- no leakage-test implementation.
- no training data.
- no training.
- no model / trainer.
- no checkpoint / weights.
- no evaluation implementation.
- no model-output integration.
- no model-strength evidence.
- no Tenhou / stable-dan / LuckyJ / promotion claims.
- no P8-P12.

## Candidate Future Files

Candidate future files, if a later proposal review and approval decision
approve them:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

These files are not approved for editing or creation in this task.

Do not create these files now.
Do not edit these files now.
Do not approve these files now.

## Explicitly Excluded Files

The proposal does not approve editing or creating:

- existing implementation files unless separately approved.
- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`
- real-data directories.
- CLI files.
- model / trainer / dataloader / optimizer / loss files.
- evaluation / metric / runner / benchmark harness files.
- P8-P12 files.
- third-party artifacts.
- account / session / cookie / token files.
- `.env`, dotfiles and secrets.

## Allowed Inputs

Allowed future inputs, if later approved, are limited to:

- project-authored synthetic/local in-memory records.
- existing project-authored synthetic/local fixtures if explicitly approved
  later.
- JSON-safe synthetic/local smoke records.
- no real or external data.

## Forbidden Inputs

Forbidden inputs:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token.
- hidden files / dotfiles.
- `.env` / secrets.
- model outputs.
- generated labels.
- human labels from real play.
- self-play outputs.
- league outputs.
- third-party binaries / weights / checkpoints / params.
- arbitrary user-supplied paths.
- broad directories.
- unapproved sources.
- real external data.

## Allowed Outputs

Allowed future outputs, if later approved, are limited to:

- JSON-safe smoke summary.
- normalized synthetic/local record.
- validation summary.
- provenance / guardrail flags.
- local unit-test pass/fail evidence.
- docs/governance evidence entries.

## Forbidden Outputs

Forbidden outputs:

- feature tensors.
- labels.
- targets.
- supervised examples.
- splits.
- datasets.
- training data.
- model inputs.
- model outputs.
- evaluation results.
- model-strength evidence.
- Tenhou / stable-dan / LuckyJ / promotion evidence.

## Dependency Status

| Dependency | Current status | Notes |
|---|---|---|
| source dependency | not approved | The proposal cannot rely on any real or external source. |
| source approval dependency | not approved | No source is approved for training, ingestion or feature/label use. |
| parser / reader / ingestion dependency | out of scope | Current accepted parser-reader smoke is synthetic/local only and not broad ingestion. |
| feature / label dependency | not approved | No actual feature extraction or label generation is approved. |
| dataset / split / leakage dependency | not approved | No dataset construction, split creation or leakage-test implementation is approved. |
| training-data dependency | not approved | No training data is approved or constructed. |
| model / trainer dependency | not approved | No model architecture, trainer, dataloader, optimizer, loss, checkpoint or weights are approved. |
| evaluation dependency | not approved | No evaluation implementation, metric implementation, runner or benchmark harness is approved. |
| model-output dependency | blocked | Model-output integration remains blocked until later model/trainer/evaluation approvals exist. |
| real-data dependency | blocked | Real Tenhou, real haifu, external logs and platform data remain blocked. |
| P8-P12 dependency | later-stage | Self-play, league, RL and Tenhou target validation remain later-stage and unapproved. |

## Candidate Future Validation Commands

Candidate future validation commands, if later approved:

```text
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
```

These are candidates only. They are not run now as future tests because the
future files do not exist and are not approved for creation in this task. They
are not permission to create tests and not permission to implement code.

Current validation commands for this docs-only task:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Rollback Plan

Future rollback plan, if a later implementation is approved and fails:

- revert the exact future implementation commit.
- remove only the exact future implementation files approved for that task.
- preserve existing synthetic/local smoke artifacts.
- expect no real-data deletion because real data must not be used.
- update docs/governance if the future implementation fails.
- stop if rollback would touch unrelated files.

## Stop Conditions

Stop if:

- proposal wording implies approval.
- proposal wording implies implementation can start immediately.
- proposal requires real data.
- proposal requires source approval.
- proposal requires source ingestion.
- proposal requires broad ingestion.
- proposal requires CLI.
- proposal emits features / labels / examples / dataset.
- proposal touches training / model / evaluation.
- proposal touches model output.
- proposal touches P8-P12.
- proposal makes model-strength / Tenhou / LuckyJ / promotion claims.
- exact future files are unclear.
- rollback is unclear.
- governance sync is unclear.

## Risk Controls

- Proposal draft mistaken for approval: mark `approved_now = No` and require
  proposal review plus separate approval decision.
- Candidate files mistaken for edit permission: list future files explicitly
  as not approved for editing or creation now.
- Synthetic/local smoke mistaken for real pipeline: limit inputs and outputs
  to JSON-safe synthetic/local smoke summaries.
- Source approval gap: keep source approval dependency `not approved`.
- Parser / reader / ingestion creep: forbid arbitrary paths, broad
  directories, CLI and real/external sources.
- Feature / label creep: forbid feature tensors, labels, targets and examples.
- Dataset / training creep: forbid datasets, splits, training data, training
  runs and checkpoints.
- Evaluation / model-output creep: forbid evaluation results, model outputs,
  metrics, runners and benchmark harnesses.
- P8-P12 creep: keep self-play, league, RL and Tenhou target validation
  later-stage.
- Model-strength overclaim: use proposal-draft evidence only.
- Governance mismatch: update `10_NEXT`, handoff, evidence, risk, decision,
  stage contract, backlog and milestones together.

## Evidence Grade

```text
P7 minimal implementation proposal draft evidence only.
```

Explicit non-evidence:

- not proposal approval.
- not implementation approval.
- not source approval.
- not ingestion.
- not feature extraction.
- not label generation.
- not dataset.
- not training.
- not model.
- not evaluation.
- not model-output.
- not model-strength evidence.
- not P8-P12 evidence.

## Approval Separation

Lifecycle:

1. proposal draft.
2. proposal review.
3. separate approval decision.
4. exact implementation prompt only if approved.
5. implementation execution.
6. implementation review.
7. current-scope acceptance if warranted.

This task only performs step 1.

## First Task Candidate

If this proposal draft has no blocker, the next task should be:

```text
Review P7 minimal implementation proposal before approval decision.
```

The next task must be a docs-only proposal review. It is not proposal
approval, implementation, code, tests, fixtures, data files, source approval,
ingestion, feature / label work, dataset construction, training, evaluation,
model-output integration or P8-P12.
