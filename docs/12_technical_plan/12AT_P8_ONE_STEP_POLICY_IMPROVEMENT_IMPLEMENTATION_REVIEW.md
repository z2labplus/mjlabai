# 12AT_P8_ONE_STEP_POLICY_IMPROVEMENT_IMPLEMENTATION_REVIEW

## Scope

This document reviews only commit
`22828c362ba82c12ad113e637b236c3e48de3cd7` against the exact `12AS`
approval. It does not modify production code or tests and does not approve a
broader P8 scope.

Reviewed implementation files:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_one_step_policy_improvement_smoke.py`
- `tests/rl/test_synthetic_one_step_policy_improvement_smoke.py`

## Findings

No correctness, scope, provenance, evidence or test blocker was found.

## Approval Compliance

| Requirement | Evidence | Result |
|---|---|---|
| Exact approved files/API | one module, package exports, focused tests and the four approved symbols | Pass |
| Exact inputs | one reviewed model, exact three probes and exact outer tuple of two four-transition batches | Pass |
| Candidate validation | both selected and unselected batches pass reviewed transition validation; eight IDs globally distinct | Pass |
| Action binding | batch 0/1 first transition binds to action 0/1; controlled before action indexes only the matching batch | Pass |
| Helper order | exact reviewed call order is decision, training, decision | Pass |
| Training bound | selected batch only, exactly one trainer call and `epoch_count = 1` | Pass |
| Before/after lineage | trainer receives before normalized model; after decision receives trainer final model and same probes | Pass |
| Diagnostics | selected IDs, before/after actions, change flag, frozen helper results and warnings are preserved | Pass |
| Determinism / immutability | repeated equality, complete input non-mutation and frozen result | Pass |
| Error surface | candidate/before/training/after failures are stage-indexed and chained | Pass |
| Forbidden scope | no copied Q/TD/greedy formulas, general environment, episode loop, replay, self-play, persistence or evaluation API | Pass |

## Validation Evidence

Passed:

```text
10 one-step policy-improvement tests
136 previously approved regression tests
python3 -m compileall -q src/mjlabai/rl tests/rl
git diff --check
```

Total approved unit tests: 146.

Independent probes confirmed both action paths:

```text
initial action 0 -> batch 0 only -> after action 1
initial action 1 -> batch 1 only -> after action 0
helper order = decision, training, decision
```

They also confirmed full input non-mutation and absence of random, file,
unbounded-loop and copied formula surfaces.

## Review Decision

```text
A. Review can close.
```

The exact one-step policy-improvement implementation conforms to `12AS`. No
production code or test fix is required.

## Evidence Grade

```text
P8 exact one-step synthetic/local policy-improvement closed-loop smoke
implementation review closure evidence only.
```

This is an executable fixed closed loop, but it is not a general environment,
episode or self-play system, production training/evaluation, policy-quality
evidence, model-strength evidence, Tenhou ranked evidence, stable-dan evidence,
LuckyJ comparison, candidate-promotion evidence or P9-P12 evidence.

## Next-Step Constraint

The next task must decide current-scope acceptance and directly approve or
defer one materially progressive executable P8 task. It must not create
another fixed one-step wrapper or boundary chain.

The preferred next executable outcome is one bounded deterministic
synthetic/local policy-improvement sequence over an exact tuple of 1 through 4
already-loaded closed-loop step inputs. It must reuse the reviewed one-step
helper, carry each final model into the next step, preserve step results and
global record identity, and stop at a hard cap. A single acceptance decision
must fix exact files, API, inputs, continuity, outputs, tests and evidence
warnings with zero gates before code. It must not add a general environment,
episode generation, self-play, real/external/platform data, model loading,
persistence/checkpoint, CLI, dependency, production evaluation or strength
claim.

```text
remaining mandatory gate count before a new exact code task = 1
exit criterion = accept or reject the reviewed scope and directly approve or
                 defer one non-repetitive executable outcome
```

Broad P8, general environment/gameplay, self-play, production model training/
evaluation, real/external/platform data and P9-P12 remain unapproved.
