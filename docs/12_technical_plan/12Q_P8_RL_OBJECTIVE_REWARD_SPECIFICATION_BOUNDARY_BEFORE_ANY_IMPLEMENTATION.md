# 12Q_P8_RL_OBJECTIVE_REWARD_SPECIFICATION_BOUNDARY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 RL objective / reward specification boundary
before any implementation. It is a docs-only planning artifact.

This task is not P8 entry or implementation approval, an implementation
prompt or first executable task, reward/objective/loss implementation, RL
algorithm selection for execution, self-play or RL execution, training,
tuning, evaluation, league, source approval/ingestion, real-data access,
broad file ingestion, CLI work, feature/label/dataset construction,
model-output integration, strength evidence, Tenhou ranked evidence,
stable-dan evidence, LuckyJ `10.68` comparison, promotion or P9-P12 approval.

North-star relationship: this boundary supports the long-term Tenhou
stable-dan `> 10.68` goal only by preventing future optimization signals from
being confused with evaluation evidence. It does not select a reward and is
not evidence that a model can beat LuckyJ.

## Full P7 / P8 Planning Recap

- Full P7 is closed only for documented P7 supervised-learning scope.
- `12I`/`12J` defined and reviewed P8 scope and entry criteria.
- `12K`/`12L` defined and reviewed the P8 risk/evidence taxonomy.
- `12M`/`12N` defined and reviewed the P8 self-play/RL dependency map.
- `12O`/`12P` defined and reviewed the P8 self-play protocol boundary.
- `12P` recorded `A. Review can close.`
- P8 remains docs-only planning; entry and implementation are unapproved.
- P9-P12 remain unapproved.

## P8 Objective / Reward Non-Approval Baseline

- No RL objective or reward specification is approved for execution.
- No P8 reward function exists or is approved for execution.
- No RL loss, policy-update rule, discount factor, reward weight/coefficient,
  scaling, normalization or clipping rule is approved.
- No training loop, self-play execution or evaluation is approved.
- No model-output path or P8 execution environment/simulator is approved.
- No reward evidence or RL-result evidence exists.
- Training return is not model-strength evidence.
- No current artifact is Tenhou, stable-dan, LuckyJ or promotion evidence.

## Objective / Reward Vocabulary

| term | boundary meaning |
|---|---|
| raw outcome | Uninterpreted protocol result before reward mapping. |
| objective / optimization objective | Future quantity an approved optimizer would seek to improve. |
| reward / reward component | Future versioned training signal or one decomposable part. |
| per-step / terminal reward | Signal assigned during a transition or after terminal outcome. |
| sparse / dense reward | Signal frequency classification, not quality evidence. |
| shaping reward | Auxiliary behavioral signal requiring anti-exploit review. |
| auxiliary objective | Additional future target, distinct from evaluation evidence. |
| constraint / penalty | Future rule or negative component; neither is selected now. |
| illegal-action penalty | Candidate treatment requiring legality and failure-policy review. |
| abort / invalid treatment | Explicit eligibility and accounting rule for failed episodes. |
| return | Future aggregation of rewards under a declared specification. |
| undiscounted / discounted return | Aggregation without/with a declared discount rule. |
| discount factor | Future versioned parameter; no value is approved now. |
| scale / weight | Future component magnitude/combination parameters. |
| normalization / clipping / saturation | Future transformations requiring explicit versioning. |
| credit assignment | Future attribution of delayed outcomes to actions/participants. |
| policy objective / value target / advantage / baseline | Future algorithm-facing quantities, all unapproved. |
| entropy regularization | Future policy-distribution term; no coefficient is approved. |
| KL penalty / trust-region control | Future update-control term; no method/value is approved. |
| evaluation metric | Independently approved measure of behavior/performance. |
| training metric | Run diagnostic that cannot substitute for evaluation. |
| model-strength evidence | Evidence produced only by an approved evaluation chain. |
| reward version / manifest | Immutable future identity and provenance for one specification. |
| non-evidence warning | Required warning preventing optimization results from overclaim. |

Vocabulary definition neither selects an algorithm nor implements a reward.
Objective, reward, loss, evaluation metric and strength evidence are distinct.

## Objective / Reward / Evaluation Separation

The following layers must remain separate:

1. Protocol raw outcome.
2. Training reward.
3. Optimization objective or loss.
4. Training diagnostic.
5. Offline evaluation metric.
6. Model-strength evidence.
7. Tenhou, stable-dan, LuckyJ or promotion evidence.

Raw outcome does not automatically become reward; reward does not
automatically become loss. High return, low training loss or self-play win
rate does not automatically show a strong policy. Stable dan `> 10.68` is a
long-term evaluation target, not an automatic reward definition. LuckyJ
comparison cannot be encoded as an unreviewed reward. Optimization metrics
cannot impersonate evaluation metrics, and evaluation metrics cannot
impersonate ranked evidence.

## Candidate Objective / Reward Families

| candidate_family | intended purpose | potential benefits | major risks | required prerequisites | approved_now | selected_now | implementation_allowed_now | cannot_support | notes |
|---|---|---|---|---|---:|---:|---:|---|---|
| terminal raw-outcome mapping | map a valid terminal result to a future signal | simple/auditable | sparse credit, mapping bias | reviewed outcome schema | no | no | no | strength claims | no formula/sign/scale selected |
| placement/rank terminal signal | align with final placement | closer to rank goal | ignores score context, high variance | seat/opponent controls | no | no | no | stable-dan proof | no values selected |
| score/point-delta terminal signal | preserve score movement | denser terminal distinction | score-vs-placement mismatch | ruleset/outcome review | no | no | no | Tenhou proof | unit and scale unselected |
| legality/protocol constraint or penalty | discourage invalid behavior | protects protocol integrity | exploit/abort incentives | legality/failure policy | no | no | no | policy quality | penalty treatment unselected |
| dense shaping signal | improve future learning signal density | potential credit support | reward hacking/domination | anti-hacking review | no | no | no | strength claims | separate review required |
| risk/variance-aware candidate objective | account for downside/variance | may support fourth-place control | distorted incentives | risk metric boundary | no | no | no | promotion | no risk functional selected |
| auxiliary predictive objective | improve representation/task signal | possible sample efficiency | proxy overfit/leakage | feature/label approval | no | no | no | policy strength | no target/loss selected |
| multi-component weighted objective | combine candidate concerns | decomposable tradeoffs | hidden weights/scale drift | component/version review | no | no | no | LuckyJ comparison | no weights selected |
| evaluation-only metric family | measure future behavior | independent diagnostics | accidental reward reuse | evaluation protocol | no | no | no | training approval | must not become reward automatically |

No family, formula, sign, scale, discount, weight or clipping threshold is
selected. Shaping requires a separate anti-reward-hacking review.

## Reward Signal Source and Timing Boundary

Every future component must record its source field/event, per-step or
terminal timing, computation time, recipient participant/role, public/private/
post-episode classification, environment/outcome derivation, version,
provenance and deterministic-computation expectation.

A terminal outcome may be used for post-episode reward computation only after
separate approval. Terminal/post-outcome information must never enter the
decision-time observation. Reward computation must not create hidden/future
information leakage. This task implements no calculator and reads no real
data.

## Invalid / Aborted / Retried Episode Boundary

A future specification must explicitly classify normal terminal, invalid
action, participant/environment error, timeout, resource failure, protocol or
artifact mismatch, aborted/retried/duplicate episode and incomplete
provenance.

- Invalid/aborted episodes cannot be silently deleted or excluded by keeping
  only successful episodes.
- Retry lineage and original/retry seeds must be auditable.
- Whether retry replaces or supplements the original must be explicit.
- Reward eligibility and evidence eligibility are separate fields.
- No failure penalty or retry/reward behavior is selected or implemented now.

## Seat / Role / Opponent Bias Boundary

Future reviews must account for seat/role and starting asymmetry, participant
ordering, opponent and policy-version distributions, retry selection,
invalid/aborted denominators, self-copy limitations and non-stationary
opponents.

Reward must not implicitly reward favorable seats. Comparisons must preserve
seat/role context. Opponent-pool composition cannot be hidden, and self-copy
play does not prove generalization. This task defines no opponent pool and
approves no league.

## Reward-Hacking / Objective-Mismatch Boundary

Future reviews must cover terminal-state, episode-length, stalling,
forced-abort, retry, illegal-action and fallback exploitation; score/placement
mismatch; local/long-term mismatch; shaping domination; clipping/saturation
distortion; scale instability; opponent collusion/cycling; mode collapse;
environment-bug exploitation; evidence cherry-picking; and training-metric
overclaim.

Each future component must record intended behavior, known failure modes,
anti-exploit invariants, monitoring signals, stop triggers, rollback/disable
path and evidence limitations. This task implements no mitigation.

## Reward Scaling / Weighting / Normalization Boundary

A future specification must record component weight, sign, scale, unit,
aggregation, normalization basis, clipping and saturation, discounting,
episode-length treatment, seat/participant normalization, missing/invalid
behavior and version.

No number, discount factor, clipping rule or normalization rule is selected.
Scale/weight changes create a new specification version and cannot be silent.
Multi-component rewards must remain decomposable and aggregate return must be
traceable to components.

## Credit Assignment Boundary

Future planning must address per-step versus terminal credit, delayed/sparse
outcomes, dense shaping, participant/team attribution if later applicable,
multi-agent effects, action-to-outcome ambiguity and invalid/aborted episode
attribution.

No credit-assignment algorithm, advantage estimator, value target, return
calculation or policy/value loss is selected or implemented.

## Algorithm / Loss Independence Boundary

Reward specification is not PPO, DQN, A2C, MCTS, policy gradient or another
algorithm selection. This boundary approves no policy gradient, value
function, entropy/KL coefficient, optimizer or trainer. Algorithm choice
requires a separate docs-only boundary and approval chain. No executable loss
is produced.

## Training vs Evaluation Separation

Training reward cannot substitute for evaluation metrics, and evaluation
metrics cannot be reduced to training reward. Training episodes cannot
automatically become holdout evaluation. Evaluation participants, versions
and freezing require separate approval. Reward tuning against holdout evidence
must be declared, and reward selection/final evaluation must avoid leakage.
No training or evaluation is approved.

## Model-Strength Evidence Boundary

No current artifact is model-strength evidence. Future strength evidence
requires an approved evaluation protocol and model-output path, sample
definition, sufficient sample size, uncertainty method, leakage controls,
opponent/seat/version accounting, governance review and separate approval.

High reward is not high strength; high return is not Tenhou rank; training
improvement is not stable-dan improvement; self-play dominance is not LuckyJ
comparison; and unit tests, synthetic smoke or reward definitions are not
model-strength evidence.

## Tenhou / Stable-Dan / LuckyJ / Promotion Boundary

No current artifact is Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68`
comparison or promotion evidence. Future evidence requires approved source and
protocol, participant identity, sample definition, uncertainty, leakage
review, seat/opponent accounting, governance approval and rollback. The
long-term target is not reward approval.

## Source / Real-Data Boundary

This boundary approves no source or ingestion and uses no real Tenhou, real
haifu, external logs, platform data or account/session/cookie/token material.
Future real-data reward analysis requires separate rights/privacy/platform/
approval/ingestion gates. Future self-play data requires a separate
provenance/data boundary. No self-play or reward data is created now.

## Model-Output / Environment Dependency Boundary

No model-output integration or P8 execution environment/simulator is
approved. Future reward execution requires reviewed environment/simulator and
state-transition authority, protocol manifest, model-output interface,
action-legality path, termination handling and reward specification, followed
by an exact approval decision and exact `10_NEXT` task.

This task assumes no concrete environment API and creates no runner.

## Candidate Reward Specification Record

Candidate future fields are:

```text
objective_id
objective_version
reward_spec_id
reward_spec_version
component_id
component_name
component_type
source_event
timing
recipient_role
sign
scale
weight
aggregation_rule
normalization_rule
clipping_rule
discounting_status
invalid_episode_rule
abort_rule
retry_rule
seat_normalization_rule
opponent_context_required
observation_leakage_forbidden
intended_behavior
known_failure_modes
anti_exploit_invariants
monitoring_signals
stop_triggers
provenance_version
training_status
evaluation_status
model_strength_status
explicit_non_evidence_warning
```

These are candidate fields only. They are not an approved schema and do not
approve a JSON fixture, parser/reader, reward implementation or training
configuration. No schema, code, fixture or data is created.

## Evidence Boundary

Current evidence grade:

```text
P8 RL objective / reward specification boundary definition evidence only.
```

It supports vocabulary, separation-of-concepts, reward-hacking control and
future-review readiness only. It supports no P8 entry/implementation, reward
implementation, RL/self-play/training/evaluation/league/model-output evidence,
strength/Tenhou/stable-dan/LuckyJ/promotion evidence or P9-P12 approval.

## Future Objective / Reward Entry Criteria

- OR-E1. P8 scope review is closed.
- OR-E2. P8 risk/evidence taxonomy review is closed.
- OR-E3. P8 self-play/RL dependency-map review is closed.
- OR-E4. P8 self-play protocol boundary review is closed.
- OR-E5. RL objective/reward boundary is defined and reviewed.
- OR-E6. Environment/simulator boundary is defined and reviewed.
- OR-E7. Raw-outcome schema and provenance boundary are defined and reviewed.
- OR-E8. Reward component source/timing boundary is defined and reviewed.
- OR-E9. Invalid/abort/retry handling is defined and reviewed.
- OR-E10. Seat/opponent/bias controls are defined and reviewed.
- OR-E11. Training/evaluation separation is defined and reviewed.
- OR-E12. Model-output dependency is defined and reviewed.
- OR-E13. Source/real-data status remains separately governed.
- OR-E14. A separate approval decision authorizes an exact future task.
- OR-E15. `docs/10_next/10_NEXT.md` authorizes that exact task.

None of OR-E1 through OR-E15 is implementation approval by itself.

## Stop Conditions

Stop if a future task implies P8 entry/implementation approval, generates an
unapproved implementation prompt, selects final reward/numerical weights or an
RL algorithm prematurely, implements reward/loss, runs self-play/RL/training/
tuning/evaluation/league, calls models/checkpoints, assumes an unapproved
environment, accesses real/external/platform data, approves ingestion, creates
code/tests/fixtures/data, claims return as strength/Tenhou/stable-dan/LuckyJ/
promotion evidence, enters P9-P12, changes `10_NEXT` to implementation without
approval, uses unknown artifacts or calls third-party binaries.

## Candidate Next Directions

| candidate | current_status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this objective/reward boundary. | available | checks completeness and non-approval | low if review-only | none | yes | no | low | low | selected |
| B. Define environment/simulator boundary. | deferred | clarifies transition authority | may imply execution | objective review | yes | no | medium | low | defer |
| C. Define raw-outcome/reward-provenance boundary. | deferred | strengthens traceability | may imply schema approval | objective review | yes | no | medium | low | defer |
| D. Define model-output interface dependency. | deferred | clarifies policy calls | may imply model loading | environment review | yes | no | medium | low | defer |
| E. Define training/evaluation dependency boundary. | deferred | separates run purposes | broad scope | objective/environment reviews | yes | no | medium | low | defer |
| F. Define RL algorithm-selection boundary. | deferred | later controls algorithm choice | premature algorithm focus | objective/environment reviews | yes | no | medium | low | defer |
| G. Prepare P8 entry approval decision. | rejected now | could advance stage | criteria incomplete | OR-E5-OR-E15 | yes | no | high | medium | reject |
| H. Draft P8 implementation proposal. | forbidden | none now | premature implementation | entry/exact approval | no | no | high | high | forbid |
| I. Start reward implementation. | forbidden | none now | no approved spec | review/approval | no | no | high | high | forbid |
| J. Start self-play/RL. | forbidden | none now | no execution approval | multiple gates | no | no | high | high | forbid |
| K. Start training/tuning. | forbidden | none now | no run approval | training gates | no | no | high | high | forbid |
| L. Start evaluation/league. | forbidden | none now | evaluation/P10 jump | later protocols | no | no | high | high | forbid |
| M. Start real-data/Tenhou work. | forbidden | none now | rights/platform risk | source review | no | no | high | high | forbid |
| N. Integrate model output or evaluate strength. | forbidden | none now | interface/evidence overclaim | model/evaluation approvals | no | no | high | high | forbid |
| O. Enter P9-P12. | forbidden | none now | stage jump | separate stage reviews | no | no | high | high | forbid |

Selected next direction:

```text
Review P8 RL objective / reward specification boundary before any implementation.
```

## Planning Decision

```text
P8 RL objective / reward specification boundary is defined before any implementation.
```

This task approves no P8 entry/implementation/prompt, reward/objective/loss
implementation, RL algorithm selection for execution, self-play/RL/training/
tuning/evaluation/league, source/real-data/model-output work, strength claim,
promotion or P9-P12 entry. The next safe task is a docs-only review.

## Evidence Grade

```text
P8 RL objective / reward specification boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not entry/implementation approval, an implementation prompt
or executable task, reward/objective/loss implementation, RL algorithm
selection, self-play/RL/training/tuning/evaluation/league, source approval/
ingestion, real Tenhou/haifu/external/platform data, model-output integration,
strength/Tenhou/stable-dan/LuckyJ/promotion evidence or P9-P12 approval.

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
