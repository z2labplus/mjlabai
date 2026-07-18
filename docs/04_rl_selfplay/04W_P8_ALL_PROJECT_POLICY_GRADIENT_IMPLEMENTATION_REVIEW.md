# 04W_P8_ALL_PROJECT_POLICY_GRADIENT_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04V` seed-1 shared categorical-MLP all-project-seat raw-outcome
update smoke.

APPROVED for next exact implementation task:
one seeds-(1,3) two-round sequential all-project-seat raw-outcome training
smoke with direct parameter continuity and exactly two updates.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
d59f4a1  Update shared MahJax MLP from four seats
```

## Conformance Review

- Only the exact two approved source/test files plus direct governance changed.
- The module exposes exactly six approved symbols and an immutable array-free
  result; reviewed MLP arrays remain private and in process.
- All seats use one project policy. No bundled rule participant is imported or
  invoked.
- Exact seed `1` splits independent environment and policy-action RNG streams.
  Every one of 77 sampled actions is selected after the complete environment
  legal mask and checked before step.
- Actor counts are `(21,22,17,17)` and raw/global outcomes match the approved
  probe. Every decision return equals its actor's cumulative raw reward divided
  by 100.
- Exactly one `jax.value_and_grad` call and one `0.01` update operate on all four
  MLP arrays. Objective and four finite deltas match `04V`.
- Same-seed replay after the small update has identical actor/action/legal
  traces, outcome and scores.
- The implementation has no second round/update, rule participant, replay,
  persistence, path/CLI, external/real data or strength claim.

## Validation

```text
9 focused tests OK
413 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent public-result and two-round continuity probes pass
```

## Two-Round Continuity Probe

Starting from the reviewed imitation parameters, exact seeds `(1,3)` execute
in order with one update after each terminal trajectory.

Round 1 reproduces `04V`. Round 2 receives round-1 arrays directly:

```text
seed = 3
transition_count = 84
seat_decision_counts = (23,22,19,20)
cumulative_raw_rewards = (-10,-10,20,-10)
final_raw_rewards = (-10,-10,30,-10)
final_scores = (240,240,270,240)
objective = -0.05535889 -> -0.05543957
parameter_delta_l2 =
  (0.0002636357,0.0000601950,0.0008506179,0.0000944084)
```

The same seed-3 trajectory from fresh imitation parameters has initial
objective `-0.05533995`, while carried round-1 arrays yield `-0.05535889`.
That difference plus the round-1 deltas proves direct parameter continuity.
After two updates, initial-to-final parameter deltas are:

```text
(0.0010158311,0.0001864599,0.0025688238,0.0002769242)
```

Exact seed-3 replay after update 2 remains the same legal 84-step outcome. This
is repeated update/continuity evidence only, not policy improvement.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_all_project_policy_gradient_smoke.py
src/mjlabai/rl/mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke.py
tests/rl/test_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke.py
```

Direct governance synchronization is allowed. In the existing source, only
the private rollout helper may be generalized to receive an explicit seed; the
public `04V` API/result and seed-1 behavior must remain unchanged.

Exact new public API:

```text
MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS
MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE
MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError
MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult
run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke
```

### Exact sequence contract

1. obtain reviewed imitation arrays once and retain the initial arrays privately;
2. execute exact ordered seeds `(1,3)` in one explicit two-item loop;
3. collect each round through the reviewed all-project helper with that seed;
4. verify complete legality, terminal/no truncation, exact transition/seat/
   action-prefix/raw/global diagnostics and four nonzero seat returns;
5. apply the reviewed actor-indexed helper exactly once after each round;
6. assign each update's arrays directly as the next round's input; never
   retrain/reinitialize between rounds;
7. pin both objective pairs/per-step deltas and the exact initial-to-final four
   parameter deltas;
8. replay exact seed 3 after update 2 and pin the unchanged legal trajectory and
   outcome;
9. return frozen summaries/traces only; arrays remain private and unexported.

### Required tests

- exact six-symbol API/constants/frozen array-free result;
- unchanged `04V` public result and seed-1 diagnostics;
- exact ordered seeds, two rounds, two updates and direct array continuity;
- exact 77/84 transitions, seat counts, action prefixes, legality and outcomes;
- exact two objective pairs, eight per-step deltas and four final deltas;
- carried seed-3 objective differs from the pinned fresh value;
- exact post-update-2 replay, determinism and failure translation;
- source proves one two-item loop/helper reuse and no I/O/reinitialization;
- warnings deny production self-play, evaluation, improvement and strength.

## Forbidden Scope

- no third seed/round/update, replay, batch optimizer or persistence;
- no baseline/critic/discount/GAE/entropy/reward shaping;
- no rule participant, opponent pool, league or promotion;
- no saved dataset/model/checkpoint/artifact/path/CLI;
- no external/real data, Tenhou, haifu or platform data;
- no production self-play/evaluation or strength comparison;
- no P9-P12.

## Evidence Grade

```text
P8 all-project update implementation-review evidence and exact two-round
sequential all-project training task approval only.
```
