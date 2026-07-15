# 12AA_P8_MODEL_ARTIFACT_PROVENANCE_MANIFEST_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 model / artifact provenance-manifest boundary
before any implementation. It is a docs-only planning artifact.

This task is not P8 entry or implementation approval, an implementation
prompt or first executable task, a manifest schema/record/dataclass/database,
a JSON/YAML/TOML manifest, a fixture/data file, a loader/validator/hasher/
signer/verifier, artifact packaging/download, model/checkpoint/snapshot/weight
creation or loading, training-data or training-run approval, training, tuning,
evaluation, checkpoint selection, inference/action generation, model-output
integration, environment/self-play/RL/league execution, source approval or
ingestion, real-data access, strength evidence or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` target only by making future artifact identity, lineage,
lifecycle, verification and use eligibility auditable. It creates and loads no
artifact and provides no evidence that any policy can beat LuckyJ.

## Full P7 / P8 Planning Recap

- Full P7 is closed only for the documented P7 supervised-learning scope.
- `12I`/`12J` defined and reviewed P8 scope and entry criteria.
- `12K`/`12L` defined and reviewed the P8 risk/evidence taxonomy.
- `12M`/`12N` defined and reviewed P8 self-play/RL dependencies.
- `12O`/`12P` defined and reviewed the P8 self-play protocol boundary.
- `12Q`/`12R` defined and reviewed the objective/reward boundary.
- `12S`/`12T` defined and reviewed environment/simulator authority.
- `12U`/`12V` defined and reviewed raw-outcome/environment provenance.
- `12W`/`12X` defined and reviewed model-output interface dependencies.
- `12Y`/`12Z` defined and reviewed training/evaluation model use.
- `12Z` recorded `A. Review can close.`
- P8 remains docs-only planning; entry and implementation are unapproved.
- P9-P12 remain unapproved.

## Provenance-Manifest Non-Approval Baseline

- No P8 model/artifact provenance manifest or artifact-use path is approved.
- No manifest schema, record class, database model or serialization is
  approved.
- No loader, validator, hasher, signer or signature verifier is approved.
- No model, policy, artifact, checkpoint, snapshot or weight is approved,
  created, read, scanned, hashed, packaged, downloaded or loaded.
- No artifact package, storage path, backend or retention policy is approved.
- No hash, canonicalization, signature or identity-generation algorithm is
  selected.
- No signing key or attestation-authority implementation is approved.
- No training or evaluation artifact exists for P8 execution.
- No artifact-use evidence exists beyond docs-only planning.
- A manifest record is not model-strength evidence.
- Frozen, verified, selected or eligible labels are not model-quality claims.

These statements are scoped to current P8 provenance-manifest work. They are
not repository-global claims about every historical file, hash, metadata field
or helper.

## Provenance Vocabulary

| term | boundary meaning |
|---|---|
| model | Future behavior-producing computational specification; none is approved. |
| policy | Versioned decision behavior bound to one logical and artifact identity. |
| architecture identity | Logical identity of a future model structure; not content proof. |
| logical policy identity | Continuity label across reviewed versions; not immutable bytes. |
| artifact | Future immutable content or component set; none exists for P8 execution. |
| artifact class/version | Candidate role and version vocabulary; not an approved enum. |
| immutable content identity | Future content-bound identity; method and algorithm are deferred. |
| logical identifier | Human/governance continuity identity; not integrity proof. |
| locator/path/URI | Mutable location hint; never immutable content identity by itself. |
| manifest/provenance record | Candidate future statement about identity, lineage and status. |
| manifest identity/version | Identity/version of the provenance record, distinct from artifact content. |
| component/component identity | Separately identified future constituent of an artifact bundle. |
| artifact bundle | Candidate component collection; no package format is selected. |
| root/parent/child/derived artifact | Explicit candidate lineage roles; no lineage graph exists. |
| training/recovery/model-only checkpoint | Candidate future capture classes with different uses. |
| optimizer-state artifact | Candidate training-state component, not evaluation content by implication. |
| snapshot | Candidate immutable state capture with declared components and use. |
| frozen evaluation artifact | Candidate immutable evaluation-use artifact; not strength evidence. |
| baseline/reference/opponent artifact | Candidate comparison/interaction roles; names grant no benchmark status. |
| adapter artifact | Candidate interface-related component; no adapter is approved. |
| third-party artifact | Externally sourced candidate; blocked pending separate review. |
| creation/derivation event | Candidate auditable production or transformation event. |
| freeze/thaw event | Candidate lifecycle/use transition; no mechanism is implemented. |
| verification event | Candidate integrity/consistency check record; none is executed. |
| attestation | Candidate authority-backed statement; format/authority are deferred. |
| integrity/verification status | Candidate status, not strength or evaluation eligibility. |
| quarantine/revocation | Candidate block or withdrawal state with retained audit history. |
| supersession/deprecation | Candidate replacement/retirement state that preserves history. |
| active head | Candidate current lineage head under separately reviewed resolution rules. |
| compatibility status | Candidate declared/verified compatibility state; no checker exists. |
| license/provenance/security status | Candidate governance classifications, not use permission alone. |
| use/evidence eligibility | Separate future governance decisions; artifacts cannot self-grant them. |
| non-evidence warning | Required warning preventing provenance records from becoming strength claims. |

Logical identity, immutable content identity and manifest identity are three
different identities. A path, tag or display name is only a locator. Frozen is
a use/integrity property, not a quality claim. This vocabulary approves no
schema, record, loader, artifact or implementation.

## Authority Separation

| authority | may own in a separately approved future task | must not self-grant |
|---|---|---|
| artifact producer | candidate bytes/components, creation/derivation event, parent lineage and candidate manifest data | verified/frozen eligibility, source/license approval, strength or promotion |
| manifest/provenance authority | record identity, content-reference binding, lineage/lifecycle declaration and completeness status | integrity verification, evaluation eligibility or strength |
| verification authority | integrity, manifest/artifact consistency, compatibility and attestation results | artifact production, evaluation eligibility or model quality |
| evaluation governance | eligibility for one exact evaluation use | training approval, strength classification or promotion |
| evidence governance | engineering/training/strength/ranked/promotion evidence grade | artifact production, loading, inference or evaluation execution |
| storage system | future storage/retrieval under separate approval | identity, verification, eligibility or strength classification |
| loader | future exact loading behavior under separate approval | silent repair, substitution, migration, upgrade or eligibility |

No authority or system is implemented now. Producer assertions never become
verified status or use permission by implication.

## Candidate Artifact Classes

Every class has `approved_now = no`, `selected_now = no`,
`creation_allowed_now = no`, `loading_allowed_now = no` and
`implementation_allowed_now = no`.

| candidate class | intended future role | principal risk | approved_now | selected_now | creation_allowed_now | loading_allowed_now | implementation_allowed_now |
|---|---|---|---:|---:|---:|---:|---:|
| model-only immutable artifact | inference-relevant content only | omitted behavior dependency | no | no | no | no | no |
| training recovery checkpoint | restart an approved run | mistaken evaluation artifact | no | no | no | no | no |
| optimizer/training-state artifact | optimizer/scheduler/RNG state | leakage into evaluation | no | no | no | no | no |
| frozen evaluation artifact | exact future evaluation participant | freeze mistaken for strength | no | no | no | no | no |
| baseline/reference artifact | bounded comparison | LuckyJ overclaim by name | no | no | no | no | no |
| opponent-policy artifact | later interaction participant | opponent-pool/league implication | no | no | no | no | no |
| adapter/interface artifact | future compatibility metadata/code | silent semantic conversion | no | no | no | no | no |
| recurrent-state compatibility artifact | future state-compatibility declaration | cross-policy leakage | no | no | no | no | no |
| synthetic/local provenance-contract smoke artifact | future contract-only smoke | impersonating a model artifact | no | no | no | no | no |
| remote/third-party artifact | possible external artifact | rights/privacy/security/integrity | no | no | no | no | no |

A recovery checkpoint does not become an evaluation artifact. Optimizer state
does not merge into model content by implication. Frozen does not mean strong.
Baseline/reference naming is not LuckyJ comparison. Opponent identity does not
approve a pool or league. Synthetic smoke cannot impersonate a model artifact.
Remote/third-party artifacts remain blocked.

## Three-Layer Identity Boundary

### Logical Identity

Candidate logical identities include `policy_id`, `architecture_id`,
`artifact_family_id` and `candidate_name`. They may continue across reviewed
versions but cannot prove immutable content, integrity or reproducibility.

### Immutable Content Identity

Future immutable identity must bind actual content for every included
component. The hash/content-identity algorithm, canonical byte representation
and method version remain deferred for separate review. A mutable path or tag
is insufficient. Any content change requires a new content identity.

### Manifest / Provenance Record Identity

The future record has its own identity and version. It is not the artifact
content identity. Correcting or superseding a record must not rewrite artifact
bytes, and one record must never silently refer to different content. No ID
generation algorithm or record implementation is approved.

## Artifact Component / Bundle Boundary

A future artifact may reference separately identified candidate components:

- model weights.
- architecture/config description.
- observation/action and model-output contract references.
- runtime/backend/device/precision compatibility metadata.
- optimizer state, scheduler state and RNG/training-state snapshot.
- recurrent-state compatibility and adapter metadata.
- license/provenance documents and verification/attestation records.

Component composition and package format are unselected. Model-only and
training-recovery bundles remain distinct. Evaluation artifacts must declare
allowed components; optimizer/RNG/training state cannot enter silently. Every
component needs identity and status, and partial bundles must be explicit. No
bundle, archive or package is created.

## Creation and Derivation Provenance

Future provenance should bind:

```text
producer_authority_identity
creation_event_identity
creation_reason
parent_artifact_identity
derivation_relationship
training_run_identity_if_approved
training_step_or_update_identity_if_approved
code_revision
model_configuration_version
architecture_identity
reward_objective_version
protocol_environment_ruleset_versions
observation_model_output_contract_versions
source_data_status
backend_runtime_device_precision
seeds_and_known_nondeterminism
component_identities
creation_completeness_status
```

Parent/child lineage does not prove training approval. Every derived artifact
requires new content identity. Parent substitution and in-place child creation
under the parent identity are forbidden. No run or artifact is created now.

## Lineage Graph Boundary

Future lineage must distinguish parent/child edges, roots, derived artifacts,
siblings, checkpoint sequences, recovery lineage, selection lineage,
freeze/thaw lineage, supersession lineage, revocation impact and external
origin.

- Lineage must be acyclic.
- Every edge requires an explicit relationship type.
- Multiple parents require separately reviewed semantics.
- Missing or unverifiable parents remain explicit.
- Parent deletion must not erase historical provenance.
- Correction and supersession preserve original records and resolvable heads.
- No graph, database or resolver implementation is approved.

## Artifact Lifecycle Vocabulary

Candidate statuses include:

```text
proposed
produced_unverified
verification_pending
verified
verification_failed
frozen
thawed
mutable
quarantined
revoked
superseded
deprecated
missing
unavailable
rejected
incomplete
```

These statuses are not an approved enum or schema. Produced is not verified;
verified is not evaluation eligible; frozen is not strong. Revoked artifacts
cannot remain silently eligible. Supersession preserves history. Every status
transition requires explicit authority, reason, event identity and provenance.
No lifecycle mechanism exists.

## Freeze / Thaw Boundary

A future freeze event should bind artifact content identity, all behavior-
affecting components, code/config/runtime/backend/device/precision,
environment/protocol/ruleset/reward/model-output contracts, freeze authority,
event identity, effective-use range, verification status, intended use and
revocation/supersession policy.

Freeze is not a mutable boolean. Finalization must be auditable. Evaluation
use requires separately approved freeze semantics. Thaw is a new lifecycle/use
event; content changes create new content identity, and thaw cannot silently
retain evaluation eligibility. No freeze/thaw mechanism is implemented.

## Verification / Attestation Boundary

Candidate future verification categories include:

- content-identity verification.
- manifest/artifact consistency and component completeness.
- parent-lineage consistency.
- environment/protocol/contract and runtime/backend/precision compatibility.
- license/provenance and security/malware-policy verification.
- freeze-attestation and reproducibility-status verification.

Hash/canonicalization/signature algorithms, signing keys, authorities and
attestation formats are unselected. Verification pass is not model-strength
evidence. Failure remains visible and cannot be filtered away. No validator,
hasher, signer or verifier is implemented.

## Compatibility and Dependency Binding

Future provenance should reference immutable or separately reviewed versions
for architecture, model configuration, code, runtime/backend/device/precision,
observation contract, action vocabulary/legal-action contract, model-output
contract, recurrent-state compatibility, protocol, environment/simulator,
ruleset, reward/objective, raw-outcome provenance and training/evaluation use.

A declaration is not compatibility evidence. A loader cannot silently migrate
or convert. An adapter cannot silently change semantics. Incompatibility must
fail explicitly. No checker or migration tool is implemented.

## Locator / Storage Boundary

File path, directory, URI, object key and database key are locators only.
Locators may change and cannot prove immutable content. Storage backend,
manifest location, package format, content-addressed storage, database,
retention and garbage-collection policy are unselected and unapproved.
Revoked/superseded records must remain auditable. No storage or retrieval
implementation exists.

## Revocation / Quarantine / Supersession Boundary

Future lifecycle events should bind affected artifact, event type/reason,
authority, event identity/version, effective range, affected uses, dependent
children/evaluations, replacement identity and verification/evidence impact.

Silent deletion is forbidden. Revoked artifacts cannot silently remain
eligible. Quarantine blocks use pending review but does not itself prove
invalidity. Supersession preserves the earlier artifact and must remain
acyclic. No revocation service or database is implemented.

## Training / Evaluation Model-Use Binding

The `12Y`/`12Z` boundary remains controlling:

- Mutable training use binds an explicit update schedule and parent/child
  lineage under separate approval.
- Frozen evaluation use binds immutable content and a freeze event.
- A training artifact does not automatically become an evaluation artifact.
- Checkpoint selection does not create promotion evidence.
- Evaluation use references one exact eligible manifest identity.
- Model use cannot bypass TU-E14/TU-E15.
- No model use, training or evaluation is approved.

## Artifact Eligibility Boundary

Candidate future statuses may distinguish `training_use_eligible`,
`recovery_use_eligible`, `validation_use_eligible`, `selection_use_eligible`,
`holdout_evaluation_eligible`, `opponent_use_eligible`,
`reference_use_eligible`, `ranked_evidence_ineligible`, `pending_review`,
`quarantined` and `revoked`.

They are not schema. An artifact cannot self-grant eligibility. Verification
does not automatically grant evaluation eligibility, and evaluation
eligibility does not grant strength evidence. Every transition needs explicit
authority, reason and audit identity. No eligibility decision is made now.

## Reproducibility Boundary

Future provenance should bind immutable artifact/component identities,
architecture/config/code, parent lineage, approved run/update and data/source/
split status if any, seeds/nondeterminism, runtime/backend/device/precision,
environment/protocol/reward/model-output versions, verification, freeze/use,
third-party provenance and failure/restart lineage.

Same path/tag/checkpoint name or same seed is not reproducibility. Verified
content is necessary but insufficient. Training and evaluation reproducibility
remain distinct. No reproducibility result is generated.

## Source / Privacy / License / Security Boundary

- No source approval or ingestion.
- No real Tenhou/haifu/external/platform data.
- No account/session/cookie/token/API key or secret in candidate fields.
- No unknown checkpoint/model, remote model service or third-party binary.
- No Akochan `system.exe`, `libai.so`, artifact download or vendoring.
- External artifacts require separate license, redistribution, provenance,
  integrity, privacy and security review.
- Compatible format never grants use permission.

## Candidate Manifest Fields

The following are candidate future fields only:

```text
manifest_record_id
manifest_record_version
manifest_status
logical_policy_id
policy_version
architecture_identity
artifact_id
artifact_version
artifact_class
artifact_content_identity
content_identity_method
content_identity_method_version
canonicalization_status
component_ids
component_content_identities
bundle_completeness_status
parent_artifact_ids
parent_relationship_types
root_artifact_id
creation_event_id
producer_authority_id
derivation_reason
training_run_id_if_approved
training_step_identity_if_approved
checkpoint_id_if_approved
snapshot_id_if_approved
code_revision
model_config_version
reward_objective_version
protocol_id
protocol_version
environment_id
environment_version
ruleset_version
observation_contract_version
model_output_contract_version
raw_outcome_provenance_version
runtime_identity
backend_identity
device_identity
precision_identity
mutable_or_frozen_status
freeze_event_id
freeze_authority_id
effective_use_range
thaw_event_id
verification_status
verification_event_ids
attestation_status
license_provenance_status
security_status
compatibility_status
quarantine_status
revocation_status
revocation_event_id
supersedes_artifact_id
storage_locator
locator_status
training_use_status
validation_use_status
selection_use_status
holdout_evaluation_use_status
opponent_use_status
ranked_evidence_status
model_strength_status
provenance_completeness_status
explicit_non_evidence_warning
```

They are not an approved schema, API or database model. No fixture, record,
loader, validator, artifact or model is created. Hash/canonicalization/
signature and storage choices remain unselected. Locator is not content
identity.

## Evidence Boundary

Current evidence grade:

```text
P8 model / artifact provenance manifest boundary definition evidence only.
```

It supports only vocabulary, identity/content/lineage, lifecycle,
freeze/thaw/revocation, verification/eligibility and future-review readiness.
It does not support P8 entry/implementation, schema/loader/validator evidence,
artifact creation/loading, checkpoint/model-use, training/evaluation/inference,
self-play/RL/league, strength/Tenhou/stable-dan/LuckyJ/promotion evidence or
P9-P12 approval.

## Future Provenance-Manifest Entry Criteria

- PM-E1. P8 scope review is closed.
- PM-E2. P8 risk/evidence taxonomy review is closed.
- PM-E3. P8 self-play/RL dependency-map review is closed.
- PM-E4. P8 self-play protocol boundary review is closed.
- PM-E5. P8 objective/reward boundary review is closed.
- PM-E6. P8 environment/simulator boundary review is closed.
- PM-E7. P8 raw-outcome/provenance boundary review is closed.
- PM-E8. P8 model-output interface boundary review is closed.
- PM-E9. P8 training/evaluation model-use boundary review is closed.
- PM-E10. This provenance-manifest boundary is defined and reviewed.
- PM-E11. Content identity, component, lineage and lifecycle semantics are
  reviewed.
- PM-E12. Freeze/thaw/revocation/verification/eligibility semantics are
  reviewed.
- PM-E13. Source/license/privacy/security and third-party status remain
  separately governed.
- PM-E14. A separate approval decision authorizes one exact future task.
- PM-E15. `docs/10_next/10_NEXT.md` authorizes that exact future task.

None of PM-E1 through PM-E15 is implementation approval. Defined and reviewed
does not mean a manifest exists. PM-E14 and PM-E15 are hard gates before any
schema, fixture, loader, validator, artifact, checkpoint, model, code, test or
data work.

## Stop Conditions

Stop if a current or future task:

- implies P8 entry/implementation or generates an unapproved implementation
  prompt.
- selects hash/canonicalization/signature/storage implementation.
- creates manifest schema/record/database/fixture or executable tooling.
- scans, hashes, creates, loads, downloads or vendors an artifact/model/
  checkpoint/weight/snapshot.
- changes content under one identity or uses path/tag as content proof.
- changes lineage silently, creates cycles or ignores missing parents.
- freezes without immutable content or silently thaws an evaluation artifact.
- silently revokes, deletes or supersedes records.
- treats verification/freeze/selection as strength or promotion evidence.
- runs inference/training/tuning/evaluation/self-play/RL/league.
- accesses or approves real/platform data or source ingestion.
- creates code/tests/fixtures/data or enters P9-P12.
- claims Tenhou/stable-dan/LuckyJ/promotion evidence.
- uses unknown third-party artifacts, services or binaries.

## Candidate Next Directions

| candidate | current_status | benefit | principal risk | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---:|---:|---|
| A. Review this provenance-manifest boundary | candidate safe next | validate semantics and non-approval | review mistaken for execution | current definition | yes | no | low | low | selected next |
| B. Define training-data/training-run dependency boundary | deferred | clarify run provenance | data/training authorization drift | review and separate task | yes | no | medium | low | not selected |
| C. Define evaluation protocol/metric boundary | deferred | clarify evaluation use | premature evaluation approval | review and separate task | yes | no | medium | medium | not selected |
| D. Define verification/attestation evidence boundary | deferred | refine integrity evidence | algorithm/authority selection | review and separate task | yes | no | medium | low | not selected |
| E. Define checkpoint-selection/early-stopping boundary | deferred | refine selection leakage | execution/strength overclaim | review and separate task | yes | no | medium | low | not selected |
| F. Define RL algorithm-selection boundary | later | prepare algorithm review | premature RL selection | P8 entry and dependencies | yes | no | high | medium | not selected |
| G. Draft manifest schema proposal | blocked | future executable contract | schema by implication | PM-E10-PM-E15 | yes | no | high | low | not selected |
| H. Prepare P8 entry approval | blocked | possible stage transition | premature approval | all entry evidence | yes | no | high | medium | not selected |
| I. Draft P8 implementation proposal | blocked | future implementation planning | bypasses approval | P8 entry and exact approval | yes | no | high | medium | not selected |
| J. Implement manifest/loader/validator | forbidden now | future tooling | executable scope jump | PM-E14/PM-E15 | no | yes | high | medium | not selected |
| K. Create/load model/checkpoint/weight | forbidden now | future model use | unknown artifact and execution | separate approvals | no | yes | high | high | not selected |
| L. Run training/evaluation/inference | forbidden now | future evidence | execution without gates | separate approvals | no | yes | high | high | not selected |
| M. Execute self-play/RL/league | forbidden now | future P8/P10 work | stage jump | P8/P10 gates | no | yes | high | high | not selected |
| N. Start real-data/Tenhou work | forbidden now | future external evidence | rights/platform risk | source/compliance approval | no | yes | high | high | not selected |
| O. Claim strength or enter P9-P12 | forbidden now | none at this stage | evidence/stage overclaim | later-stage evidence | no | yes | high | high | not selected |

Selected next direction:

```text
Review P8 model / artifact provenance manifest boundary before any implementation.
```

## Planning Decision

```text
P8 model / artifact provenance manifest boundary is defined before any implementation.
```

This task does not approve P8 entry, P8 implementation, an implementation
prompt, a manifest schema/record/fixture/database, loader/validator/hash/
signature implementation, model/checkpoint/snapshot/weight/artifact creation
or loading, training-data approval, training-run approval, training, tuning,
evaluation, checkpoint selection, inference, action generation, model-output
integration, self-play/RL/league, source approval/ingestion, real data,
strength/Tenhou/stable-dan/LuckyJ/promotion evidence or P9-P12 entry. The next
safe task is a docs-only review of this boundary.

## Evidence Grade

```text
P8 model / artifact provenance manifest boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P8 entry/implementation, an implementation prompt or executable task.
- a manifest schema, record, database, fixture, data file or storage backend.
- a loader, validator, hasher, signer, verifier or compatibility checker.
- artifact/model/checkpoint/snapshot/weight creation, reading or loading.
- training-data/training-run approval, training, tuning or checkpoint selection.
- evaluation, inference, action generation or model-output integration.
- environment, transition, episode, self-play, RL or league execution.
- source approval/ingestion or real Tenhou/haifu/external/platform data.
- model strength, Tenhou ranked, stable-dan, LuckyJ or promotion evidence.
- P9-P12 approval.

## Deferred Decisions

The following choices are intentionally deferred to separate review/approval:

- content-identity/hash and canonicalization algorithms.
- manifest serialization and storage backend.
- signature algorithm, signing key and attestation authority.
- artifact package and component composition.
- retention, revocation, quarantine and garbage-collection implementation.
- third-party, remote or external artifact use.

No current human decision is needed because this boundary does not select any
of those choices.

## Validation

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

These checks validate repository formatting and existing synthetic/local
boundaries only. They do not inspect, hash, load or execute any model artifact.
