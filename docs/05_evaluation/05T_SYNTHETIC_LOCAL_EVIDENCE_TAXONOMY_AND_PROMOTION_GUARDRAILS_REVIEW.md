# 05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW

## Review Scope

This document reviews P5 synthetic/local evaluation evidence taxonomy and
promotion guardrails.

The review checks:

- evidence-grade vocabulary.
- non-evidence warnings.
- promotion and ranking guardrails.
- LuckyJ / Tenhou / stable-dan claim boundaries.
- stage-boundary wording across P5 evaluation artifacts.
- governance, backlog, evidence-log and risk-register consistency.

This is a docs-only review gate. It does not:

- add production code.
- add or modify tests.
- add or modify fixtures.
- implement metrics.
- change metric registry code.
- change metric units or directions.
- change evidence taxonomy definitions.
- change promotion criteria.
- add CLI or broad file ingestion.
- measure latency.
- calculate fixed-position exact-match.
- add legal-action checker, canonicalizer, broad evaluator or production
  evaluator logic.
- connect model output.
- call model APIs, OpenAI APIs, third-party binaries, Akochan `system.exe` or
  `libai.so`.
- read real Tenhou, real haifu, external logs or platform data.
- train, tune, self-play, run league or run runner behavior.
- enter P6-P12.

The review supports the north-star target only indirectly by keeping P5
evidence wording conservative before any training, league, model-output or
Tenhou validation work is allowed. It is not model-strength evidence and is not
a LuckyJ `10.68` comparison.

P5 has accumulated many completed subtracks. The project should now avoid
extending P5 indefinitely through more schema/review churn. The next useful
P5-only step should define closure criteria and an exit-readiness checklist for
the evaluation groundwork stage rather than broaden implementation scope.

## Reviewed Artifacts

Evaluation documents:

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
docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md
```

Governance and tracking:

```text
docs/00_HANDOFF.md
docs/00_DOCS_INDEX.md
docs/10_next/10_NEXT.md
docs/09_governance/09_EVIDENCE_LOG.md
docs/09_governance/09_RISK_REGISTER.md
docs/09_governance/09_STAGE_TASK_CONTRACT.md
docs/07_development_execution/07B_TASK_BACKLOG.md
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
```

Read-only source, tests and fixtures used for context:

```text
src/mjlabai/eval/offline_result.py
src/mjlabai/eval/stable_dan.py
src/mjlabai/eval/legal_action_metric.py
src/mjlabai/eval/tiny_benchmark_harness.py
src/mjlabai/eval/__init__.py
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

## Evidence Taxonomy Table

| evidence_label | applies_to | allowed_interpretation | forbidden_interpretation | promotion_allowed | ranking_allowed | Tenhou_claim_allowed | LuckyJ_claim_allowed | notes |
|---|---|---|---|---:|---:|---:|---:|---|
| P5 synthetic/local stable-dan diagnostic evidence only | synthetic stable-dan fixtures, reports and API smoke paths | stable-dan calculation/reporting path works on synthetic/local inputs | model strength, Tenhou ranked result, stable-dan ranked-game evidence, LuckyJ proof | no | no | no | no | point estimate, CI and threshold helper are governance diagnostics until valid real samples exist |
| P5 synthetic/local legal-action diagnostic evidence only | synthetic legal-action evaluator and counts/rates | strict `dahai` legality branches work for project-authored fixture | policy quality, broad evaluator readiness, Tenhou legality, model strength | no | no | no | no | `legal_action_rate` is basic legality only |
| P5 synthetic/local engineering diagnostic evidence only | tiny benchmark harness and `wrapper_smoke_success` | fixed synthetic fixture can be validated and summarized | model quality, benchmark result, Tenhou evidence, stable-dan evidence | no | no | no | no | `wrapper_smoke_success` is smoke success only |
| P5 synthetic/local fixture schema smoke evidence only | schema-only fixtures and shape tests | fixture shape, safety flags and warning text match boundary | evaluator implementation, metric calculation, latency measurement | no | no | no | no | fixed-position expectation fields are future diagnostics only |
| P5 synthetic/local implementation review evidence only | implementation review docs for narrow synthetic tools | current fixture-scope implementation boundary was reviewed | permission to broaden evaluator, add CLI, use model output or real data | no | no | no | no | review can close current scope only |
| P5 synthetic/local offline envelope coverage review evidence only | offline envelope review for tiny benchmark diagnostics | existing envelope can represent current synthetic/local diagnostic | production evaluator expansion or evidence sufficiency for promotion | no | no | no | no | envelope records results; it does not generate or validate strength |
| P5 synthetic/local metric registry consistency review evidence only | metric registry consistency review | names, units, directions and statuses are consistent | metric implementation, registry code change, strength evidence | no | no | no | no | future latency/fixed-position names remain planning names |
| P5 synthetic/local review evidence only | general docs-only P5 review gates | wording, scope and guardrails were reviewed | implementation, promotion or ranked-game evidence | no | no | no | no | review gates do not change criteria |
| P5 schema evidence only | offline schema and placeholder registry entries | schema can record future result fields | implemented metric, production evaluator, strength evidence | no | no | no | no | schema fields may be placeholders |
| P5 synthetic/local diagnostic evidence only | umbrella label for current P5 synthetic/local outputs | local diagnostic infrastructure is auditable | P5 overall completion, model strength, Tenhou or LuckyJ evidence | no | no | no | no | use only when a more specific label is not needed |

## Promotion Guardrail Table

| artifact_or_metric | current_status | allowed_use | forbidden_use | promotion_guardrail | blocker |
|---|---|---|---|---|---|
| `stable_dan_point_estimate` | implemented for offline synthetic/local reports | diagnostic point estimate in a report | LuckyJ claim, model ranking, candidate promotion | needs valid sample source, enough games, CI lower-bound pass, sample-size guardrail and human review before any future claim | none |
| `stable_dan_ci_lower` | implemented for bootstrap reports | uncertainty diagnostic | proof from synthetic fixtures or low-sample reports | lower bound can matter only with valid samples, acceptable undefined rate and claim-ready sample size | none |
| `stable_dan_threshold_outcome` | implemented category | threshold-helper status for report wording | project-level LuckyJ comparison from synthetic/local smoke data | `clear_pass` semantics still require valid sample context and review | none |
| `legal_action_rate` | implemented for project-authored synthetic fixture only | basic legality diagnostic | strength ranking, policy quality, LuckyJ comparison | cannot promote candidates; only supports later diagnostic readiness | none |
| `invalid_action_rate` | implemented for project-authored synthetic fixture only | basic invalid-action diagnostic | strength ranking or policy quality | lower value is not candidate-promotion evidence | none |
| `missing_action_rate` | implemented for project-authored synthetic fixture only | missing-output diagnostic | model ranking or broad adapter quality claim | no promotion from fixture-only result | none |
| `parse_failure_rate` | implemented for project-authored synthetic fixture only | parse-failure diagnostic | model ranking or canonicalizer readiness claim | no promotion from fixture-only result | none |
| `wrapper_smoke_success` | implemented for synthetic tiny benchmark envelope | engineering smoke success | model quality, benchmark win, candidate promotion | smoke success cannot rank or promote | none |
| `sample_size` | envelope metadata | report denominator/scope | strength proxy or sufficient evidence by itself | sample size is necessary context, not a claim | none |
| `latency_ms = None` | current tiny benchmark envelope field | explicit no-latency-measured marker | latency benchmark, throughput claim, model speed claim | latency evidence requires a future approved task and method | none |
| `evidence_refs` | envelope metadata | trace the docs/tests/fixtures supporting a result | proof of strength or external validation by itself | references only identify evidence sources | none |
| safety flags | envelope metadata | record whether high-risk categories are involved | permission to use high-risk data or tools | current P5 synthetic/local smoke outputs keep flags false | none |
| synthetic/local warnings | envelope/report warnings | prevent overclaiming and document boundary | boilerplate that can be ignored for promotion | warnings must remain visible in reviews and reports | none |
| future tiny benchmark latency percentile names | fixture planning names only | future metric-name planning | current registered/emitted metrics or measured latency | require future approved metric/harness task before use | none |
| future fixed-position exact-match planning names | fixture planning names only | future diagnostic planning | current exact-match computation, supervised accuracy or policy quality | require future schema/evaluator task before use | none |

## Findings

### Evidence Taxonomy Vocabulary Consistency

The reviewed evidence labels are conservative and non-conflicting.

The specific labels separate:

- stable-dan diagnostic evidence.
- legal-action diagnostic evidence.
- engineering diagnostic evidence.
- fixture schema smoke evidence.
- implementation review evidence.
- offline envelope coverage review evidence.
- metric registry consistency review evidence.
- generic P5 synthetic/local review evidence.
- P5 schema evidence.

No label was found that upgrades synthetic/local artifacts into strength
evidence, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ
comparison evidence or candidate-promotion evidence. P5 overall remains marked
open.

### Non-Evidence Warning Consistency

The non-evidence warnings are consistent across the current P5 docs:

- synthetic stable-dan smoke is not LuckyJ threshold evidence.
- legal-action synthetic evaluator output is not model quality or policy
  quality evidence.
- `wrapper_smoke_success` is not model quality evidence.
- offline envelope and metric registry reviews are not production evaluator
  evidence.
- future tiny benchmark latency and fixed-position planning names are not
  current implemented evidence.

The wording varies slightly between `model-strength evidence` and `model
strength evidence`, but the meaning is consistent and not a blocker.

### Stable-Dan Promotion Guardrails

Stable-dan guardrails remain conservative.

Current synthetic/local stable-dan fixtures and smoke reports are diagnostic
only. They can validate calculations, bootstrap behavior, threshold-helper
categories, sample-size reporting and JSON serialization. They cannot support a
LuckyJ `10.68` claim or model-strength statement.

Any future project-level LuckyJ comparison still needs:

- a lawful and valid sample source.
- consistent room/rules context.
- enough games and fourth-place count.
- acceptable undefined bootstrap resample rate.
- bootstrap lower bound above `10.68`.
- sample-size guardrail readiness.
- complete report schema.
- human review and later evaluation protocol.

### Legal-Action Guardrails

Legal-action guardrails remain conservative.

The current evaluator is only for the project-authored synthetic fixture. It
uses strict `dahai` matching over actor, action type, tile and `tsumogiri`.
It is not a broad evaluator, canonicalizer, legal-action checker, rule engine,
CLI, file-ingestion path or model-output integration.

The current counts/rates show only branch coverage and basic legality
diagnostics for the fixture. They do not show model strength, policy quality,
Tenhou ranked performance or LuckyJ comparison readiness.

### Tiny Benchmark Guardrails

Tiny benchmark guardrails remain conservative.

The current harness only loads the project-authored synthetic fixture and emits
an offline envelope with:

- `evaluation_type = "tiny_benchmark_harness"`.
- `wrapper_smoke_success = true`.
- `sample_size = 1`.
- `latency_ms = None`.
- all safety flags false.
- synthetic/local warnings.
- evidence references.

`wrapper_smoke_success` is engineering smoke success only. `sample_size = 1`
only records the fixed synthetic fixture scope. `latency_ms = None` explicitly
records that no latency was measured. Future latency percentile and
fixed-position exact-match names remain planning names, not current metrics or
evidence.

### Offline Envelope / Metric Registry Guardrails

Offline envelope and registry guardrails remain consistent.

The envelope records P5 diagnostic results produced elsewhere. It does not
execute training, self-play, league, Tenhou or platform automation. It does not
turn a diagnostic into strength evidence.

The registry records metric names, units, directions and descriptions. It is
not a calculator, evaluator or promotion gate. Registry consistency review is
not metric implementation or registry code change.

### Stage-Boundary Consistency

The reviewed docs continue to state that the active work is P5 evaluation
groundwork. They continue to forbid:

- P6-P12.
- training or tuning.
- self-play.
- league or runner behavior.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- model-output integration.
- CLI or broad file ingestion.
- latency measurement code.
- model-strength claims.

P5 overall is still open. However, many P5 subtracks are already complete for
their current synthetic/local scope. The next task should begin defining P5
closure criteria instead of adding more open-ended review gates.

### Governance / Backlog / Risk Consistency

The governance and tracking docs are consistent with the review:

- evidence log entries classify P5 outputs as internal synthetic/local or
  review-gate evidence, not external ranked evidence.
- risk register entries cover overclaiming synthetic diagnostics as strength,
  promotion or LuckyJ evidence.
- backlog and `10_NEXT` keep only one active P5 task.
- stage contract preserves the P5 versus P6-P12 boundary.

The main governance gap is not a blocker: because P5 has grown broad, the next
task should define stage closure criteria and exit readiness so P5 does not
continue indefinitely.

## Blockers

No blocker was found for the current P5 synthetic/local evidence taxonomy and
promotion guardrails.

## Follow-Up Needed

The next task should define how P5 evaluation groundwork can close.

That follow-up should identify:

- which P5 subtracks are complete for current scope.
- which remaining items are necessary versus optional.
- what evidence is required before any transition beyond P5.
- which tasks must remain explicitly out of scope until a later stage.
- what minimum checklist must be satisfied before broader harness, model-output,
  real-data, league or training work can even be proposed.

## Review Conclusion

```text
The P5 synthetic/local evaluation evidence taxonomy and promotion guardrails
review can close for the current stable-dan, legal-action, tiny benchmark,
offline envelope and metric registry diagnostic scope.
```

No blocker was found. The next task remains P5-only and should define P5
evaluation-groundwork closure criteria and an exit-readiness checklist.

## Evidence Grade

Current evidence grade:

```text
P5 synthetic/local evidence taxonomy and promotion guardrails review evidence only.
```

## Explicit Non-Evidence

This review is not:

- production evaluator expansion.
- metric implementation.
- registry code change.
- promotion criteria change.
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
Define P5 evaluation groundwork closure criteria and exit readiness checklist.
```

That task should remain docs/review/spec only. It should not close P5
automatically. It should define the minimum necessary closure criteria,
remaining required items, optional deferred items and explicit non-entry
conditions for P6-P12.

The next task must not:

- add production code.
- add or modify tests.
- add fixtures.
- implement metrics.
- change registry code.
- change promotion criteria.
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
