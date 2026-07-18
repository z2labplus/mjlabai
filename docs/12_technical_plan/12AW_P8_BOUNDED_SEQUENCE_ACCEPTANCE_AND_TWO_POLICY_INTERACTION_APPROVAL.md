# 12AW_P8_BOUNDED_SEQUENCE_ACCEPTANCE_AND_TWO_POLICY_INTERACTION_APPROVAL

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact bounded implementation task.
```

The exact bounded sequence implemented in `338de0a`, fixed in `8897793` and
review-closed in `12AV` is accepted only for its synthetic/local scope.

Next executable task:

```text
Implement exact bounded P8 synthetic/local two-policy alternating policy-
improvement interaction smoke only.
```

No proposal, sibling boundary or additional approval may precede code.

## Exact Approved Files

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_two_policy_interaction_smoke.py`
- `tests/rl/test_synthetic_two_policy_interaction_smoke.py`
- direct docs/governance synchronization.

No fixture/data, path/CLI, dependency, environment, persistence, checkpoint or
artifact file is approved.

## Exact Public API

```text
SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION
MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS
SyntheticTwoPolicyParticipantInput
SyntheticTwoPolicyInteractionTurnInput
SyntheticTwoPolicyInteractionTurnResult
SyntheticTwoPolicyInteractionSmokeError
SyntheticTwoPolicyInteractionResult
run_synthetic_two_policy_interaction_smoke
```

The module must reuse `run_synthetic_one_step_policy_improvement_smoke` and
the reviewed candidate-batch validator. It must not copy decision, action-
value, training or one-step orchestration logic.

## Exact Participants

`SyntheticTwoPolicyParticipantInput` is frozen and contains only:

```text
policy_id
initial_model
```

The interaction accepts one exact tuple of exactly two exact participants.
Policy IDs must be non-empty exact strings and distinct. Participant order
defines actor indices 0 and 1. No dynamic participant count or mapping is
approved.

## Exact Turn Input

`SyntheticTwoPolicyInteractionTurnInput` is frozen and contains only:

```text
turn_id
actor_policy_id
decision_probes
candidate_transition_batches
learning_rate
discount_factor
```

The interaction accepts an exact tuple of exactly 2 or exactly 4 turns:

- turn IDs are non-empty exact strings and globally distinct.
- actor IDs must alternate participant 0, participant 1, then optionally
  participant 0, participant 1.
- probes, batches and numeric parameters are validated by reviewed helpers.
- all candidate transition IDs across all selected and unselected batches in
  all turns are globally pairwise distinct.
- list, mapping, generator, tuple subclass, odd turn count and more than four
  turns are rejected.

## Exact Interaction Semantics

1. validate exact participant and turn outer tuples and hard bounds.
2. keep exactly two independent current policy-model variables.
3. iterate turns once in deterministic input order with one bounded `for`
   loop.
4. require exact actor alternation starting with participant 0.
5. call the reviewed one-step helper exactly once for the current actor.
6. update only that actor's current model from the one-step final model.
7. leave the non-actor model unchanged for that turn.
8. preserve each policy's independent continuity across its own turns.
9. reject candidate transition-ID reuse globally.
10. wrap helper failures with one-based turn index and chained cause.

No opponent-generated observation, state transition authority, environment,
episode outcome, reward generation, retry, shuffle, random selection,
concurrency, replay or production self-play is approved.

## Exact Turn Result

`SyntheticTwoPolicyInteractionTurnResult` is frozen and contains only:

```text
turn_index
turn_id
actor_policy_id
non_actor_policy_id
actor_initial_model
actor_final_model
non_actor_model_before
non_actor_model_after
one_step_result
non_actor_model_unchanged
```

The non-actor before/after values must be equal. Actor initial/final values
must exactly bind to the reviewed one-step result.

## Exact Interaction Result

`SyntheticTwoPolicyInteractionResult` is frozen and contains only:

```text
interaction_version
participant_count
turn_count
max_turns
policy_ids
initial_models
final_models
turn_ids
turn_results
selected_actions
after_actions
global_candidate_transition_record_ids
interaction_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

- participant count is 2 and max turns is 4.
- turn count is exactly 2 or 4.
- ordered outputs derive only from normalized inputs and reviewed results.
- global IDs contain exactly `8 * turn_count` distinct IDs.
- interaction/safety flags are true.

Warnings must state bounded two-policy synthetic/local interaction only,
exactly two participants, two/four alternating turns, one reviewed closed-loop
call per turn, no environment/episode/outcome/replay/production self-play, no
persistence/checkpoint/dependency, not production training/evaluation,
interaction action changes are not policy-quality/strength evidence, not
LuckyJ/stable-dan and not candidate promotion.

## Exact Tests

Focused tests must cover:

1. exact two-turn A/B output and both policy updates.
2. exact four-turn A/B/A/B independent policy continuity.
3. exact participant tuple/count/type/ID validation and frozen inputs.
4. exact turn tuple/count/type, two/four bound and actor alternation.
5. exact frozen turn input and non-empty/distinct turn IDs.
6. global candidate transition-ID uniqueness across turns.
7. one reviewed helper call per turn and actor model continuity.
8. non-actor model unchanged on every turn.
9. one-based turn error wrapping with chained cause.
10. deterministic equality, complete non-mutation and frozen outputs.
11. exact result/turn fields, counts, IDs, evidence and warnings.
12. exact package surface, one explicit turn loop and no copied formulas.

Validation must include all 267 explicit repository tests, focused tests,
`compileall` and `git diff --check`.

## Forbidden Scope And Evidence

No third participant, odd turn count, more than four turns, general
environment/transition function, episode/outcome generation, opponent-derived
state, replay, production self-play, stochastic exploration, dynamic data,
model loading, persistence/checkpoint, production evaluation, real Tenhou/
haifu, external logs, platform data, path/CLI, dependency, strength claim,
broad P8 or P9-P12 is approved.

Future passing evidence is only:

```text
P8 exact bounded synthetic/local two-policy alternating interaction smoke
evidence only.
```

It is not an environment, game episode, production self-play/training/
evaluation, policy-quality, model-strength, Tenhou, stable-dan, LuckyJ or
promotion evidence.

## Gate Accounting

```text
bounded sequence current-scope acceptance = satisfied
two-policy interaction approval = satisfied
exact file/API/participant/turn/continuity/output/test boundaries = satisfied
remaining mandatory gate count before implementation = 0
```
