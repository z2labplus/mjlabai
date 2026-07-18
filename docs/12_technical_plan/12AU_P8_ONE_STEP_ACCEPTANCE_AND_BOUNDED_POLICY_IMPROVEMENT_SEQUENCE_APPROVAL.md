# 12AU_P8_ONE_STEP_ACCEPTANCE_AND_BOUNDED_POLICY_IMPROVEMENT_SEQUENCE_APPROVAL

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact bounded implementation task.
```

The exact one-step closed loop implemented in `22828c3` and reviewed in
`12AT` is accepted only for its fixed synthetic/local scope.

Next executable task:

```text
Implement exact bounded P8 synthetic/local policy-improvement sequence smoke
only.
```

No proposal, boundary or additional approval may be inserted before code.

## Exact Approved Files

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_improvement_sequence_smoke.py`
- `tests/rl/test_synthetic_policy_improvement_sequence_smoke.py`
- direct docs/governance synchronization.

No fixture/data, path/CLI, dependency, persistence, checkpoint or artifact is
approved.

## Exact Public API

```text
SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION
MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS
SyntheticPolicyImprovementStepInput
SyntheticPolicyImprovementSequenceSmokeError
SyntheticPolicyImprovementSequenceResult
run_synthetic_policy_improvement_sequence_smoke
```

The module must reuse `run_synthetic_one_step_policy_improvement_smoke` and
must not copy decision, action-value, training or one-step orchestration logic.

## Exact Step Input

`SyntheticPolicyImprovementStepInput` is frozen and contains only:

```text
step_id
decision_probes
candidate_transition_batches
learning_rate
discount_factor
```

The sequence helper accepts one exact initial reviewed linear model and one
exact tuple of 1 through 4 exact step inputs.

Requirements:

- `MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS = 4`.
- step IDs are non-empty exact strings and pairwise distinct.
- each step's probes, batches and numeric parameters are validated by the
  reviewed one-step helper.
- all candidate transition IDs across all selected and unselected batches in
  all steps are globally pairwise distinct before a success result returns.
- lists, mappings, generators, paths and tuple subclasses are rejected for the
  outer step tuple.

## Exact Sequence Semantics

1. validate exact outer tuple and hard `1..4` step count.
2. initialize current model from the exact initial model.
3. iterate step inputs once in deterministic input order with one bounded
   standard-library `for` loop.
4. call the reviewed one-step helper exactly once per step.
5. pass each step result's `training_result.final_model` directly as the next
   step's initial model.
6. wrap one-step failures with one-based step index and chained cause.
7. reject duplicate transition IDs globally across every candidate batch.
8. return frozen initial/final model and ordered step history without mutation.

No retry, early stop, convergence rule, shuffle, random sampling, alternate
batch execution, general environment, episode generation, replay or self-play
is approved.

## Exact Result

`SyntheticPolicyImprovementSequenceResult` is frozen and contains only:

```text
sequence_version
step_count
max_steps
initial_model
final_model
step_ids
step_results
selected_actions
after_actions
global_candidate_transition_record_ids
sequence_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

- `1 <= step_count <= 4`, `max_steps = 4`.
- each step result is the reviewed frozen one-step result in input order.
- selected/after actions and IDs derive only from step results/inputs.
- global candidate IDs contain `8 * step_count` distinct IDs in step/batch/
  record order.
- sequence/safety flags are true.

Warnings must state bounded synthetic/local sequence only, maximum four steps,
one reviewed closed-loop call per step, no general environment/episode/replay/
self-play, no persistence/checkpoint/external dependency, not production
training/evaluation, action changes are not policy-quality/strength evidence,
not LuckyJ/stable-dan and not candidate promotion.

## Exact Tests

Focused tests must cover:

1. exact one-step sequence output.
2. exact two-step model continuity and selected/after actions.
3. lower/upper limits: empty and five rejected, four accepted.
4. exact outer tuple/type and tuple-subclass rejection.
5. exact frozen step input, non-empty/distinct step IDs.
6. global candidate transition-ID uniqueness across steps.
7. one-step helper call count/order and model continuity; no copied logic.
8. one-based step error wrapping with chained cause.
9. deterministic equality, complete input non-mutation and frozen output.
10. exact fields/counts/IDs/evidence/warnings and narrow package surface.

Validation must include the 146 approved regressions, focused tests,
`compileall` and `git diff --check`.

## Forbidden Scope And Evidence

No more than four steps, unbounded loop, general environment/transition
function, episode generation, self-play, replay, stochastic exploration,
dynamic data, model loading, persistence/checkpoint, production evaluation,
real Tenhou/haifu, external logs, platform data, path/CLI, dependency, strength
claim, broad P8 or P9-P12 is approved.

Future passing evidence is only:

```text
P8 exact bounded synthetic/local policy-improvement sequence smoke evidence
only.
```

It is not environment/self-play, production training/evaluation, policy-
quality, model-strength, Tenhou, stable-dan, LuckyJ or promotion evidence.

## Gate Accounting

```text
one-step current-scope acceptance = satisfied
bounded sequence approval = satisfied
exact file/API/input/continuity/output/test boundaries = satisfied
remaining mandatory gate count before implementation = 0
```
