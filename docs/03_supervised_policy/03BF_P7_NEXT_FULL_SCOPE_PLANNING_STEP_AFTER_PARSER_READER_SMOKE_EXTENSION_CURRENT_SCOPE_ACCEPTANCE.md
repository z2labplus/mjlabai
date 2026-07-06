# 03BF_P7_NEXT_FULL_SCOPE_PLANNING_STEP_AFTER_PARSER_READER_SMOKE_EXTENSION_CURRENT_SCOPE_ACCEPTANCE

## Scope

This document defines the next P7 full-scope planning step after `03BE`
accepted the exact P7 minimal synthetic/local parser-reader smoke extension
implementation as current-scope complete.

This task is docs-only next-task definition. It is not:

- implementation.
- production code.
- tests.
- fixtures.
- data files.
- full P7 closure.
- broader P7 implementation approval.
- source approval.
- source ingestion.
- parser / reader / ingestion approval.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- training-data approval.
- training-run approval.
- training.
- model architecture / trainer implementation.
- evaluation implementation.
- model-output integration.
- model-strength evidence.
- real data approval.
- self-play.
- league.
- P8-P12 entry.

North-star relationship: this planning step supports the long-term Tenhou
stable-dan `> 10.68` target only by preventing P7 from drifting into endless
small smoke tasks or premature implementation. It is not model-strength
evidence, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ
`10.68` comparison or candidate-promotion evidence.

## Current Accepted P7 Current Scope

The accepted P7 current-scope items are:

- docs-only supervised-learning readiness / boundary / proposal / review /
  approval / acceptance chain.
- exact minimal synthetic/local supervised feature-label smoke implementation
  accepted in `03Q`.
- exact broader P7 minimal synthetic/local parser-reader smoke implementation
  accepted as current-scope complete after `03AV`.
- exact P7 minimal synthetic/local parser-reader smoke extension
  implementation accepted in `03BE`.
- direct docs / governance synchronization for those exact scopes.

The current accepted implementation surface is synthetic/local only:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

This accepted scope does not approve real data, source approval, source
ingestion, broad parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, training,
evaluation, model-output integration, self-play, league or P8-P12.

## Current Full P7 Open Scope

Full P7 remains open. The following ranges are not complete and remain
unapproved:

- source approval.
- source ingestion.
- broad parser / reader / ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split / leakage implementation.
- training-data approval.
- training-run approval.
- training.
- model architecture / trainer implementation.
- dataloader / optimizer / loss implementation.
- checkpoint / weights / snapshot creation.
- evaluation implementation.
- metric implementation.
- evaluation runner.
- benchmark harness.
- model-output integration.
- model-strength evidence.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token handling.
- self-play.
- league.
- P8-P12.

## Why Full P7 Cannot Close Now

Full P7 cannot close now because the accepted artifacts are current-scope
synthetic/local smoke artifacts and docs/governance artifacts. They do not
cover source approval, real-data legality, broad ingestion, feature extraction,
label generation, dataset construction, split/leakage controls, training-data
approval, model/trainer readiness, evaluation readiness, model-output
integration or model-strength evidence.

Closing full P7 now would incorrectly treat smoke guardrails as full supervised
learning readiness.

## Why P8-P12 Cannot Start Now

P8-P12 require mature upstream supervised/data/evaluation evidence that does
not exist yet. Current P7 evidence does not include approved training data, a
trained supervised model, model outputs, evaluation results, self-play
readiness, league readiness, Tenhou ranked evidence, stable-dan ranked-game
evidence or LuckyJ `10.68` comparison evidence.

P8-P12 entry remains blocked until full P7 closure and a separate transition
review define a later-stage scope, entry criteria, risks and first task.

## Why Immediate Implementation Is Not Selected

Immediate implementation is not selected because `03BE` accepted only one
exact current-scope smoke extension. That acceptance does not identify or
approve the next exact implementation files. It also does not answer whether
full P7 should continue with more synthetic/local smoke implementation,
source-specific planning, feature/label planning, dataset planning or closure
criteria.

The safer next move is to define full P7 closure criteria, so the project can
avoid endless documentation churn and avoid premature implementation.

## Remaining Workstreams

| workstream | status | classification | notes |
|---|---|---|---|
| Source approval / data rights | not approved | required before real/source work | Must define source-specific approvals before ingestion or training data use. |
| Source ingestion | not approved | required before real/source readers | No broad file ingestion, arbitrary paths or platform data are approved. |
| Broad parser / reader / ingestion | not approved | required before source-backed feature work | Current parser-reader smoke is not broad ingestion. |
| Actual feature extraction | not approved | required before training data | Current smoke emits no feature tensors or examples. |
| Actual label generation | not approved | required before training data | Current smoke labels are placeholders / schema guardrails only. |
| Supervised dataset construction | not approved | required before training | No dataset records, manifests or splits are approved. |
| Split / leakage implementation | not approved | required before training-data approval | Hidden/future information controls must precede training. |
| Training-data approval | not approved | required before training run | Must remain separate from dataset construction. |
| Training-run approval | not approved | required before training | No trainer commands or artifact creation are approved. |
| Model architecture / trainer | not approved | required before supervised training | No dataloader, optimizer, loss or checkpoint code is approved. |
| Evaluation implementation | not approved | required before model-strength claims | P5 patterns may inform future docs only. |
| Model-output integration | blocked | blocked until model/trainer/evaluation prerequisites | No model outputs exist or are approved. |
| Real Tenhou / real haifu / external logs / platform data | blocked | blocked until source-specific review | No real-data use is approved. |
| Self-play / league / P8-P12 | later-stage / out-of-scope | later-stage only | Requires full P7 closure and separate transition review. |
| Governance / evidence / risk records | active | required | Must stay updated at every gate. |
| Full P7 closure criteria | not defined after `03BE` | required next planning step | Needed to decide how full P7 can eventually close. |

Required near-term workstreams:

- full P7 closure criteria definition.
- full P7 remaining required/deferred/blocked/later-stage classification.
- evidence and risk requirements for any future closure review.

Deferred workstreams:

- source-specific approval process.
- implementation proposal drafting for any further synthetic/local smoke task.
- feature/label, dataset, training and evaluation proposal chains.

Blocked workstreams:

- real Tenhou / real haifu / external logs / platform data.
- model-output integration.
- training and model artifact creation.

Later-stage / out-of-scope workstreams:

- self-play.
- league.
- P8-P12.
- Tenhou ranked validation.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

## Candidate Next Directions

| candidate | current status | benefits | risks | blocked_by | docs-only | implementation approval | P8-P12 risk | decision |
|---|---|---|---|---|---:|---:|---:|---|
| A. Define full P7 closure criteria after current-scope parser-reader smoke extension acceptance. | available | Prevents endless P7 expansion; defines required/deferred/blocked/later-stage closure conditions; keeps smoke evidence in its lane. | Could be mistaken for closure if wording is weak. | none if explicitly docs-only | yes | no | low | selected |
| B. Define full P7 remaining scope inventory update after parser-reader smoke extension acceptance. | available | Updates inventory after `03BE`; useful if closure criteria need more inventory first. | Duplicates much of `03AW` / `03AX` unless tied to closure criteria. | none | yes | no | low | not selected; closure criteria can include inventory update |
| C. Define P7 source approval / data-readiness decision process. | possible later | Clarifies real/source approvals before ingestion. | May be misread as source approval or real-data permission. | closure criteria not yet updated after `03BE` | yes | no | medium | deferred |
| D. Define next exact minimal synthetic/local implementation proposal. | possible later | Could continue small synthetic/local safety checks. | Encourages endless implementation-proposal loops before full P7 closure criteria are clear. | no post-`03BE` closure criteria | yes | no | medium | deferred |
| E. Prepare post-current-scope transition review. | premature | Could frame later-stage transition. | Might imply full P7 is close or P8-P12 can be considered. | full P7 not closed | yes | no | high | rejected for now |
| F. Attempt immediate implementation. | not allowed | None for this docs-only gate. | Scope drift into code, tests, fixtures, data or real implementation. | no exact approved task | no | yes | high | rejected |
| G. Attempt full P7 closure. | not allowed | None now. | Prematurely closes P7 while major workstreams remain unapproved. | missing full P7 closure criteria and required evidence | no | no | high | rejected |
| H. Attempt P8-P12 entry. | not allowed | None now. | Stage jump into self-play, league, validation or Tenhou claims without supervised/data/eval readiness. | full P7 not closed; no transition review | no | no | high | rejected |

## Recommended Next Task

Recommended next task:

```text
Define full P7 closure criteria after parser-reader smoke extension current-scope acceptance.
```

This next task must be docs-only. It must define full P7 closure criteria,
required evidence, deferred / blocked / later-stage classifications and
non-closure conditions. It must not close full P7, approve implementation,
approve source approval, approve source ingestion, approve broad parser /
reader / ingestion, approve actual feature extraction, approve actual label
generation, approve supervised dataset construction, approve split creation,
approve leakage-test implementation, approve training-data approval, approve
training-run approval, approve training, approve model architecture / trainer,
approve evaluation, approve model-output integration, produce model-strength
evidence, approve real data, approve self-play, approve league or approve
P8-P12.

## Rationale

This is the safest next P7 full-scope planning step because:

- P7 already has multiple accepted current-scope synthetic/local smoke
  artifacts.
- `03AW` and `03AX` already define and review the full-P7 expansion plan.
- `03BE` adds another accepted exact current-scope parser-reader smoke
  extension.
- Continuing directly to more implementation proposals risks indefinite P7
  growth.
- Full P7 closure criteria are needed to define what must be required,
  deferred, blocked or later-stage before any future closure review.
- Current-scope smoke evidence must not be mistaken for full P7 closure.
- Source approval, real data, training, evaluation, self-play, league and
  P8-P12 must remain unapproved unless later gates explicitly approve them.

## Rejected Candidates

Immediate implementation is rejected because no exact next implementation
scope is approved, and this task is docs-only.

Full P7 closure is rejected because source approval, ingestion, feature
extraction, label generation, dataset construction, split/leakage controls,
training-data approval, training-run approval, model/trainer work, evaluation
and model-output integration remain unapproved.

P8-P12 entry is rejected because full P7 is not closed, no trained supervised
model exists, no model-strength evidence exists and no transition review has
approved later-stage work.

Source approval and real-data work are deferred because source-specific rights,
allowed-use, storage, privacy/compliance and ingestion boundaries must be
defined separately before any real/source data is used.

Training and evaluation work are rejected because no supervised dataset,
training-data approval, training-run approval, model/trainer approval,
model-output integration or evaluation implementation approval exists.

## Planning Decision

```text
The next P7 full-scope planning step is to define full P7 closure criteria
after parser-reader smoke extension current-scope acceptance.
```

This decision is docs-only and does not approve full P7 closure, broader P7
implementation, source approval, source ingestion, broad parser / reader /
ingestion, actual feature extraction, actual label generation, supervised
dataset construction, split creation, leakage-test implementation,
training-data approval, training-run approval, training, model architecture /
trainer implementation, evaluation implementation, model-output integration,
model-strength evidence, real data, self-play, league or P8-P12 entry.

## First Task Candidate

If no blocker is found, the new first unchecked task in `10_NEXT` should be:

```text
Define full P7 closure criteria after parser-reader smoke extension current-scope acceptance.
```

The task must explicitly remain:

- docs-only criteria definition.
- not full P7 closure.
- not implementation.
- not source approval.
- not source ingestion.
- not broad parser / reader / ingestion.
- not feature extraction.
- not label generation.
- not dataset construction.
- not training.
- not evaluation.
- not model-output integration.
- not model-strength evidence.
- not real data approval.
- not self-play.
- not league.
- not P8-P12.

## Evidence Grade

```text
P7 next full-scope planning step definition evidence only.
```

## Explicit Non-Evidence

This next-step definition is not:

- full P7 closure.
- broader P7 implementation approval.
- source approval.
- source ingestion.
- broad parser / reader / ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- training-data approval.
- training-run approval.
- training.
- model architecture.
- trainer.
- evaluation implementation.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- real data.
- self-play.
- league.
- P8-P12 entry approval.
