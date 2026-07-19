# 04AF_P8_CAUSAL_RUNNING_BASELINE_COMPARISON_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04AE` raw-return versus causal per-seat running-baseline comparison.

APPROVED for next exact implementation task:
run exactly four ordered 0..31 causal-baseline training passes and one disjoint
52..83 before/after evaluation, with no intermediate selection.
```

Zero planning, proposal or boundary gates remain before that code.

## Reviewed Commit

```text
6b9a640  Compare MahJax causal running baseline
```

## Conformance Review

- Only the two exact `04AE` files plus direct governance changed.
- The six-symbol API and nested frozen array-free raw reference are exact.
- Both branches use the reviewed initialization, `0.01` rate, ordered `0..31`
  training and disjoint zero-update `52..83` evaluation.
- Current advantages use only earlier records; each baseline update happens
  after its policy update. Seed-1 baseline and seed-2 prior mean are pinned.
- Raw produces 10/32 nonzero updates. Baseline produces 31/32; seed 0 is the
  only no-op.
- All 32 training transition counts and action digests match raw exactly,
  isolating the advantage estimator from trajectory sampling.
- Reward vector/sum `-312` and counts `2/20` remain unchanged. Baseline differs
  from initial at `(52,65,72)` and from raw at `(65,)`.
- No estimator/checkpoint is selected; no arrays, persistence, path, CLI,
  third branch, real data, production evaluation or P9-P12 path exists.

No code or test blocker was found.

## Validation

```text
10 focused tests OK in 851.549 seconds
487 explicit repository tests OK in 4614.293 seconds; 2 existing skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent leave-one-out batch and four-pass causal-baseline probes pass
```

## Independent Next-Step Probes

An order-independent frozen-census leave-one-out batch baseline performs one
small aggregate update but leaves all fixed evaluation records unchanged at
sum `-312`. It is rejected and not approved.

One predeclared four-pass causal-baseline probe repeats exact ordered seeds
`0..31` four times, carries policy and baseline continuously, performs no
intermediate evaluation/selection and evaluates once on disjoint `52..83`.

```text
attempts: 128
per-pass nonzero update counts: (31,32,32,32)
per-pass nonzero raw-outcome counts: (10,10,10,11)
final baseline: (0.00625,-0.040390625,-0.054140625,0.0609375)
final parameter deltas:
  (0.0119271539,0.0016169089,0.0243039839,0.0027456258)
initial/final evaluation sums: -312 / -297
initial/final positive counts: 2 / 2
initial/final negative counts: 20 / 19
changed evaluation seeds: (52,58,65,70,72)
```

The exact reward-vector change is seed 58 from `-15` to `0`; no positive
outcome is added. This is a bounded deterministic improvement diagnostic, not
robust evaluation, model strength or a selected checkpoint.

## Direct Four-Pass Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke.py
tests/rl/test_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke.py
```

Direct governance synchronization is allowed. Existing reviewed source/test
logic and public APIs must not change.

Implementation must:

1. load the reviewed imitation parameters once and use learning rate `0.01`;
2. evaluate initial parameters without updates on exact seeds `52..83`;
3. run exactly four passes, each exact ordered seeds `0..31`, carrying policy
   arrays and the causal prior-record per-seat running mean across pass edges;
4. perform exactly 128 attempts and no intermediate evaluation, selection,
   early stop, shuffle, replay buffer or checkpoint;
5. retain complete per-pass/per-attempt legal trajectories, baselines,
   advantages, objectives, parameter deltas and action digests;
6. pin the exact per-pass counts, final baseline and parameter deltas above;
7. evaluate final parameters with zero updates on exact disjoint `52..83` and
   pin exact vector, `-312 -> -297`, counts and changed seeds;
8. return frozen array-free diagnostics, no selected checkpoint or parameters,
   and label the result bounded improvement diagnostic only.

## Forbidden Scope

- no fifth pass, alternate pass count, early stopping, selection or tuning;
- no third estimator, learned critic, GAE, entropy, KL, clipping, optimizer or
  learning-rate change;
- no replay buffer, persistence, artifact, path or CLI;
- no real/external data, Tenhou, production self-play/evaluation or league;
- no robust improvement, superiority, stable-dan, LuckyJ or promotion claim;
- no P9-P12.

## Evidence Grade

```text
P8 exact implementation-review and bounded four-pass training approval
evidence only; not model-strength or promotion evidence.
```
