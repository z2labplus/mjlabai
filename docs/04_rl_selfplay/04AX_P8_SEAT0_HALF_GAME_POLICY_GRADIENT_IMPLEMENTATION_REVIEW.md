# 04AX P8 Seat-0 Half-Game Policy-Gradient Implementation Review

## Decision

```text
A. Review can close.

ACCEPTED as current implementation scope:
the exact one-update seed-0 seat-0 half-game raw-outcome training and disjoint
seed-1 zero-update evaluation implementation in commit 930b15e.

APPROVED for next exact implementation task:
two sequential training half-games on contiguous seeds (0,1), one update after
each, followed by fixed zero-update evaluation on disjoint seeds (2,3).
```

Zero planning, proposal or review gates remain before the exact code task.

## Conformance Review

- Public output is frozen and contains no parameter, feature or mask arrays.
- Reviewed imitation parameters and the exact 882-feature encoder are reused
  in memory; no artifact is loaded or saved.
- Seed 0 uses independent environment, project-action and rule-policy RNG
  streams. Project seat 0 samples only from the environment legal mask; bundled
  rule policy remains fixed at seats 1/2/3.
- All 427 training transitions and 102 project decisions are legal. Exact
  strict PON-to-PON_RED normalization remains the sole permitted rule-policy
  correction, though this trajectory requires none.
- Seat-0 cumulative raw reward /100 is exactly `-0.53` and weights every
  project decision. One fixed `0.01` update changes all four parameter arrays.
- Disjoint seed-1 greedy evaluation makes zero updates and honestly records
  cumulative seat-0 reward `-300 -> -320` and final score `-70 -> -80`.
- All three half-games terminate naturally at environment-owned round 5 without
  truncation. Complete action/round provenance is retained.
- Ten focused tests passed in `139.407s`; nine neighboring all-project update
  tests passed in `157.392s`; compile, dependency and diff checks passed.

No conformance, correctness, safety or evidence blocker remains.

## Rejected Immediate Variants

Two in-memory probes were not approved as standalone next tasks:

1. averaging seed-0 and seed-2 terminal-return gradients changes parameter
   magnitude but reproduces the same negative seed-1 greedy behavior;
2. assigning seed-0 round-local raw returns also changes gradient magnitude but
   reproduces that same behavior.

These are plateau observations only. They do not justify seed, reward, rate or
estimator search. The next step instead tests direct parameter continuity over
two complete training half-games.

## Direct Two-Half-Game Approval

Exact future files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_two_half_game_policy_gradient_sequence_smoke.py
tests/rl/test_mahjax_categorical_mlp_two_half_game_policy_gradient_sequence_smoke.py
```

Direct RL exports and governance synchronization are allowed. The task must:

1. train reviewed in-memory parameters on exact ordered seeds `(0,1)`;
2. reuse the existing reviewed collector and one-update helper directly;
3. sample only project seat 0, keep rule seats 1/2/3 fixed and preserve strict
   legality normalization plus full immutable provenance;
4. carry the first updated arrays directly into seed 1, applying exactly one
   fixed `0.01` raw-outcome update after each half-game, for two updates total;
5. evaluate initial and final arrays greedily on exact disjoint seeds `(2,3)`
   with zero evaluation updates and identical per-seed RNG construction;
6. return no arrays, selected model, checkpoint or artifact and perform no
   rollback, early stopping or branch selection;
7. pin all approved probe values below, including the aggregate negative result.

Approved probe values:

```text
training seed 0:
  transitions/project decisions = 427/102
  cumulative rewards = (-53,82,429,-468)
  final rewards/scores/round = (0,87,0,-77)/(201,297,556,-54)/5
  return scale = -0.53
  objective = -0.5453851223 -> -0.5463446379
  delta L2 = (0.0009908610,0.0002095903,0.0028836143,0.0003556903)

training seed 1 after direct continuity:
  transitions/project decisions = 797/196
  cumulative rewards = (-259,140,155,-56)
  final rewards/scores/round = (-27,65,-14,-14)/(-16,440,382,194)/8
  return scale = -2.59
  objective = -3.4532430172 -> -3.4597692490
  delta L2 = (0.0031369785,0.0007574092,0.0072538634,0.0013632783)

evaluation seed 2:
  initial transitions/project decisions = 780/202
  initial cumulative rewards/scores = (-344,157,-242,419)/(-26,412,23,591)
  final transitions/project decisions = 820/215
  final cumulative rewards/scores = (-387,207,-236,396)/(-69,472,29,568)

evaluation seed 3:
  initial transitions/project decisions = 907/228
  initial cumulative rewards/scores = (-288,-29,389,-102)/(-48,221,549,278)
  final transitions/project decisions = 1099/262
  final cumulative rewards/scores = (-247,-37,482,-268)/(-7,263,642,102)

initial/final seat-0 evaluation raw sum = -632/-634
training normalizations = (0,0)
all evaluation normalizations = 0
training update count / evaluation update count = 2/0
```

The aggregate `-2` change is retained as bounded negative evidence. Seed 3
improves while seed 2 degrades; neither is selected or hidden.

## Forbidden Scope And Evidence Grade

- no third training half-game, replay, baseline/critic, reward/rate search,
  evaluation-driven selection, checkpoint or persistence;
- no general self-play runner, league, real data, Tenhou or P9-P12;
- no improvement, robustness, strength, stable-dan or LuckyJ claim.

```text
P8 local one-update implementation-review closure and exact two-half-game
sequential-training task approval only.
```
