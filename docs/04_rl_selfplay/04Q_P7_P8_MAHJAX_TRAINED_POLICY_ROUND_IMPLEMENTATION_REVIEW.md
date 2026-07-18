# 04Q_P7_P8_MAHJAX_TRAINED_POLICY_ROUND_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04P` held-out initial/trained MahJax policy round smoke.

APPROVED for next exact implementation task:
one mixed-policy MahJax single round with the trained project policy in seat 0
and the pinned bundled rule policy in seats 1, 2 and 3.
```

Zero planning/review gates remain before that code.

## Reviewed Commit

```text
c266945  Run trained MahJax policy on held-out round
```

## Conformance Review

- The exact new five-symbol API and four approved source/test files conform to
  `04P`; no package export or dependency was added.
- Training parameters cross the module boundary only through an unexported
  in-process helper. The public training function still returns only the same
  frozen diagnostic summary.
- Seed 2 is distinct from training seed 0 and evaluation-label seed 1. Initial
  and trained policies receive identical seed-2 environment initialization.
- Both rounds use only the reviewed public 630-feature encoder and authoritative
  bool 87-action mask. Complete legal tuples accompany every selected action.
- Both rounds terminate without truncation under the 256 cap. Initial/trained
  traces contain 88/94 actions, first actions 12/71, equal global scores
  `(250,250,250,250)` and unequal action trajectories.
- Source has no path, persistence, model-loading, checkpoint, hidden state,
  reward update, RL update or self-play-learning surface.

## Validation

```text
9 focused tests OK
355 repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent private-API/legality/outcome/determinism probe pass
```

## Direct Mixed-Policy Round Approval

Exact files:

```text
src/mjlabai/environment/mahjax_mixed_policy_round_smoke.py
tests/environment/test_mahjax_mixed_policy_round_smoke.py
```

The reviewed private training helper may be imported read-only. No existing
production file, package export or dependency change is required. Direct
governance synchronization is allowed.

Exact public API:

```text
MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION
MAHJAX_MIXED_POLICY_ROUND_SEED
MahJaxMixedPolicyRoundSmokeError
MahJaxMixedPolicyRoundStep
MahJaxMixedPolicyRoundResult
run_mahjax_mixed_policy_round_smoke
```

The implementation must:

1. call the reviewed private in-memory training helper once and use only its
   trained `(630,87)+87` parameters plus frozen summary;
2. initialize exact MahJax seed 0 by splitting one root key into environment
   initialization and bundled-rule-policy RNG streams;
3. assign exact seat 0 to the deterministic trained project policy and seats
   1, 2 and 3 to the pinned bundled red rule policy;
4. use one JIT environment step, one JIT project score function and one JIT
   bundled rule function, with one explicit 256-cap transition loop;
5. use only the public encoder for project decisions, apply authoritative legal
   masks, and recheck every project/rule action against the complete legal tuple;
6. record each step index, acting seat, policy identity, complete legal tuple
   and selected action in a frozen trace;
7. preserve raw/cumulative rewards and global `state.round_state.score` without
   reward shaping or evaluation conversion;
8. pin independent-probe acceptance values: 54 transitions, terminal true,
   truncated false, final raw rewards `(0,0,140,-120)`, cumulative raw rewards
   `(0,0,120,-140)`, global scores `(250,250,380,120)`, 10 project-policy turns,
   and every project-policy selected action equal to legal action 71.

Tests must cover exact API/frozen objects, participant-seat identity, RNG
separation, unchanged training summary, complete legal trace, exact acceptance
values, global score authority, deterministic equality, cap failure, warnings,
source structure, no persistence and full regressions.

## Forbidden Scope

- no multiple rounds/matches, seat rotation, aggregate ranking or league;
- no parameter/data/checkpoint/artifact persistence, loader, path or CLI;
- no reward/RL update, policy-gradient/TD update or self-play learning;
- no real Tenhou/haifu, external logs, platform data/account/automation;
- no hidden/private observation, production evaluation or promotion;
- no policy-quality, strength, stable-dan or LuckyJ claim;
- no broad P8 or P9-P12.

## Evidence Grade

```text
P7/P8 local held-out trained-policy implementation-review evidence and exact
mixed-policy environment-interaction task approval only.
```
