# 04AE_P8_PREDECLARED_CENSUS_TRAINING_EVALUATION_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04AD` ordered 0..31 raw-return training and disjoint 52..83
zero-update evaluation diagnostic.

APPROVED for next exact implementation task:
compare the reviewed raw-return branch with one causal per-seat running-mean
baseline branch on the same predeclared training/evaluation protocol.
```

Zero planning, proposal or boundary gates remain before that code.

## Reviewed Commit

```text
b525424  Train MahJax on predeclared census
```

## Conformance Review

- Only the two exact `04AD` source/test files plus direct governance changed.
- The six-symbol public API, frozen array-free result and exact seed constants
  match approval.
- Ordered seeds `0..31` retain all 32 legal terminal attempts: 10 nonzero
  updates at `(1,3,5,7,11,17,25,26,27,31)` and 22 exact no-ops.
- Complete transition, actor, action, legal-action, reward, score, digest,
  objective and parameter-delta diagnostics are returned and pinned.
- Initial/final parameters receive zero-update evaluation on exact disjoint
  seeds `52..83`; the raw vector and sum remain identical at `-312`, positive
  and negative counts remain `2/20`, and complete records change only at
  `(52,65,72)`.
- Parameters change, but no checkpoint/protocol is selected or persisted.
- No filtering, replacement, shuffle, replay, second pass, path, CLI, real
  data, production evaluation, P9-P12 path or strength claim exists.

No code or test blocker was found.

## Validation

```text
9 focused tests OK in 459.001 seconds
477 explicit repository tests OK in 4185.294 seconds; 2 existing skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent centered-return and causal-running-baseline probes pass
```

## Independent Algorithm Probes

Both probes use exact ordered training seeds `0..31`, disjoint zero-update
evaluation seeds `52..83`, the reviewed learning rate and no persistence.

Seat-centering changes final parameter scale slightly but reproduces the raw
branch's complete reward vector, sum `-312`, counts `2/20` and changed seeds
`(52,65,72)`. It does not address the observable diagnostic.

A causal per-seat running-mean baseline uses only prior rounds. Before attempt
`n`, each seat advantage is:

```text
advantage[n, seat] = raw_return[n, seat] / 100
                     - mean(raw_return[0:n, seat] / 100)
```

The baseline is updated only after the current policy update. It converts the
raw branch's 10/32 nonzero updates into 31/32 nonzero updates (only seed 0 is a
no-op), while the evaluation reward vector, sum `-312`, counts `2/20` and
changed seeds `(52,65,72)` remain unchanged. This is signal-densification
without reward improvement, not algorithm superiority.

Probe final running baseline and parameter deltas:

```text
baseline: (-0.0121875,-0.015625,-0.05,0.0528125)
deltas:   (0.0035393923,0.0006425792,0.0084222732,0.0009679428)
```

## Direct Raw-Versus-Baseline Comparison Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke.py
tests/rl/test_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke.py
```

Direct governance synchronization is allowed. Existing reviewed source/test
logic and public APIs must not change.

Implementation must:

1. reuse the reviewed raw full-range result as the fixed reference branch;
2. load identical reviewed imitation initialization for one independent causal
   running-baseline branch;
3. train exact ordered seeds `0..31` once at `0.01`, with no filtering,
   replacement, replay, shuffle, epoch or second pass;
4. compute each current advantage only from the current raw seat return and
   the mean of prior records, then update the mean after the policy update;
5. retain all 32 attempts and pin seed 0 as the only no-op and seeds `1..31`
   as nonzero updates, plus complete legal trajectory/update diagnostics;
6. evaluate the baseline branch with zero updates on exact disjoint `52..83`;
7. pin the probe baseline, deltas, identical reward vector/sum/counts and
   changed seeds above;
8. return no parameters, selected estimator or checkpoint and explicitly
   classify the result as signal-densification without reward improvement.

## Forbidden Scope

- no centered/standardized third branch, learned critic, GAE, entropy, KL,
  clipping, optimizer or learning-rate change;
- no extra seed, repeat, replay, epoch, search, tuning or scale-up;
- no checkpoint/model selection, persistence, artifact, path or CLI;
- no real/external data, Tenhou, production self-play/evaluation or league;
- no improvement, superiority, stable-dan, LuckyJ or promotion claim;
- no P9-P12.

## Evidence Grade

```text
P8 exact implementation-review and causal-baseline comparison approval
evidence only; not policy-quality or strength evidence.
```
