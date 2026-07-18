# 12AV_P8_BOUNDED_POLICY_IMPROVEMENT_SEQUENCE_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close after blocker fix.
```

Commit `338de0a` implemented the exact `12AU` scope. Review found one concrete
conformance blocker: step inputs were traversed once for validation and again
for execution, while `12AU` requires one deterministic bounded step loop.
Commit `8897793` merges validation, global identity checking, helper execution
and model carry into one loop and adds an AST regression assertion.

No blocker remains after that exact source/test fix.

## Reviewed Scope

The review covers only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_improvement_sequence_smoke.py`
- `tests/rl/test_synthetic_policy_improvement_sequence_smoke.py`
- direct implementation governance synchronization.

No general environment, episode generator, replay, self-play, persistence,
production evaluation, real/external/platform data, broad P8 or P9-P12 scope
was reviewed or approved.

## Exact Findings

### Files And Public API

- Only the exact source/export/test files approved in `12AU` were added.
- The public API contains the six symbols explicitly listed in `12AU`.
- The package exports those exact symbols.
- The earlier governance summary count of seven was corrected to six without
  changing the approved API.

### Inputs, Bound And Identity

- The outer input must be an exact tuple and tuple subclasses are rejected.
- The hard step count is 1 through 4; zero and five are rejected.
- Every element must be an exact frozen step input with a non-empty distinct
  step ID.
- Both candidate batches in every step are validated by the reviewed
  candidate validator.
- All `8 * step_count` candidate transition IDs are globally pairwise
  distinct and returned in deterministic step/batch/record order.

### Helper Reuse And Continuity

- The reviewed one-step helper is called exactly once per step.
- No Q-value, TD-update or greedy-selection formula is copied.
- Each step's training final model is passed directly as the next step's
  initial model.
- The fixed implementation contains exactly one explicit `for` node and no
  `while` node, retry, early stop, shuffle or random branch.

### Output And Errors

- The result and step input are frozen dataclasses with the exact approved
  fields.
- Step results, IDs, selected actions and after actions preserve input order.
- Candidate-validation and one-step failures include the one-based step index
  and retain a chained cause.
- Repeated calls are deterministic and inputs are not mutated.

## Validation Evidence

```text
python3 -m unittest tests/rl/test_synthetic_policy_improvement_sequence_smoke.py
Ran 10 tests: OK

python3 -m unittest <all explicit test modules>
Ran 267 tests: OK (skipped=2 environment-gated real-executable checks)

python3 -m compileall -q src tests
passed

git diff --check
passed
```

Independent probes confirm:

| Steps | One-step calls | Selected | After | Global IDs |
|---:|---:|---|---|---:|
| 1 | 1 | `(0,)` | `(1,)` | 8 unique |
| 2 | 2 | `(0, 1)` | `(1, 0)` | 16 unique |
| 4 | 4 | `(0, 1, 0, 1)` | `(1, 0, 1, 0)` | 32 unique |

All probes preserve model continuity and complete input non-mutation.

## Evidence Grade

```text
P8 exact bounded synthetic/local policy-improvement sequence implementation
review closure evidence only.
```

This is not a general environment, episode, replay or self-play system. It is
not production training/evaluation, policy-quality, model-strength, Tenhou,
stable-dan, LuckyJ, promotion or P9-P12 evidence.

## Next-Step Constraint

The next task must accept or reject this exact current scope and directly
approve or defer one materially progressive bounded synthetic/local two-policy
alternating policy-improvement interaction smoke. It must use exact files,
hard bounds and reviewed helpers with zero gates before code if approved.

Another single-policy sequence wrapper, proposal chain or sibling boundary is
forbidden. A future approval must not authorize a general environment,
unbounded episode, replay, production self-play, persistence, real data,
strength claims, broad P8 or P9-P12.
