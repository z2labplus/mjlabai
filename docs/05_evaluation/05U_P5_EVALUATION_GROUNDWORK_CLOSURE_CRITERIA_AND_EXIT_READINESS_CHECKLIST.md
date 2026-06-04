# 05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST

## Scope

This document defines P5 evaluation groundwork closure criteria and an exit
readiness checklist.

It does not close P5. It defines how P5 can later be reviewed for closure.

This is a docs-only closure criteria / exit readiness specification. It does
not:

- add production code.
- add tests or fixtures.
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
- train, tune, self-play, run league or runner behavior.
- enter P6-P12.

The purpose is to stop P5 from extending indefinitely through more
schema/review churn. P5 is near closure, but it remains open until a later
closure review gate confirms readiness.

## Current P5 Scope

Current P5 evaluation groundwork covers:

- stable-dan calculation/reporting groundwork.
- offline evaluation result envelope and metric registry.
- legal-action synthetic/local diagnostic evaluator.
- action canonicalization schema and boundary.
- tiny benchmark synthetic/local fixture schema.
- tiny benchmark synthetic/local harness.
- metric registry consistency.
- synthetic/local evidence taxonomy and promotion guardrails.
- governance, evidence log, risk register, backlog, handoff and `10_NEXT`
  consistency.

It does not cover:

- production evaluator expansion.
- broad evaluator or rule engine.
- model-output integration.
- real Tenhou, real haifu, external logs or platform data.
- CLI or broad file ingestion.
- latency measurement.
- fixed-position exact-match computation.
- training, tuning, self-play, league or runner behavior.
- candidate promotion.
- LuckyJ `10.68` validation.
- P6-P12 execution.

## Current P5 Subtrack Inventory

| subtrack | current artifact(s) | current status | evidence grade | current-scope complete? | blocker | defer notes |
|---|---|---|---|---:|---|---|
| stable-dan evaluation API | `05H`, `stable_dan.py`, stable-dan tests | implemented/documented for synthetic/local API path | P5 synthetic/local stable-dan diagnostic evidence only | yes | none | real ranked-game evidence deferred |
| stable-dan smoke report path | `stable_dan_placements_smoke.json`, `test_stable_dan_report_smoke.py` | synthetic placement-to-report smoke path implemented | P5 synthetic/local stable-dan diagnostic evidence only | yes | none | real sample claim path deferred |
| stable-dan groundwork review | `05I` | current-scope complete, P5 still open | P5 synthetic/local review evidence only | yes | none | final project-level LuckyJ proof deferred |
| offline envelope schema | `offline_result.py`, `05J`, `test_offline_result.py` | implemented/tested | P5 schema evidence only | yes | none | broader production result sources deferred |
| synthetic stable-dan envelope smoke | `test_offline_envelope_smoke.py` | implemented/tested | P5 synthetic/local offline envelope smoke evidence only | yes | none | real data envelope use deferred |
| legal-action metric spec | `05K` | denominators, counts/rates, skipped/missing/parse-failure rules defined | P5 synthetic/local legal-action diagnostic spec evidence only | yes | none | broad legality evaluator deferred |
| action canonicalization schema | `05L` | current minimum `dahai` + strict schema defined | P5 synthetic/local schema evidence only | yes | none | reach/chi/pon/kan/hora/ryukyoku and canonicalizer implementation deferred |
| legal-action synthetic fixture schema | `legal_action_metric_smoke.json`, `test_legal_action_fixture_schema_smoke.py` | project-authored synthetic fixture shape implemented/tested | P5 synthetic/local fixture schema smoke evidence only | yes | none | real model-output fixtures deferred |
| legal-action synthetic evaluator | `legal_action_metric.py`, `test_legal_action_metric.py` | implemented for project-authored fixture only | P5 synthetic/local legal-action diagnostic evidence only | yes | none | broad evaluator/rule engine deferred |
| legal-action evaluator coverage review | `05M` | minimum outcome coverage complete for synthetic `dahai` + strict scope | P5 synthetic/local review evidence only | yes | none | complete real action-space coverage deferred |
| tiny benchmark boundary | `05N` | future harness boundary defined | P5 docs-only boundary evidence only | yes | none | broad harness scope deferred |
| tiny benchmark fixture schema | `tiny_benchmark_harness_smoke.json`, schema smoke test, `05O` | synthetic/local fixture shape implemented and reviewed | P5 synthetic/local fixture schema smoke evidence only | yes | none | model-output/fixed-position real data deferred |
| tiny benchmark harness implementation | `tiny_benchmark_harness.py`, `test_tiny_benchmark_harness.py`, `05P` | fixed project-authored synthetic fixture harness implemented | P5 synthetic/local engineering diagnostic evidence only | yes | none | latency measurement and broad benchmark deferred |
| tiny benchmark implementation review | `05Q` | current fixture-scope implementation reviewed | P5 synthetic/local implementation review evidence only | yes | none | broader implementation deferred |
| tiny benchmark envelope coverage | `05R` | current diagnostic can be represented in existing envelope | P5 synthetic/local offline envelope coverage review evidence only | yes | none | additional metrics deferred |
| metric registry consistency | `05S` | current names, units, directions and statuses reviewed | P5 synthetic/local metric registry consistency review evidence only | yes | none | future metric additions deferred |
| evidence taxonomy / promotion guardrails | `05T` | evidence labels and non-evidence warnings reviewed | P5 synthetic/local evidence taxonomy and promotion guardrails review evidence only | yes | none | promotion criteria changes deferred |
| P5 closure criteria / exit readiness | this document | closure criteria defined; not reviewed yet | P5 closure criteria specification evidence only | near complete | needs review gate | closure decision deferred to next task |
| final P5 closure review | not yet created | not started | none yet | no | required before closure | must be a separate review gate |

## P5 Closure Criteria

P5 can be considered for closure only when all of the following are true:

1. Every current-scope P5 subtrack has a clear documentation entry.
2. Key P5 artifacts are listed in `docs/00_DOCS_INDEX.md`.
3. `docs/00_HANDOFF.md` clearly states the current stage, completed P5
   subtracks, remaining items and next step.
4. `docs/10_next/10_NEXT.md` has exactly one active P5 closure/review/finalize
   task.
5. `docs/09_governance/09_EVIDENCE_LOG.md` classifies all P5 synthetic/local
   evidence conservatively.
6. `docs/09_governance/09_RISK_REGISTER.md` covers synthetic evidence
   overclaiming, P5 stage creep and P5 indefinite-extension risk.
7. `docs/09_governance/09_STAGE_TASK_CONTRACT.md` clearly preserves the P5
   versus P6-P12 boundary.
8. Current P5 validation tests pass.
9. No P5 blocker remains unresolved.
10. No unclassified required P5 item remains.
11. Deferred items have a reason, earliest possible later stage/condition and
    guardrail.
12. Non-evidence warnings are clear and consistent.
13. Promotion guardrails are clear and unchanged.
14. No P5 synthetic/local evidence is described as model-strength, Tenhou,
    stable-dan ranked-game, LuckyJ, candidate-promotion or P6-P12 evidence.
15. A final human review confirms that P5 is ready to close.

## Exit Readiness Checklist

| checklist_item | status | evidence | blocker | required_before_closure | notes |
|---|---|---|---|---:|---|
| docs consistency | ready | `00_HANDOFF`, `00_DOCS_INDEX`, `05H`-`05T`, `10_NEXT` | none | yes | current docs consistently frame outputs as P5 synthetic/local diagnostics |
| source/test consistency | ready | current eval tests and source context | none | yes | source/tests match documented synthetic/local scope |
| fixture scope consistency | ready | stable-dan, legal-action and tiny benchmark fixtures | none | yes | fixtures are project-authored synthetic/local only |
| metric registry consistency | ready | `05S`, `offline_result.py`, `test_offline_result.py` | none | yes | current names/units/directions/statuses are consistent |
| offline envelope consistency | ready | `05J`, `05R`, envelope tests | none | yes | envelope can represent current synthetic diagnostics |
| evidence taxonomy consistency | ready | `05T` | none | yes | evidence labels and non-evidence warnings are consistent |
| promotion guardrail consistency | ready | `05F`, `05T` | none | yes | no P5 diagnostic is promotion/ranking evidence |
| governance tracking consistency | ready | changelog, evidence log, risk register, backlog, stage contract | none | yes | tracking docs are synchronized |
| `10_NEXT` hygiene | ready | current `10_NEXT` | none | yes | one active task is defined |
| risk / evidence log hygiene | ready | `09_EVIDENCE_LOG`, `09_RISK_REGISTER` | none | yes | overclaiming and indefinite-P5 risks are tracked |
| test validation | ready | required unittest commands | none | yes | must be rerun in the closure review gate |
| no unplanned production code | ready | git history and current task scope | none | yes | this task added docs only |
| no stage creep | ready | stage contract and `10_NEXT` limits | none | yes | P6-P12 remain forbidden |
| final human review | not ready | not yet performed | requires next review gate | yes | P5 cannot close until a dedicated closure review confirms readiness |
| P6 first-task definition | not applicable | P5 remains open | none | no | should be defined only after P5 closure review allows transition planning |

## Required Remaining P5 Items

The remaining required P5 items should stay small and review/finalization
oriented:

1. Review P5 evaluation groundwork closure criteria and exit readiness
   checklist.
2. If the review finds no blocker, prepare a final P5 handoff/evidence index
   finalization task.
3. Run a final P5 closure review gate after handoff/evidence finalization.

No current implementation blocker requires production code, tests, fixtures,
metric implementation, registry code changes, CLI, latency measurement,
model-output integration or real-data work before this closure checklist can be
reviewed.

## Deferred Items

| deferred_item | defer_reason | earliest_stage_or_condition | why_not_required_for_current_p5_closure | guardrail |
|---|---|---|---|---|
| production evaluator expansion | current P5 is synthetic/local groundwork | later approved evaluation implementation stage | P5 only needs closure of current synthetic/local foundation | do not add broad evaluator in P5 closure tasks |
| broad evaluator | requires rule/action coverage beyond current scope | later approved spec and implementation task | current legal-action evaluator is deliberately fixture-only | no broad ingestion or model-output path |
| real Tenhou ingestion | compliance/data rights/platform risk | explicit later compliance/data-system approval | P5 uses no real Tenhou data | no Tenhou accounts, sessions or platform data |
| real haifu ingestion | data rights and parser scope not defined | later data/replay schema stage | not needed for synthetic/local closure | no real haifu reader in P5 closure |
| external logs | data provenance and rights unclear | later audited dataset task | current fixtures are project-authored | no external-log ingestion |
| platform data | compliance and privacy risk | later compliance-cleared stage | not needed for P5 synthetic/local diagnostics | all safety flags remain false |
| model-output integration | would broaden evaluator and evidence claims | later adapter/evaluation stage after P5 closure | current diagnostics do not evaluate real model output | no model API or adapter path |
| CLI | would create user-facing ingestion/execution surface | later approved tooling task | current APIs/tests are enough for P5 closure | no CLI in closure tasks |
| broad file ingestion | scope/data provenance risk | later approved ingestion spec | fixed fixtures are sufficient for P5 | no arbitrary path scanning |
| latency measurement | timing method and target not approved | later latency diagnostic task | current envelope uses `latency_ms = None` | no timing APIs in closure tasks |
| fixed-position exact-match computation | evaluator/schema not implemented | later fixed-position schema/evaluator task | current fixture only plans future metric names | no exact-match calculation |
| legal-action checker / rule engine | broad mahjong rules implementation | later evaluator/rules stage | synthetic strict `dahai` evaluator suffices for P5 | no rule engine in P5 closure |
| canonicalizer implementation | action normalization scope not approved | later canonicalizer implementation task | schema/boundary is enough for P5 | no reach/call/kan expansion |
| model league | belongs to later league stages | after P5 closure and later stage approval | P5 diagnostics are not league evidence | no league/runner behavior |
| training / tuning | belongs to later model stages | after evaluation foundation and data/model stages | P5 is evaluation groundwork only | no training commands |
| self-play | belongs to later RL/league stages | after appropriate stages and gate approval | P5 has no self-play requirement | no self-play |
| candidate promotion | requires later real evaluation evidence | only after future funnel gates | P5 synthetic/local diagnostics cannot promote | no promotion claims |
| LuckyJ `10.68` validation | requires valid ranked-game evidence and final protocol | F7-style validation after prior gates | P5 only defines guardrails | no LuckyJ comparison claims |
| P6 data system work | separate stage scope | after P5 closure review and P6 task definition | P5 closure does not require P6 implementation | no P6 execution from this task |
| P7-P12 work | later model/evaluation/validation stages | after explicit stage transition | not needed for P5 closure | no stage jump |

## Non-Entry Conditions For P6-P12

Do not enter P6-P12 if any of the following are true:

- P5 closure checklist has not been reviewed.
- Any closure blocker remains unresolved.
- Required tests are failing.
- `docs/00_HANDOFF.md` and `docs/10_next/10_NEXT.md` disagree.
- evidence log entries are incomplete or overclaim synthetic/local evidence.
- risk register does not cover synthetic evidence overclaiming or stage creep.
- synthetic/local evidence is described as model-strength, Tenhou, stable-dan
  ranked-game, LuckyJ or candidate-promotion evidence.
- required P5 items and deferred items are mixed together.
- final human review has not approved P5 closure.
- P6 has no independent scope, entry criteria and first task.
- any task proposes training, tuning, self-play, league, runner, real Tenhou,
  real haifu, external logs, platform data, model-output integration, CLI,
  broad file ingestion, latency measurement, fixed-position exact-match,
  metric implementation or registry-code change without a later-stage approval.

## Closure Readiness Assessment

```text
P5 closure criteria are defined, but P5 remains open until reviewed.
```

Current interpretation:

- P5 is not closed.
- P5 is near closure.
- P5 should not enter P6-P12.
- At least one closure review gate is still required.

## Review Status

The closure criteria and exit readiness checklist were reviewed in:

```text
docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md
```

Review result:

```text
closure criteria review can close, but P5 remains open pending final P5
handoff/evidence index finalization and final closure review.
```

The review found no closure-criteria blocker and did not approve P5 closure or
P6-P12 entry.

## Next P5-Only Task Recommendation

The next narrow task should be:

```text
Finalize P5 handoff and evidence index before final closure review.
```

That task should remain docs-only finalization. It should not close P5 or enter
P6-P12. It should synchronize final P5 handoff and evidence-index materials
for a later final closure review gate. It must not add code, tests, fixtures,
metrics, registry changes, CLI, latency measurement, fixed-position exact-match,
model-output integration, real-data ingestion, training, self-play, league or
runner behavior.

## Evidence Grade

Current evidence grade:

```text
P5 evaluation groundwork closure criteria and exit readiness specification evidence only.
```

## Explicit Non-Evidence

This document is not:

- P5 closure itself.
- P6-P12 entry approval.
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
