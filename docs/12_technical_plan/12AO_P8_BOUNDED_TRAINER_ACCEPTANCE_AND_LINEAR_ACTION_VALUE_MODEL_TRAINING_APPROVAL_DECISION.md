# 12AO_P8_BOUNDED_TRAINER_ACCEPTANCE_AND_LINEAR_ACTION_VALUE_MODEL_TRAINING_APPROVAL_DECISION

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact minimal implementation task.
```

The exact bounded tabular trainer implemented in `cd9cdc1` and reviewed in
`12AN` is accepted only for its 1-through-8-pass synthetic/local scope.

The next executable task is:

```text
Implement exact minimal P8 synthetic/local linear action-value model training
smoke only.
```

This is the first approved P8 smoke that trains parameterized model weights.
No proposal, boundary or additional approval may be inserted before code.

## Why This Outcome

The bounded tabular loop is deterministic, review-closed and has no blocker.
The smallest materially progressive step is a fixed-dimension linear
action-value function trained by deterministic temporal-difference updates on
already-loaded project-authored synthetic/local transitions. This exercises
actual parameterized model training without an environment, self-play,
external dependency, file ingestion, persistence, checkpoint or production
training system.

Another table wrapper or docs-only boundary is forbidden.

## Exact Approved Files

The implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_linear_action_value_training_smoke.py`
- `tests/rl/test_synthetic_linear_action_value_training_smoke.py`
- direct docs/governance synchronization required by repository rules.

No fixture, data file, dependency, CLI, path reader, persistence, checkpoint
or artifact file is approved.

## Exact Public API

The new module may export only:

```text
SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION
LINEAR_ACTION_VALUE_FEATURE_COUNT
LINEAR_ACTION_VALUE_ACTION_COUNT
MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS
SyntheticLinearActionValueTrainingSmokeError
SyntheticLinearQTransition
SyntheticLinearActionValueModel
SyntheticLinearActionValueTrainingResult
train_synthetic_linear_action_value_model_smoke
```

No generic model, optimizer, dataset, dataloader or persistence API is
approved.

## Exact Model Boundary

The model is a frozen two-action linear action-value function over exactly two
real-valued features:

```text
Q(features, action) = bias[action]
                    + weights[action][0] * features[0]
                    + weights[action][1] * features[1]
```

`SyntheticLinearActionValueModel` contains only:

```text
weights
biases
```

Required exact shapes:

```text
weights = ((w00, w01), (w10, w11))
biases = (b0, b1)
```

All six parameters must be finite real numbers, normalized to `float`, and
stored in exact nested tuples. Boolean values, tuple subclasses, lists,
mappings, tensors and arrays are rejected. The initial model is immutable and
must not be mutated.

## Exact Transition Boundary

`SyntheticLinearQTransition` is frozen and contains only:

```text
record_id
source_kind
state_features
action_index
reward
next_state_features
terminal
project_authored
synthetic
local_only
uses_real_data
uses_external_log
uses_platform_data
uses_model_output
uses_self_play
```

The trainer accepts an exact tuple of exactly four exact transition objects.
Record IDs must be non-empty strings and pairwise distinct. `source_kind`
must equal the existing canonical `project_authored_synthetic_local` token.

Each feature vector is an exact tuple of two finite real numbers. Action index
is exact integer `0` or `1` and must not be boolean. Reward is finite. A
terminal transition requires `next_state_features is None`; a non-terminal
transition requires an exact two-feature next-state tuple.

Every provenance flag must enforce project-authored synthetic/local-only use:

```text
project_authored = true
synthetic = true
local_only = true
uses_real_data = false
uses_external_log = false
uses_platform_data = false
uses_model_output = false
uses_self_play = false
```

No path, file, replay, environment, episode, real/external/platform data or
model-generated transition input is approved.

## Exact Training Parameters

```text
learning_rate: finite real, 0 < learning_rate <= 1
discount_factor: finite real, 0 <= discount_factor <= 1
epoch_count: exact int, 1 <= epoch_count <= 8
```

`MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS = 8`. Booleans, non-finite values and
out-of-range values are rejected.

## Exact Training Semantics

The trainer must:

1. validate and normalize the exact model, transition tuple and parameters.
2. create local parameter values without mutating any input.
3. iterate epochs and the four transitions in deterministic input order.
4. compute both current action values from the current parameters.
5. compute the selected-action prediction.
6. compute target:

```text
terminal target = reward
non_terminal target = reward + discount_factor * max(Q(next_features, 0),
                                                      Q(next_features, 1))
```

7. compute `td_error = target - prediction`.
8. update only the selected action row:

```text
weight[action][j] += learning_rate * td_error * state_features[j]
bias[action] += learning_rate * td_error
```

9. accumulate `td_error * td_error` and return one mean value per epoch.
10. return a newly frozen model and frozen deterministic diagnostics.

Exactly `4 * epoch_count` ordered updates occur. No shuffle, minibatch,
optimizer object, autograd, backpropagation framework, target network, replay,
retry, early stop, schedule, convergence rule or random sampling is approved.

## Exact Result

`SyntheticLinearActionValueTrainingResult` is frozen and contains only:

```text
training_version
feature_count
action_count
epoch_count
max_epochs
transition_count
update_count
initial_model
final_model
epoch_mean_squared_td_errors
record_ids
training_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Requirements:

- `feature_count = 2`, `action_count = 2`, `transition_count = 4`.
- `1 <= epoch_count <= 8`, `max_epochs = 8`.
- `update_count = 4 * epoch_count`.
- initial/final models are exact frozen normalized model values.
- epoch mean-squared TD errors are a tuple of finite non-negative floats with
  length `epoch_count`.
- `record_ids` preserves the four transition IDs in input order.
- `training_applied = true`.
- `safety_guardrails_all_satisfied = true`.

Warnings must include at least:

- synthetic/local linear action-value model training smoke only.
- fixed two features, two actions, four transitions and at most eight epochs.
- deterministic ordered temporal-difference updates only.
- no environment, replay buffer, self-play or model-generated data.
- no external dependency, tensor framework, optimizer or checkpoint.
- not production training or evaluation.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The focused test module must cover:

1. exact one-epoch parameter and loss output from a fixed zero model.
2. terminal and non-terminal target behavior.
3. exact two-epoch deterministic carry-forward behavior.
4. epoch lower/upper bounds: zero and nine rejected, eight accepted.
5. exact model nested tuple shapes/types and finite-number normalization.
6. exact four-transition outer tuple/type and tuple-subclass rejection.
7. feature shape/type, action index, reward and terminal consistency.
8. exact provenance flags/source and pairwise-distinct IDs.
9. deterministic ordered update count and selected-action-only updates.
10. repeated equality, complete input non-mutation and frozen output.
11. exact result fields/shapes/counts, evidence grade and warnings.
12. package imports, narrow API and absence of path/file/persistence/
    environment/replay/self-play/checkpoint/production-evaluation APIs.
13. huge finite-but-non-float-representable numeric input is normalized to the
    approved error with chained cause rather than leaking `OverflowError`.

Validation must include the 112 currently approved tests, the new focused
tests, compile checks and `git diff --check`.

## Forbidden Scope

This approval does not permit:

- dimensions other than two features and two actions.
- transition count other than exactly four or more than eight epochs.
- shuffle, minibatch, retry, early stop, convergence or scheduling.
- mutable/dynamic model API, generic optimizer, tensor/autograd framework.
- persistence, serialization, checkpoint, resume or artifact creation/use.
- dataset, dataloader, replay buffer, environment, episode, gameplay,
  legality, action selection or self-play.
- production training/evaluation, metrics, ranking or candidate selection.
- path/CLI, dependency, timing, concurrency, GPU/distributed or third-party
  binary/service use.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- broad P8, league, strength claims or P9-P12.

## Rollback And Stop Conditions

If implementation needs any unapproved file, shape, behavior, dependency or
evidence claim, stop before commit and record one exact blocker without
silently widening scope.

## Evidence Grade

Current decision evidence:

```text
P8 bounded tabular trainer current-scope acceptance and exact synthetic/local
linear action-value model-training task approval evidence only.
```

Future passing implementation evidence:

```text
P8 exact synthetic/local linear action-value model training smoke evidence
only.
```

This is actual fixed synthetic parameter-update execution, but it is not
production model training, environment/self-play training, model-strength,
Tenhou ranked, stable-dan, LuckyJ comparison, candidate-promotion or P9-P12
evidence.

## Gate Accounting

```text
bounded tabular trainer current-scope acceptance = satisfied by this decision
linear model training approval = satisfied by this decision
exact file/API/input/model/formula/output/test boundaries = satisfied
remaining mandatory gate count before implementation = 0
```

No gate is satisfied for broader P8.
