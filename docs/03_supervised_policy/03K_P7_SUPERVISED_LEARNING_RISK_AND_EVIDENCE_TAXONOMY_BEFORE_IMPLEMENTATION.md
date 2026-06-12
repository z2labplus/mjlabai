# 03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION

## Scope

This document defines the P7 supervised-learning risk and evidence taxonomy
before implementation.

This is P7 docs-only readiness / governance groundwork. It defines how future
P7 risks and evidence grades must be named, interpreted and reviewed before any
source approval, parser work, feature extraction, label generation, dataset
construction, model architecture, training loop, model-output integration or
P8-P12 transition can start.

This document does not approve:

- P7 implementation.
- P7 first-task execution.
- training data source selection.
- source ingestion.
- parser, dataset reader or ingestion.
- feature extraction.
- label generation.
- supervised dataset construction.
- model architecture, dataloader, optimizer, loss, trainer or checkpoint work.
- real Tenhou, real haifu, external-log or platform-data use.
- model-output integration.
- CLI or broad file ingestion.
- training, tuning, self-play, league or runner behavior.
- P8-P12 entry.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claims.

## Post Readiness Context

P5 is closed only for the current synthetic/local evaluation groundwork scope.
Full P6 is closed only for the documented P6 data-system scope:
docs/governance/source-rights planning, accepted synthetic/local minimal
replay schema and project-authored synthetic fixture smoke implementation, and
deferred / blocked / later-stage inventory.

The current P7 readiness chain is:

```text
03E P7 scope / entry criteria / first-task definition
-> 03F P7 scope review: Review can close
-> 03G P7 data/source readiness inventory
-> 03H data/source readiness review: Review can close
-> 03I feature and label readiness boundary
-> 03J feature and label readiness review: Review can close
-> this 03K risk and evidence taxonomy definition
```

The completed P7 documents are readiness and review evidence only. They do not
approve a training data source, source ingestion, parser, dataset reader,
ingestion, feature extraction, label generation, supervised dataset
construction, model architecture, training, model-output integration,
real-data use or P8-P12 entry.

## P7 Risk Taxonomy

| risk_category | risk_description | current_status | mitigation | required_before_implementation | owner_doc_or_followup | blocker_if_unresolved | notes |
|---|---|---|---|---|---|---|---|
| scope / stage creep risk | Docs-only P7 readiness work may be mistaken for implementation approval. | open | Keep `10_NEXT`, handoff, evidence log and stage contract explicit. | Review this taxonomy and require later implementation proposal / approval decision. | `03K`, future `03K` review | yes | Applies to all P7 readiness docs. |
| source approval risk | A listed source category may be treated as approved for training or ingestion. | open | Require source-specific approval and rights review. | source id, rights, allowed use, storage policy and human/Web approval. | `03G`, future source approval doc | yes | Current approved P7 training source is `None`. |
| training-data approval risk | Synthetic fixtures or docs may be treated as P7 training data. | open | Label fixtures/docs as planning or smoke evidence only. | reviewed source approval and dataset policy. | `03G`, evidence log | yes | P6 synthetic fixture is not training data. |
| parser / reader / ingestion creep risk | A future P7 task may start data-path code while framed as readiness work. | open | Keep parser, reader, ingestion, CLI and broad file ingestion as separate approvals. | explicit parser / reader / ingestion boundary and approval decision. | future parser / ingestion boundary | yes | No parser, reader or ingestion path is approved now. |
| feature extraction approval ambiguity risk | Candidate feature families may be read as approved feature schemas. | open | Mark candidates as planning-only until implementation approval. | feature schema, public-information policy, validation plan and approval. | `03I`, future feature proposal | yes | No feature extraction is approved. |
| label generation approval ambiguity risk | Candidate label families may be read as approved label generation. | open | Mark candidates as planning-only until label policy and source approval exist. | label source policy, label version, validation plan and approval. | `03I`, future label proposal | yes | No label generation is approved. |
| hidden-information leakage risk | Features or labels may include information unavailable to the acting player. | open | Require public-information-only policy and hidden-info exclusion checks. | observation boundary, schema version and leakage validation. | `03I`, future feature schema | yes | Highest P7 data-quality risk. |
| future-information leakage risk | Future draws, future discards or final outcomes may leak into decision-time inputs. | open | Require timestamp policy, decision boundary and future-event exclusion. | feature / label leakage tests and split policy. | `03I`, future leakage policy | yes | Outcome targets must be separated from decision-time features. |
| train / validation / test leakage risk | Same-game, source, temporal or near-duplicate leakage may inflate results. | open | Require split policy before dataset construction. | train / validation / test split policy and leakage checks. | future split policy | yes | No supervised dataset exists now. |
| model-output integration too early risk | Model outputs may be used as labels or inputs before a policy exists. | open | Keep model-output integration forbidden until separately approved. | model-output policy, provenance, versioning and validation. | future model-output boundary | yes | Current P7 artifacts do not approve model-output labels. |
| real-data / platform-data leakage risk | Real Tenhou, real haifu, external logs or platform data may be used without approval. | open | Keep real/external/platform sources blocked by rights, privacy and platform review. | source-specific lawful approval and storage policy. | `03G`, risk register | yes | No real data is approved. |
| account / cookie / token risk | Account, session, cookie or token data may enter the project. | open | Forbid account/session/cookie/token use unless a later lawful task approves it. | compliance review and explicit `10_NEXT` task. | risk register / platform compliance | yes | Forbidden now. |
| third-party binary / weights / params risk | Third-party binaries, params, weights or checkpoints may be downloaded, vendored or used. | open | Forbid unknown or unreviewed artifacts and keep checksums/provenance required. | lawful artifact review, usage rights, checksum and storage policy. | future artifact review | yes | Includes `system.exe`, `libai.so`, `params/`, `*.pth`, `*.pt`, checkpoints and snapshots. |
| training-before-approval risk | Training may start before data, feature, label, model and evidence gates exist. | open | Require proposal review and approval decision before any training task. | approved source, dataset, features, labels, model config and validation plan. | future P7 implementation proposal | yes | Training is not approved. |
| model artifact provenance risk | Future checkpoints may lack source, seed, config or checksum traceability. | open | Require artifact id, checksum, config, seed and storage policy before use. | artifact provenance policy and evidence log entry. | future artifact policy | yes | No model artifacts now. |
| metric / evidence overclaim risk | Planning evidence may be interpreted as performance evidence. | open | Use evidence-to-claim mapping and explicit non-evidence lists. | reviewed evidence taxonomy and future metric approval. | `03K`, evidence log | yes | This taxonomy is not performance evidence. |
| model-strength overclaim risk | Readiness docs, smoke tests or training logs may be used to claim strength. | open | Require approved evaluation protocol and P5/P10/P12 evidence before strength claims. | offline evaluation / league / Tenhou evidence as stage-appropriate. | evaluation docs / future review | yes | No model-strength claim is allowed now. |
| LuckyJ / Tenhou / stable-dan comparison overclaim risk | Current P7 evidence may be used as LuckyJ or Tenhou proof. | open | Reserve LuckyJ / ranked Tenhou claims for explicit later protocol and evidence. | P12 validation and reviewed comparison protocol. | P5/P12 docs | yes | P7 readiness evidence cannot compare to LuckyJ. |
| P8/P10/P12 stage creep risk | P7 readiness may drift into RL, league or Tenhou validation. | open | Require separate transition reviews, scope, entry criteria and first-task approval. | stage-specific transition review and approval. | future P8/P10/P12 docs | yes | P8-P12 remain unapproved. |
| candidate promotion overclaim risk | A candidate may be promoted from readiness or smoke evidence. | open | Use racing-funnel gates and forbid promotion without gate evidence. | funnel-stage evidence, uncertainty and review. | racing funnel / evaluation docs | yes | No candidate promotion evidence exists. |

## P7 Evidence Taxonomy

| evidence_type | allowed_interpretation | forbidden_interpretation | implementation_allowed | training_allowed | model_strength_claim_allowed | P8_P12_entry_allowed | required_supporting_artifacts | notes |
|---|---|---|---:|---:|---:|---:|---|---|
| docs-only P7 scope evidence | P7 scope, boundaries and next docs task are defined. | implementation, training, source approval or strength. | no | no | no | no | `03E`, `03F`, handoff, `10_NEXT` | Planning evidence only. |
| data/source readiness evidence | Candidate source categories and blockers are inventoried. | source approval or training-data approval. | no | no | no | no | `03G`, `03H`, source inventory refs | Inventory is not approval. |
| feature/label readiness boundary evidence | Future feature and label prerequisites are defined. | feature extraction or label generation approval. | no | no | no | no | `03I`, `03J` | Boundary is not schema implementation. |
| risk/evidence taxonomy evidence | Risk categories, evidence grades and claim mapping are defined. | implementation approval, source approval or model strength. | no | no | no | no | this document, review gate | Current task evidence type. |
| future proposal evidence | A future exact task may be proposed for review. | approval or execution by itself. | no | no | no | no | proposal document, allowed files, stop conditions | Needs separate approval decision. |
| future approval-decision evidence | A narrow implementation task may be approved if criteria pass. | broad stage approval, training approval or later-stage entry. | only exact approved scope | only if explicitly approved | no | no | decision record, `10_NEXT`, validation plan | Approval must name exact files and non-goals. |
| future synthetic/local smoke implementation evidence | Synthetic/local code path works for a narrow approved fixture. | real-data support, policy quality or strength. | only exact approved scope | no | no | no | code, tests, fixture, evidence/risk updates | Engineering smoke only. |
| future feature/label schema smoke evidence | Feature/label schema shape validates on approved synthetic/local input. | feature quality, label quality or training readiness. | only exact approved scope | no | no | no | schema doc, fixture, tests, leakage notes | Not training data approval. |
| future training-run engineering evidence | A training job ran under approved data/config boundaries. | Tenhou strength, LuckyJ comparison or candidate promotion. | yes if approved | yes if approved | no | no | source approvals, config, seed, logs, artifact checksums | Training run is engineering evidence. |
| future offline evaluation evidence | Approved offline metrics were produced under reviewed protocol. | Tenhou ranked proof or LuckyJ proof by itself. | no by itself | no | maybe limited offline claim | no | result envelope, metrics, sample size, uncertainty | Claim scope depends on metric protocol. |
| future model-strength evidence candidate | Multiple approved evaluations support a strength hypothesis. | final Tenhou / LuckyJ proof without P12. | no by itself | no | maybe after review | no | P5/P10 evidence, uncertainty, review | Candidate evidence, not final proof. |
| future Tenhou validation evidence candidate | Lawful P12 validation may support Tenhou ranked claims. | any pre-P12 claim. | no | no | yes only after P12 review | only after transition | P12 protocol, legal/compliance review, sample size, logs | Not available in P7. |

## Current P7 Evidence Classification

| artifact | current_evidence_classification | allowed_claim | forbidden_claim |
|---|---|---|---|
| `03E` | docs-only P7 scope / entry criteria / first-task definition evidence | P7 scope is defined for review. | P7 implementation or first-task execution is approved. |
| `03F` | docs-only P7 scope review evidence | Scope review can close. | P7 implementation, training or source approval is granted. |
| `03G` | data/source readiness inventory evidence | Candidate source categories and blockers are inventoried. | Any source is approved for P7 training or ingestion. |
| `03H` | data/source readiness inventory review evidence | Inventory review can close. | Parser, reader, ingestion, feature extraction or label generation is approved. |
| `03I` | feature/label readiness boundary definition evidence | Future feature/label prerequisites are defined. | Feature extraction or label generation implementation is approved. |
| `03J` | feature/label readiness boundary review evidence | Feature/label boundary review can close. | Feature/label schemas, data sources, training or implementation are approved. |
| `03K` | risk/evidence taxonomy definition evidence | P7 risk categories, evidence grades and claim mapping are defined. | P7 implementation, training, model strength or P8-P12 entry is approved. |

Current P7 evidence is not:

- P7 implementation evidence.
- training evidence.
- source approval evidence.
- feature extraction evidence.
- label generation evidence.
- model-strength evidence.
- Tenhou evidence.
- LuckyJ comparison evidence.
- candidate promotion evidence.

## Future P7 Evidence Requirements

Future P7 implementation, training or evaluation tasks must record the
applicable fields below before their outputs can be interpreted:

- `source_id`.
- source approval status.
- source rights / license / terms.
- parser / reader version.
- ingestion version.
- schema version.
- feature version.
- label version.
- training dataset id.
- train / validation / test split policy.
- leakage checks.
- model architecture id.
- training config id.
- random seed.
- dependency versions.
- hardware / runtime if relevant.
- validation commands.
- metric outputs.
- evaluation envelope.
- artifact checksum.
- failure modes.
- known exclusions.
- explicit non-evidence warning.

Missing fields must be treated as blockers or deferred requirements for the
claim that depends on them.

## Evidence-To-Claim Mapping

| evidence | may_support | cannot_support |
|---|---|---|
| docs-only boundary evidence | boundary / planning claim only | implementation, training, source approval, strength, Tenhou or LuckyJ claims |
| source readiness evidence | readiness inventory claim only | source-use approval, ingestion approval or training-data approval |
| source approval evidence | source-use claim after separate approval | feature extraction, label generation, training or strength by itself |
| synthetic smoke evidence | narrow engineering smoke claim | real-data support, model performance, policy quality or promotion |
| training run evidence | training-run engineering claim | Tenhou strength or LuckyJ comparison by itself |
| offline evaluation evidence | offline performance claim if metrics, sample size and protocol are approved | Tenhou ranked claim or LuckyJ proof by itself |
| model league evidence | relative model comparison only if P10 is approved | P12 Tenhou validation or LuckyJ proof by itself |
| Tenhou validation evidence | Tenhou ranked claim only if P12 protocol and compliance are approved | any pre-P12 claim |
| LuckyJ comparison evidence | LuckyJ comparison only with explicit comparison protocol, data, sample size and stage approval | current P7 planning or smoke evidence |

## Forbidden Evidence Interpretations

The following interpretations are forbidden:

- Docs evidence interpreted as model strength.
- P6 synthetic fixture interpreted as training data approval.
- P7 data/source readiness interpreted as source approval.
- Feature/label boundary interpreted as implementation approval.
- Risk taxonomy interpreted as approval decision.
- Smoke tests interpreted as model performance.
- Offline metric planning interpreted as actual offline performance.
- Training logs interpreted as Tenhou strength.
- Self-play wins interpreted as Tenhou strength without P10 / P12.
- Any current P7 artifact interpreted as LuckyJ `10.68` comparison or
  candidate promotion.

## Risk / Evidence Dependency Map

Future P7 work must follow this dependency order:

```text
P7 scope / entry criteria
-> data/source readiness
-> feature/label readiness
-> risk/evidence taxonomy
-> implementation proposal
-> proposal review
-> approval decision
-> exact minimal implementation
-> implementation review
-> evidence/risk update
-> future training / evaluation gates
```

If any predecessor is missing, ambiguous or rejected, later implementation must
remain blocked or deferred. A readiness document can only define future gates;
it cannot satisfy those gates by itself.

## Evidence Log / Risk Register Update Requirements

Future P7 tasks must update governance records according to their evidence
grade:

| governance_file | required_update |
|---|---|
| `docs/09_governance/09_EVIDENCE_LOG.md` | Record evidence type, stage, artifacts reviewed or created, validation commands, allowed interpretation and explicit non-evidence. |
| `docs/09_governance/09_RISK_REGISTER.md` | Record new or changed risks, mitigations, blocker status and whether unresolved risks block implementation. |
| `docs/09_governance/09_DECISION_RECORD.md` | Record decisions that approve, reject, defer or close review gates. |
| `docs/09_governance/09_STAGE_TASK_CONTRACT.md` | Keep current stage, allowed scope and forbidden scope aligned with `10_NEXT`. |
| `docs/10_next/10_NEXT.md` | Keep exactly one first unchecked task and make its stage, allowed files and forbidden work explicit. |
| `docs/00_HANDOFF.md` | Summarize current stage, latest evidence grade, next task and non-evidence warnings. |

## P8-P12 Non-Entry Boundary

This taxonomy does not approve:

- P8 reinforcement learning.
- P9 search / risk model implementation.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou validation.

Future P7 closure also must not automatically approve P8-P12. Each later stage
requires a separate transition review, scope definition, entry criteria, risk
review, evidence taxonomy and first-task approval.

## Review Status

`docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`
reviews this taxonomy and records:

```text
Review can close.
```

That review does not approve P7 implementation, P7 first-task execution,
source approval, source ingestion, parser, dataset reader, ingestion, feature
extraction, label generation, training, model-output integration or P8-P12
entry. It only allows the next docs-only proposal-definition task:

```text
Define minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation.
```

## Planning Decision

```text
P7 supervised-learning risk and evidence taxonomy is defined before implementation. This does not approve P7 implementation, P7 first-task execution, training, source ingestion, parser, dataset reader, feature extraction, label generation, real data, model-output integration, self-play, league, model-strength claims or P8-P12 entry.
```

## Historical Next Task Recommendation

Recommended next task:

```text
Review P7 supervised-learning risk and evidence taxonomy before implementation.
```

This recommended review gate was completed in `03L` and recorded `Review can
close`. It did not implement P7, approve P7 first-task execution, approve
source ingestion, approve parser / dataset reader / ingestion, approve feature
extraction, approve label generation, approve training or approve P8-P12.

## Evidence Grade

```text
P7 supervised-learning risk and evidence taxonomy definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P7 implementation.
- P7 first-task execution.
- P8-P12 entry approval.
- training.
- tuning.
- self-play.
- league.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- parser.
- dataset reader.
- data ingestion.
- feature extraction implementation.
- label generation implementation.
- source approval.
- training-data approval.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
