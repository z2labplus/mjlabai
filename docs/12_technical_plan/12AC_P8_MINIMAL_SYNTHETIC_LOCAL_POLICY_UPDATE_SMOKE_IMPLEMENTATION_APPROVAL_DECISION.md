# 12AC_P8_MINIMAL_SYNTHETIC_LOCAL_POLICY_UPDATE_SMOKE_IMPLEMENTATION_APPROVAL_DECISION

## Scope

This document records the exact approval decision for the first executable P8
synthetic/local policy-update smoke after the reviewed `12AA`/`12AB`
provenance-manifest boundary pair.

This task is an approval decision only. It does not add code, tests, fixtures,
data, a model, an artifact, an environment, self-play, training or evaluation.

North-star relationship: the approved future smoke is the smallest executable
check that a deterministic learning update can be represented, validated and
tested in this repository. It is not evidence that the update improves
mahjong play or can exceed LuckyJ or stable dan `10.68`.

## Reviewed Basis

- The user explicitly instructed Codex to continue after `12AB` reported that
  one exact approval gate remained before code. This records the human
  planning-to-implementation transition authorization required by P8-E15.
- `12I`/`12J` define and review P8 scope and entry criteria.
- `12K` through `12Z` define and review P8 risk, dependency, protocol, reward,
  environment, outcome, model-output and model-use boundaries.
- `12AA`/`12AB` define and review artifact/provenance boundaries.
- `12AB` found no genuine blocker and prohibited another sibling boundary.
- Existing repository packages use Python `>=3.9` and standard-library unit
  tests; no ML framework is currently required for this smoke.

## Decision Options

| option | meaning | selected |
|---|---|---:|
| Approved for next exact minimal implementation task. | The next `10_NEXT` task may create only the files and behavior named here. | yes |
| Deferred pending a genuine blocker. | Code remains closed and the blocker must be recorded. | no |
| Rejected. | The candidate is unsuitable for P8. | no |

## Decision

```text
Approved for next exact minimal implementation task.
```

This approval is limited to one synthetic/local numerical update smoke. It is
not broad P8 entry, production RL, self-play, model training, evaluation,
artifact/model use, real-data approval, strength evidence or P9-P12 approval.

## Exact Approved Future Task

```text
Implement exact minimal P8 synthetic/local policy-update smoke only.
```

The implementation must perform exactly one deterministic tabular action-
value temporal-difference update for one already-loaded project-authored
synthetic/local record.

## Exact Approved Future Files

The future implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_update_smoke.py`
- `tests/rl/test_synthetic_policy_update_smoke.py`
- direct docs/governance files required to record the implementation,
  validation, risks and next task.

No fixture or data file is approved. No other source or test file is approved.

## Exact Approved API Boundary

The implementation may expose only the equivalent of:

```text
SYNTHETIC_POLICY_UPDATE_SMOKE_VERSION
SYNTHETIC_LOCAL_SOURCE_KIND
SyntheticPolicyUpdateSmokeError
SyntheticPolicyUpdateInput       # frozen dataclass
SyntheticPolicyUpdateResult      # frozen dataclass
apply_synthetic_policy_update_smoke(input_record, *, learning_rate, discount_factor)
```

Names may receive a minor style adjustment only if all behavior and file scope
remain exact. No batch API, path API, CLI or persistence API is approved.

## Exact Input Boundary

`SyntheticPolicyUpdateInput` must contain only:

```text
record_id: non-empty ASCII identifier token
source_kind: exactly project_authored_synthetic_local
state_id: non-empty ASCII synthetic identifier token
action_id: non-empty ASCII synthetic identifier token
current_action_value: finite number
reward: finite number
next_max_action_value: finite number for non-terminal, None for terminal
terminal: bool
project_authored: exactly true
synthetic: exactly true
local_only: exactly true
uses_real_data: exactly false
uses_external_log: exactly false
uses_platform_data: exactly false
uses_model_output: exactly false
uses_self_play: exactly false
```

Function parameters must satisfy:

```text
0 < learning_rate <= 1
0 <= discount_factor <= 1
both finite real numbers, excluding bool
```

No field may carry a path, raw log, observation tensor, hidden information,
model output, artifact bytes, checkpoint or external source reference.
Identifier tokens may contain only ASCII letters, digits, `_`, `-`, `.`, and
`:`; they must reject `/`, `\\`, `.` and `..` as complete values.

## Exact Update Semantics

For a terminal record:

```text
target_value = reward
```

For a non-terminal record:

```text
target_value = reward + discount_factor * next_max_action_value
```

For both:

```text
td_error = target_value - current_action_value
updated_action_value = current_action_value + learning_rate * td_error
```

All derived values must be finite. The input dataclass must not be mutated.
The same input and parameters must produce exactly equal result objects.

This equation is selected only as a tabular numerical smoke. It does not
select Q-learning, TD learning or any other algorithm as the project mainline.
It does not define a policy distribution, choose an action, run an episode or
optimize a model.

## Exact Output Boundary

The frozen result may contain only:

```text
smoke_version
record_id
source_kind
state_id
action_id
terminal
learning_rate
discount_factor
current_action_value
reward
next_max_action_value
target_value
td_error
updated_action_value
update_applied = true
evidence_grade = P8 synthetic/local numerical policy-update smoke evidence only
warnings
safety flags copied or summarized as all-safe
```

Warnings must state at least:

- synthetic/local only.
- not real Tenhou or haifu data.
- not self-play.
- not production training.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

The result must not contain a model, policy distribution, selected action,
checkpoint, artifact, dataset, evaluation metric, ranked result or strength
claim.

## Exact Validation Requirements

The future test module must cover:

1. terminal update formula.
2. non-terminal update formula.
3. deterministic repeated output and input immutability.
4. invalid learning rate and discount factor rejection.
5. NaN/infinity and bool-as-number rejection.
6. terminal/non-terminal `next_max_action_value` consistency.
7. rejection of any false synthetic/local provenance guardrail.
8. identifier token and path-like identifier rejection.
9. warnings, evidence grade and safe output boundary.
10. import through `mjlabai.rl` if the package exports the API.

Future validation commands:

```text
python3 -m unittest tests/rl/test_synthetic_policy_update_smoke.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
git diff --check
```

The current approval task must not create or run the future RL test.

Current approval-decision validation:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

`git diff --check` passed. The six existing unittest commands ran 46 tests
with all tests passing. No future RL test, training, inference, artifact or
data command was run.

## Explicitly Forbidden Future Scope

The approval does not permit:

- batch/episode/environment/simulator/runner or self-play behavior.
- action selection, policy inference, model-output integration or legal-action
  checking.
- model architecture, neural network, optimizer, autograd, gradient, tensor,
  checkpoint, weight, snapshot or persisted artifact.
- training loop, tuning, evaluation, benchmark, league or candidate promotion.
- fixture/data creation, source ingestion, path/file/URL input or CLI.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- third-party binaries/services, GPU/distributed execution or new dependency.
- P9-P12 work or model-strength/Tenhou/stable-dan/LuckyJ claims.

## Rollback Plan

If the future implementation violates this approval or fails validation:

- stop before push if possible.
- remove only the three exact implementation/test files added by that task.
- do not modify or revert unrelated user work.
- record the exact blocker in governance and set `10_NEXT` to an exact fix,
  deferment or closure decision.
- require a new explicit approval before expanding any file or behavior scope.

## Stop Conditions

The future implementation must stop if it needs:

- any source/test file outside the exact approved list.
- a fixture, data file, parser, reader, path, CLI or dependency.
- a model, environment, episode, self-play, training loop or evaluation.
- real/external/platform data or third-party artifacts/services.
- nondeterminism, timing, concurrency, GPU or distributed execution.
- a change to the approved formula, API boundary or evidence classification.
- a model-strength, ranked, stable-dan, LuckyJ or promotion claim.

## Gate Accounting

```text
P8-E15 human transition authorization = satisfied for this exact task
PM-E14 exact approval decision = satisfied by 12AC
P8-E14 exact 10_NEXT authorization = satisfied only when the implementation is first
PM-E15 exact 10_NEXT authorization = satisfied only when the implementation is first
remaining mandatory gate count before exact implementation = 0 after this commit
```

No gate is satisfied for any broader P8 task.

## Evidence Grade

Current approval evidence:

```text
P8 exact minimal synthetic/local policy-update smoke approval-decision evidence only.
```

Future implementation evidence, if validation passes:

```text
P8 synthetic/local numerical policy-update smoke evidence only.
```

Neither grade is model-strength, Tenhou ranked, stable-dan, LuckyJ comparison,
candidate-promotion, production-training or P9-P12 evidence.
