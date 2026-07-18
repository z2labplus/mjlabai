# 12AX_P8_TWO_POLICY_INTERACTION_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.
```

Commit `b2e6ade` conforms to the exact `12AW` approval. No correctness,
scope, provenance, evidence or test blocker was found, and no production code
or test change was required during review.

## Reviewed Scope

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_two_policy_interaction_smoke.py`
- `tests/rl/test_synthetic_two_policy_interaction_smoke.py`
- direct implementation governance synchronization.

No environment, game episode/outcome, replay, production self-play/evaluation,
real/external/platform data, broad P8 or P9-P12 scope was reviewed or approved.

## Exact Findings

### Participants And Turns

- Participants are an exact tuple of exactly two exact frozen participant
  inputs with non-empty distinct policy IDs.
- Turns are an exact tuple of exactly two or exactly four exact frozen turn
  inputs.
- Actors must alternate participant 0, participant 1, then optionally repeat.
- Turn IDs are non-empty and pairwise distinct.
- All `8 * turn_count` candidate transition IDs are globally distinct.

### Helper Reuse And Independent State

- The reviewed one-step helper is called exactly once per turn.
- No action-value, TD-update, greedy-selection or one-step formula is copied.
- Each actor receives only its own latest model.
- Only the actor model is replaced after a turn.
- Every turn records equal non-actor before/after models.
- Four-turn probes confirm independent A-turn-1 to A-turn-3 and B-turn-2 to
  B-turn-4 continuity.

### Bound, Output And Errors

- The source contains one explicit bounded turn `for` loop and no `while`.
- Odd counts, one/five turns, tuple subclasses, wrong alternation and malformed
  candidate batches are rejected.
- Participant, turn and result dataclasses are frozen and expose exact fields.
- Candidate and one-step failures include one-based turn index with chained
  cause.
- Repeated calls are deterministic and completely non-mutating.

## Validation Evidence

```text
python3 -m unittest tests/rl/test_synthetic_two_policy_interaction_smoke.py
Ran 12 tests: OK

python3 -m unittest <all explicit test modules>
Ran 279 tests: OK (skipped=2 environment-gated real-executable checks)

python3 -m compileall -q src tests
passed

git diff --check
passed
```

Independent probes confirm:

| Turns | Helper calls | Actors | Selected | After | IDs |
|---:|---:|---|---|---|---:|
| 2 | 2 | A/B | `(0, 1)` | `(1, 0)` | 16 unique |
| 4 | 4 | A/B/A/B | `(0, 1, 1, 0)` | `(1, 0, 0, 1)` | 32 unique |

Both probes confirm non-actor equality, deterministic output and complete
input non-mutation.

## Evidence Grade

```text
P8 exact bounded synthetic/local two-policy alternating interaction
implementation review closure evidence only.
```

This is not a Mahjong environment, game episode, outcome generator,
production self-play/training/evaluation, policy-quality, model-strength,
Tenhou, stable-dan, LuckyJ, promotion or P9-P12 evidence.

## Next-Step Constraint

The project must not add another synthetic interaction wrapper. The next task
must accept or reject this exact current scope and resolve the real P8
environment prerequisite by either:

1. directly approving one exact minimal unified synthetic/local environment
   state-transition implementation under the appropriate earlier-stage
   contract, with zero gates before code; or
2. explicitly deferring P8 execution and activating the missing P4 environment
   prerequisite.

The decision must inspect existing P4 contracts and code before choosing. It
must not approve a general game engine, production self-play, real data,
Tenhou integration, strength claims, broad P8 or P9-P12.
