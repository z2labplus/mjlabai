# 03M Minimal P7 Synthetic/Local Supervised Fixture And Feature-Label Smoke Proposal Before Implementation

## Scope

This document defines a docs-only proposal for a future minimal P7
synthetic/local supervised fixture and feature-label smoke path before any
implementation.

This is P7 supervised-learning planning only. It does not create a fixture,
test, production module, data file, parser, dataset reader, ingestion path,
feature extractor, label generator, training dataset, trainer, model-output
path, CLI or model artifact.

North-star relationship: this proposal supports the long-term Tenhou stable
dan `> 10.68` goal only indirectly by making future supervised-learning inputs
auditable before implementation. It is not model-strength evidence, Tenhou
ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
candidate-promotion evidence.

## Proposal Purpose

The purpose is to define the smallest future synthetic/local supervised smoke
path that could be reviewed before code. The proposal creates a narrow target
for later approval without approving that later work.

The proposal answers these planning questions:

- What future implementation class is being considered.
- Which exact future files may be considered.
- Which fixture source boundary must hold.
- Which feature and label smoke checks may be considered.
- Which validation commands would be required later.
- Which approval conditions must pass before implementation.
- Which stop conditions must halt the future task.
- Which risks must remain visible before code.

## Minimal Future Implementation Candidate

Future implementation, if separately approved, may be limited to these
candidate classes only:

| Candidate class | Future purpose | Current status |
|---|---|---|
| Synthetic/local supervised fixture | Represent a tiny project-authored supervised smoke sample. | Proposed only; not created. |
| Feature / label schema helper | Define JSON-safe feature and label smoke object boundaries. | Proposed only; not created. |
| Fixture schema smoke test | Validate synthetic fixture shape and guardrails. | Proposed only; not created. |
| Feature / label boundary smoke test | Validate future feature / label shape without extraction or generation. | Proposed only; not created. |
| Direct docs / governance sync | Record evidence grade, risks and next task. | Required for any future approved implementation. |

The future task must remain standard-library-only unless a later approval
explicitly says otherwise.

## Candidate Exact Files

These are candidate future file paths only. They are not approved for creation
by this document, and they are not created in this task.

| Candidate path | Purpose | Current status | Future approval requirement |
|---|---|---|---|
| `src/mjlabai/supervised/feature_label_schema.py` | Minimal feature / label schema and validation helper, if approved. | Not created. | Must be explicitly approved by a later `10_NEXT` first task. |
| `tests/fixtures/supervised/synthetic_supervised_smoke.json` | Project-authored synthetic/local supervised smoke fixture, if approved. | Not created. | Must be explicitly approved by a later `10_NEXT` first task. |
| `tests/supervised/test_feature_label_schema.py` | Unit tests for the minimal feature / label schema, if approved. | Not created. | Must be explicitly approved by a later `10_NEXT` first task. |
| `tests/supervised/test_synthetic_supervised_fixture_schema.py` | Fixture schema smoke test, if approved. | Not created. | Must be explicitly approved by a later `10_NEXT` first task. |

Any additional file, directory, module, fixture or test requires a separate
approval decision before implementation.

## Candidate Synthetic / Local Fixture Boundary

The future fixture may be approved only if it remains:

- project-authored synthetic/local data.
- tiny and deterministic.
- repo-local.
- explicitly marked as not Tenhou data.
- explicitly marked as not real haifu.
- explicitly marked as not external logs.
- explicitly marked as not platform data.
- explicitly marked as not model output.
- explicitly marked as not human-labeled real play.
- explicitly marked as not self-play or league output.
- explicitly marked as not model-strength evidence.
- explicitly marked as not LuckyJ `10.68` comparison.
- explicit about provenance and warnings.
- aligned with `03G`, `03H`, `03I`, `03J`, `03K` and `03L`.

Forbidden fixture inputs:

- real Tenhou logs.
- real haifu.
- external logs.
- platform data.
- online accounts, sessions, cookies or tokens.
- scraped data.
- third-party binary output.
- Akochan `system.exe` output.
- `libai.so` output.
- unknown `*.pth`, `*.pt`, checkpoint or snapshot output.
- model outputs.
- self-play outputs.
- league outputs.
- unapproved human labels.
- generated labels from an unapproved label generator.

The future fixture must not be used as a training dataset. It may only be a
smoke artifact for shape, leakage and guardrail checks.

## Candidate Feature / Label Smoke Boundary

The future feature / label smoke checks may validate only:

- field names.
- JSON-serializable primitive values.
- explicit schema version.
- public-information-only placeholders.
- explicit absence of hidden information.
- explicit absence of future information.
- source/provenance fields.
- warnings and non-evidence text.
- compatibility with the candidate synthetic fixture shape.

They must not:

- extract features from replay records.
- generate labels.
- parse real or synthetic replay logs.
- implement a dataset reader.
- implement ingestion.
- construct a supervised dataset.
- approve a feature schema for training.
- approve a label schema for training.
- run model code.
- evaluate policy quality.
- compute supervised accuracy.
- train, tune or checkpoint a model.
- connect model outputs.
- use real Tenhou, real haifu, external logs or platform data.

The future smoke path may check that a feature/label object is shaped safely.
It must not claim that the feature or label is strategically correct.

## Candidate Validation Commands

If a later task explicitly approves implementation of the exact candidate
files, its minimum validation should include:

```bash
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

The current docs-only proposal task validates only:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Future Implementation Approval Conditions

A future implementation task must not start unless all conditions below pass:

- A proposal review task closes with no blocker.
- `docs/10_next/10_NEXT.md` explicitly names the exact implementation task as
  the first unchecked item.
- The exact candidate files are approved.
- Additional files are either absent or separately approved.
- The task remains synthetic/local only.
- No source approval, source ingestion, parser, reader, ingestion, feature
  extraction, label generation or training is introduced.
- No real Tenhou, real haifu, external logs, platform data, accounts, sessions,
  cookies or tokens are read.
- No third-party binaries, weights, params or artifacts are used or stored.
- No model-output integration is introduced.
- No CLI or broad file ingestion is introduced.
- The evidence grade and non-evidence warnings are preserved.
- Validation commands are explicit.
- Rollback and stop conditions are explicit.
- Governance documents are updated.
- Web ChatGPT review or equivalent human approval confirms the boundary.

## Stop Conditions

Stop before commit if any of these appear:

- production behavior beyond the approved candidate files.
- any unapproved fixture, test, module or data file.
- real Tenhou, real haifu, external logs or platform data.
- account, session, cookie or token handling.
- parser, reader, ingestion or broad file ingestion behavior.
- feature extraction or label generation behavior.
- supervised dataset construction.
- model-output integration.
- CLI.
- training, tuning, checkpointing or model-artifact work.
- self-play, league or runner behavior.
- third-party binary, source, params, weights or build artifact usage.
- evidence overclaiming.
- P8-P12 drift.
- validation failure.

## Proposal Risks

| Risk | Category | Severity | Mitigation |
|---|---|---|---|
| Proposal is mistaken for implementation approval. | Governance / Scope | High | This document states that no fixture, tests, code or data files are created or approved. |
| Candidate files are mistaken as already created. | Governance / Scope | Medium-High | Candidate paths are labeled proposed only and require future `10_NEXT` approval. |
| Synthetic fixture is mistaken for a training dataset. | Data / Governance | High | The fixture boundary says smoke artifact only, not training data. |
| Feature/label smoke is mistaken for extraction or generation. | Leakage / Governance | High | Smoke checks may validate shape only and must not extract or generate. |
| Real data enters through convenience examples. | Compliance / Data | High | Real Tenhou, real haifu, external logs and platform data are forbidden. |
| Parser/reader/ingestion creeps into a fixture task. | Governance / Scope | High | Parser, reader and ingestion remain separate unapproved tasks. |
| Training starts before source and label approval. | Governance / ML | High | Training, tuning, dataloaders, checkpoints and model artifacts remain forbidden. |
| Smoke evidence is overclaimed as strength evidence. | Evaluation / Governance | High | Evidence grade is proposal evidence only with explicit non-evidence warnings. |
| P8/P10/P12 work is treated as implicitly approved. | Stage Control | High | Later stages require separate transition reviews and approvals. |
| Extra files expand scope silently. | Engineering / Scope | Medium-High | Any additional file requires separate approval before implementation. |

## Planning Decision

```text
A minimal P7 synthetic/local supervised fixture and feature-label smoke proposal is defined before implementation. This does not approve P7 implementation, fixture creation, tests, production code, data files, feature extraction, label generation, parser, dataset reader, ingestion, training, model-output integration, real data, self-play, league or P8-P12 entry.
```

## Next Task Recommendation

```text
Review minimal P7 synthetic/local supervised fixture and feature-label smoke proposal before implementation.
```

The next task must be a docs-only review gate. It must not approve or execute
implementation unless a later task separately records that decision.

## Follow-Up Status

`docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md`
now reviews this proposal and records `Review can close` with no blocker. The
follow-up approval decision is now recorded in
`docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
with decision `Approved for next minimal implementation task.` That decision
only permits the next exact minimal synthetic/local smoke implementation task.
It must not expand into parser / dataset reader / ingestion, actual feature
extraction, actual label generation, training, model-output integration, real
data or P8-P12 work.

The exact minimal implementation has now been reviewed in
`docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`,
which records `Review can close`. That review is limited to the exact files
approved by `03O`; it does not approve broad P7 implementation, source
ingestion, parser / reader / ingestion, actual feature extraction, actual
label generation, training, real data, model-output integration or P8-P12
entry.

## Evidence Grade

```text
P7 minimal synthetic/local supervised fixture and feature-label smoke proposal evidence only.
```

## Explicit Non-Evidence

This proposal is not:

- P7 implementation.
- P7 first-task execution.
- fixture creation.
- test creation.
- production code.
- data-file creation.
- source approval.
- training-data approval.
- parser.
- dataset reader.
- ingestion.
- feature extraction.
- label generation.
- supervised dataset construction.
- model-output integration.
- CLI.
- broad file ingestion.
- training.
- tuning.
- checkpointing.
- model-artifact evidence.
- self-play.
- league.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
- P8-P12 entry approval.
