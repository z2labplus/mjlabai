# 04AO P8 Symmetric Conflict-Projected Update Implementation Review

## Decision

```text
A. Review can close.
```

Commit `032a340` conforms to the exact `04AN` approval. No code, test,
evidence or scope blocker was found.

## Conformance Findings

1. The implementation reuses identical reviewed initialization and exact
   first batches `0..31` and `116..147`.
2. It reproduces the reviewed negative original dot, computes both projection
   coefficients from the unmodified original pair and applies the single
   simultaneous symmetric formula. There is no sequential/random order.
3. It averages the two projected gradients and applies exactly one update at
   the fixed reviewed effective mean-gradient rate `0.32`.
4. Original cosine is approximately `-0.1868775008`; projected cosine is
   `+0.1868781623`. Combined global norm is `0.0209439239`, and all four
   parameter groups change.
5. Final evaluation occurs only on exact zero-update windows `52..83` and
   `84..115`. Both reward vectors/sums remain exact initial `-312/-1056`, with
   zero changed seeds.
6. Complete training/evaluation geometry and provenance are frozen and array-
   free. No protocol/model/multiplier/projection/pass/checkpoint is selected.
7. Source contains one fixed formula/rate, two exact batches/evaluations and no
   candidate search, I/O, replay, artifact, external or real-data behavior.

## Validation Evidence

```text
Deterministic probe: completed in 733.19 seconds
Focused: 9 tests OK in 722.105 seconds (727.67 seconds wall)
Fast synthetic RL regression: 122 tests OK in 0.046 seconds
Claim-control regression: 7 tests OK in 0.001 seconds
Compile/dependency/static/diff checks: OK
Commit/source/provenance review: OK
```

The diagnostic, prior expensive smokes and full suite are not rerun here.

## Evidence Boundary

The projection changes gradient geometry and parameters but not fixed-window
behavior after one update. This is a valid no-observed-behavior-change result,
not a failed test and not evidence of improvement, robustness, model strength,
promotion, Tenhou/stable-dan/LuckyJ performance or P9-P12 readiness.

One step cannot distinguish argmax invariance from a method that needs bounded
continuation. Searching update scale or projection variants would introduce
post-hoc selection. The next falsifiable task therefore keeps every mechanism
fixed and only extends to the already reviewed four-pass horizon.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement an exact four-pass shared-policy symmetric conflict-projected
training and fixed-window diagnostic.
```

Exact future files:

- Modify the one-step projected-update source only to factor its exact private
  projection/update calculation into a reusable private helper while
  preserving public one-step behavior.
- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke.py`.
- Direct governance synchronization only. Do not modify existing expensive
  focused tests unless a compatibility blocker is found.

Exact implementation contract:

1. Start one shared branch from the reviewed imitation parameters.
2. Perform exactly four passes. At each pass-start parameters, independently
   collect exact frozen-policy batches `0..31` and `116..147`, 32 trajectories
   each, with the same other-31 baselines/objectives/mean gradients.
3. At each pass, apply the exact one-step simultaneous projection formula to
   that pass's original pair, average once and update once at fixed `0.32`.
   Carry updated parameters directly into the next pass.
4. Record all four original/projected dot/cosine values, norms, coefficients,
   combined gradients, parameter deltas and complete batch provenance. Accept
   positive, zero or negative values; do not skip or select a pass.
5. Perform no intermediate evaluation. After pass four, evaluate exactly once
   on zero-update `52..83` and `84..115`; retain any result sign and compare
   only to reviewed initial vectors.
6. Totals must be 256 training trajectories, four updates, two evaluation
   calls and zero evaluation updates. Return frozen array-free diagnostics and
   no protocol/model/multiplier/projection/pass/checkpoint selection.
7. Run one deterministic probe, focused and fast checks only. Do not run the
   one-step focused test, prior four-pass focused tests or the full suite.

Forbidden:

- fifth pass, alternate update count or intermediate evaluation;
- projection formula/order/coefficient/epsilon/threshold search;
- multiplier/rate/optimizer/entropy/temperature/exploration search;
- third protocol, seed search or third evaluation window;
- critic, GAE, clipping, replay, persistence or artifact;
- external/real data, Tenhou, league, selection or P9-P12;
- robustness/generalization/policy-quality/model-strength claims.

No additional proposal, boundary, review-before-code or approval document is
required. Zero mandatory gates remain before exact code.
