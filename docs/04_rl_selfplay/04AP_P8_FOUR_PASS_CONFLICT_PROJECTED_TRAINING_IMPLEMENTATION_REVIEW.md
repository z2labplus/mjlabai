# 04AP P8 Four-Pass Conflict-Projected Training Implementation Review

## Decision

```text
A. Review can close.
```

Commit `ad737a6` conforms to the exact `04AO` approval. No code, test,
evidence or scope blocker was found.

## Conformance Findings

1. The one-step source factors only its exact private projection/update
   arithmetic. Its public API and pinned first-pass geometry remain unchanged.
2. The new diagnostic owns one shared parameter branch and performs exactly
   four passes. Every pass collects exact frozen-policy batches `0..31` and
   `116..147` at that pass's shared start parameters.
3. Every pass uses the same simultaneous original-pair projection, one average
   and one fixed-rate `0.32` update. Parameters carry directly between passes.
4. All four original dot products/cosines are negative. All four projected dot
   products/cosines are positive. Every update and cumulative parameter delta
   is finite, nonzero and recorded without pass selection.
5. There is no intermediate evaluation. Final evaluation uses only exact zero-
   update windows `52..83` and `84..115`, for two calls and zero updates.
6. Totals are exactly 256 training trajectories, four updates, zero
   intermediate evaluation calls and two final evaluation calls.
7. Public output is frozen and array-free with complete batch, action, reward,
   score, objective, gradient-geometry and parameter-continuity provenance.
8. No protocol, model, multiplier, projection, pass or checkpoint is selected.
   Source contains no I/O, replay, artifact, external or real-data path.

## Validation Evidence

```text
Deterministic probe: completed
Focused: 9 tests OK in 2293.912 seconds
Fast synthetic RL regression: 122 tests OK in 0.034 seconds
Claim-control regression: 7 tests OK in 0.001 seconds
Compile/dependency/static/diff checks: OK
Commit/source/provenance review: OK
```

The probe, focused test, prior expensive smokes and full suite are not rerun in
this review.

## Evidence Boundary

The projection repeatedly changes gradient geometry, but does not improve the
fixed behavior windows. Primary reward remains exact `-312` with no changed
seed. Replication reward degrades from `-1056` to `-1133`; only seed `92`
changes, for delta `-77`.

This is valid mechanism plus bounded negative behavior evidence. It is not
evidence of improvement, robustness, generalization, policy quality, model
strength, promotion, Tenhou/stable-dan/LuckyJ performance or P9-P12 readiness.

The repeated result rejects a fifth pass and rejects projection/rate/window
search. The unresolved question is whether the aggregate conflict is broad
across both fixed distributions or dominated by a small number of trajectory
gradient contributions. The next task therefore changes the diagnostic level,
not the update count.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement an exact first-pass per-trajectory cross-protocol gradient influence
diagnostic with no update or evaluation.
```

Exact future files:

- Modify
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`
  only to retain each already-computed private trajectory gradient inside its
  private batch-gradient result while preserving all existing sum/update
  behavior.
- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke.py`.
- Direct governance synchronization only. Do not modify existing expensive
  focused tests unless a compatibility blocker is found.

Exact implementation contract:

1. Start from the reviewed imitation parameters and collect exact batches
   `0..31` and `116..147` once each, from identical frozen parameters.
2. Preserve each protocol's reviewed other-31 same-seat baseline and objective.
   Reuse the exact per-trajectory gradients already calculated for each batch;
   do not introduce a second gradient formula.
3. For every one of the 64 trajectories, record protocol ID, seed, action-trace
   hash, parameter-group/global gradient norms and dot/cosine against both its
   own protocol aggregate mean gradient and the opposite protocol aggregate
   mean gradient.
4. Record predeclared counts of negative/zero/positive opposite-aggregate
   alignment for each protocol and retain every trajectory regardless of sign.
   Do not rank, select, exclude or promote any seed.
5. Apply zero parameter updates and zero evaluations. Totals must remain 64
   trajectories, zero updates and zero evaluation calls.
6. Return frozen array-free diagnostics with complete provenance and no
   protocol/model/trajectory/direction/checkpoint selection.
7. Run one deterministic probe, focused and fast checks only. Do not run the
   four-pass focused test, prior expensive smokes or the full suite.

Forbidden:

- fifth projected pass or any parameter update/evaluation;
- seed removal, outlier clipping, ranking or trajectory selection;
- projection/rate/formula/optimizer/entropy/temperature/exploration search;
- third protocol, new seed window or real/external data;
- critic, GAE, clipping, replay, persistence or artifact;
- strength, promotion, Tenhou, stable-dan, LuckyJ or P9-P12 claim.

No additional proposal, boundary, review-before-code or approval document is
required. Zero mandatory gates remain before exact code.
