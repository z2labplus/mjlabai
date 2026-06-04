# 05S_METRIC_REGISTRY_CONSISTENCY_REVIEW

## Review Scope

This document reviews P5 metric registry consistency across stable-dan,
legal-action and tiny benchmark diagnostics.

The review checks:

- metric names.
- metric units.
- `higher_is_better` directions.
- current implementation or schema status.
- source-note and evidence-grade consistency.
- non-evidence guardrails.

This is a docs-only review gate. It does not:

- add production code.
- change metric registry code.
- change metric units.
- change `higher_is_better` directions.
- add tests or fixtures.
- implement new metrics.
- add CLI or broad file ingestion.
- measure latency.
- calculate fixed-position exact-match.
- add legal-action checker, canonicalizer, broad evaluator or production
  evaluator logic.
- connect model output.
- call model APIs, OpenAI APIs, third-party binaries, Akochan `system.exe` or
  `libai.so`.
- read real Tenhou, real haifu, external logs or platform data.
- enter P6-P12.

The review supports the north-star target only indirectly by keeping P5
diagnostic metrics auditable before any training, league, model-output or
Tenhou validation work is allowed. It is not model-strength evidence and is not
a LuckyJ `10.68` comparison.

## Reviewed Artifacts

Source and registry:

```text
src/mjlabai/eval/offline_result.py
src/mjlabai/eval/stable_dan.py
src/mjlabai/eval/legal_action_metric.py
src/mjlabai/eval/tiny_benchmark_harness.py
src/mjlabai/eval/__init__.py
```

Evaluation docs:

```text
docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md
docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md
docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md
docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md
docs/05_evaluation/05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION.md
docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md
docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md
```

Tests and fixtures:

```text
tests/eval/test_stable_dan.py
tests/eval/test_placement_counts.py
tests/eval/test_stable_dan_report_smoke.py
tests/eval/test_legal_action_metric.py
tests/eval/test_legal_action_fixture_schema_smoke.py
tests/eval/test_tiny_benchmark_harness.py
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
tests/eval/test_offline_result.py
tests/eval/test_offline_envelope_smoke.py
tests/fixtures/eval/stable_dan_placements_smoke.json
tests/fixtures/eval/legal_action_metric_smoke.json
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
```

## Metric Consistency Table

| metric_name | subtrack | unit | higher_is_better | current_status | implementation / schema status | evidence grade | non-evidence warning |
|---|---|---:|---:|---|---|---|---|
| `stable_dan_point_estimate` | stable-dan | `dan` | true | implemented | deterministic calculator and report metric | P5 synthetic/local stable-dan diagnostic evidence only | point estimate is not LuckyJ proof |
| `stable_dan_ci_lower` | stable-dan | `dan` | true | implemented | bootstrap CI lower bound | P5 synthetic/local stable-dan diagnostic evidence only | synthetic CI is not ranked-game evidence |
| `stable_dan_ci_upper` | stable-dan | `dan` | true | implemented | bootstrap CI upper bound | P5 synthetic/local stable-dan diagnostic evidence only | upper bound is not a claim |
| `stable_dan_threshold_outcome` | stable-dan | `category` | null | implemented | threshold helper category | P5 synthetic/local stable-dan diagnostic evidence only | synthetic threshold output is not LuckyJ comparison evidence |
| `stable_dan_sample_size_status` | stable-dan | `category` | null | implemented | sample-size guardrail category | P5 synthetic/local stable-dan diagnostic evidence only | reportable status is not strength proof |
| `legal_action_rate` | legal-action | `rate` | true | implemented for synthetic fixture only | strict `dahai` synthetic evaluator | P5 synthetic/local legal-action diagnostic evidence only | legality is not model strength |
| `invalid_action_rate` | legal-action | `rate` | false | implemented for synthetic fixture only | strict `dahai` synthetic evaluator | P5 synthetic/local legal-action diagnostic evidence only | low invalid rate is not policy quality |
| `evaluated_decision_count` | legal-action | `count` | null | implemented for synthetic fixture only | denominator count | P5 synthetic/local legal-action diagnostic evidence only | count is not a ranking direction |
| `legal_action_count` | legal-action | `count` | null | implemented for synthetic fixture only | legal count | P5 synthetic/local legal-action diagnostic evidence only | count is not strength evidence |
| `invalid_action_count` | legal-action | `count` | null | implemented for synthetic fixture only | invalid count | P5 synthetic/local legal-action diagnostic evidence only | count is not strength evidence |
| `missing_action_count` | legal-action | `count` | null | implemented for synthetic fixture only | missing count | P5 synthetic/local legal-action diagnostic evidence only | count is not strength evidence |
| `parse_failure_count` | legal-action | `count` | null | implemented for synthetic fixture only | parse-failure count | P5 synthetic/local legal-action diagnostic evidence only | count is not strength evidence |
| `skipped_count` | legal-action | `count` | null | implemented for synthetic fixture only | skipped count | P5 synthetic/local legal-action diagnostic evidence only | skipped records are not evaluated decisions |
| `missing_action_rate` | legal-action | `rate` | false | implemented for synthetic fixture only | missing-action rate | P5 synthetic/local legal-action diagnostic evidence only | lower missing rate is not strength proof |
| `parse_failure_rate` | legal-action | `rate` | false | implemented for synthetic fixture only | parse-failure rate | P5 synthetic/local legal-action diagnostic evidence only | lower parse-failure rate is not strength proof |
| `command_exit_code` | wrapper/audit schema | `exit_code` | false | schema field only | registry placeholder for offline command summaries | P5 schema evidence only | exit code is not model quality |
| `latency_ms` | latency schema | `ms` | false | schema field only | envelope field; tiny benchmark currently uses `None` | P5 schema evidence only | no latency is measured in current tiny benchmark |
| `parse_success_rate` | parser schema | `rate` | true | placeholder definition only | not currently emitted by tiny benchmark | P5 schema evidence only | parse success is not model strength |
| `wrapper_smoke_success` | tiny benchmark | `boolean` | true | implemented for synthetic tiny benchmark envelope | fixed fixture smoke success metric | P5 synthetic/local engineering diagnostic evidence only | smoke success is not model quality |

## Findings

### Stable-Dan Metric Consistency

The stable-dan metric names, units and directions are consistent between
`offline_result.py`, `05J`, stable-dan smoke tests and the ranking protocol.

Stable-dan metrics are implemented for the current offline synthetic path:

- deterministic point estimate.
- bootstrap CI lower and upper bounds.
- categorical threshold outcome.
- categorical sample-size status.

The guardrails are conservative: synthetic fixtures, point estimates, reportable
status and low-sample threshold outcomes are not model-strength evidence and
cannot support a LuckyJ `10.68` claim.

### Legal-Action Metric Consistency

The legal-action metric names, units and directions are consistent between the
registry, `05J`, `05K`, `05M`, `legal_action_metric.py` and the current tests.

The count metrics correctly use `higher_is_better = None`. The diagnostic rates
use directions that match their semantics:

- `legal_action_rate`: higher is better as a legality diagnostic only.
- `invalid_action_rate`: lower is better.
- `missing_action_rate`: lower is better.
- `parse_failure_rate`: lower is better.

The review found no same-name semantic conflict. The current implementation is
still project-authored synthetic fixture only, strict `dahai` only, and not a
broad evaluator, legal-action checker, canonicalizer, CLI, model-output path or
strength measure.

### Tiny Benchmark Diagnostic Metric Consistency

The currently emitted tiny benchmark envelope metric is:

```text
wrapper_smoke_success
```

It is registered as `boolean` with `higher_is_better = true`, and the docs/tests
consistently frame it as engineering smoke success only. It is not model quality,
policy quality, Tenhou evidence, stable-dan evidence or LuckyJ comparison
evidence.

The current envelope also records:

- `sample_size = 1`.
- `latency_ms = None`.
- all safety flags false.
- synthetic/local warnings.
- evidence references.

These are envelope fields or metadata, not additional current metric registry
entries.

The tiny benchmark fixture includes future diagnostic names such as
`latency_ms_mean`, `latency_ms_p50`, `latency_ms_p95`, `latency_ms_max`,
`fixed_position_decision_count` and `fixed_position_exact_match_rate`. Those
names are shape-planning names in the synthetic fixture. They are not registered
metrics yet and are not emitted by the current tiny benchmark envelope. This is
not a blocker for current registry consistency because `05N`, `05O`, `05P`,
`05Q` and `05R` all keep them as future diagnostic planning, not implemented
metric evidence.

### Cross-Track Naming Consistency

No conflicting same-name metrics were found across the three subtracks.

- `stable_dan_*` names are stable-dan-specific.
- legal-action count/rate names use direct denominator/count semantics.
- `wrapper_smoke_success` is reserved for smoke/integration success.
- envelope-level `sample_size`, `warnings`, `evidence_refs`, safety flags and
  `latency_ms` remain envelope fields, not overloaded cross-track metric names.

### Unit Consistency

The reviewed units match the registry and `05J`:

- stable-dan estimates and CI bounds use `dan`.
- stable-dan outcomes and sample-size statuses use `category`.
- legal-action rates use `rate`.
- legal-action counts use `count`.
- command exit code uses `exit_code`.
- latency uses `ms`.
- parse success uses `rate`.
- wrapper smoke success uses `boolean`.

No unit blocker was found.

### Higher-Is-Better Direction Consistency

The reviewed directions are consistent:

- stable-dan point estimate and CI bounds: true.
- stable-dan category metrics: null.
- legal action rate: true as a legality diagnostic only.
- invalid, missing and parse-failure rates: false.
- count metrics: null.
- command exit code: false.
- latency: false if measured later; current tiny benchmark keeps `latency_ms =
  None`.
- parse success rate: true.
- wrapper smoke success: true as engineering smoke success only.

No direction blocker was found.

### Status and Source-Note Consistency

The current statuses are clear:

- stable-dan calculators/helpers, report schema and synthetic smoke paths exist.
- legal-action metrics are implemented only for the project-authored synthetic
  fixture.
- tiny benchmark emits only a synthetic fixed-fixture smoke success metric.
- command, latency and parse-success metrics remain schema/placeholder metrics
  unless emitted by a specific P5 task.

No source-note blocker was found. The registry source note correctly says some
metrics are placeholders for future evaluators and not implemented calculators
in the registry module.

### Evidence Grade Consistency

Evidence grades remain conservative and consistent:

- stable-dan synthetic fixture/report smoke: P5 synthetic/local stable-dan
  diagnostic evidence only.
- legal-action synthetic evaluator: P5 synthetic/local legal-action diagnostic
  evidence only.
- tiny benchmark harness: P5 synthetic/local engineering diagnostic evidence
  only.
- offline envelope coverage and this registry review: P5 synthetic/local review
  evidence only.

None of these are:

- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan evidence from real ranked games.
- LuckyJ `10.68` comparison evidence.
- candidate-promotion evidence.
- P6-P12 evidence.

### Promotion and Ranking Guardrail Consistency

`05F_ALGORITHM_RANKING_PROTOCOL.md` continues to prevent the major misuse cases:

- `legal_action_rate` must not rank model strength.
- `wrapper_smoke_success` must not rank model strength.
- synthetic stable-dan smoke fixtures must not support LuckyJ comparison.
- synthetic tiny benchmark envelopes must not support candidate promotion.
- P5 synthetic/local diagnostics must not be treated as Tenhou ranked evidence.

## Blockers

No blocker was found for the current P5 metric registry consistency.

## Follow-Up Needed

The tiny benchmark fixture already lists future diagnostic names for latency and
fixed-position diagnostics, but the current registry intentionally does not
define those future names as implemented metrics. A future P5-only task should
keep evidence taxonomy and promotion guardrails explicit before any broader
metric or harness work.

## Review Conclusion

```text
The P5 metric registry consistency review can close for the current
stable-dan, legal-action and tiny benchmark diagnostic scope.
```

No blocker was found. The next task remains P5-only.

## Evidence Grade

Current evidence grade:

```text
P5 synthetic/local metric registry consistency review evidence only.
```

## Explicit Non-Evidence

This review is not:

- production evaluator expansion.
- metric implementation.
- registry code change.
- latency measurement.
- legal-action checker.
- canonicalizer.
- fixed-position exact-match computation.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P6-P12 evidence.

## Next P5-Only Task Recommendation

The next narrow task should be:

```text
Review P5 synthetic/local evaluation evidence taxonomy and promotion guardrails.
```

That follow-up review is recorded in:

```text
docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md
```

It found no blocker in the current evidence taxonomy or promotion guardrails
and recommends defining P5 evaluation groundwork closure criteria next. The
follow-up remained docs/review only and reviewed the vocabulary used for P5
synthetic/local evidence grades, non-evidence warnings and promotion guardrails
across current stable-dan, legal-action, tiny benchmark and envelope review
artifacts.

The next task must not:

- add production code.
- add or modify tests.
- add fixtures.
- implement metrics.
- change registry code.
- measure latency.
- calculate fixed-position exact-match.
- add legal-action checker, canonicalizer or broad evaluator behavior.
- connect model output.
- add CLI or broad file ingestion.
- read real Tenhou, real haifu, external logs or platform data.
- call third-party binaries, Akochan `system.exe` or `libai.so`.
- train, tune, self-play, run league or runner behavior.
- enter P6-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game evidence,
  LuckyJ `10.68` comparison or candidate promotion.

## Verification

Recommended validation:

```bash
git diff --check
python3 -m unittest tests/eval/test_stable_dan.py
python3 -m unittest tests/eval/test_placement_counts.py
python3 -m unittest tests/eval/test_stable_dan_report_smoke.py
python3 -m unittest tests/eval/test_legal_action_metric.py
python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_tiny_benchmark_harness.py
python3 -m unittest tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_offline_result.py
python3 -m unittest tests/eval/test_offline_envelope_smoke.py
```
