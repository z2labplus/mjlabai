# 12P_P8_SELF_PLAY_PROTOCOL_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION

## Scope

This document reviews
`docs/12_technical_plan/12O_P8_SELF_PLAY_PROTOCOL_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`.

This is a docs-only review gate. It does not modify `12O`, approve P8 entry or
implementation, create an implementation prompt or executable task, or
execute self-play, RL, training, tuning, evaluation, league, source ingestion,
real-data access, model-output integration or P9-P12 work.

## Reviewed Artifacts

Primary artifact:

- `docs/12_technical_plan/12O_P8_SELF_PLAY_PROTOCOL_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`

Planning context:

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

| review area | result | finding |
|---|---|---|
| Scope | pass | `12O` is definition evidence only and grants no entry or execution permission. |
| Full P7 / P8 recap | pass | Closure and P8 planning-chain status are accurate and bounded. |
| Non-approval baseline | pass with note | No P8 self-play-specific runner, environment or simulator is approved; this is not a repository-global capability claim. |
| Protocol vocabulary | pass | Required identities, lifecycle, information, action, outcome and evidence terms are distinct. |
| Candidate classes | pass | All five classes have `approved_now = no` and `execution_allowed_now = no`. |
| Participant / artifact identity | pass with note | Episode-local policy immutability is explicit; future cross-episode updates require versioned schedule and artifact identity. |
| Episode lifecycle | pass | Validation, assignment, observation, legal action, transition, termination and provenance are ordered and descriptive only. |
| Information / observation | pass | Decision-time/public-private/provenance rules prevent hidden, future and post-outcome leakage. |
| Action / legality | pass | Separately approved legal set, no silent correction/fallback and deterministic invalid handling are required. |
| Seed / seat / reproducibility | pass with note | Seeds and assignment are recorded; future environment work must address seat/retry selection bias and resource nondeterminism. |
| Termination / abort / invalid episode | pass | Failure classes and evidence eligibility are explicit; invalid/aborted episodes cannot silently enter evidence. |
| Candidate manifest | pass with note | Fields are candidates only; retry lineage, update schedule, resource policy and raw-outcome schema remain future refinements. |
| Training / evaluation separation | pass | Protocol classes and evidence reuse are separated. |
| RL objective / reward | pass | Reward definition remains a separate docs-only boundary and no algorithm/loss/reward is selected. |
| Opponent pool / league | pass | Pool, matchmaking, league and promotion remain unapproved/later-stage. |
| Source / real data | pass | Rights, privacy, platform and ingestion chains remain separate and unapproved. |
| Model output | pass | Interface, checkpoint and model calls remain unapproved. |
| Evidence boundary | pass | Grade is protocol-boundary definition evidence only. |
| SP-E1-SP-E15 | pass | Separate reviews, approval decision and exact `10_NEXT` authorization are required. |
| Stop conditions | pass | Stage jumps, execution, data/model/artifact access and overclaims require stopping. |
| Candidate directions | pass | Review is the only current action; objective/reward boundary is the next safe docs-only definition. |
| Governance synchronization | pass | Control documents consistently keep all execution and stronger evidence unapproved. |

## Full P7 / P8 Planning Recap Review

The recap passes:

- Full P7 is closed only for documented P7 supervised-learning scope.
- `12I`/`12J`, `12K`/`12L` and `12M`/`12N` are accurately described.
- P8 remains docs-only planning; P8 entry and implementation are unapproved.
- P9-P12 remain unapproved.

## Non-Approval Baseline Review

The baseline passes with one scope note. The phrase "No runner, environment or
simulator exists or is approved" appears inside the P8 self-play protocol
non-approval section and is reviewed only as:

```text
No P8 self-play-specific runner, environment or simulator exists or is approved.
```

It is not a global assertion about every repository helper, wrapper, test
harness or historical environment concept. The surrounding scope and repeated
non-approval language prevent a substantive misreading, so this is a review
note rather than a blocker. Future governance summaries must use the scoped
formulation.

No participant policy, checkpoint, model-output path, RL reward/objective,
opponent pool, league or real-data source is approved. No self-play result
evidence exists, and raw future outcomes would not be strength evidence by
default.

## Protocol Vocabulary Review

The vocabulary passes. It distinguishes protocol/version, run/episode/match,
participants and roles, policy/artifact/checkpoint/environment identities,
ruleset, seed/seat assignment, observation/decision-time information, legal/
selected/fallback actions, transition/termination, invalid/aborted/retry,
provenance/manifest/raw outcome, training/evaluation self-play, opponent pool,
frozen/mutable policy and evidence/non-evidence warnings.

Vocabulary definition grants no implementation or execution permission.

## Candidate Protocol Classes Review

All candidate classes pass:

- synthetic/local protocol smoke.
- training self-play protocol.
- frozen-policy evaluation self-play.
- opponent-pool protocol.
- league protocol.

Every class is `approved_now = no` and `execution_allowed_now = no`. Training
self-play cannot double as evaluation. An evaluation label cannot create
strength evidence. Opponent-pool work remains unapproved and league remains
later-stage P10 work.

## Participant / Artifact Identity Review

The identity boundary passes with a future refinement note:

- participant, role, policy version and immutable artifact identity are
  required.
- code, configuration, ruleset, environment and protocol versions are
  required.
- checkpoint use remains separately approved only.
- policy behavior cannot silently change inside an episode.
- evaluation episodes require stricter separately approved freezing/version
  rules.
- unknown weights/checkpoints and unapproved artifacts are forbidden.

If future training allows policy changes between episodes, the manifest or a
separately reviewed run protocol must record the update schedule, resulting
`policy_version`, immutable `artifact_id`, parent version and effective episode
range. A `participant_id` cannot silently point to a different policy. This is
a future field-level requirement, not an approval or a current blocker.

## Episode Lifecycle Review

The lifecycle passes. It orders manifest, identity, ruleset/environment,
seed/seat and state validation before decision-time observation. Model output
requires separate approval, selected actions require legality validation, and
termination records raw outcome and provenance while separating valid,
invalid and aborted episodes. Silent discard and silent retry are forbidden.

The lifecycle is descriptive only. It creates no environment, runner, model
call, action, transition or episode.

## Information / Observation Review

The boundary passes. It requires decision-time information, explicit public/
private classification, versioned observation provenance and no hidden,
future, post-outcome or opponent-private leakage. It does not implement an
encoder, create feature tensors or treat P7 smoke artifacts as self-play
observation approval.

## Action / Legality Review

The boundary passes. A separately approved environment must provide the legal
set; the selected action must belong to it. Illegal-action and fallback policy
must be explicit, deterministic and auditable. Silent correction, unlogged
fallback and hidden illegal-action rates are forbidden. No legal-action
engine, sampler, fallback or transition is implemented.

## Seed / Seat / Reproducibility Review

The boundary passes with future bias-control notes. It records run/episode
seeds, participant ordering, seat assignment, versions, configuration hash,
artifact identity, retries, replay expectations and known nondeterminism. It
correctly states that the same seed alone is not full reproducibility.

Future environment/run boundaries must additionally specify:

- a seat-assignment design and balance report sufficient to detect systematic
  seat bias.
- retry lineage, original and retry seeds, participant ordering and the rule
  deciding whether the retry replaces or supplements the original episode.
- denominators that retain invalid/aborted episodes instead of silently
  selecting successful episodes.
- timeout/resource-budget versions and declared time/resource nondeterminism.

These are follow-up requirements because `12O` already requires recorded seat
assignment, explicit retry policy, known nondeterminism and no silent discard.
They are not current execution permission and do not block boundary review.

## Termination, Abort and Invalid-Episode Review

The boundary passes. It distinguishes normal/rules terminal, timeout, invalid
action, environment/participant error, artifact/protocol mismatch, manual
cancellation, resource failure and unknown failure. It requires termination,
validity, abort, retry, evidence-eligibility, raw-outcome availability and
provenance fields. Invalid or aborted episodes cannot silently enter training
or evaluation evidence.

## Candidate Manifest Review

The candidate manifest passes. It covers protocol/run/episode/class,
ruleset/environment, participant/artifact/policy, frozen status, seeds/seat,
observation/action/termination/retry/provenance versions, source/real-data/
training/evaluation/self-play/league/strength status and non-evidence warning.

The fields are candidates only. They are not an approved schema and authorize
no JSON fixture, data file, code, parser, reader or ingestion. Future reviews
should consider `parent_episode_id` or equivalent retry lineage, policy-update
schedule, timeout/resource-budget version and raw-outcome schema version. Their
absence is not a blocker at this docs-only boundary because the corresponding
identity, retry, resource-failure, raw-outcome and provenance concepts already
exist and remain separately gated.

## Training vs Evaluation Self-Play Review

The separation passes. Training/evaluation are different protocol classes;
training episodes do not automatically become holdout evaluation; evaluation
requires separately approved freezing/version rules; evaluation policies
cannot silently update inside an episode; result reuse requires approval; raw
outcomes and win rate are not strength evidence. Neither class is approved.

## RL Objective / Reward Boundary Review

The boundary passes. Protocol semantics precede reward/objective definition.
Reward requires a separate docs-only boundary and review; raw outcome does not
automatically become reward; reward-hacking/objective-mismatch risks remain
open; and no algorithm, loss, reward implementation or RL execution is
approved.

## Opponent Pool / League Review

The boundary passes. Opponent pool, matchmaking, historical-checkpoint pool,
league, mainline and promotion remain unapproved. League is later-stage P10.
Copies of one policy do not establish robustness, and diversity claims require
separate evidence.

## Source / Real-Data Review

The boundary passes. It approves and accesses no Tenhou, real haifu, external
logs, platform data or account/session/cookie/token material. Future real data
requires independent rights/privacy/platform/approval/ingestion gates. Future
self-play-generated data requires a separate provenance/data boundary. No
self-play data is created.

## Model-Output Review

The boundary passes. No model-output integration, interface, checkpoint,
logits, values or policy distribution is approved or produced. Future model
calls require independent interface/schema/environment/evaluation/risk review
and approval.

## Evidence Boundary Review

The evidence grade is correctly limited to:

```text
P8 self-play protocol boundary definition evidence only.
```

It supports vocabulary, lifecycle, information/action, reproducibility and
future-review readiness only. It supports no entry, implementation, self-play
result, RL, training, evaluation, league, model-output, strength, Tenhou,
stable-dan, LuckyJ or promotion evidence.

## SP-E1 Through SP-E15 Review

SP-E1 through SP-E15 pass. In particular:

- SP-E4 requires this boundary to be reviewed.
- SP-E5-SP-E12 retain separate environment, identity, observation, legality,
  reproducibility, termination, model-output and training/evaluation gates.
- SP-E13 preserves separate source/real-data governance.
- SP-E14 requires a separate exact approval decision.
- SP-E15 requires exact `10_NEXT` authorization.

No SP-E criterion is implementation approval by itself.

## Stop Conditions Review

The stop conditions pass. They stop on implied entry/implementation approval,
an implementation prompt, self-play/RL/training/evaluation/league, premature
algorithm/reward execution, model/checkpoint/unknown artifact use, real or
external data, ingestion, code/tests/fixtures/data/runners/environments,
strength/Tenhou/stable-dan/LuckyJ/promotion claims, P9-P12 jumps,
unauthorized `10_NEXT` implementation or third-party binary use.

## Candidate Next Directions Review

No candidate other than this review is executed now. With the protocol
boundary reviewed, the narrowest next docs-only planning task is:

```text
Define P8 RL objective / reward specification boundary before any implementation.
```

This follows `12O`'s dependency order. It does not approve or implement a
reward, select an RL algorithm, execute RL/self-play/training/evaluation/
league, approve P8 entry/implementation, use source/real/model data or enter
P9-P12.

The environment/simulator boundary remains required under SP-E5 and must be
defined and reviewed before any future execution. It does not need to precede
the docs-only reward/objective semantic boundary because that next task cannot
execute or assume an environment.

## Governance Synchronization Review

Handoff, index, `10_NEXT`, technical plan, evidence log, risk register,
decision record, stage contract, changelog, milestones and backlog are aligned
to this review, the non-approval posture and the next docs-only objective/
reward boundary task.

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

No blocker or overclaim was found. The four review notes above are explicit
future boundary refinements, not present execution permission and not blockers
to closing this docs-only protocol-boundary review.

## Next Task Recommendation

```text
Define P8 RL objective / reward specification boundary before any implementation.
```

The next task must remain docs-only and must not approve P8 entry or
implementation, create an implementation prompt, implement reward, select or
run RL, execute self-play/training/tuning/evaluation/league, approve source/
real-data/model-output work, claim strength or enter P9-P12.

## Evidence Grade

```text
P8 self-play protocol boundary review evidence only.
```

## Explicit Non-Evidence

This review is not P8 entry/implementation approval, an implementation prompt
or executable task, self-play/RL/training/tuning/evaluation/league, source
approval/ingestion, real Tenhou/haifu/external/platform data, model-output
integration, reward implementation, model-strength/Tenhou-ranked/stable-dan/
LuckyJ/promotion evidence or P9-P12 approval.
