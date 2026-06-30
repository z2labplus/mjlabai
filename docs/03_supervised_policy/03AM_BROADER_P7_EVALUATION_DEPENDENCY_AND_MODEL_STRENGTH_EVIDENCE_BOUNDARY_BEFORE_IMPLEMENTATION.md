# 03AM Broader P7 Evaluation Dependency And Model-Strength Evidence Boundary Before Implementation

## Scope

This document defines the broader P7 evaluation dependency and
model-strength evidence boundary before implementation.

It is docs-only boundary definition evidence. It is not evaluation
implementation, metric implementation, an evaluation runner, benchmark
harness implementation, model-output integration, source approval, source
ingestion, parser / reader / ingestion, actual feature extraction, actual
label generation, supervised dataset construction, split creation,
leakage-test implementation, training-data approval, training-run approval,
training, model architecture approval, trainer approval, checkpoint approval,
weights approval, self-play, league, P8-P12 entry, model-strength evidence,
Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68`
comparison or candidate-promotion evidence.

## Purpose

The north-star target is a Japanese riichi mahjong AI whose long-term Tenhou
stable dan exceeds LuckyJ `10.68`. Future evaluation work can help that target
only if it distinguishes planning, engineering validation and real evidence.

This document defines:

- future broader P7 evaluation dependency boundaries.
- future model-strength evidence acceptance boundaries.
- the difference between engineering validation, training-run evidence,
  offline evaluation evidence, synthetic/local evidence, model-strength
  evidence, Tenhou evidence, stable-dan evidence, LuckyJ comparison and
  candidate-promotion evidence.
- future evaluation dependency prerequisites.
- future evidence-record fields.
- allowed and forbidden future behavior.
- stop conditions.
- risk controls.
- evidence requirements.

It prevents four failure modes:

- treating docs-only boundary work as evaluation implementation approval.
- treating synthetic/local smoke results as model strength.
- treating a training run or checkpoint as evidence of Tenhou performance.
- treating stable-dan or LuckyJ wording as a comparison without approved
  source, protocol, sample size, uncertainty and evidence review.

## Current Evaluation / Evidence Status

Current broader P7 evaluation status:

- No model-strength evidence exists.
- No Tenhou ranked evidence exists.
- No stable-dan ranked-game evidence exists.
- No LuckyJ `10.68` comparison exists.
- No candidate-promotion evidence exists.
- No evaluation implementation is approved.
- No evaluation runner is approved.
- No metric implementation beyond existing P5 synthetic/local diagnostics is
  approved for broader P7.
- No benchmark harness beyond existing P5 synthetic/local diagnostic harness
  is approved for broader P7.
- No model output is approved.
- No trained model is approved.
- No training run is approved.
- No training data is approved.
- No source is approved for broader P7 training or evaluation.
- No real Tenhou, real haifu, external-log or platform-data source is
  approved.

Current synthetic/local smoke tests are engineering validation only. They
validate schemas, guardrails or small project-authored synthetic/local code
paths. They are not model-strength evidence.

P5 evaluation groundwork is useful evaluation infrastructure. It is not
current model-strength evidence. Stable-dan groundwork is not ranked-game
evidence. LuckyJ threshold documentation is not current LuckyJ comparison
evidence.

## Concept Definitions

`engineering validation`:
A local validation that a schema, helper, guardrail or synthetic/local code
path behaves as expected. It is not model strength.

`docs-only review evidence`:
Evidence that governance, boundary or review documents were created and
reviewed. It can guide future work, but cannot prove model strength.

`synthetic/local smoke evidence`:
Evidence from project-authored synthetic/local fixtures or in-memory mappings.
It can validate structure and diagnostic behavior, but cannot represent real
mahjong performance.

`training-run evidence`:
Future evidence that an approved training run executed under approved inputs,
configuration and artifact policy. It can show that training ran, but it is
not model-strength evidence by itself.

`offline evaluation evidence`:
Future evidence from an approved evaluation protocol and approved data source.
It may support model-strength review only if provenance, denominator, sample
size, uncertainty, leakage controls and model-output integration are approved.

`model-output evidence`:
Future evidence derived from approved model outputs. It cannot exist before
model-output integration is approved.

`model-strength evidence`:
Future evidence that an approved model artifact performs well under an
approved evaluation protocol with approved source, sample size, uncertainty,
leakage controls, reproducibility and evidence review.

`Tenhou ranked evidence`:
Future evidence from approved Tenhou ranked-game source and protocol. It
requires platform-policy, rights, privacy, source, ingestion, model-output and
evaluation approvals.

`stable-dan ranked-game evidence`:
Future stable-dan evidence computed from approved ranked-game placement
source with approved formula, room policy, sample-size policy and uncertainty
method.

`LuckyJ comparison evidence`:
Future evidence that compares an approved model against a documented LuckyJ
`10.68` comparator protocol with approved data, uncertainty and review. No
synthetic proxy can satisfy this.

`candidate-promotion evidence`:
Future evidence reviewed for moving a model candidate through the project
funnel. It requires separate promotion criteria and decision review.

`evaluation dependency`:
An upstream item required before evaluation can be meaningful: approved model
artifact, approved model outputs, approved source, approved parser/reader,
approved feature/label/dataset/split artifacts, approved protocol and
approved metric semantics.

`evaluation implementation`:
Future code that computes an evaluation result. It is not approved by this
document.

`evaluation runner`:
Future orchestration around one or more evaluation implementations. It is not
approved by this document.

`metric implementation`:
Future code that computes a metric. It is not approved by this document.

`benchmark harness`:
Future orchestration for repeatable diagnostic or comparison runs. Existing
P5 synthetic/local harness evidence does not approve broader P7 harness work.

`result envelope`:
A structured record for evaluation results, metrics, reproducibility,
warnings and safety flags. A result envelope records evidence; it does not
create model strength by itself.

`evidence grade`:
The allowed interpretation level of an artifact. Lower-grade evidence cannot
substitute for higher-grade evidence.

`promotion gate`:
A future decision point that may promote a model only after approved evidence,
risk review and criteria are satisfied.

`non-evidence warning`:
An explicit warning that an artifact is not model strength, Tenhou evidence,
stable-dan ranked-game evidence, LuckyJ comparison or candidate-promotion
evidence.

These concepts are not interchangeable. A schema smoke test cannot substitute
for a training run. A training run cannot substitute for model-strength
evidence. Offline diagnostics cannot substitute for Tenhou ranked evidence.

## Dependency Map

Future model-strength evidence is downstream of this order:

```text
source approval
-> parser / reader / ingestion approval
-> actual feature extraction approval
-> actual label generation approval
-> supervised dataset construction approval
-> split / leakage approval
-> training-data approval
-> model architecture / trainer approval
-> training-run approval
-> training-run execution
-> model artifact / checkpoint review
-> model-output integration boundary
-> evaluation dependency boundary
-> evaluation implementation proposal
-> evaluation implementation approval
-> offline evaluation execution
-> model-strength evidence review
-> candidate promotion review
-> later-stage P8 / P10 / P12 transition review
```

If any predecessor is missing, the project must not claim model-strength
evidence, Tenhou evidence, stable-dan ranked-game evidence, LuckyJ comparison
or candidate promotion.

## Evaluation Dependency Boundary

Future evaluation dependencies may reference only approved artifacts and
sources:

- approved model artifacts.
- approved model outputs.
- approved data sources.
- approved parser / reader / ingestion outputs.
- approved feature / label outputs.
- approved supervised datasets.
- approved split / leakage controls.
- approved training artifacts.
- approved evaluation protocols.
- approved metric semantics.

A future evaluation dependency record must define:

- evidence grade.
- metric names and definitions.
- forbidden metric interpretations.
- denominators.
- sample size.
- uncertainty or confidence method.
- provenance.
- model-output integration boundary.
- validation commands.
- raw and derived artifact storage policy.
- stop conditions.

Future evaluation dependency work must stop before model-strength claims
unless model-strength evidence criteria are explicitly satisfied and reviewed.

## Model-Strength Evidence Boundary

Future model-strength evidence requires:

- approved model artifact.
- approved model-output collection path.
- approved evaluation protocol.
- approved benchmark or source.
- approved evaluation dataset.
- documented sample size.
- documented denominator.
- uncertainty or confidence method.
- leakage controls.
- selection-bias controls.
- reproducibility metadata.
- evidence grade.
- non-evidence warnings.
- separate evidence review.

Synthetic/local smoke cannot be model-strength evidence. A training run alone
cannot be model-strength evidence. Offline diagnostics alone cannot be Tenhou
ranked evidence.

## Tenhou / Stable-Dan / LuckyJ Evidence Boundary

Future Tenhou ranked evidence requires:

- approved source and source rights.
- platform-policy and privacy review.
- approved parser / reader / ingestion.
- approved model-output integration.
- approved evaluation protocol.
- sample size and uncertainty method.
- anti-leakage and selection-bias controls.
- reproducibility metadata.
- evidence review.

Future stable-dan evidence requires:

- approved placement source.
- room and ruleset policy.
- stable-dan formula protocol.
- fourth-count handling.
- confidence interval or bootstrap method.
- undefined-rate policy for low or invalid denominator.
- no low-sample overclaim.
- evidence grade and review.

Future LuckyJ comparison evidence requires:

- approved comparator definition.
- stable threshold version.
- approved evaluation data.
- confidence lower-bound or uncertainty protocol.
- explicit comparison protocol.
- no synthetic proxy claims.
- separate review.

Future candidate promotion requires:

- approved model-strength evidence.
- risk and regression review.
- promotion criteria.
- no unresolved blockers.
- separate decision record.

## Future Evidence Record Fields

A future evidence record must include at least:

- `evidence_id`
- `evidence_type`
- `model_artifact_id`
- `model_output_source_id`
- `training_run_id`
- `training_data_approval_id`
- `evaluation_protocol_id`
- `evaluation_dataset_id`
- `source_ids`
- source approval references.
- parser / reader / ingestion references.
- feature / label / dataset references.
- split / leakage references.
- model architecture / trainer references.
- model-output integration reference.
- metric names.
- denominators.
- sample size.
- confidence method.
- leakage controls.
- selection controls.
- reproducibility metadata.
- raw artifact storage policy.
- derived artifact storage policy.
- evidence grade.
- allowed interpretation.
- forbidden interpretation.
- warnings.
- evidence log references.
- risk register references.
- decision record references.
- human review or Web ChatGPT review reference.
- explicit first unchecked `docs/10_next/10_NEXT.md` evaluation task
  requirement.

## Candidate Evaluation / Evidence Classes

| Candidate class | Current status | Approved now | Model dependency | Source dependency | Evaluation dependency | Implementation approval required | Allowed for docs planning | Forbidden until | Risk | Notes |
|---|---|---:|---|---|---|---|---:|---|---|---|
| Docs-only evidence envelope draft | Planning only | Yes, docs only | None | None | Boundary docs | No code approval | Yes | Implementation task | Overread as evidence | May define fields only |
| Synthetic/local engineering diagnostic evidence | Existing P5/P7 smoke level | Yes, limited | None or synthetic only | Project-authored synthetic/local | Smoke schema/protocol | Only exact approved tasks | Yes | Strength claim | Overclaim | Not model strength |
| Model-free evaluation protocol validator | Future concept | No | None | Approved synthetic/local only | Protocol schema | Separate approval | Yes | Implementation approval | Scope creep | Could validate structure only |
| Approved-model offline diagnostic evaluation | Future concept | No | Approved model artifact/output | Approved evaluation source | Approved offline protocol | Separate approval | Yes | Model-output integration and eval approval | Premature model claim | Diagnostic unless reviewed |
| Approved-model heldout supervised evaluation | Future concept | No | Approved model and training run | Approved heldout dataset/split | Approved supervised metric protocol | Separate approval | Yes | Dataset/split/leakage approval | Leakage | Not Tenhou evidence |
| Approved-model legal-action diagnostic evaluation | Future concept | No | Approved model output | Approved legal-action source/protocol | Approved legal-action metric | Separate approval | Yes | Model-output integration | Confused with strength | Legality diagnostic only |
| Approved-model stable-dan offline report | Future concept | No | Approved model output if model-derived | Approved placement source | Stable-dan protocol | Separate approval | Yes | Source/protocol/sample review | Low sample overclaim | Not LuckyJ comparison alone |
| Approved-model Tenhou ranked evidence | Future concept | No | Approved deployed model output | Approved Tenhou ranked source | Ranked protocol | Separate approval | No, except boundary docs | Platform/source/model-output approval | Compliance and overclaim | Later-stage evidence only |
| Approved-model LuckyJ comparison evidence | Future concept | No | Approved model evidence | Approved comparator and data | Comparison protocol | Separate approval | No, except boundary docs | Tenhou/stable-dan evidence review | Comparator drift | Needs separate review |
| Candidate promotion evidence review | Future concept | No | Approved candidate model | Approved evidence package | Promotion criteria | Separate decision | No, except boundary docs | Model-strength evidence and risk review | Premature promotion | Funnel gate only |
| Rejected synthetic/local model-strength proxy | Current forbidden class | No | None | Synthetic/local only | Smoke tests | Not allowed | No | Never as strength proxy | False confidence | Must be labeled non-evidence |
| Rejected training-run-as-strength-evidence | Current forbidden class | No | Training run only | Training data | Training logs | Not allowed | No | Separate evaluation evidence | Loss/strength confusion | Training logs are not strength |
| Rejected low-sample LuckyJ comparison | Current forbidden class | No | Any | Low sample | Weak comparison | Not allowed | No | Sample/uncertainty approval | False positive | Do not compare |
| Rejected unapproved real-data evaluation | Current forbidden class | No | Any | Unapproved real data | Any | Not allowed | No | Source and ingestion approval | Compliance breach | Stop condition |
| Rejected model-output evidence before integration approval | Current forbidden class | No | Unapproved output | Any | Any | Not allowed | No | Model-output integration approval | Provenance gap | Stop condition |

## Allowed Future Boundary

Future tasks may be proposed only through a separate first unchecked
`docs/10_next/10_NEXT.md` item and separate review. Allowed planning classes:

- docs-only evaluation dependency record draft.
- docs-only model-strength evidence record draft.
- docs-only evidence envelope schema draft.
- model-free evidence validator proposal.
- synthetic/local engineering diagnostic review.
- approved-model-only evaluation protocol proposal.
- approved-model-only evidence review proposal.

These are allowed only as boundary or proposal work unless a later task
explicitly approves exact implementation files and validation commands.

## Forbidden Evaluation / Evidence Scope

This boundary forbids:

- evaluation implementation.
- metric implementation.
- evaluation runner implementation.
- benchmark harness implementation.
- model-output integration.
- real Tenhou evaluation.
- real haifu evaluation.
- external-log evaluation.
- platform-data evaluation.
- model-strength claims.
- Tenhou ranked claims.
- stable-dan ranked-game claims.
- LuckyJ `10.68` comparison claims.
- candidate-promotion claims.
- using synthetic/local smoke as strength evidence.
- using a training run as strength evidence.
- using low-sample stable-dan output as LuckyJ comparison.
- using unapproved model outputs, sources or parser outputs.
- source approval.
- parser / reader / ingestion approval.
- actual feature extraction approval.
- actual label generation approval.
- supervised dataset construction approval.
- training-data approval.
- training-run approval.
- training.
- self-play.
- league.
- P8-P12 entry.

## Stop Conditions

Stop work and record a blocker if any of these appear:

- unapproved source is introduced.
- unapproved model output is introduced.
- unapproved model artifact is introduced.
- unapproved evaluation data is introduced.
- sample size is too small for the intended claim.
- uncertainty method is missing.
- leakage controls are missing.
- selection-bias controls are missing.
- denominator is ambiguous.
- synthetic/local evidence is treated as model strength.
- training-run evidence is treated as model strength.
- Tenhou evidence is claimed without approved protocol.
- LuckyJ comparison is claimed without approved comparator protocol.
- candidate promotion is proposed without evidence review.
- P8-P12 work enters the task.
- validation fails.
- language overclaims the artifact.

## Risk Controls

| Risk | Control |
|---|---|
| Boundary definition is mistaken for evaluation implementation approval. | Require a later exact implementation task, review and validation command list. |
| Synthetic/local smoke evidence is overclaimed as model strength. | Require non-evidence warnings and evidence grade on every record. |
| Training logs are treated as performance evidence. | Separate training-run evidence from model-strength evidence. |
| Stable-dan point estimate is overclaimed. | Require sample size, denominator and confidence method. |
| LuckyJ comparison is attempted with weak or proxy evidence. | Require approved comparator definition and explicit comparison protocol. |
| Real Tenhou or real haifu enters before approval. | Require source approval, rights review and parser / reader / ingestion approval first. |
| Model output appears before integration approval. | Treat as stop condition until model-output integration is approved. |
| Leakage or selection bias is missed. | Require leakage and selection-control fields in future evidence records. |
| Candidate promotion starts too early. | Require separate model-strength evidence review and decision record. |
| P8-P12 drift occurs. | Keep later stages closed until separate transition review and first-task approval. |

## Evidence Requirements

Future evidence records must be reproducible and auditable. They must record:

- exact model artifact id if any.
- exact model-output source id if any.
- exact source ids and source approvals.
- parser / reader / ingestion approvals.
- feature / label / dataset / split approvals.
- training data approval.
- training run id and approval.
- evaluation protocol id.
- evaluation dataset id.
- metric names and units.
- denominator.
- sample size.
- confidence or uncertainty method.
- leakage and selection controls.
- reproducibility metadata.
- commands or test paths.
- artifact storage policy.
- allowed interpretation.
- forbidden interpretation.
- warnings.
- evidence grade.
- linked risks and decisions.

## First Task Candidate

If no blocker is found, the next task should be:

```text
Review broader P7 evaluation dependency and model-strength evidence boundary before implementation.
```

That next task must be docs-only. It must not implement evaluation, metrics,
runner logic, benchmark harness, model-output integration, source ingestion,
parser / reader / ingestion, actual feature extraction, actual label
generation, supervised dataset construction, training, self-play, league or
P8-P12 work.

## Planning Decision

```text
Broader P7 evaluation dependency and model-strength evidence boundary is defined before implementation. This does not approve evaluation implementation, metric implementation, evaluation runner, model-output integration, model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ 10.68 comparison, candidate promotion, training, source approval, parser, dataset reader, ingestion, actual feature extraction, actual label generation, supervised dataset construction, model architecture, trainer, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 evaluation dependency and model-strength evidence boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- source approval.
- source ingestion approval.
- parser / reader / ingestion approval.
- feature extraction approval.
- label generation approval.
- supervised dataset approval.
- training-data approval.
- training-run approval.
- model architecture approval.
- trainer approval.
- evaluation implementation approval.
- model-output integration approval.
- self-play approval.
- league approval.
- P8-P12 entry approval.
