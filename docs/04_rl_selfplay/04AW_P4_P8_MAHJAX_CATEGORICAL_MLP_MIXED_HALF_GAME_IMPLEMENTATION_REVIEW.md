# 04AW P4/P8 Categorical-MLP Mixed Half-Game Implementation Review

## Decision

```text
A. Review can close after the exact import-order blocker fix.

ACCEPTED as current implementation scope:
the exact read-only categorical-MLP-seat-0 versus rule-seats-1/2/3 MahJax
half-game smoke in commit 4af4784 plus lazy package exports that preserve
supervised-first imports.

APPROVED for next exact implementation task:
one seed-0 sampled project-seat half-game raw-outcome update followed by one
disjoint seed-1 greedy read-only pre/post evaluation.
```

Zero planning, proposal or review gates remain before that exact code task.

## Reviewed Commit And Blocker Fix

```text
4af4784  Add MahJax categorical MLP mixed half-game smoke
```

The implementation conforms on runtime/model pins, legal masking, seat roles,
one capped loop, full trace, round boundaries, strict legality normalization,
immutable array-free output and zero half-game updates.

Review found one import-order blocker: eager export from
`mjlabai.environment.__init__` made a direct supervised-module import re-enter
the partially initialized supervised module. The exact fix lazily resolves only
the six mixed-half-game exports. A separate-process regression imports the
supervised module first and then the package export. No rollout behavior,
parameter, action, reward or result changed.

## Exact Implementation Evidence

- MahJax `0.1.2`, red-mahjong `beta`, seed 0, `round_mode="half"` and
  `next_round_style="auto"` remain pinned.
- The reviewed 882-feature categorical MLP greedily drives seat 0 under the
  environment legal mask; bundled rule policy drives seats 1/2/3.
- One 2048-capped loop records all 825 transitions, including 200 project
  decisions, policy identity, legal actions and raw/applied action.
- The only normalization is transition 450, actor 3, raw PON 75 to legal
  PON_RED 76. Every other illegal rule-policy output raises.
- Eight round boundaries lead to round-8 terminal scores `(40,265,379,316)`,
  final rewards `(-20,0,30,0)` and cumulative rewards `(-200,15,12,123)`.
- Output contains no arrays, parameters, weights, checkpoint or artifact.
- Eleven focused tests passed before review in `206.526s`; 20 neighboring
  environment tests passed in `83.364s`; compile, dependency and diff checks
  passed. The import-order regression passes in `0.032s` after the fix.

## Direct Half-Game Update Approval

Exact future files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke.py
tests/rl/test_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke.py
```

Direct exports and governance synchronization are allowed. The implementation
must:

1. obtain the reviewed in-memory categorical-MLP imitation parameters and use
   the exact 882-feature encoder without persistence;
2. collect exactly one seed-0 MahJax half-game with independently split init,
   seat-0 sampled-action and rule-policy RNG streams;
3. let only project seat 0 sample legal-masked categorical actions; keep
   bundled rule seats 1/2/3 and the exact strict PON-to-PON_RED normalizer;
4. retain project features, legal masks and actions only in memory, then apply
   exactly one actor-seat-0 cumulative raw return divided by 100 to every
   selected seat-0 log probability;
5. use loss `-mean(return_scale * selected_log_probability)` and exactly one
   fixed learning-rate `0.01` update over the four reviewed parameter arrays;
6. run greedy read-only initial and updated policies on disjoint seed 1 with
   identical init/rule RNG construction and zero evaluation updates;
7. pin the approved probe values below and retain complete legal transition,
   normalization, terminal score/reward and update provenance;
8. perform no second training half-game, second update, replay, checkpoint,
   persistence, search, tuning, selection or rollback based on evaluation.

Approved probe values:

```text
training seed = 0
training transitions / project decisions = 427 / 102
training cumulative rewards = (-53,82,429,-468)
training final rewards = (0,87,0,-77)
training final scores / round = (201,297,556,-54) / 5
training normalizations = ()
seat-0 return scale = -0.53
objective before / after = -0.5453851223 / -0.5463446379
parameter delta L2 =
  (0.0009908610,0.0002095903,0.0028836143,0.0003556903)

evaluation seed = 1
initial transitions / project decisions = 526 / 132
initial cumulative rewards = (-300,-34,178,96)
initial scores = (-70,278,376,416)
updated transitions / project decisions = 524 / 130
updated cumulative rewards = (-320,-54,158,156)
updated scores = (-80,268,366,446)
evaluation normalizations = () for both paths
evaluation update count = 0
```

Early terminal round 5 is environment-owned bankruptcy behavior, not
truncation or cap exhaustion. The observed seed-1 seat-0 reward/score decrease
must be reported as bounded negative behavior evidence and must not be hidden.

## Forbidden Scope

- no second update, seed/rate/reward search or evaluation-driven selection;
- no general self-play runner, replay buffer, league or candidate promotion;
- no saved parameters, checkpoint, dataset, real Tenhou, real haifu, external
  log, platform data or third-party artifact;
- no strength, stable-dan, LuckyJ 10.68 or P9-P12 claim.

## Evidence Grade

```text
P4/P7/P8 exact local mixed-half-game implementation-review closure, import-order
blocker fix and one bounded half-game update task approval only.
```
