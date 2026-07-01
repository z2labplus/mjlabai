# 03BA_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_EXTENSION_IMPLEMENTATION_APPROVAL_DECISION

## Scope

This document prepares and records the approval decision for the P7 minimal
synthetic/local parser-reader smoke extension implementation candidate after
the `03AY` proposal and the `03AZ` proposal review.

This task only prepares and records an approval decision. It is not:

- implementation.
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

North-star relationship: this decision supports the long-term Tenhou
stable-dan `> 10.68` target only by allowing one narrowly bounded
synthetic/local P7 guardrail implementation to become auditable later. It is
not model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## Reviewed Proposal Chain

Reviewed proposal chain:

- `03AY` drafted the P7 minimal implementation proposal.
- `03AZ` reviewed the proposal.
- `03AZ` recorded `Review can close`.
- `03AZ` found no blocker.
- This task prepares the approval decision only.

Reviewed documents:

- `docs/03_supervised_policy/03AY_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_AFTER_FULL_SCOPE_REVIEW.md`
- `docs/03_supervised_policy/03AZ_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION.md`
- `docs/03_supervised_policy/03AW_P7_FULL_SCOPE_EXPANSION_PLAN_AFTER_CURRENT_SCOPE_ACCEPTANCE.md`
- `docs/03_supervised_policy/03AX_P7_FULL_SCOPE_EXPANSION_PLAN_REVIEW_AFTER_CURRENT_SCOPE_ACCEPTANCE.md`
- `docs/03_supervised_policy/03AU_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
- `docs/03_supervised_policy/03AV_BROADER_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_IMPLEMENTATION_REVIEW.md`

Reviewed context files only:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`

## Decision Options

| option | meaning | selected |
| --- | --- | ---: |
| Approved for next exact minimal implementation task. | A later exact `10_NEXT` implementation task may create only the exact approved files and scope. | yes |
| Deferred pending blocker or clarification. | Implementation remains closed and a docs-only blocker-resolution or revised proposal task is needed. | no |
| Rejected / not approved. | Implementation remains closed because the proposal is not acceptable. | no |

## Decision

```text
Approved for next exact minimal implementation task.
```

This approval is not implementation execution.

This approval is not broad P7 implementation approval.

This approval is not full P7 closure.

This approval is not source approval.

This approval is not source ingestion.

This approval is not training approval.

This approval is not evaluation approval.

This approval is not P8-P12 entry.

## Approved Future Task If Approved

Exact approved future task:

```text
Implement P7 minimal synthetic/local parser-reader smoke extension only.
```

The future task must remain limited to the exact approved synthetic/local
parser-reader smoke extension scope. It may not become broader P7
implementation.

## Exact Approved Future Files If Approved

The next exact implementation task may create or modify only these
implementation files:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

No other implementation files are approved.

No fixture or data file is approved by default.

Direct docs/governance synchronization may be updated only as needed to record
the future implementation evidence, validation results, risks and next task.

## Explicitly Excluded Files

The next implementation task must not modify these files unless a later
approval decision explicitly amends the exact scope:

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

## Allowed Future Inputs If Approved

The future exact implementation task may use only:

- project-authored synthetic/local in-memory records.
- JSON-safe synthetic/local smoke records.
- existing project-authored synthetic/local fixtures only if explicitly
  allowed later as read-only test input.
- no real or external data.

The approval does not create a general file reader and does not approve
arbitrary paths, broad directories, CLI paths or source ingestion.

## Forbidden Future Inputs If Approved

The future exact implementation task must not use:

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

## Allowed Future Outputs If Approved

The future exact implementation task may output only:

- JSON-safe smoke summary.
- normalized synthetic/local record summary.
- manifest-style validation summary.
- provenance / guardrail flags.
- local unit-test pass/fail evidence.
- docs/governance evidence entries.

## Forbidden Future Outputs If Approved

The future exact implementation task must not output:

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

| Dependency | Status |
|---|---|
| source dependency | not approved |
| source approval dependency | not approved |
| parser / reader / ingestion dependency | limited only to exact synthetic/local smoke extension if approved |
| feature / label dependency | not approved |
| dataset / split / leakage dependency | not approved |
| training-data dependency | not approved |
| model / trainer dependency | not approved |
| evaluation dependency | not approved |
| model-output dependency | blocked |
| real-data dependency | blocked |
| P8-P12 dependency | later-stage |

## Future Validation Commands If Approved

Future implementation validation commands may include:

```text
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

This current approval-decision task must not run the future non-existing test:

```text
tests/supervised/test_synthetic_parser_reader_smoke_extension.py
```

Future validation commands are not current implementation permission beyond
the exact next task approved here.

## Current Validation Commands

Current approval-decision validation is limited to existing commands:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Future Rollback Plan

If the future exact implementation expands scope or fails validation, rollback
must:

- revert the exact future implementation commit.
- remove only the exact future implementation files.
- preserve existing synthetic/local smoke artifacts.
- require no real-data deletion, because no real data may be used.
- update docs/governance if the future implementation fails.
- stop if rollback would touch unrelated files.

## Future Stop Conditions

The future implementation task must stop before commit if any of these occur:

- it needs any file outside the exact approved scope.
- it needs a new fixture or data file.
- it needs real data.
- it needs source approval.
- it needs source ingestion.
- it reads arbitrary paths.
- it adds CLI behavior.
- it becomes broad ingestion.
- it emits feature tensors.
- it emits labels.
- it emits targets.
- it emits supervised examples.
- it constructs a dataset.
- it creates a split.
- it creates leakage checks.
- it trains.
- it touches model / trainer / checkpoint / weights.
- it touches evaluation / metric / runner / harness.
- it touches model-output integration.
- it makes model-strength / Tenhou / LuckyJ / promotion claims.
- it drifts into P8-P12.
- validation fails.
- governance cannot be updated consistently.

## Risk Controls

| risk | control |
| --- | --- |
| Approval decision mistaken for implementation execution. | This document records approval only; implementation is a later `10_NEXT` task. |
| Narrow approval mistaken for broad P7 implementation. | Exact approved future files and future outputs are listed; full P7 remains open. |
| Candidate files mistaken for current edits. | Candidate files are approved only for the next exact implementation task, not this decision task. |
| Synthetic/local smoke extension mistaken for real pipeline. | Inputs remain project-authored synthetic/local and in-memory; real/external data remains forbidden. |
| Source approval gap. | Source dependency and source approval dependency remain not approved. |
| Source ingestion creep. | Source ingestion, arbitrary paths, broad directories and CLI remain forbidden. |
| Parser / reader / ingestion creep. | Approval is limited only to exact synthetic/local smoke extension behavior. |
| Feature / label creep. | Feature tensors, labels, targets and examples are forbidden outputs. |
| Dataset / training creep. | Datasets, splits, training data, training runs, checkpoints and weights are forbidden. |
| Evaluation / model-output creep. | Evaluation results, metric implementation, runners, benchmark harnesses and model outputs are forbidden. |
| Real data / platform / account risk. | Real Tenhou, real haifu, external logs, platform data, accounts, sessions, cookies and tokens remain forbidden. |
| P8-P12 creep. | Self-play, league, RL and later-stage Tenhou validation remain unapproved. |
| Model-strength overclaim. | Evidence grade is approval-decision evidence only and explicit non-evidence warnings are recorded. |
| Governance mismatch. | `10_NEXT`, handoff, index, technical plan, evidence, risk, decision, stage contract, milestones, backlog and changelog must be synchronized. |

## Evidence Grade

```text
P7 minimal synthetic/local parser-reader smoke extension approval-decision evidence only.
```

Explicit non-evidence:

- not implementation.
- not source approval.
- not source ingestion.
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

This task performs only step 3.

This task does not perform step 4 or step 5.

## Next Task

Because the decision is approved, the next first `10_NEXT` task should be:

```text
Implement P7 minimal synthetic/local parser-reader smoke extension only.
```

That task must remain limited to the exact approved future files and direct
docs/governance synchronization. It must not add a fixture or data file by
default, must not use real data, must not approve source or ingestion, must
not become broad parser / reader / ingestion, must not add CLI or broad file
ingestion, must not extract features, must not generate labels, must not
construct a dataset, must not train, must not implement evaluation, must not
integrate model output, must not self-play, must not run league, must not
enter P8-P12 and must not make model-strength claims.

## Planning Decision

```text
Approved for next exact minimal implementation task: Implement P7 minimal
synthetic/local parser-reader smoke extension only. This approval is limited
to the exact synthetic/local parser-reader smoke extension scope and exact
approved files. It does not approve broader P7 implementation, source
approval, source ingestion, broad parser / reader / ingestion, actual feature
extraction, actual label generation, supervised dataset construction, split
creation, leakage-test implementation, training-data approval,
training-run approval, training, model architecture implementation, trainer
implementation, checkpoint, weights, evaluation implementation,
model-output integration, model-strength evidence, Tenhou ranked evidence,
stable-dan ranked-game evidence, LuckyJ 10.68 comparison, candidate
promotion, real data, self-play, league or P8-P12 entry.
```
