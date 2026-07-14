# 12W_P8_MODEL_OUTPUT_INTERFACE_DEPENDENCY_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 model-output interface dependency boundary before
any implementation. It is a docs-only planning artifact.

This task is not P8 entry or implementation approval, an implementation prompt
or first executable task, a model-output schema/API/adapter/parser/reader/
ingestion path, model/checkpoint/weight loading, inference, action generation,
logit/probability/value/tensor generation, recurrent-state handling, batching,
queueing, timeout/retry/fallback code, environment/simulator/runner execution,
self-play, RL, training, tuning, evaluation, league, source approval/ingestion,
real-data access, strength evidence or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` goal only by requiring future model proposals to be
identity-bound, auditable, isolated from hidden information and subordinate to
environment legality and transition authority. It loads no model, produces no
action or score and provides no evidence that a model can beat LuckyJ.

## Full P7 / P8 Planning Recap

- Full P7 is closed only for the documented P7 supervised-learning scope.
- `12I`/`12J` defined and reviewed P8 scope and entry criteria.
- `12K`/`12L` defined and reviewed the P8 risk/evidence taxonomy.
- `12M`/`12N` defined and reviewed P8 self-play/RL dependencies.
- `12O`/`12P` defined and reviewed the self-play protocol boundary.
- `12Q`/`12R` defined and reviewed the objective/reward boundary.
- `12S`/`12T` defined and reviewed environment/simulator authority.
- `12U`/`12V` defined and reviewed raw-outcome/environment provenance.
- `12V` recorded `A. Review can close.`
- P8 remains docs-only planning; entry and implementation are unapproved.
- P9-P12 remain unapproved.

## Model-Output Non-Approval Baseline

- No model-output interface, request/response schema, adapter or service is
  approved.
- No model, policy, checkpoint, weight, artifact or remote endpoint is
  approved or loaded.
- No observation encoder, tensorizer, inference runtime or action decoder is
  approved.
- No logits, scores, probabilities, values, actions or hidden states exist.
- No timeout, retry, fallback, batching, queue, cache or session mechanism is
  approved.
- No environment, episode, self-play, RL, training or evaluation execution is
  approved.
- No real-data source, external model API or third-party artifact is approved.
- Current evidence is docs-only boundary-definition evidence only.

This wording is scoped to current P8 model-output work. It is not a
repository-global assertion that no historical wrapper, result object or
synthetic smoke helper exists elsewhere.

## Vocabulary

| term | boundary meaning |
|---|---|
| model-output interface | Future reviewed handoff between a decision request and a model/policy response. |
| request | Candidate immutable decision-time envelope; no schema is approved. |
| response | Candidate immutable result tied to exactly one request and policy identity. |
| policy / model / artifact identity | Separate future identities for behavior, architecture/runtime and executable bytes/weights. |
| observation | Participant-specific decision-time projection authorized by the environment. |
| legal-action handoff | Environment-authoritative candidate set supplied for constrained model choice. |
| candidate action | Model proposal only; never an authoritative applied action. |
| score / logit / probability | Optional future numeric output classes with explicit semantics and calibration status. |
| value / auxiliary output | Optional future diagnostic or policy-support outputs; never raw outcome or reward authority. |
| response status | Explicit lifecycle result such as success, timeout, invalid or stale. |
| stale response | Response whose request/state/version is no longer current. |
| duplicate response | Repeated response for one request identity. |
| fallback | Separately governed action selection after explicit failure; never silent model correction. |
| recurrent / hidden state | Future policy-internal state with explicit episode, participant and version ownership. |
| session state | Future bounded interface state; never environment authoritative state. |
| batch / queue | Future transport grouping and scheduling concepts, not approved implementations. |
| training model | Mutable policy/artifact used by a separately approved training process. |
| evaluation model | Frozen identity used by a separately approved evaluation process. |
| non-evidence warning | Required warning preventing interface artifacts from being overclaimed. |

Vocabulary definition approves no schema, type, API, adapter, runtime or call.

## Authority Separation

| authority | future responsibility | must not own |
|---|---|---|
| environment | authoritative state, observation projection authorization, legal set, accepted action, transition, terminal status and raw outcome | policy scores, reward meaning or strength claims |
| protocol | participant/request/episode identity, ordering, timeout/retry/fallback policy and provenance requirements | legality, model internals or transition |
| model-output interface | bind request and response identities, transport status and declared output semantics | hidden information, legality authority, transition or outcome |
| participant model/policy | propose a candidate action and optional declared outputs from approved observation/legal set | applied action, terminal status, raw outcome or reward |
| reward specification | map approved immutable events/outcome to training signal | model response or environment transition |
| evaluation protocol | aggregate frozen eligible results under separate approval | training updates or model-output authority |
| evidence governance | classify what claims the records can support | inference or game-state authority |

The model may propose only a candidate action. The environment independently
validates and applies an action. A model response cannot rewrite the legal set,
state, transition, terminal status or raw outcome.

## Candidate Interface Classes

All candidate classes are unapproved, unselected and non-executable.

| candidate_class | intended future use | major risk | prerequisite | approved_now | selected_now | executable_now | implementation_allowed_now |
|---|---|---|---|---:|---:|---:|---:|
| in-process synchronous policy call | minimal local request/response | hidden shared state, blocking | reviewed contract and artifact | no | no | no | no |
| local subprocess interface | process isolation | binary/protocol drift | executable provenance/security | no | no | no | no |
| local service interface | service isolation | queue/session leakage | endpoint/auth/timeout review | no | no | no | no |
| remote service interface | remote inference | privacy, network, rights | separate remote/security approval | no | no | no | no |
| deterministic synthetic stub | contract smoke only | smoke mistaken for model | exact synthetic approval | no | no | no | no |
| frozen evaluation-policy interface | later evaluation | model/version drift | evaluation/freeze approval | no | no | no | no |
| mutable training-policy interface | later training self-play | race and stale weights | training/update approval | no | no | no | no |
| batched local inference interface | later throughput | response misassociation | batch/isolation review | no | no | no | no |
| recurrent/session policy interface | stateful policies | cross-episode leakage | state-lifecycle review | no | no | no | no |
| ensemble/multi-head policy interface | multiple outputs/policies | semantic ambiguity | output/selection review | no | no | no | no |

No class is selected by this document. Naming a candidate does not approve its
transport, runtime, process model, artifact or output.

## Model / Artifact / Policy Identity Boundary

Future requests and responses must bind separately versioned identities for:

```text
participant_id
policy_id
policy_version
model_architecture_id_or_version
artifact_id
artifact_content_identity_or_hash
checkpoint_id_if_separately_approved
code_revision
runtime_id_and_version
configuration_identity
precision_and_backend_identity
mutable_or_frozen_status
update_schedule_identity_if_applicable
```

Path, filename, display name or mutable tag alone is insufficient. Unknown
weights/checkpoints are forbidden. An artifact cannot silently change under
one policy identity. These are candidate identity concepts, not an approved
manifest, hash algorithm, loader or model artifact.

## Request Boundary

A future request must be attributable to one run, episode, attempt,
participant, decision and authoritative pre-action state version. It must bind
protocol/environment/ruleset/observation/legal-set and model-policy identities,
plus ordering, deadline and retry context where approved.

A request is immutable after dispatch. Repeated attempts use new attempt
identity and explicit parent lineage. A request must not contain reward,
post-action state, terminal outcome, opponent-private information, future
events, audit-only secrets or undeclared model mutation instructions.

No request object, serialization, endpoint or transport is implemented.

## Observation / Input Boundary

Only an environment-authorized participant-specific decision-time observation
may become future model input. It must be bound to observation projection,
environment, ruleset, state and decision identities. Public information,
acting-participant private information, hidden/opponent-private information,
future information, post-outcome information and audit-only fields remain
explicitly classified.

Hidden, opponent-private, future or post-outcome leakage is forbidden. The
model cannot receive authoritative internal state by default. No feature
extraction, tensorization, normalization, tokenization, padding, device
transfer or input validation code is approved.

## Legal-Action Handoff Boundary

The environment remains the sole legal-action authority. A future request may
carry a versioned legal-action set or immutable reference derived from the
same authoritative state and ruleset. The request must detect mismatch among
actor, decision, state, ruleset and legal-set identity.

The model cannot add authoritative legal actions, reinterpret rules, silently
normalize an unapproved action or convert an illegal proposal into a legal
one. Empty/missing/malformed legal sets and mismatched identities produce an
explicit non-success status. No legal-action checker, canonicalizer or rule
engine is implemented.

## Candidate Action Output Boundary

A future successful response may propose at most one declared candidate
action under the current request and legal set, or an explicit no-action
status if a later contract permits it. The response must bind request,
decision, participant, policy/artifact and output-semantics versions.

The candidate action is not an applied action. Environment validation remains
mandatory. Silent correction, implicit default action, unlogged sampling and
response reuse across decisions are forbidden. No action generation,
sampling, decoding, canonicalization or application is implemented.

## Score / Logit / Probability Boundary

Future numeric action outputs require explicit declarations for domain,
action ordering, mask semantics, dtype/precision, shape, normalization,
temperature, calibration, missing/NaN/Inf handling and whether values are raw
scores, logits or probabilities. These classes are not interchangeable.

Probabilities must not be inferred from undeclared scores. Legal masking must
not hide an illegal unmasked preference. Scores are neither rewards nor
strength evidence. This document selects no output class, tensor shape,
softmax, threshold, sampler or numeric value.

## Value / Auxiliary Output Boundary

Value, rank, risk, uncertainty, hidden-state or other auxiliary outputs remain
optional future classes requiring separate semantics, target/provenance,
timing, shape, precision and use approval. They cannot define terminal status,
raw outcome, reward, evaluation result or fallback behavior by implication.

No value head, risk head, auxiliary tensor, target, loss or metric is selected
or produced.

## Response Status Boundary

Candidate future response statuses include:

```text
success
no_action
invalid_request
invalid_observation
invalid_legal_action_handoff
unsupported_output_contract
model_unavailable
artifact_mismatch
timeout
cancelled
stale
duplicate
malformed_output
numeric_error
internal_error
```

Statuses are candidate semantics, not an enum or API. Every failure remains
visible and attributable. Failure cannot be converted to success by omission.

## Timeout / Stale / Duplicate / Retry Boundary

Future timeout policy must declare deadline authority, clock/timing semantics,
cancellation behavior and late-response handling. A response after state,
decision, policy or request invalidation is stale and cannot be applied.
Duplicate responses cannot produce duplicate transitions.

Retries require a new request-attempt identity, parent identity, reason,
deadline, artifact/version consistency rule and explicit counting policy.
Silent retry, success-only retention and reuse of the same response under a
new state are forbidden. No clock, timeout, cancellation, retry or deduplication
implementation is approved.

## Fallback Boundary

Fallback is protocol/environment policy, not hidden model behavior. Any future
fallback requires separate approval, explicit trigger/status, deterministic or
declared-random selection semantics, legal-set validation, provenance, metric
accounting and non-evidence warnings.

Fallback cannot erase timeout, invalid or malformed model output. No fallback
action, heuristic, random choice or implementation is selected.

## Recurrent / Hidden / Session State Boundary

Future policy state must be participant-, episode-, attempt-, policy- and
artifact-scoped with explicit initialization, update, reset, serialization,
compatibility and failure semantics. It cannot contain environment-authority
state or leak opponent/private/future information.

No state may cross episodes, seats, participants, training/evaluation uses or
artifact versions without separate explicit approval. Session/cache state is
not provenance by itself. No recurrent state, cache or session is implemented.

## Batching / Concurrency / Isolation Boundary

Future batching must preserve one-to-one request/response association,
ordering semantics, per-request legal set and observation, deadlines,
participant/episode isolation, artifact/version consistency and partial-failure
status. Padding, sorting, cancellation or retry cannot change identity or
silently mix samples.

Future concurrency requires no shared mutable episode/model state across
participants unless separately reviewed, no cross-request hidden-state leak,
no queue starvation hidden from latency/error records and auditable resource
failures. No batcher, queue, worker, scheduler or concurrency code is approved.

## Determinism / Precision / Reproducibility Boundary

Future records must distinguish deterministic expectation from known
nondeterminism and bind code, runtime, backend, device, precision, artifact,
configuration, seed/RNG where relevant, request input identity and output
contract version. Same seed or same checkpoint name is not complete
reproducibility.

Precision/backend changes, nondeterministic kernels, batching and concurrency
may change outputs and must be visible. Bitwise equality is not assumed unless
separately specified. No GPU benchmark, inference run or reproducibility claim
is made.

## Training Model vs Evaluation Model Boundary

Training-policy and evaluation-policy interfaces are separate future uses.
Training may involve mutable artifacts only under a separately approved update
schedule. Evaluation requires frozen immutable policy/artifact/configuration
identity and no hidden updates during an evaluation unit.

Training responses, self-play outcomes or checkpoints do not automatically
become evaluation evidence. No model, training or evaluation use is approved.

## Environment / Raw Outcome / Reward Separation

The model proposes a candidate action only. The environment owns legality,
applied action, transition, terminal status and raw outcome. Reward/objective
mapping consumes separately approved immutable events/outcomes and does not
belong in the model response by default.

A model score/value is not a raw outcome, reward or return. A response cannot
declare episode success, terminal placement or evidence eligibility. No
environment, outcome or reward integration is implemented.

## Evaluation / Strength Boundary

Interface conformance, latency, parse success, legal-candidate rate or output
stability are engineering/diagnostic evidence only. They do not prove policy
quality, model strength, Tenhou ranked performance, stable dan, LuckyJ `10.68`
comparison or candidate promotion.

Strength claims require separate approved evaluation protocol, frozen models,
eligible data/episodes, sample size, uncertainty, seat/opponent accounting,
leakage review and governance. None is approved or executed now.

## Source / Privacy / Remote Boundary

This boundary uses no real Tenhou, real haifu, external logs, platform data,
account/session/cookie/token material or remote model endpoint. Future remote
calls require separate rights, privacy, security, data-transfer, retention,
authentication, availability and reproducibility review.

Observations, requests, responses and provenance must not expose secrets or
opponent-private/audit-only information. No source, endpoint or network use is
approved.

## Third-Party Boundary

No Akochan `system.exe`, `libai.so`, third-party model service, unknown
checkpoint, binary, runtime, source or artifact is loaded, called, vendored or
approved. Future third-party use requires license, provenance, integrity,
interface, sandbox/security and redistribution review. A compatible interface
does not grant artifact-use permission.

## Candidate Model-Output Record Fields

Candidate future fields are:

```text
model_output_record_id
model_output_record_version
model_output_contract_version
request_id
request_attempt_id
parent_request_attempt_id
run_id
episode_id
episode_attempt_id
decision_id
step_index
participant_id
actor
protocol_id
protocol_version
environment_id
environment_version
ruleset_id
ruleset_version
authoritative_state_identity
observation_identity
observation_projection_version
legal_action_set_identity
legal_action_contract_version
policy_id
policy_version
model_architecture_identity
artifact_id
artifact_content_identity
checkpoint_id_if_approved
code_revision
runtime_identity
configuration_identity
backend_identity
device_class
precision_identity
frozen_or_mutable_status
update_schedule_identity
request_created_identity
deadline_policy_version
response_status
candidate_action
candidate_action_contract_version
score_output_class
score_semantics_version
score_shape
value_output_class
auxiliary_output_classes
recurrent_state_input_identity
recurrent_state_output_identity
session_identity
batch_identity
batch_position
queue_policy_version
timeout_status
stale_status
duplicate_status
retry_index
fallback_status
error_class_or_code
determinism_expectation
known_nondeterminism
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

These are candidate concepts only. They are not an approved schema, API,
dataclass, JSON object, tensor layout, endpoint, adapter, parser, reader,
ingestion path, model manifest or storage contract. No field is implemented.

## Evidence Boundary

Current evidence grade:

```text
P8 model-output interface dependency boundary definition evidence only.
```

It supports vocabulary, authority/identity separation, failure/isolation
planning and future review only. It supports no P8 entry/implementation,
model/artifact loading, inference/action/score/value production, environment/
self-play/RL/training/evaluation/league evidence, strength/Tenhou/stable-dan/
LuckyJ/promotion evidence or P9-P12 approval.

## Future Model-Output Entry Criteria

- MO-E1. P8 scope review is closed.
- MO-E2. P8 risk/evidence taxonomy review is closed.
- MO-E3. P8 self-play/RL dependency-map review is closed.
- MO-E4. Self-play protocol boundary is defined and reviewed.
- MO-E5. Objective/reward boundary is defined and reviewed.
- MO-E6. Environment/simulator authority boundary is defined and reviewed.
- MO-E7. Raw-outcome/environment-provenance boundary is defined and reviewed.
- MO-E8. Model-output interface dependency boundary is defined and reviewed.
- MO-E9. Model/policy/artifact identity and immutability are reviewed.
- MO-E10. Observation/legal-set/request/response authority and leakage
  controls are reviewed.
- MO-E11. Timeout/stale/duplicate/retry/fallback and status accounting are
  reviewed.
- MO-E12. Recurrent/session/batching/concurrency isolation and reproducibility
  are reviewed.
- MO-E13. Training/evaluation/source/remote/third-party boundaries remain
  separately governed.
- MO-E14. A separate approval decision authorizes one exact future task.
- MO-E15. `docs/10_next/10_NEXT.md` authorizes that exact task.

No criterion is implementation approval. Defined/reviewed does not mean an
interface exists. MO-E14 and MO-E15 are hard gates before schema, adapter,
model loading, inference, fixture, test, code or data work.

## Stop Conditions

Stop if a future task implies P8 entry/implementation, creates an unapproved
implementation prompt, selects a candidate class, defines an executable
schema/API/tensor contract, loads/downloads a model/checkpoint/weight, calls a
local or remote model, generates actions/logits/probabilities/values, exposes
hidden/future/private information, lets a model control legality/transition/
terminal/outcome, silently retries/corrects/falls back, applies stale or
duplicate output, leaks state across participants/episodes/uses, implements
batching/queues/caches/sessions, runs environment/self-play/RL/training/
evaluation/league, accesses real/platform/external data, claims strength or
ranked evidence, enters P9-P12, changes `10_NEXT` to implementation without
separate approval, downloads unknown artifacts or calls third-party binaries.

## Candidate Next Directions

| candidate | current_status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this model-output interface dependency boundary. | available | checks authority, leakage, identity and failure semantics | low if review-only | none | yes | no | low | low | selected |
| B. Define training/evaluation model-use boundary. | deferred | clarifies frozen/mutable uses | use-approval creep | model-output review | yes | no | medium | low | defer |
| C. Define model/artifact provenance manifest boundary. | deferred | improves reproducibility | schema/artifact creep | model-output review | yes | no | medium | low | defer |
| D. Define model-output validation evidence boundary. | deferred | prepares conformance review | test/implementation creep | model-output review | yes | no | medium | low | defer |
| E. Define timeout/fallback accounting boundary. | deferred | controls failure bias | fallback implementation creep | model-output review | yes | no | medium | low | defer |
| F. Define recurrent/batching isolation boundary in more detail. | deferred | controls state leakage | runtime-design creep | model-output review | yes | no | medium | low | defer |
| G. Draft candidate model-output schema proposal. | rejected now | prepares representation | premature schema/API | MO-E8-MO-E15 | yes | no | high | medium | reject |
| H. Prepare P8 entry approval. | rejected now | could advance stage | criteria incomplete | multiple gates | yes | no | high | medium | reject |
| I. Draft P8 implementation proposal. | forbidden | none now | premature implementation path | entry/exact approval | no | no | high | high | forbid |
| J. Implement interface/adapter/model loading. | forbidden | none now | no approval/artifact | multiple gates | no | no | high | high | forbid |
| K. Run inference/action generation. | forbidden | none now | execution unapproved | multiple gates | no | no | high | high | forbid |
| L. Execute self-play/RL/training. | forbidden | none now | run approval absent | multiple gates | no | no | high | high | forbid |
| M. Run evaluation/league or claim strength. | forbidden | none now | evidence/P10 jump | later protocols | no | no | high | high | forbid |
| N. Start real-data/Tenhou/remote-model work. | forbidden | none now | rights/privacy/platform risk | separate reviews | no | no | high | high | forbid |
| O. Enter P9-P12. | forbidden | none now | stage jump | separate stage reviews | no | no | high | high | forbid |

Selected next direction:

```text
Review P8 model-output interface dependency boundary before any implementation.
```

## Planning Decision

```text
P8 model-output interface dependency boundary is defined before any implementation.
```

This decision means the dependency and authority boundary is documented. It
does not approve P8 entry, a candidate interface class, implementation,
schema/API/adapter, model/artifact loading, inference, action generation,
environment/self-play/RL/training/evaluation/league, source/real-data/remote
work, strength claims or P9-P12. The next safe task is docs-only review.

## Evidence Grade

```text
P8 model-output interface dependency boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P8 entry, implementation approval or an implementation prompt.
- an interface, schema, API, adapter, parser, reader, ingestion path or CLI.
- a model, checkpoint, weight, artifact, loader or inference runtime.
- an observation tensor, action, logit, probability, value or hidden state.
- environment, episode, self-play, RL, reward, training or evaluation work.
- model quality, policy quality or legal-play quality.
- Tenhou ranked performance, stable dan or LuckyJ `10.68` comparison.
- candidate promotion, league performance or P9-P12 approval.

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

No training, model execution, inference, self-play, environment, evaluation,
league, real-data, external-log, platform-data or third-party command is
permitted.
