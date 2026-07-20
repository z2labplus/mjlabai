# 04AU P8 Four-Pass Norm-Matched Unit-Gradient Training Implementation Review

## Decision

```text
A. Review can close.

ACCEPTED as exact bounded P8 negative behavior evidence:
the four-pass shared norm-matched unit-gradient continuation in commit 4ccd386.

APPROVED for next exact implementation task:
one pinned local MahJax half-game bundled-rule-policy rollout smoke.
```

Zero planning or review gates remain before that exact code task.

## Reviewed Commit

```text
4ccd386  Test MahJax four-pass unit gradient training
```

## Conformance Review

- One shared branch starts from the reviewed imitation parameters and carries
  the updated arrays continuously through exactly four ordered passes.
- Every pass collects exact reference seeds `0..31` and alternate seeds
  `116..147` at the current parameters. All 64 finite nonzero trajectory
  gradients receive identical unit-norm treatment.
- Each pass averages the two protocol directions, matches that direction once
  to the same pass raw-combined global L2 norm and applies exactly one fixed
  `0.32` update. Every parameter group changes on every pass.
- Complete per-pass trajectory provenance, unit-norm alignment and update
  geometry are frozen in the public array-free result.
- There is no intermediate evaluation. Exact existing windows `52..83` and
  `84..115` run once only after pass four, with zero evaluation updates.
- No pass/model/rate/scale/seed/window/checkpoint is selected. No artifact,
  persistence, I/O, real data, Tenhou or P9-P12 path exists.

## Exact Result

Normalized cross-protocol cosine by pass:

```text
pass 0: +0.2355091237
pass 1: -0.0164135117
pass 2: +0.2696807705
pass 3: +0.3166833373
```

Final fixed-window behavior:

```text
primary:     -312 -> -312, delta 0, changed reward seeds ()
replication: -1056 -> -1133, delta -77, changed reward seeds (92,)
```

Positive geometry and nonzero parameter motion did not produce fixed-window
improvement. The result is retained as negative mechanism evidence. It does
not justify a fifth pass, rate/scale tuning or any selection.

## Validation

```text
one deterministic probe: pass
first focused run: 7 pass, 1 test-only tolerance mismatch
corrected focused run: 8 tests OK in 2383.115s
122 synthetic RL tests OK
7 claim-control tests OK
compileall pass
pip check: no broken requirements
git diff --check pass
```

The correction changed only the assertion to the already approved `1e-8`
global-norm-match tolerance. Production values and behavior were unchanged.

## Stage Decision

The norm-matched unit-gradient branch stops here. A fifth pass or any
rate/scale/pass/seed/window/formula search would be low-information selection
after two different four-pass gradient-conflict mechanisms both failed to
improve the fixed windows.

The current training/evaluation path uses MahJax `round_mode="single"` only.
MahJax `0.1.2` exposes the pinned local `round_mode="half"` path, which is a
materially different and north-star-relevant environment prerequisite. An
independent seed-0 rule-policy probe terminated naturally after 938 legal
transitions in about 46.25 seconds, at round 8, with no truncation or illegal
action and final scores `(203,441,76,280)`.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/environment/mahjax_rule_based_half_game_smoke.py
tests/environment/test_mahjax_rule_based_half_game_smoke.py
```

`src/mjlabai/environment/__init__.py` may add only the direct public exports.
Direct governance synchronization is allowed.

The exact task must:

1. pin MahJax `0.1.2`, environment `red_mahjong`/`beta`, JAX CPU and
   `round_mode="half"`, `next_round_style="auto"`;
2. use all four seats with the bundled deterministic rule policy and separate
   initialization/policy RNG lineage from exact seed `0`;
3. use one explicit loop with hard cap `2048`, environment-owned legal masks
   and exactly one environment step per selected legal action;
4. record complete global transition identity, round/round-step identity,
   actor, legal actions, selected action, round-boundary summaries, raw rewards,
   cumulative rewards and global final scores;
5. pin the probe's 938 transitions, natural terminal/nontruncated status, zero
   illegal actions, final round 8, final scores `(203,441,76,280)`, final raw
   rewards `(-3,-3,-5,21)` and cumulative raw rewards `(73,151,-284,10)`;
6. return frozen array-free diagnostics and reject invalid seeds/cap exhaustion;
7. add no project model, learning, update, optimizer, checkpoint, self-play
   league, real data, Tenhou connection, strength claim or P9-P12 path.

## Evidence Grade

```text
P8 exact four-pass implementation-review closure and P4/P8 pinned local
half-game environment-prerequisite task approval only.
```

Neither the reviewed training result nor the approved environment smoke is
model-strength, stable-dan, Tenhou, LuckyJ 10.68 or promotion evidence.
