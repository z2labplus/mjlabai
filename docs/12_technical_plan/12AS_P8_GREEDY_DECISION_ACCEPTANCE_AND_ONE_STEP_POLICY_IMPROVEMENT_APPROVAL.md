# 12AS_P8_GREEDY_DECISION_ACCEPTANCE_AND_ONE_STEP_POLICY_IMPROVEMENT_APPROVAL

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact minimal implementation task.
```

The exact greedy-decision diagnostic implemented in `475997a` and reviewed in
`12AR` is accepted only for its fixed synthetic/local scope.

The next executable task is:

```text
Implement exact P8 one-step synthetic/local policy-improvement closed-loop
smoke only.
```

No proposal, boundary or additional approval may be inserted before code.

## Exact Approved Files

The implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_one_step_policy_improvement_smoke.py`
- `tests/rl/test_synthetic_one_step_policy_improvement_smoke.py`
- direct docs/governance synchronization required by repository rules.

No fixture, data file, dependency, CLI, path reader, persistence, checkpoint
or artifact file is approved.

## Exact Public API

The new module may export only:

```text
SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION
SyntheticOneStepPolicyImprovementSmokeError
SyntheticOneStepPolicyImprovementResult
run_synthetic_one_step_policy_improvement_smoke
```

It must reuse:

- `SyntheticLinearActionValueModel`
- `SyntheticLinearDecisionProbe`
- `SyntheticLinearQTransition`
- `run_synthetic_linear_greedy_decision_diagnostic`
- `train_synthetic_linear_action_value_model_smoke`

It must not copy the action-value, greedy-decision, TD-target, TD-error or
parameter-update formulas.

## Exact Input Boundary

The helper signature is:

```text
run_synthetic_one_step_policy_improvement_smoke(
    initial_model,
    decision_probes,
    candidate_transition_batches,
    *,
    learning_rate,
    discount_factor,
)
```

Inputs:

- `initial_model`: exact reviewed frozen linear model.
- `decision_probes`: exact three-probe tuple accepted by the reviewed greedy-
  decision helper. Probe 0 is the controlled policy decision; probes 1 and 2
  remain fixed audit probes.
- `candidate_transition_batches`: exact outer tuple of two exact four-
  transition tuples. Index 0 is selected only by controlled action 0; index 1
  only by controlled action 1.
- first transition in batch 0 must have `action_index = 0`; first transition
  in batch 1 must have `action_index = 1`.
- all eight candidate transition IDs must be pairwise distinct.
- `learning_rate` and `discount_factor` use reviewed trainer validation.

No list, mapping, generator, path, tuple subclass, data source, environment or
model-generated input is approved. All probes/transitions remain project-
authored synthetic/local only through reviewed validation.

## Exact Closed-Loop Semantics

The helper must execute exactly:

1. validate the candidate batch outer tuple, exact two batches, first-action
   binding and eight global IDs without mutating inputs.
2. call the reviewed greedy-decision helper once with the initial model and
   exact probes.
3. read only `before.decisions[0].selected_action_index`.
4. select exactly `candidate_transition_batches[selected_action_index]`.
5. call the reviewed linear model trainer exactly once with:
   - the normalized model from the before diagnostic.
   - the selected exact four-transition batch.
   - reviewed learning rate and discount factor.
   - `epoch_count = 1` fixed internally.
6. call the reviewed greedy-decision helper exactly once with the frozen final
   model and the same probes.
7. return frozen before/training/after diagnostics and whether controlled
   action changed.

There is no loop, retry, exploration, alternate batch execution, environment
step, episode, replay, self-play or convergence behavior.

## Exact Result

`SyntheticOneStepPolicyImprovementResult` is frozen and contains only:

```text
smoke_version
initial_model
before_diagnostic
selected_action_index
selected_transition_record_ids
training_result
after_diagnostic
after_selected_action_index
controlled_action_changed
closed_loop_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Requirements:

- selected action is exact integer 0 or 1 from controlled probe 0.
- selected IDs are the four IDs from only the selected batch in order.
- training result has `epoch_count = 1` and `update_count = 4`.
- after diagnostic uses the training result's frozen final model.
- `controlled_action_changed` compares only before/after probe 0 decisions.
- `closed_loop_applied = true` and safety summary is true.

Warnings must include at least:

- one-step synthetic/local policy-improvement closed-loop smoke only.
- one before decision, one selected four-transition batch, one training epoch
  and one after decision.
- unselected candidate batch is not trained.
- no general environment, episode, replay buffer or self-play.
- no model loading, persistence, checkpoint or external dependency.
- not production training, inference or evaluation.
- action change is not policy-quality or model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The focused test module must cover:

1. controlled action 0 selects only batch 0 and can change to action 1.
2. controlled action 1 selects only batch 1 and can change to action 0.
3. exactly two decision-helper calls and one trainer call in correct order.
4. trainer receives `epoch_count = 1`, selected batch and before model.
5. exact outer two-batch tuple, inner shape and tuple-subclass rejection.
6. first-transition action binding and global eight-ID uniqueness.
7. reviewed helper errors wrapped with stage name and chained cause.
8. deterministic repeated output, complete input non-mutation and frozen
   output.
9. exact result fields, selected IDs, update counts, evidence grade/warnings.
10. package imports, narrow API, no copied formulas and absence of general
    environment/replay/self-play/file/model-loading/persistence/evaluation APIs.

Validation must include the 136 currently approved tests, the new focused
tests, compile checks and `git diff --check`.

## Forbidden Scope

This approval does not permit a general environment, transition function,
episode loop, multiple improvement steps, self-play, stochastic exploration,
replay buffer, dynamic batches, model loading, persistence/checkpoint,
production training/inference/evaluation, path/CLI, dependency, real Tenhou/
haifu, external logs, platform data, strength claims, broad P8 or P9-P12.

## Evidence Grade

Current decision evidence:

```text
P8 fixed greedy-decision current-scope acceptance and exact one-step synthetic/
local policy-improvement task approval evidence only.
```

Future passing implementation evidence:

```text
P8 exact one-step synthetic/local policy-improvement closed-loop smoke evidence
only.
```

Neither is environment/self-play, production training/evaluation, policy-
quality, model-strength, Tenhou ranked, stable-dan, LuckyJ comparison,
candidate-promotion or P9-P12 evidence.

## Gate Accounting

```text
greedy-decision current-scope acceptance = satisfied by this decision
one-step closed-loop approval = satisfied by this decision
exact file/API/input/helper/output/test boundaries = satisfied
remaining mandatory gate count before implementation = 0
```

No gate is satisfied for broader P8.
