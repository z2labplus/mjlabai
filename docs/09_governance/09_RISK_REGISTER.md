# 09_RISK_REGISTER

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Evaluation overclaims | Research | High | Medium | Require documented sample size and uncertainty | Open |
| Platform automation compliance | Compliance | High | Medium | Offline/self-play first; compliance review before integration | Open |
| Data rights ambiguity | Data | Medium | Medium | Track source, rights and allowed use | Open |
| Hidden information leakage | Evaluation | High | Medium | Add leakage tests to regression suite | Open |
| Optimizing loss instead of Tenhou EV | Research | High | High | Every experiment reports Tenhou-oriented metrics | Open |

## 2026-06-12 — P7 supervised-learning risk and evidence taxonomy risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 risk/evidence taxonomy is mistaken for P7 implementation approval. | Governance / Scope | High | Medium | `03K`, `10_NEXT`, handoff and evidence log state that taxonomy definition does not approve implementation or first-task execution. | Open |
| P7 risk/evidence taxonomy is mistaken for source approval or training-data approval. | Data / Governance | High | Medium | `03K` maps source readiness evidence to readiness inventory claims only and requires separate source approval evidence. | Open |
| Evidence grades are overread as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `03K` defines evidence-to-claim mapping and forbidden interpretations. | Open |
| The next review task drifts into implementation, parser, reader, ingestion, feature extraction, label generation or training. | Governance / Scope | High | Medium | `10_NEXT` defines the next task as a docs-only review gate and forbids production code, tests, fixtures and implementation behavior. | Open |
| Later P8/P10/P12 work is treated as implicitly approved by P7 taxonomy. | Governance / Stage Control | High | Medium | `03K` records a P8-P12 non-entry boundary requiring separate transition reviews and approvals. | Open |

## 2026-06-12 — P7 feature and label readiness boundary review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 feature/label readiness review closure is mistaken for feature extraction approval. | Governance / Scope | High | Medium | `03J`, `10_NEXT`, evidence log and handoff state that review can close but no feature extraction implementation is approved. | Open |
| P7 feature/label readiness review closure is mistaken for label generation approval. | Governance / Scope | High | Medium | `03J` repeats that no candidate label family is approved for generation. | Open |
| The next risk/evidence taxonomy task drifts into implementation or source approval. | Governance / Scope | High | Medium | `10_NEXT` defines the next task as docs-only taxonomy work and forbids implementation, source approval, feature extraction, label generation and training. | Open |
| Review evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `03J` evidence grade is boundary review evidence only with explicit non-evidence warnings. | Open |
| P7 docs-only planning drifts into P8-P12, self-play, league or runner behavior. | Governance / Stage Control | High | Medium | `03J`, stage contract and `10_NEXT` keep P8-P12 closed until separate transition reviews. | Open |

## 2026-06-12 — P7 feature and label readiness boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 feature/label readiness boundary is mistaken for feature extraction approval. | Governance / Scope | High | Medium | `03I`, `10_NEXT`, evidence log and handoff state that no feature extraction implementation is approved. | Open |
| P7 feature/label readiness boundary is mistaken for label generation approval. | Governance / Scope | High | Medium | `03I` defines label readiness requirements but keeps all candidate label families not approved for generation. | Open |
| Hidden-information leakage enters future features. | Data / Leakage | High | Medium | `03I` requires public-information-only policy, hidden-info exclusion and validation before implementation. | Open |
| Future-information leakage enters future features or labels. | Data / Leakage | High | Medium | `03I` requires decision-time boundary, future-info exclusion and validation before implementation. | Open |
| Train/validation leakage is ignored during feature / label planning. | Data / Leakage | High | Medium | `03I` requires split leakage policy before supervised dataset construction. | Open |
| Candidate feature or label families are treated as approved schemas. | Governance / Scope | High | Medium | `03I` marks every candidate family as planning only and implementation not allowed now. | Open |
| Parser, reader or ingestion work creeps into feature/label review. | Governance / Scope | High | Medium | `03I` keeps parser / reader / ingestion as separate dependencies and `10_NEXT` forbids implementation. | Open |
| P7 boundary evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | Evidence grade is P7 feature/label readiness boundary definition evidence only with explicit non-evidence warnings. | Open |
| P7 planning drifts into P8/P10 self-play or league label sources. | Governance / Stage Control | High | Medium | `03I` forbids self-play and league labels before later-stage approval. | Open |

## 2026-06-12 — P7 data/source readiness inventory review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 data/source readiness inventory review closure is mistaken for source approval. | Data / Governance | High | Medium | `03H`, `10_NEXT`, evidence log and handoff state that review can close but no source is approved for P7 training or ingestion. | Open |
| P7 data/source readiness inventory review is mistaken for training-data approval. | Data / Scope | High | Medium | `03H` repeats that current approved P7 training source is `None.` | Open |
| The next feature/label boundary task drifts into feature extraction or label generation implementation. | Governance / Scope | High | Medium | `10_NEXT` defines the next task as docs-only boundary work and forbids feature extraction, label generation, datasets, training and model code. | Open |
| Parser, reader or ingestion scope creeps into feature/label readiness planning. | Governance / Scope | High | Medium | `03H` keeps parser, reader, ingestion, CLI and broad file ingestion unapproved and routes them to separate future approvals. | Open |
| P7 review evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `03H` evidence grade is inventory review evidence only with explicit non-evidence warnings. | Open |
| P7 planning drifts into P8-P12, self-play, league or runner behavior. | Governance / Stage Control | High | Medium | `03H`, stage contract and `10_NEXT` keep P8-P12 closed until separate transition reviews. | Open |

## 2026-06-08 — P7 data/source readiness inventory risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 data/source readiness inventory is mistaken for source approval. | Data / Governance | High | Medium | `03G`, `10_NEXT`, evidence log and handoff state that no source is approved for P7 training or ingestion. | Open |
| P6 synthetic/local fixture is mistaken for P7 training data. | Data / Scope | High | Medium | `03G` classifies it as docs/schema context only and repeats that it is not training data. | Open |
| Repository documentation is mistaken for a dataset. | Governance / Data | Medium-High | Medium | `03G` classifies docs as `docs_context_only`, not data. | Open |
| Real Tenhou, real haifu, external logs or platform data are used before source-specific review. | Compliance / Data | High | Medium | `03G` keeps these categories blocked by rights, privacy and platform terms. | Open |
| Parser, reader or ingestion scope creeps into the next review gate. | Governance / Scope | High | Medium | `10_NEXT` requires the next task to remain docs-only and forbids parser, reader and ingestion. | Open |
| Feature extraction or label generation starts before readiness review. | Governance / Leakage | High | Medium | `03G` records feature/label boundaries as missing and unapproved. | Open |
| P7 data/source readiness is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `03G` evidence grade is inventory definition evidence only with explicit non-evidence warnings. | Open |
| P7 planning drifts into P8-P12, self-play, league or runner behavior. | Governance / Stage Control | High | Medium | `03G`, stage contract and `10_NEXT` keep P8-P12 closed until separate transition reviews. | Open |

## 2026-06-08 — P7 scope / entry criteria review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 review closure is mistaken for P7 implementation approval. | Governance / Stage Control | High | Medium | `03F`, `10_NEXT`, evidence log and stage contract state that review can close but P7 implementation remains unapproved. | Open |
| The next data/source readiness inventory is mistaken for source approval or ingestion approval. | Data / Governance | High | Medium | `10_NEXT` and `03F` require the next task to remain docs-only and distinguish inventory from approval. | Open |
| P7 data/source planning drifts into parser, reader, ingestion, feature extraction or label generation. | Governance / Scope | High | Medium | `03F` recommends only an inventory task and keeps parser, reader, ingestion, feature and label work unapproved. | Open |
| P7 readiness work drifts into training, model architecture, dataloader, optimizer, loss, checkpoint or model-artifact work. | Governance / Scope | High | Medium | `03F` and `10_NEXT` forbid implementation prompts, training and model artifacts until later explicit approval. | Open |
| P7 review evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `03F` classifies this as P7 scope / entry criteria / first-task review evidence only. | Open |
| P7 planning drifts into P8-P12. | Governance / Stage Control | High | Medium | `03F` repeats that each later stage needs separate transition review, scope, entry criteria, risk review and first-task approval. | Open |

## 2026-06-08 — P7 scope / entry criteria definition risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P7 scope definition is mistaken for P7 implementation approval. | Governance / Stage Control | High | Medium | `03E`, `10_NEXT`, evidence log and stage contract state that the next step is a docs-only review gate and that implementation remains unapproved. | Open |
| P7 entry criteria are treated as already satisfied. | Governance / Process | High | Medium | `03E` separates criterion definition from criterion satisfaction and marks most implementation prerequisites as open. | Open |
| Supervised-learning training begins before source/data approval. | Data / Governance | High | Medium | `03E` requires source-rights review, selected data-source approval and training data policy before implementation. | Open |
| Parser, reader, ingestion, feature extraction or label generation starts under the P7 scoping label. | Governance / Scope | High | Medium | `03E` and `10_NEXT` explicitly forbid parser, reader, ingestion, feature extraction and label generation for the next review gate. | Open |
| P7 scoping drifts into P8-P12. | Governance / Stage Control | High | Medium | `03E` defines P8-P12 non-entry boundaries and requires separate transition reviews for later stages. | Open |
| P7 planning evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `03E` and evidence log classify this as P7 scope / entry criteria / first-task definition evidence only. | Open |

## 2026-06-07 — Post-full-P6 transition review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Post-full-P6 transition review is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `12D`, evidence log, decision record and `10_NEXT` state that only docs-only P7 scope definition is allowed next. | Open |
| The next P7 scoping task is mistaken for P7 implementation approval. | Governance / Scope | High | Medium | `12D` and `10_NEXT` forbid production code, tests, fixtures, parser, reader, ingestion, feature extraction, label generation, training, self-play, league and real data. | Open |
| Full P6 closure is treated as training dataset approval. | Data / Governance | High | Medium | `12D` repeats that full P6 closure does not approve parser, reader, ingestion, feature extraction, label generation, real Tenhou, real haifu, external logs or platform data. | Open |
| P7 scope definition drifts into model-output integration, CLI or broad ingestion. | Governance / Scope | High | Medium | `12D` and `10_NEXT` keep model-output integration, CLI and broad file ingestion forbidden for the next task. | Open |
| Transition review evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `12D` evidence grade is transition review evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 final full closure review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Full P6 closure is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02AA`, evidence log, handoff, stage contract and `10_NEXT` state that the next step is a post-full-P6 transition review before defining any P7 task. | Open |
| Full P6 closure is mistaken for P7 first-task approval. | Governance / Stage Control | High | Medium | `02AA` and `10_NEXT` explicitly forbid P7 execution and P7 first-task approval in the closure decision. | Open |
| Full P6 closure is overread as parser, reader, ingestion, feature or label approval. | Governance / Scope | High | Medium | `02AA` accepted boundary excludes parser, dataset reader, ingestion, feature extraction and label generation. | Open |
| Full P6 closure is overread as source approval, real-data approval or platform-data approval. | Data / Compliance | High | Medium | `02AA` keeps real Tenhou, real haifu, external logs, platform data, accounts and source-specific real-data approval unapproved. | Open |
| Full P6 closure evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02AA` evidence grade is final full-closure review evidence only with explicit non-evidence boundaries. | Open |
| Post-full-P6 transition review drifts into P7 implementation. | Governance / Process | High | Medium | `10_NEXT` requires the next task to remain docs-only and to avoid production code, tests, fixtures, parser, ingestion, training, self-play, league and model-strength claims. | Open |

## 2026-06-07 — P6 risk-register and source-rights consistency review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Risk/source-rights consistency review is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02Z`, evidence log, handoff and `10_NEXT` state that the review can close but full P6 remains open until a later final closure gate explicitly passes. | Open |
| Risk/source-rights consistency review is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02Z` and `10_NEXT` keep P7-P12 unapproved and require a later post-full-P6 transition review even if final closure passes. | Open |
| The next final full P6 closure review drifts into implementation. | Governance / Scope | High | Medium | `02Z` and `10_NEXT` forbid production code, tests, fixtures, parser, reader, ingestion, feature extraction, label generation, CLI, model-output integration and real-data paths. | Open |
| Consistent source inventory is overread as real-data, source-ingestion or platform-data approval. | Data / Compliance | High | Medium | `02Z` confirms real Tenhou, real haifu, external logs, platform data, accounts and source-specific real-data approval remain blocked or unapproved. | Open |
| Consistent risk inventory is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02Z` evidence grade is risk/source-rights consistency review evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 full handoff and evidence index finalization risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Handoff / evidence finalization is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02Y`, evidence log, handoff and `10_NEXT` state full P6 remains open and the next task is risk/source-rights review. | Open |
| Handoff / evidence finalization is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02Y` and `10_NEXT` keep P7-P12 unapproved and require later final closure plus post-full-P6 transition review. | Open |
| The next risk/source-rights review drifts into implementation. | Governance / Scope | High | Medium | `02Y` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction, label generation, CLI and model-output integration. | Open |
| Evidence index entries are overread as source approval or real-data approval. | Data / Compliance | High | Medium | `02Y` evidence table marks real-data/source approval as not allowed and routes source consistency to the next docs-only review. | Open |
| Handoff finalization evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02Y` evidence grade is handoff / evidence-index finalization evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 full-closure criteria review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Closure criteria review is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02X`, evidence log, handoff and `10_NEXT` state that review can close but full P6 remains open. | Open |
| Closure criteria review is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02X` and `10_NEXT` keep P7-P12 unapproved and select only a docs-only handoff / evidence finalization task. | Open |
| The next handoff / evidence finalization task drifts into implementation. | Governance / Scope | High | Medium | `02X` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction, label generation, CLI and model-output integration. | Open |
| Required remaining items are misread as parser, dataset reader, ingestion, feature extraction or label generation approval. | Governance / Scope | High | Medium | `02X` confirms required remaining full-P6 items are docs/review/closure-only. | Open |
| Criteria review evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02X` evidence grade is review evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 full-closure criteria definition risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Closure criteria definition is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02W`, evidence log, handoff and `10_NEXT` state that this only defines criteria and full P6 remains open. | Open |
| Closure criteria definition is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02W` and `10_NEXT` keep P7-P12 unapproved and select only a docs-only criteria review gate. | Open |
| The next criteria review gate drifts into implementation. | Governance / Scope | High | Medium | `02W` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction, label generation, CLI and model-output integration. | Open |
| Required closure criteria accidentally turn parser, dataset reader, ingestion, feature extraction or label generation into required current implementation. | Governance / Scope | High | Medium | `02W` classifies those items as deferred or blocked, not required full-P6 closure items. | Open |
| Blocked real Tenhou, real haifu, external-log or platform-data categories are interpreted as source approval. | Data / Compliance | High | Medium | `02W` keeps these items blocked until source-specific lawful rights, privacy, storage and platform reviews are complete. | Open |
| Criteria-definition evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02W` evidence grade is criteria-definition evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 full-closure roadmap and remaining-scope inventory review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Roadmap review closure is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02V`, evidence log, handoff and `10_NEXT` state the review can close but full P6 remains open. | Open |
| Roadmap review closure is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02V` and `10_NEXT` keep P7-P12 unapproved and select only a docs-only closure criteria definition task. | Open |
| The next closure-criteria definition task drifts into implementation. | Governance / Scope | High | Medium | `02V` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction, label generation, CLI and model-output integration. | Open |
| Required/deferred/blocked classifications are used to approve real data or ingestion implicitly. | Data / Compliance | High | Medium | `02V` confirms real Tenhou, real haifu, external logs, platform data and source-specific real-data approval remain blocked. | Open |
| Review evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02V` evidence grade is review evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 full-closure roadmap and remaining-scope inventory risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The roadmap / inventory definition is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02U`, evidence log, handoff and `10_NEXT` state that full P6 remains open and that the next task is only a docs-only review gate. | Open |
| The roadmap / inventory definition is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02U` keeps P7-P12 unapproved and requires separate transition review, scope, entry criteria, risk review and first-task approval. | Open |
| Deferred parser, dataset reader, ingestion, feature extraction or label generation items are treated as approved implementation. | Governance / Scope | High | Medium | `02U` classifies these as deferred or blocked and states no implementation can proceed without a future explicit `10_NEXT` task and approval. | Open |
| Blocked real Tenhou, real haifu, external-log or platform-data categories are interpreted as source approval. | Data / Compliance | High | Medium | `02U` lists these as blocked until source-specific lawful rights, privacy, storage and platform reviews are complete. | Open |
| Roadmap evidence is overclaimed as model-strength, Tenhou ranked, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02U` and the evidence log classify it as roadmap / inventory evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 post-current-scope transition review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Post-current-scope transition review is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `12C`, evidence log, handoff and `10_NEXT` state that full P6 remains open and that the next task is only a docs-only roadmap / inventory. | Open |
| Post-current-scope transition review is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `12C` explains why P7 is premature and `10_NEXT` forbids P7-P12 execution. | Open |
| The next full-P6 roadmap task drifts into implementation. | Governance / Scope | High | Medium | `12C` and `10_NEXT` forbid production code, tests, fixtures, parser, reader, ingestion, feature extraction and label generation. | Open |
| Remaining full-P6 inventory is used to approve real data or ingestion implicitly. | Data / Compliance | High | Medium | `12C` requires source-specific future approval and keeps real Tenhou, real haifu, external logs and platform data unapproved. | Open |
| Transition review evidence is overclaimed as model-strength, Tenhou, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `12C` evidence grade is transition review evidence only with explicit non-evidence boundaries. | Open |

## 2026-06-07 — P6 final current-scope data-system closure review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Current-scope P6 closure is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02T`, evidence log, handoff and `10_NEXT` state that only the accepted synthetic/local minimal scope is closed. | Open |
| Current-scope P6 closure is mistaken for P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02T` and `10_NEXT` require a post-current-scope transition review before any next-stage planning or P7 task. | Open |
| Current-scope P6 closure is mistaken for parser, reader, ingestion, feature or label approval. | Governance / Scope | High | Medium | `02T` accepted boundary excludes those items and keeps them unapproved. | Open |
| Current-scope P6 closure is overclaimed as real-data, model-strength, Tenhou, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02T` evidence grade and explicit non-evidence list keep the decision as data-system closure review evidence only. | Open |
| Post-current-scope transition review drifts into implementation. | Governance / Process | High | Medium | `10_NEXT` sets the next task to docs-only transition review and forbids code, tests, fixtures, ingestion, real data, training and P7-P12. | Open |

## 2026-06-07 — P6 current-scope data-system closure criteria review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Closure criteria review is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02S`, evidence log and `10_NEXT` state that the review can close but full P6 remains open. | Open |
| Closure criteria review is mistaken for current-scope P6 closure. | Governance / Stage Control | High | Medium | `02S` selects a later final current-scope closure review gate and does not itself close current-scope P6. | Open |
| Closure criteria review is mistaken for implementation approval. | Governance / Scope | High | Medium | `02S` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction and label generation. | Open |
| Final closure review gate is treated as P7-P12 entry approval. | Governance / Stage Control | High | Medium | `02S` recommends only a docs-only current-scope P6 closure gate; P7-P12 still require separate scope, risk review and approval. | Open |
| Review evidence is overclaimed as data ingestion, model-strength, Tenhou, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02S` and evidence log classify it as P6 closure-criteria review evidence only with explicit non-evidence boundaries. | Open |
| A final closure review tries to fix code, tests or fixtures instead of recording a blocker. | Governance / Process | High | Medium | `10_NEXT` requires the next task to remain docs-only and to avoid implementation changes. | Open |

## 2026-06-07 — P6 current-scope data-system closure criteria definition risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Closure criteria definition is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02R`, handoff, evidence log and `10_NEXT` state that it defines criteria only and does not close full P6. | Open |
| Closure criteria definition is mistaken for current-scope P6 closure. | Governance / Stage Control | High | Medium | `02R` requires a later docs-only closure-criteria review and final current-scope closure review before closure. | Open |
| Closure criteria definition is mistaken for implementation approval. | Governance / Scope | High | Medium | `02R` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction and label generation. | Open |
| Deferred items are treated as required blockers and P6 expands unnecessarily. | Planning / Scope | Medium-High | Medium | `02R` lists deferred items and explains why parser, reader, ingestion, feature, label, real data, CLI and P7-P12 are not required for current-scope closure. | Open |
| Review gate is skipped and the project jumps directly to final closure or P7-P12. | Governance / Process | High | Medium | `02R` and `10_NEXT` set the next task to a closure-criteria review gate and list P7-P12 non-entry conditions. | Open |
| Closure criteria evidence is overclaimed as data ingestion, model-strength, Tenhou, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02R` and evidence log classify this as closure-criteria definition evidence only with explicit non-evidence boundaries. | Open |
| Real-data or source-approval ambiguity enters closure review. | Data / Compliance | High | Medium | `02R` requires source inventory consistency and keeps real Tenhou, real haifu, external logs and platform data deferred. | Open |

## 2026-06-07 — P6 next current-scope data-system task definition risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The selected closure-criteria task is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02Q`, evidence log and `10_NEXT` state the next task only defines closure criteria and does not close P6. | Open |
| The selected closure-criteria task is mistaken for implementation approval. | Governance / Scope | High | Medium | `02Q` and `10_NEXT` forbid code, tests, fixtures, parser, reader, ingestion, feature extraction and label generation. | Open |
| P6 continues indefinitely through additional task-definition gates without closure criteria. | Planning / Scope | Medium-High | Medium | `02Q` selects current-scope closure criteria as the next task specifically to avoid unbounded P6 expansion. | Open |
| Candidate next-task language pulls the project toward validation-error APIs or additional synthetic implementation too early. | Governance / Scope | Medium-High | Medium | `02Q` defers error taxonomy, fixture checklist and implementation approval criteria until after closure criteria. | Open |
| Next-task definition evidence is overclaimed as data-system, real-data, model-strength or LuckyJ evidence. | Evaluation / Governance | High | Medium | `02Q` and evidence log classify it as P6 task-definition evidence only with explicit non-evidence boundaries. | Open |
| P6 task planning drifts into P7-P12. | Governance / Stage Control | High | Medium | `02Q`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-07 — P6 minimal replay schema and synthetic fixture current-scope acceptance risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Current-scope acceptance is mistaken for full P6 closure. | Governance / Stage Control | High | Medium | `02P`, evidence log, handoff and `10_NEXT` state that only the exact minimal replay schema module, project-authored synthetic/local fixture and two minimal tests are accepted. | Open |
| Current-scope acceptance is mistaken for approval to add more implementation. | Governance / Scope | High | Medium | `02P` sets the next task to docs-only task definition and forbids new code, tests, fixtures, schema expansion, parser, reader, ingestion, feature extraction and label generation. | Open |
| The next docs-only task boundary is skipped and P6 expands directly into implementation. | Governance / Process | High | Medium | `02P` required a docs-only next-task definition and `02Q` now selects a docs-only closure-criteria task before any further implementation. | Open |
| The accepted synthetic fixture is overclaimed as real data, training data or data-ingestion evidence. | Data / Compliance | High | Medium | `02P` and evidence log classify the fixture as project-authored synthetic/local only and not ingestion, source approval, real Tenhou, real haifu, external-log or platform-data evidence. | Open |
| Acceptance evidence is overclaimed as model-strength, Tenhou ranked, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02P`, evidence log and `10_NEXT` repeat explicit non-evidence boundaries. | Open |
| P6 acceptance planning drifts into P7-P12. | Governance / Stage Control | High | Medium | `02P`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-07 — P6 minimal replay schema and synthetic fixture implementation review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Implementation review closure is mistaken for broad P6 implementation approval. | Governance / Stage Control | High | Medium | `02O`, evidence log and `10_NEXT` state the review can close only for the exact minimal implementation. | Open |
| Implementation review is mistaken for P6 current-scope completion or P7 entry. | Governance / Stage Control | High | Medium | The next task is a separate docs-only current-scope acceptance decision and P7-P12 remain closed. | Open |
| Review evidence is overclaimed as data ingestion, parser, dataset-reader, feature or label evidence. | Data / Evidence | High | Medium | `02O` explicit non-evidence list keeps those categories absent. | Open |
| Review evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02O`, evidence log and `10_NEXT` classify it as implementation-review evidence only. | Open |
| A follow-up task uses the review result to modify code, tests or fixtures without approval. | Governance / Scope | High | Medium | `10_NEXT` requires the next task to remain docs-only and forbids production code, tests and fixtures. | Open |

## 2026-06-07 — P6 minimal replay schema and synthetic fixture implementation risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Minimal replay schema helper is mistaken for parser, dataset reader or ingestion approval. | Governance / Data | High | Medium | `replay_schema.py`, changelog, evidence log and `10_NEXT` state it validates in-memory mappings only and the next step is review. | Open |
| Synthetic replay fixture is mistaken for real Tenhou, real haifu, external-log or platform-data evidence. | Data / Compliance | High | Medium | The fixture source note, warnings and provenance flags state project-authored synthetic/local only and all real/external/platform flags false. | Open |
| Fixture content is overclaimed as training data, labels, model output or model-strength evidence. | Evaluation / Governance | High | Medium | The schema helper forbids model-output / label fields and docs repeat non-evidence boundaries. | Open |
| Account, session, cookie, token or private-log identifiers enter future fixtures. | Privacy / Security | High | Low-Medium | The helper rejects forbidden keys such as `account_id`, `session_id`, `cookie`, `token` and `private_log`. | Open |
| Review gate is skipped and P6 expands directly into parser, reader, ingestion, feature extraction or label generation. | Governance / Stage Control | High | Medium | `10_NEXT` makes the next task a docs-only review gate and forbids new code/tests/fixtures/data files. | Open |
| P6 minimal implementation is used as P7-P12 entry or LuckyJ / stable-dan evidence. | Governance / Evaluation | High | Medium | Evidence log and risk register classify it as P6 synthetic/local schema smoke implementation evidence only. | Open |

## 2026-06-07 — P6 minimal replay schema and synthetic fixture implementation approval-decision risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The approval decision is mistaken for broad P6 implementation approval. | Governance / Stage Control | High | Medium | `02N` and `10_NEXT` approve only the exact next minimal implementation task and exact file list. | Open |
| The approval decision is mistaken for implementation execution evidence. | Governance / Evidence | High | Medium | `02N` evidence grade states approval-decision evidence only; no code, tests or fixtures were created in this task. | Open |
| The next task expands beyond the four exact implementation files. | Governance / Scope | High | Medium | `02N` and `10_NEXT` name exact allowed files and require stop if unapproved files appear. | Open |
| Minimal schema work expands into parser, dataset reader, ingestion, feature extraction or label generation. | Data / Engineering | High | Medium | `02N` forbidden future expansion and stop conditions keep those classes closed. | Open |
| Synthetic fixture implementation is mistaken for real Tenhou, real haifu, external-log or platform-data approval. | Data / Compliance | High | Medium | `02N` allows only project-authored synthetic/local fixture work and keeps all real / external / platform sources blocked. | Open |
| Validation tests become broad file ingestion, source approval or real-data checks. | Data / Scope | High | Medium | `02N` limits tests to the approved synthetic fixture and schema behavior only. | Open |
| Approval evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02N`, evidence log and `10_NEXT` repeat explicit non-evidence boundaries. | Open |
| P6 approval planning drifts into P7-P12. | Governance / Stage Control | High | Medium | `02N`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-07 — P6 minimal replay schema and synthetic fixture implementation proposal review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Proposal review closure is mistaken for P6 implementation approval. | Governance / Stage Control | High | Medium | `02M`, evidence log and `10_NEXT` state review can close but implementation remains closed. | Open |
| No-blocker review is mistaken for permission to create candidate files. | Governance / Scope | High | Medium | `02M` repeats that `src/mjlabai/data/replay_schema.py`, `tests/fixtures/data/synthetic_replay_smoke.json` and future tests remain candidate paths only. | Open |
| The next approval-decision gate is skipped and implementation starts directly. | Governance / Process | High | Medium | `10_NEXT` sets a docs-only approval-decision task as the next first item. | Open |
| Future minimal implementation expands into parser, dataset reader, ingestion, feature extraction or label generation. | Data / Engineering | High | Medium | `02M` confirms `02L` forbidden future expansion and stop conditions are sufficient. | Open |
| Synthetic/local fixture implementation is overread as permission to use real Tenhou, real haifu, external logs or platform data. | Data / Compliance | High | Medium | `02M` keeps future scope project-authored synthetic/local only and keeps real/external/platform sources blocked. | Open |
| Review evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02M` evidence grade and explicit non-evidence list classify it as proposal-review evidence only. | Open |
| P6 approval planning drifts into P7-P12. | Governance / Stage Control | High | Medium | `02M`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-07 — P6 minimal replay schema and synthetic fixture implementation proposal risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Minimal proposal drafting is mistaken for P6 implementation approval. | Governance / Stage Control | High | Medium | `02L`, evidence log and `10_NEXT` state the proposal is for review before code and implementation remains closed. | Open |
| Proposed file candidates are mistaken for files to create now. | Governance / Scope | High | Medium | `02L` marks every candidate path as `implementation_allowed_now = no` and requires later review. | Open |
| The next review gate is skipped and implementation starts directly. | Governance / Process | High | Medium | `10_NEXT` sets the next task to review the proposal before code. | Open |
| Future minimal implementation expands into parser, dataset reader, ingestion, feature extraction or label generation. | Data / Engineering | High | Medium | `02L` explicitly forbids those classes and includes stop conditions and rollback criteria. | Open |
| A synthetic fixture candidate includes real Tenhou, real haifu, external logs or platform data. | Data / Compliance | High | Medium | `02L` requires project-authored synthetic/local content only and no-real-data guardrails. | Open |
| Account/session/cookie/token or private-log data enters through a fixture proposal. | Privacy / Security | High | Low-Medium | `02L` forbids account/private identifiers and requires stop before implementation. | Open |
| Proposal evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02L` evidence grade and explicit non-evidence list classify it as proposal drafting evidence only. | Open |
| P6 proposal planning drifts into P7-P12. | Governance / Stage Control | High | Medium | `02L`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-06 — P6 replay schema and synthetic fixture implementation proposal boundary review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Proposal-boundary review closure is mistaken for P6 implementation approval. | Governance / Stage Control | High | Medium | `02K`, evidence log and `10_NEXT` state review can close but implementation remains closed. | Open |
| The next proposal-drafting task is mistaken for code approval. | Governance / Scope | High | Medium | `10_NEXT` limits the next task to docs-only proposal drafting before code review. | Open |
| Future proposal drafting creates fixtures, tests or schema code. | Data / Engineering | High | Medium | `02K` repeats that fixture files, tests, dataclasses, pydantic models, JSON schema and parsers remain closed. | Open |
| Parser, dataset reader, ingestion, feature extraction or label generation starts from review wording. | Data / Stage Control | High | Medium | `02K` keeps those classes closed and requires later explicit approval. | Open |
| Real Tenhou, real haifu, external logs or platform data are introduced through proposal drafting. | Data / Compliance | High | Medium | `02K` and `10_NEXT` keep real/external/platform sources blocked. | Open |
| Review evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02K` evidence grade and explicit non-evidence list classify the artifact as review evidence only. | Open |
| P6 proposal planning drifts into P7-P12. | Governance / Stage Control | High | Medium | Stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-06 — P6 replay schema and synthetic fixture implementation proposal boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Proposal boundary definition is mistaken for P6 implementation approval. | Governance / Stage Control | High | Medium | `02J`, evidence log and `10_NEXT` state proposal definition is not implementation approval. | Open |
| Future implementation proposal becomes too broad. | Governance / Scope | High | Medium | `02J` requires allowed/forbidden files, allowed/forbidden code changes, rollback plan and blockers before review. | Open |
| Proposal language expands into parser, dataset reader, data ingestion, feature extraction or label generation. | Data / Engineering | High | Medium | `02J` forbids those classes and marks them deferred until separate approval. | Open |
| Real Tenhou, real haifu, external logs or platform data are introduced through a proposal. | Data / Compliance | High | Medium | `02J` limits candidate work to project-authored synthetic/local source category and keeps source approval separate. | Open |
| Tests or fixtures are created from proposal-boundary language. | Governance / Scope | High | Medium | `02J` defines test/fixture candidates only and `10_NEXT` forbids code, tests and fixtures in the review task. | Open |
| Proposal evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02J` evidence grade and explicit non-evidence list keep the artifact as proposal-boundary definition evidence only. | Open |
| P6 planning drifts into P7-P12 after proposal-boundary definition. | Governance / Stage Control | High | Medium | `02J`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-06 — P6 replay schema and fixture implementation readiness checklist review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Readiness checklist review closure is mistaken for replay schema or fixture implementation approval. | Governance / Stage Control | High | Medium | `02I`, evidence log and `10_NEXT` state review can close but implementation remains closed. | Open |
| No-blocker review is mistaken for `ready_for_implementation`. | Governance / Process | High | Medium | `02I` repeats that schema and fixture decisions remain `not_ready_for_implementation`. | Open |
| Future proposal-boundary task drifts into code, tests or fixture creation. | Governance / Scope | High | Medium | `10_NEXT` marks the next task docs-only and forbids production code, tests, fixtures, schema code, parsers, readers and ingestion. | Open |
| Parser, dataset reader, feature extraction, label generation or data ingestion starts from the review wording. | Data / Engineering | High | Medium | `02I` keeps those classes deferred/not approved and requires separate future review and explicit `10_NEXT` approval. | Open |
| Source approval or ingestion approval is inferred from checklist review. | Data / Rights | High | Medium | `02I` repeats source approval and ingestion approval remain separate and absent. | Open |
| Review evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02I` and evidence log classify the artifact as checklist review evidence only with explicit non-evidence warnings. | Open |
| P6 docs planning drifts into P7-P12 after review closure. | Governance / Stage Control | High | Medium | `02I`, stage contract and `10_NEXT` keep P7-P12, training, self-play, league and runner behavior closed. | Open |

## 2026-06-06 — P6 replay schema and fixture implementation readiness checklist risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Readiness checklist definition is mistaken for replay schema or fixture implementation approval. | Governance / Stage Control | High | Medium | `02H`, evidence log and `10_NEXT` state no candidate implementation class is approved and the next task is review only. | Open |
| A `ready_for_review_only` checklist status is mistaken for `ready_for_implementation`. | Governance / Process | High | Medium | `02H` defines separate decision vocabulary and keeps implementation task approval, human approval and explicit `10_NEXT` approval as required future gates. | Open |
| Future review skips source-specific rights, storage, privacy or platform terms before implementation. | Data / Compliance | High | Medium | `02H` requires source-specific approval, storage policy, privacy / terms review and evidence references before implementation. | Open |
| Parser, dataset reader, feature extraction or label generation is started from checklist language. | Governance / Engineering | High | Medium | `02H`, stage contract and `10_NEXT` keep parser, reader, feature and label implementation closed. | Open |
| A future fixture task copies real Tenhou, real haifu, external logs or platform data into a synthetic/local fixture. | Data / Compliance | High | Medium | `02H` requires project-authored fixture content, no real logs, no player/account identifiers and explicit future validation before fixture creation. | Open |
| Checklist evidence is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02H` and evidence log classify the artifact as checklist-definition evidence only with explicit non-evidence warnings. | Open |
| P6 checklist planning drifts into P7-P12 implementation. | Governance / Stage Control | High | Medium | `02H`, stage contract and `10_NEXT` keep training, self-play, league, runner behavior and P7-P12 closed. | Open |

## 2026-06-06 — P6 synthetic/local replay fixture boundary review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic/local replay fixture boundary review is mistaken for fixture implementation approval. | Governance / Stage Control | High | Medium | `02G`, evidence log and `10_NEXT` state review can close but fixture implementation remains unapproved. | Open |
| Review closure is mistaken for replay schema implementation approval. | Governance / Stage Control | High | Medium | `02G` keeps replay schema code, dataclasses, pydantic models, JSON schema and parser contracts closed. | Open |
| Future readiness checklist task drifts into code, tests or fixture creation. | Governance / Scope | Medium-High | Medium | `10_NEXT` marks the next task docs-only and forbids production code, tests, fixtures, schema code, parsers, readers and ingestion. | Open |
| Source inventory dependency is overread as source approval. | Data / Rights | High | Medium | `02G` repeats that `02A` / `02D` are prerequisites only and source approval remains separate. | Open |
| Shape-family review is treated as parser, dataset-reader, feature or label readiness. | Data / Engineering | High | Medium | `02G` labels shape families as documentation boundaries and keeps implementation entry criteria unsatisfied. | Open |
| P6 fixture planning is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02G` evidence grade is review evidence only with explicit non-evidence warnings. | Open |
| P6 docs planning drifts into P7-P12 after review closure. | Governance / Stage Control | High | Medium | `02G`, stage contract and `10_NEXT` keep training, self-play, league, runner behavior and P7-P12 closed. | Open |

## 2026-06-06 — P6 synthetic/local replay fixture boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic/local replay fixture boundary is mistaken for fixture implementation approval. | Governance / Stage Control | High | Medium | `02F`, evidence log and `10_NEXT` state fixture implementation remains unapproved. | Open |
| Future fixture shape families are treated as concrete JSON schema, dataclass or parser contract. | Data / Engineering | Medium-High | Medium | `02F` labels shape families as documentation boundary only and requires later review before implementation. | Open |
| Real Tenhou, real haifu or external log content is copied into a future synthetic fixture. | Compliance / Data | High | Medium | `02F` forbids real/external/platform content and requires future no-real-data validation. | Open |
| Player/account identifiers enter a future fixture. | Privacy / Security | High | Low-Medium | `02F` requires synthetic seat ids, no account identifiers and privacy review before creation. | Open |
| Model outputs, labels or features creep into future fixture planning. | Governance / Data Quality | High | Medium | `02F` forbids model output, feature extraction and labels from real data; P7 remains closed. | Open |
| Synthetic replay fixture is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02F` and evidence log classify this as boundary definition evidence only. | Open |
| Future fixture boundary is used to bypass source approval or ingestion approval. | Data / Rights | High | Medium | `02F` depends on `02A` / `02D` and requires explicit future `10_NEXT` implementation approval. | Open |
| Fixture boundary expands into broad ingestion, CLI, parser or dataset reader work. | Governance / Scope | High | Medium | `02F`, stage contract and `10_NEXT` keep fixture implementation, CLI, parser and reader work closed. | Open |
| P6 fixture planning drifts into P7-P12. | Governance / Stage Control | High | Medium | `02F` keeps training, self-play, league, runner behavior and P7-P12 closed. | Open |

## 2026-06-06 — P6 replay schema documentation boundary review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Replay schema boundary review is mistaken for replay schema implementation approval. | Governance / Stage Control | High | Medium | `02E`, evidence log and `10_NEXT` state the review can close but implementation remains unapproved. | Open |
| The next synthetic/local replay fixture boundary task is mistaken for fixture implementation or schema code approval. | Governance / Stage Control | Medium-High | Medium | `02E` recommends a docs-only boundary task and `10_NEXT` forbids production code, tests, fixtures and schema code. | Open |
| Source inventory dependency is overread as source approval after the review found no blocker. | Data / Rights | High | Medium | `02E` repeats that `02A` / `02D` are prerequisites, not source approval, ingestion approval or implementation approval. | Open |
| Field-family draft is treated as a concrete JSON schema, dataclass or parser contract. | Data / Engineering | Medium-High | Medium | `02E` reviews all field families as documentation boundary only and keeps implementation entry criteria unsatisfied. | Open |
| Replay schema review drifts into real Tenhou, real haifu, external logs or platform data. | Compliance / Scope | High | Medium | `02E`, stage contract and `10_NEXT` keep real/external/platform data closed. | Open |
| Replay schema review is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02E` classifies this as P6 replay schema documentation boundary review evidence only. | Open |
| P6 docs planning drifts into P7-P12 after review closure. | Governance / Stage Control | High | Medium | `02E` and `10_NEXT` keep implementation and P7-P12 closed; next task remains docs-only. | Open |

## 2026-06-06 — P6 replay schema documentation boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Replay schema documentation boundary is mistaken for replay schema implementation approval. | Governance / Stage Control | High | Medium | `02B`, evidence log and `10_NEXT` state that the boundary is docs-only and implementation remains unapproved. | Open |
| Field-family names are treated as a concrete JSON schema, dataclass or parser contract. | Data / Engineering | Medium-High | Medium | `02B` labels the field-family draft as documentation boundary only and requires a later review before implementation. | Open |
| Source inventory review plus replay schema boundary are mistaken for source ingestion approval. | Data / Rights | High | Medium | `02B` requires source-specific approval, storage policy, evidence references and an explicit implementation task before ingestion. | Open |
| Hidden-information leakage enters future decision-state or label fields. | Evaluation / Data Quality | High | Medium | `02B` requires observation / decision-state boundaries, hidden-information policy and later leakage tests before implementation. | Open |
| Real Tenhou, real haifu, external logs or platform data are introduced under replay-schema planning. | Compliance / Scope | High | Medium | `02B`, stage contract and `10_NEXT` keep real/external/platform sources blocked pending source-specific review. | Open |
| Replay schema planning is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02B` and evidence log classify the artifact as P6 replay schema documentation boundary definition evidence only. | Open |
| P6 replay schema review drifts into feature extraction, label generation, CLI or broad file ingestion. | Governance / Stage Control | High | Medium | The next task is a docs-only review gate and must not implement schema code, readers, CLI, feature extraction or label generation. | Open |
| P7-P12 work starts from replay schema planning without implementation and transition approval. | Governance / Stage Control | High | Medium | `02B`, stage contract and `10_NEXT` keep training, self-play, league, runner behavior and P7-P12 closed. | Open |

## 2026-06-06 — P6 source inventory review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Source inventory review is mistaken for source-ingestion approval. | Governance / Data | High | Medium | `02D`, evidence log and `10_NEXT` state the review can close but P6 implementation, replay schema implementation and data ingestion remain closed. | Open |
| Replay schema boundary definition drifts into schema code or dataset readers. | Governance / Stage Control | High | Medium | The next task is docs-only boundary definition and must not implement replay schema code, ingestion, feature extraction, label generation, CLI or broad file ingestion. | Open |
| Real Tenhou, real haifu, external logs or platform data are treated as approved because the inventory review found no blocker. | Data / Compliance | High | Medium | `02D` says no source category is over-approved and real/external/platform sources remain unapproved or blocked pending source-specific review. | Open |
| P6 planning review is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02D` and evidence log classify this as P6 source inventory review evidence only. | Open |
| P7-P12 work starts from replay schema boundary planning without implementation approval. | Governance / Stage Control | High | Medium | `02D`, stage contract and `10_NEXT` keep P6 implementation and P7-P12 closed. | Open |

## 2026-06-05 — P6 data-source provenance and rights inventory risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Rights ambiguity for future sources leads to unsafe ingestion. | Data / Rights | High | Medium | `02A` requires owner/rightsholder, license/terms summary and allowed/forbidden use before ingestion. | Open |
| Platform terms ambiguity is ignored for Tenhou or other platform-derived data. | Compliance | High | Medium | `02A` keeps real Tenhou/platform sources blocked until source-specific legal/terms review. | Open |
| Real data is accidentally ingested before approval. | Data / Stage Control | High | Medium | `02A`, stage contract and `10_NEXT` state this task is docs-only and next step is review gate. | Open |
| Private or personal data enters the project without review. | Privacy | High | Low-Medium | `02A` requires privacy/personal-data review and blocks account/session/cookie/token sources. | Open |
| Account, session, cookie or token leakage occurs through future platform access. | Security / Compliance | High | Low-Medium | `02A` forbids account tooling and platform-account data in current P6 planning. | Open |
| Scraping, automation or evasion logic is introduced under a data-source task. | Compliance / Scope | High | Medium | `02A` and `10_NEXT` explicitly forbid platform automation, scraping, evasion and anti-detection tooling. | Open |
| Raw real data is committed to Git. | Data Hygiene | High | Medium | `02A` requires Git inclusion policy and keeps raw real data out of Git. | Open |
| Third-party artifacts are committed to Git. | License / Hygiene | High | Medium | `02A` forbids third-party source, binaries, `params/` and build artifacts without explicit approval. | Open |
| Model weights are committed or used without provenance. | Reproducibility / Governance | High | Medium | `02A` keeps unknown `*.pth`, `*.pt`, checkpoints and snapshots blocked. | Open |
| Source contamination or train/test leakage enters future datasets. | Data Quality | High | Medium | `02A` requires source ids, schema family, transform/version and future split/leakage controls before implementation. | Open |
| Synthetic fixtures are overclaimed as real-data or strength evidence. | Evaluation / Governance | High | Medium | `02A` marks synthetic fixtures as smoke/review context only and repeats non-evidence warnings. | Open |
| Stage creep into P7-P12 starts from P6 inventory review. | Governance / Stage Control | High | Medium | `02A` and `10_NEXT` require docs-only review before implementation and keep P7-P12 closed. | Open |
| P6 source inventory is mistaken for ingestion approval. | Governance / Data | High | Medium | `02A` states the inventory is definition evidence only and requires a review gate plus later implementation approval. | Open |
| P6 source inventory is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | Evidence log and `02A` classify it as P6 inventory-definition evidence only, not Tenhou/LuckyJ/stable-dan evidence. | Open |

## 2026-06-05 — P6 data-system scope definition risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The P6 scope definition is mistaken for approval to implement replay schema code or ingest data. | Governance / Stage Control | High | Medium | `02C`, stage contract and `10_NEXT` state that P6 implementation remains closed and the next task is provenance/rights inventory only. | Open |
| The next P6 provenance task drifts into real Tenhou, real haifu, external logs, platform data or online account access. | Data / Compliance | High | Medium | `02C` forbids these inputs until a later source-rights and compliance review approves them. | Open |
| A source is treated as usable before rights, allowed use, storage and redistribution status are recorded. | Data / Rights | High | Medium | `02C` requires source id, owner/origin, license/terms, allowed/forbidden use, storage, checksum/version and evidence reference before ingestion. | Open |
| P6 planning artifacts are overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `02C`, evidence log and `10_NEXT` classify this task as P6 planning evidence only and repeat non-evidence warnings. | Open |
| P7-P12 work starts before P6 source/provenance and data-system implementation gates are approved. | Governance / Stage Control | High | Medium | `02C` records P7-P12 non-entry boundaries and requires separate transition, scope, entry criteria and first-task approval for later stages. | Open |

## 2026-06-04 — Post-P5 transition review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The docs-only P6 scope definition task is mistaken for P6 implementation approval. | Governance / Stage Control | High | Medium | `12B`, stage contract and `10_NEXT` state the next task may define P6 scope/entry criteria/first task only and must not implement replay schema code, data ingestion or pipelines. | Open |
| P6 planning jumps directly into real Tenhou, real haifu, external logs or platform data before source rights and compliance boundaries are defined. | Data / Compliance | High | Medium | `12B` requires P6 allowed/forbidden inputs, provenance guardrails and evidence requirements before any ingestion. | Open |
| P6 planning is overclaimed as model-strength, Tenhou, stable-dan, LuckyJ or candidate-promotion evidence. | Evaluation / Governance | High | Medium | `12B`, evidence log and `10_NEXT` classify the transition as planning evidence only and forbid strength/ranking claims. | Open |

## 2026-06-04 — Final P5 closure review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| P5 closure is mistaken for P6-P12 entry approval or P6 first-task approval. | Governance / Stage Control | High | Medium | `05X`, handoff, evidence log, stage contract and `10_NEXT` state P5 closure is not P6-P12 entry and the next task is separate post-P5 transition review. | Open |
| Synthetic/local P5 evidence is overclaimed as model strength, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ comparison or candidate promotion. | Evaluation / Governance | High | Medium | `05X` repeats explicit non-evidence boundaries and `05W` evidence index marks promotion/ranking/Tenhou/LuckyJ/P6-P12 entry as `no` for all rows. | Open |
| Post-P5 transition planning skips independent scope, entry criteria, risk review and first task. | Governance / Planning | High | Medium | `05X` and `10_NEXT` require a separate post-P5 transition review before defining any P6 task. | Open |

## 2026-06-04 — P5 handoff and evidence index finalization risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Handoff/evidence index finalization is mistaken for P5 closure or P6-P12 entry approval. | Governance / Scope | High | Medium | `05W`, evidence log, handoff and `10_NEXT` state P5 remains open until the final closure review gate. | Open |
| Final closure review is misused to execute P6 directly or generate a P6 task without a separate transition decision. | Governance / Stage Control | High | Medium | `05W` and `10_NEXT` state the final closure review may decide whether P5 can close but must not directly execute P6-P12. | Open |
| Evidence index rows are misread as promotion/ranking/Tenhou/LuckyJ permission. | Evaluation / Governance | High | Medium | `05W` marks promotion, ranking, Tenhou claim, LuckyJ claim and P6-P12 entry as `no` for every indexed artifact. | Open |

## 2026-06-04 — P5 closure criteria review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Closure criteria review is mistaken for P5 closure or P6-P12 entry approval. | Governance / Scope | High | Medium | `05V`, evidence log, handoff and `10_NEXT` state that the review can close but P5 remains open pending final handoff/evidence index finalization and final closure review. | Open |
| Finalization is used to sneak in production code, metric implementation, registry changes, CLI, latency measurement, model-output integration or real-data paths. | Scope / Engineering | High | Medium | The next task is docs-only finalization and explicitly forbids code, tests, fixtures, registry changes, promotion criteria changes, real data, model output, CLI, broad ingestion and P6-P12 work. | Open |
| Deferred later-stage items are reclassified as current blockers and cause P5 to extend indefinitely. | Planning / Scope | Medium-High | Medium | `05V` confirms deferred items are correctly classified and not blockers for current P5 finalization. | Open |

## 2026-06-04 — P5 closure criteria risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Closure criteria specification is mistaken for P5 closure or P6-P12 entry approval. | Governance / Scope | High | Medium | `05U`, evidence log and `10_NEXT` state P5 remains open until a closure review gate confirms readiness. | Open |
| Deferred items such as real data ingestion, model-output integration or latency measurement are treated as required blockers for current P5 closure. | Planning / Scope | Medium-High | Medium | `05U` separates required remaining P5 items from deferred later-stage items and records defer reasons. | Open |
| P5 closure review skips human review or ignores failing validation. | Governance / Quality | High | Low-Medium | `05U` lists final human review, passing tests and governance consistency as required before closure. | Open |

## 2026-06-04 — Evidence taxonomy and promotion guardrails review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Evidence taxonomy review is mistaken for permission to promote candidates, change promotion criteria or claim model strength from P5 synthetic/local diagnostics. | Governance / Evaluation | High | Medium | `05T` states the review is docs-only and not promotion criteria change, model-strength evidence, Tenhou evidence, stable-dan ranked-game evidence or LuckyJ comparison. | Open |
| P5 continues indefinitely through additional schema/review gates without defining closure criteria. | Planning / Scope | Medium-High | Medium | `05T`, handoff and `10_NEXT` set the next task to define P5 evaluation groundwork closure criteria and an exit readiness checklist. | Open |
| Evidence labels are treated as interchangeable and lose subtrack-specific meaning. | Documentation / Evaluation | Medium | Medium | `05T` records an evidence taxonomy table that separates stable-dan, legal-action, engineering, schema, implementation review, envelope review and registry review labels. | Open |

## 2026-05-30 — Metric registry consistency review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Metric registry consistency review is mistaken for permission to change registry code, implement future metrics or expand tiny benchmark diagnostics. | Scope / Governance | Medium-High | Medium | `05S` is docs-only and `10_NEXT` sets an evidence taxonomy / promotion guardrail review as the next P5-only task. | Open |
| Future tiny benchmark planning names such as latency percentiles are mistaken for current registered/emitted metrics. | Evaluation / Documentation | Medium-High | Medium | `05S` records these names as future fixture planning names only and not current envelope metrics. | Open |
| Direction values such as `higher_is_better = true` for `legal_action_rate` or `wrapper_smoke_success` are overclaimed as strength rankings. | Evaluation / Governance | High | Medium | `05S`, `05F` and evidence log state these are diagnostics only and not model-strength, Tenhou, stable-dan or LuckyJ evidence. | Open |

## 2026-05-30 — Tiny benchmark offline envelope coverage review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The envelope coverage review is mistaken for authorization to add new metrics, schema fields, production code or broader benchmark behavior. | Scope / Governance | High | Medium | `05R` closes only the current synthetic/local envelope representation and `10_NEXT` sets a registry-consistency review as the next P5-only task. | Open |
| `wrapper_smoke_success` or `sample_size = 1` is overclaimed as strength, Tenhou, stable-dan, latency or LuckyJ evidence. | Evaluation / Governance | High | Medium | `05R`, evidence log and ranking protocol state the evidence grade is offline envelope coverage review evidence only and not model-strength or LuckyJ comparison. | Open |
| The next registry review drifts into code changes or metric implementation. | Scope / Engineering | Medium-High | Medium | `10_NEXT` forbids production code, tests, fixtures, registry code changes, latency measurement, fixed-position exact-match, model-output integration and P6-P12 work. | Open |

## 2026-05-30 — Tiny benchmark harness implementation review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The implementation review is mistaken for authorization to expand the harness into model-output integration, CLI, real data or league behavior. | Scope / Governance | High | Medium | `05Q` closes only the current project-authored synthetic/local fixture scope and `10_NEXT` sets a P5 envelope-coverage review as the next task. | Open |
| `wrapper_smoke_success` is overclaimed as strength, Tenhou, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `05Q`, evidence log and ranking protocol state the evidence grade is implementation review evidence only and not model-strength or LuckyJ comparison. | Open |
| The next envelope review drifts into production code or metric expansion. | Scope / Engineering | Medium-High | Medium | `10_NEXT` forbids new production code, tests, fixtures, CLI, latency measurement, broad ingestion, model-output integration and P6-P12 work. | Open |

## 2026-05-30 — Tiny benchmark harness implementation risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The synthetic tiny benchmark harness is mistaken for a real benchmark harness or production evaluator. | Scope / Engineering | High | Medium | `05P` and tests state the harness loads only the fixed project-authored synthetic fixture and does not add CLI, broad ingestion, model output, real data, league or runner behavior. | Open |
| `smoke_success` is mistaken for model strength, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | The envelope warnings, `05P`, evidence log and ranking protocol state the result is P5 synthetic/local engineering diagnostic evidence only. | Open |
| The latency diagnostic plan is mistaken for measured latency or throughput. | Evaluation / Engineering | Medium-High | Medium | The harness validates plan shape only, stores `latency_ms = None` in the envelope and does not import timing APIs or measure latency. | Mitigated in implementation |
| Future work expands from the synthetic harness into model-output integration, real data, CLI or P6-P12. | Scope / Compliance | High | Medium | `10_NEXT` sets a review gate as the next task and forbids model output, real Tenhou, real haifu, external logs, platform data, CLI, broad ingestion, league, runner and P6-P12. | Open |

## 2026-05-30 — Tiny benchmark fixture schema review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The fixture schema review is mistaken for benchmark harness implementation readiness beyond synthetic/local scope. | Scope / Engineering | High | Medium | `05O` states the schema is only a front-door input boundary for a future P5-only synthetic/local harness and does not implement the harness. | Open |
| The next harness task expands into model-output integration, real data, CLI, league or runner behavior. | Scope / Compliance | High | Medium | `10_NEXT`, `05O` and the stage contract restrict the next task to the project-authored synthetic fixture and forbid model output, real Tenhou, real haifu, external logs, platform data, CLI, broad ingestion, league, runner and P6-P12 work. | Open |
| Fixture schema sufficiency is misread as model strength, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `05O`, evidence log and ranking protocol state the evidence grade is P5 synthetic/local fixture schema smoke evidence only, not model strength, Tenhou, stable-dan, LuckyJ or candidate promotion evidence. | Open |

## 2026-05-30 — Tiny benchmark harness fixture schema smoke risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The tiny benchmark fixture schema smoke test is mistaken for a benchmark harness implementation. | Scope / Engineering | High | Medium | Fixture/test docs state it validates shape only and does not add production code, harness, CLI, file ingestion, runner, league, model-output integration or latency measurement. | Open |
| The latency diagnostic plan is mistaken for measured benchmark results. | Evaluation / Engineering | Medium-High | Medium | The fixture contains plan fields only; the schema test rejects measured-result fields and does not import `time` or call timing APIs. | Mitigated in test |
| The fixed-position synthetic record is mistaken for supervised labels, policy quality or strength evidence. | Evaluation / Governance | High | Medium | Fixture interpretation and docs state fixed-position expectations are future diagnostics only, not supervised labels, policy-quality evidence, model-strength evidence or LuckyJ comparison. | Open |
| Future work jumps from schema smoke coverage into harness implementation, real data ingestion or model-output integration without review. | Scope / Compliance | High | Medium | `10_NEXT` sets a review gate as the next task and explicitly forbids benchmark harness implementation, real Tenhou, real haifu, external logs, model-output integration, CLI, broad file ingestion and P6-P12 work. | Open |

## 2026-05-30 — Tiny benchmark harness boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| A future tiny benchmark harness boundary is mistaken for harness implementation or production evaluator readiness. | Scope / Engineering | High | Medium | `05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md` states the task is docs-only and adds no harness, code, tests, fixtures, CLI, file ingestion, runner or league behavior. | Open |
| Legal-action rate, latency or fixed-position diagnostics are used as model strength or LuckyJ evidence. | Evaluation / Governance | High | Medium | `05N`, `05F`, evidence log and `10_NEXT` state these diagnostics are not model-strength evidence, Tenhou ranked evidence, stable-dan evidence, policy-quality evidence, candidate-promotion evidence or LuckyJ `10.68` comparison. | Open |
| A future schema smoke task expands into real Tenhou, real haifu, external logs, model-output integration or third-party binary paths. | Compliance / Scope | High | Medium | `05N` and `10_NEXT` restrict the next task to synthetic/local fixture schema smoke coverage and explicitly forbid real Tenhou, external data, Akochan binaries, model weights, CLI, runner, league and P6-P12 work. | Open |
| Latency diagnostics are misread as GPU, training, self-play or league throughput benchmarks. | Engineering / Evaluation | Medium-High | Medium | `05N` restricts latency to local offline synthetic/local evaluation code paths and requires environment, sample count, timing method and repetitions when implemented later. | Open |

## 2026-05-30 — Legal-action synthetic evaluator review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Current-scope completion is mistaken for complete real-game legal-action evaluation. | Evaluation / Governance | High | Medium | The review document states completion is only for P5 synthetic-only `dahai` + strict scope and lists remaining gaps for reach, calls, kan, hora, ryukyoku, red fives, tile notation and real model outputs. | Open |
| The next tiny benchmark task jumps directly into a runner, CLI or league implementation. | Scope / Engineering | High | Medium | `10_NEXT` sets a boundary-definition task before implementation and explicitly forbids runner, CLI, file ingestion, league, real Tenhou and external data. | Open |
| Synthetic legal-action coverage is used as model ranking or LuckyJ comparison evidence. | Evaluation / Governance | High | Medium | `05M`, evidence log and algorithm ranking protocol state this is diagnostic P5 smoke evidence only, not model-strength, Tenhou or LuckyJ evidence. | Open |

## 2026-05-30 — Synthetic legal-action parse-failure coverage risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The synthetic `parse_failure` fixture case is mistaken for expanded action support or a canonicalizer. | Evaluation / Scope | Medium-High | Medium | Docs state the case uses `dahai` plus `tsumogiri = null` only to exercise the strict parse-failure branch; current supported scope remains `dahai` + strict matching. | Open |
| Null or unknown `tsumogiri` is accidentally treated as acceptable strict matching input. | Evaluation / Data Quality | Medium-High | Medium | Evaluator tests expect the project fixture to count the null-`tsumogiri` record as `parse_failure`, not legal or invalid. | Mitigated in tests |
| Fixture labels such as `expected_future_outcome = parse_failure` are mistaken for evaluator output or model predictions. | Governance / Evaluation | Medium-High | Medium | Existing tests verify labels are not used for computation; docs repeat labels are future expectations only. | Mitigated in implementation |
| Synthetic legality diagnostics are overclaimed as Tenhou evidence, model strength evidence or LuckyJ 10.68 comparison. | Evaluation / Governance | High | Medium | Evidence log, docs and envelope warnings state synthetic-only, not Tenhou, not real haifu, not model strength evidence and not LuckyJ comparison. | Open |

## 2026-05-29 — Synthetic legal-action metric evaluator risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic legal-action rates are mistaken for model strength, Tenhou evidence or LuckyJ comparison. | Evaluation / Governance | High | Medium | Result warnings, docs and evidence log state synthetic-only, not Tenhou, not real haifu, not model strength evidence and not LuckyJ 10.68 comparison. | Open |
| The narrow fixture evaluator is expanded into broad file ingestion, model-output evaluation, CLI, runner or league behavior. | Scope / Engineering | High | Medium | Current implementation accepts an in-memory fixture mapping only; `10_NEXT` restricts the next task to synthetic parse-failure fixture coverage. | Open |
| Strict `dahai` comparison is treated as a full canonicalizer. | Engineering / Evaluation | Medium-High | Medium | Docs and tests state current comparison is only actor/action_type/tile/tsumogiri; no reach/calls/kans/red-five/tile-normalization support exists. | Open |
| `expected_future_outcome` labels leak into evaluator logic. | Evaluation / Test Quality | Medium-High | Low-Medium | Unit test mutates labels and verifies computed counts/rates do not change. | Mitigated in implementation |
| Zero-denominator cases fabricate `0.0` or `1.0` rates. | Evaluation / Data Quality | High | Low | `LegalActionMetricResult` requires all rates to be `None` when `evaluated_decision_count == 0`. | Mitigated in implementation |

## 2026-05-28 — v0.4 algorithm racing-funnel risks

| Risk | Severity | Mitigation |
|---|---|---|
| 完整训练所有候选算法导致算力和时间浪费。 | High | 使用 F0-F7 赛马漏斗，只有通过前一阶段的候选才能获得下一阶段资源。 |
| 不同候选使用不同评测环境，导致比较失真。 | High | 所有候选必须进入统一 Tenhou-like harness，记录规则、对手池、种子、样本量。 |
| 过早相信 repo 或论文强度声明。 | Medium-High | F0/F1 必须记录证据来源、可复现性和缺失证据；未核验前只能 Watch 或 ReferenceOnly。 |
| 只优化动作预测准确率，忽略四位率和 pt EV。 | High | 主指标固定为稳定段位、pt EV、平均顺位、四位率和南场避四。 |
| 早期小样本结果被误认为已经超过 LuckyJ。 | High | F7 之前不得声称超过 LuckyJ；必须报告样本量和 bootstrap confidence interval。 |

## 2026-05-28 — v0.5 documentation sync risks

| Risk | Severity | Mitigation | Status |
|---|---|---|---|
| `docs/10_next/10_NEXT.md` referenced missing `templates/prompts/09_ALGORITHM_RACING_FUNNEL.md`, which could block the next local Codex step. | Medium | Replaced the missing template reference with existing `docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md`. | Mitigated |

## 2026-05-28 — Mortal F1 audit risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Local shell cannot resolve `github.com` or `raw.githubusercontent.com`, blocking source clone and model artifact retrieval. | Infrastructure | High | High | Fix DNS/proxy/network configuration or provide an approved local source archive with recorded commit and checksum. | Open |
| Required runtime/build tools are missing locally: Rust/Cargo, Docker, conda and PyTorch. | Engineering | High | High | Choose one reproducibility path, either Docker or native build, then install only the minimal dependencies needed for F1 inference. | Open |
| Mortal model weights are not included in the repository and must be obtained separately. | Reproducibility | Medium-High | High | Record model source, version/tag, checksum, license/usage constraints and exact config before running inference. | Open |
| Mortal code is AGPL-3.0-or-later, which may affect future integration, service deployment or redistribution. | License | Medium | Medium | Keep F1/F2 local research-only until license review confirms integration obligations. | Open |

## 2026-05-28 — Mortal F1 blocker-resolution risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Mortal source tarball can be retrieved only through explicit host resolution while normal system DNS and normal `git clone` remain unreliable. | Infrastructure | Medium | High | Keep recorded source tarball checksum for audit, but fix system DNS/proxy before treating source access as reproducible. | Open |
| Official Mortal trained model appears unavailable for public local inference; README-linked gist says there is currently no plan to release trained parameters. | Reproducibility | High | High | Require a lawful user-provided artifact with version, usage constraints and checksum, or pause Mortal as runnable baseline and move to another F1 baseline. | Open |
| Installing Rust through Homebrew is blocked by inability to resolve `formulae.brew.sh`. | Engineering | Medium | High | Fix DNS/proxy or use an approved offline/local toolchain; avoid broad dependency installation until model artifact path is decided. | Open |

## 2026-05-29 — Technical-plan-first risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Web-side research conclusions drift away from local Git/docs state. | Governance | High | Medium | Treat Git + docs as the only source of truth; require Codex to land decisions in docs before execution. | Open |
| Paper-first narrative causes premature claims or stage skipping. | Research | High | Medium | Use `12A_TECHNICAL_PLAN_v0.1.md` as execution charter; paper remains a future summary only. | Open |
| Main route becomes too broad and consumes resources before funnel gates. | Planning | Medium-High | Medium | Keep baseline racing funnel and `10_NEXT` single-task rule; do not train or scale until gates justify it. | Open |
| LuckyJ is mistakenly treated as a full-reproduction target instead of benchmark line. | Research | Medium | Medium | Keep LuckyJ role documented as target benchmark, not implementation seed or direct full-reproduction object. | Open |

## 2026-05-29 — Mortal runnable-baseline pause risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Unknown Mortal weight files such as `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` are mistaken for usable project artifacts. | Reproducibility / Governance | High | Medium | Do not use unknown model artifacts. Any future Mortal artifact must record source, version/tag, usage constraints and checksum before F1 can be re-opened. | Open |
| Pausing Mortal leaves the project without a runnable local baseline until another candidate passes F1. | Planning | Medium | High | Move the next baseline F1 audit to Akochan and keep the audit limited to repository, license, dependency, artifact and minimal-run viability. | Open |
| Mortal reference code is accidentally treated as evidence of runnable strength. | Evaluation | Medium-High | Medium | Keep Mortal labeled as source-code, mjai-interface, methodology and engineering reference only; do not promote to F2 or claim strength without runnable evidence. | Open |

## 2026-05-29 — Akochan F1 audit risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Akochan license is a custom Japanese usage agreement rather than a standard open-source license. | License / Compliance | High | High | Restrict current use to private research audit; get legal/Web ChatGPT Pro review and likely author permission before redistribution, AI-part modification, commercial use or public release. | Open |
| Local macOS ARM build is blocked by missing or incompatible LLVM/OpenMP/Boost toolchain. | Engineering | High | High | Use a supported Linux build environment with `g++`, Boost and OpenMP, or install/verify Homebrew LLVM/OpenMP/Boost before retrying F1 build. | Open |
| Normal `git clone` still depends on unreliable local GitHub DNS. | Infrastructure | Medium | High | Fix DNS/proxy or document explicit host-resolution only as a temporary audit workaround; do not treat source access as fully reproducible until normal clone works. | Open |
| Akochan exposed promising JSON/legal-action/mjai surfaces before any minimal run had succeeded. | Reproducibility | High | High | Require successful `legal_action` and/or `mjai_log` evidence before F2. | Mitigated by GitHub Actions run `26617347785`; local macOS remains blocked |
| Repository-included `params/` text files are necessary runtime artifacts and may be mistaken for code-only dependency. | Reproducibility / Data | Medium | Medium | Treat `params/` as required artifacts tied to commit `53188a0b926fbab38177f88c3cd87d554cf412af`; record checksums if separated from the repository. | Open |

## 2026-05-29 — Akochan F1 blocker-resolution risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Preferred Docker Linux build path is unavailable because Docker is not installed. | Infrastructure / Engineering | High | High | Provision Docker or another approved temporary Linux environment outside the repository before retrying F1. | Open |
| Homebrew reports formula prefixes but the expected LLVM/Boost/OpenMP files are absent. | Engineering | High | High | Verify or reinstall Homebrew LLVM, Boost and libomp explicitly before using the macOS build path; do not run global installs without user approval. | Open |
| Repeated F1 attempts may leave external temporary clone/build directories behind. | Hygiene | Low | Medium | Keep all third-party source in `/tmp` or `../_external`, record paths, and clean temporary clones after evidence is captured. | Open |

## 2026-05-29 — Akochan GitHub Actions build-audit risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| GitHub Actions workflow succeeds in Ubuntu but local macOS remains unable to build Akochan. | Reproducibility | Medium | Medium | Treat a successful workflow as Ubuntu-runner evidence only; record runner OS, commit and commands before deciding F1 status. | Open |
| Workflow logs may include too much third-party output. | Governance | Low | Medium | Workflow writes short summaries with `head -c` limits for sample output and uploads no artifacts. | Open |
| A workflow definition may be mistaken for successful F1 evidence before it is run. | Governance / Evaluation | High | Medium | Keep candidate status tied to actual workflow run IDs and logs, not workflow existence. | Mitigated by successful run `26617347785` |
| GitHub workflow syntax/context errors can block F1 before any Ubuntu build starts. | Infrastructure / Governance | Medium | Medium | Record failed workflow run IDs, fix workflow validation issues locally, and do not count failed validation runs as build evidence. | Mitigated by fix and successful run `26617347785` |
| GitHub Actions `actions/checkout@v4` currently emits a Node.js 20 deprecation warning. | Infrastructure / Maintenance | Medium | Medium | Track the warning and update workflow action/runtime before GitHub removes Node.js 20 support. | Open |
| Akochan F1 evidence is Ubuntu-runner evidence, not local macOS reproducibility. | Reproducibility | Medium | High | Treat F1 as Conditional Pass; keep local macOS build blocked unless Docker or verified Homebrew LLVM/Boost/OpenMP is added later. | Open |

## 2026-05-29 — Akochan F2 interface risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| F2 wrapper accidentally vendors or stores Akochan source, `system.exe`, `libai.so`, `params/` or third-party build artifacts. | License / Governance | High | Medium | Keep wrapper-only boundary; use external path or GitHub Actions temporary directory; add checks that fail if third-party artifacts are added to the repository. | Open |
| F2 implementation drifts from fixed samples into self-play, match, training or real Tenhou commands. | Scope / Compliance | High | Medium | Limit next task to fixed `legal_action` and `mjai_log` samples; audit log must record training/self-play/Tenhou flags as false. | Open |
| Akochan custom license is misunderstood as a standard open-source license. | License / Compliance | High | High | Keep private/internal audit only; require license review or author permission before modification, redistribution, commercial use or public release. | Open |
| Legal-action checker output is mistaken for playing strength evidence. | Evaluation | Medium-High | Medium | Label F2 as interface/legal-action only; do not claim model strength without F3+ evaluation evidence. | Open |
| Wrapper output schema may over-normalize and lose raw mjai/Akochan fields. | Engineering | Medium | Medium | Preserve raw output in `raw` and require parseable JSON plus output hashes. | Open |

## 2026-05-29 — Akochan F2 wrapper skeleton risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Fake-executable smoke tests are mistaken for real Akochan compatibility or strength evidence. | Evaluation / Governance | High | Medium | Document fake executable as a test substitute only; require a separate run against real externally built `system.exe` before claiming real compatibility. | Open |
| The wrapper can call an external executable path, so a wrong local path could point to an unaudited binary. | Reproducibility / Security | Medium-High | Medium | Require explicit `system_exe` or `AKOCHAN_SYSTEM_EXE`, record external commit/build environment in audit logs, and avoid unknown binaries or artifacts. | Open |
| Real Ubuntu-built `system.exe` may produce output that differs from the fake executable shape. | Engineering | Medium | Medium | Preserve raw stdout, keep parse warnings, and make the next task a fixed-sample real `system.exe` validation without artifact upload. | Open |
| The initial wrapper skeleton may be expanded too quickly into broad adapter, match, league or Tenhou integration work. | Scope / Compliance | High | Medium | Keep `10_NEXT` on the single real fixed-sample validation step; no self-play, match, training or Tenhou commands. | Open |

## 2026-05-29 — Akochan F2 real-exe workflow risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The real-exe workflow definition is mistaken for successful real `system.exe` compatibility evidence before it is run. | Governance / Evaluation | High | Medium | Keep candidate status tied to successful run IDs and logs. | Mitigated by successful run `26629344590` for fixed-sample wrapper validation |
| Workflow logs could expose too much third-party build output or sample stdout. | Governance | Low-Medium | Medium | Write only short summaries to GitHub Step Summary and do not upload artifacts. | Open |
| GitHub Actions temporary build succeeds but local macOS remains unable to run real Akochan. | Reproducibility | Medium | High | Treat evidence as Ubuntu-runner compatibility only; keep local macOS build limits documented. | Open |
| Real `mjai_log` stdout may be newline-delimited JSON, another multi-record JSON stream or an allowlisted mixed stream rather than a single JSON document. | Engineering | Medium | Medium | Wrapper supports strict JSON streams plus exactly the allowlisted `calculating review` status line. | Mitigated by successful run `26629344590` |
| The workflow accidentally persists third-party source or binaries. | License / Governance | High | Low | Use runner temp directories only and do not configure artifact upload or caches for Akochan outputs. | Open |
| Akochan `system.exe` depends on runtime config files such as `setup_mjai.json` being visible from the process working directory. | Engineering / Reproducibility | Medium-High | High | Wrapper uses explicit `working_dir`, `AKOCHAN_WORKING_DIR` or default executable directory as subprocess cwd; workflow sets runner-temp `AKOCHAN_WORKING_DIR`. | Mitigated by successful runs `26623247276` and `26629344590` |

## 2026-05-29 — Akochan F2 working-directory fix risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Local fake tests may pass while real Akochan still needs additional runtime files or cwd assumptions beyond `setup_mjai.json`. | Engineering / Reproducibility | Medium | Medium | Rerun `Akochan F2 Wrapper Real Exe Audit` against the Ubuntu-built real `system.exe` and record the run ID/logs before closing F2 real-exe compatibility. | Mitigated for fixed samples by successful run `26629344590` |
| `AKOCHAN_WORKING_DIR` could point to a directory that does not match the audited executable or commit. | Reproducibility / Governance | Medium | Medium | Require explicit environment setup in workflow, record `working_dir` in every audit log, and keep external commit/build environment in the audit record. | Open |

## 2026-05-29 — Akochan F2 real mjai_log parser risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Real `mjai_log` stdout is multi-record or mixed-format output that the current wrapper parser cannot represent. | Engineering / Reproducibility | Medium-High | High | Parser preserves raw stdout, records parsed records and warnings, supports strict JSON streams plus exactly `calculating review`, and raises bounded diagnostics on residue. | Mitigated for fixed samples by successful run `26629344590` |
| Parser fixes could silently discard non-JSON lines that matter for reproducibility or debugging. | Governance / Engineering | Medium | Medium | Strict parser rejects partial parses and unknown non-JSON lines, reports bounded stdout summaries, stdout SHA256, failure position and parsed-record count; keep raw stdout on success. | Mitigated for fixed samples by successful run `26629344590`; keep open for broader outputs |

## 2026-05-29 — Akochan F2 allowlisted mixed stdout parser risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Allowlisting a non-JSON `mjai_log` status line could accidentally hide unexpected runtime output. | Governance / Engineering | Medium-High | Medium | Only the exact line `calculating review` is allowlisted; every other non-JSON line still raises `AkochanOutputParseError` with bounded diagnostics and stdout SHA256. | Mitigated for fixed samples by successful run `26629344590`; keep open for broader outputs |
| The real `mjai_log` output may contain additional known status lines not covered by local fake tests. | Engineering / Reproducibility | Medium | Medium | Rerun the real-exe workflow and add only specific, reviewed status lines if logs prove they are necessary and safe. | Open |
| Local parser tests may pass while the real GitHub Actions output still has an unmodeled stdout shape. | Reproducibility | Medium | Medium | Require run ID/log review before closing F2 real-exe compatibility. | Mitigated by successful run `26629344590` for fixed samples |

## 2026-05-29 — Akochan F2 closeout risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Fixed-sample wrapper validation is mistaken for Akochan or mjlabai strength evidence. | Evaluation / Governance | High | Medium | Label run `26629344590` as fixed-sample integration evidence only; require F3+ offline/evaluation evidence before any strength claim. | Open |
| Akochan is expanded into broader evaluator/reviewer integration without rechecking license boundaries. | License / Scope | High | Medium | Keep Akochan at private/internal audit boundary; create a separate task and require Web/legal review before modification, redistribution, commercial use or public release. | Open |
| GitHub Actions Node.js 20 deprecation warning later breaks the workflow even though current F2 validation passed. | Infrastructure / Maintenance | Medium | Medium | Track workflow action/runtime updates; warning does not affect run `26629344590` but should be addressed before relying on repeated CI. | Open |

## 2026-05-29 — Stable-dan calculator risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| A deterministic stable-dan point estimate is mistaken for statistically reliable strength evidence. | Evaluation / Governance | High | Medium | Label the calculator as point-estimate infrastructure only; require bootstrap confidence intervals and sample-size reporting before comparing against LuckyJ. | Mitigated by bootstrap CI implementation; threshold helper still needed |
| `fourth_count == 0` is misreported as infinite or superior strength. | Evaluation | High | Medium | Calculator raises `StableDanUndefinedError` when `fourth_count` is zero. | Mitigated in implementation |
| Room aliases or weights are applied to the wrong Tenhou room. | Evaluation | Medium-High | Medium | Canonicalize supported room aliases and expose formula weights in `StableDanResult` for audit. | Open |

## 2026-05-29 — Stable-dan bootstrap CI risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Bootstrap lower/upper bounds are mistaken for proof that a model beats LuckyJ without an explicit threshold decision rule. | Evaluation / Governance | High | Medium | Next task is a threshold comparison helper using the bootstrap lower bound against LuckyJ 10.68. | Open |
| High undefined-resample rate makes the CI unstable or misleading. | Evaluation | Medium-High | Medium | `StableDanBootstrapResult` reports `undefined_resamples` and `undefined_rate`; docs require treating high undefined rate as unreliable. | Open |
| Bootstrap resamples with zero fourth-place count are silently converted to infinite stable dan. | Evaluation | High | Low | Implementation skips and counts undefined resamples; if all resamples are undefined, it raises `StableDanBootstrapUndefinedError`. | Mitigated in implementation |

## 2026-05-29 — Stable-dan threshold comparison risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| A helper outcome of `clear_pass` is treated as a full model-strength claim without sample-size and reporting context. | Evaluation / Governance | High | Medium | Next task defines minimum sample-size and reporting schema before project-level LuckyJ comparison claims. | Open |
| Point estimate above LuckyJ 10.68 is mistaken for a threshold pass. | Evaluation | High | Medium | Helper returns `point_estimate_only` with `clears_threshold=False` when lower bound does not exceed threshold. | Mitigated in implementation |
| High undefined rate is ignored when threshold lower bound looks strong. | Evaluation | Medium-High | Medium | Helper returns `unreliable` and `clears_threshold=False` when `undefined_rate > max_undefined_rate`. | Mitigated in implementation |

## 2026-05-29 — Stable-dan reporting schema risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Internal sample-size guardrails are mistaken for Tenhou official standards or statistical proof. | Governance / Evaluation | Medium-High | Medium | Report source note and docs label them as project-internal governance defaults only. | Open |
| A report with `clears_threshold=True` but insufficient sample size is used as a LuckyJ claim. | Evaluation / Governance | High | Medium | Report separates `clears_threshold` from `can_enter_threshold_review`; low sample adds a warning note. | Mitigated in implementation |
| Future callers feed inconsistent threshold comparison and bootstrap results into the report. | Engineering / Evaluation | Medium | Medium | Report builder validates matching point estimate, bounds, confidence level and resample counts before building a report. | Mitigated in implementation |

## 2026-05-29 — Stable-dan placement aggregation risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Placement input aliases are over-expanded and accidentally accept ambiguous or zero-based values. | Evaluation / Data Quality | Medium-High | Medium | Aggregator accepts only explicit `1`/`2`/`3`/`4` values and a small whitelist of aliases; zero-based, bool, float and unknown strings fail. | Mitigated in implementation |
| Placement aggregation helper is mistaken for a league harness or real Tenhou ingestion path. | Scope / Compliance | High | Medium | Document helper as offline input preparation only; it does not read accounts, platform data, logs, Tenhou, league or match runner outputs. | Open |
| Bad placement records are silently skipped, biasing stable-dan counts. | Evaluation / Data Quality | High | Medium | Missing keys, invalid records and invalid placements raise clear errors instead of being skipped. | Mitigated in implementation |
| Aggregated placement counts are used as strength evidence without bootstrap, threshold and sample-size report context. | Evaluation / Governance | High | Medium | Require composition with stable-dan calculator, bootstrap CI, threshold helper and reporting schema before any threshold review. | Open |

## 2026-05-29 — Stable-dan smoke fixture risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic smoke fixture output is mistaken for a model result or LuckyJ evidence. | Evaluation / Governance | High | Medium | Fixture and docs label it as synthetic-only code-path validation; report notes still say not model-strength evidence and not a Tenhou ranked result. | Open |
| A smoke test becomes a hidden CLI, file-ingestion path or league harness. | Scope | Medium-High | Medium | Keep the smoke test under `tests/`; it reads only the checked-in synthetic fixture and writes no output files. | Mitigated in implementation |
| The 100-record synthetic sample is treated as threshold-review ready. | Evaluation / Governance | High | Medium | Test asserts `can_enter_threshold_review=False` because the sample is below the project-internal `1000` game threshold-review minimum. | Mitigated in implementation |

## 2026-05-29 — Stable-dan API documentation risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Documentation examples drift from the actual Python API signature. | Documentation / Engineering | Medium | Medium | The API doc was written against the current `build_stable_dan_evaluation_report(...)` signature and notes that model/dataset metadata is not yet part of the report schema. | Open |
| API documentation is mistaken for an endorsement to build CLI or ingestion tooling. | Scope | Medium-High | Medium | Docs explicitly say API-only, no CLI, no file ingestion path, no league and no Tenhou integration. | Open |
| Synthetic example documentation is mistaken for strength evidence. | Evaluation / Governance | High | Medium | Docs label the fixture as synthetic only and repeat that point estimate, bootstrap, threshold and report examples are not model-strength evidence. | Open |

## 2026-05-29 — Stable-dan groundwork review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Stable-dan subtrack current-scope completion is mistaken for full P5 completion. | Governance / Planning | High | Medium | `05I_STABLE_DAN_GROUNDWORK_REVIEW.md` explicitly says only the stable-dan subtrack is complete and P5 overall remains open. | Open |
| Stable-dan groundwork completion is mistaken for model-strength or LuckyJ evidence. | Evaluation / Governance | High | Medium | The review document repeats that there are no real model samples, no Tenhou ranked results and no final LuckyJ proof. | Open |
| The next metric-registry task expands into league, training or external-data ingestion. | Scope | High | Medium | `10_NEXT.md` limits the next task to P5 offline metric registry and result envelope schema; no league, training, self-play, Tenhou or P6-P12. | Open |

## 2026-05-29 — Offline evaluation result envelope schema risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Registry placeholder metrics are mistaken for implemented evaluators. | Evaluation / Governance | Medium-High | Medium | `05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md` labels legal-action, invalid-action, parse-success and latency metrics as schema placeholders unless separate evaluator tasks implement them. | Open |
| Result envelope is mistaken for a runner or evidence generator. | Scope | High | Medium | The schema records results only; docs and tests confirm it does not run commands, read data, train, self-play, league or connect to Tenhou. | Open |
| High-risk safety flags are ignored in downstream reports. | Governance | Medium | Medium | Envelope preserves safety flags and adds warnings when high-risk flags are true. | Open |

## 2026-05-29 — Offline envelope smoke fixture risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic envelope smoke result is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | The smoke test and evidence log label the input as synthetic-only and not strength evidence. | Open |
| Envelope smoke test is mistaken for a CLI, runner or data-ingestion path. | Scope | Medium-High | Medium | The test constructs an envelope in-process, writes no output files and reads only the checked-in synthetic fixture. | Open |
| Legal-action / invalid-action placeholder metrics are used before precise metric denominators are defined. | Evaluation | Medium-High | Medium | `05K_LEGAL_ACTION_METRIC_SPEC.md` now defines denominator rules; next task should define canonical action fixture schema before implementation. | Mitigated for metric definitions; canonical schema remains open |

## 2026-05-29 — Legal-action metric specification risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| `legal_action_rate` is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | `05K_LEGAL_ACTION_METRIC_SPEC.md` states that legality is necessary but not sufficient and cannot support LuckyJ comparison by itself. | Open |
| Parse failures or missing actions are incorrectly counted as invalid actions without explicit mode. | Evaluation / Metric Definition | Medium-High | Medium | The spec separates `invalid_action_count`, `parse_failure_count` and `missing_action_count`; strict-mode changes must be explicit future work. | Open |
| Skipped records silently hide denominator problems. | Evaluation / Data Quality | Medium-High | Medium | The spec requires skipped records to be excluded from denominator but reported through `skipped_count` and skipped categories. | Open |
| Canonical action matching is implemented inconsistently across future fixtures. | Engineering / Evaluation | Medium-High | Medium | `05L_ACTION_CANONICALIZATION_SCHEMA.md` now defines canonical fields and strict `dahai` matching before evaluator implementation. | Mitigated for schema; fixture smoke test remains open |

## 2026-05-29 — Action canonicalization schema risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The schema is mistaken for an implemented canonicalizer. | Scope / Engineering | Medium-High | Medium | `05L_ACTION_CANONICALIZATION_SCHEMA.md` explicitly says it is documentation only and no parser/canonicalizer was implemented. | Open |
| Strict matching rejects valid future representations when `tsumogiri` or tile notation differs across tools. | Evaluation / Compatibility | Medium | Medium | The schema records strict mode as default and leaves relaxed modes / tile normalization as explicit future tasks. | Open |
| Future fixture authors use real Tenhou or external logs as shortcut data. | Compliance / Data | High | Medium | The schema says the first fixture must be synthetic/local only; no Tenhou, external logs, platform data or strength evidence. | Open |
| Edge cases such as reach, calls, kans and red fives are underspecified for implementation. | Evaluation / Engineering | Medium | Medium | The schema records them as future edge cases; next tasks should start with minimal `dahai` fixture smoke tests before broader actions. | Open |

## 2026-05-29 — Synthetic legal-action fixture schema smoke risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| `expected_future_outcome` labels are mistaken for actual evaluator output. | Evaluation / Governance | High | Medium | The fixture and test docstring label outcomes as future labels only; the test does not compute legal/invalid rates or canonical equality. | Open |
| Schema smoke test is mistaken for a legal-action evaluator. | Scope / Engineering | High | Medium | Keep the task limited to JSON shape validation; define an explicit evaluator boundary before implementation. | Open |
| Synthetic fixture is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | Fixture/source notes and evidence log state synthetic-only, not Tenhou, not model output and not strength evidence. | Open |
| Dahai-only fixture scope hides future edge cases for reach, calls, kans and red fives. | Evaluation / Engineering | Medium | Medium | Keep `dahai` as the minimum smoke scope and require separate tasks for broader canonicalization and evaluator behavior. | Open |

## 2026-05-29 — Synthetic legal-action evaluator boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The future synthetic evaluator expands from fixture-only code into a broad evaluator, file ingestion path or runner. | Scope / Engineering | High | Medium | `05K_LEGAL_ACTION_METRIC_SPEC.md` limits the next implementation to the project-authored synthetic fixture and requires a separate boundary change before broader inputs. | Open |
| Synthetic legal-action rates are mistaken for model-strength evidence or LuckyJ comparison. | Evaluation / Governance | High | Medium | Boundary warnings require synthetic-only, not Tenhou data, not real haifu, not strength evidence and not LuckyJ comparison. | Open |
| Future implementation accidentally reads real Tenhou, external logs or platform data. | Compliance / Data | High | Medium | Boundary explicitly forbids real Tenhou, real haifu, platform data, online accounts and external logs. | Open |
| Future implementation silently fabricates rates when `evaluated_decision_count == 0`. | Evaluation / Data Quality | High | Low-Medium | Boundary requires all rates to be undefined when denominator is zero and preserves the count invariant. | Open |
| Future implementation treats `expected_future_outcome` as authoritative evaluator output. | Evaluation / Governance | Medium-High | Medium | Boundary states labels are smoke expectations only and not model predictions, evaluator output or strength evidence. | Open |
