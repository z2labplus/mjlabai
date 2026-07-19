# 04AL P8 Leave-One-Out Batch Training-Protocol Implementation Review

## Decision

```text
A. Review can close.
```

Commit `e0f346a` conforms to the exact `04AK` approval. No code, test,
evidence or scope blocker was found.

## Reviewed Scope

- Commit: `e0f346a` (`Diagnose MahJax batch baseline variance control`).
- Production file:
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`.
- Test file:
  `tests/rl/test_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`.
- Ten direct governance documents.
- Approval source: `04AK`.

## Conformance Findings

1. Two independent branches start from identical reviewed parameters and use
   exact ordered training seeds `0..31` and `116..147`.
2. Each branch performs exactly four passes. Every pass freezes pass-start
   parameters while collecting all 32 trajectories, then applies one update.
3. Every trajectory/seat baseline is the normalized same-seat mean of the
   other 31 trajectories. The current trajectory is excluded, and per-seat
   advantage sums center to numerical zero.
4. Each trajectory objective is its mean actor-indexed negative advantage-
   weighted log probability. The pass objective is the mean of 32 trajectory
   objectives and uses one update at learning rate `0.01`.
5. There are 256 training trajectories and eight aggregate updates total. All
   actions are legal and all rounds terminate.
6. No evaluation occurs between passes. Each final branch uses only zero-update
   fixed primary `52..83` and replication `84..115` evaluation.
7. Both branches lower each pass objective and change all parameter groups.
   Final parameter changes are approximately `0.0004/0.0010` in the largest
   groups, substantially smaller than the prior online-update diagnostic.
8. Both branches retain exact initial primary and replication reward vectors/
   sums `-312/-1056`, with zero changed reward seeds. Reducing update-order
   variance does not produce observed fixed-window behavior improvement.
9. Complete trajectories, legal actions, leave-one-out baselines/advantages,
   objectives, parameter deltas and evaluation records remain frozen and
   array-free. No protocol/model/pass/checkpoint is selected.
10. Source probes find bounded loops, two evaluation call sites used once per
    branch, no open-ended loop and no path, serialization, network, subprocess,
    replay or artifact behavior.

## Validation Evidence

```text
Deterministic probe: completed in 2443.53 seconds
Focused: 10 tests OK in 2440.773 seconds (2449.75 seconds wall)
Fast synthetic RL regression: 122 tests OK in 0.035 seconds
Compile: OK
Dependency check: OK
git diff --check: OK
Commit/source/provenance review: OK
```

The 6955-second full suite and the 2440-second focused suite are not rerun in
this review.

## Evidence Boundary

The observed protocol agreement is agreement on no fixed-window reward change,
not robust improvement. This does not establish policy quality, a useful
checkpoint, model strength, candidate promotion, Tenhou/stable-dan/LuckyJ
performance or P9-P12 readiness.

The result isolates a plausible bottleneck: averaging 32 gradients while
retaining learning rate `0.01` makes each pass update small. A third seed range
would not address this mechanism and is rejected.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement an exact batch-size-compensated leave-one-out batch-gradient
diagnostic for the same two protocols.
```

Exact future files:

- Modify
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`
  only to let its private batch/protocol helpers accept an explicit gradient
  multiplier while preserving the existing public mean-gradient run at `1.0`.
- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke.py`.
- Direct governance synchronization only. Do not modify the existing expensive
  focused test unless a real compatibility blocker is found.

Exact implementation contract:

1. Reuse the reviewed leave-one-out batch collection, baseline, objective and
   protocol helpers. Preserve the existing mean-gradient public run exactly.
2. Add an explicit private gradient multiplier. The existing run passes `1.0`.
   The new compensated run passes exactly `32.0`, so one update equals the sum
   of the 32 trajectory gradients at base learning rate `0.01`.
3. Use no alternative multiplier, threshold search or adaptive scaling.
4. Run the same independent identical-init protocols `0..31` and `116..147`,
   four passes each, with 32 frozen-policy trajectories and one compensated
   update per pass.
5. Use only final zero-update fixed `52..83` and `84..115` windows. Do not run
   the mean-gradient or online reference branches inside the new smoke; compare
   against their reviewed immutable summaries.
6. Retain complete batch/update/evaluation diagnostics, the base rate `0.01`,
   multiplier `32.0` and effective mean-gradient rate `0.32` in a frozen,
   array-free result.
7. Accept and pin results regardless of sign. Return no selected protocol,
   model, pass or checkpoint.
8. Run one deterministic probe and focused/fast checks only. Do not run the
   existing 2440-second focused test or the full suite.

Forbidden:

- any multiplier other than `32.0`, scale/rate search or adaptive tuning;
- a third seed protocol, fifth pass or third evaluation window;
- critic, GAE, entropy, KL, clipping, optimizer search or replay;
- persistence, artifacts, real data, external logs, Tenhou or league;
- selection, robustness/generalization/strength claims or P9-P12.

No additional proposal, boundary or approval document is required before this
exact code. Zero mandatory gates remain.
