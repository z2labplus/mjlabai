# 12AQ_P8_LINEAR_MODEL_TRAINING_ACCEPTANCE_AND_GREEDY_DECISION_APPROVAL

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact minimal implementation task.
```

The exact linear action-value model training implemented in `870befb` and
reviewed in `12AP` is accepted only for its fixed synthetic/local scope.

The next executable task is:

```text
Implement exact P8 synthetic/local linear-model inference and greedy-decision
diagnostic only.
```

No proposal, boundary or additional approval may be inserted before code.

## Why This Outcome

The reviewed trainer proves actual deterministic parameter updates. The
smallest materially progressive step is to use one frozen model to compute
action values and deterministic greedy decisions for fixed project-authored
synthetic/local probes. This closes the first training-to-model-output link
without adding an environment, gameplay, self-play, model loading, file
ingestion, persistence or production evaluation.

Another trainer wrapper or docs-only boundary is forbidden.

## Exact Approved Files

The implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_linear_greedy_decision_smoke.py`
- `tests/rl/test_synthetic_linear_greedy_decision_smoke.py`
- direct docs/governance synchronization required by repository rules.

No fixture, data file, dependency, CLI, path reader, model loader,
persistence, checkpoint or artifact file is approved.

## Exact Public API

The new module may export only:

```text
SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION
SyntheticLinearGreedyDecisionSmokeError
SyntheticLinearDecisionProbe
SyntheticLinearDecision
SyntheticLinearGreedyDecisionDiagnosticResult
run_synthetic_linear_greedy_decision_diagnostic
```

It must reuse `SyntheticLinearActionValueModel` and the reviewed private model/
feature/action-value validation helpers from
`synthetic_linear_action_value_training_smoke`. It must not duplicate the
linear action-value formula or add a generic model/inference framework.

## Exact Probe Boundary

`SyntheticLinearDecisionProbe` is frozen and contains only:

```text
probe_id
source_kind
features
legal_action_indices
project_authored
synthetic
local_only
uses_real_data
uses_external_log
uses_platform_data
uses_model_output
uses_self_play
```

The diagnostic accepts:

- one exact `SyntheticLinearActionValueModel`.
- one exact tuple of exactly three exact probes.
- pairwise-distinct non-empty probe IDs.
- canonical project-authored synthetic/local source and exact safe provenance
  flags.
- exact two-float feature tuples validated by the reviewed helper.
- `legal_action_indices` as the exact tuple `(0, 1)` only.

Lists, mappings, strings, bytes, bytearrays, paths, generators, tuple
subclasses and arbitrary iterables are rejected for the outer tuple, features
and legal-action tuple. No real/external/platform/model-generated probe input
is approved.

## Exact Inference And Decision Semantics

For each probe in input order, the diagnostic must:

1. normalize the model through the reviewed model helper.
2. validate and normalize the exact probe.
3. compute `Q(features, 0)` and `Q(features, 1)` exactly once each through the
   reviewed action-value helper.
4. preserve action values as exact tuple `(q0, q1)`.
5. set `tie_detected = (q0 == q1)`.
6. select action `1` only when `q1 > q0`; otherwise select action `0`.

The exact tie rule is therefore lower-index action `0`. No randomness,
sampling, softmax, temperature, epsilon-greedy, fallback, legality engine,
environment or gameplay behavior is approved.

## Exact Per-Probe Decision

`SyntheticLinearDecision` is frozen and contains only:

```text
probe_id
features
legal_action_indices
action_values
selected_action_index
tie_detected
```

## Exact Diagnostic Result

`SyntheticLinearGreedyDecisionDiagnosticResult` is frozen and contains only:

```text
diagnostic_version
model
probe_count
decisions
probe_ids
inference_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Requirements:

- `probe_count = 3`.
- normalized frozen model is preserved.
- decisions and IDs preserve input order.
- `inference_applied = true`.
- `safety_guardrails_all_satisfied = true`.

Warnings must include at least:

- synthetic/local linear-model inference and greedy-decision diagnostic only.
- fixed two features, two actions and three probes.
- deterministic lower-action-index tie break.
- no environment, gameplay, replay buffer or self-play.
- no model loading, external dependency, persistence or checkpoint.
- not production inference or evaluation.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The focused test module must cover:

1. exact action values and decisions for three fixed probes.
2. exact lower-index tie behavior.
3. integration with the reviewed trainer's frozen final model.
4. exact three-probe outer tuple/type and tuple-subclass rejection.
5. exact feature and `(0, 1)` legal-action tuple validation.
6. exact source/provenance flags and pairwise-distinct probe IDs.
7. reviewed model/feature/action-value helper reuse and no formula copy.
8. deterministic repeated output, complete input non-mutation and frozen
   output.
9. exact result/decision fields, counts, evidence grade and warnings.
10. package imports, narrow API and absence of file/model-loading/persistence/
    environment/replay/self-play/production-evaluation APIs.
11. invalid and huge numeric model/feature inputs use the approved diagnostic
    error with chained original cause where applicable.

Validation must include the 125 currently approved tests, the new focused
tests, compile checks and `git diff --check`.

## Error Boundary

Errors from the reviewed model/feature/action-value helpers must be wrapped as
`SyntheticLinearGreedyDecisionSmokeError` with probe index where relevant and
the original exception chained. No raw validation or numeric exception may
leak.

## Forbidden Scope

This approval does not permit:

- dynamic feature/action dimensions or probe count other than exactly three.
- model loading, serialization, persistence, checkpoint or artifact use.
- stochastic action selection, softmax, epsilon-greedy or exploration.
- environment, episode, gameplay, legality engine, replay buffer or self-play.
- training changes, optimizer, tensor/autograd framework or new model class.
- production inference/evaluation, metrics, ranking or candidate selection.
- path/CLI, dependency, timing, concurrency, GPU/distributed or third-party
  binary/service use.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- broad P8, league, strength claims or P9-P12.

## Evidence Grade

Current decision evidence:

```text
P8 fixed linear model-training current-scope acceptance and exact synthetic/
local greedy-decision task approval evidence only.
```

Future passing implementation evidence:

```text
P8 exact synthetic/local linear-model inference and greedy-decision diagnostic
evidence only.
```

Neither is production inference/evaluation, environment/self-play,
model-strength, Tenhou ranked, stable-dan, LuckyJ comparison,
candidate-promotion or P9-P12 evidence.

## Gate Accounting

```text
linear model-training current-scope acceptance = satisfied by this decision
greedy-decision diagnostic approval = satisfied by this decision
exact file/API/input/formula/output/test boundaries = satisfied
remaining mandatory gate count before implementation = 0
```

No gate is satisfied for broader P8.
