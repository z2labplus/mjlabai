# 12U_P8_RAW_OUTCOME_ENVIRONMENT_PROVENANCE_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 raw-outcome / environment-provenance boundary
before any implementation. It is a docs-only planning artifact.

This task is not P8 entry or implementation approval, an implementation
prompt or first executable task, raw-outcome schema/record/parser/reader/
ingestion implementation, environment/simulator/runner/reset/step/transition/
terminal implementation, episode/match/self-play/RL execution, reward/
objective/loss implementation, RL algorithm selection, training, tuning,
evaluation, league, source approval/ingestion, real-data access, model-output
integration, strength evidence or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` goal only by requiring every future outcome used by
reward, evaluation or evidence work to have an immutable, complete and
auditable environment lineage. It creates no outcome, data or strength
evidence and does not show that a model can beat LuckyJ.

## Full P7 / P8 Planning Recap

- Full P7 is closed only for documented P7 supervised-learning scope.
- `12I`/`12J` defined and reviewed P8 scope and entry criteria.
- `12K`/`12L` defined and reviewed the P8 risk/evidence taxonomy.
- `12M`/`12N` defined and reviewed P8 self-play/RL dependencies.
- `12O`/`12P` defined and reviewed the P8 self-play protocol boundary.
- `12Q`/`12R` defined and reviewed the P8 objective/reward boundary.
- `12S`/`12T` defined and reviewed environment/simulator authority.
- `12T` recorded `A. Review can close.`
- P8 remains docs-only planning; entry and implementation are unapproved.
- P9-P12 remain unapproved.

## Raw-Outcome / Provenance Non-Approval Baseline

- No raw-outcome schema, record class, parser, reader or calculator is
  approved.
- No provenance database, ingestion or storage path is approved.
- No integrity checker, environment, simulator or runner is approved.
- No transition, episode, match, self-play, RL or outcome data exists.
- No reward mapping or evaluation aggregation is approved.
- No real-data source is approved or accessed.
- Current raw-outcome evidence is docs-only boundary planning only.
- No current artifact is model-strength or ranked evidence.

This wording is scoped to current P8 raw-outcome/provenance work. It is not a
repository-global assertion that no result object, fixture or historical log
concept exists elsewhere.

## Raw-Outcome / Provenance Vocabulary

| term | boundary meaning |
|---|---|
| environment event | Future versioned occurrence emitted by environment authority. |
| transition event | Event linked to one authoritative state transition. |
| terminal transition | Final authoritative transition establishing terminal status. |
| terminal status / termination reason | Environment-owned end determination and stable reason. |
| episode status | Candidate lifecycle classification for one initialized attempt. |
| raw outcome / payload | Environment-authoritative uninterpreted result and future content. |
| raw-outcome identity / version | Immutable record identity and generation/version. |
| raw-outcome schema version | Candidate representation identity; no schema is approved. |
| canonical outcome-status record | Future authoritative status record for one episode attempt. |
| valid / invalid / aborted / incomplete episode | Explicit episode disposition, never implicit filtering. |
| retried / duplicate episode | Explicit linked attempt or duplicate requiring audit. |
| superseded outcome / correction record | Preserved original plus linked immutable replacement. |
| retry / failure lineage | Parent/attempt/failure relationships, seeds, versions and eligibility. |
| completeness / integrity status | Explicit classification of required fields and integrity. |
| provenance / provenance chain | Bound identities and immutable upstream history. |
| participant / artifact / policy identity | Future participant and executable-policy identities. |
| environment / simulator / conformance identity | Authority, carrier and reviewed relationship identities. |
| ruleset / protocol / transition identity | Immutable interpretation, lifecycle and state-change identities. |
| raw-outcome hash / integrity marker | Candidate concepts; no hash/signature is implemented. |
| evidence-eligibility input | Fact for separate governance, not a strength decision. |
| training / evaluation eligibility | Separate future use decisions. |
| non-evidence warning | Required warning preventing raw-record overclaim. |

Raw outcome is environment-authoritative and uninterpreted. It is not reward,
an evaluation result or model-strength evidence. Vocabulary definition
approves no schema, storage, parser, validator or execution.

## Authority and Lineage Chain

The future authority chain must be:

1. Protocol manifest identifies run, episode and participants.
2. Environment manifest identifies environment, simulator, ruleset and
   immutable versions.
3. Initialization binds identities, seeds, seats/roles and resource policy.
4. Transition lineage records authoritative state changes.
5. Terminal transition records terminal status and reason.
6. One canonical raw-outcome or outcome-status record is finalized.
7. Separately approved reward mapping may consume that immutable record.
8. Separately approved evaluation may interpret eligible approved records.
9. Separate evidence governance decides evidence eligibility.

Participant/model cannot provide authoritative raw outcome. Reward is not
terminal authority. Evaluation cannot modify raw outcome. No layer may
silently rewrite upstream records; every downstream record references
immutable upstream identities.

## Canonical Episode Outcome Boundary

Future design should require one canonical outcome-status record for every
allocated episode attempt, including failed initialization after attempt
identity allocation. Candidate statuses are:

```text
pending
valid_terminal
invalid
aborted
incomplete
failed_initialization
superseded
```

A valid terminal episode may carry a separately approved future payload.
Other statuses still retain provenance. Missing normal outcome cannot make an
episode disappear, and successful attempts cannot be the only retained
sample. These are candidate semantics, not an executable enum or schema.

## Raw-Outcome Finalization and Immutability Boundary

Future finalization requires explicit finalization state, immutable outcome
identity, environment authority and terminal-transition identities,
environment/ruleset/protocol versions, participant/artifact identities,
completeness/provenance status and explicit correction rules.

A finalized record cannot change in place. Correction creates a new
superseding record with reason, author/authority identity,
timestamp-or-version identity and `supersedes_record_id`; the original is
preserved. No storage mechanism, timestamp format, class or correction
implementation is selected.

## Environment / Simulator Conformance Provenance

Future provenance must bind:

```text
environment_id
environment_version
environment_build_identity
simulator_id
simulator_version
simulator_conformance_identity_or_reviewed_evidence_ref
ruleset_id
ruleset_version
transition_policy_version
legality_policy_version
termination_policy_version
raw_outcome_policy_or_schema_version
```

Simulator output is not automatically authoritative. A simulator belongs to a
declared reviewed conformance chain, and version mismatch must be visible. No
conformance record, test, schema or implementation is approved.

## Episode / Transition Provenance Boundary

Future lineage must preserve:

```text
run_id
episode_id
attempt_id
parent_episode_id
retry_index
initialization_identity
terminal_transition_id
transition_count
final_step_index
pre_terminal_state_identity
post_terminal_state_identity
event_order_policy_version
concurrency_policy_version
resource_policy_version
failure_lineage_identity
```

State identities are candidate fields only if separately approved later.
Stale-state transitions cannot enter canonical lineage, duplicates cannot
silently apply or count, gaps remain visible and partial commit produces
incomplete/aborted status. No transition log, event store or database exists.

## Retry / Duplicate / Replacement Boundary

Future retry handling specifies original identity, retry parent/attempt,
original/retry seeds and versions, reason, supplement-versus-replacement
analytic policy, retention, deduplication identity and evidence eligibility.

Silent retry, replacement, failed-original deletion and success-only filtering
are forbidden. Retry outcome cannot overwrite original outcome, and reward or
evaluation cannot hide lineage. No retry/deduplication implementation is
approved.

## Completeness / Integrity Boundary

Future records separately classify identity, environment-version,
participant/artifact, transition-lineage, terminal, raw-payload, seed/seat,
failure/retry and provenance completeness plus integrity status.

Incomplete cannot impersonate valid terminal. Missing provenance is not
guessed or default-filled; unknown/partial status is explicit. Hashes,
signatures and integrity markers remain candidate concepts. No validator is
implemented, and integrity pass is not model-strength evidence.

## Participant / Artifact / Policy Provenance

Future outcome provenance binds participant ID/role, policy version, artifact
ID/hash or immutable identity, separately approved checkpoint ID, code/config
revision, frozen/mutable status and update-schedule identity if cross-episode
updates are later approved.

Policy cannot silently change within an episode. Evaluation participants need
separately approved freezing rules. Unknown weights/checkpoints are forbidden;
no artifact is approved for P8 self-play and no model is loaded now.

## Seed / Seat / RNG Provenance Boundary

Future provenance references RNG algorithm/version, run/episode seeds,
component/substream identities, seat method/version/seed, participant order,
retry-seed policy, known nondeterminism and concurrency/event-order policy.

Same seed is not complete reproducibility. Outcomes retain seat context;
parallel scheduling cannot silently alter provenance. RNG state/substreams
need separate future review. No RNG is implemented.

## Terminal / Failure / Resource Provenance

Future records distinguish normal terminal, invalid action, participant or
environment error, ruleset/invariant failure, artifact/protocol mismatch,
timeout, memory/resource/concurrency failure, cancellation and unknown
failure.

Candidate fields include termination reason, stable error class/code, episode
validity, abort reason, retry permission/count, resource-policy version,
raw-outcome availability, evidence-eligibility input and provenance
completeness. Failure cannot silently become success; resource changes are
versioned; invalid/aborted episodes cannot silently enter training/evaluation.
No failure handler is implemented.

## Candidate Raw-Outcome Record Fields

Candidate future fields are:

```text
raw_outcome_record_id
raw_outcome_record_version
raw_outcome_schema_version
record_status
supersedes_record_id
correction_reason
run_id
episode_id
attempt_id
parent_episode_id
retry_index
protocol_id
protocol_version
environment_id
environment_version
environment_build_identity
simulator_id
simulator_version
simulator_conformance_identity
ruleset_id
ruleset_version
transition_policy_version
terminal_transition_id
final_step_index
participant_ids
participant_roles
participant_artifact_ids
participant_policy_versions
run_seed
episode_seed
RNG_version
seat_assignment
seat_assignment_policy_version
concurrency_policy_version
event_order_policy_version
retry_policy_version
resource_policy_version
terminal_flag
termination_reason
episode_status
valid_episode
aborted
incomplete
raw_outcome_available
raw_outcome_payload_reference
raw_outcome_payload_version
raw_outcome_integrity_identity
completeness_status
provenance_status
source_status
real_data_status
training_status
evaluation_status
self_play_status
league_status
model_strength_status
explicit_non_evidence_warning
```

These are candidate fields only. They are not an approved schema, API, JSON
fixture, database model, parser/reader, environment implementation, data-file
approval or training/evaluation configuration. No code, fixture or data is
created.

## Raw Outcome vs Reward / Objective Boundary

Raw outcome remains uninterpreted. Reward mapping is separate/versioned and
references immutable raw-outcome, environment and protocol identities. Raw
outcome contains no reward by default, return is not authoritative raw
outcome, and reward cannot alter terminal status or rewrite an outcome. No
reward/objective/loss implementation is approved.

## Raw Outcome vs Evaluation / Strength Boundary

Raw outcome is not an evaluation metric, and one episode is not strength
evidence. Aggregation requires separately approved evaluation, seat/opponent/
version/failure/retry accounting, sample definition/size and uncertainty.
Training-self-play outcomes cannot automatically become holdout evidence;
evaluation outcomes require frozen/versioned participants and environment.

High score, win or placement does not prove Tenhou, stable-dan or LuckyJ
strength. No evaluation, ranked or strength evidence exists.

## Training-Self-Play vs Evaluation-Self-Play Outcome Use

Future use classification requires distinct status, separately approved
protocol/environment identities where applicable, frozen evaluation
participants, explicit eligibility and leakage review, separate aggregation/
reporting, visible environment fixes/version changes and disclosed reward
tuning against evaluation outcomes.

This document approves neither use. Outcome-use classification is not training
or evaluation approval.

## Source / Real-Data Boundary

This boundary approves no source/ingestion and uses no real Tenhou, real
haifu, external logs, platform data or account/session/cookie/token material.
Future self-play outcomes need separate provenance/data policy. Simulation
cannot impersonate real-platform evidence; real-log audit needs independent
rights/privacy/platform/approval gates. No outcome/data file is created.

## Privacy / Security / Third-Party Boundary

No account identifier, secret, private payload, unknown binary, Akochan
`system.exe`, `libai.so`, unknown weight, third-party rules engine or vendored
artifact is used. Future third-party use requires license, provenance,
integrity, interface and security review. Provenance cannot leak secrets. No
download or external execution is performed.

## Evidence Boundary

Current evidence grade:

```text
P8 raw-outcome and environment-provenance boundary definition evidence only.
```

It supports vocabulary, lineage/provenance planning, completeness/retry/
correction readiness and future review only. It supports no P8 entry/
implementation, schema/parser/environment/episode/self-play/RL/reward/
training/evaluation/league/model-output evidence, strength/Tenhou/stable-dan/
LuckyJ/promotion evidence or P9-P12 approval.

## Future Raw-Outcome / Provenance Entry Criteria

- RO-E1. P8 scope review is closed.
- RO-E2. P8 risk/evidence taxonomy review is closed.
- RO-E3. P8 self-play/RL dependency-map review is closed.
- RO-E4. P8 self-play protocol boundary review is closed.
- RO-E5. P8 objective/reward boundary review is closed.
- RO-E6. P8 environment/simulator boundary review is closed.
- RO-E7. Raw-outcome/environment-provenance boundary is defined and reviewed.
- RO-E8. Environment/protocol/ruleset/participant identities are bound and
  reviewed.
- RO-E9. Terminal/failure/retry/correction lineage is defined and reviewed.
- RO-E10. Completeness/integrity/evidence-eligibility separation is reviewed.
- RO-E11. Training/evaluation outcome-use separation is reviewed.
- RO-E12. Model-output/reward/evaluation transformations remain separately
  governed.
- RO-E13. Source/real-data status remains separately governed.
- RO-E14. A separate approval decision authorizes an exact future task.
- RO-E15. `docs/10_next/10_NEXT.md` authorizes that exact task.

No criterion is implementation approval. Defined/reviewed does not mean a
schema is implemented. RO-E14 and RO-E15 are hard gates before schema, code,
fixture or data work.

## Stop Conditions

Stop if a future task implies P8 entry/implementation, creates an unapproved
implementation prompt, implements raw-outcome schema/record/parser/reader/
ingestion/database or fixtures/data, implements/executes environment/
simulator/runner/transition/episode/match, starts self-play/RL/training/
evaluation/league, implements reward/loss, selects executable RL, rewrites a
finalized outcome, deletes failed originals, silently retries/replaces, hides
failure/retry/seat/opponent denominators, loses lineage, trusts an unconformed
simulator, accesses real/platform data, approves ingestion, calls models/
checkpoints, claims strength/ranked evidence, enters P9-P12, changes
`10_NEXT` to implementation without approval, downloads unknown artifacts or
calls third-party binaries.

## Candidate Next Directions

| candidate | current_status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this raw-outcome/environment-provenance boundary. | available | checks lineage, immutability and non-approval | low if review-only | none | yes | no | low | low | selected |
| B. Define model-output interface dependency. | deferred | clarifies candidate actions/artifacts | model-loading creep | outcome review | yes | no | medium | low | defer |
| C. Define training/evaluation outcome-use boundary. | deferred | clarifies eligible uses | use-approval creep | outcome review | yes | no | medium | low | defer |
| D. Define environment validation/invariant evidence. | deferred | prepares assurance | test/schema creep | outcome review | yes | no | medium | low | defer |
| E. Define candidate raw-outcome schema proposal. | rejected now | prepares representation | premature schema/API | RO-E7-RO-E15 | yes | no | high | medium | reject |
| F. Prepare P8 entry approval. | rejected now | could advance stage | criteria incomplete | multiple gates | yes | no | high | medium | reject |
| G. Draft P8 implementation proposal. | forbidden | none now | premature scope | entry/exact approval | no | no | high | high | forbid |
| H. Implement raw-outcome schema/parser. | forbidden | none now | no approval | multiple gates | no | no | high | high | forbid |
| I. Implement environment/simulator/runner. | forbidden | none now | execution unapproved | multiple gates | no | no | high | high | forbid |
| J. Execute self-play/RL. | forbidden | none now | execution unapproved | multiple gates | no | no | high | high | forbid |
| K. Run training/tuning. | forbidden | none now | run approval absent | multiple gates | no | no | high | high | forbid |
| L. Run evaluation/league. | forbidden | none now | evaluation/P10 jump | later protocols | no | no | high | high | forbid |
| M. Start real-data/Tenhou ingestion. | forbidden | none now | rights/platform risk | source review | no | no | high | high | forbid |
| N. Integrate model output or claim strength. | forbidden | none now | evidence overclaim | separate approvals | no | no | high | high | forbid |
| O. Enter P9-P12. | forbidden | none now | stage jump | separate reviews | no | no | high | high | forbid |

Selected next direction:

```text
Review P8 raw-outcome and environment-provenance boundary before any implementation.
```

## Planning Decision

```text
P8 raw-outcome and environment-provenance boundary is defined before any implementation.
```

This task approves no P8 entry/implementation/prompt, raw-outcome schema/
record/parser/reader/ingestion/database, environment/simulator/runner/reset/
transition/terminal implementation, episode/match/self-play/RL execution,
reward/objective/loss implementation, RL algorithm selection, training,
tuning, evaluation, league, source/real-data/model-output work, strength/
Tenhou/stable-dan/LuckyJ/promotion evidence or P9-P12 entry. The next safe task
is a docs-only review of this boundary.

## Evidence Grade

```text
P8 raw-outcome and environment-provenance boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not P8 entry/implementation approval, an implementation
prompt or executable task, raw-outcome schema/record/parser/reader/ingestion/
database implementation, environment/simulator/runner/reset/step/transition/
terminal implementation, transition/episode/match/self-play/RL execution,
reward/objective/loss implementation, RL algorithm selection, training,
tuning, evaluation, league, source approval/ingestion, real Tenhou/haifu/
external/platform data, model-output integration, strength/Tenhou-ranked/
stable-dan/LuckyJ/promotion evidence or P9-P12 approval.

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
