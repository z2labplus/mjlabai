# 03AC Broader P7 Parser Reader Ingestion Boundary Before Implementation

## Scope

This document defines the broader P7 parser, reader and ingestion boundary
before implementation.

This is a docs-only boundary definition. It is not:

- parser implementation.
- reader implementation.
- ingestion implementation.
- parser / reader / ingestion approval.
- source ingestion approval.
- source approval.
- training-data approval.
- real-data use.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training.
- broader P7 implementation approval.
- P8-P12 entry.

## Purpose

This document exists to make any future broader P7 parser / reader / ingestion
work auditable before implementation.

It defines:

- parser, reader, ingestion and source-ingestion vocabulary.
- the relationship between parser / reader / ingestion, source approval,
  source ingestion approval, feature extraction, label generation and dataset
  construction.
- future approval preconditions.
- future approval-record fields.
- allowed and forbidden future behavior.
- stop conditions.
- evidence requirements and risk controls.

The main guardrail is:

```text
Source readiness and docs context are not parser / reader / ingestion approval.
```

This supports the north-star target indirectly. A future supervised policy may
need lawful, reproducible and leakage-controlled data paths before training can
support later RL, search, league and Tenhou validation. This document does not
read data, train or evaluate a model and is not model-strength evidence.

## Current Parser Reader Ingestion Status

Current broader P7 parser / reader / ingestion status:

- no parser is approved.
- no dataset reader is approved.
- no ingestion is approved.
- no source ingestion is approved.
- no broad file ingestion is approved.
- no CLI data path is approved.
- no real-data reader is approved.
- no Tenhou reader is approved.
- no real haifu reader is approved.
- no external-log reader is approved.
- no platform-data reader is approved.
- no account / session / cookie / token reader is approved.
- the current synthetic/local supervised smoke fixture helper is not parser /
  reader / ingestion approval.
- the P6 minimal replay schema helper is not broader P7 parser / reader /
  ingestion approval.
- repository docs are not parseable training data.
- source readiness and source-specific approval are not parser / reader /
  ingestion approval.

## Concept Definitions

| concept | definition | approved now |
|---|---|---:|
| parser | Code or process that transforms a source format into a structured internal representation. | no |
| dataset reader | Code or process that loads a bounded dataset, fixture, manifest or record collection into memory for validation, feature work, labels or training. | no |
| ingestion | Any process that accepts source content into project storage, indexes, manifests, normalized records, derived records or downstream pipelines. | no |
| source ingestion | Ingestion behavior tied to a specific approved source and its rights, storage, privacy and platform-terms policy. | no |
| broad file ingestion | Unbounded or generic filesystem loading, recursive scanning or arbitrary user-supplied file/path ingestion. | no |
| CLI data path | Command-line path or argument that causes project code to load source data. | no |
| source-specific approval | Review that approves a named source for limited allowed use, storage and provenance policy. It does not approve parser / reader / ingestion. | no |
| parser / reader / ingestion approval | Review and decision that approve exact parser / reader / ingestion behavior and exact files for approved sources or synthetic/local scope. | no |
| actual feature extraction | Producing feature values or tensors from source/record content for supervised learning or diagnostics. | no |
| actual label generation | Producing labels, targets, annotations or pseudo-labels from source/record content. | no |
| supervised dataset construction | Building examples, splits, manifests or batches intended for supervised training/evaluation. | no |
| training data approval | Approval that a source, derived data, splits and leakage controls may be used for training. | no |

No concept above can substitute for another approval.

## Boundary Dependency Map

The future dependency order is:

```text
source readiness
-> source-specific approval
-> parser / reader / ingestion boundary
-> parser / reader / ingestion proposal
-> parser / reader / ingestion approval decision
-> exact implementation files
-> synthetic/local or approved-source-only implementation
-> implementation review
-> feature / label boundary
-> dataset construction boundary
-> training approval
```

If any required predecessor is missing, parser / reader / ingestion must not be
implemented. For synthetic/local work, the source-specific approval dependency
may be replaced only by an explicit project-authored synthetic/local boundary,
proposal, approval decision and exact first `10_NEXT` implementation task.

## Future Parser Reader Ingestion Candidate Classes

All candidate classes below are not approved now.

| candidate_class | current_status | approved_now | source_dependency | source_approval_required | implementation_approval_required | allowed_for_docs_planning | forbidden_until | risk | notes |
|---|---|---:|---|---:|---:|---:|---|---|---|
| synthetic/local fixture reader | candidate | no | project-authored synthetic/local fixture boundary | no, if explicitly synthetic/local | yes | yes | exact proposal and approval decision | scope creep into generic file reader | Must be exact-file scoped. |
| project-authored synthetic supervised fixture reader | candidate | no | future project-authored synthetic P7 fixture | no, if explicitly synthetic/local | yes | yes | fixture boundary, schema and review | fixture mistaken for training data | Smoke validation only unless later approved. |
| approved-source replay reader | candidate | no | future approved replay source | yes | yes | yes | source-specific approval and reader approval | real-data rights/privacy risk | Cannot start from current docs. |
| approved-source metadata reader | candidate | no | future approved metadata source | yes | yes | yes | source-specific approval and reader approval | metadata may contain identifiers | Requires privacy policy. |
| raw-to-normalized replay parser | candidate | no | future approved source format | yes | yes | yes | source approval, parser proposal and review | parser may imply feature extraction | Must stop before feature/label work. |
| ingestion manifest validator | candidate | no | future approved manifest schema | depends on source | yes | yes | manifest boundary and approval | can become ingestion pipeline | Validator only; no source content loading. |
| provenance / checksum validator | candidate | no | source approval or synthetic fixture boundary | depends on source | yes | yes | provenance boundary and approval | checksum may expose raw paths | Must avoid secret/path leakage. |
| split manifest reader | candidate | no | future dataset/split policy | yes for real sources | yes | yes | split/leakage policy approval | split leakage risk | Not dataset construction by itself. |
| dataset index reader | candidate | no | future approved dataset index | yes | yes | yes | dataset construction boundary | index may imply dataset approval | Cannot imply training-data approval. |
| broad arbitrary file ingestion | rejected | no | none | not applicable | not applicable | risk discussion only | not currently allowed | unbounded data/privacy risk | Rejected for current P7. |
| CLI path ingestion | rejected | no | none | not applicable | not applicable | risk discussion only | separate CLI boundary, if ever | broad ingestion creep | Rejected for current P7. |
| account/session/cookie/token reader | rejected | no | platform/account data | yes plus compliance | yes | risk discussion only | separate lawful compliance approval | privacy/platform/security risk | Forbidden now. |
| platform scraper | rejected | no | platform data | yes plus compliance | yes | risk discussion only | separate lawful compliance approval | automation/evasion risk | Forbidden now. |
| real Tenhou reader before explicit approval | rejected | no | real Tenhou source | yes | yes | risk discussion only | source-specific approval plus reader approval | platform/account/legal risk | Forbidden now. |

## Future Approval Record Fields

Any future parser / reader / ingestion approval record must include:

- `component_id`.
- `component_type`: parser / reader / ingestion.
- source_id dependency.
- approved source categories.
- forbidden source categories.
- input path policy.
- output path policy.
- raw storage policy.
- derived storage policy.
- `may_enter_git`.
- privacy / platform terms status.
- account / session / cookie / token prohibition.
- parser scope.
- reader scope.
- ingestion scope.
- validation commands.
- exact files.
- dependency versions.
- evidence log reference.
- risk register reference.
- decision record reference.
- stop conditions.
- rollback plan.
- human / Web ChatGPT approval reference.
- `10_NEXT` explicit task requirement.

If any required field is missing, the component is not approved.

## Allowed Future Implementation Boundary

A future parser / reader / ingestion implementation must be exactly one of:

- synthetic/local only.
- approved-source-only.
- docs-only validator.

It must:

- be exact-file scoped.
- be reviewed and approved before implementation.
- avoid broad file ingestion.
- avoid CLI unless separately approved.
- avoid account / session / cookie / token handling.
- avoid platform automation.
- avoid unknown third-party binaries.
- avoid real data unless the source is approved and the reader is approved.
- preserve provenance, storage, evidence and risk logs.
- stop before actual feature extraction unless feature extraction is separately
  approved.
- stop before actual label generation unless label generation is separately
  approved.
- stop before supervised dataset construction unless dataset construction is
  separately approved.

## Forbidden Parser Reader Ingestion Scope

The following are forbidden now:

- arbitrary filesystem ingestion.
- recursive broad ingestion.
- CLI user-supplied data path.
- hidden file / dotfile ingestion.
- `.env` / secret / token reading.
- account / session / cookie / token reading.
- real Tenhou reader before explicit source and reader approval.
- real haifu reader before explicit source and reader approval.
- external logs before explicit source and reader approval.
- platform data before explicit source and reader approval.
- scraping / automation / evasion.
- parser that emits feature tensors without feature boundary approval.
- reader that emits labels without label boundary approval.
- ingestion that constructs supervised dataset without dataset policy approval.
- ingestion that trains or calls a model.
- writing raw real data into the repository.
- vendoring third-party data or artifacts into the repository.
- model-output ingestion before model-output policy.
- self-play / league output ingestion before later-stage approval.

## Stop Conditions

Future parser / reader / ingestion implementation must stop if:

- an unapproved source appears.
- an unapproved file type appears.
- real data appears without approval.
- path policy is unclear.
- parser behavior starts extracting features.
- reader behavior starts generating labels.
- ingestion behavior starts constructing a dataset.
- training behavior appears.
- a model call appears.
- CLI or broad ingestion is needed.
- account / session / cookie / token data appears.
- a third-party binary or weights are needed.
- P8-P12 drift appears.
- validation fails.
- evidence is overclaimed.

## Risk Controls

| risk | mitigation | current_status |
|---|---|---|
| parser mistaken as feature extraction | Require parser output boundary to stop at normalized records unless feature boundary is separately approved. | open |
| reader mistaken as label generation | Require reader scope to exclude labels unless label boundary is separately approved. | open |
| ingestion mistaken as dataset construction | Require dataset construction boundary and training-data approval before examples/splits/batches. | open |
| source approval mistaken as ingestion approval | Keep source-specific approval and parser / reader / ingestion approval separate. | open |
| docs context mistaken as parseable data | State that repository docs are planning context, not parseable training data. | open |
| current smoke fixture mistaken as real dataset | Classify synthetic/local smoke fixtures as smoke artifacts, not training sources or reader approval. | open |
| broad file ingestion creep | Forbid arbitrary, recursive and CLI path ingestion unless separately approved. | open |
| CLI ingestion creep | Keep CLI data paths unapproved and require a separate CLI boundary if ever considered. | open |
| secret/token leak | Forbid `.env`, hidden files, account/session/cookie/token data and platform credentials. | open |
| platform/account data leak | Block platform/account sources until lawful privacy/platform review and explicit approval. | open |
| real-data rights violation | Require source-specific rights/provenance/storage approval before any reader. | open |
| split/leakage error | Require split/leakage policy before dataset construction or training use. | open |
| model-output/self-play/league data too early | Classify these as later-stage or unapproved until separate stage review. | open |
| training creep | Keep training approval separate from parser / reader / ingestion approval. | open |
| P8-P12 creep | Require separate transition reviews, scope, entry criteria and first-task approval. | open |
| model-strength overclaim | Evidence grade remains boundary definition only. | open |

## Evidence Requirements

Future parser / reader / ingestion evidence must record:

- `component_id`.
- `component_type`.
- `source_id`.
- source approval status.
- parser / reader / ingestion approval status.
- exact files.
- input policy.
- output policy.
- provenance policy.
- storage policy.
- privacy / platform status.
- validation commands.
- evidence log reference.
- risk register reference.
- decision record reference.
- known exclusions.
- explicit non-evidence warning.

## First Task Candidate

Recommended next task:

```text
Review broader P7 parser, reader and ingestion boundary before implementation.
```

The next task must be a docs-only review gate. It must not implement parser,
reader, ingestion, broad file ingestion or CLI behavior; read real data; approve
source ingestion; approve source use; perform actual feature extraction; perform
actual label generation; construct a supervised dataset; train; implement model
architecture / trainer code; integrate model output; or enter P8-P12.

## Planning Decision

```text
Broader P7 parser, reader and ingestion boundary is defined before
implementation. This does not approve parser, dataset reader, source
ingestion, broad file ingestion, CLI data path, real-data use, actual feature
extraction, actual label generation, supervised dataset construction,
training, model architecture, model-output integration, self-play, league or
P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 parser, reader and ingestion boundary definition evidence only.
```

## Explicit Non-Evidence

This boundary definition is not:

- parser implementation.
- reader implementation.
- ingestion implementation.
- parser / reader / ingestion approval.
- source approval.
- source ingestion approval.
- training-data approval.
- broad file ingestion.
- CLI.
- real-data use.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training.
- model architecture.
- trainer.
- model-output integration.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- self-play.
- league.
- P8-P12 entry approval.
- broader P7 implementation.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
