# 12AR_P8_LINEAR_GREEDY_DECISION_IMPLEMENTATION_REVIEW

## Scope

This document reviews only commit
`475997a2934f689521d480376d816237f659dccc` against the exact `12AQ`
approval. It does not modify production code or tests and does not approve a
broader P8 scope.

Reviewed implementation files:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_linear_greedy_decision_smoke.py`
- `tests/rl/test_synthetic_linear_greedy_decision_smoke.py`

## Findings

No correctness, scope, provenance, evidence or test blocker was found.

## Approval Compliance

| Requirement | Evidence | Result |
|---|---|---|
| Exact approved files/API | one module, package exports, focused tests and the six approved symbols | Pass |
| Exact model/probes | one reviewed fixed linear model and exact tuple of three exact probes | Pass |
| Provenance | canonical source and project-authored/synthetic/local flags required; unsafe flags rejected | Pass |
| Legal action boundary | every probe requires exact integer tuple `(0, 1)` | Pass |
| Helper reuse | reviewed model and feature helpers are called once/three times; reviewed action-value helper exactly six times | Pass |
| Action values | `(q0, q1)` is preserved in action-index order for every probe | Pass |
| Greedy/tie semantics | action 1 only when `q1 > q0`; exact equality records a tie and selects action 0 | Pass |
| Determinism / immutability | normalized frozen output, repeated equality and full input non-mutation | Pass |
| Error surface | model/feature/action-value errors are wrapped with chained approved causes and probe index | Pass |
| Forbidden scope | no dynamic probes/model, stochastic policy, file/model loader, environment, gameplay, replay, self-play, persistence or evaluation API | Pass |

## Validation Evidence

Passed:

```text
11 linear greedy-decision tests
125 previously approved regression tests
python3 -m compileall -q src/mjlabai/rl tests/rl
git diff --check
```

Total approved unit tests: 136.

Independent probes confirmed:

```text
action values = ((1.5, -1.25), (-3.5, -1.25), (0.125, 0.125))
selected actions = (0, 1, 0)
tie flags = (false, false, true)
reviewed action-value helper calls = 6
```

They also confirmed outer tuple-subclass, duplicate-ID and external-log
rejection, input non-mutation and absence of file, randomness, exploration and
unbounded-loop surfaces.

## Review Decision

```text
A. Review can close.
```

The exact inference and greedy-decision implementation conforms to `12AQ`.
No production code or test fix is required.

## Evidence Grade

```text
P8 exact synthetic/local linear-model inference and greedy-decision diagnostic
implementation review closure evidence only.
```

This is an executable fixed training-to-model-output diagnostic, but it is not
an environment, gameplay loop, self-play system, production inference or
evaluation, policy-quality evidence, model-strength evidence, Tenhou ranked
evidence, stable-dan evidence, LuckyJ comparison, candidate-promotion evidence
or P9-P12 evidence.

## Next-Step Constraint

The next task must decide current-scope acceptance and directly approve or
defer one materially progressive executable P8 task. It must not create
another isolated inference wrapper or boundary chain.

The preferred next executable outcome is one exact deterministic one-step
synthetic/local policy-improvement closed-loop smoke:

```text
initial frozen model
-> reviewed greedy decision on one fixed state
-> one project-authored synthetic transition selected by that action
-> reviewed linear model training helper
-> reviewed greedy decision on the same state
-> frozen before/after diagnostics
```

A single acceptance decision must fix the exact initial model, candidate
transitions, selected-action binding, training call, before/after probe,
outputs, files, tests and evidence warnings before code. It must not add a
general environment, episode loop, self-play, real/external/platform data,
model loading, persistence/checkpoint, CLI, dependency, production evaluation
or strength claim.

```text
remaining mandatory gate count before a new exact code task = 1
exit criterion = accept or reject the reviewed scope and directly approve or
                 defer one non-repetitive executable outcome
```

Broad P8, general environment/gameplay, self-play, production model training/
evaluation, real/external/platform data and P9-P12 remain unapproved.
