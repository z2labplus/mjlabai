# 12R_P8_RL_OBJECTIVE_REWARD_SPECIFICATION_BOUNDARY_REVIEW_BEFORE_ANY_IMPLEMENTATION

## Scope

This document reviews
`docs/12_technical_plan/12Q_P8_RL_OBJECTIVE_REWARD_SPECIFICATION_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`.

This is a docs-only review gate. It does not modify `12Q`, approve P8 entry or
implementation, create an implementation prompt or executable task, select or
implement a reward/objective/loss or RL algorithm, or execute self-play, RL,
training, tuning, evaluation, league, source ingestion, real-data access,
model-output integration or P9-P12 work.

## Reviewed Artifacts

Primary artifact:

- `docs/12_technical_plan/12Q_P8_RL_OBJECTIVE_REWARD_SPECIFICATION_BOUNDARY_BEFORE_ANY_IMPLEMENTATION.md`

Planning context:

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

Each row records result, finding, evidence and downstream implication.

| review area | result | finding | evidence | downstream implication |
|---|---|---|---|---|
| Scope | pass | `12Q` is definition evidence only and grants no entry, selection or execution permission. | Scope and explicit non-evidence sections. | Continue docs-only planning only. |
| Full P7 / P8 recap | pass | Closure and P8 planning-chain status are accurate and bounded. | `03BL`, `12F`-`12P` references. | P8 and P9-P12 remain unapproved. |
| Non-approval baseline | pass | No executable objective, reward, loss, algorithm, environment or run is approved. | Non-approval baseline. | No implementation proposal or approval follows from this review. |
| Vocabulary | pass | Raw outcome, reward, objective, loss, diagnostics, evaluation and strength terms are distinct. | Vocabulary table. | Future specs must preserve this separation. |
| Concept separation | pass | Seven evidence/optimization layers are explicit. | Objective/reward/evaluation separation. | Return or loss cannot substitute for strength evidence. |
| Candidate families | pass with note | All nine families are unapproved, unselected and non-executable; evaluation-only metrics are classification only. | Candidate-family table. | A future review must prevent evaluation metrics from becoming rewards by default. |
| Signal source/timing | pass | Future source, timing, recipient, visibility, provenance and determinism are required. | Signal source/timing boundary. | Future records must bind to versioned upstream identities. |
| Invalid/abort/retry | pass with note | Silent deletion and success-only selection are forbidden; lineage is required. | Failure/retry boundary. | Future manifest/schema work should make episode and retry lineage explicit. |
| Seat/role/opponent bias | pass | Asymmetry, ordering, distributions, retries and invalid denominators are covered. | Bias boundary. | Future normalization needs separate review and evidence. |
| Reward hacking/mismatch | pass | Required exploit classes, monitoring, stop and rollback concepts are comprehensive. | Reward-hacking boundary. | Every future component needs an explicit anti-exploit record. |
| Scaling/weighting/normalization | pass | Required fields and immutable version changes are defined; no values are selected. | Scaling boundary. | Numerical choices remain separately reviewed and approved. |
| Credit assignment | pass | Sparse/delayed/multi-agent ambiguity is covered without choosing an algorithm. | Credit-assignment boundary. | Return, advantage and value-target work remains unapproved. |
| Algorithm/loss independence | pass | Reward semantics do not imply PPO/DQN/A2C/MCTS or an executable loss. | Algorithm/loss boundary. | Algorithm selection needs a separate boundary and approval chain. |
| Training/evaluation separation | pass | Training rewards/episodes cannot replace evaluation metrics/holdouts. | Training/evaluation section. | Evaluation freezing, leakage and version rules remain separate. |
| Model-strength evidence | pass | Approved protocol, sample, uncertainty, leakage and accounting remain prerequisites. | Strength boundary. | High return cannot support strength claims. |
| Tenhou/stable-dan/LuckyJ/promotion | pass | No current ranked or comparison evidence exists. | Ranked-evidence boundary. | The north-star target is not a reward approval. |
| Source/real data | pass | No source, ingestion, account material or real data is approved or accessed. | Source/real-data boundary. | Rights/privacy/platform review remains separate. |
| Model-output/environment dependency | pass with note | Both remain unapproved and required before future reward execution. | Dependency boundary. | Environment/simulator authority is the next narrow docs-only dependency. |
| Candidate reward-spec record | pass with note | Candidate fields are sufficient for current semantics but are not schema approval. | Candidate record section. | Future refinement should explicitly bind protocol, environment, raw-outcome and retry-lineage versions. |
| Evidence boundary | pass | Grade is boundary-definition evidence only. | Evidence section. | No executable or strength evidence is created. |
| OR-E1-OR-E15 | pass | Review, environment, provenance, model, source, exact approval and `10_NEXT` gates remain independent. | OR-E1-OR-E15. | No criterion alone grants implementation permission. |
| Stop conditions | pass | Premature selection, execution, data/model use, overclaim and stage jump all require stopping. | Stop-conditions section. | Blocked actions remain blocked. |
| Candidate next directions | pass | Review is current; environment/simulator boundary is the safest next docs-only dependency. | Candidate-direction table. | Define only the environment/simulator authority boundary next. |
| Governance synchronization | pass | Direct control documents preserve non-approval and non-evidence status. | Handoff, index, plan and governance records. | Keep the next task docs-only and exact. |

## Scope and Planning Recap Review

The scope and recap pass:

- Full P7 is closed only for documented P7 supervised-learning scope.
- `12I`/`12J`, `12K`/`12L`, `12M`/`12N` and `12O`/`12P` are accurately
  described.
- `12Q` is a docs-only definition artifact, not entry, implementation,
  selection, execution or evidence approval.
- P8 entry and implementation remain unapproved.
- P9-P12 remain unapproved.

## Non-Approval and Vocabulary Review

The baseline passes. No objective/reward specification, reward function,
executable loss, policy update, discount factor, component weight, scaling,
normalization, clipping, return calculation, advantage/value target, trainer,
optimizer, environment, model-output path, self-play, RL, training or
evaluation is approved.

The vocabulary separates raw outcome, objective, reward component, return,
loss-facing quantities, diagnostics, evaluation metrics, strength evidence,
ranked evidence, transformations, credit assignment and version manifests.
In particular:

```text
raw outcome != reward
reward != objective
objective != executable loss
training diagnostic != evaluation metric
evaluation metric != model-strength or ranked evidence
```

This vocabulary creates no algorithm or implementation permission.

## Objective / Reward / Evaluation Separation Review

The seven-layer separation passes:

1. protocol raw outcome.
2. training reward.
3. optimization objective or loss.
4. training diagnostic.
5. offline evaluation metric.
6. model-strength evidence.
7. Tenhou, stable-dan, LuckyJ or promotion evidence.

Raw outcome does not automatically become reward, reward does not
automatically become loss, and return/loss/self-play win rate does not
automatically establish strength. Stable dan `> 10.68` remains a long-term
evaluation target, not a reward formula. LuckyJ comparison remains a separate
approved evidence chain.

## Candidate Objective / Reward Families Review

All nine candidate families pass the non-selection review. Every family
remains:

```text
approved_now = no
selected_now = no
implementation_allowed_now = no
```

No formula, sign, scale, weight, discount, clipping threshold or
normalization is selected. Placement, score, legality, shaping, risk-aware,
auxiliary and multi-component candidates are not presumed correct.

`evaluation-only metric family` is a separation/classification reminder. It
is not a reward candidate and cannot become a reward merely because it appears
in the candidate-family inventory. This is an explicit future review note,
not a blocker.

## Signal Source, Timing and Provenance Review

The source/timing boundary passes. A future component must identify source
field/event, step or terminal timing, computation time, recipient, visibility,
environment/outcome derivation, version, provenance and deterministic
expectation. Terminal or post-outcome information cannot enter a decision-time
observation.

Future candidate records should bind these concepts explicitly to immutable
`protocol_version`, `environment_version` and `raw_outcome_schema_version`
identities rather than relying only on a generic provenance field. `12Q`
already requires version/provenance and upstream linkage, so this is a future
field-level refinement rather than a blocker or schema approval.

## Invalid, Abort, Retry and Bias Review

The failure boundary passes. Invalid/aborted episodes cannot be silently
deleted, retries must preserve lineage and seeds, replacement versus
supplement behavior must be explicit, and reward eligibility remains distinct
from evidence eligibility. Future records should carry explicit
`episode_id`, `parent_episode_id` or equivalent retry lineage plus protocol,
environment, outcome-schema and participant/artifact versions.

The seat/role/opponent boundary also passes. Seat and starting asymmetry,
participant ordering, opponent/policy distributions, retry selection,
invalid/aborted denominators, self-copy limitations and non-stationarity are
covered. No normalization or opponent pool is approved. These controls prevent
success-only sample selection from being mistaken for improvement.

## Reward-Hacking, Scaling and Credit Review

The anti-hacking boundary covers terminal-state, episode-length, stalling,
forced-abort, retry, illegal/fallback, score/placement, local/long-term,
shaping, clipping, scale, collusion, collapse, environment-bug, cherry-pick
and overclaim risks. Every future component must record intended behavior,
failure modes, invariants, monitors, stop triggers, rollback and evidence
limits.

Scaling/weighting/normalization requirements are auditable and versioned. No
number is selected. Aggregate returns must remain decomposable to components,
and transformations cannot hide seat, opponent or invalid-episode bias.

Credit-assignment coverage includes per-step/terminal, delayed/sparse,
multi-agent and invalid/aborted attribution. No return, advantage estimator,
value target or policy/value loss is selected or implemented.

## Algorithm, Training and Evaluation Independence Review

The boundary correctly keeps reward semantics independent from PPO, DQN,
A2C, MCTS, policy gradient and all other algorithm choices. It approves no
policy/value loss, entropy/KL term, optimizer or trainer.

Training reward cannot replace evaluation metrics. Training episodes cannot
automatically become holdout evidence. Evaluation freezing, versioning,
reward-tuning disclosure and leakage prevention remain separately reviewed and
approved. No executable loss or training/evaluation path exists.

## Strength, Ranked and Promotion Evidence Review

No current artifact is model-strength, Tenhou ranked, stable-dan ranked-game,
LuckyJ `10.68` comparison or promotion evidence. Future strength evidence
still requires approved evaluation and model-output paths, sample definition,
sample size, uncertainty, leakage controls, seat/opponent/version accounting,
governance review and separate approval.

High reward, high return, lower training loss, self-play dominance, unit tests,
synthetic smoke and boundary documents cannot support those claims.

## Source, Model-Output and Environment Review

The source boundary passes. No real Tenhou, real haifu, external log, platform
data, account/session/cookie/token material or ingestion is accessed or
approved. Future real-data and self-play-data work retain separate rights,
privacy, platform, provenance and approval chains.

No model-output path or P8 execution environment/simulator is approved. Future
reward execution requires reviewed transition authority, legality,
termination, raw-outcome provenance, protocol manifest and model interface,
then a separate exact approval decision and exact `10_NEXT` authorization.

Because environment/simulator authority is the common upstream dependency for
transition, legality, termination, raw-outcome generation and later reward
execution, defining that authority boundary is the narrowest safe next
docs-only task. It does not approve or implement an environment.

## Candidate Reward Specification Record Review

The candidate record passes for the current semantic boundary. It can express
identity/version, source/timing/recipient, transformations, failure/retry,
bias context, anti-exploit controls, provenance, statuses and non-evidence
warnings.

The fields remain candidates only. They are not an approved schema, fixture,
parser, reward implementation or training configuration. A future schema
review should make protocol/environment/raw-outcome versions and episode/retry
lineage explicit. This refinement is not current implementation permission and
does not block closure because `12Q` already requires those relationships in
the surrounding boundary text.

## OR-E1 Through OR-E15 Review

OR-E1 through OR-E15 pass. In particular:

- OR-E5 requires `12Q` to be defined and reviewed; this review closes only
  that docs-only criterion.
- OR-E6-OR-E12 retain separate environment, outcome-provenance, timing,
  failure/retry, bias, training/evaluation and model-output gates.
- OR-E13 retains separate source/real-data governance.
- OR-E14 requires a separate approval decision.
- OR-E15 requires exact `10_NEXT` authorization.

No OR-E criterion is implementation approval by itself.

## Stop Conditions Review

The stop conditions pass. They stop on implied P8 entry/implementation,
implementation prompts, final reward or numeric selection, RL algorithm
selection, reward/loss code, self-play/RL/training/evaluation/league,
model/checkpoint use, unapproved environments, real/external/platform data,
ingestion, code/tests/fixtures/data, return-as-strength claims, ranked or
promotion claims, P9-P12 jumps, unauthorized `10_NEXT` implementation,
unknown artifacts and third-party binaries.

## Candidate Next Directions Review

No candidate other than this review is executed now. With the objective/reward
semantic boundary reviewed, the narrowest next docs-only planning task is:

```text
Define P8 environment / simulator boundary before any implementation.
```

Environment authority precedes any later reward execution, model-output path,
algorithm selection or training/evaluation run. The next task must not approve
P8 entry/implementation, implement an environment/simulator/runner, select or
implement reward/RL, execute self-play/training/evaluation/league, approve
source/real-data/model-output work, claim strength or enter P9-P12.

## Governance Synchronization Review

Handoff, index, `10_NEXT`, technical plan, evidence log, risk register,
decision record, stage contract, changelog, milestones and backlog are aligned
to this review, the non-approval posture and the next docs-only environment /
simulator boundary task.

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

No blocker or overclaim was found. Notes about evaluation-only metrics,
explicit upstream-version identities, episode/retry lineage and environment
authority are future boundary refinements. They do not select a reward,
approve a schema or grant current execution permission.

## Next Task Recommendation

```text
Define P8 environment / simulator boundary before any implementation.
```

The next task must remain docs-only and must not approve P8 entry or
implementation, create an implementation prompt, implement an environment,
simulator or runner, implement or select reward/RL, execute self-play,
training, tuning, evaluation or league, approve source/real-data/model-output
work, claim strength or enter P9-P12.

## Evidence Grade

```text
P8 RL objective / reward specification boundary review evidence only.
```

## Explicit Non-Evidence

This review is not P8 entry/implementation approval, an implementation prompt
or executable task, objective/reward/loss or RL-algorithm selection,
environment/simulator/runner implementation, self-play/RL/training/tuning/
evaluation/league, source approval/ingestion, real Tenhou/haifu/external/
platform data, model-output integration, strength/Tenhou-ranked/stable-dan/
LuckyJ/promotion evidence or P9-P12 approval.
