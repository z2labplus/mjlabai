# 12O_P8_SELF_PLAY_PROTOCOL_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 self-play protocol boundary before any
implementation. It is a docs-only planning artifact.

This task is not P8 entry approval, P8 implementation approval, a P8
implementation prompt, a P8 first executable task, self-play or RL execution,
training, tuning, evaluation, league, opponent-pool execution, source approval
or ingestion, real-data access, broad file ingestion, CLI work, feature or
label generation, dataset construction, model-output integration, strength
evidence, Tenhou ranked evidence, stable-dan evidence, LuckyJ `10.68`
comparison, candidate promotion or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` target only by making any future self-play run auditable,
reproducible and separable from evaluation evidence. It is not evidence that a
model can beat LuckyJ.

## Full P7 / P8 Planning Recap

- Full P7 is closed only for the documented P7 supervised-learning scope.
- `12I` defined P8 scope and entry criteria; `12J` reviewed it.
- `12K` defined P8 risks R1-R20 and evidence families E1-E25; `12L` reviewed
  that taxonomy.
- `12M` defined the P8 self-play / RL dependency map; `12N` reviewed it and
  recorded `A. Review can close.`
- P8 remains docs-only planning. P8 entry and implementation are unapproved.
- P9-P12 remain unapproved.

## P8 Self-Play Protocol Non-Approval Baseline

- No self-play protocol is approved for execution.
- No runner, environment or simulator exists or is approved.
- No participant policy, checkpoint, model-output path or training loop is
  approved.
- No RL objective, reward, opponent pool or league is approved.
- No real-data source is approved.
- No self-play evidence currently exists.
- No self-play result is model-strength evidence by default.

## Protocol Vocabulary

| term | boundary meaning |
|---|---|
| protocol definition | Reviewed rules for a future run; not execution permission. |
| protocol version | Immutable identifier for one protocol definition. |
| run | A future bounded collection of episodes under one manifest. |
| episode | One future initialized-to-terminated interaction sequence. |
| match | A future comparison unit that may contain one or more episodes. |
| participant | A future policy-bearing actor in an episode. |
| participant role | Seat, control role or other explicit assignment. |
| policy identity | Immutable identity of the participant policy behavior. |
| artifact identity | Auditable identity for code, configuration or weights. |
| checkpoint identity | Immutable checkpoint identifier, if separately approved. |
| environment / simulator identity | Versioned identity of the future transition authority. |
| ruleset version | Immutable rules configuration for a run. |
| seed | Recorded input to a declared random process. |
| seat / role assignment | Explicit mapping from participants to episode roles. |
| observation | Decision-time information supplied to a participant. |
| decision-time information | Information legally available at the decision point. |
| legal action set | Actions authorized by a separately approved environment. |
| selected / fallback action | Chosen action, or separately specified fallback if ever approved. |
| transition | State change applied by a separately approved environment. |
| terminal condition | Declared condition that normally ends an episode. |
| termination reason | Recorded cause for normal, invalid or aborted termination. |
| invalid / aborted episode | Episode that fails protocol validity or cannot continue. |
| retry | Explicit repeat governed by a declared retry policy. |
| provenance record | Auditable identities, versions, seeds and status metadata. |
| protocol manifest | Future run/episode configuration and provenance contract. |
| raw outcome | Uninterpreted terminal result; not reward or strength evidence. |
| training self-play | Future protocol class whose data may feed approved training only. |
| evaluation self-play | Separate future protocol class with frozen evaluation rules. |
| opponent pool | Future approved set and selection policy for opponents. |
| frozen / mutable policy | Policy update status explicitly declared by protocol class. |
| protocol evidence | Evidence that protocol rules were followed, not strength evidence. |
| non-evidence warning | Required warning preventing stronger unsupported claims. |

Vocabulary definition does not approve implementation or execution.

## Candidate Protocol Classes

| protocol_class | purpose | approved_now | execution_allowed_now | boundary note |
|---|---|---:|---:|---|
| synthetic/local protocol smoke | Future minimal protocol-shape validation | no | no | Requires a separate reviewed proposal and approval. |
| training self-play protocol | Future generation of training interactions | no | no | Must not double as evaluation. |
| frozen-policy evaluation self-play | Future controlled comparison of frozen policies | no | no | Is not strength evidence without an approved evaluation protocol. |
| opponent-pool protocol | Future opponent sampling and diversity control | no | no | Pool and sampling policy remain unapproved. |
| league protocol | Future league scheduling and promotion support | no | no | Later-stage P10 work. |

No protocol class is approved by this document. Training self-play and
evaluation self-play are separate. Neither an evaluation self-play label nor a
raw result creates model-strength evidence.

## Participant and Artifact Identity Boundary

A future protocol must record:

- `participant_id`, `participant_role` and `policy_version`.
- `artifact_id` plus an artifact hash or another immutable identifier.
- `checkpoint_id` only if a later approval permits checkpoints.
- code revision, configuration revision, ruleset version, environment version
  and protocol version.

Participant identity must be explicit. Policy behavior must not silently
change within an episode. Artifact provenance must be auditable. Unknown
weights or checkpoints are forbidden. No current or third-party artifact is
approved for self-play.

## Episode Lifecycle Boundary

A future episode lifecycle must be defined as:

1. Validate the protocol manifest.
2. Validate participant and artifact identities.
3. Validate ruleset and environment versions.
4. Assign seeds and seats or roles.
5. Initialize episode state.
6. Produce a decision-time observation.
7. Obtain an action only through a separately approved model-output boundary.
8. Validate action legality.
9. Apply a legal transition.
10. Repeat until normal terminal, invalid or aborted.
11. Record termination reason and raw outcome.
12. Persist provenance and integrity records.
13. Separate valid, invalid and aborted episodes.
14. Never silently discard or silently retry an invalid episode.

This lifecycle is descriptive only. No environment, runner or model call is
implemented; no action is generated and no episode is executed.

## Information and Observation Boundary

A future protocol must require decision-time information only, no hidden or
future information leakage, no post-outcome information, and no opponent
private state unless rules explicitly make it public. Observation schemas must
be versioned, public/private fields classified and provenance auditable.

This task does not implement an observation encoder, generate feature tensors
or connect feature extraction. Existing synthetic/local smoke tests do not
approve self-play observations.

## Action and Legality Boundary

A future protocol must require a legal-action set from a separately approved
environment. A selected action must belong to that set. Illegal-action and
fallback policies must be explicit, deterministic and auditable. There must be
no silent correction, unlogged fallback or hidden illegal-action rate.

This task does not implement a legal-action engine, action reconstruction,
action sampler, fallback policy or environment transition.

## Seed and Reproducibility Boundary

A future protocol must record:

- `run_seed`, `episode_seed`, participant ordering and seat assignment.
- environment and protocol versions, configuration hash and artifact identity.
- retry policy, deterministic replay expectations and known nondeterministic
  components.

The same seed alone does not prove full reproducibility. Nondeterminism must be
declared, and retries must not silently alter evidence. This task produces no
reproducibility result.

## Termination, Abort and Invalid-Episode Boundary

A future protocol must distinguish normal/rules terminal, timeout, invalid
action, environment error, participant error, artifact mismatch, protocol
mismatch, manual cancellation, resource failure and unknown failure.

Each episode must record `termination_reason`, a `valid_episode` flag,
`abort_reason`, `retry_count`, `evidence_eligibility`, raw-outcome availability
and provenance completeness. Invalid or aborted episodes cannot silently enter
training or evaluation evidence.

## Protocol Manifest Boundary

Candidate future manifest fields are:

```text
protocol_id
protocol_version
run_id
episode_id
protocol_class
ruleset_version
environment_version
participant_ids
participant_artifact_ids
participant_policy_versions
frozen_within_episode
run_seed
episode_seed
seat_assignment
observation_boundary_version
action_legality_boundary_version
termination_policy_version
retry_policy
provenance_version
source_status
real_data_status
training_status
evaluation_status
self_play_status
league_status
model_strength_status
explicit_non_evidence_warning
```

These fields are not an approved implementation schema. This task creates no
JSON fixture, data file or code.

## Training-Self-Play vs Evaluation-Self-Play Separation

- Training and evaluation self-play are distinct protocol classes.
- Training episodes cannot automatically become holdout evaluation.
- Evaluation participants require separately approved freezing and version
  rules; updates cannot occur silently within an evaluation episode.
- Result reuse requires explicit approval.
- Raw outcomes and win rate alone are not model-strength evidence.
- No training or evaluation is approved now.

## RL Objective / Reward Boundary

Self-play protocol semantics must precede reward/objective specification. A
separate docs-only boundary and review are required for reward definition.
Reward must not be inferred automatically from protocol raw outcomes, and
reward-hacking/objective-mismatch risks remain open. No RL algorithm, loss or
final reward is selected or implemented, and no RL execution is approved.

## Opponent Pool and League Boundary

No opponent pool, matchmaking policy, historical-checkpoint pool, league,
mainline promotion or candidate promotion is approved. League belongs to P10
unless governance later changes that boundary. Opponent diversity claims need
separate evidence, and self-play against copies of one policy is not robust
evidence by default.

## Source / Real-Data Boundary

This protocol boundary approves no real data. It uses no Tenhou data, external
logs, platform data, account/session/cookie/token material or real haifu.
Future real-data use requires separate rights, privacy, platform-policy,
approval and ingestion chains. Future self-play-generated data also requires a
separate provenance/data boundary. No self-play data is created now.

## Model-Output Boundary

No model-output integration, model interface or checkpoint is approved. No
logits, values or policy distributions are produced. Future model calls require
separate interface, schema, environment, evaluation, risk review and approval.
Protocol definition does not authorize a model call.

## Evidence Boundary

Current evidence grade:

```text
P8 self-play protocol boundary definition evidence only.
```

This supports protocol-vocabulary, lifecycle, information/action,
reproducibility and future-review readiness only. It does not support P8 entry
or implementation approval, self-play result evidence, RL/training/evaluation/
league/model-output evidence, strength evidence, Tenhou ranked evidence,
stable-dan evidence, LuckyJ `10.68` comparison or candidate promotion.

## Future Protocol Entry Criteria

- SP-E1. P8 scope review is closed.
- SP-E2. P8 risk/evidence taxonomy review is closed.
- SP-E3. P8 self-play/RL dependency-map review is closed.
- SP-E4. Self-play protocol boundary is defined and reviewed.
- SP-E5. Environment/simulator boundary is defined and reviewed.
- SP-E6. Participant/artifact identity boundary is defined and reviewed.
- SP-E7. Observation/information boundary is defined and reviewed.
- SP-E8. Action-legality/fallback boundary is defined and reviewed.
- SP-E9. Seed/reproducibility boundary is defined and reviewed.
- SP-E10. Termination/abort/invalid-episode policy is defined and reviewed.
- SP-E11. Model-output interface dependency is defined and reviewed.
- SP-E12. Training/evaluation self-play separation is defined and reviewed.
- SP-E13. Source/real-data status remains explicit and separately governed.
- SP-E14. A separate approval decision authorizes an exact future task.
- SP-E15. `docs/10_next/10_NEXT.md` authorizes that exact future task.

None of SP-E1 through SP-E15 is implementation approval by itself.

## Stop Conditions

Stop if a future task implies P8 entry/implementation approval, generates an
implementation prompt, starts self-play/RL/training/tuning/evaluation/league,
selects an RL algorithm for execution, defines reward without a separate gate,
calls a model/checkpoint, uses unknown artifacts or real/external/platform
data, approves ingestion, creates code/tests/fixtures/data/runners/environments,
claims strength/Tenhou/stable-dan/LuckyJ/promotion evidence, enters P9-P12,
changes `10_NEXT` to implementation without separate approval, or requires
Akochan `system.exe`, `libai.so` or another third-party binary.

## Candidate Next Directions

| candidate | current_status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this protocol boundary. | available | Checks completeness and non-approval semantics. | Low if review-only. | none | yes | no | low | low | selected |
| B. Define RL objective/reward boundary. | deferred | Controls reward semantics. | Could imply RL approval. | protocol review | yes | no | medium | low | defer |
| C. Define environment/simulator boundary. | deferred | Clarifies transition authority. | Could imply executable environment. | protocol review | yes | no | medium | low | defer |
| D. Define model-output interface dependency. | deferred | Clarifies participant calls. | Could imply model loading. | protocol/environment reviews | yes | no | medium | low | defer |
| E. Define training/evaluation dependency boundary. | deferred | Separates run purposes. | Broad downstream scope. | protocol/objective reviews | yes | no | medium | low | defer |
| F. Prepare P8 entry approval decision. | rejected now | Could advance governance. | Entry prerequisites remain incomplete. | SP-E4-SP-E15 | yes | no | high | medium | reject |
| G. Draft P8 implementation proposal. | forbidden | None now. | Premature implementation path. | P8 entry and exact approval | no | no | high | high | forbid |
| H. Start P8 implementation. | forbidden | None now. | Stage jump. | all implementation gates | no | no | high | high | forbid |
| I. Start self-play/RL. | forbidden | None now. | No protocol or approval. | protocol and execution gates | no | no | high | high | forbid |
| J. Start training/tuning. | forbidden | None now. | No data/run approval. | training gates | no | no | high | high | forbid |
| K. Start league. | forbidden | None now. | P10 stage jump. | P10 scope/evaluation | no | no | high | high | forbid |
| L. Start real-data/Tenhou work. | forbidden | None now. | Rights/platform risk. | source review | no | no | high | high | forbid |
| M. Integrate model output or claim strength. | forbidden | None now. | Interface/evidence overclaim. | model/evaluation approvals | no | no | high | high | forbid |
| N. Enter P9-P12. | forbidden | None now. | Stage jump. | separate stage scopes | no | no | high | high | forbid |

Selected next direction:

```text
Review P8 self-play protocol boundary before any implementation.
```

## Planning Decision

```text
P8 self-play protocol boundary is defined before any implementation.
```

This task approves no P8 entry, implementation, implementation prompt,
self-play/RL execution, training, tuning, evaluation, league, source/real-data
work, model-output integration, strength claim, candidate promotion or P9-P12
entry. The next safe task is a docs-only review of this boundary.

## Evidence Grade

```text
P8 self-play protocol boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not P8 entry/implementation approval, an implementation
prompt or executable task, self-play/RL/training/tuning/evaluation/league,
source approval/ingestion, real Tenhou/haifu/external/platform data,
model-output integration, model-strength/Tenhou-ranked/stable-dan/LuckyJ or
promotion evidence, or P9-P12 approval.

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
