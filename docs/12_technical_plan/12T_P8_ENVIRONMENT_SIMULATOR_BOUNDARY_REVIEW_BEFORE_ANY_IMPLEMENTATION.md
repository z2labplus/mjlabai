# 12T_P8_ENVIRONMENT_SIMULATOR_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION

## Scope

This document reviews
`docs/12_technical_plan/12S_P8_ENVIRONMENT_SIMULATOR_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`.

This is a docs-only review gate. It does not modify `12S`, approve P8 entry or
implementation, create an implementation prompt or executable task, implement
an environment/simulator/runner/API/schema, execute transitions, episodes,
matches, self-play or RL, select or implement reward/objective/loss or an RL
algorithm, or run training, tuning, evaluation, league, source ingestion,
real-data access, model-output integration or P9-P12 work.

North-star relationship: this review reduces the risk that future work uses an
ambiguous authority for state, legality, transition, randomness, termination
or raw outcome. It is not environment-correctness or model-strength evidence
and provides no evidence that a model can beat LuckyJ.

## Reviewed Artifacts

Primary artifact:

- `docs/12_technical_plan/12S_P8_ENVIRONMENT_SIMULATOR_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`

Planning and governance context:

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
- Direct handoff, index, technical-plan, governance, milestone and backlog
  records.
- Existing synthetic/local P6/P7 validation artifacts, read-only.

## Review Checklist

Each row records result, finding, supporting artifact and downstream
implication.

| review area | result | finding | supporting artifact | downstream implication |
|---|---|---|---|---|
| Scope | pass | `12S` is authority-boundary definition evidence only and grants no entry, implementation or execution permission. | Scope and explicit non-evidence sections. | Continue docs-only planning only. |
| Full P7 / P8 recap | pass | Full P7 closure and the `12I`-`12R` P8 planning chain are accurate and bounded. | Recap plus linked definition/review artifacts. | P8 entry/implementation and P9-P12 remain unapproved. |
| Non-approval baseline | pass | No P8 self-play-specific environment, API, state, rule, transition, RNG, run or result is approved. | Non-approval baseline. | No implementation prompt or approval follows from review closure. |
| Vocabulary | pass | Authority, state, observation, transition, RNG, terminal, outcome, failure, manifest and evidence terms are distinct. | Vocabulary table. | Future specs must preserve these distinctions. |
| Authority separation | pass | Environment, participant/model, protocol, reward and evaluation ownership are separated. | Authority table. | Models cannot own legality, state change, terminal status or raw outcome. |
| Simulator conformance | pass with note | A simulator is not automatically rules authority; future implementation should require versioned conformance evidence. | Vocabulary and authority sections. | Conformance remains a separately reviewed future requirement, not schema approval. |
| Candidate classes | pass | All six classes remain unselected, unapproved, non-executable and non-implementable. | Candidate-class table. | Smoke, training, evaluation, pool, league and audit uses remain separate. |
| Authoritative state | pass | One versioned authority, visibility classification, isolation, lineage and invariants are required. | Authoritative-state section. | No state schema/object/hash/validator is approved. |
| Reset / initialization | pass with note | Atomic reset, manifest binding, failure records and retry lineage are required. | Reset/initialization section. | Future records should preserve non-first reset reason and retry-parent identity. |
| Step / transition | pass with note | Candidate inputs/outputs cover authority and provenance; duplicate application is forbidden. | Step/transition section. | Future review must define atomicity, stale-state rejection, transition identity and application semantics. |
| Ruleset / legality | pass | Ruleset is immutable per episode and legal actions come only from authoritative state. | Ruleset/legality section. | No silent correction, fallback or hidden denominator is allowed. |
| Observation projection | pass | Participant-specific versioned projections exclude hidden, future, opponent-private and audit-only data. | Observation section. | No encoder, feature tensor or model input is approved. |
| RNG / seed / reproducibility | pass with note | Ownership, versions, seeds, substreams, retries and nondeterminism are required. | RNG/seed section. | Future review should bind immutable RNG identity and parallel substream/event-order policy. |
| Seat / role | pass | Assignment, rotation, asymmetry, grouping and balance reporting are covered. | Seat/role section. | No scheduler or opponent pool is approved. |
| Terminal / raw outcome | pass | Environment alone owns terminal state, validity and versioned raw outcome. | Terminal/raw-outcome section. | Raw outcome remains separate from reward, evaluation and strength evidence. |
| Error / abort / retry / resource | pass | Failure classes, validity, lineage, seeds, resource version and eligibility are auditable. | Error/resource section. | Silent retry, filtering, timeout extension and budget changes remain forbidden. |
| Concurrency / isolation | pass with note | State/RNG/model isolation, event ordering, race detection and partial failures are covered. | Concurrency section. | Future review should define transition serialization, partial-commit and duplicate-episode semantics. |
| Invariants / integrity | pass | Transition, ruleset, legality, identity, terminal and provenance invariants are listed. | Invariant section. | No executable Mahjong invariant or policy-strength conclusion exists. |
| Identity / version / provenance | pass | Environment, simulator and all authority-policy versions must be immutable and visible. | Identity/version/provenance section. | Version changes require comparability review and cannot be silent. |
| Candidate manifest | pass with note | Candidate fields cover current authority and status boundaries without becoming schema approval. | Candidate-manifest section. | Future refinement should add conformance/build, transition, retry-parent, failure, outcome and event-order identities. |
| Reward / objective interface | pass | Environment emits events/raw outcome only; reward mapping remains separate. | Reward interface section. | No reward implementation or return-as-strength interpretation is approved. |
| Model-output interface | pass | Model can propose only candidate actions under a separate future interface. | Model-output section. | No checkpoint, logits, model call or hidden-state access is approved. |
| Training / evaluation separation | pass | Uses require separate approval and visible frozen/versioned differences. | Training/evaluation section. | Bug fixes and configuration changes require version/comparability review. |
| Source / real data / third party | pass | No source, real data, account material, binary, weight or vendoring is approved or used. | Source and third-party sections. | Rights, privacy, provenance, integrity and security remain separate gates. |
| Evidence boundary | pass | Grade is P8 environment/simulator boundary definition evidence only. | Evidence and explicit non-evidence sections. | No executable, ranked, strength or promotion evidence is created. |
| ENV-E1-ENV-E15 | pass | Completed reviews, future boundary reviews, exact approval and exact `10_NEXT` remain independent gates. | Future entry-criteria section. | ENV-E6 closes only the docs review portion; ENV-E7-ENV-E15 remain future gates. |
| Stop conditions | pass | Premature entry, implementation, execution, leakage, silent correction/drift, real data and overclaim all stop work. | Stop-conditions section. | Blocked actions remain blocked. |
| Candidate next directions | pass | Raw-outcome/environment-provenance is the narrowest safe downstream definition task. | Candidate-direction table and dependency chain. | Define lineage only; do not implement a schema, parser, environment or execution path. |
| Governance synchronization | pass | Direct control documents preserve non-approval, non-evidence and exact next-task status. | Handoff, index, technical plan and governance records. | Keep the next task docs-only. |

## Scope and Planning Recap Review

The scope and recap pass:

- Full P7 is closed only for documented P7 supervised-learning scope.
- `12I`/`12J`, `12K`/`12L`, `12M`/`12N`, `12O`/`12P` and `12Q`/`12R`
  are accurately described.
- `12S` defines only a docs-only authority boundary.
- P8 entry, P8 implementation and an implementation prompt remain
  unapproved.
- P9-P12 remain unapproved.

The scoped phrase "No P8 self-play-specific environment, simulator or runner
is approved" is not a repository-global claim that no helper, test harness,
wrapper or historical environment concept exists.

## Vocabulary and Authority Separation Review

The vocabulary and responsibility split pass. The environment is the abstract
authority for state, rules, legality, transition, randomness, termination,
raw outcome, invariants and environment failures. A simulator is only a future
carrier or approximation. A participant/model proposes a candidate action;
the protocol owns identities, seed/seat/retry policies and provenance;
separately reviewed reward and evaluation specifications own neither state
transition nor terminal authority.

The boundary forbids silent illegal-action acceptance or rewriting, unapproved
reward embedding, model mutation of state and reward/evaluation takeover of
transition authority.

## Simulator Conformance Review

The simulator distinction passes because `12S` says that implementing or
approximating the boundary does not automatically make a simulator the rules
authority. A future simulator implementation should require a versioned
conformance statement or separately reviewed conformance evidence against the
declared environment authority boundary. Environment/simulator incompatibility
and version drift must remain visible.

This is a future review note. It does not approve a conformance schema, test,
simulator, authority implementation or execution path and does not block the
current docs-only review.

## Candidate Classes and State Review

All six candidate environment classes remain:

```text
approved_now = no
execution_allowed_now = no
implementation_allowed_now = no
```

Synthetic/local contract smoke is not self-play approval. Training and frozen
evaluation uses remain separate. Evaluation does not automatically create
strength evidence. Opponent-pool work remains unapproved, league work remains
P10, and deterministic replay/audit work does not approve real logs.

The authoritative-state boundary requires one explicit versioned state and
immutable episode identity, participant-specific projection, visibility
classification, isolation, transition lineage and declared invariants. It
creates no executable state schema, object, class, fixture, hash or validator.

## Reset and Transition Review

Reset/initialization passes: future reset must be explicit and atomic, bind
the manifest and versions, prevent prior-state leakage, retain retry lineage
and emit an invalid/aborted record on failure. Future records should make
non-first reset reasons and retry-parent identity explicit so a retry cannot
silently replace participant, version, seed, state or resource context.

The candidate step input/output concepts cover episode/step identity,
pre/post-state identity, actor/action source, legality, applied action, events,
terminal/outcome status, errors and provenance. They are not an API or schema.
Future review should define:

- atomic transition application.
- stale pre-state rejection.
- duplicate-request handling.
- idempotency or immutable transition identity.
- exactly-once versus at-most-once application semantics.
- monotonic step indexing and no unrecorded transition.

`12S` already forbids silent duplicate application and unrecorded transition,
so these are future contract refinements rather than blockers.

## Legality and Observation Review

Ruleset and legality authority pass. One immutable ruleset version governs an
episode, the legal set derives only from authoritative state, the environment
independently validates the candidate action and mismatch/failure is explicit.
No silent substitution, fallback or hidden denominator is allowed.

Observation projection also passes. Public, private, hidden, audit-only,
decision-time and post-outcome information are separated. A versioned
participant-specific projection cannot contain opponent-private, future,
post-outcome or audit-only data. No encoder, feature tensor, model input or
dataset example is implemented or approved.

## RNG, Seat and Reproducibility Review

The boundary requires RNG ownership, algorithm/version, run/episode/component
seeds, stochastic-source inventory, seat/retry policy, ordering, known
nondeterminism and replay expectation. It correctly states that equal seeds do
not prove reproducibility, global mutable RNG is forbidden and parallel
episodes need isolated RNG state.

Future review should make immutable RNG-state/substream identity, substream
collision prevention, retry seed reuse, parallel scheduling/event-order
effects and time/resource nondeterminism explicit. This is not current RNG
implementation permission.

Seat/role assignment covers assignment method, ordering, balance, asymmetric
starts, rotation, mirror/duplicate policy and comparison grouping. Seat
context remains necessary for later reward/evaluation accounting. No scheduler
or opponent pool is approved.

## Terminal, Failure and Concurrency Review

The environment is the sole authority for terminal status, termination reason,
episode validity and versioned raw outcome/provenance. Raw outcome is not
reward, evaluation or strength evidence, and post-terminal transition is
forbidden unless separately modeled and logged.

Failure handling distinguishes invalid action, participant/environment error,
ruleset/invariant/artifact/protocol mismatch, timeout, resource/concurrency
failure, cancellation and unknown failure. Future records retain validity,
abort reason, retry lineage/seeds, resource version, evidence eligibility and
outcome/provenance completeness. Silent retry, success-only filtering, timeout
extension and resource-budget drift are forbidden.

Concurrency coverage passes. Future work must isolate state, RNG and model
state, preserve deterministic event ordering, prevent cross-episode leakage,
version concurrency configuration, detect races and audit partial failures.
Future review should define transition serialization, partial-commit/rollback,
worker retry, cancellation isolation and duplicate-episode handling. No worker,
queue, process pool or distributed runner is approved.

## Invariant, Identity and Manifest Review

Candidate invariants cover transition validity, ruleset/participant/seat/
legality consistency, monotonic step indices, impossible states, duplicate
transitions, terminal immutability, provenance, artifact versions and replay
expectation. They are non-executable candidates and cannot prove policy
strength.

Identity/version/provenance fields bind environment, simulator, ruleset,
protocol, state, observation, legality, transition, RNG, termination, raw
outcome, retry/resource policy, code/config and artifacts. Version changes are
visible and may invalidate comparability.

The candidate manifest is sufficient for the current semantic boundary and is
not an approved schema/API/fixture. Future refinement should explicitly bind:

- simulator-to-environment conformance version.
- environment immutable build/artifact identity.
- transition identity/policy version.
- retry parent and failure lineage.
- raw-outcome provenance identity.
- concurrency and event-order policy identity.

These are future candidate fields only and do not block closure.

## Dependency and Use-Separation Review

Environment output remains limited to versioned events and raw outcome.
Reward mapping stays separately reviewed and cannot own state, legality,
terminal status or evaluation. A future model may only propose candidate
actions and cannot mutate state, provide the legal set/terminal/outcome or
access hidden state. No model output, checkpoint, logits or model call exists.

Training and evaluation are separately approved uses. Their differences must
be versioned and visible; evaluation configuration and participants must be
frozen; environment changes cannot silently propagate; bug fixes require a
new version and comparability review. Neither use is approved now.

## Source, Artifact and Evidence Review

No source, ingestion, real Tenhou, real haifu, external log, platform data,
account/session material, Akochan binary, unknown simulator, model weight or
third-party rules engine is approved, accessed, downloaded or vendored.
Future source and third-party use retain independent rights, privacy,
provenance, integrity, interface and security review.

Current evidence grade is:

```text
P8 environment / simulator boundary review evidence only.
```

It supports only the conclusion that the docs-only authority boundary was
reviewed and found sufficient for the current planning scope.

## ENV-E1 Through ENV-E15 Review

ENV-E1 through ENV-E15 pass. In particular:

- ENV-E1-ENV-E5 accurately reference completed scope, taxonomy, dependency,
  protocol and objective/reward reviews.
- ENV-E6 is satisfied only for the docs-only definition and review.
- ENV-E7-ENV-E13 retain separate state/observation/legality/transition, RNG,
  terminal/outcome, failure/retry/resource, provenance, model-output,
  training/evaluation and source governance.
- ENV-E14 still requires a separate exact approval decision.
- ENV-E15 still requires exact `10_NEXT` authorization.

No ENV-E criterion is implementation approval by itself. Defined and reviewed
does not mean implemented.

## Stop Conditions Review

The stop conditions pass. They stop on implied P8 entry/implementation,
implementation prompts, environment/simulator/runner/reset/transition code,
episodes/matches/self-play/RL/training/evaluation/league, reward/RL selection,
model/checkpoint calls, hidden-state leakage, model-owned authority, silent
correction/retry/filtering, untracked RNG, silent version/resource drift,
real/external/platform data, ingestion, code/tests/fixtures/data, strength or
ranked overclaim, P9-P12 jump, unauthorized `10_NEXT` implementation and
unknown third-party artifacts.

## Candidate Next Directions Review

No candidate other than this review is executed now. The narrowest downstream
docs-only task is:

```text
Define P8 raw-outcome and environment-provenance boundary before any implementation.
```

The environment authority already owns terminal/raw-outcome generation, and
`12Q`/`12R` require immutable raw-outcome provenance before any future reward
mapping. Defining the environment-to-raw-outcome lineage therefore precedes a
model-output interface, training/evaluation use or algorithm selection.

The next task must not approve P8 entry/implementation, create an
implementation prompt, implement a raw-outcome schema/parser/environment/
simulator/runner, execute transitions/episodes/self-play/RL, implement reward,
select an RL algorithm, run training/evaluation/league, approve source/real
data/model output, claim strength or enter P9-P12.

## Governance Synchronization Review

Handoff, index, `10_NEXT`, technical plan, evidence log, risk register,
decision record, stage contract, changelog, milestones and backlog are aligned
to this review, its non-blocking future notes, the non-approval posture and the
next docs-only raw-outcome/environment-provenance boundary task.

## Validation Results

```text
git diff --check: passed
parser-reader smoke extension: passed, 15 tests
parser-reader smoke: passed, 11 tests
feature-label schema: passed, 11 tests
synthetic supervised fixture schema: passed, 1 test
replay schema: passed, 7 tests
synthetic replay fixture schema: passed, 1 test
```

## Review Decision

```text
A. Review can close.
```

No blocker or overclaim was found. Notes about simulator conformance,
reset/retry identity, transition atomicity/idempotency, RNG substreams,
parallel event ordering/partial failure and manifest provenance are future
boundary refinements. They do not modify `12S`, approve a schema/API or grant
current implementation or execution permission.

## Next Task Recommendation

```text
Define P8 raw-outcome and environment-provenance boundary before any implementation.
```

The next task must remain docs-only. It must not approve P8 entry or
implementation, create an implementation prompt, implement a raw-outcome
schema, parser, environment, simulator or runner, execute transitions,
episodes, matches, self-play or RL, implement reward/objective, select an RL
algorithm, run training, tuning, evaluation or league, approve source/real
data/model-output work, claim strength or enter P9-P12.

## Evidence Grade

```text
P8 environment / simulator boundary review evidence only.
```

## Explicit Non-Evidence

This review is not P8 entry/implementation approval, an implementation prompt
or executable task, environment/simulator/runner/API/schema/state/reset/step/
transition implementation, episode/match/self-play/RL execution, reward/
objective/loss implementation, RL algorithm selection, training, tuning,
evaluation, league, source approval/ingestion, real Tenhou/haifu/external/
platform data, model-output integration, strength/Tenhou-ranked/stable-dan/
LuckyJ/promotion evidence or P9-P12 approval.
