# 12AD_P8_MINIMAL_SYNTHETIC_LOCAL_POLICY_UPDATE_SMOKE_IMPLEMENTATION_REVIEW

## Scope

This document reviews commit `a7c83d578edba433f54b12c091d148e908f08573`
against the exact implementation approval in `12AC`.

This is one implementation review, not another boundary or proposal. It does
not modify production code or tests and does not approve broad P8, an
environment, self-play, a model, production training/evaluation, real data or
P9-P12.

## Reviewed Artifacts

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_update_smoke.py`
- `tests/rl/test_synthetic_policy_update_smoke.py`
- `docs/12_technical_plan/12AC_P8_MINIMAL_SYNTHETIC_LOCAL_POLICY_UPDATE_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`

## Review Findings

The implementation stays inside the three approved source/test files, exports
only the approved API, uses the standard library, accepts only already-loaded
synthetic/local records and implements the exact terminal target,
non-terminal target, TD-error and updated-value formulas.

The focused tests cover formulas, determinism, input immutability, parameter
ranges, NaN/infinity/bool rejection, terminal consistency, provenance,
identifier tokens, output fields, warnings and package imports. No fixture,
data, path/CLI, environment, episode, self-play, action selection, model,
optimizer, training loop, evaluation, artifact or external-data path was
added.

One blocker exists in `_finite_real`: a `Real` value such as `10**10000` is
finite but raises raw `OverflowError` during `float(value)`. The approved API
defines `SyntheticPolicyUpdateSmokeError` as its validation error, so this
conversion failure must not escape as an unrelated built-in exception.

## Decision

```text
B. Review cannot close because blockers exist.
```

| blocker_type | description | impacted_area | required_fix | severity | code change needed |
|---|---|---|---|---|---:|
| Numeric validation error normalization | Finite but non-float-representable `Real` input leaks `OverflowError` instead of `SyntheticPolicyUpdateSmokeError`. | `_finite_real` and focused numeric validation tests | Normalize float-conversion overflow to `SyntheticPolicyUpdateSmokeError` and add exact regression coverage without changing formulas or public API. | Medium | yes |

## Validation Evidence

The approved commands passed before the adversarial probe:

- focused P8 test module: 11 tests passed.
- six approved P6/P7 regression modules: 46 tests passed.
- total: 57 tests passed.
- `git diff --check`: passed.

The additional in-memory probe produced:

```text
OverflowError
int too large to convert to float
```

No real/external/platform data, model, environment, self-play, training,
evaluation or artifact was used by the probe.

## Exact Next Task

```text
Fix P8 policy-update smoke numeric-conversion error normalization and add exact regression coverage.
```

The fix may modify only:

- `src/mjlabai/rl/synthetic_policy_update_smoke.py`
- `tests/rl/test_synthetic_policy_update_smoke.py`
- direct docs/governance synchronization.

It must not change the formula, dataclass fields, public API, evidence grade or
scope. It must not add a fixture, dependency, batch/episode/environment,
self-play, model, training/evaluation, path/CLI, real/external/platform data or
P9-P12 work.

## Evidence Grade

```text
P8 exact synthetic/local numerical policy-update implementation review evidence only.
```

Neither the passing tests nor this blocker review is model-strength, Tenhou
ranked, stable-dan, LuckyJ comparison or candidate-promotion evidence.
