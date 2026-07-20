# 04AR P8 Gradient Influence Concentration Implementation Review

## Decision

```text
A. Review can close.
```

Commit `757fe45` conforms to the exact anonymous summary contract approved in
`04AQ`. No code, test, evidence or scope blocker was found.

## Findings

1. The implementation derives every summary from the same 32 opposite-
   aggregate dot products per protocol, for the same 64 retained trajectories.
   It collects no new trajectory, gradient, update or evaluation.
2. Each signed mean reproduces the reviewed aggregate dot product within the
   pinned tolerance. Positive, absolute-negative and absolute totals are
   internally consistent and all values are finite.
3. Cancellation, absolute-contribution HHI, effective contribution count and
   fixed largest/top-4/top-8 shares use one anonymous absolute-value sort only.
   No seed identity or ranked record is returned.
4. Reference effective count/largest share are about `12.06/16.0%`; alternate
   values are about `5.15/41.6%`. This establishes greater concentration under
   the exact alternate batch, not causality or a generally inferior protocol.
5. There is no identity filtering, clipping, reweighting, selection, parameter
   update, evaluation, file ingestion, real data or P9-P12 path.

The recorded probe, ten focused, 122 synthetic and seven claim-control passing
tests plus compile/dependency/static/diff checks are sufficient. The expensive
focused diagnostic is not repeated in this review.

## Evidence Boundary

The fixed summaries show that opposite-alignment magnitude is more concentrated
for the exact alternate batch. They do not identify a removable trajectory,
justify reweighting, prove that magnitude causes the negative aggregate cosine,
or establish improvement, robustness, model strength, Tenhou performance,
stable dan or a LuckyJ comparison.

## Direct Next Approval

```text
Approved: add the exact unit-norm per-trajectory aggregate alignment diagnostic
to the existing first-pass influence smoke.
```

Exact future files:

- Modify only
  `src/mjlabai/rl/mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke.py`.
- Modify only
  `tests/rl/test_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke.py`.
- Direct governance synchronization only.

Exact contract:

1. Reuse the same 64 already-computed individual trajectory gradients from the
   exact `0..31` and `116..147` batches. Collect nothing new.
2. Normalize every nonzero trajectory gradient by its full global L2 norm,
   then average the 32 unit vectors for each protocol.
3. Record each unit-normalized protocol aggregate's existing parameter-group
   norms, global norm, cross-protocol dot product and cosine similarity.
4. Require all 64 source global norms to be finite and strictly positive. Do
   not add an epsilon, clipping rule, threshold or zero-gradient fallback.
5. Preserve all existing raw aggregate, per-trajectory and concentration
   results exactly. Apply zero updates and zero evaluations.
6. Run one deterministic probe, focused tests and fast checks only. Do not run
   previous expensive diagnostics or the full suite.

Forbidden: seed identity ranking/removal, filtering, reweighting, threshold or
normalization search, protocol selection, new data/window, update/evaluation,
strength claim or P9-P12. Zero docs gates remain before code.
