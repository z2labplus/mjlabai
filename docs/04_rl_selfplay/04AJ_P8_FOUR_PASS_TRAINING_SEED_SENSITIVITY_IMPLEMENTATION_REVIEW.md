# 04AJ P8 Four-Pass Training-Seed Sensitivity Implementation Review

## Decision

```text
A. Review can close.
```

Commit `e462ff3` conforms to the exact `04AI` approval. No code, test,
evidence or scope blocker was found.

## Reviewed Scope

- Commit: `e462ff3` (`Diagnose MahJax four-pass training seed sensitivity`).
- Production file:
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke.py`.
- Test file:
  `tests/rl/test_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke.py`.
- Ten direct governance documents.
- Approval source: `04AI`.

## Conformance Findings

1. Alternate training uses exact ordered seeds `116..147` for four passes and
   128 attempts, with the reviewed initialization, learning rate `0.01` and
   causal prior-record per-seat running baseline.
2. The reference training branch is not rerun. Reviewed reference rewards are
   compared by immutable values.
3. No evaluation occurs between passes. Exactly two evaluation call sites run
   after alternate training on fixed primary `52..83` and replication
   `84..115`; both perform zero updates.
4. Training, primary and replication seed sets are pairwise disjoint. All
   training actions are legal and every round terminates.
5. Parameters change. Per-pass nonzero update counts are `(24,32,32,32)`, and
   final per-seat parameter deltas are all positive.
6. Alternate final primary rewards exactly equal the initial vector/sum
   `-312`; the alternate is `15` below the reference final `-297`.
7. Alternate final replication rewards exactly equal the initial vector/sum
   `-1056`; the alternate is `121` below the reference final `-935`.
8. The reference fixed-window improvements therefore do not reproduce under
   the alternate training-seed protocol. This is training-protocol sensitivity,
   not a failed test and not evidence for selecting the reference protocol.
9. Complete training/update and final evaluation diagnostics are retained in a
   frozen, array-free result. No parameters or artifacts are returned or saved.
10. Selected training protocol, pass and checkpoint fields remain `None`.
11. Source probes find one exact bounded four-pass loop, two `_evaluate` call
    sites, zero reference reruns and no open-ended loop, path, serialization,
    subprocess, network or external-data behavior.

## Validation Evidence

```text
Focused: 11 tests OK in 1238.800 seconds
Full explicit suite: 510 tests OK in 6943.869 seconds; 2 existing skips
Full command wall time: 6955.03 seconds
Compile: OK
Dependency check: OK
git diff --check: OK
Commit/source/provenance review: OK
```

The expensive suites are not rerun in this review. Their committed evidence is
reused, while commit checks and lightweight source/provenance probes are run
against `e462ff3`.

## Evidence Boundary

The two observed training protocols disagree on whether either fixed window
improves. Therefore neither protocol may be selected and no robust improvement
is established. This evidence does not establish:

- generalization, policy quality or optimizer superiority;
- a selected protocol, model, pass or checkpoint;
- model strength, candidate promotion or league superiority;
- Tenhou, stable-dan or LuckyJ 10.68 performance;
- P9-P12 readiness.

A third seed range, fifth pass or third evaluation window is rejected as the
next action. It would add selection opportunity and substantial runtime without
first enforcing the already observed non-reproduction boundary.

## Runtime Finding

The explicit suite now takes `6955.03s` wall time. This is a realized delivery
risk. The next task must be fast and must not import or execute either expensive
training function. Future reviews should use focused tiers plus recorded full-
suite evidence unless behavior changes justify another complete run.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement a fast no-selection two-protocol robustness evidence gate over the
reviewed MahJax four-pass summary values only.
```

Exact future files:

- `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate.py`
- `tests/rl/test_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate.py`
- direct governance synchronization only.

Exact implementation contract:

1. Use only reviewed immutable summary values for reference and alternate
   protocols: primary deltas `15/0` and replication deltas `121/0`.
2. Add no MahJax/JAX/environment/training/evaluation call and do not import the
   two expensive smoke modules.
3. Return one frozen, array-free report that records both protocol IDs, both
   fixed-window deltas, disagreement/non-reproduction, robustness false and
   all selection fields `None`.
4. Use no tunable threshold and no winner/ranking score. Zero is not a positive
   improvement.
5. Classify the output only as P8 local reviewed-summary evidence gating.
6. Tests must run quickly and pin exact values, frozen output, no-selection
   behavior, warnings and absence of expensive/runtime/I-O imports or calls.

Forbidden:

- training, evaluation rollout, another seed protocol/window/pass or search;
- model/protocol/checkpoint selection, ranking or promotion;
- JAX, MahJax, environment, model parameters or artifacts;
- real data, external logs, Tenhou, league or P9-P12;
- robustness, generalization or strength claims.

No additional proposal, boundary or approval document is required before this
exact code. Zero mandatory gates remain.
