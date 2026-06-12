# 03W Full P7 Closure Roadmap And Remaining Scope Inventory After Current-Scope Closure

## Scope

This document defines the full P7 closure roadmap and remaining scope
inventory after P7 current-scope closure.

This is docs-only roadmap / inventory definition. It does not close full P7,
approve broader P7 implementation, approve training, approve source ingestion,
approve parser / dataset reader / ingestion, approve actual feature
extraction, approve actual label generation, approve supervised dataset
construction, approve model architecture / trainer, approve real data, approve
model-output integration or approve P8-P12 entry.

## Current-Scope Closure Context

P7 current scope is already closed only for the exact current scope:

- docs-only supervised-learning readiness chain.
- accepted minimal synthetic/local supervised feature-label smoke
  implementation.
- direct docs/governance synchronization.

Accepted current-scope implementation artifacts are limited to:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`

That accepted scope validates only in-memory JSON-safe synthetic/local smoke
mappings, candidate feature/label family names, public-information-only
placeholder fields and non-evidence guardrails. It is not a parser, dataset
reader, ingestion path, actual feature extractor, actual label generator,
training dataset, model architecture, trainer or strength evaluation.

## Full P7 Remaining Scope Inventory

| item | category | current_status | required_before_full_p7_closure | blocker | evidence_needed | notes |
|---|---|---|---:|---|---|---|
| Broader P7 scope / entry criteria / first task | required | not defined after current-scope closure | yes | full-P7 inventory must be reviewed first | docs-only scope definition and review | Must happen before broader implementation. |
| Broader P7 data/source readiness | required | only candidate categories inventoried in `03G`/`03H` | yes | no source approved for training or ingestion | source readiness update and review | Inventory is not source approval. |
| Source-specific approval decision | required | none approved | yes | source rights, privacy, platform and storage status unresolved | source id, rights, allowed use, storage policy, human/Web approval | Any real/external source remains blocked until separate approval. |
| Parser / reader / ingestion boundary | required | unapproved | yes if any data path is used | no approved source and no boundary | boundary doc, review, approval decision | Synthetic-only tasks may explicitly state parser/reader/ingestion are not required. |
| Actual feature extraction implementation boundary | required | boundary prerequisites defined in `03I`/`03J`; implementation unapproved | yes | no source/parser/ingestion approval and no implementation proposal | feature schema, public-info policy, leakage checks, review | Must preserve decision-time public information only. |
| Actual label generation implementation boundary | required | boundary prerequisites defined in `03I`/`03J`; implementation unapproved | yes | no label source approval and no label policy | label source policy, label version, leakage checks, review | Labels from unapproved real data/model output/self-play/league remain forbidden. |
| Supervised dataset construction policy | required | not defined | yes | source, feature and label approvals missing | dataset id, provenance, storage policy, inclusion/exclusion policy | Must separate smoke fixtures from training data. |
| Train / validation / test split policy | required | not defined | yes | no dataset construction policy | split strategy, grouping, temporal/source leakage checks | Must prevent same-game, source and near-duplicate leakage. |
| Leakage prevention policy | required | partially bounded in `03I`/`03K`; not full policy | yes | no full data path | hidden-info, future-info and split leakage policy | Highest risk for supervised learning. |
| Model architecture / trainer planning | required | unapproved | yes before training | no dataset/source/features/labels approved | architecture/trainer proposal, config, validation plan | Planning only; no dataloader, optimizer, loss or trainer code now. |
| Training evidence requirements | required | taxonomy defined in `03K`; no training evidence exists | yes | no training approval | source, config, seed, logs, artifact checksums, validation commands | Training-run evidence would still not be Tenhou or LuckyJ evidence by itself. |
| Evaluation dependency requirements | required | P5/P6 context exists; P7-specific dependency map not full-closure ready | yes | no trained model or dataset | metric protocol, offline envelope, sample-size/uncertainty policy | P7 outputs must remain tied to approved evaluation evidence. |
| P7 final full closure criteria | required | not defined | yes | roadmap/inventory not yet reviewed | C-list criteria, exit checklist, non-entry conditions | Later docs-only criteria task after roadmap review. |
| P7 full closure review | required | not run | yes | full-P7 criteria and approved work incomplete | final review document, validation results, governance sync | Only after all approved full-P7 work is complete. |
| Additional supervised fixtures | deferred | not approved beyond minimal smoke fixture | maybe | depends on future scope | fixture boundary, schema smoke test, review | Synthetic/local only unless later approved. |
| Project-authored synthetic/local expansion | deferred | possible future smoke path only | maybe | needs explicit first `10_NEXT` task | proposal, exact files, validation commands | Not training data by default. |
| Model-output integration | deferred | unapproved | no for current roadmap | no policy | model-output boundary, provenance and review if ever proposed | Cannot be label source now. |
| CLI or broad file ingestion | deferred | unapproved | no | scope creep risk | separate boundary and approval if ever needed | Not needed for current docs-only planning. |
| Real Tenhou | blocked | not approved | no until lawful source approval | platform / privacy / account risk | compliance, source rights, storage and no-account-risk review | No Tenhou access, scraping or automation. |
| Real haifu | blocked | not approved | no until source approval | rights/provenance unresolved | source approval, storage policy, parser boundary | Do not read or ingest now. |
| External logs | blocked | not approved | no until source approval | rights/provenance/privacy unresolved | source approval, storage policy, parser boundary | Do not read or ingest now. |
| Platform data | blocked | not approved | no until compliance approval | platform terms, privacy, account/session risk | lawful compliance and privacy review | No account/session/cookie/token handling. |
| Third-party binaries / weights / params / checkpoints | blocked | not approved | no | artifact provenance and license risk | lawful artifact review, checksum, usage constraints | Do not download, vendor, save or use now. |
| Self-play | later_stage | unapproved | no for P7 closure roadmap | P8 not approved | P8 transition review and scope | Belongs to P8, not current P7. |
| League / runner | later_stage | unapproved | no for P7 closure roadmap | P10 not approved | P10 transition review and scope | Not current P7. |
| P8 RL | later_stage | unapproved | no | full P7 not closed | P8 transition review after P7 conditions | No P8 execution now. |
| P9 search / risk model | later_stage | unapproved | no | P8/P9 not reached | P9 transition review | Not current P7. |
| P10 model league | later_stage | unapproved | no | P10 not reached | P10 transition review | Not current P7. |
| P11 large-scale training | later_stage | unapproved | no | P7/P8/P10 evidence missing | P11 transition review | Not current P7. |
| P12 Tenhou target validation | later_stage | unapproved | no | P12 not reached | P12 protocol and compliance review | Final target validation only. |
| Model-strength evidence | out_of_scope | none | no | no approved model/evaluation evidence | later approved evaluation/league/Tenhou evidence | Current P7 docs/smoke artifacts cannot support it. |
| LuckyJ comparison | out_of_scope | none | no | no P12/approved comparison evidence | explicit comparison protocol and sufficient evidence | No LuckyJ `10.68` claim from P7 roadmap. |
| Candidate promotion | out_of_scope | none | no | no racing-funnel evidence | approved funnel gate evidence | No promotion from roadmap/smoke evidence. |

## Required Items

The following are required before full P7 closure can be considered:

1. Broader P7 scope / entry criteria / first task definition and review.
2. Broader P7 data/source readiness update and review.
3. Source-specific approval decision for any source used beyond docs/smoke
   context.
4. Parser / reader / ingestion boundary before any data path.
5. Feature extraction implementation boundary before feature code.
6. Label generation implementation boundary before label code.
7. Supervised dataset construction policy.
8. Train / validation / test split policy.
9. Leakage prevention policy covering hidden information, future information
   and split leakage.
10. Model architecture / trainer planning before any training code.
11. Training evidence requirements before any training run can be interpreted.
12. Evaluation dependency requirements for any P7 output.
13. Full P7 closure criteria.
14. Final full P7 closure review after approved work is complete.

All are currently incomplete for full P7.

## Deferred Items

The following are deferred rather than current blockers for this roadmap
definition:

- additional synthetic/local supervised fixtures.
- project-authored synthetic/local expansion beyond the accepted smoke path.
- model-output integration.
- CLI.
- broad file ingestion.
- broader implementation proposal preparation after roadmap review.

Deferred does not mean approved. Each item needs a later first `10_NEXT` task,
scope, review and approval before implementation.

## Blocked Items

The following are blocked until separate approval:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token handling.
- real-data parser / reader / ingestion.
- source-specific training data approval.
- third-party binaries, weights, params, checkpoints or snapshots.

## Later-Stage Items

The following belong to later stages and cannot be used to close full P7 now:

- self-play.
- league.
- P8 reinforcement learning.
- P9 search / risk model.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou target validation.

## Out-Of-Scope / Non-Evidence Items

This roadmap and inventory are not evidence of:

- model strength.
- Tenhou ranked performance.
- stable-dan ranked-game performance.
- LuckyJ `10.68` comparison.
- candidate promotion.
- supervised policy quality.
- training-data approval.
- real-data approval.
- P8-P12 entry approval.

## Roadmap Toward Full P7 Closure

Conservative full-P7 roadmap:

1. Review full P7 closure roadmap and remaining scope inventory.
2. Define broader P7 scope / entry criteria / first task before implementation.
3. Review broader P7 scope / entry criteria / first task.
4. Define broader P7 data/source readiness and source approval boundary.
5. Define parser / reader / ingestion boundary before implementation.
6. Define actual feature extraction / label generation implementation proposal
   boundary.
7. Prepare approval decision for a narrow broader P7 implementation task only
   if source, parser/reader/ingestion, feature/label, leakage, evidence and
   risk boundaries are sufficient.
8. Continue only after explicit approval through the first unchecked
   `docs/10_next/10_NEXT.md` task.
9. Later define full P7 closure criteria.
10. Run final full P7 closure review only after all approved work is complete
    and validation/governance evidence is synchronized.

This roadmap is intentionally docs-first. It does not authorize direct
implementation.

## Why Not Broader Implementation Yet

Broader P7 implementation cannot start now because:

- no training source is approved.
- source ingestion is unapproved.
- parser / reader / ingestion are unapproved.
- actual feature extraction is unapproved.
- actual label generation is unapproved.
- supervised dataset construction is unapproved.
- split and leakage policies are not full-P7 ready.
- model architecture, dataloader, optimizer, loss and trainer are unapproved.
- real data and model-output integration are unapproved.
- current-scope closure does not approve broader implementation.

## Why Not P8-P12 Yet

P8-P12 cannot start now because:

- full P7 is not closed.
- no approved P7 training exists.
- no P7 model-strength evidence exists.
- no P7 supervised model candidate is ready for RL, search, league or Tenhou
  validation.
- each later stage requires separate transition review, scope, entry criteria,
  risk/evidence taxonomy and first-task approval.

## Validation Commands

Validation commands for this docs-only roadmap task:

```text
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Planning Decision

```text
Full P7 closure roadmap and remaining scope inventory are defined after
current-scope closure.
P7 current scope is closed only for the exact current scope.
Full P7 remains open.
Broader P7 implementation, training, source ingestion, parser / reader /
ingestion, actual feature extraction, actual label generation, supervised
dataset construction, model architecture / trainer, real data, model-output
integration, self-play, league and P8-P12 remain unapproved.
```

## Next Task Recommendation

If no blocker is found, the next first task should be:

```text
Review full P7 closure roadmap and remaining scope inventory after current-scope closure.
```

That task must remain a docs-only review gate. It must not add code, tests,
fixtures, data files, parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, training, model
architecture, trainer, model-output integration, real data, self-play, league,
P8-P12 work or model-strength claims.

## Evidence Grade

```text
Full P7 closure roadmap and remaining scope inventory definition evidence only.
```

## Explicit Non-Evidence

This roadmap / inventory is not:

- full P7 closure.
- broader P7 implementation.
- P7 training.
- source approval.
- training-data approval.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- model architecture.
- trainer.
- model-output integration.
- CLI.
- broad file ingestion.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- self-play.
- league.
- P8-P12 entry approval.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
