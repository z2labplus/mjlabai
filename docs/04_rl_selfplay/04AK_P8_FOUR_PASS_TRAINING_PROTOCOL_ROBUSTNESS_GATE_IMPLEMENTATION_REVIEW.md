# 04AK P8 Four-Pass Training-Protocol Robustness Gate Implementation Review

## Decision

```text
A. Review can close.
```

Commit `e498fcb` conforms to the exact `04AJ` approval. No code, test,
evidence or scope blocker was found.

## Reviewed Scope

- Commit: `e498fcb` (`Gate MahJax training protocol robustness claims`).
- Production file:
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate.py`.
- Test file:
  `tests/rl/test_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate.py`.
- Ten direct governance documents.
- Approval source: `04AJ`.

## Conformance Findings

1. Reviewed reference/alternate primary deltas are exactly `15/0` and
   replication deltas are exactly `121/0`.
2. Zero is not treated as positive improvement. Per-window reproduced fields
   are both false, protocol agreement is false and robustness is false.
3. Selection is explicitly prohibited. Protocol, model, pass and checkpoint
   selection fields are all `None`.
4. The result is frozen and array-free. It contains no parameters, threshold,
   winner, ranking or score field.
5. The builder takes no arguments and performs zero training/evaluation calls.
6. Source imports only `__future__`, `dataclasses` and `typing`. It does not
   import the expensive smoke modules, JAX, MahJax or environment code.
7. Source contains no path, file, serialization, subprocess, network or
   artifact behavior.
8. Warnings clearly deny robustness/generalization, selection, policy quality,
   model strength, stable-dan, Tenhou and LuckyJ claims.

## Validation Evidence

```text
Focused: 7 tests OK in 0.001 seconds
Fast synthetic RL regression: 122 tests OK in 0.033 seconds
Compile: OK
Dependency check: OK
git diff --check: OK
Commit/source/provenance review: OK
```

No expensive training or full suite is run in this review.

## Evidence Boundary

The gate correctly prevents selection after observed non-reproduction. It is
claim-control infrastructure, not evidence that either protocol or estimator
is strong. It does not establish robustness, generalization, model strength,
candidate promotion, Tenhou/stable-dan/LuckyJ performance or P9-P12 readiness.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement an exact two-protocol four-pass leave-one-out batch-baseline
variance-control training diagnostic.
```

Exact future files:

- `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`
- `tests/rl/test_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`
- direct governance synchronization only.

Exact implementation contract:

1. Reuse the reviewed categorical-MLP initialization, MahJax runtime,
   all-project trajectory collector, legal masking/log-probability model path
   and fixed evaluation helper.
2. Start two independent branches from identical reviewed parameters: exact
   reference ordered seeds `0..31` and exact alternate ordered seeds
   `116..147`.
3. Run exactly four passes per branch. For each pass, collect all 32 on-policy
   trajectories using unchanged pass-start parameters before any update.
4. Normalize four-seat cumulative raw returns by `100.0`. For each trajectory
   and seat, compute the baseline as the mean same-seat return of the other 31
   trajectories. The current trajectory must not contribute to its own
   baseline.
5. Actor-index each leave-one-out advantage. Define each trajectory objective
   as its mean negative advantage-weighted selected-action log probability,
   then define the pass objective as the mean of the 32 trajectory objectives.
6. Apply exactly one aggregated gradient update per pass at learning rate
   `0.01`: four updates per branch, eight total. No update may occur during
   trajectory collection.
7. Perform no evaluation between passes and no early stopping or selection.
8. After both branches finish, evaluate each final policy with zero updates on
   existing fixed primary `52..83` and replication `84..115` only. Compare
   against pinned initial vectors by immutable values; do not run an initial
   evaluation branch.
9. Retain complete per-pass trajectories, legal-action traces, leave-one-out
   baselines/advantages, objectives, parameter deltas and final fixed-window
   diagnostics in a frozen array-free result.
10. Accept and pin all results regardless of sign. Return no selected protocol,
    model, pass or checkpoint.
11. Run one deterministic probe to obtain expected values, then focused tests.
    Do not rerun the full 6955-second suite; use fast regression/static checks.

Forbidden:

- a third seed protocol, seed search, fifth pass or third evaluation window;
- online causal updates inside the 32-trajectory pass batch;
- threshold tuning, optimizer/rate search, critic, GAE, entropy, KL or clipping;
- replay, persistence, model artifact or production trainer;
- real data, external logs, Tenhou, league or model promotion;
- robustness/generalization/strength claims or P9-P12.

This is the first direct algorithmic variance-control experiment after the
non-reproduction finding. No additional proposal, boundary or approval document
is required before the exact code. Zero mandatory gates remain.
