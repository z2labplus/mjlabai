# 12Y_P8_TRAINING_EVALUATION_MODEL_USE_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 training / evaluation model-use boundary before
any implementation. It is a docs-only planning artifact.

This task is not P8 entry or implementation approval, an implementation prompt
or first executable task, training-data or training-run approval, training,
tuning, evaluation approval or execution, holdout evaluation, checkpoint
selection, candidate promotion, model/policy/checkpoint/weight loading,
checkpoint/snapshot creation, trainer/optimizer/loss/dataloader implementation,
model-output integration, inference/action generation, self-play/RL/environment
execution, league, source approval/ingestion, real-data access, strength
evidence or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` goal only by preventing future mutable training policies,
frozen evaluation policies, checkpoint selection and holdout evidence from
being silently mixed. It loads, trains and evaluates no model and provides no
evidence that any policy can beat LuckyJ.

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
- `12X` recorded `A. Review can close.`
- P8 remains docs-only planning; entry and implementation are unapproved.
- P9-P12 remain unapproved.

## Training / Evaluation Model-Use Non-Approval Baseline

- No P8 training or evaluation model use is approved.
- No training model, evaluation model, mutable policy or frozen evaluation
  policy is approved for execution.
- No model, checkpoint, snapshot, weight or other model artifact is approved,
  loaded or created.
- No training data, training run, optimizer state or update process is approved.
- No evaluation protocol, evaluation run, holdout campaign, model selection,
  checkpoint selection or candidate promotion is approved.
- No model-use evidence exists beyond docs-only boundary planning.
- Training diagnostics are not model-strength evidence.
- An evaluation-looking name does not create evaluation approval.

These statements are scoped to current P8 training/evaluation model use. They
are not repository-global claims about every historical helper or document.

## Model-Use Vocabulary

| term | boundary meaning |
|---|---|
| model | Future behavior-producing computational specification; no architecture or runtime is approved. |
| policy | Versioned decision behavior associated with one use and artifact identity. |
| model artifact | Immutable future content used to instantiate a policy. |
| artifact identity | Content-bound identity; not a mutable path, name, tag or branch. |
| parent / child artifact | Auditable lineage relation created by an approved update or derivation. |
| checkpoint | Future training-state capture at an approved update point. |
| snapshot | Future immutable state capture with declared contents and use. |
| mutable policy | Policy eligible for separately approved updates; not evaluation eligible by implication. |
| frozen policy | Policy whose behavior-affecting identities are immutable for a declared use interval. |
| training policy | Mutable or declared training-only participant under a separately approved run. |
| validation policy | Frozen candidate used on a separately approved validation resource. |
| selection policy | Frozen candidate evaluated only for separately approved selection. |
| holdout evaluation policy | Frozen candidate eligible for a separately approved untouched holdout campaign. |
| reference / baseline / opponent policy | Separately identified comparison or interaction participant; not a strength benchmark by name. |
| candidate / promoted policy | Candidate is under review; promoted requires a separate decision and evidence. |
| training run | Separately approved update process with immutable configuration and lineage. |
| update step / schedule | Declared mutation event and ordering policy; neither is approved here. |
| freeze event | Auditable transition from a mutable lineage to a declared frozen use identity. |
| thaw / unfreeze event | End of frozen use; it creates a new use status and requires new review. |
| evaluation unit / campaign | Smallest eligible scored unit and the fixed collection/protocol that aggregates units. |
| validation / selection / holdout / test set | Separate future use classes whose reuse changes evidence eligibility. |
| ranked evidence | Later platform/ranked evidence under separate source and protocol approval. |
| model-use status / eligibility | Future governance classification; not an executable enum or self-declared permission. |
| checkpoint selection / early stopping | Future selection processes, not strength or promotion decisions. |
| hyperparameter / reward tuning | Adaptive use of results to alter behavior or optimization choices. |
| repeated evaluation / peeking | Reuse or inspection that may contaminate an untouched evidence claim. |
| contamination / leakage | Unauthorized information or feedback flow across training, selection and evaluation uses. |
| model-use manifest | Candidate future provenance record; no manifest or schema is approved. |
| non-evidence warning | Required warning preventing engineering or training records from becoming strength claims. |

Vocabulary definition approves no model, artifact, checkpoint, run, schema,
loader, evaluator or use. `Evaluation model` is a future use class, not
evaluation approval. `Frozen` requires immutable behavior-affecting identity,
not a mutable boolean flag. Promotion always requires a separate later-stage
decision.

## Authority Separation

| authority | future responsibility if separately approved | must not own |
|---|---|---|
| training process | approved mutable updates, optimizer/training state, update schedule, checkpoint-emission events and training diagnostics | holdout decisions, strength classification, promotion, environment authority or evidence grade |
| evaluation protocol | eligible units, frozen participant requirements, metric aggregation, invalid/incomplete handling and uncertainty reporting | policy updates, reward tuning, optimizer state, transitions or implied promotion |
| evidence governance | classify engineering, training, validation, strength, ranked, stable-dan, LuckyJ and promotion claims | training, inference or game-state authority |
| model-output interface | separately reviewed request/response handoff | training/evaluation use approval |
| environment | legality, applied action, transition, terminal state and raw outcome | policy mutation, reward meaning or strength claims |

Training and evaluation responsibilities remain separate even when they use
the same architecture or artifact lineage. No process is implemented now.

## Candidate Model-Use Classes

Every candidate class has `approved_now = no`, `selected_now = no`,
`execution_allowed_now = no` and `implementation_allowed_now = no`.

| candidate class | intended future use | principal risk | approved_now | selected_now | execution_allowed_now | implementation_allowed_now |
|---|---|---|---:|---:|---:|---:|
| mutable training policy | separately approved optimization | silent mutation and lineage loss | no | no | no | no |
| frozen validation policy | diagnostic validation | validation/holdout confusion | no | no | no | no |
| frozen checkpoint-selection policy | compare candidate checkpoints | repeated-comparison bias | no | no | no | no |
| frozen holdout evaluation policy | untouched final evaluation | peeking and contamination | no | no | no | no |
| frozen baseline/reference policy | bounded comparison | benchmark overclaim | no | no | no | no |
| frozen opponent policy | later interaction | opponent/seat selection bias | no | no | no | no |
| candidate-promotion policy | later promotion review | promotion by implication | no | no | no | no |
| historical checkpoint policy | reproducibility or comparison | hidden artifact drift | no | no | no | no |
| synthetic/local model-use contract smoke | future contract-only smoke | smoke mistaken for model execution | no | no | no | no |
| remote/third-party model use | future external service/artifact | rights, privacy and security | no | no | no | no |

No class is selected. Training policy does not mean training approval;
validation is not holdout; checkpoint selection is not strength evidence;
baseline comparison is not LuckyJ comparison; historical checkpoints do not
approve an opponent pool or league; synthetic smoke cannot impersonate model
execution; remote and third-party use remains blocked.

## Artifact / Checkpoint / Policy Identity Boundary

Future model use must bind separately versioned identities for:

```text
participant_id
participant_role
policy_id
policy_version
model_architecture_identity
artifact_id
immutable_artifact_content_identity
parent_artifact_id
training_run_id_if_approved
training_step_or_update_identity_if_approved
checkpoint_id_if_approved
snapshot_id_if_approved
code_revision
model_configuration_version
reward_objective_version
observation_model_output_contract_version
environment_protocol_ruleset_versions
backend_runtime_device_precision_identities
mutable_or_frozen_status
update_schedule_identity
freeze_event_identity
license_provenance_status
explicit_non_evidence_warning
```

Path, filename, display name, mutable tag or branch name is not immutable
identity. Content must not change under the same artifact identity. Parent/
child lineage does not approve a training run. These are candidate fields,
not an approved schema, manifest, hash algorithm, loader or artifact. No
checkpoint or model is loaded or created now.

## Mutable Training Policy Boundary

Future mutable training-policy use requires separate approval for:

- training data and the exact training run.
- mutable status, update schedule and update boundary.
- new artifact/version identity per approved update unit.
- parent/child artifact lineage.
- optimizer and training-state identity.
- reward/objective, environment/protocol and model-output contract identity.
- seeds, RNG and known nondeterminism.
- checkpoint-emission policy and retention.
- interruption, failure and restart lineage.

No policy may mutate silently within an episode. Between-episode updates are
not approved by implication. A mutable training policy cannot impersonate a
frozen evaluation participant. Training diagnostics are not evaluation
evidence. No trainer, optimizer, update loop or checkpoint emitter is
implemented.

## Frozen Evaluation Policy Boundary

Future frozen evaluation use requires:

- immutable artifact content identity.
- frozen code, configuration, runtime, backend, device and precision identity.
- frozen environment, protocol and ruleset identity.
- frozen observation and model-output contract identity.
- reward-independent evaluation semantics.
- no optimizer/training-state mutation, weight update or hidden update schedule.
- explicit recurrent/session reset and no cross-unit contamination.
- evaluation-unit and campaign identity.
- model-use eligibility and artifact-mismatch handling.

Freeze applies to every behavior-affecting identity, not weights alone. An
artifact cannot silently change between evaluation units. Thawing creates a
new use status, identity and review requirement. Frozen status says nothing
about quality. No evaluation participant is approved now.

## Within-Episode / Between-Episode Update Boundary

- Within-episode policy update is forbidden unless a future exact protocol
  defines and separately approves it.
- Current planning assumes no silent within-episode update.
- Between-episode update requires an explicit schedule and a new policy or
  artifact identity.
- An evaluation campaign may require one frozen identity across every unit.
- Checkpoint switching inside a campaign is forbidden unless separate
  candidates and units are declared in advance.
- Update events cannot overwrite earlier artifact identity or provenance.
- No update mechanism is implemented now.

## Training / Validation / Selection / Holdout Separation

Future governance must distinguish:

1. training use.
2. training-diagnostic use.
3. validation use.
4. hyperparameter/reward-tuning use.
5. checkpoint-selection use.
6. holdout evaluation use.
7. ranked/platform evidence use.
8. candidate-promotion use.

Training records do not automatically become validation evidence. Validation
is not holdout; selection data is not final evaluation; repeatedly inspected
holdout is no longer untouched. Ranked/platform evidence requires separate
source and protocol approval. Promotion requires an independent decision. No
current split, dataset, training run or evaluation set is approved.

## Checkpoint Selection / Early Stopping Boundary

Future checkpoint selection must declare:

- candidate checkpoint identities and generation process.
- selection data or episodes and their exact use status.
- selection metric, frequency and early-stopping rule.
- tie-breaking and repeated-comparison accounting.
- failure/incomplete-candidate handling.
- selected and non-selected checkpoint identities and retention policy.
- separation from final holdout and evidence limitations.

Selecting a checkpoint is not candidate promotion. Best validation score is
not model-strength evidence. No checkpoint exists or is loaded for this P8
work; no selection metric, early-stopping rule or repeated-comparison
correction is chosen.

## Hyperparameter / Reward-Tuning Leakage Boundary

Future leakage review must account for hyperparameter search, reward-weight
tuning, objective/architecture/seed/environment/checkpoint/opponent selection,
repeated evaluation, manual inspection, adaptive stopping and metric
cherry-picking.

Data, episodes or results used to tune a decision are no longer untouched
holdout. Evaluation feedback cannot silently flow into training. Reward tuning
against holdout must be disclosed. Repeated peeking changes evidence status.
No tuning or evaluation occurs now.

## Training-Self-Play vs Evaluation-Self-Play Model Use

Future training self-play may use only a separately approved mutable policy,
update schedule, training-only episode eligibility, diagnostics and opponent
policy. Future evaluation self-play requires frozen participant and opponent
identities, a separately approved environment and protocol, no training
updates and explicit evaluation eligibility.

Training episodes do not automatically become evaluation units. Evaluation
episodes do not automatically become training data. A training policy cannot
impersonate a frozen evaluation policy. No self-play use is approved now.

## Reference / Baseline / Opponent Policy Boundary

Future reference or opponent use requires immutable identity, provenance and
license status, mutable/frozen declaration, intended use, selection rationale,
environment/protocol compatibility, update policy, seat/opponent accounting,
eligibility and evidence limits.

A reference policy is not a strength benchmark by name. Baseline win rate is
not Tenhou evidence. No opponent pool or league is approved. Unknown or
unapproved third-party artifacts are forbidden. No reference or opponent
model is loaded now.

## Recurrent / Session / Cache Model-Use Boundary

Future use must distinguish model recurrent state, session/cache state,
environment state, participant observation and optimizer state. It requires:

- an evaluation reset policy.
- no cross-episode or cross-participant leakage.
- no training/evaluation state sharing.
- no state migration across artifact versions without review.
- explicit retry/cancellation reset behavior.
- frozen-evaluation recurrent-state policy.

No recurrent, cache or session implementation is approved.

## Model-Output Interface Dependency

The `12W`/`12X` boundary remains controlling:

- Training/evaluation use does not approve a model-output interface.
- Request/response identity remains separately governed.
- A model only proposes candidate output.
- Environment owns legality, applied action and transition.
- Hidden, opponent-private, future and post-outcome leakage is forbidden.
- Stale, duplicate, retry and fallback status remains explicit.
- No model loading, inference or action generation is approved.
- Use classification cannot bypass MO-E14 or MO-E15.

## Environment / Protocol / Reward / Outcome Version Binding

A future model-use record must bind protocol, environment/simulator, ruleset,
observation projection, legal-action contract, model-output contract,
reward/objective for training use, raw-outcome/provenance, evaluation protocol
and source/data-use status versions.

Environment or protocol changes may invalidate comparability. Reward changes
require a new training-use identity. Evaluation metric/protocol changes
require a new evaluation-use identity. A model-use record cannot detach from
upstream immutable identities. No manifest or schema is implemented.

## Evaluation Eligibility Boundary

Candidate future statuses include:

```text
eligible
ineligible
pending
invalid
incomplete
contaminated
training-use-only
validation-use-only
selection-use-only
holdout-eligible
ranked-evidence-ineligible
superseded
```

These are not an approved enum or schema. Eligibility is assigned only by
separately approved evaluation governance, never model self-declaration.
Incomplete, failed or mismatched units cannot become success. Training output
cannot silently become holdout eligible. No eligibility decision is made now.

## Failure / Timeout / Artifact-Mismatch Boundary

Future model-use records must preserve artifact/policy/version/model-output-
contract/environment/protocol mismatch, timeout, unavailable model,
incomplete unit, invalid episode, cancellation, resource failure, retry
lineage, replacement artifact identity and eligibility impact.

Silent retry and silent checkpoint substitution are forbidden. Failed units
remain visible; success-only filtering is forbidden. Replacing an artifact
creates a new evaluation identity. No failure handler or retry code is
implemented.

## Reproducibility Boundary

Future provenance should include artifact content identity, code/config
revision, training-run/update/checkpoint identity, backend/runtime/device/
precision, environment/protocol/reward versions, approved dataset/split
identity, seeds and nondeterminism, opponent/reference identities, evaluation
campaign identity, model-output contract and retry/failure lineage.

Same filename or seed alone is not reproducibility. Backend, precision and
device changes remain visible. Training reproducibility and evaluation
reproducibility are distinct claims. No reproducibility evidence is generated.

## Model-Strength Evidence Boundary

- Training loss is not model-strength evidence.
- Reward return is not model-strength evidence.
- Validation score is not final strength evidence.
- Selected checkpoint is not promoted-candidate evidence.
- Successful inference is not strength evidence.
- Legal-action rate is an engineering diagnostic only.
- Frozen evaluation is necessary but insufficient.

Strength evidence still requires an approved evaluation protocol, eligible
samples, sample size, uncertainty, leakage review, seat/opponent/version
accounting and governance approval. No model-strength evidence exists now.

## Tenhou / Stable-Dan / LuckyJ / Promotion Boundary

- No current P8 model is Tenhou validated.
- No current P8 model has stable-dan evidence.
- No current artifact supports a LuckyJ `10.68` comparison.
- No candidate promotion is approved.
- Ranked/platform evidence requires separate source, protocol, privacy and
  platform approval.
- The north-star target cannot become training or evaluation approval.
- P10, P11 and P12 remain later-stage and unapproved.

## Source / Real-Data / Privacy / Third-Party Boundary

No source, ingestion, real Tenhou, real haifu, external log, platform data,
account/session/cookie/token/API key, remote model service, unknown checkpoint,
third-party binary, Akochan `system.exe` or `libai.so` is approved. Future use
requires separate rights, privacy, security, license and provenance review.
Model-use records must not contain secrets. No download, loading or external
execution occurs now.

## Candidate Model-Use Record Fields

Candidate future fields only:

```text
model_use_record_id
model_use_record_version
use_class
use_status
eligibility_status
participant_id
participant_role
policy_id
policy_version
model_architecture_identity
artifact_id
artifact_content_identity
parent_artifact_id
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
observation_projection_version
model_output_contract_version
raw_outcome_provenance_version
evaluation_protocol_version
backend_identity
runtime_identity
device_identity
precision_identity
mutable_or_frozen_status
update_schedule_identity
freeze_event_identity
evaluation_unit_id
evaluation_campaign_id
validation_use_status
selection_use_status
holdout_use_status
ranked_evidence_status
retry_status
failure_status
contamination_status
leakage_review_status
source_status
real_data_status
training_status
evaluation_status
self_play_status
league_status
model_strength_status
provenance_status
explicit_non_evidence_warning
```

These are not an approved schema, API, manifest, JSON fixture, parser, reader,
checkpoint/model loader or trainer/evaluator configuration. No code or data is
created.

## Evidence Boundary

Current evidence grade:

```text
P8 training / evaluation model-use boundary definition evidence only.
```

It supports training/evaluation vocabulary readiness, mutable/frozen
separation readiness, artifact/update/freeze/eligibility planning, leakage
controls and future review. It supports no P8 entry/implementation, training
or evaluation approval, model/checkpoint loading, training/evaluation run,
checkpoint selection, self-play/RL, model-output runtime, strength/Tenhou/
stable-dan/LuckyJ/promotion evidence or P9-P12 approval.

## Future Model-Use Entry Criteria

- TU-E1. P8 scope review is closed.
- TU-E2. P8 risk/evidence taxonomy review is closed.
- TU-E3. P8 self-play/RL dependency-map review is closed.
- TU-E4. P8 self-play protocol boundary review is closed.
- TU-E5. P8 objective/reward boundary review is closed.
- TU-E6. P8 environment/simulator boundary review is closed.
- TU-E7. P8 raw-outcome/provenance boundary review is closed.
- TU-E8. P8 model-output interface dependency boundary review is closed.
- TU-E9. Training/evaluation model-use boundary is defined and reviewed.
- TU-E10. Artifact/update/freeze/lineage semantics are reviewed.
- TU-E11. Training/validation/selection/holdout separation is reviewed.
- TU-E12. Leakage/contamination/eligibility/failure handling is reviewed.
- TU-E13. Training-data, training-run, evaluation, source and third-party
  status remain separately governed.
- TU-E14. A separate approval decision authorizes one exact future task.
- TU-E15. `docs/10_next/10_NEXT.md` authorizes that exact future task.

None of TU-E1 through TU-E15 is implementation approval. Defined/reviewed
does not mean a model is loaded, trained or evaluated. TU-E14 and TU-E15 are
hard gates before any model/checkpoint/training/evaluation code, fixture or
data work.

## Stop Conditions

Stop if a future task implies P8 entry/implementation, generates an
implementation prompt without approval, loads or creates a model/checkpoint/
weight/snapshot, runs training/tuning/evaluation/checkpoint selection/early
stopping, mutates a frozen model, substitutes artifacts silently, reuses
validation/selection as holdout, repeatedly peeks without changing evidence
status, leaks evaluation feedback into training, mixes training/evaluation
episodes, hides failed/incomplete units, treats training loss/return/
validation as strength, runs self-play/RL/league, implements model-output
integration, accesses real/platform data, creates code/tests/fixtures/data,
claims Tenhou/stable-dan/LuckyJ/promotion evidence, enters P9-P12, changes
`10_NEXT` to implementation without separate approval or uses unknown/
third-party artifacts.

## Candidate Next Directions

| candidate | current_status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this training/evaluation model-use boundary. | available | checks identity, freeze, separation, leakage and eligibility | low if review-only | none | yes | no | low | low | selected |
| B. Define model/artifact provenance manifest boundary. | deferred | strengthens identity/lineage | schema creep | this review | yes | no | medium | low | defer |
| C. Define training-data and training-run dependency boundary. | deferred | prepares exact run governance | training-approval creep | separate source/data review | yes | no | high | medium | defer |
| D. Define evaluation protocol/metric boundary. | deferred | prepares eligible evaluation | execution/strength creep | this review | yes | no | high | medium | defer |
| E. Define model-output validation evidence boundary. | deferred | prepares contract conformance | test/runtime creep | model-output review | yes | no | medium | low | defer |
| F. Define checkpoint-selection/early-stopping boundary. | deferred | controls selection leakage | premature checkpoint work | this review | yes | no | high | medium | defer |
| G. Define RL algorithm-selection boundary. | deferred | prepares later method review | execution creep | multiple P8 gates | yes | no | high | medium | defer |
| H. Prepare P8 entry approval decision. | rejected now | could advance stage | criteria incomplete | multiple gates | yes | no | high | medium | reject |
| I. Draft P8 implementation proposal. | forbidden | none now | premature implementation | exact approval absent | no | no | high | high | forbid |
| J. Load a model/checkpoint. | forbidden | none now | artifact/use unapproved | TU-E9-TU-E15 | no | no | high | high | forbid |
| K. Run training/tuning. | forbidden | none now | data/run unapproved | TU-E9-TU-E15 | no | no | high | high | forbid |
| L. Run evaluation/checkpoint selection. | forbidden | none now | protocol/eligibility unapproved | TU-E9-TU-E15 | no | no | high | high | forbid |
| M. Execute self-play/RL/league. | forbidden | none now | execution unapproved | multiple gates | no | no | high | high | forbid |
| N. Start real-data/Tenhou work. | forbidden | none now | rights/privacy/platform risk | separate approvals | no | no | high | high | forbid |
| O. Claim strength or enter P9-P12. | forbidden | none now | evidence/stage jump | later stages | no | no | high | high | forbid |

Selected next direction:

```text
Review P8 training / evaluation model-use boundary before any implementation.
```

## Planning Decision

```text
P8 training / evaluation model-use boundary is defined before any implementation.
```

This decision does not approve P8 entry/implementation or an implementation
prompt, training data/run, training/tuning, evaluation approval/execution,
model/checkpoint/weight loading, checkpoint/snapshot creation, inference/action
generation, model-output integration, self-play/RL/league, source/real-data
use, strength/Tenhou/stable-dan/LuckyJ/promotion evidence or P9-P12 entry. The
next safe task is a docs-only review of this boundary.

## Evidence Grade

```text
P8 training / evaluation model-use boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P8 entry, implementation approval, an implementation prompt or executable task.
- training-data/training-run approval, training, tuning or optimizer work.
- evaluation approval/execution, holdout evaluation or checkpoint selection.
- a model, policy, checkpoint, weight, snapshot, loader or artifact.
- checkpoint/snapshot creation, trainer, optimizer, loss or dataloader.
- inference, action generation or model-output integration.
- environment, episode, self-play, RL or league execution.
- source approval/ingestion or real Tenhou/haifu/external/platform data.
- model/policy strength, Tenhou ranked, stable-dan or LuckyJ evidence.
- candidate promotion or P9-P12 approval.

## Validation

Required validation for this docs-only task:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

No model/checkpoint/weight loading, inference, training, tuning, evaluation,
checkpoint selection, self-play/RL, league, environment execution, real-data,
Tenhou/platform, strength-evidence or third-party command is permitted.
