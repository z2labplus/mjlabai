# 04AS P8 Unit-Norm Gradient Alignment Implementation Review

## Decision

```text
A. Review can close.
```

Commit `795c2c0` conforms to the exact `04AR` unit-norm diagnostic approval.
No code, test, evidence or scope blocker was found.

## Findings

1. The implementation reuses exactly the same 64 already-computed trajectory
   gradients from batches `0..31` and `116..147`; it collects nothing new.
2. Every full trajectory gradient has a finite positive global L2 norm. Every
   one is divided by that norm without epsilon, clipping or threshold, then all
   32 unit vectors are averaged uniformly per protocol.
3. Frozen output pins both parameter-group/global norms and cross-protocol
   dot/cosine. All prior aggregate, per-trajectory and concentration results
   remain exact and present.
4. Raw cross-protocol dot/cosine remain
   `-0.0001429308562/-0.1868768328`; unit-norm aggregate dot/cosine are
   `0.00927360775/+0.2355091237`.
5. There are zero parameter updates and zero evaluation calls. No identity,
   ranking, filtering, reweight interface, search, new data or P9-P12 path was
   added.

The recorded probe, 11 focused, 122 synthetic and seven claim-control passing
tests plus compile/dependency/diff checks are sufficient. The 579-second test
and probe are not repeated in this review.

## Evidence Boundary

The sign reversal establishes that aggregate cross-protocol geometry is
sensitive to contribution magnitude for these exact batches. It does not prove
general causality, approve per-trajectory normalization as an optimizer, or
establish behavior improvement, robustness, model strength, Tenhou performance,
stable dan or LuckyJ comparison evidence.

## Direct Next Approval

```text
Approved: run one exact norm-matched unit-normalized aggregate update followed
by the two existing fixed evaluation windows.
```

Exact future files:

- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke.py`.
- Modify `src/mjlabai/rl/__init__.py` only if an export is required by the
  established local pattern.
- Direct governance synchronization only.

Exact contract:

1. Start from the reviewed imitation-trained initial parameters and collect
   only exact batches `0..31` and `116..147` once each.
2. Reuse the reviewed other-31 trajectory gradients. Normalize each full
   gradient to unit global L2, average 32 per protocol, then average the two
   protocol means. Do not project, clip or select.
3. Compute the original raw combined mean from the same two raw protocol means.
   Scale the unit-normalized combined direction once so its global L2 equals
   the raw combined mean global L2. No candidate scale or search is allowed.
4. Apply exactly one update at fixed reviewed rate `0.32` to one shared branch.
5. Evaluate only the existing zero-update windows `52..83` and `84..115` after
   the update. Retain every reward, trace, score and changed-seed record.
6. Record raw and pre/post-scale group/global geometry, scale coefficient,
   parameter deltas, provenance, one update and two evaluation calls.
7. Run one deterministic probe, focused tests and fast checks only. Do not run
   prior expensive smokes or the full suite.

Forbidden: a second update, projection, epsilon, clipping, identity ranking,
filtering, per-seed weights, scale/rate/seed/window search, selection, replay,
real data, strength claim or P9-P12. Zero docs gates remain before code.
