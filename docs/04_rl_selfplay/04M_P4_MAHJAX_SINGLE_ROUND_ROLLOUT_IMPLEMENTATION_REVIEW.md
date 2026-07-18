# 04M_P4_MAHJAX_SINGLE_ROUND_ROLLOUT_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close after the exact global-seat-score blocker fix.

ACCEPTED as current-scope complete:
the exact `04L` MahJax lowest-legal-action single-round rollout smoke.

APPROVED for next exact implementation task:
one pinned MahJax built-in rule-based four-seat single-round rollout smoke.
```

No proposal, boundary or review gate remains before the next code task.

## Reviewed Commits

```text
a8fd6b1  Implement MahJax single-round rollout smoke
86199af  Fix MahJax rollout seat score ordering
```

## Exact Conformance Review

- The module exposes exactly the six `04L` symbols and package exports them.
- Both result objects are frozen; every step records pre-step index, actor,
  complete 87-action-mask-derived legal tuple and selected action.
- Runtime identity remains `mahjax==0.1.2`, `jax==0.4.30`,
  `jaxlib==0.4.30`, `red_mahjong` and environment version `beta`.
- Source creates exactly one `jax.jit(environment.step)`, contains one explicit
  `for`, no `while`, and uses the exact 256-transition cap.
- Every transition chooses `legal_actions[0]`, blocks until ready and requires
  exact monotonic step progress.
- Seed 0 terminates after exactly 94 transitions without truncation. Final and
  cumulative raw rewards are four zeroes; final global seat scores are four
  250 values.
- Invalid seeds fail before runtime load and cap exhaustion raises the project
  error instead of widening the bound.
- Source has no path, network, model, optimizer, checkpoint, persistence,
  multi-game, training or production self-play path.

## Review Blocker And Exact Fix

The first review probe found that MahJax observation `scores` are ordered from
the current player's perspective. Equal seed-0 scores hid that difference.
An independent built-in-rule-policy terminal probe produced:

```text
current player: 2
global seat order:    (240, 250, 390, 120)
observer-relative:    (390, 120, 240, 250)
```

Commit `86199af` changes only the approved source/test behavior needed to read
`state.round_state.score` and adds a regression assertion. The blocker is
closed; final score identity is now stable across observer changes.

## Validation

```text
python3 -m unittest tests/environment/test_mahjax_single_round_rollout_smoke.py
12 tests OK

python3 -m unittest <all repository test files>
314 tests OK; 2 existing environment-gated skips

python3 -m compileall -q src tests
pass

python3 -m pip check
No broken requirements found.

git diff --check
pass
```

An independent normalized seed-0 project probe confirms the exact 94-step
result, first legal tuple `(2,4,5,8,10,11,14,17,19,21,27,71)` with action 2,
and final pre-step 93 legal tuple `(6,30,33,36,71)` with action 6.

## Direct Next Executable Approval

The next task must implement one deterministic local round in which all four
seats use MahJax `v0.1.2`'s bundled public
`mahjax.red_mahjong.players.rule_based_player`. This is the first executable
policy-to-environment bridge and is materially different from another fixed
action wrapper.

Exact implementation files:

```text
src/mjlabai/environment/__init__.py
src/mjlabai/environment/mahjax_rule_based_single_round_smoke.py
tests/environment/test_mahjax_rule_based_single_round_smoke.py
```

Direct governance synchronization is also allowed. Dependency pins remain
unchanged.

Exact public API:

```text
MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION
MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP
MahJaxRuleBasedSingleRoundSmokeError
MahJaxRuleBasedSingleRoundStep
MahJaxRuleBasedSingleRoundResult
run_mahjax_rule_based_single_round_smoke
```

The function accepts only exact uint32-range integer seeds. It splits one root
key into initialization and policy streams, constructs the exact reviewed
single-round red environment, JIT-compiles exactly the environment step and
bundled rule policy, and uses one explicit `for` bounded at 256. On each step
it must split the policy key once, require the selected rule-policy action to
be present in the complete environment legal tuple, record an immutable step,
apply one transition, accumulate unshaped four-seat raw rewards and stop only
on terminal/truncated state.

The result must expose pinned identities, seed, transition count/cap, complete
trace, terminal status, final raw rewards, cumulative raw rewards, global
seat-ordered scores, evidence grade and warnings.

Seed-0 acceptance values from an independent pinned-runtime probe:

```text
transition_count = 54
terminated = true
truncated = false
final_rewards = (0.0, 0.0, 150.0, -120.0)
cumulative_rewards = (-20.0, 0.0, 130.0, -130.0)
final_scores = (240, 250, 390, 120)  # global seat order
```

Focused tests must cover exact API/frozen outputs, identity/pins, exact seed-0
result, complete legal trace, policy-action legality, deterministic RNG/result,
global score order, raw reward shape, hard cap exhaustion, invalid seeds,
source structure and full regressions.

## Forbidden Scope

- no project model, model-output adapter or learned policy;
- no policy update, gradient, optimizer, checkpoint or training;
- no multiple rounds/games, batching, parallelism or league;
- no reward shaping, replay, persistence, file/CLI or GPU/remote path;
- no real Tenhou, real haifu, external log, platform data/account/automation;
- no production self-play/evaluation or candidate promotion;
- no model-strength, stable-dan or LuckyJ claim;
- no broad P8 or P9-P12 work.

## Evidence Grade

The reviewed implementation is only:

```text
P4 pinned local single-round environment rollout review-closure evidence.
```

The approved next implementation may provide only:

```text
P4 pinned local rule-policy-to-environment single-round smoke evidence.
```
