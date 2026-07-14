# 12S_P8_ENVIRONMENT_SIMULATOR_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 environment / simulator authority boundary before
any implementation. It is a docs-only planning artifact.

This task is not P8 entry or implementation approval, an implementation
prompt or first executable task, environment/simulator/runner/reset/step/
transition/legal-action/observation implementation, episode/match/self-play/RL
execution, reward/objective/loss implementation, RL algorithm selection,
training, tuning, evaluation, league, source approval/ingestion, real-data
access, model-output integration, strength evidence or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` goal only by requiring future game-state transitions,
legality, randomness, termination and raw outcomes to have one auditable
authority. It is not an environment implementation and provides no evidence
that a model can beat LuckyJ.

## Full P7 / P8 Planning Recap

- Full P7 is closed only for documented P7 supervised-learning scope.
- `12I`/`12J` defined and reviewed P8 scope and entry criteria.
- `12K`/`12L` defined and reviewed the P8 risk/evidence taxonomy.
- `12M`/`12N` defined and reviewed P8 self-play/RL dependencies.
- `12O`/`12P` defined and reviewed the P8 self-play protocol boundary.
- `12Q`/`12R` defined and reviewed the P8 objective/reward boundary.
- `12R` recorded `A. Review can close.`
- P8 remains docs-only planning; entry and implementation are unapproved.
- P9-P12 remain unapproved.

## Environment / Simulator Non-Approval Baseline

- No P8 self-play-specific environment, simulator or runner is approved for
  execution.
- No reset, step, transition, episode or match API is approved.
- No rules engine, legal-action authority or observation projection is
  approved for P8 execution.
- No RNG implementation, seed policy, model-output path, reward-execution path
  or training/evaluation environment is approved.
- No self-play, RL, training or evaluation result exists.
- Current environment evidence is docs-only boundary planning only.
- No current artifact is model-strength or ranked evidence.

This is scoped wording. It is not a repository-global claim that no helper,
test harness, wrapper or historical environment concept exists.

## Environment / Simulator Vocabulary

| term | boundary meaning |
|---|---|
| environment | Abstract future authority for state, rules, legality, transition, termination and raw outcome. |
| simulator | Future execution carrier or approximation that may implement a reviewed environment boundary. |
| authoritative transition system | Single declared source of truth for applying a valid action to authoritative state. |
| transition / rules / legality authority | Ownership of state change, rules interpretation and legal-set determination. |
| observation projection | Versioned participant-specific view derived from authoritative state. |
| authoritative state | Complete environment-owned episode state, including fields hidden from participants. |
| public / private / hidden state | Visibility classification for state fields. |
| state snapshot / version | Candidate immutable state identity and representation version. |
| ruleset version | Immutable interpretation identity for one episode. |
| reset / initialization | Explicit atomic establishment of one episode state and manifest. |
| step / transition | Future single authoritative action-validation and state-change operation. |
| event / action | Versioned occurrence or participant proposal; an action is not authoritative until validated/applied. |
| legal action set | Environment-derived candidate actions valid for the current authoritative state. |
| selected / applied / fallback action | Proposed action, authoritative accepted action and separately governed fallback. |
| invalid action | Candidate action rejected under the current authoritative legal set. |
| stochastic process / RNG | Versioned randomness source and state owned by the future environment. |
| run / episode seed | Inputs to a declared RNG policy, not complete reproducibility evidence. |
| seat / role assignment | Versioned participant placement and asymmetric-role policy. |
| terminal state / raw outcome | Environment-determined end state and uninterpreted versioned result. |
| invalid / aborted episode | Episode unable to support normal terminal processing or declared valid use. |
| timeout / resource failure | Explicit termination classes, never silent filtering rules. |
| environment / participant error | Failure attributed to authority or participant under a stable category. |
| deterministic replay | Future expectation that declared inputs and versions reproduce transitions. |
| reproducibility | Identity, versions, seeds, configuration, artifacts and known nondeterminism together. |
| state / transition hash | Future integrity identities; no hash implementation is approved now. |
| invariant | Future declared integrity condition, not current executable validation. |
| environment / simulator identity | Immutable future identity/version of authority and execution carrier. |
| environment manifest | Candidate provenance record; it is not an approved schema. |
| environment evidence | Evidence about an approved environment process, not policy strength by default. |
| non-evidence warning | Required statement preventing environment artifacts from overclaim. |

Environment is the abstract authoritative boundary. A simulator may later
implement or approximate it, but a simulator is not automatically the rules
authority. Vocabulary definition approves neither implementation nor
execution.

## Environment vs Simulator Authority Boundary

| owner | future authority boundary | does not own |
|---|---|---|
| environment authority | state initialization, ruleset interpretation, legal-action determination, accepted-action validation, state transition, randomness, terminal determination, raw-outcome production, invariants and environment errors | reward meaning, evaluation conclusions or model policy |
| participant/model | proposes a candidate action under a separately approved interface | legal set, transition, terminal/raw outcome or hidden-state visibility |
| protocol | participant/artifact identities, protocol class, run/episode identity, seed and seat policy, retry policy and provenance requirements | authoritative state transition or reward mapping |
| reward specification | future approved mapping from versioned events/raw outcome to training signal | transition, legality, termination or evaluation authority |
| evaluation protocol | future approved interpretation and aggregation of frozen outputs/outcomes | training reward or environment transition authority |

A future model output is only a candidate action. The environment must
independently validate legality, must not silently accept or rewrite an
illegal action and must not embed an unapproved reward.

## Candidate Environment Classes

| candidate_class | intended purpose | authority level | major risks | prerequisites | approved_now | execution_allowed_now | implementation_allowed_now | cannot_support | notes |
|---|---|---|---|---|---:|---:|---:|---|---|
| synthetic/local environment-contract smoke | later validate a minimal contract with project-authored inputs | contract-level only | smoke mistaken for self-play approval | reviewed schema/approval | no | no | no | strength or self-play | no class selected |
| training self-play environment | later produce training episodes | full transition authority | reward leakage, nondeterminism, exploit | protocol/reward/model/run approvals | no | no | no | evaluation by default | distinct future use |
| frozen-policy evaluation environment | later run frozen diagnostic/evaluation episodes | full transition authority | leakage/version drift/overclaim | evaluation/freeze approvals | no | no | no | strength by default | no evidence exists |
| opponent-pool environment | later coordinate approved opponents | transition plus pool context | distribution bias/cycling | pool and matchmaking review | no | no | no | league approval | opponent pool unapproved |
| league environment | later support P10 league semantics | later-stage authority | P10 stage jump/promotion leakage | P10 scope/approval | no | no | no | current P8 work | later stage only |
| deterministic replay/audit environment | later audit versioned synthetic/local transitions | replay/audit authority only | mistaken real-log approval | replay/provenance review | no | no | no | real Tenhou/log access | no real data approved |

Synthetic/local smoke is not self-play approval. Training and evaluation uses
are separate. Evaluation does not automatically produce strength evidence.
Opponent-pool and league uses remain unapproved. No class is selected for
implementation.

## Authoritative State Boundary

A future environment must require:

- one explicit authoritative state per episode and one immutable episode ID.
- versioned state representation, explicit owner and participant projection.
- explicit public, private, hidden and audit-only field classification.
- no participant access to authoritative hidden state.
- no cross-episode mutable-state leakage.
- no silent state repair or rollback.
- later-approved snapshots/hashes, declared invariants and auditable
  transition lineage.

This task defines no executable state schema, object, class, fixture, hash or
invariant checker.

## Reset / Initialization Boundary

Future reset/initialization must bind protocol/environment/ruleset IDs and
versions, run/episode IDs, participant and artifact/policy versions, run and
episode seeds, seat/role assignment, initial-state provenance, resource-budget
version, initialization status and any non-first reset reason.

Reset must be explicit and atomic. Previous episode state cannot leak. Retry
reset cannot silently reuse or replace state, and retry lineage must remain
auditable. Failed initialization creates an invalid/aborted record. No episode
may begin without a valid manifest. No reset code is implemented now.

## Step / Transition Contract Boundary

Candidate future step input concepts:

```text
protocol_version
environment_version
ruleset_version
episode_id
step_index
acting_participant_or_role
pre_state_identity_or_hash
candidate_action
action_source_identity
action_source_version
timeout_or_resource_context
```

Candidate future step output concepts:

```text
legality_decision
applied_action
events
post_state_identity_or_hash
next_acting_participant
terminal_flag
termination_reason
raw_outcome_availability
environment_error_status
provenance_record
```

These are candidate concepts, not an approved API/schema. No Python interface,
JSON schema, fixture, parser, reader or transition is created. A transition
must eventually be one authoritative operation. Rejected actions cannot
create unrecorded transitions; step indices cannot silently jump; duplicate
steps cannot silently apply.

## Ruleset and Legality Authority Boundary

A future environment must keep one immutable ruleset version per episode,
derive the legal set only from authoritative state and validate the selected
action against that set. A participant/model cannot supply the authoritative
legal set. Illegal-action handling must be explicit, with no silent
substitution, unlogged fallback or hidden denominator. Ruleset mismatch must
produce an explicit invalid/abort outcome.

Legality evidence is not policy-strength evidence. This task implements no
legal-action reconstruction, rules engine, fallback, correction or step.

## Information / Observation Projection Boundary

Future boundaries must separate authoritative state, public state,
acting-participant private information, opponent-private information,
hidden/random state, decision-time observation, post-outcome information and
audit-only information.

Observations must be participant-specific versioned projections from
authoritative state, bound to environment/ruleset versions and provenance.
Hidden, future, post-outcome and opponent-private leakage is forbidden. Audit
records may be broader but cannot be passed to a policy. Environment internal
state is not model input by default. No encoder, feature tensor, model input
or dataset example is implemented.

## Randomness / RNG / Seed Boundary

A future environment must define RNG ownership, algorithm/version, run seed,
episode seed, substream/component seeds, shuffle/draw/stochastic sources, seat
seed, retry seed policy, participant ordering, known nondeterminism, time/
resource nondeterminism and deterministic-replay expectation.

The same seed alone does not prove reproducibility. Untracked global mutable
RNG is forbidden. Parallel episodes require isolated RNG state. Retries cannot
silently alter evidence, seed reuse must be explicit, and environment version
changes invalidate naive seed equivalence. No RNG code is implemented.

## Seat / Role Assignment Boundary

Future environment/protocol records must include assignment method/seed,
participant order, seat/role balance plan, asymmetric starting conditions,
rotation, duplicate/mirror policy, comparison grouping and balance-report
requirements.

Seat assignment can bias reward/evaluation and its context must be retained.
Self-copy play does not prove generalization. No seat/match scheduler or
opponent pool is implemented or approved.

## Terminal / Raw-Outcome Authority Boundary

The future environment is authoritative for terminal flag, termination
reason, valid/invalid/aborted status, raw outcome, outcome-schema version,
outcome provenance, completeness and the input to later evidence-eligibility
decisions.

Raw outcome is not reward, evaluation result or strength evidence. A
participant/model cannot supply terminal status or raw outcome. Post-terminal
transition is forbidden unless separately modeled and logged. No raw-outcome
schema or calculator is implemented now.

## Error / Abort / Timeout / Resource Boundary

A future environment must distinguish invalid action, participant error,
environment error, ruleset/state-invariant/artifact/protocol mismatch,
timeout, memory/resource/concurrency failure, manual cancellation and unknown
failure.

Future records must include stable error class/code, termination reason,
episode validity, abort reason, retry permission/count/lineage, original and
retry seeds, resource-budget version, evidence eligibility, raw-outcome
availability and provenance completeness.

Silent retry, success-only filtering, timeout extension, resource-budget
change or admission of invalid/aborted episodes into training/evaluation is
forbidden. No error handling is implemented.

## Concurrency and Episode-Isolation Boundary

Future parallel execution requires unique run/episode identity, isolated
authoritative and RNG state, isolated participant/model state where required,
deterministic event-order policy, no shared mutable episode state, no
cross-episode observation leakage, no checkpoint mutation in frozen
evaluation, versioned concurrency configuration, race detection and auditable
partial-failure handling.

Parallel execution, workers, queues, process pools and distributed runners are
unapproved. Concurrency planning is not scaling approval; compute escalation
requires separate governance.

## Invariant and Integrity Boundary

Candidate future invariants include state-transition validity, ruleset,
participant/seat and legal-action consistency, monotonic step index, no
impossible state, no duplicate transition, terminal-state immutability,
provenance completeness, artifact/version consistency and declared replay
expectation.

No mahjong assertion, invariant test or validator is implemented. Passing an
invariant would not automatically establish policy strength.

## Environment Identity / Version / Provenance Boundary

Future records must bind:

```text
environment_id
environment_version
simulator_id
simulator_version
ruleset_id
ruleset_version
protocol_id
protocol_version
state_schema_version
observation_projection_version
legality_policy_version
transition_policy_version
RNG_version
termination_policy_version
raw_outcome_schema_version
retry_policy_version
resource_policy_version
code_revision
configuration_revision
artifact_hashes
explicit_non_evidence_warning
```

Environment version changes may invalidate comparability and cannot be
silent. Protocol/reward/model records must reference immutable environment
identity. These fields are candidates only, not schema approval; no manifest
code or fixture is created.

## Candidate Environment Manifest Boundary

Candidate future manifest fields are:

```text
environment_manifest_id
environment_id
environment_version
simulator_id
simulator_version
ruleset_id
ruleset_version
protocol_id
protocol_version
state_schema_version
observation_projection_version
legality_policy_version
transition_policy_version
RNG_version
termination_policy_version
raw_outcome_schema_version
retry_policy_version
resource_policy_version
participant_ids
participant_artifact_ids
run_id
episode_id
run_seed
episode_seed
seat_assignment
concurrency_mode
deterministic_replay_expectation
source_status
real_data_status
model_output_status
reward_status
training_status
evaluation_status
self_play_status
league_status
model_strength_status
explicit_non_evidence_warning
```

These are candidate fields only. They are not an approved schema, API, JSON
fixture, parser/reader, environment implementation, training configuration or
model configuration.

## Reward / Objective Interface Boundary

The future environment may emit only versioned events/raw outcomes under its
authority. It cannot silently define training reward. Reward mapping remains
a separately reviewed specification referencing immutable environment,
protocol and outcome versions. Reward cannot alter decision-time observation
and is not terminal or evaluation authority. Return is not strength evidence.
No reward implementation is approved.

## Model-Output Interface Dependency Boundary

No model-output integration is approved. A future participant/model may only
propose a candidate action. The environment independently validates legality;
the model cannot mutate state, supply terminal/raw outcome or access hidden
state. A future model interface needs separate schema, version, risk, review
and approval. No model/checkpoint/logits are used.

## Training vs Evaluation Environment Separation

Training and evaluation environments are distinct approved uses whose
configuration/version differences must be visible. Evaluation requires frozen
ruleset, protocol and participant rules. Training-time environment changes
cannot silently propagate to holdout use, and evaluation outcomes cannot be
mixed into training without approval. Environment bug fixes require a version
change and comparability review. Neither use is approved now.

## Source / Real-Data Boundary

This boundary approves no source or ingestion and uses no real Tenhou, real
haifu, external logs, platform data or account/session/cookie/token material.
Simulation cannot impersonate real-platform evidence. Future replay/audit work
requires separate rights/privacy/platform/approval/ingestion gates. Future
self-play data requires a separate provenance/data boundary. No episode or
data is created.

## Third-Party / Binary / Artifact Boundary

This task calls no Akochan `system.exe`, `libai.so`, unknown simulator binary,
unknown model weight or unreviewed third-party rules engine. It vendors no
third-party source, binary, parameter or artifact. Future dependencies require
license, provenance, integrity, interface and security review. No download is
performed.

## Evidence Boundary

Current evidence grade:

```text
P8 environment / simulator boundary definition evidence only.
```

It supports vocabulary, authority separation, state/transition/legality,
reproducibility/provenance and future-review readiness only. It supports no P8
entry/implementation, environment/simulator/transition/episode/self-play/RL/
reward/training/evaluation/league/model-output evidence, strength/Tenhou/
stable-dan/LuckyJ/promotion evidence or P9-P12 approval.

## Future Environment Entry Criteria

- ENV-E1. P8 scope review is closed.
- ENV-E2. P8 risk/evidence taxonomy review is closed.
- ENV-E3. P8 self-play/RL dependency-map review is closed.
- ENV-E4. P8 self-play protocol boundary review is closed.
- ENV-E5. P8 objective/reward boundary review is closed.
- ENV-E6. Environment/simulator boundary is defined and reviewed.
- ENV-E7. State, observation, legality and transition authority are defined
  and reviewed.
- ENV-E8. RNG/seed/seat/reproducibility boundaries are defined and reviewed.
- ENV-E9. Terminal/raw-outcome authority is defined and reviewed.
- ENV-E10. Error/abort/retry/resource handling is defined and reviewed.
- ENV-E11. Environment identity/version/provenance is defined and reviewed.
- ENV-E12. Model-output interface dependency is defined and reviewed.
- ENV-E13. Training/evaluation environment separation and source status remain
  separately governed.
- ENV-E14. A separate approval decision authorizes an exact future task.
- ENV-E15. `docs/10_next/10_NEXT.md` authorizes that exact task.

No ENV-E criterion is implementation approval by itself. Defined and reviewed
does not mean implemented. ENV-E14 and ENV-E15 are hard gates before any
future implementation.

## Stop Conditions

Stop if a future task implies P8 entry/implementation approval, creates an
unapproved implementation prompt, implements an environment/simulator/runner/
reset/step/transition, runs an episode/match/self-play/RL/training/tuning/
evaluation/league, implements reward/objective/loss, selects an RL algorithm,
calls models/checkpoints, exposes hidden/private state, lets a model control
legality/transition/terminal outcome, silently corrects actions or retries/
filters failures, uses global/untracked RNG, silently changes versions or
resources, accesses real/external/platform data, approves ingestion, creates
code/tests/fixtures/data, claims environment correctness as strength/ranked/
promotion evidence, enters P9-P12, changes `10_NEXT` to implementation without
approval, downloads unknown artifacts or calls third-party binaries.

## Candidate Next Directions

| candidate | current_status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this environment/simulator boundary. | available | checks authority and non-approval | low if review-only | none | yes | no | low | low | selected |
| B. Define raw-outcome/environment provenance. | deferred | strengthens lineage | may imply schema | environment review | yes | no | medium | low | defer |
| C. Define model-output interface dependency. | deferred | clarifies candidate actions | model-loading creep | environment review | yes | no | medium | low | defer |
| D. Define training/evaluation environment separation. | deferred | clarifies run uses | evaluation creep | environment review | yes | no | medium | low | defer |
| E. Define RL algorithm-selection boundary. | deferred | later controls algorithms | premature algorithm focus | environment/reward reviews | yes | no | medium | low | defer |
| F. Define environment validation/invariant evidence. | deferred | prepares future assurance | test/schema creep | environment review | yes | no | medium | low | defer |
| G. Prepare P8 entry approval. | rejected now | could advance stage | criteria incomplete | ENV-E6-ENV-E15 | yes | no | high | medium | reject |
| H. Draft P8 implementation proposal. | forbidden | none now | premature implementation | entry/exact approval | no | no | high | high | forbid |
| I. Implement environment/simulator/runner. | forbidden | none now | no reviewed approval | multiple gates | no | no | high | high | forbid |
| J. Start self-play/RL. | forbidden | none now | execution unapproved | multiple gates | no | no | high | high | forbid |
| K. Start training/tuning. | forbidden | none now | run approval absent | training gates | no | no | high | high | forbid |
| L. Start evaluation/league. | forbidden | none now | evaluation/P10 jump | later protocols | no | no | high | high | forbid |
| M. Start real-data/Tenhou work. | forbidden | none now | rights/platform risk | source review | no | no | high | high | forbid |
| N. Start model output/strength work. | forbidden | none now | interface/evidence overclaim | separate approvals | no | no | high | high | forbid |
| O. Enter P9-P12. | forbidden | none now | stage jump | separate stage reviews | no | no | high | high | forbid |

Selected next direction:

```text
Review P8 environment / simulator boundary before any implementation.
```

## Planning Decision

```text
P8 environment / simulator authority boundary is defined before any implementation.
```

This task approves no P8 entry/implementation/prompt, environment/simulator/
runner/reset/transition implementation, episode/match/self-play/RL execution,
reward/objective/loss implementation, RL algorithm selection, training,
tuning, evaluation, league, source/real-data/model-output work, strength/
Tenhou/stable-dan/LuckyJ/promotion evidence or P9-P12 entry. The next safe task
is a docs-only review of this boundary.

## Evidence Grade

```text
P8 environment / simulator boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not P8 entry/implementation approval, an implementation
prompt or executable task, environment/simulator/runner/reset/transition
implementation, transition/episode/match/self-play/RL execution, reward/
objective/loss implementation, RL algorithm selection, training, tuning,
evaluation, league, source approval/ingestion, real Tenhou/haifu/external/
platform data, model-output integration, strength/Tenhou-ranked/stable-dan/
LuckyJ/promotion evidence or P9-P12 approval.

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
