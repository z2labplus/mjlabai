# 04AT P8 Norm-Matched Unit-Gradient Update Implementation Review

## Decision

```text
A. Review can close.
```

Commit `986f4ad` conforms to the exact `04AS` one-step update approval. No
code, test, evidence or scope blocker was found.

## Findings

1. The implementation uses exact training batches `0..31` and `116..147` once
   from the reviewed initial parameters and retains complete protocol evidence.
2. All 64 full gradients receive identical unit-norm treatment. The combined
   unit direction is deterministically scaled by `0.11023811`, matching raw
   combined global L2 `0.01765190` within tolerance.
3. Exactly one shared fixed-rate `0.32` update changes all four parameter
   groups. No projection, epsilon, clipping, identity, per-seed weighting,
   branch or selection exists.
4. Only fixed zero-update windows `52..83` and `84..115` are evaluated. Reward
   vectors, transition counts and changed-seed records are complete.
5. Both windows remain exact initial behavior: `-312/-1056`, no changed reward
   seed and no changed transition count. This result is retained as negative
   one-step behavior evidence.

The recorded probe, eight focused, 122 synthetic and seven claim-control
passing tests plus compile/dependency/diff checks are sufficient. The
722-second focused test and probe are not repeated in this review.

## Evidence Boundary

The one-step update proves that nonzero norm-matched parameter movement does
not cross any observed fixed-window action boundary. It does not prove that
unit-normalized training generally fails, nor does it establish improvement,
robustness, strength, Tenhou performance, stable dan or LuckyJ comparison.

## Direct Next Approval

```text
Approved: run one exact four-pass shared-policy continuation of the same
norm-matched unit-gradient update with final-only existing-window evaluation.
```

Exact future files:

- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke.py`.
- Modify `src/mjlabai/rl/__init__.py` only if required by local export pattern.
- Direct governance synchronization only.

Exact contract:

1. Start from the same reviewed imitation parameters and one shared branch.
2. Execute exactly four ordered passes. At every pass collect only exact batches
   `0..31` and `116..147` from the current shared parameters.
3. At every pass uniformly normalize all 64 full gradients, average per
   protocol, average the two protocol means, and deterministically match that
   direction's global L2 to the same pass's raw combined mean global L2.
4. Apply exactly one fixed-rate `0.32` update per pass. Carry the updated shared
   parameters into the next pass without branch, rollback or selection.
5. Record every pass's raw/unit/scaled geometry, scale, parameter deltas,
   trajectory/trace provenance, legal/termination/centering invariants and
   exact update order.
6. Perform no intermediate evaluation. After pass four, evaluate only existing
   zero-update windows `52..83` and `84..115`, retaining all outcomes.
7. Run one deterministic probe, focused tests and fast checks only. Do not run
   earlier expensive smokes or the full suite.

Forbidden: a fifth pass, rate/scale/pass/seed/window search, projection,
epsilon, clipping, identity filtering, per-seed weights, intermediate eval,
checkpoint/model selection, replay, real data, strength claim or P9-P12. Zero
docs gates remain before code.
