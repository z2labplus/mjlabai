# 04AQ P8 Per-Trajectory Gradient Influence Implementation Review

## Decision

```text
A. Review can close.
```

Commit `8e483ad` conforms to the exact `04AP` approval. No code, test,
evidence or scope blocker was found.

## Findings

1. The existing private batch helper only retains gradients already produced
   inside its unchanged accumulation loop. Baselines, objectives, sums and
   update consumers are not changed.
2. Exact `0..31` and `116..147` batches are collected once each from identical
   reviewed initial parameters. There are 64 trajectories, zero parameter
   updates and zero evaluation calls.
3. Every trajectory records protocol/seed/hash, gradient group/global norms
   and dot/cosine against own and opposite aggregate means. Output is frozen,
   array-free and complete.
4. Reference own/opposite signs are `13-/0/19+` and `14-/0/18+`; alternate
   signs are `7-/0/25+` and `18-/0/14+`. Every sign is retained.
5. No trajectory, protocol, model, direction or checkpoint is ranked, removed,
   selected or promoted. There is no I/O, replay, artifact or real-data path.

Recorded probe, nine focused, 122 synthetic and seven claim-control passing
tests plus compile/dependency/static/diff evidence are sufficient. Expensive
runs are not repeated in this review.

## Evidence Boundary

Mixed opposite-alignment signs across both groups show that disagreement is not
confined to one lone negative-sign trajectory. Sign counts do not establish
whether a small number of large-magnitude contributions dominate the aggregate
negative dot product. They do not justify seed filtering, improvement or
strength claims.

## Direct Next Approval

```text
Approved: add exact opposite-alignment magnitude-concentration summaries to
the existing per-trajectory diagnostic.
```

Exact future files:

- Modify only
  `src/mjlabai/rl/mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke.py`.
- Modify only
  `tests/rl/test_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke.py`.
- Direct governance synchronization only.

Exact contract:

1. Reuse the existing 64 opposite-aggregate dot products; collect no new seed,
   trajectory, gradient, update or evaluation.
2. For each protocol record signed sum, positive sum, absolute negative sum,
   absolute sum, net cancellation ratio, absolute-contribution HHI, effective
   contribution count, largest absolute share and fixed top-4/top-8 absolute
   shares.
3. Verify each protocol signed-sum divided by 32 equals the reviewed aggregate
   dot product within tolerance.
4. Sorting may be used only internally for fixed aggregate shares. Do not
   return ranked seed identities or create a filtering/selection interface.
5. Preserve all 64 trajectory records and zero update/evaluation counts.
6. Run one probe, focused and fast checks only. Do not run prior expensive
   smokes or the full suite.

Forbidden: seed identity ranking/removal, threshold search, clipping,
reweighting, update/evaluation, new protocol/window/data, model selection,
strength claim or P9-P12. Zero docs gates remain before code.
