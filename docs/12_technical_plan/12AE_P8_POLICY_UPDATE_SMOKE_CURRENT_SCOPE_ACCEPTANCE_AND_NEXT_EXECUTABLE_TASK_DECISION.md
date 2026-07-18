# 12AE_P8_POLICY_UPDATE_SMOKE_CURRENT_SCOPE_ACCEPTANCE_AND_NEXT_EXECUTABLE_TASK_DECISION

## Scope

This document decides current-scope acceptance for the exact single-record P8
policy-update smoke and directly approves one materially progressive executable
task. It is the decision required by `10_NEXT`, not another boundary or
proposal.

No code, test, fixture, data, model, environment, self-play, training or
evaluation is added in this decision.

## Reviewed Basis

- `12AC` approved the exact single-record implementation.
- commits `a7c83d5` and `7089307` implemented the smoke and exact blocker fix.
- `12AD` records `A. Review can close after blocker fix.`
- 12 focused tests and 46 approved regression tests pass.
- public API, dataclass fields, formulas, warnings and evidence grade remain
  within `12AC`.
- no real/external/platform data or broad P8/P9-P12 path exists.

## Current-Scope Acceptance Decision

```text
ACCEPTED as current-scope complete.
```

Acceptance is limited to:

- one already-loaded project-authored synthetic/local record.
- one deterministic standard-library tabular action-value numerical update.
- exact terminal/non-terminal target, TD-error and updated-value formulas.
- exact provenance, identifier, finite-number and output validation.
- executable synthetic/local numerical smoke evidence only.

It does not accept an RL algorithm as project mainline, an environment,
episode, gameplay, self-play, model, optimizer, training loop, evaluation,
artifact, dataset, real data, strength evidence, broad P8 or P9-P12.

## Next Executable Outcome Selection

Selected:

```text
An exact deterministic two-step chained policy-update sequence smoke.
```

This is materially beyond one isolated update because it verifies ordered
state continuity across two validated updates. It remains small enough to need
no environment, episode runner, self-play, model, optimizer or persistence.

## Exact Approved Next Task

```text
Implement exact minimal P8 synthetic/local two-step policy-update sequence smoke only.
```

No further proposal, boundary, review or approval task may precede this code
task.

## Exact Approved Files

The next task may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_update_sequence_smoke.py`
- `tests/rl/test_synthetic_policy_update_sequence_smoke.py`
- direct docs/governance synchronization.

It must not modify the reviewed single-record implementation or test unless a
genuine blocker is found and recorded before commit. No fixture or data file
is approved.

## Exact Approved API

The sequence module may expose only the equivalent of:

```text
SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION
SyntheticPolicyUpdateSequenceSmokeError
SyntheticPolicyUpdateSequenceResult       # frozen dataclass
apply_synthetic_policy_update_sequence_smoke(
    input_records,
    *,
    learning_rate,
    discount_factor,
)
```

It must reuse `SyntheticPolicyUpdateInput`, `SyntheticPolicyUpdateResult` and
`apply_synthetic_policy_update_smoke`; it must not duplicate the base update
formula or add a second single-step implementation.

## Exact Input Boundary

`input_records` must be an in-memory tuple containing exactly two
`SyntheticPolicyUpdateInput` objects.

Required sequence invariants:

- record IDs are non-empty, valid and distinct.
- both records have identical `source_kind`, `state_id` and `action_id`.
- all provenance flags satisfy the existing synthetic/local helper.
- the first record is non-terminal and has a finite next value.
- the second record is terminal and has `next_max_action_value=None`.
- the second `current_action_value` exactly equals the first computed
  `updated_action_value`.
- the same finite `learning_rate` and `discount_factor` apply to both steps.

Strings, bytes, bytearrays, mappings, lists, paths and arbitrary iterables are
not accepted as the top-level sequence. There is no path, file, URL, fixture,
reader, parser or ingestion API.

## Exact Sequence Semantics

1. Validate the exact tuple shape and cross-record identity constraints.
2. Apply the existing single-record helper to the first record.
3. Require exact continuity from first updated value to second current value.
4. Apply the existing single-record helper to the second record.
5. Return one immutable deterministic sequence summary.

Any base `SyntheticPolicyUpdateSmokeError` must be wrapped as
`SyntheticPolicyUpdateSequenceSmokeError` with the failing step index and the
base exception chained. Inputs must not be mutated. Repeated identical calls
must return equal results.

This is not an episode or environment transition. The two records are
project-authored numerical smoke inputs only.

## Exact Output Boundary

The frozen result may contain only:

```text
sequence_version
step_count = 2
record_ids
source_kind
state_id
action_id
learning_rate
discount_factor
initial_action_value
intermediate_action_value
final_action_value
step_results
sequence_applied = true
safety_guardrails_all_satisfied = true
evidence_grade
warnings
```

`step_results` is the exact two-element tuple of existing frozen single-step
results. Warnings must include at least:

- synthetic/local two-step numerical smoke only.
- not an environment or episode.
- not self-play.
- not production training.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The next test module must cover:

1. exact first and second update formulas plus final value.
2. exact two-record tuple requirement and top-level type rejection.
3. first non-terminal / second terminal ordering.
4. identical source/state/action identity and distinct record IDs.
5. exact intermediate-value continuity rejection.
6. base validation error wrapping with step index and chained cause.
7. deterministic repeated output and input immutability.
8. frozen result, exact output fields, evidence grade and warnings.
9. import through `mjlabai.rl`.
10. absence of path/fixture/dependency/environment/self-play/model/training APIs.

Validation commands:

```text
python3 -m unittest tests/rl/test_synthetic_policy_update_sequence_smoke.py
python3 -m unittest tests/rl/test_synthetic_policy_update_smoke.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
git diff --check
```

## Forbidden Scope

The approval does not permit:

- a third step, variable-length batch, replay buffer, episode or environment.
- action selection, legal-action logic, observations, game state or rewards
  derived from gameplay.
- model/network, tensor, autograd, optimizer, gradient or training loop.
- evaluation, benchmark, checkpoint, artifact, persistence or CLI.
- path/file/URL input, parser/reader/ingestion or new dependency.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- nondeterminism, timing, concurrency, GPU/distributed work or third-party
  binaries/services.
- broad P8, self-play, league, model-strength claims or P9-P12.

## Rollback And Stop Conditions

If implementation needs any unapproved file, input, behavior, dependency or
evidence claim:

- stop before commit.
- do not widen scope silently.
- record the exact blocker in governance and set one exact fix/defer task.
- remove only task-owned changes if rollback is required; preserve unrelated
  user work.

## Evidence Grade

Current decision evidence:

```text
P8 exact policy-update smoke current-scope acceptance and next-task approval evidence only.
```

Future passing implementation evidence:

```text
P8 synthetic/local two-step numerical policy-update sequence smoke evidence only.
```

Neither is model-strength, Tenhou ranked, stable-dan, LuckyJ comparison,
candidate-promotion, production-training or P9-P12 evidence.

## Gate Accounting

```text
single-record current-scope acceptance = satisfied by this decision
next exact task approval = satisfied by this decision
next exact file/API/input/output/test boundaries = satisfied by this decision
remaining mandatory gate count before the exact two-step implementation = 0
```

No gate is satisfied for broader P8.
