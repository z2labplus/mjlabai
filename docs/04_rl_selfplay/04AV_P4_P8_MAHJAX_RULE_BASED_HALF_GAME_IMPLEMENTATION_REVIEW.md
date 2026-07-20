# 04AV P4/P8 MahJax Rule-Policy Half-Game Implementation Review

## Decision

```text
A. Review can close after the exact round-step identity blocker fix.

ACCEPTED as current environment-prerequisite scope:
the pinned local bundled-rule-policy half-game smoke in commit a3bcaf5 plus
the exact review fix that makes round_step_index truly round-local.

APPROVED for next exact implementation task:
one read-only categorical-MLP-seat-0 versus rule-seats-1/2/3 half-game smoke
with one strict PON-to-PON_RED legality normalization.
```

Zero planning/review gates remain before that exact code task.

## Reviewed Commit And Blocker Fix

```text
a3bcaf5  Add MahJax rule-policy half-game smoke
```

The first static review found one local semantic blocker: MahJax
`state.step_count` is global across the half-game, while the new trace field was
named `round_step_index`. The exact fix now:

- proves `state.step_count == transition_index` on every state;
- computes `round_step_index` from the most recent round boundary;
- resets that local origin after each boundary;
- tests every round-local sequence as exact `0..n-1`.

No terminal value, action, reward, score, RNG or environment behavior changed.
Nine focused tests pass after the fix in `56.366s`.

## Conformance Review

- Runtime pins are MahJax `0.1.2`, red-mahjong `beta`, JAX CPU,
  `round_mode="half"` and `next_round_style="auto"`.
- Exact seed 0 uses separately split initialization and bundled-policy RNG.
- One explicit loop is hard-capped at 2048 transitions. There is no `while`,
  recursion, I/O, persistence or external service.
- Every transition records global index, true round-local index, round, actor,
  full environment legal-action tuple and selected bundled-rule action.
- Eight environment-owned round boundaries record transition count, previous/
  next round and global scores.
- All 938 actions are legal. The half-game terminates naturally at round 8
  without truncation; final scores are `(203,441,76,280)`, final raw rewards
  `(-3,-3,-5,21)` and cumulative raw rewards `(73,151,-284,10)`.
- Frozen outputs contain no JAX arrays, parameters, weights or artifacts.
- No project model, update, optimizer, checkpoint, production self-play,
  league, real data, Tenhou connection, strength claim or P9-P12 path exists.

## Validation

```text
9 focused tests OK in 55.282s before review
34 neighboring environment tests OK in 72.974s
9 focused tests OK in 61.157s deterministic repeat
9 focused tests OK in 56.366s after exact blocker fix
compileall pass
pip check: no broken requirements
git diff --check pass
```

## Mixed Project-Model Probe

The next material step is to prove that the reviewed categorical MLP can make
legal decisions through a complete half-game without updates. The first probe
correctly rejected an old 630-feature encoder; the current MLP requires its
reviewed 882-feature encoder.

With that encoder, one upstream MahJax bundled-rule-policy inconsistency was
exposed at transition 450, actor 3:

```text
raw bundled action = 75 (PON)
environment legal actions = (76,84) (PON_RED,PASS)
```

MahJax `_pon_logic` can return `PON` when only `PON_RED` is legal. The next
task is approved with exactly one auditable normalization:

```text
if raw action == PON and PON is illegal and PON_RED is legal:
    applied action = PON_RED
else:
    raw action must already be legal, or fail
```

There is no general fallback, random replacement or nearest-action mapping.
An exact probe with this normalization finishes naturally:

```text
transitions = 825
project seat-0 decisions = 200
normalizations = ((450,3,75,76),)
final round = 8
final scores = (40,265,379,316)
final raw rewards = (-20,0,30,0)
cumulative raw rewards = (-200,15,12,123)
terminated = true
truncated = false
```

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/environment/mahjax_categorical_mlp_mixed_half_game_smoke.py
tests/environment/test_mahjax_categorical_mlp_mixed_half_game_smoke.py
```

Direct exports in `src/mjlabai/environment/__init__.py` and governance
synchronization are allowed.

The exact implementation must:

1. obtain the reviewed in-memory categorical-MLP imitation parameters and its
   exact 882-feature encoder; save no parameter/artifact;
2. use project greedy legal-masked policy only at seat 0 and bundled rule
   policy at seats 1/2/3 in the same pinned seed-0 half-game environment;
3. use one 2048-capped loop and record complete transition, round, actor,
   policy identity, raw/applied action, legal actions and normalization flag;
4. apply only the exact `PON -> PON_RED` rule above and fail every other raw
   illegal action;
5. pin all probe values, eight round boundaries and the sole normalization at
   transition 450/actor 3;
6. perform zero half-game gradient, update, optimizer, selection or evaluation-
   driven adaptation;
7. make no comparison/superiority/strength/promotion claim and add no real
   data, Tenhou, production self-play/league or P9-P12 path.

## Evidence Grade

```text
P4/P8 exact local half-game environment implementation-review closure and
read-only project-model half-game task approval only.
```

Neither result is model-strength, stable-dan, Tenhou, LuckyJ 10.68 or
candidate-promotion evidence.
