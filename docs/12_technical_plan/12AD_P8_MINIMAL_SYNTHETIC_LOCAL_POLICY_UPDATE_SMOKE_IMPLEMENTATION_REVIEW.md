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

## Blocker-Fix Implementation Status

The exact fix is now implemented, pending the separate re-review required by
`10_NEXT`:

- `_finite_real` catches float-conversion `OverflowError` and raises
  `SyntheticPolicyUpdateSmokeError` with the original exception chained.
- `test_non_float_representable_real_uses_validation_error` covers
  `current_action_value=10**10000`.
- the former probe now returns the approved validation exception.
- 12 focused tests and 46 approved regression tests pass; `git diff --check`
  passes.
- no formula, dataclass field, public API, warning, evidence grade or scope
  changed.

This status records implementation evidence only. It does not replace the
required re-review decision and does not yet close the review blocker.

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

## Exact Fix Task Completed

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

## Current Re-review Task

```text
Re-run exact minimal P8 synthetic/local policy-update smoke implementation review after numeric-conversion blocker fix.
```

The re-review must update this document rather than create another review
document. It must confirm the exception type, 58 passing tests and unchanged
formula/API/provenance/output/evidence scope before closing the blocker.

## Re-review After Blocker Fix

Re-reviewed fix commit `70893079addb91b97f241fc9ed583d97ddadadd7`.

Confirmed:

- the former `10**10000` probe raises `SyntheticPolicyUpdateSmokeError` and
  chains the original `OverflowError` as its cause.
- the focused P8 module runs 12 tests and all pass.
- the six approved P6/P7 regression modules run 46 tests and all pass.
- all 58 tests and `git diff --check` pass.
- public exports, input/result dataclass fields and function signature remain
  exactly within `12AC`.
- target, TD-error and updated-value formulas are unchanged.
- no fixture/data, dependency, path/CLI, environment, episode, self-play,
  model, optimizer, training/evaluation, real/external/platform data, broad P8
  or P9-P12 work was added.

Re-review decision:

```text
A. Review can close after blocker fix.
```

The numeric-conversion blocker is closed. This closes only the exact
implementation review; it does not accept broader P8, approve self-play or
training, or provide model-strength evidence.

## Evidence Grade

```text
P8 exact synthetic/local numerical policy-update implementation review evidence only.
```

Neither the passing tests nor this blocker review is model-strength, Tenhou
ranked, stable-dan, LuckyJ comparison or candidate-promotion evidence.
