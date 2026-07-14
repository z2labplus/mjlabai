# 12X_P8_MODEL_OUTPUT_INTERFACE_DEPENDENCY_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION

## Scope

This document reviews
`docs/12_technical_plan/12W_P8_MODEL_OUTPUT_INTERFACE_DEPENDENCY_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`.
It is a docs-only review gate.

This review does not modify `12W`, approve P8 entry or implementation, create
an implementation prompt or first executable task, implement a schema/API/
adapter/parser/reader/ingestion path/CLI, load a model/checkpoint/weight, run
inference or action generation, produce scores/logits/probabilities/values/
tensors/hidden states, implement recurrent/session/cache/batching/queueing,
run an environment/transition/episode/self-play/RL/training/evaluation/league,
approve a source or real-data use, create strength evidence or approve P9-P12.

North-star relationship: reviewing this dependency boundary reduces future
hidden-information, stale-response, state-isolation and provenance risks on
the route to Tenhou stable dan `> 10.68`. It does not load or evaluate a model
and provides no evidence that any policy can beat LuckyJ.

## Reviewed Artifacts

Primary artifact:

- `docs/12_technical_plan/12W_P8_MODEL_OUTPUT_INTERFACE_DEPENDENCY_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`

Upstream boundary and review chain:

- `docs/12_technical_plan/12V_P8_RAW_OUTCOME_ENVIRONMENT_PROVENANCE_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12U_P8_RAW_OUTCOME_ENVIRONMENT_PROVENANCE_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12T_P8_ENVIRONMENT_SIMULATOR_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12S_P8_ENVIRONMENT_SIMULATOR_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12R_P8_RL_OBJECTIVE_REWARD_SPECIFICATION_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12Q_P8_RL_OBJECTIVE_REWARD_SPECIFICATION_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12P_P8_SELF_PLAY_PROTOCOL_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12O_P8_SELF_PLAY_PROTOCOL_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12N_P8_SELF_PLAY_RL_DEPENDENCY_MAP_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12M_P8_SELF_PLAY_RL_DEPENDENCY_MAP_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12L_P8_RISK_AND_EVIDENCE_TAXONOMY_REVIEW_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12K_P8_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_ANY_IMPLEMENTATION.md`
- `docs/12_technical_plan/12J_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_REVIEW.md`
- `docs/12_technical_plan/12I_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_AFTER_P8_P12_TRANSITION_SCOPE_REVIEW.md`
- `docs/12_technical_plan/12H_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_REVIEW.md`
- `docs/12_technical_plan/12G_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK.md`
- `docs/12_technical_plan/12F_POST_FULL_P7_TRANSITION_REVIEW.md`
- `docs/03_supervised_policy/03BL_FINAL_FULL_P7_CLOSURE_REVIEW.md`

Existing synthetic/local code, tests and fixtures were inspected read-only.
They were not changed or treated as model-output evidence.

## Review Result Vocabulary

| result | meaning |
|---|---|
| pass | The current boundary is sufficient for this docs-only gate. |
| pass with note | Sufficient now; a future reviewed contract should refine the recorded item. |
| blocker | The review cannot close until a separately authorized docs-only correction task resolves the issue. |

A note is not implementation permission, schema approval or evidence of an
executable interface.

## Review Matrix

| area | result | finding | supporting artifact | downstream implication |
|---|---|---|---|---|
| 1. Scope | pass | Definition is docs-only and explicitly excludes every executable/model/data/strength path. | `12W` Scope | Review may close without implementation. |
| 2. Full P7/P8 recap | pass | Full P7 closure is scoped; `12I`-`12V` chain and P8/P9-P12 non-approval are accurate. | `03BL`, `12F`-`12V` | P8 remains planning-only. |
| 3. Non-approval baseline | pass | Interface, artifacts, runtime, outputs and execution remain unapproved; wording is scoped. | `12W` Non-Approval Baseline | No historical repository-global claim is implied. |
| 4. Vocabulary | pass | Interface, identities, input/output, failure/state and use terms are separated. | `12W` Vocabulary | Future contract can reuse terms after separate review. |
| 5. Authority separation | pass | Environment, protocol, interface, policy, reward, evaluation and governance authorities do not overlap improperly. | `12W` Authority Separation; `12S` | Model remains candidate-action proposer only. |
| 6. Candidate classes | pass | All ten classes are unapproved, unselected and non-executable. | `12W` Candidate Interface Classes | No transport/runtime class is selected. |
| 7. Model/artifact/policy identity | pass | Immutable identity, versions and frozen/mutable/update status are required; unknown artifacts are forbidden. | `12W` Identity Boundary | Future artifact use still needs approval. |
| 8. Request identity/immutability | pass with note | Request binding and retry lineage are sufficient; content/finalization/cancellation identities need future refinement. | `12W` Request Boundary | Future contract review must make binding atomic and unique. |
| 9. Observation/leakage | pass | Participant-specific decision-time projections and visibility classes block hidden/future/post-outcome access. | `12W` Observation Boundary; `12S` | Recurrent/cache paths remain subject to the same leakage rule. |
| 10. Legal-action handoff | pass | Environment remains sole legality authority and identity mismatch is non-success. | `12W` Legal-Action Handoff; `12S` | No checker, mask or canonicalizer is approved. |
| 11. Candidate-action output | pass with note | Candidate/applied action separation is clear; vocabulary, selection and RNG semantics need future versioning. | `12W` Candidate Action Output | No sampler, decoder or action generator is approved. |
| 12. Score/logit/probability | pass with note | Numeric classes are separated and no class/shape/softmax is selected; explicit calibration/mask record fields may be added later. | `12W` Numeric Output Boundary | Numeric outputs remain advisory candidate concepts. |
| 13. Value/auxiliary output | pass | Typed/versioned optional outputs cannot own outcome/reward/evaluation/fallback. | `12W` Value/Auxiliary Boundary; `12Q` | No head, target, loss or metric is approved. |
| 14. Response status | pass with note | Statuses cover current failure classes; finalization/content identity and correction semantics need future review. | `12W` Response Status Boundary | Non-success cannot disappear into success. |
| 15. Timeout/stale/duplicate/retry | pass with note | Stale/duplicate rejection and retry lineage are sufficient; timebase/completion/latency identities remain future details. | `12W` Timeout Boundary | No clock, retry or deduplication code is approved. |
| 16. Fallback | pass with note | Authority and failure preservation are safe; policy/source/RNG/original-failure fields remain future refinements. | `12W` Fallback Boundary | No fallback action or policy is selected. |
| 17. Recurrent/session/cache | pass with note | Scope/reset/isolation rules are sufficient; content identity/update lineage/compatibility need future review. | `12W` Recurrent Boundary | No state mechanism is approved. |
| 18. Batching/concurrency/isolation | pass | One-to-one identity, per-request isolation and visible partial failure prevent sample mixing. | `12W` Batching Boundary | No batcher, queue, worker or scheduler is approved. |
| 19. Determinism/precision/reproducibility | pass with note | Required identities and known nondeterminism are explicit; RNG/batch/kernel details remain future refinements. | `12W` Reproducibility Boundary | No reproducibility or benchmark result is claimed. |
| 20. Training/evaluation model use | pass | Mutable training and frozen evaluation identities are separated and both remain unapproved. | `12W` Training vs Evaluation | Safe next boundary topic is available. |
| 21. Environment/outcome/reward/evaluation | pass | Candidate response, legality/transition/outcome, reward and evaluation authorities stay separate. | `12W`, `12S`, `12U`, `12Q` | No integration is approved. |
| 22. Evaluation/strength | pass | Interface diagnostics are explicitly not policy/strength/ranked evidence. | `12W` Evaluation Boundary; `12K` | No promotion or LuckyJ claim is supported. |
| 23. Source/privacy/remote/third party | pass with note | Current use is absent and blocked; future remote privacy/redaction and artifact licensing need separate review. | `12W` Source and Third-Party Boundaries | Compatibility grants no artifact-use permission. |
| 24. Candidate fields | pass with note | Coverage is sufficient and explicitly non-schema; future identity/calibration/privacy fields remain candidates. | `12W` Candidate Fields | No dataclass, manifest, JSON or tensor contract exists. |
| 25. Evidence boundary | pass | Definition and review grades are bounded below executable/strength evidence. | `12W` Evidence Boundary; this review | Review produces only boundary-review evidence. |
| 26. MO-E1-MO-E15 | pass | Upstream review, identity/leakage/failure/isolation and exact approval gates remain intact. | `12W` Future Entry Criteria | MO-E14/MO-E15 remain hard pre-implementation gates. |
| 27. Stop conditions | pass | Stage jumps, executable interfaces, model calls, leakage, silent failure and evidence overclaim are blocked. | `12W` Stop Conditions | Any trigger requires stopping and separate authorization. |
| 28. Candidate next directions | pass | Training/evaluation model-use boundary is the narrowest safe docs-only successor. | `12W` Candidate Directions | No entry/implementation task follows this review. |
| 29. Governance synchronization | pass | Direct governance files preserve P8/P9-P12 non-approval and exact next-task status. | handoff/index/plan/governance/backlog | Repository state remains auditable. |

No blocker was found.

## Scope Review

`12W` defines only a dependency and authority boundary. It does not approve or
implement P8 entry, P8 implementation, an implementation prompt, an executable
task, schema/API/adapter/parser/reader/ingestion/CLI, model/artifact loading,
inference/action/numeric output, state/cache/batching, environment/episode/
self-play/RL/reward/training/evaluation/league, source/real-data use, strength
evidence or P9-P12. Result: **pass**.

## Full P7 / P8 Planning Recap Review

`03BL` closes Full P7 only for documented supervised-learning scope. `12F`
permits later docs-only transition planning, and `12G` through `12V` preserve
definition/review pairs without entry or execution approval. `12W` accurately
summarizes that chain. P8 remains docs-only planning and P9-P12 remain
unapproved. Result: **pass**.

## Non-Approval Baseline Review

No P8 model-output path, schema, interface class, service, policy, checkpoint,
weight, endpoint, encoder, tensorizer, runtime, decoder, output, timeout/retry/
fallback mechanism, state/cache/batcher, environment execution, real-data
source, remote API or third-party artifact is approved. The scoped disclaimer
avoids a false repository-global assertion. Result: **pass**.

## Vocabulary Review

The vocabulary distinguishes interface from runtime, request from response,
policy/model/artifact identities, participant observation from environment
hidden/private state, candidate action from applied action, score/logit/
probability from one another, optional value/auxiliary outputs from outcome/
reward, and training from evaluation model use. Recurrent model state is not
environment hidden state. No term creates a schema or call approval. Result:
**pass**.

## Authority Separation Review

Environment owns authoritative state, observation-projection authorization,
legal set, applied action, transition, terminal status and raw outcome.
Protocol owns/configures lifecycle identity, ordering and future timeout/retry/
fallback policy. Interface owns request/response binding, transport/result
status and declared output semantics. Policy may only propose candidate action
and declared advisory outputs. Reward, evaluation and evidence governance stay
downstream and separate. Result: **pass**.

## Candidate Interface Classes Review

All ten candidate classes have `approved_now = no`, `selected_now = no`,
`executable_now = no` and `implementation_allowed_now = no`. The synthetic
stub cannot impersonate a model; frozen evaluation and mutable training classes
do not approve those uses; remote service remains blocked. Result: **pass**.

## Model / Artifact / Policy Identity Review

Participant, policy, architecture, immutable artifact, separately approved
checkpoint, code, runtime, configuration, backend/device/precision,
frozen/mutable and update-schedule identities are required. Mutable path/name/
tag alone is insufficient, silent artifact change is forbidden and unknown
weights/checkpoints remain forbidden. No loader or artifact is approved.
Result: **pass**.

## Request Identity / Immutability Review

Requests bind run/episode/attempt/participant/decision/pre-action state,
protocol/environment/ruleset/observation/legal set and policy identity; dispatch
makes a request immutable; retries use new attempt/parent lineage; forbidden
post-action/private/future/audit information is excluded. Stale reuse cannot be
valid under the state-binding rule. Result: **pass with note**.

Future contract review should define request content identity, dispatch/
finalization authority, monotonic decision identity, request-attempt
uniqueness, atomic observation/legal-set/pre-state binding and cancellation or
correction lineage. Their absence is not a current blocker because `12W`
already requires immutable identity binding and explicit stale/retry status.

## Observation / Information-Leakage Review

Only environment-authorized participant-specific decision-time projections
are eligible. Public, participant-private, hidden, opponent-private, future,
post-outcome and audit-only classes remain explicit. Environment internals are
not default model input; feature extraction/tensorization/device transfer are
unapproved. Recurrent/session/cache state is governed by the same leakage and
isolation rules and cannot become a side channel. Result: **pass**.

## Legal-Action Handoff Review

The environment remains sole legal authority. The legal set/reference derives
from the same state/ruleset/decision, and actor/decision/state/ruleset/legal-set
mismatch produces non-success. Models cannot add authoritative actions,
reinterpret rules, silently correct/canonicalize or bypass independent
validation. No checker, mask, canonicalizer or rule engine is approved.
Result: **pass**.

## Candidate-Action Output Review

A candidate action is bound to one request/decision/legal set and is not the
applied action. Participant/policy/artifact/output semantics remain bound,
environment validation is mandatory, and default action/unlogged sampling/
cross-decision reuse are forbidden. Result: **pass with note**.

Future contract review should specify allowed action/score/distribution
combinations, action-vocabulary/mapping identity, tie-breaking/selection/
sampling authority and selection-policy/inference-RNG identity. No sampler or
action generator is approved now.

## Score / Logit / Probability Review

Domain, ordering, mask, dtype, precision, shape, normalization, temperature,
calibration, NaN/Inf/missing handling and advisory/selecting use are required.
Logits are not probabilities, normalized probability is not calibrated
probability, score is not legality and confidence is not correctness. No class,
shape, softmax, threshold or sampler is selected. Result: **pass with note**.

Future candidate records may make calibration and mask status more explicit;
that refinement is not an output implementation approval.

## Value / Auxiliary Output Review

Optional value/auxiliary outputs require separate typing/versioning and cannot
own raw outcome, reward, evaluation, transition or fallback. They do not
approve feature/label work. No head, tensor, target, loss or metric is
approved. Result: **pass**.

## Response Status Review

Current statuses distinguish success/no action, invalid request/observation/
legal handoff, unsupported contract, unavailable/artifact mismatch, timeout/
cancelled, stale/duplicate and malformed/numeric/internal errors. Non-success
cannot be omitted or default-filled and status is not evidence grade. Result:
**pass with note**.

Future review should define partial-response semantics, response content and
finalization identity, one active final response per request attempt,
completion/authority identity and correction/supersession semantics if ever
needed. No enum, API or record is approved.

## Timeout / Stale / Duplicate / Retry Review

Deadline authority, timing semantics, cancellation/late handling, stale
rejection, duplicate non-application, new retry attempt/parent identity,
reason/deadline/artifact/version/counting and no silent success-only retention
are covered. Result: **pass with note**.

Future contract review should bind clock/timebase, received/completed identity,
latency provenance, cancellation acknowledgement and idempotent response
handling. No timing or retry code is approved.

## Fallback Review

Fallback belongs to separately governed protocol/environment policy. Trigger,
status, selection, legality, provenance and metric accounting must be explicit,
and original timeout/invalid/malformed status remains visible. Result:
**pass with note**.

Future candidate records may include fallback-policy version, action source,
original-failure reference, selection RNG and evidence eligibility. No default,
random, heuristic or fallback implementation is selected.

## Recurrent / Session / Cache State Review

State is scoped to participant/episode/attempt/policy/artifact with explicit
initialization/update/reset/serialization/compatibility/failure and no
environment-authority, opponent-private or future information. Cross-episode/
seat/participant/use/artifact leakage is forbidden; cache/session is not
provenance. Result: **pass with note**.

Future review should define state content identity, reset/update/finalization
lineage, compatibility/migration authority and retry/cancellation handling. No
state/cache/session implementation is approved.

## Batching / Concurrency / Isolation Review

One-to-one request/response association, ordering, per-request observation/
legal set/deadline, participant/episode isolation, artifact consistency and
visible partial failure are required. Padding/sorting/cancellation/retry cannot
alter identity; sample mixing, hidden queue starvation and cross-request state
leakage are forbidden. Result: **pass**. No batcher/queue/worker/scheduler is
approved.

## Determinism / Precision / Reproducibility Review

Determinism expectation and known nondeterminism are separate; code/runtime/
backend/device/precision/artifact/config/input/contract and applicable seed/RNG
identities are required. Same seed/checkpoint name is insufficient, backend/
precision/batch/concurrency changes remain visible and bitwise equality is not
assumed. Result: **pass with note**.

Future review should add inference-RNG, batch-composition, kernel/determinism
flags and device-specific limitation details. No benchmark or reproducibility
result is claimed.

## Training vs Evaluation Model Review

Mutable training use requires a separately approved update schedule. Evaluation
requires frozen immutable policy/artifact/configuration identity with no hidden
update inside an evaluation unit. Training responses/checkpoints do not become
evaluation evidence. Neither use is approved. Result: **pass**.

## Environment / Raw Outcome / Reward / Evaluation Separation Review

Model proposes a candidate response only. Environment owns legality, applied
action, transition, terminal and raw outcome. Reward consumes separately
approved immutable events/outcomes; scores/values are not outcome/reward/
return; evaluation remains separate. Result: **pass**. No integration is
approved.

## Evaluation / Strength Review

Conformance, latency, parse success, legal-candidate rate and output stability
are engineering diagnostics only. Inference success is not policy strength,
legal action is not strong action and confidence is not correctness. Strength
requires separate frozen-model protocol, eligible samples, uncertainty,
seat/opponent accounting, leakage review and governance. Result: **pass**.

## Source / Privacy / Remote / Third-Party Review

No endpoint/network/API key/token/account/session/cookie, real Tenhou/haifu/
external/platform data, Akochan `system.exe`, `libai.so`, unknown model/runtime/
binary, download or vendoring is used or approved. Compatibility grants no
artifact-use permission. Result: **pass with note**.

Future remote/third-party work requires separate license, security, privacy,
redaction, provenance, interface, reliability and retention review. Current
requests/responses/provenance cannot carry secrets or private/audit-only data.

## Candidate Record Fields Review

The candidate field list covers record/contract/request-attempt lineage,
run/episode/decision, participant/protocol/environment/state/observation/
legal-set, policy/model/artifact/runtime/backend/device/precision, update
status, response/action/numeric/auxiliary/state/batch/failure/retry/fallback,
reproducibility, source/use/evidence and non-evidence warning concepts. It is
explicitly not a schema/API/tensor contract/manifest. Result: **pass with
note**.

Future candidate refinements may include action-vocabulary and selection/
sampling versions, inference-RNG, calibration/mask status, response content/
finalization/completion/timebase, fallback policy/source, recurrent-state
content identity, privacy/redaction and artifact license/provenance. None is
approved now.

## Evidence Boundary Review

Definition evidence remains:

```text
P8 model-output interface dependency boundary definition evidence only.
```

This review produces only:

```text
P8 model-output interface dependency boundary review evidence only.
```

Neither supports P8 entry/implementation, schema/adapter/model loading,
inference/action generation, runtime conformance, self-play/RL/reward/training/
evaluation/league, strength/ranked/promotion evidence or P9-P12. Result:
**pass**.

## MO-E1 Through MO-E15 Review

- MO-E1 through MO-E7 correctly reference completed scope, taxonomy,
  dependency, protocol, reward, environment and outcome/provenance reviews.
- MO-E8 requires definition plus this review; this review closes only that
  docs-only review condition.
- MO-E9 through MO-E13 preserve identity, leakage, failure, state isolation,
  training/evaluation/source/remote/third-party review requirements.
- MO-E14 requires a separate exact approval decision.
- MO-E15 requires exact `10_NEXT` authorization.
- No criterion is implementation approval, and defined/reviewed does not mean
  an interface exists.
- MO-E14 and MO-E15 remain hard gates before schema, adapter, model loading,
  inference, test, fixture, code or data work.

Result: **pass**.

## Stop Conditions Review

The stop conditions block implied P8 entry/implementation, implementation
prompts, executable class/schema/API/tensor selection, model download/loading,
local/remote calls, action/numeric generation, information leakage, model-owned
environment authority, silent retry/correction/fallback, stale/duplicate
application, cross-scope state leakage, cache/session/batching runtime,
environment/self-play/RL/training/evaluation/league, real/platform data,
strength claims, P9-P12 jumps, unauthorized `10_NEXT` implementation and
unknown artifacts/binaries. Result: **pass**.

## Candidate Next Directions Review

The selected review is now complete. The narrowest safe next direction is:

```text
Define P8 training / evaluation model-use boundary before any implementation.
```

It should define only mutable training-policy versus frozen evaluation-policy
artifact/update/freeze/use/leakage/eligibility semantics. It must not approve
P8 entry/implementation, an implementation prompt, model/artifact loading,
inference/action generation, training/tuning, evaluation execution, self-play/
RL/league, source/real-data use, model-output integration or strength claims.
P9-P12 remain unapproved. Result: **pass**.

Model/artifact provenance manifest, validation evidence, fallback accounting
and recurrent/batching refinements remain separate later boundary candidates.

## Governance Synchronization Review

The handoff, docs index, technical plan, stage contract, next-task list,
milestones, backlog, changelog, evidence log, risk register and decision record
are synchronized to this review decision and next docs-only task. P8 entry,
P8 implementation and P9-P12 remain unapproved. Result: **pass**.

## Validation Results

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

All required checks pass. The six unittest commands run 46 existing tests.
No test, code, fixture or data file was added or modified.

## Review Decision

```text
A. Review can close.
```

No blocker or overclaim was found. The notes for request/response finalization,
action vocabulary/selection/RNG, timing/latency provenance, fallback identity,
numeric semantics, recurrent-state identity, batching reproducibility and
remote privacy/redaction are future contract refinements. They are not
implementation permission, present schema fields or blockers.

`12W` was not modified.

## Next Task Recommendation

```text
Define P8 training / evaluation model-use boundary before any implementation.
```

The next task must remain docs-only. It must not approve P8 entry or
implementation, generate an implementation prompt, load models/checkpoints/
weights, execute inference/action generation/training/evaluation/self-play/RL/
league, implement model-output integration, approve source/real-data use,
claim strength or enter P9-P12.

## Evidence Grade

```text
P8 model-output interface dependency boundary review evidence only.
```

## Explicit Non-Evidence

This review is not evidence of:

- P8 entry, P8 implementation or an implementation prompt.
- an interface, schema, API, adapter, parser, reader, ingestion path or CLI.
- a model, artifact, checkpoint, weight, loader or inference runtime.
- action, score, logit, probability, value, tensor or hidden-state output.
- environment, transition, episode, self-play, RL, reward or training work.
- evaluation execution, model-output runtime conformance or league work.
- source approval, real-data use, remote-service use or third-party use.
- model/policy strength, Tenhou ranked, stable-dan or LuckyJ evidence.
- candidate promotion or P9-P12 approval.
