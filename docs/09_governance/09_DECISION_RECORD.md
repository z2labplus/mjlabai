# 09_DECISION_RECORD

## Purpose

This file records project-level technical and governance decisions.

Each decision should include:

- Date.
- Decision.
- Context.
- Rationale.
- Consequences.
- Linked docs.
- Status.

## 2026-06-08 — DR-0051 — Define P7 Scope And Entry Criteria Before Implementation

Decision:

```text
P7 scope, entry criteria and first task are defined for review before
implementation. The next task is a docs-only review gate.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Full P6 is closed only for the documented P6 data-system scope recorded in
  `02AA`.
- `12D` completed the post-full-P6 transition review and allowed only a
  docs-only P7 scope / entry criteria / first-task definition task.
- P7 implementation and P7 first-task execution remained unapproved before
  this decision.
- P8-P12 entry remained unapproved before this decision.

Rationale:

- P7 supervised learning cannot safely start before independent scope, entry
  criteria, source/data readiness, feature/label readiness, risk review and
  evidence requirements are documented.
- Defining P7 scope is necessary to avoid both indefinite P6 churn and
  premature supervised-learning implementation.
- A docs-only review gate should confirm the P7 scope before any later
  implementation prompt is considered.

Consequences:

- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
  records P7 purpose, allowed docs-only scope, forbidden scope, entry
  criteria, exit criteria draft, required inputs, risk review requirements,
  evidence requirements, P8-P12 non-entry boundary and the first task
  candidate.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P7 scope, entry criteria and first task before implementation.`
- P7 implementation is not approved.
- P7 first-task execution is not approved.
- P8-P12 entry is not approved.
- Parser, dataset reader, ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.
- This decision is not model-strength evidence, Tenhou ranked evidence,
  stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
  candidate-promotion evidence.

Linked docs:

- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted planning decision recorded.
```

## 2026-06-07 — DR-0050 — Post-Full-P6 Transition Review

Decision:

```text
Define P7 scope, entry criteria and first task as the next docs-only task
before implementation.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Full P6 is closed only for the documented P6 data-system scope recorded in
  `02AA`.
- P7-P12 entry remained unapproved before this transition review.
- P7 implementation and P7 first-task execution remained unapproved before
  this transition review.

Rationale:

- Full P6 closure is complete for the documented data-system scope.
- P7 supervised learning cannot be implemented safely until independent scope,
  entry criteria, source/data readiness, feature/label readiness, risk review
  and first-task boundaries are documented.
- A docs-only P7 scope definition can be prepared without executing P7.
- Continuing P6 maintenance would risk unnecessary stage churn after full P6
  closure.

Consequences:

- `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md` records the
  transition review.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P7 scope, entry criteria and first task before implementation.`
- P7 implementation is not approved.
- P7 first-task execution is not approved.
- P8-P12 entry is not approved.
- Parser, dataset reader, ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.
- This decision is not model-strength evidence, Tenhou ranked evidence,
  stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
  candidate-promotion evidence.

Linked docs:

- `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted transition decision recorded.
```

## 2026-06-07 — DR-0049 — Final Full P6 Closure Review

Decision:

```text
Full P6 can close for the documented P6 data-system scope, and the next task
is a docs-only post-full-P6 transition review before defining any P7 task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- `02W` defined C1-C27 full-P6 closure criteria.
- `02X` reviewed those criteria with no blocker.
- `02Y` finalized the full-P6 handoff and evidence index.
- `02Z` found no risk/source-rights blocker for final full P6 closure review.
- P7-P12 entry remained unapproved before this decision.

Rationale:

- The full P6 review chain from `02A` through `02Z` is complete.
- C1-C27 pass in the final closure review.
- The accepted implementation remains limited to the exact synthetic/local
  minimal replay schema and project-authored fixture smoke artifacts.
- Deferred, blocked and later-stage items remain classified and are not
  silently approved.
- Real Tenhou, real haifu, external logs, platform data, source-specific
  real-data approval, parser, reader, ingestion, feature extraction, label
  generation, CLI, model-output integration, training, self-play and league
  remain unapproved.
- Required validation commands pass.
- Governance documents are synchronized.

Consequences:

- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md` records the final
  full P6 closure review.
- Full P6 is closed only for the documented P6 data-system scope:
  docs/governance/source-rights planning, accepted synthetic/local minimal
  replay schema and project-authored synthetic fixture smoke implementation,
  and deferred/blocked/later-stage inventory.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Run post-full-P6 transition review before defining any P7 task.`
- P7-P12 entry is not approved.
- P7 first task is not approved.
- No implementation, source approval, real-data approval, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI,
  model-output integration, training, self-play, league or P7-P12 work is
  approved.
- This decision is not model-strength evidence, Tenhou ranked evidence,
  stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
  candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- `docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
- `docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
- `docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted closure decision recorded.
```

## 2026-06-07 — DR-0048 — Review Full P6 Risk And Source-Rights Consistency

Decision:

```text
Close the full P6 risk-register and source-rights inventory consistency review
with no blocker, and select a docs-only final full P6 closure review gate as
the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- `02Y` finalized the full P6 handoff and evidence index after `02X`.
- The remaining required item before final full P6 closure review was
  risk-register and source-rights inventory consistency review.

Rationale:

- `02A` and `02D` continue to keep project-authored synthetic/local fixtures
  separate from unapproved real Tenhou, real haifu, external-log, platform,
  account, model-output and third-party artifact sources.
- `09_RISK_REGISTER.md` covers overclaim, stage drift, implementation drift,
  source-rights ambiguity, platform/account and third-party artifact risks.
- `02U`-`02Y` consistently classify parser, dataset reader, ingestion, feature
  extraction, label generation, CLI, model-output integration, real data,
  training, self-play, league and P7-P12 as deferred, blocked, later-stage or
  out of scope.
- No risk/source-rights blocker was found for the final full P6 closure
  review gate.

Consequences:

- `docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
  records the review.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Run final full P6 closure review gate.`
- Full P6 remains open until that later final closure review explicitly
  passes.
- P7-P12 entry remains unapproved.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval, source
  approval, data-ingestion approval, model-strength evidence, Tenhou ranked
  evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
  candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
- `docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted review recorded.
```

## 2026-06-07 — DR-0047 — Finalize Full P6 Handoff and Evidence Index

Decision:

```text
Finalize the full P6 handoff and evidence index after closure criteria review,
and select a docs-only risk register and source-rights inventory consistency
review as the next task before final full P6 closure review.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- `02W` defines full P6 closure criteria, and `02X` reviews those criteria
  with no blocker.
- Parser, dataset reader, data ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

Rationale:

- Full P6 closure criteria require a finalization-ready handoff and evidence
  index before risk/source-rights consistency review and final closure review.
- The evidence index must distinguish accepted current-scope evidence from
  roadmap / criteria / review / finalization evidence.
- Real-data, source-rights, parser, reader, ingestion, feature and label
  categories must remain blocked/deferred unless a later explicit task changes
  their status.
- P7-P12 entry must wait for full P6 closure and a separate transition review.

Consequences:

- `docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
  records the finalization.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review full P6 risk register and source-rights inventory consistency before final closure review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval,
  model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
- `docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted finalization recorded.
```

## 2026-06-07 — DR-0046 — Review Full P6 Closure Criteria

Decision:

```text
Close the full P6 closure criteria review with no blocker, and select a
docs-only full P6 handoff and evidence index finalization task as the next
task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- `02W` defines full P6 closure criteria after the roadmap and remaining scope
  review.
- Parser, dataset reader, data ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

Rationale:

- `02W` scope is correct.
- Full P6 closure scope is reasonable.
- C1-C27 criteria are sufficient, conservative and auditable.
- Exit readiness checklist is auditable.
- Required remaining items are docs/review/closure-only.
- Deferred, blocked, later-stage and out-of-scope classifications are safe.
- P7-P12 non-entry conditions are sufficient.
- No blocker was found.

Consequences:

- `docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
  records the review.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Finalize full P6 handoff and evidence index after closure criteria review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval,
  model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted review recorded.
```

## 2026-06-07 — DR-0044 — Review Full P6 Closure Roadmap and Remaining Scope Inventory

Decision:

```text
Close the full P6 closure roadmap and remaining scope inventory review with no
blocker, and select a docs-only full P6 closure criteria definition as the next
task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- `02U` defines the full P6 closure roadmap and remaining scope inventory.
- Parser, dataset reader, data ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

Rationale:

- `02U` scope is correct.
- The current-scope closed chain is complete.
- The remaining inventory classification is conservative and auditable.
- The roadmap requires docs-only closure criteria, criteria review, handoff /
  evidence finalization, risk / source-rights consistency review and a final
  full P6 closure review gate.
- No blocker was found.

Consequences:

- `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
  records the review.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define full P6 closure criteria after roadmap and remaining scope review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval,
  model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
- `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted review recorded.
```

## 2026-06-07 — DR-0045 — Define Full P6 Closure Criteria

Decision:

```text
Define full P6 closure criteria after the roadmap and remaining scope review,
and select a docs-only criteria review gate as the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- `02U` defines the full P6 closure roadmap and remaining scope inventory.
- `02V` reviews that roadmap / inventory with no blocker.
- Parser, dataset reader, data ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

Rationale:

- Full P6 closure needs explicit, auditable criteria before any final closure
  gate.
- Required closure items should remain docs/review/finalization items, not
  parser, reader, ingestion, feature, label or real-data implementation.
- Deferred, blocked, later-stage and out-of-scope classifications prevent
  implicit approval.
- P7-P12 entry must wait for full P6 closure and a separate transition review.

Consequences:

- `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
  records full-P6 closure scope, C1-C27 criteria, exit readiness, required
  remaining closure items, deferred / blocked / later-stage / out-of-scope
  classifications and P7-P12 non-entry conditions.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review full P6 closure criteria after roadmap and remaining scope review.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval,
  model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
- `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted criteria definition recorded.
```

## 2026-06-07 — DR-0043 — Define Full P6 Closure Roadmap and Remaining Scope Inventory

Decision:

```text
Define the full P6 closure roadmap and remaining scope inventory after
accepted current-scope closure, and select a docs-only review gate as the next
step.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- `12C` completed the post-current-scope P6 transition review and selected a
  full P6 closure roadmap / remaining-scope inventory task.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- Parser, dataset reader, data ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

Rationale:

- Current-scope P6 closure is narrower than full P6 closure.
- A roadmap / inventory is needed to prevent P6 from extending indefinitely
  through more small planning tasks.
- The inventory must distinguish required closure items from deferred, blocked,
  later-stage and explicitly out-of-scope work.
- A separate review gate is required before converting the roadmap into full
  P6 closure criteria.

Consequences:

- `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
  records the roadmap / inventory.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review full P6 closure roadmap and remaining scope inventory after
  current-scope closure.`
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval,
  model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

Linked docs:

- `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
- `docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
- `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted roadmap / inventory recorded.
```

## 2026-06-07 — DR-0042 — Complete Post-Current-Scope P6 Transition Review

Decision:

```text
Complete the post-current-scope P6 transition review and select a docs-only
full P6 closure roadmap / remaining-scope inventory task as the next step.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored fixture scope.
- Full P6 remains open.
- P7-P12 entry remains unapproved.
- Parser, dataset reader, data ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

Rationale:

- Current-scope P6 closure is narrower than full P6 closure.
- Direct P7 readiness or P7 task definition would be premature without full P6
  closure criteria, source-specific data readiness, feature / label readiness
  and risk review.
- A full P6 closure roadmap / remaining inventory reduces the risk of P6
  continuing indefinitely while also preventing stage creep into P7.

Consequences:

- `docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
  records the transition review.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define full P6 closure roadmap and remaining scope inventory after
  current-scope closure.`
- The next task is docs-only.
- No implementation, parser, dataset reader, ingestion, feature extraction,
  label generation, real data, model-output integration, CLI, training,
  self-play, league or P7-P12 work is approved.
- This decision is not full P6 closure, P7-P12 entry approval,
  model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

Linked docs:

- `docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
- `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted transition review recorded.
```

## 2026-06-07 — DR-0041 — Close Accepted Current-Scope P6 Data-System Scope

Decision:

```text
Current-scope P6 data system can close for the accepted synthetic/local
minimal replay schema and project-authored synthetic fixture scope.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 scope, entry criteria and first task were defined in `02C`.
- P6 source inventory and replay / fixture / readiness / proposal boundaries
  were defined and reviewed with no blocker.
- `02N` approved only the exact minimal implementation task.
- The exact implementation was completed only in:
  - `src/mjlabai/data/replay_schema.py`
  - `tests/fixtures/data/synthetic_replay_smoke.json`
  - `tests/data/test_replay_schema.py`
  - `tests/data/test_synthetic_replay_fixture_schema.py`
- `02O` reviewed that exact implementation with no blocker.
- `02P` accepted that exact implementation as current-scope complete.
- `02R` defined closure criteria.
- `02S` reviewed the closure criteria with no blocker.
- `02T` runs the final current-scope closure review gate.

Rationale:

- The current-scope P6 review chain is complete.
- Closure criteria pass.
- Required validation commands pass.
- Governance documents are synchronized.
- No unresolved blocker remains.
- Deferred items are explicitly not required for the accepted current-scope
  closure.
- P7-P12 non-entry conditions remain clear.

Consequences:

- Current-scope P6 closes only for the accepted synthetic/local minimal replay
  schema and project-authored synthetic fixture scope.
- Full P6 is not closed.
- P7-P12 entry is not approved.
- Parser, dataset reader, data ingestion, feature extraction, label
  generation, real data, model-output integration, CLI, training, self-play
  and league remain unapproved.
- The next task is a docs-only post-current-scope P6 transition review before
  defining any next-stage data-system or P7 task.
- This decision is not model-strength evidence, Tenhou ranked evidence,
  stable-dan ranked-game evidence, LuckyJ `10.68` comparison or candidate
  promotion evidence.

Linked docs:

- `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
- `docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`
- `docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
- `docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted current-scope closure recorded.
```

## 2026-06-07 — DR-0040 — Approve Next Minimal P6 Replay Schema And Synthetic Fixture Implementation Task

Decision:

```text
Approve only the next exact minimal P6 replay schema and project-authored
synthetic fixture implementation task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning.
- The P6 data-source provenance and rights inventory is defined and reviewed
  with no blocker.
- The P6 replay schema documentation boundary is defined and reviewed with no
  blocker.
- The P6 synthetic/local replay fixture boundary is defined and reviewed with
  no blocker.
- The P6 replay schema and fixture implementation readiness checklist is
  defined and reviewed with no blocker.
- The P6 replay schema and synthetic fixture implementation proposal boundary
  is defined and reviewed with no blocker.
- The P6 minimal replay schema and synthetic fixture implementation proposal
  is prepared in `02L` and reviewed in `02M` with no blocker.

Rationale:

- All approval criteria in `02N` pass.
- The proposed implementation is narrow enough to create the first tiny P6
  data-system smoke artifact without introducing real sources, ingestion,
  parser / reader work, feature extraction, label generation, model output or
  later-stage execution.
- Approving only the next exact implementation task prevents continued
  docs-only drift while still keeping P7-P12 and real-data work closed.

Consequences:

- `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
  records the approval decision.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Implement minimal P6 replay schema and project-authored synthetic fixture only.`
- The only approved implementation files are:
  - `src/mjlabai/data/replay_schema.py`
  - `tests/fixtures/data/synthetic_replay_smoke.json`
  - `tests/data/test_replay_schema.py`
  - `tests/data/test_synthetic_replay_fixture_schema.py`
- Directly related docs/governance synchronization is allowed.
- Real Tenhou, real haifu, external logs, platform data, parser, dataset
  reader, ingestion, feature extraction, label generation, CLI, model-output
  integration, training, self-play, league and P7-P12 remain unapproved.
- The approval decision is not implementation execution evidence, not source
  approval, not ingestion evidence, not model-strength evidence and not LuckyJ
  comparison evidence.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
- `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
- `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-07 — DR-0039 — Close P6 Minimal Replay Schema and Synthetic Fixture Implementation Proposal Review

Decision:

```text
Close the P6 minimal replay schema and synthetic fixture implementation
proposal review with no blocker, keep all implementation classes closed, and
allow only a docs-only approval-decision gate as the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- The P6 synthetic/local replay fixture boundary has been defined and reviewed
  with no blocker.
- The P6 replay schema and fixture implementation readiness checklist has been
  defined and reviewed with no blocker.
- The P6 replay schema and synthetic fixture implementation proposal boundary
  has been defined and reviewed with no blocker.
- The P6 minimal replay schema and synthetic fixture implementation proposal
  is prepared in `02L`.

Rationale:

- `02L` is sufficiently bounded for a later approval-decision task.
- The review found no blocker in scope, candidate implementation classes,
  proposed file candidates, minimal schema / fixture / validation test
  candidate boundaries, allowed future minimal scope, forbidden expansion,
  rollback plan, stop conditions, human / Web ChatGPT approval requirements or
  P7-P12 non-entry.
- Keeping the next step as docs-only approval decision prevents premature
  replay schema code, fixture creation, tests, parser, dataset reader,
  ingestion, feature extraction, label generation or P7-P12 drift.

Consequences:

- `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
  records the review.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Replay fixture implementation remains closed.
- Tests remain closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- P7-P12 remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Prepare approval decision for minimal P6 replay schema and synthetic fixture implementation task.`
- The next task must remain docs-only and must not implement fixture files,
  tests, replay schema code, dataclasses, pydantic models, JSON schema,
  parsers, dataset readers, ingestion, feature extraction, label generation,
  CLI, model-output integration, real Tenhou, real haifu, external-log
  ingestion, platform-data ingestion, training, self-play, league, runner
  behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
- `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-07 — DR-0038 — Prepare P6 Minimal Replay Schema and Synthetic Fixture Implementation Proposal Before Code

Decision:

```text
Prepare the P6 minimal replay schema and synthetic fixture implementation
proposal for review before code, keep all implementation classes closed, and
allow only a docs-only proposal review as the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- The P6 synthetic/local replay fixture boundary has been defined and reviewed
  with no blocker.
- The P6 replay schema and fixture implementation readiness checklist has been
  defined and reviewed with no blocker.
- The P6 replay schema and synthetic fixture implementation proposal boundary
  has been defined and reviewed with no blocker.

Rationale:

- A minimal implementation proposal is needed before any code, fixture or test
  can be considered.
- The proposal names exact candidate future files and preserves scope,
  validation, evidence, risk, rollback, stop-condition and human approval
  boundaries.
- Keeping the next step as review-only prevents premature replay schema code,
  fixture creation, tests, parser, dataset reader, ingestion, feature
  extraction, label generation or P7-P12 drift.

Consequences:

- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
  records the proposal.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Replay fixture implementation remains closed.
- Tests remain closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- P7-P12 remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P6 minimal replay schema and synthetic fixture implementation proposal before code.`
- The next task must remain docs-only review and must not implement fixture
  files, tests, replay schema code, dataclasses, pydantic models, JSON schema,
  parsers, dataset readers, ingestion, feature extraction, label generation,
  CLI, model-output integration, real Tenhou, real haifu, external-log
  ingestion, platform-data ingestion, training, self-play, league, runner
  behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0037 — Close P6 Replay Schema and Synthetic Fixture Implementation Proposal Boundary Review

Decision:

```text
Close the P6 replay schema and synthetic fixture implementation proposal
boundary review with no blocker, keep all implementation classes closed, and
allow only docs-only minimal implementation proposal drafting as the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- The P6 synthetic/local replay fixture boundary has been defined and reviewed
  with no blocker.
- The P6 replay schema and fixture implementation readiness checklist has been
  defined and reviewed with no blocker.
- The P6 replay schema and synthetic fixture implementation proposal boundary
  is defined in `02J`.

Rationale:

- `02J` is sufficient as a proposal boundary before code.
- The review found no blocker in scope, proposal classes, required sections,
  allowed/forbidden boundaries, source/fixture constraints, future approval
  conditions, decision vocabulary, P7-P12 non-entry or governance
  synchronization.
- The next step can draft a minimal implementation proposal for later review,
  but cannot implement replay schema code, fixture files, tests or ingestion.

Consequences:

- `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
  records the review.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Replay fixture implementation remains closed.
- Tests remain closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- P7-P12 remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Prepare P6 minimal replay schema and synthetic fixture implementation proposal for review before code.`
- The next task must remain docs-only proposal drafting and must not implement
  fixture files, tests, replay schema code, dataclasses, pydantic models, JSON
  schema, parsers, dataset readers, ingestion, feature extraction, label
  generation, CLI, model-output integration, real Tenhou, real haifu,
  external-log ingestion, platform-data ingestion, training, self-play, league,
  runner behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0036 — Define P6 Replay Schema and Synthetic Fixture Implementation Proposal Boundary Before Code

Decision:

```text
Define the P6 replay schema and synthetic fixture implementation proposal
boundary before code, keep all implementation classes closed, and allow only a
docs-only proposal-boundary review as the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- The P6 synthetic/local replay fixture boundary has been defined and reviewed
  with no blocker.
- The P6 replay schema and fixture implementation readiness checklist has been
  defined and reviewed with no blocker.

Rationale:

- A future implementation proposal needs its own boundary before any code,
  fixture or test can be considered.
- The proposal boundary prevents a proposal from being mistaken for replay
  schema implementation, fixture creation, parser/reader work, ingestion,
  feature extraction, label generation or later-stage work.
- Keeping the next step as review-only prevents premature P6 implementation and
  P7-P12 drift.

Consequences:

- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
  records the boundary.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Replay fixture implementation remains closed.
- Tests remain closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P6 replay schema and synthetic fixture implementation proposal boundary before code.`
- The next task must remain docs-only and must not implement fixture files,
  tests, replay schema code, dataclasses, pydantic models, JSON schema,
  parsers, dataset readers, ingestion, feature extraction, label generation,
  CLI, model-output integration, real Tenhou, real haifu, external-log
  ingestion, platform-data ingestion, training, self-play, league, runner
  behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0035 — Close P6 Replay Schema and Fixture Implementation Readiness Checklist Review

Decision:

```text
Close the P6 replay schema and fixture implementation readiness checklist
review with no blocker, keep all P6 implementation classes closed, and allow
only a docs-only proposal-boundary definition as the next task.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- The P6 synthetic/local replay fixture boundary has been defined and reviewed
  with no blocker.
- The P6 replay schema and fixture implementation readiness checklist is
  defined in `02H`.

Rationale:

- The review found that `02H` has sufficient scope, candidate implementation
  class coverage, replay schema readiness criteria, synthetic/local fixture
  readiness criteria, deferred parser / reader / feature / label / ingestion
  readiness coverage, decision vocabulary, dependency map, P7-P12 non-entry
  boundary, risks and governance synchronization.
- Closing the review permits the project to define a proposal boundary, but it
  does not permit implementation.
- Keeping the next step docs-only prevents premature replay schema code,
  fixture creation, ingestion, parser, dataset reader, feature extraction,
  label generation or P7-P12 drift.

Consequences:

- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
  records the review.
- Review can close.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Replay fixture implementation remains closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P6 replay schema and synthetic fixture implementation proposal boundary before code.`
- The next task must remain docs-only and must not implement fixture files,
  replay schema code, dataclasses, pydantic models, JSON schema, parsers,
  dataset readers, ingestion, feature extraction, label generation, CLI,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, training, self-play, league, runner behavior or
  P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0034 — Define P6 Replay Schema and Fixture Implementation Readiness Checklist Before Code

Decision:

```text
Define the P6 replay schema and fixture implementation readiness checklist
before code, keep all implementation classes closed, and require a docs-only
review gate before any replay schema or fixture implementation can be proposed.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- The P6 synthetic/local replay fixture boundary has been defined and reviewed
  with no blocker.
- P6 implementation, replay schema implementation, fixture implementation and
  data ingestion remain closed.

Rationale:

- A readiness checklist is needed before any future task can safely propose
  replay schema code, fixture files, validation tests, parsers, dataset readers,
  feature extraction, label generation or data ingestion.
- The checklist separates `ready_for_review_only` from
  `ready_for_implementation` so planning progress is not mistaken for code
  approval.
- Keeping the next step as a review gate prevents premature P6 implementation,
  source-approval bypass and P7-P12 drift.

Consequences:

- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
  records the checklist.
- No candidate implementation class is approved by this decision.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Replay fixture implementation remains closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P6 replay schema and fixture implementation readiness checklist before code.`
- The next task must remain docs-only and must not implement fixture files,
  replay schema code, dataclasses, pydantic models, JSON schema, parsers,
  dataset readers, ingestion, feature extraction, label generation, CLI,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, training, self-play, league, runner behavior or
  P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0033 — Close P6 Synthetic/Local Replay Fixture Boundary Review

Decision:

```text
Close the P6 synthetic/local replay fixture boundary review with no blocker,
keep fixture implementation and replay schema implementation closed, and
require a docs-only readiness-checklist task before any code or fixture work.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
  defines the synthetic/local replay fixture boundary before schema
  implementation.

Rationale:

- A review gate is required before any fixture file, replay schema code,
  parser, dataset reader, ingestion, feature extraction or label generation
  work can be considered.
- The review found that `02F` has sufficient scope, allowed/forbidden boundary,
  source dependency, replay-schema dependency, shape-family, entry-criteria,
  validation and risk coverage.
- Keeping the next step docs-only prevents premature P6 implementation and
  P7-P12 drift.

Consequences:

- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
  records the review.
- Review can close.
- Fixture implementation remains closed.
- Replay schema implementation remains closed.
- P6 implementation remains closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P6 replay schema and fixture implementation readiness checklist before code.`
- The next task must remain docs-only and must not implement fixture files,
  replay schema code, dataclasses, pydantic models, JSON schema, parsers,
  dataset readers, ingestion, feature extraction, label generation, CLI,
  model-output integration, real Tenhou, real haifu, external-log ingestion,
  platform-data ingestion, training, self-play, league, runner behavior or
  P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0032 — Define P6 Synthetic/Local Replay Fixture Boundary Before Schema Implementation

Decision:

```text
Define the P6 synthetic/local replay fixture boundary before schema
implementation, keep fixture implementation unapproved, and require a docs-only
review gate before any fixture file or schema implementation.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The P6 replay schema documentation boundary has been defined and reviewed
  with no blocker.
- Replay schema implementation remains closed.

Rationale:

- A future replay fixture needs a source/provenance, privacy, storage and
  non-evidence boundary before any fixture file can be created.
- Defining the boundary first reduces the risk of accidental real-data
  inclusion, account identifiers, model outputs, labels/features, broad
  ingestion or parser work.
- Keeping this task docs-only prevents premature P6 implementation or P7-P12
  drift.

Consequences:

- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
  records the boundary.
- Fixture implementation remains closed.
- Replay schema implementation remains closed.
- P6 implementation remains closed.
- Data ingestion, dataset readers, parsers, feature extraction and label
  generation remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P6 synthetic/local replay fixture boundary before schema implementation.`
- The next task must remain docs-only and must not implement fixture files,
  replay schema code, parsers, dataset readers, ingestion, feature extraction,
  label generation, CLI, model-output integration, real Tenhou, real haifu,
  external-log ingestion, platform-data ingestion, training, self-play, league,
  runner behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0031 — Close P6 Replay Schema Documentation Boundary Review

Decision:

```text
Close the P6 replay schema documentation boundary review with no blocker,
keep replay schema implementation closed, and require a docs-only synthetic/local
replay fixture boundary task before any schema implementation.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines replay schema allowed
  documentation scope, forbidden scope, source dependencies, field families,
  validation expectations, future implementation entry criteria and risks.

Rationale:

- The replay schema boundary needs a review gate before any implementation
  task can even be considered.
- The review found that `02B` is conservative enough to prevent premature
  schema code, ingestion, source approval, feature extraction, label generation
  or P7-P12 drift.
- A synthetic/local replay fixture boundary is the smallest safe next step
  before any fixture or schema implementation.

Consequences:

- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
  records the review.
- Review can close.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Data ingestion, dataset readers, feature extraction and label generation
  remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P6 synthetic/local replay fixture boundary before schema implementation.`
- The next task must remain docs-only and must not implement replay schema
  code, fixtures, data ingestion, dataset readers, feature extraction, label
  generation, CLI, model-output integration, real Tenhou, real haifu,
  external-log ingestion, platform-data ingestion, training, self-play, league,
  runner behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0030 — Define P6 Replay Schema Documentation Boundary Before Implementation

Decision:

```text
Define the P6 replay schema documentation boundary after source inventory
review, keep replay schema implementation unapproved, and require a docs-only
review gate before any schema code or ingestion work.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- The P6 data-source provenance and rights inventory has been defined and
  reviewed with no blocker.
- The project needed a replay schema boundary before any implementation could
  be safely considered.

Rationale:

- Future replay records must be traceable to approved sources, provenance,
  rights, storage policy and validation metadata.
- Replay schema field families should be defined before parser, reader,
  feature, label or training code exists.
- Defining documentation boundaries first reduces the risk of unsafe real-data
  ingestion, hidden-information leakage, private data exposure and stage creep
  into P7-P12.

Consequences:

- `docs/02_data_system/02B_REPLAY_SCHEMA.md` now records allowed documentation
  scope, forbidden scope, source-inventory dependencies, replay field families,
  validation expectations, future implementation entry criteria and risks.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Data ingestion, feature extraction and label generation remain closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P6 replay schema documentation boundary before implementation.`
- The next task must remain docs-only and must not implement replay schema
  code, data ingestion, dataset readers, feature extraction, label generation,
  CLI, model-output integration, real Tenhou, real haifu, external-log
  ingestion, platform-data ingestion, training, self-play, league, runner
  behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-06 — DR-0029 — Close P6 Source Inventory Review Before Replay Schema Boundary Definition

Decision:

```text
Close the P6 data-source provenance and rights inventory review with no
blocker, keep P6 implementation closed, and require a docs-only replay schema
documentation boundary task before any replay schema implementation.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- `docs/02_data_system/02A_DATA_SOURCES.md` defines the source inventory,
  approval vocabulary, source categories, pre-ingestion checklist, evidence
  requirements and rights/provenance risks.
- The project needed a review gate before moving toward replay schema
  definition.

Rationale:

- The source inventory is sufficient as a pre-ingestion boundary, but it is not
  source approval or replay schema implementation approval.
- Replay schema documentation should be defined only after confirming that
  source provenance and rights boundaries are conservative.
- P6 implementation, real data, external data, model-output paths, training and
  P7-P12 remain unsafe without later explicit approval.

Consequences:

- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
  records that the review can close with no blocker.
- P6 implementation remains closed.
- Replay schema implementation remains closed.
- Data ingestion remains closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P6 replay schema documentation boundary after source inventory
  review.`
- The next task must remain docs-only and must not implement replay schema
  code, data ingestion, dataset readers, feature extraction, label generation,
  CLI, model-output integration, real Tenhou, real haifu, external-log
  ingestion, platform-data ingestion, training, self-play, league, runner
  behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-05 — DR-0028 — Require Source Provenance And Rights Inventory Review Before Replay Schema Implementation

Decision:

```text
Define the P6 data-source provenance and rights inventory, then require a
docs-only review gate before any replay schema implementation or source
ingestion can be approved.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- P6 data-system scope and entry criteria are defined for planning only.
- Future replay, feature, label and quality pipelines need source provenance,
  rights, storage and evidence boundaries before implementation.

Rationale:

- Replay schema code should not consume any unapproved source.
- Real Tenhou, real haifu, external logs, platform data, accounts, third-party
  binaries, model weights, model outputs, self-play outputs and league outputs
  carry rights, privacy, provenance or stage-boundary risks.
- A source inventory plus review gate reduces the chance of unsafe ingestion,
  raw-data Git commits, platform-terms violations or synthetic-fixture
  overclaims.

Consequences:

- `docs/02_data_system/02A_DATA_SOURCES.md` now records the P6 inventory field
  schema, approval-status vocabulary, source-category inventory,
  required-before-ingestion checklist, future evidence requirements and
  rights/provenance risk review.
- P6 implementation remains closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Review P6 data-source provenance and rights inventory before replay schema
  implementation.`
- The next task must remain docs-only and must not implement replay schema
  code, data ingestion, feature extraction, label generation, CLI, model-output
  integration, real Tenhou, real haifu, external-log ingestion, platform-data
  ingestion, training, self-play, league, runner behavior or P7-P12.

Linked docs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-05 — DR-0027 — Define P6 Data-System Scope Before Implementation

Decision:

```text
Define P6 data-system scope, entry criteria, future exit criteria and first
next task as docs-only planning before any P6 implementation.
```

Context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- The post-P5 transition review allowed exactly one docs-only task to define
  P6 data-system scope, entry criteria and first task before implementation.
- Existing data-system docs are intentionally thin and need provenance, rights
  and compliance boundaries before implementation.

Rationale:

- Future replay, feature, label and data-quality work needs lawful, auditable
  sources before any ingestion or training path exists.
- Defining source/provenance and rights requirements first reduces the risk of
  unsafe real Tenhou, real haifu, external-log or platform-data usage.
- Keeping P6 scope definition docs-only prevents a jump into replay schema code,
  data pipelines, CLI, model-output integration, training, self-play, league or
  P7-P12.

Consequences:

- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
  records the P6 scope definition.
- P6 implementation remains closed.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P6 data-source provenance and rights inventory before replay schema
  implementation.`
- The next task must remain docs-only and must not implement replay schema
  code, data ingestion, real-data access, model-output paths, training or P7-P12.

Linked docs:

- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-06-04 — DR-0026 — Allow Docs-Only P6 Data-System Scope Definition After P5 Closure

Decision:

```text
After final P5 closure, allow exactly one docs-only next task to define P6
data-system scope, entry criteria and first task before implementation.
```

Context:

- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md` records that P5 can
  close for the current synthetic/local evaluation groundwork scope.
- P5 closure explicitly does not approve P6-P12 entry, P6 implementation or a
  P6 first task.
- The project needs to avoid both indefinite P5 extension and premature P6
  implementation.

Rationale:

- P6 is the data-system stage and needs independent scope, entry criteria, risk
  review and first-task definition before any implementation.
- A docs-only P6 definition task is the smallest safe next step after P5
  closure.
- Keeping replay schema code, data ingestion, real Tenhou, real haifu, external
  logs, platform data, model-output integration, CLI, training, self-play,
  league and P7-P12 forbidden prevents stage creep.

Consequences:

- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` records the
  post-P5 transition decision.
- The next task in `docs/10_next/10_NEXT.md` is:
  `Define P6 data-system scope, entry criteria and first task before
  implementation.`
- The next task must remain documentation-only and must not implement P6 data
  pipelines, replay schema code, ingestion, model-output paths or training.

Linked docs:

- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0024 — Define Synthetic Legal-Action Evaluator Boundary Before Implementation

Decision:

```text
Before implementing any P5 synthetic legal-action evaluator, define its allowed fixture-only scope, forbidden data/tooling scope, count/rate rules and offline result envelope mapping.
```

Context:

- Legal-action and invalid-action denominator rules are defined.
- Canonical `dahai` action fixture schema is defined.
- A synthetic legal-action fixture schema smoke test exists.
- The next step may implement a narrow evaluator, so the project needs explicit boundaries before code.

Rationale:

- Fixture labels such as `expected_future_outcome` must not be mistaken for evaluator output.
- Legal-action metrics are legality diagnostics only, not model-strength evidence.
- Keeping the first evaluator synthetic-only avoids accidental real Tenhou, external-log, platform-data, Akochan binary, model or league coupling.
- Count/rate invariants and zero-denominator behavior should be written before implementation.

Consequences:

- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md` now defines the synthetic evaluator boundary.
- Future implementation is limited to project-authored synthetic/local fixtures, current `dahai` scope and strict matching unless a later task changes the boundary.
- Future result envelopes must record P5 stage, legal-action metric type, fixture/reproducibility metadata, all-false safety flags and warnings against strength/LuckyJ claims.
- No evaluator, canonicalizer, legal-action checker, production code, CLI, file ingestion, league, runner, training, self-play or Tenhou integration was implemented in this task.

Linked docs:

- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`
- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0025 — Implement Synthetic Legal-Action Evaluator Only Inside Fixture Boundary

Decision:

```text
Implement the first P5 legal-action metric evaluator only for the project-authored synthetic fixture boundary, with strict dahai comparison and no broad evaluator, canonicalizer, file ingestion, CLI, model or Tenhou coupling.
```

Context:

- Legal-action metric denominators are defined.
- Canonical `dahai` fixture schema is defined.
- The synthetic evaluator boundary is documented.
- The project-authored fixture `tests/fixtures/eval/legal_action_metric_smoke.json` exists and has shape-only smoke coverage.

Rationale:

- The project needs one executable legality-diagnostic path before broader fixed-position evaluation work.
- The first implementation must prove the denominator, skipped/missing/parse categories and envelope mapping without reading real data or connecting to models/tools.
- `expected_future_outcome` must remain a test label, not an input to evaluator logic.

Consequences:

- `src/mjlabai/eval/legal_action_metric.py` implements `evaluate_synthetic_legal_action_fixture(...)`, `LegalActionMetricResult` and `build_synthetic_legal_action_metric_envelope(...)`.
- The evaluator compares only strict `dahai` fields: actor, action type, tile and tsumogiri.
- The current fixture yields `legal=1`, `invalid=1`, `missing=1`, `parse_failure=0`, `skipped=1`, `evaluated=3`.
- No canonicalizer, broad evaluator, legal-action checker, CLI, file ingestion, league, runner, model code, training, self-play, Tenhou connection or external-data ingestion was added.

Linked docs:

- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0023 — Define Canonical Action Fixture Schema Before Smoke Tests

Decision:

```text
Define a documentation-only canonical action schema for P5 legal-action metric fixtures before adding fixture smoke tests or evaluator code.
```

Context:

- Legal-action and invalid-action metric denominators are defined.
- The next P5 task needs synthetic fixtures whose `proposed_action` and `legal_actions` can be compared structurally.
- Without a canonical action schema, fixture authors could encode actions inconsistently and make legality metrics unreliable.

Rationale:

- A shared canonical action object makes later fixture smoke tests auditable.
- Keeping the current minimum scope to `dahai` reduces ambiguity before calls, reach and kan edge cases are implemented.
- Strict matching as the default prevents relaxed behavior from silently changing legal-action rates.
- Preserving `raw_action` and `metadata` for audit while excluding them from equality keeps reproducibility without polluting matching.

Consequences:

- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md` defines canonical action fields, strict `dahai` matching, future relaxed matching, fixture shape, edge cases and envelope mapping.
- No canonicalizer, evaluator, legal-action checker, Python schema/dataclass, CLI, league, runner, training, self-play or Tenhou integration was implemented.
- The next P5-only task is to add a synthetic legal-action metric fixture schema smoke test.

Linked docs:

- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`
- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0022 — Define Legal-Action Metrics Before Evaluator Implementation

Decision:

```text
Define legal-action and invalid-action metric denominators, outcome categories and canonical matching principles before implementing any evaluator.
```

Context:

- The offline metric registry already contains `legal_action_rate` and `invalid_action_rate` as placeholders.
- The project now has a shared offline result envelope, but legal-action metrics still needed precise denominator and failure-category rules.
- Future fixed-position evaluation and wrapper validation require consistent legality reporting before any evaluator code is written.

Rationale:

- Legal-action rate is a basic validity metric, not a strength metric.
- Separating invalid actions from parse failures and missing actions prevents misleading denominator math.
- Defining skipped-record categories before implementation reduces the chance that future evaluators silently hide bad records.
- Canonical matching should be specified before fixtures and parser/canonicalizer tests are created.

Consequences:

- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md` defines decision records, legal/proposed actions, formula denominators, outcome categories, canonical matching principles and result-envelope mapping.
- No evaluator, legal-action checker, canonicalizer, CLI, league, runner, training, self-play or Tenhou integration was implemented.
- The next P5-only task is to define the action canonicalization schema for legal-action metric fixtures.

Linked docs:

- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0021 — Use a Shared Offline Evaluation Result Envelope for P5 Outputs

Decision:

```text
Define a shared P5 offline evaluation metric registry and result envelope schema.
Use the schema to record, not generate, offline evaluation outputs.
```

Context:

- Stable-dan reporting is implemented and documented.
- Akochan wrapper audit results and future fixed-position evaluations need compatible result packaging.
- P5 still lacks shared metric names, command status, reproducibility metadata, safety flags and evidence-reference fields.

Rationale:

- A shared envelope prevents each evaluator from inventing incompatible output fields.
- Metric definitions can exist before every metric calculator exists, as long as placeholder metrics are labeled clearly.
- The envelope must remain schema-only so it does not become a league harness, runner, CLI, training path or Tenhou connector.

Consequences:

- `src/mjlabai/eval/offline_result.py` defines the registry and envelope dataclasses.
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md` documents fields, guardrails and a synthetic example.
- The next P5-only task is an offline envelope smoke fixture for a synthetic stable-dan report.
- This is not model-strength evidence and not a LuckyJ comparison claim.

Linked docs:

- `src/mjlabai/eval/offline_result.py`
- `tests/eval/test_offline_result.py`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0020 — Stable-Dan Groundwork Current-Scope Complete, P5 Remains Open

Decision:

```text
Mark stable-dan evaluation groundwork complete for the current P5 scope.
Keep P5 overall open.
Set the next P5-only task to define the offline evaluation metric registry and result envelope schema.
```

Context:

- Stable-dan calculator, bootstrap CI, LuckyJ threshold helper, reporting guardrails, placement aggregation, synthetic smoke fixture and API documentation are all implemented or documented.
- The current stable-dan chain uses only synthetic/local offline placement inputs.
- The project still lacks a broader metric registry and shared result envelope for future P5 evaluation outputs.

Rationale:

- The stable-dan subtrack has enough current-scope infrastructure to stop adding local stable-dan pieces before defining how P5 results should be packaged consistently.
- P5 cannot close until other evaluation outputs, such as legal-action rate, invalid-action rate, latency, command status and reproducibility metadata, share a common reporting shape.
- The next task must remain P5-only and must not become league execution, training, self-play, real Tenhou integration or P6-P12 work.

Consequences:

- `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md` records the stable-dan current-scope completion verdict.
- `docs/10_next/10_NEXT.md` now points to `Define P5 offline evaluation metric registry and result envelope schema.`
- Stable-dan synthetic fixtures, reports and docs remain code-path / statistics infrastructure, not model-strength or LuckyJ proof.

Linked docs:

- `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md`
- `docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0019 — Stable-Dan API Examples Must Match Implemented Schema

Decision:

```text
Stable-dan evaluation API documentation must show only implemented parameters and report fields.
Caller metadata such as model_name, dataset_name and evaluation_context remains outside StableDanEvaluationReport until a future schema task adds it.
```

Context:

- Web-side drafts suggested including model/dataset/evaluation context metadata in the report builder call.
- The current implemented `build_stable_dan_evaluation_report(...)` signature accepts `bootstrap_result`, optional `threshold_comparison` and `schema_version`.
- Adding undocumented parameters to examples would create false expectations and break copy-paste usage.

Rationale:

- Documentation must be executable against the current code.
- Keeping metadata outside the report avoids unreviewed schema expansion during a docs-only task.
- Future schema changes should be explicit tasks with tests and governance updates.

Consequences:

- `docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md` uses the actual current API signature.
- The document explicitly notes that `model_name`, `dataset_name`, `evaluation_context` and arbitrary notes are not stored in `StableDanEvaluationReport` yet.
- The next task is to review P5 stable-dan evaluation groundwork completion and define the next P5-only evaluation task.

Linked docs:

- `docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md`
- `docs/00_DOCS_INDEX.md`
- `src/mjlabai/eval/stable_dan.py`
- `docs/10_next/10_NEXT.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0018 — Stable-Dan Smoke Fixtures Must Be Synthetic and CLI-Free

Decision:

```text
Stable-dan report smoke fixtures may validate API composition only from project-authored synthetic placement inputs.
They must not become CLI tools, league harnesses, external log readers, Tenhou ingestion paths or strength evidence.
```

Context:

- Placement aggregation, stable-dan calculator, bootstrap CI, threshold helper and report schema are implemented.
- The next validation need is an end-to-end code path smoke test from placement records to report serialization.
- The project must avoid implying that a synthetic fixture is a model, Tenhou or LuckyJ result.

Rationale:

- A smoke fixture catches API integration regressions without introducing platform, data-rights or training scope.
- Keeping the path CLI-free avoids prematurely creating ingestion/user-facing tooling.
- The synthetic-only boundary makes the test safe and auditable.

Consequences:

- `tests/fixtures/eval/stable_dan_placements_smoke.json` is synthetic-only and project-authored.
- `tests/eval/test_stable_dan_report_smoke.py` verifies aggregation, point estimate, bootstrap, threshold comparison, report schema and JSON serialization.
- The smoke fixture can support developer confidence in the evaluation code path but cannot support model-strength, Tenhou or LuckyJ claims.
- The next task is stable-dan evaluation API documentation with example usage from synthetic placements.

Linked docs:

- `tests/fixtures/eval/stable_dan_placements_smoke.json`
- `tests/eval/test_stable_dan_report_smoke.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0017 — Stable-Dan Placement Aggregation Accepts Only Explicit Placements

Decision:

```text
Stable-dan placement aggregation may accept only explicit 1/2/3/4 placements and a small whitelist of human-readable aliases.
It must reject zero-based, fuzzy, bool, float and unknown placement inputs instead of silently correcting them.
```

Context:

- Stable-dan calculator, bootstrap CI, threshold helper and report schema are implemented.
- Future evaluation inputs will often arrive as per-game placement records rather than precomputed counts.
- Accepting ambiguous placement labels could bias first/second/third/fourth counts and therefore stable-dan estimates.

Rationale:

- Stable-dan is highly sensitive to fourth-place counts, so silent coercion is risky.
- Explicit failure on bad records makes upstream evaluator bugs visible.
- Keeping aggregation offline and schema-limited prevents it from becoming a league harness or Tenhou ingestion path.

Consequences:

- `aggregate_placement_counts(...)` accepts `1`, `2`, `3`, `4` and whitelisted string aliases only.
- `aggregate_placement_records(...)` extracts a named placement field from mapping records and fails on missing keys.
- `StableDanPlacementCounts.to_stable_dan_kwargs()` can feed `calculate_stable_dan(...)`.
- The next task is a CLI-free stable-dan evaluation report smoke fixture from placement inputs.

Linked docs:

- `src/mjlabai/eval/placement_counts.py`
- `tests/eval/test_placement_counts.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0016 — Stable-Dan Reports Require Sample-Size Guardrails

Decision:

```text
Stable-dan reporting must separate statistical threshold outcome from project-level claim readiness.
Default sample-size guardrails are internal governance defaults, not Tenhou official standards or proof.
```

Context:

- Stable-dan point estimate, bootstrap CI and LuckyJ threshold helper are implemented.
- A `clear_pass` threshold outcome can still be based on too little data for project-level claims.
- Future reports need a standard schema so counts, CI, threshold outcome and sample-size status are always present.

Rationale:

- Separating `clears_threshold` from `can_enter_threshold_review` prevents overclaiming.
- Report schema makes future evaluation outputs easier to audit.
- Explicit notes keep the report framed as offline statistics, not Tenhou ranked proof.

Consequences:

- `assess_stable_dan_sample_size(...)` returns report and threshold-review readiness.
- `build_stable_dan_evaluation_report(...)` combines point estimate, bootstrap CI, threshold outcome and sample-size assessment.
- Default report minimum is `total_games >= 100` and `fourth_count >= 10`.
- Default threshold-review minimum is `total_games >= 1000` and `fourth_count >= 50`.
- Default maximum undefined rate is `0.05`.
- The next task is placement-count aggregation for stable-dan evaluation inputs.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0015 — Stable-Dan Threshold Pass Requires Bootstrap Lower Bound

Decision:

```text
Stable-dan threshold comparison defaults to LuckyJ stable dan 10.68.
A clear pass requires bootstrap lower_bound > threshold and acceptable undefined_rate.
Point estimate alone must never set clears_threshold=True.
```

Context:

- Stable-dan point estimate and bootstrap CI are implemented.
- The project target is stable dan above LuckyJ 10.68.
- Without a helper, callers may accidentally compare only the point estimate and overclaim strength.

Rationale:

- Lower-bound comparison is more conservative than point-estimate comparison.
- High undefined bootstrap rate means the interval is unreliable even if the lower bound looks strong.
- Encoding the outcomes in one helper makes future reports easier to audit.

Consequences:

- `compare_stable_dan_to_threshold(...)` returns `clear_pass`, `point_estimate_only`, `clear_fail`, `unreliable` or `inconclusive`.
- `bootstrap_and_compare_stable_dan_threshold(...)` combines bootstrap CI and threshold comparison.
- The next task is minimum sample-size and reporting schema for stable-dan evaluation results before using helper output for project-level LuckyJ claims.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0014 — Require Bootstrap Lower-Bound Logic Before LuckyJ Stable-Dan Claims

Decision:

```text
Implement stable-dan bootstrap confidence intervals as percentile empirical multinomial resampling.
Do not compare against LuckyJ 10.68 from point estimate alone; the next helper must use the bootstrap lower bound.
```

Context:

- The deterministic stable-dan calculator is implemented and tested.
- The project target is stable dan above LuckyJ 10.68, but point estimates alone can overstate strength.
- Bootstrap resamples can produce undefined stable dan when sampled fourth-place count is zero.

Rationale:

- Percentile empirical multinomial bootstrap is simple, dependency-free and tied directly to observed placement counts.
- Undefined resamples must be visible in the result because high undefined rate makes the CI unreliable.
- A threshold helper should encode the project rule that lower-bound evidence matters more than point-estimate optimism.

Consequences:

- `bootstrap_stable_dan_ci(...)` reports point estimate, CI bounds, confidence level, bootstrap count, successful resamples, undefined resamples and undefined rate.
- Undefined resamples are skipped and counted, never converted into infinite stable dan.
- If all resamples are undefined, `StableDanBootstrapUndefinedError` is raised.
- The next task is a LuckyJ 10.68 threshold comparison helper using the bootstrap lower bound.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0013 — Treat Stable Dan as Point Estimate Until Bootstrap CI Exists

Decision:

```text
Implement Tenhou room-specific stable-dan as a deterministic point estimate now.
Do not use it as statistically reliable strength evidence until bootstrap confidence intervals and sample-size reporting are added.
```

Context:

- The project has closed Akochan F2 fixed-sample wrapper validation and moved into P5 evaluation groundwork.
- The north-star target is stable dan above LuckyJ 10.68, so stable-dan calculation must become a first-class project metric before training or league work.
- The current task implements the room-specific official formula but explicitly excludes bootstrap CI.

Rationale:

- A deterministic point estimate is needed before uncertainty estimation.
- `fourth_count == 0` can make the formula undefined, so the calculator must refuse to fabricate infinite strength.
- The project must keep metric infrastructure separate from model-strength claims.

Consequences:

- `calculate_stable_dan(...)` supports general/ippan, upper/joukyu, expert/tokujou and phoenix/houou aliases.
- `StableDanResult` exposes counts, rates, formula weights and source note for auditability.
- `StableDanUndefinedError` is raised when `fourth_count == 0`.
- The next task is bootstrap confidence intervals for the stable-dan estimate.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0011 — Allow Only the Known Akochan mjai_log Status Line in Mixed Stdout

Decision:

```text
AkochanWrapper may parse mixed stdout only when the non-JSON line is exactly `calculating review`.
The wrapper must record skipped_non_json_lines, preserve raw_stdout and parsed_records, and reject unknown non-JSON lines or partial parses.
```

Context:

- GitHub Actions run `26628128871` showed strict JSON stream parsing improved the `mjai_log` failure diagnostics.
- The same run showed the real stdout shape: JSON event records, the non-JSON line `calculating review`, then JSON review output.
- The project needs real `mjai_log` compatibility evidence without silently accepting arbitrary mixed logs.

Rationale:

- The status line is a known Akochan progress/status message, not a JSON record.
- A single exact-string allowlist keeps the parser strict and auditable.
- Recording skipped lines and parse warnings keeps the stdout shape reviewable without uploading third-party artifacts.
- Unknown non-JSON output may indicate a runtime error or unmodeled behavior and must fail.

Consequences:

- `AkochanCommandResult` now includes `skipped_non_json_lines`.
- The parser supports single JSON, JSON Lines, concatenated JSON values, pretty-printed multi-record JSON streams and the single allowlisted mixed status line.
- Parse failures include bounded stdout summary, stdout SHA256, parsed-record count, skipped-status-line count and failure position.
- The next evidence step is rerunning the manual real-exe workflow; this decision is parser implementation evidence only, not strength evidence.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0012 — Close Akochan F2 Fixed-Sample Wrapper Validation and Move to Stable-Dan Metric Work

Decision:

```text
Treat Akochan as F1 Conditional Pass with F2 fixed-sample real-exe wrapper validation passed.
Do not treat this as strength evidence.
Set the next task to implement the Tenhou stable-dan calculator from room-specific formulas.
```

Context:

- GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` run `26629344590` succeeded.
- The run used mjlabai commit `29f5e1ed19407d169f85524e05438ac8938d2dc2`.
- Ubuntu runner built `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Fake wrapper tests passed 14 tests.
- Real external `system.exe legal_action` wrapper test passed.
- Real external `system.exe mjai_log` wrapper test passed.
- No third-party source, binary, `params/` or build artifact was stored or uploaded.

Rationale:

- F2 fixed-sample wrapper validation has enough evidence to close this narrow integration task.
- The project still lacks the evaluation metric foundation needed to compare future candidates in Tenhou terms.
- Stable dan is part of the north-star target and should be implemented before broader model comparison or strength claims.

Consequences:

- Akochan remains an interface/reviewer candidate, not a proved strength baseline.
- Broader Akochan evaluator/reviewer integration requires a separate task and license boundary review.
- `docs/10_next/10_NEXT.md` now points to the Tenhou stable-dan calculator task.
- No training, self-play, match, league, real Tenhou integration or platform automation is authorized by this decision.

Linked docs:

- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0008 — Validate Akochan F2 Wrapper Through Temporary GitHub Actions Real-Exe Workflow

Decision:

```text
Add a manual GitHub Actions workflow and default-skip unittest file to validate the Akochan F2 wrapper against a real Ubuntu-built external system.exe.
The workflow may build Akochan in the runner temp directory and set AKOCHAN_SYSTEM_EXE for tests, but must not upload or store third-party source, binaries, params or build artifacts.
```

Context:

- Akochan F1 is Conditional Pass from GitHub Actions run `26617347785`.
- The minimal Akochan F2 wrapper skeleton passes fake-executable smoke tests.
- Fake-executable tests prove wrapper behavior only; they do not prove compatibility with real `system.exe`.
- The project must keep Akochan source and binaries outside the repository because of license and governance constraints.

Rationale:

- A manual workflow gives a reproducible Ubuntu environment without requiring local Docker or macOS toolchain changes.
- Default-skip real-exe tests keep local unit tests reliable when no real external executable is available.
- Runner-temp build and no artifact upload preserve the no-vendor/no-binary boundary.

Consequences:

- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` is the controlled real-exe validation path.
- `tests/adapters/test_akochan_wrapper_real_exe.py` skips locally unless `AKOCHAN_SYSTEM_EXE` exists; the `mjai_log` test also requires `AKOCHAN_MJAI_LOG_SAMPLE`.
- The next task is to manually run the workflow and review its run ID/logs.
- Until that workflow succeeds and is reviewed, the project has no real `system.exe` wrapper compatibility evidence.
- This remains interface evidence only, not strength evidence.

Linked docs:

- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `src/mjlabai/adapters/akochan_wrapper.py`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0009 — Run External Akochan system.exe From an Audited Working Directory

Decision:

```text
AkochanWrapper must launch external system.exe with a controlled subprocess working directory.
The resolution priority is: explicit working_dir constructor argument, AKOCHAN_WORKING_DIR, then Path(system_exe).resolve().parent.
Each wrapper audit log must record the actual working_dir.
```

Context:

- GitHub Actions run `26621536548` built Akochan and passed fake wrapper tests plus real `legal_action`.
- The same run failed real `mjai_log` because `system.exe` attempted to load `setup_mjai.json` from the mjlabai checkout working directory.
- Akochan runtime files live beside the external executable in the temporary Akochan checkout/build directory.

Rationale:

- Defaulting cwd to the executable directory matches the temporary Ubuntu build layout and keeps runtime files visible.
- Supporting `AKOCHAN_WORKING_DIR` gives a reproducible override for symlinks or wrapper paths that differ from the real Akochan runtime root.
- Recording `working_dir` in audit logs makes the runtime boundary inspectable without storing third-party source or binaries.

Consequences:

- `src/mjlabai/adapters/akochan_wrapper.py` now validates and records `working_dir`.
- Fake tests cover default, explicit and environment-variable working-directory behavior.
- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` exports `AKOCHAN_WORKING_DIR=${AKOCHAN_DIR}` before real-exe tests.
- The next evidence step is rerunning the manual workflow; this decision alone is not real `mjai_log` compatibility evidence and not strength evidence.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`
- `tests/adapters/test_akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0010 — Parse Akochan stdout as a Strict JSON Stream

Decision:

```text
AkochanWrapper should parse stdout as either a single JSON value or a strict stream of JSON values.
It may support JSON Lines, concatenated JSON values and pretty-printed multi-record JSON streams, but it must not treat partial parsing as success.
```

Context:

- GitHub Actions run `26623247276` showed real `mjai_log` no longer fails on `setup_mjai.json`.
- The same run failed because real `mjai_log` stdout triggered `JSONDecodeError: Extra data`.
- The previous parser only handled a single JSON value and simple per-line JSON records.

Rationale:

- Akochan `mjai_log` can emit multiple JSON records in one stdout stream.
- Strict JSON stream parsing handles compact, line-delimited and pretty-printed records without allowing silent truncation.
- Bounded diagnostics make GitHub Actions failures reviewable without dumping large raw stdout.

Consequences:

- `AkochanCommandResult` now includes `parsed_records`.
- Successful calls preserve `raw_stdout`, `parsed_json`, `parsed_records` and `parse_warnings`.
- Parse failures include bounded stdout summary, stdout SHA256, failure position and parsed-record count.
- The next evidence step is rerunning the manual real-exe workflow; this decision is parser implementation evidence only, not strength evidence.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0007 — Implement Akochan F2 Skeleton as Fixed-Command Python Wrapper

Decision:

```text
Implement the first Akochan F2 skeleton as a minimal Python wrapper with only two fixed methods:
run_legal_action(input_json) and run_mjai_log(log_path, actor=0, mode=2).
Use fake-executable smoke tests first, then validate against a real external Ubuntu-built system.exe in a later task.
```

Context:

- Akochan F1 is Conditional Pass based on GitHub Actions run `26617347785`.
- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md` defines the no-vendor, no-training, no-Tenhou wrapper boundary.
- The repository previously had no Python package structure.
- F2 needs wrapper behavior, audit-log schema and fixed-sample smoke tests before any real external binary validation.

Rationale:

- A small Python wrapper fits the project's future evaluation tooling while keeping Akochan source and binaries outside the repository.
- Fixed methods avoid unrestricted command execution.
- Fake-executable tests prove wrapper parsing, normalization and audit logging without requiring real Akochan binaries or third-party artifacts.

Consequences:

- `pyproject.toml` and `src/mjlabai` define the initial minimal Python package.
- `AkochanWrapper` requires an explicit executable path or `AKOCHAN_SYSTEM_EXE`.
- The wrapper preserves raw stdout, parses JSON, normalizes mjai-style `dahai` actions and records the required audit-log fields.
- `tests/fixtures/akochan/fake_system_exe.py` is a test substitute only, not Akochan and not strength evidence.
- The next task must validate the wrapper against a real externally built `system.exe` without uploading or saving third-party binaries or artifacts.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper.py`
- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0001 — Technical Plan Becomes Execution Charter

Decision:

```text
The project moves from internal-paper-first planning to technical-plan-first execution.
The paper is treated as a future outcome summary, not the current execution driver.
```

Context:

- The project north-star remains Tenhou stable dan > LuckyJ 10.68.
- The current stage is P3 / baseline reproducibility audit.
- Mortal F1 is blocked by missing public trained model artifact and local environment prerequisites.
- The project needs one technical execution charter that coordinates web-side research decisions and local Codex implementation.

Rationale:

- A paper-first workflow can encourage premature narrative, overclaiming and stage skipping.
- A technical-plan-first workflow keeps the project grounded in reproducible baselines, unified evaluation, Tenhou-oriented metrics and documented decisions.
- Git + docs are the only durable way to make web-side research decisions actionable for local Codex execution.

Consequences:

- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` becomes the current technical execution charter.
- Web ChatGPT Pro is responsible for solution design, research, review and decision support.
- Local Codex App is responsible for code, tests and documentation landing.
- LuckyJ remains the target benchmark, not a direct full-reproduction object.
- Codex must continue to execute only the first unfinished task in `docs/10_next/10_NEXT.md`.
- Every real task must update changelog, evidence, risk, handoff and next.

Linked docs:

- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/00_HANDOFF.md`
- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0006 — Define Akochan F2 as Wrapper-Only Fixed-Sample Interface Task

Decision:

```text
Akochan F2 begins as a wrapper-only fixed-sample interface/legal-action task.
The next implementation may create a minimal wrapper skeleton, but must not vendor Akochan source or binaries, train, self-play, connect to Tenhou or exceed fixed legal_action/mjai_log samples.
```

Context:

- Akochan F1 is Conditional Pass based on GitHub Actions run `26617347785`.
- The project still has custom-license restrictions and local macOS build limitations.
- The next step needs a precise F2 boundary before any adapter code is written.

Rationale:

- The racing funnel allows increasing scope only after prior evidence, but F2 must remain narrower than evaluation or strength claims.
- A wrapper-only boundary preserves license hygiene and keeps third-party source/binaries outside this repository.
- Fixed `legal_action` and `mjai_log` samples are enough to prove interface viability without self-play, training or Tenhou integration.

Consequences:

- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md` is the controlling F2 task specification.
- Future F2 implementation must record audit logs with external repo/commit, command, hashes, elapsed time and explicit no-training/no-self-play/no-Tenhou flags.
- Future F2 implementation must preserve raw Akochan output and normalize only parseable JSON.
- License review or author permission remains required before modification, redistribution, commercial use, public release or treating Akochan as a mjlabai-owned component.

Linked docs:

- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0005 — Promote Akochan to F1 Conditional Pass on Ubuntu Evidence

Decision:

```text
Akochan F1 is promoted from Blocked to Conditional Pass based on successful Ubuntu GitHub Actions build and minimal non-training samples.
The next task is to define the Akochan F2 interface/legal-action adapter task, not to write adapter code yet.
```

Context:

- The first workflow run failed validation because job-level `env` used an unsupported `runner.temp` context.
- The workflow was corrected to configure temporary paths through `$GITHUB_ENV`.
- Corrected run `26617347785` succeeded on `ubuntu-latest`.
- The run generated `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Minimal `legal_action` and `mjai_log haifu_log_sample.json 0 2` samples both succeeded.
- The custom Akochan license remains restrictive for modification, redistribution, commercial use and public release.
- Local macOS build remains blocked.

Rationale:

- F1 requires reproducible build/minimal-run evidence, not model strength.
- The Ubuntu runner evidence is enough to stop treating Akochan as build-blocked.
- Remaining license and local-platform limitations mean this should be Conditional Pass rather than full unqualified Pass.

Consequences:

- `docs/10_next/10_NEXT.md` now points to defining the Akochan F2 interface/legal-action adapter task.
- F2 task definition must specify wrapper-only integration boundaries, state/action mapping, legal-action checker scope, decision log schema and license guardrails.
- Do not train, tune, self-play, connect to Tenhou or claim Akochan strength from this F1 result.
- Do not redistribute Akochan source/binaries or modify AI-part source without license review or permission.

Linked docs:

- `.github/workflows/akochan-f1-build-audit.yml`
- `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0004 — Use Manual GitHub Actions Ubuntu Runner for Akochan F1 Build Evidence

Decision:

```text
Add a manual GitHub Actions workflow to provide an Ubuntu Linux build environment for Akochan F1 build/minimal-run evidence.
```

Context:

- Local macOS ARM cannot currently build Akochan.
- Docker is not installed locally.
- Homebrew LLVM, Boost and OpenMP are not available through expected local paths.
- The project still needs a reproducible Linux build environment before Akochan can leave F1 Blocked.

Rationale:

- GitHub Actions `ubuntu-latest` gives a temporary Linux environment without polluting the local machine.
- A manual `workflow_dispatch` keeps execution explicit and avoids automatic repeated third-party builds.
- The workflow can install build dependencies inside the temporary runner, clone the fixed Akochan commit outside the repository, build, and run minimal non-training samples.

Consequences:

- `.github/workflows/akochan-f1-build-audit.yml` becomes the supported build-environment path for the next Akochan F1 evidence attempt.
- Akochan remains F1 Blocked until a workflow run succeeds and logs are reviewed.
- The workflow must not train, tune, self-play, connect to Tenhou, write adapters, enter F2, upload third-party source or publish binaries.

Linked docs:

- `.github/workflows/akochan-f1-build-audit.yml`
- `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0003 — Keep Akochan at F1 Blocked Until Build and Minimal JSON/Log Sample Pass

Decision:

```text
Akochan does not pass F1 yet.
Keep Akochan at F1 Blocked and do not define F2 adapter work until a supported build environment produces `system.exe` and a minimal `legal_action` and/or `mjai_log` sample succeeds.
```

Context:

- `critter-mj/akochan` is public and inspectable at commit `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Akochan has promising JSON, mjai, pipe, log review and legal-action entry points.
- No external neural-network weight artifact appears required; the repository includes required text parameters under `params/`.
- Local macOS ARM build failed with both the macOS and Linux Makefiles.
- No `system.exe` was produced, so no minimal run could be executed.
- The custom license allows private research audit, but redistribution, AI-part modification, commercial use and public release are restricted.

Rationale:

- F1 requires local reproducibility evidence, not only source inspection.
- Promising I/O surfaces are not enough to justify F2 adapter work without a successful build and minimal run.
- The license needs tighter review before any public/commercial or modified-source usage.

Consequences:

- `docs/10_next/10_NEXT.md` now points to resolving the Akochan build/toolchain blocker.
- Akochan remains a baseline/reviewer candidate, not a runnable baseline yet.
- The next attempt should use a supported Linux toolchain or a corrected macOS Homebrew LLVM/OpenMP/Boost toolchain.
- Do not run self-play, train, tune, connect to Tenhou or write an adapter while resolving this F1 blocker.

Linked docs:

- `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0002 — Pause Mortal Runnable Baseline and Move F1 Path to Akochan

Decision:

```text
Pause Mortal as a runnable baseline because the project currently has no lawful, verifiable and usable Mortal trained model artifact.
Keep Mortal as source-code, mjai-interface, methodology and engineering reference.
Move the next baseline F1 reproducibility audit path to Akochan.
```

Context:

- Mortal source and selected docs were inspected during F1, but the official mjai inference path requires a trained model artifact.
- No model version/tag, usage constraints or checksum can currently be recorded for a usable Mortal trained model artifact.
- Official evidence already recorded in the project says trained Mortal parameters are not currently planned for public release.
- The project must not use unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.

Rationale:

- F1 requires reproducibility evidence, including artifact provenance, usage constraints and checksum before local inference results can be trusted.
- Using unknown model files would create reproducibility, license, safety and governance risk.
- Keeping Mortal as a reference preserves useful mjai/interface and engineering lessons without pretending it is a runnable baseline.
- Akochan is the next lowest-cost baseline F1 path already listed in the racing funnel.

Consequences:

- Mortal is not promoted to F2.
- Mortal runnable-baseline work stays paused unless a lawful, verifiable and usable trained model artifact is provided later.
- Any future Mortal artifact must be verified in F1 before adapter work or evaluation work begins.
- `docs/10_next/10_NEXT.md` now points to Akochan F1 reproducibility audit as the single next task.
- This decision does not start the Akochan audit and does not authorize training, model downloads, real Tenhou access or platform automation.

Linked docs:

- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```
