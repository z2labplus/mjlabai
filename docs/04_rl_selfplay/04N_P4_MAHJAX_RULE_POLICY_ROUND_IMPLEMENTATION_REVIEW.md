# 04N_P4_MAHJAX_RULE_POLICY_ROUND_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04M` MahJax bundled-rule-policy four-seat single-round smoke.

APPROVED for next exact implementation task:
one project-owned public-observation encoder plus masked randomly initialized
linear 87-action policy single-round smoke.
```

Zero proposal, boundary or review gates remain before the next code.

## Reviewed Commit

```text
76632c9  Integrate MahJax rule policy round smoke
```

## Conformance

- Exact six-symbol module API and package exports are present.
- Root seed splits into independent environment-init and policy RNG streams;
  the policy stream splits once per transition.
- Source has exactly two JIT calls, one explicit `for`, no `while`, and the
  exact 256-transition cap.
- Every bundled-policy action is checked against and stored with the complete
  environment-owned legal tuple before transition.
- Raw/cumulative rewards are unshaped and final scores use global seat order.
- Seed 0 deterministically terminates in 54 transitions without truncation,
  with exact final raw rewards `(0,0,150,-120)`, cumulative raw rewards
  `(-20,0,130,-130)` and global scores `(240,250,390,120)`.
- Errors, frozen outputs, pins, warnings and forbidden scope conform to `04M`.
- No project/learned model, update, optimizer, persistence, multiple game,
  real data, Tenhou, production self-play/evaluation or strength path exists.

## Validation

```text
11 focused tests OK
325 repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent normalized seed-0 result/trace probe pass
```

## Material Next Step

The bundled policy proves policy-to-environment execution, but it is not a
project model. MahJax `v0.1.2` currently exposes only `dict` observation; its
`2D` observation constructor raises `ValueError("observe type 2D is not
developed yet")`. The next executable must therefore build an explicit,
auditable public-information encoder and a project-owned model-output path.

An independent pinned-runtime probe validated the approved design:

```text
feature count: 630
all features finite: true
action count: 87
seed-0 transitions: 91
terminated: true
truncated: false
final/cumulative raw rewards: all zero
global seat scores: (250,250,250,250)
```

## Exact Next Implementation

Files:

```text
src/mjlabai/environment/__init__.py
src/mjlabai/environment/mahjax_linear_policy_round_smoke.py
tests/environment/test_mahjax_linear_policy_round_smoke.py
```

Direct governance synchronization is allowed; dependency pins stay unchanged.

Exact public API:

```text
MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION
MAHJAX_LINEAR_POLICY_TRANSITION_CAP
MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT
MAHJAX_LINEAR_POLICY_ACTION_COUNT
MahJaxLinearPolicyRoundSmokeError
MahJaxLinearPolicyStep
MahJaxLinearPolicyRoundResult
encode_mahjax_public_observation
run_mahjax_linear_policy_round_smoke
```

The encoder must accept only the exact public dict observation keys and shapes:

```text
hand (14)
last_draw scalar
action_history (3,200)
shanten_count scalar
furiten scalar
scores (4), current-player-relative as documented public input
round/honba/kyotaku/prevalent_wind/seat_wind scalars
dora_indicators (4)
```

It must concatenate exactly 630 float32 features in that order, using fixed
documented scaling: tile fields `/36`, action history `/86`, shanten `/6`,
scores `/1000`, round `/12`, honba/kyotaku `/10`, winds `/3`, furiten as 0/1.
It must reject missing/extra keys, wrong shapes and non-finite output. It may
read only `environment.observe(state)`, never hidden opponent/environment state.

The round function accepts only exact uint32-range integer seeds, splits one
root key into environment-init and model-init streams, generates one fixed
project-owned float32 weight matrix `(630,87)` with JAX normal scale `0.01`
and zero bias `(87,)`, and exposes parameter count `54,897`. It JIT-compiles
exactly environment step and linear score calculation. One explicit `for`
bounded at 256 must encode the current public observation, calculate all 87
scores, mask illegal actions to negative infinity, select deterministic argmax,
record the complete legal tuple/selected score, step once, accumulate unshaped
four-seat rewards and stop only on terminal/truncated state. Final scores must
use global `state.round_state.score`.

Seed-0 tests must pin 630 features, 87 actions, 91 transitions, terminal true,
truncated false, all-zero final/cumulative raw rewards and global scores
`(250,250,250,250)`. They must also pin first action 10 and final action 7,
verify every model action is legal, deterministic equal-seed results, exact
source structure, cap/seed/observation failures, warnings and regressions.

## Forbidden Scope

- no learned/trained parameters or parameter update;
- no labels, dataset, optimizer, loss, gradient or checkpoint;
- no hidden-state/opponent-private feature access;
- no multiple games, replay, persistence, file/CLI, GPU/remote or league;
- no real Tenhou, real haifu, external log, platform data/account/automation;
- no production self-play/evaluation, strength or promotion claim;
- no broad P8 or P9-P12.

## Evidence Grade

Reviewed scope:

```text
P4 pinned bundled-rule-policy environment bridge review-closure evidence.
```

Approved next scope:

```text
P4/P8 project-owned untrained model-output-to-environment smoke evidence only.
```
