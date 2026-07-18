# 04S_P8_ONE_ROUND_POLICY_GRADIENT_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04R` one-round on-policy raw-outcome gradient-update smoke.

APPROVED for next exact implementation task:
one fixed two-round sequential on-policy raw-outcome training smoke.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
4b779d5  Apply first MahJax raw-outcome policy update
```

## Conformance Review

- Exact six-symbol API and source/test pair; no package export/dependency.
- Seed 1 splits independent environment, rule-policy and project-action RNG.
- Project seat-0 actions are legal-masked categorical samples, not greedy or
  retrospectively labeled actions. Fixed rule opponents never update.
- Only public 630-feature decisions, legal masks and sampled actions are held
  in memory. Only cumulative raw seat-0 reward divided by 100 enters objective.
- Exactly one JIT value-and-gradient update occurs; no update loop, replay,
  baseline, critic, discount, bootstrap, reward shaping or persistence exists.
- Exact 37-step pre/post trajectories, objective/deltas, raw outcomes and global
  scores match the independent probe and remain deterministic/legal.
- Evidence warnings correctly deny improvement, self-play, evaluation and
  strength claims.

## Validation

```text
10 focused tests OK
375 repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent API/RNG/legality/objective/delta/outcome probe pass
```

## Direct Two-Round Training Approval

Exact files:

```text
src/mjlabai/rl/mahjax_one_round_policy_gradient_smoke.py
tests/rl/test_mahjax_one_round_policy_gradient_smoke.py
src/mjlabai/rl/mahjax_two_round_policy_gradient_sequence_smoke.py
tests/rl/test_mahjax_two_round_policy_gradient_sequence_smoke.py
```

The one-round module may be refactored only into a private in-process one-step
update helper; its public API/result must remain unchanged. No package export or
dependency change is required. Direct governance synchronization is allowed.

Exact new public API:

```text
MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION
MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS
MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE
MahJaxTwoRoundPolicyGradientSequenceSmokeError
MahJaxTwoRoundPolicyGradientSequenceResult
run_mahjax_two_round_policy_gradient_sequence_smoke
```

The implementation must:

1. start from the reviewed imitation-trained parameters in memory;
2. execute exact round seeds `(1,5)` in that order against fixed bundled rule
   seats, using the reviewed on-policy collector and separate per-round RNG;
3. for each round use only cumulative raw seat-0 reward `/100`, the same masked
   selected-log-probability objective and exactly one update at `0.1`;
4. carry step-0 updated weights/biases directly into seed-5 collection/update;
5. perform exactly two rounds and two updates in one bounded two-item loop, no
   replay/shuffle/minibatch/early stop/retry;
6. return frozen per-step diagnostics and final aggregate delta, not arrays;
7. pin step 0 values from `04R` and step 1 probe values: seed 5, 32 transitions,
   seven project actions `(12,6,31,84,13,32,33)`, cumulative raw
   `(-40,-40,-40,120)`, raw `(-40,-40,-40,130)`, scores `(210,210,210,370)`,
   return `-0.4`, objective `-0.85308564 -> -0.87257367`, step weight/bias
   deltas `0.04183802 / 0.01353321`;
8. require direct parameter continuity and deterministic repeated summary.

Tests must cover exact API/frozen steps, seed order, two-round/two-update cap,
reviewed helper reuse, direct parameter continuity, exact step diagnostics,
finite aggregate deltas, all actions legal, deterministic equality, source
bounds, no persistence/replay and full regressions.

## Forbidden Scope

- no third round, variable epoch/trainer, replay, buffer or batching;
- no self-play learning; opponents remain fixed bundled rule policies;
- no evaluation/league/promotion, real data, Tenhou or platform automation;
- no path/CLI/persistence/checkpoint/artifact;
- no baseline/critic/discount/GAE/bootstrapping/reward shaping;
- no improvement/strength/stable-dan/LuckyJ claim;
- no P9-P12.

## Evidence Grade

```text
P8 one-round on-policy update implementation-review evidence and exact bounded
two-round sequential training task approval only.
```
