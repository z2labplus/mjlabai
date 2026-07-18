# 12AG_P8_TWO_STEP_SEQUENCE_ACCEPTANCE_AND_INTERLEAVED_TRACE_APPROVAL_DECISION

## Scope

This document decides current-scope acceptance for the exact `12AE`
implementation closed by `12AF` and directly approves one materially
progressive executable P8 task. It is not another boundary or proposal.

No code, test, fixture, data, environment, self-play, model, optimizer,
training or evaluation is added in this decision.

## Reviewed Basis

- commit `f238f3d0e88d700701a1eae29aae24f2b8b81019` contains the exact
  two-step implementation.
- `12AF` records `A. Review can close.`
- all 10 sequence tests, 12 base tests and 46 approved regressions pass.
- compile/diff checks and additional tuple/error-chain probes pass.
- no correctness, provenance, scope, evidence or test blocker remains.

## Current-Scope Acceptance Decision

```text
ACCEPTED as current-scope complete.
```

Acceptance is limited to:

- one exact tuple of two project-authored synthetic/local records.
- one state-action key shared by both records.
- one non-terminal update followed by one terminal update.
- exact intermediate-value continuity.
- deterministic reuse of the reviewed single-step numerical helper.
- P8 synthetic/local two-step numerical smoke evidence only.

It does not accept an RL algorithm as mainline, an environment, episode,
gameplay, self-play, model, optimizer, variable training loop, evaluation,
artifact, dataset, real data, strength evidence, broad P8 or P9-P12.

## Next Executable Outcome Selection

Selected:

```text
An exact deterministic four-record interleaved two-key policy-update trace
smoke.
```

This is materially beyond the accepted two-record chain because it verifies
independent continuity for two distinct state-action keys while their updates
are interleaved. It is more useful than merely adding a third update, but it
remains fixed, deterministic and in-memory and does not become a variable
training loop, replay buffer, environment or self-play system.

## Exact Approved Next Task

```text
Implement exact minimal P8 synthetic/local four-record interleaved policy-update trace smoke only.
```

No further proposal, boundary, review or approval task may precede this code
task.

## Exact Approved Files

The next task may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_update_trace_smoke.py`
- `tests/rl/test_synthetic_policy_update_trace_smoke.py`
- direct docs/governance synchronization.

It must not modify the reviewed base or two-step modules/tests unless a genuine
blocker is found and recorded before commit. No fixture or data file is
approved.

## Exact Approved API

The trace module may expose only the equivalent of:

```text
SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION
SyntheticPolicyUpdateTraceSmokeError
SyntheticPolicyUpdateTraceResult       # frozen dataclass
apply_synthetic_policy_update_trace_smoke(
    input_records,
    *,
    learning_rate,
    discount_factor,
)
```

It must reuse `SyntheticPolicyUpdateInput`, `SyntheticPolicyUpdateResult` and
`apply_synthetic_policy_update_smoke`. It must not duplicate the base formula
or create a second single-step updater.

## Exact Input Boundary

`input_records` must be an exact in-memory tuple containing exactly four
`SyntheticPolicyUpdateInput` objects.

Let the two distinct state-action keys be:

```text
key A = (state_id A, action_id A)
key B = (state_id B, action_id B)
```

Required exact order:

```text
step 1 = key A, non-terminal first occurrence
step 2 = key B, non-terminal first occurrence
step 3 = key A, terminal second occurrence
step 4 = key B, terminal second occurrence
```

Required invariants:

- all four record IDs are valid and pairwise distinct.
- all four records have the same canonical synthetic/local `source_kind`.
- exactly two distinct `(state_id, action_id)` keys exist.
- step 1 and step 3 have key A; step 2 and step 4 have key B.
- key A and key B are not equal.
- steps 1 and 2 are non-terminal and have finite next values.
- steps 3 and 4 are terminal and have `next_max_action_value=None`.
- step 3 `current_action_value` exactly equals step 1
  `updated_action_value`.
- step 4 `current_action_value` exactly equals step 2
  `updated_action_value`.
- the same finite `learning_rate` and `discount_factor` apply to all steps.
- all base provenance, identifier and numeric guardrails remain mandatory.

Strings, bytes, bytearrays, mappings, lists, paths, tuple subclasses and
arbitrary iterables are rejected as top-level input. There is no path, file,
URL, fixture, reader, parser or ingestion API.

## Exact Trace Semantics

1. Validate the exact tuple shape, element types, unique IDs, source identity
   and A/B/A/B key pattern.
2. Validate first-occurrence non-terminal and second-occurrence terminal
   ordering.
3. Apply the existing single-step helper to step 1 and step 2 in input order.
4. Require exact key-A continuity, then apply the existing helper to step 3.
5. Require exact key-B continuity, then apply the existing helper to step 4.
6. Return one immutable deterministic trace summary.

Any base `SyntheticPolicyUpdateSmokeError` must be wrapped as
`SyntheticPolicyUpdateTraceSmokeError` with the failing one-based step index
and the base exception chained. Inputs must not be mutated. Repeated identical
calls must return equal results.

This trace is not an episode, environment transition, replay buffer, optimizer
step or training epoch. The four records are project-authored numerical smoke
inputs only.

## Exact Output Boundary

The frozen result may contain only:

```text
trace_version
step_count = 4
record_ids
source_kind
learning_rate
discount_factor
state_action_keys
initial_action_values
intermediate_action_values
final_action_values
step_results
trace_applied = true
safety_guardrails_all_satisfied = true
evidence_grade
warnings
```

Exact tuple shapes:

- `record_ids`: four strings in input order.
- `state_action_keys`: `(key A, key B)`.
- `initial_action_values`: values from steps 1 and 2.
- `intermediate_action_values`: updated values from steps 1 and 2.
- `final_action_values`: updated values from steps 3 and 4.
- `step_results`: four existing frozen single-step results in input order.

Warnings must include at least:

- synthetic/local four-record interleaved numerical smoke only.
- not an environment, episode or replay buffer.
- not self-play.
- not a variable or production training loop.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The next test module must cover:

1. exact four-step A/B/A/B formulas and both final values.
2. exact four-record tuple and top-level type rejection, including tuple
   subclasses.
3. exactly two distinct state-action keys and exact A/B/A/B ordering.
4. pairwise-distinct record IDs and shared synthetic/local source kind.
5. first-occurrence non-terminal / second-occurrence terminal ordering.
6. exact independent continuity rejection for key A and key B.
7. base validation error wrapping with one-based step index and chained cause.
8. deterministic repeated output and input immutability.
9. frozen result, exact fields/tuple shapes, evidence grade and warnings.
10. import through `mjlabai.rl`.
11. absence of path/fixture/dependency/environment/episode/replay/self-play/
    model/optimizer/training APIs and absence of duplicated update formula.

Validation commands:

```text
python3 -m unittest tests/rl/test_synthetic_policy_update_trace_smoke.py
python3 -m unittest tests/rl/test_synthetic_policy_update_sequence_smoke.py
python3 -m unittest tests/rl/test_synthetic_policy_update_smoke.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
python3 -m compileall -q src/mjlabai/rl tests/rl
git diff --check
```

## Forbidden Scope

The approval does not permit:

- any input length other than four or key pattern other than A/B/A/B.
- a generic batch/epoch/trainer, replay buffer, dataset or persistence.
- environment, episode, gameplay, observation, legal-action or action-selection
  behavior.
- self-play, model/network, tensor, autograd, gradient, optimizer or training
  loop.
- evaluation, benchmark, checkpoint, artifact, path/CLI or new dependency.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- nondeterminism, timing, concurrency, GPU/distributed work or third-party
  binaries/services.
- broad P8, league, model-strength claims or P9-P12.

## Rollback And Stop Conditions

If implementation needs an unapproved file, input shape, behavior, dependency
or evidence claim:

- stop before commit.
- do not widen scope silently.
- record the exact blocker and create only one exact fix/defer task.
- remove only task-owned changes if rollback is required.

## Evidence Grade

Current decision evidence:

```text
P8 exact two-step sequence current-scope acceptance and interleaved-trace task
approval evidence only.
```

Future passing implementation evidence:

```text
P8 synthetic/local four-record interleaved two-key numerical policy-update
trace smoke evidence only.
```

Neither is self-play, production training, model-strength, Tenhou ranked,
stable-dan, LuckyJ comparison, candidate-promotion or P9-P12 evidence.

## Gate Accounting

```text
two-step current-scope acceptance = satisfied by this decision
next exact task approval = satisfied by this decision
next exact file/API/input/output/test boundaries = satisfied by this decision
remaining mandatory gate count before the exact trace implementation = 0
```

No gate is satisfied for broader P8.
