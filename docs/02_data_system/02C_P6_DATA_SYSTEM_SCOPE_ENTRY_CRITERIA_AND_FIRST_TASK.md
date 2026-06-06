# 02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK

## Scope

This document defines P6 data-system scope, entry criteria, exit criteria and
the first next task before any P6 implementation.

P5 is closed for the current synthetic/local evaluation groundwork scope. The
post-P5 transition review allows only this docs-only P6 definition task.

This document does not:

- approve P6 implementation.
- approve P7-P12 entry.
- add production code.
- add tests or fixtures.
- implement replay schema code.
- implement dataset readers.
- implement feature extraction.
- implement label generation.
- implement data ingestion.
- implement CLI or broad file ingestion.
- read real Tenhou, real haifu, external logs, platform data or online account
  data.
- use platform automation, scraping, evasion or account tooling.
- call OpenAI APIs, LLM APIs, model APIs, Akochan `system.exe`, `libai.so` or
  third-party binaries.
- use unknown model weights, `*.pth`, `*.pt`, checkpoints or snapshots.
- vendor third-party source, binaries, `params/` or build artifacts.
- train, tune, self-play, run league or runner behavior.
- change metrics, registry code, evidence taxonomy or promotion criteria.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## P6 Purpose

P6 is the data-system stage.

Roadmap purpose:

```text
Build replay, feature, label and quality pipelines for training and evaluation.
```

Current P6 purpose before implementation:

```text
Define the data-system boundary so future replay, feature, label and quality
work can be lawful, reproducible, auditable and stage-gated.
```

P6 supports the north-star target indirectly. The project cannot eventually
train and evaluate a Tenhou AI against LuckyJ `10.68` without trustworthy
data provenance, replay semantics, feature/label reproducibility and quality
checks. However, P6 scope planning itself is not model-strength evidence and is
not a LuckyJ comparison.

## Current P6 Status

| item | status | notes |
|---|---|---|
| P5 final closure | complete | closed only for current synthetic/local evaluation groundwork scope |
| post-P5 transition review | complete | allows this docs-only P6 definition task |
| P6 scope definition | complete after this document | docs-only, no implementation |
| P6 implementation | not open | requires later explicit approval |
| P7-P12 | not open | require separate stage gates |

## Allowed P6 Planning Scope

The current P6 planning scope may define:

- data-source taxonomy.
- data-source provenance and rights inventory.
- replay schema requirements.
- feature schema requirements.
- label schema requirements.
- data-quality checklist.
- reproducibility metadata requirements.
- privacy, license, platform and redistribution guardrails.
- synthetic/local placeholder examples as documentation only.
- future acceptance criteria for data-system implementation tasks.
- future evidence requirements for any real data source.

The current P6 planning scope may reference existing project docs, code, tests
and synthetic/local fixtures as context only.

## Forbidden P6 Planning Scope

P6 planning must not become:

- replay parser implementation.
- real haifu ingestion.
- real Tenhou ingestion.
- external-log ingestion.
- platform-data ingestion.
- arbitrary file ingestion.
- model-output ingestion.
- feature extraction implementation.
- label generation implementation.
- data pipeline implementation.
- dataset download.
- model training.
- supervised-learning task.
- self-play or league task.
- CLI or runner task.
- third-party binary wrapper task.
- P7-P12 entry task.

## Allowed Inputs For Future P6 Tasks

Future P6 tasks may use only these inputs after the relevant task explicitly
approves them:

- existing repository documentation.
- project-authored synthetic/local fixtures.
- in-memory synthetic examples.
- source/provenance tables.
- compliance notes and license summaries.
- checksums and metadata for approved non-committed local artifacts.
- lawfully obtained datasets only after a rights/provenance review approves
  their use.

Any future data source must have a source identifier, allowed-use summary,
license/rights status, storage boundary, redistribution status, privacy notes,
schema version and evidence reference before ingestion.

## Forbidden Inputs

The following inputs are forbidden until a later explicit data-source,
compliance and implementation task approves them:

- real Tenhou logs.
- real Tenhou account/session data.
- real haifu.
- online platform data.
- scraped data.
- external logs.
- private datasets without documented rights.
- data produced by platform automation.
- Akochan `system.exe` output.
- `libai.so` output.
- third-party binary output.
- unknown model checkpoints.
- Mortal/Akochan/other model outputs.
- training, self-play or league outputs.
- model weights, `*.pth`, `*.pt`, checkpoints or snapshots.
- third-party source, binaries, `params/` or build artifacts stored in this
  repository.

## P6 Entry Criteria

P6 can enter docs-only planning when all of these are true:

1. P5 is closed for the current synthetic/local evaluation groundwork scope.
2. The post-P5 transition review is complete.
3. `docs/10_next/10_NEXT.md` names a P6 docs-only definition task.
4. The task forbids P6 implementation and P7-P12 entry.
5. The task forbids real Tenhou, real haifu, external logs, platform data and
   online accounts.
6. The task forbids training, tuning, self-play, league and runner behavior.
7. The task forbids model-output integration, CLI and broad file ingestion.
8. The task records evidence and risk requirements for P6 before implementation.

These criteria are met for this docs-only scope definition.

P6 implementation remains blocked until a later task defines and approves the
specific implementation boundary.

## P6 Implementation Entry Criteria

Before any P6 implementation task starts, the project must have:

1. An approved data-source provenance and rights inventory.
2. A replay/source schema boundary that distinguishes synthetic fixtures from
   real data.
3. A storage rule for raw data, derived data and metadata.
4. A no-Git rule for large datasets, raw logs, third-party artifacts, secrets
   and model weights.
5. A data-quality checklist.
6. A reproducibility metadata checklist.
7. A privacy/compliance review for any real or platform-derived source.
8. A specific next implementation task in `docs/10_next/10_NEXT.md`.
9. Clear evidence and non-evidence wording.

Without these, P6 implementation is not open.

## P6 Exit Criteria

P6 should not be considered complete until later approved implementation tasks
provide, at minimum:

1. Approved source/provenance inventory.
2. Replay record schema and decision-state schema.
3. Feature and label schema definitions.
4. Data-quality validation plan.
5. Reproducibility metadata requirements.
6. Storage and artifact policy.
7. Rights/compliance review for every non-synthetic source.
8. Evidence log entries for any accepted source.
9. Risk-register entries for leakage, rights, privacy and overclaiming risks.
10. Explicit handoff criteria for P7 supervised-policy work.

P6 exit does not automatically approve P7. P7 needs a separate transition,
scope, entry criteria and first task.

## Provenance, Rights And Compliance Requirements

Every future data source must record:

- source id.
- source name.
- source type.
- source owner / origin.
- access method.
- date checked.
- license or terms summary.
- allowed use.
- forbidden use.
- redistribution status.
- raw-data storage location.
- whether raw data may enter Git.
- checksum or version when applicable.
- privacy or personal-data notes.
- platform-account involvement.
- ruleset / room / table context when applicable.
- evidence-log id.
- reviewer / approval status.

If any of these are unknown for a real or external source, the source must not
enter an ingestion or training path.

`docs/02_data_system/02A_DATA_SOURCES.md` now defines the detailed P6
data-source provenance and rights inventory for review before replay schema
implementation. That inventory definition is not ingestion approval and does
not open P6 implementation.

## Evidence Requirements

P6 docs-only planning evidence may include:

- scope documents.
- source inventory documents.
- schema documents.
- review documents.
- risk and compliance notes.

P6 implementation evidence, if later approved, must include:

- commit hash.
- source/provenance id.
- schema version.
- validation command.
- sample count.
- checksum or fixture id.
- rights/compliance reference.
- known limitations.
- explicit non-evidence warnings.

P6 evidence is not:

- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P7-P12 entry approval.

## Risk Review

| risk | severity | mitigation |
|---|---:|---|
| P6 scope definition is mistaken for implementation approval | high | keep this document docs-only and set the next task to provenance inventory before implementation |
| data rights ambiguity leads to unsafe ingestion | high | require source/provenance/rights inventory before any ingestion |
| synthetic/local examples are overclaimed as real-data readiness | high | classify this as P6 planning evidence only |
| hidden information leakage enters training data later | high | require future leakage and reproducibility checks before P7 |
| platform data is used before compliance review | high | forbid real Tenhou, platform data and online accounts until separately approved |
| P6 jumps to training or model-output integration | high | keep P7-P12 non-entry boundaries explicit |
| raw logs, third-party artifacts or weights enter Git | high | maintain no-Git storage and artifact policy |
| replay schema becomes code before rights/source boundaries are known | medium-high | make the next task data-source provenance and rights inventory |

## P7-P12 Non-Entry Boundaries

This P6 scope definition does not approve:

- P7 supervised-policy training.
- P8 RL/self-play.
- P9 search / risk model / inference expansion.
- P10 league or tournament evaluation.
- P11 model promotion.
- P12 LuckyJ `10.68` validation.

Any P7-P12 task must wait for its own scope, entry criteria, risk review and
first-task approval.

## First P6 Task Candidate

The next task should be:

```text
Define P6 data-source provenance and rights inventory before replay schema implementation.
```

That task should remain docs-only and should:

- fill or extend `docs/02_data_system/02A_DATA_SOURCES.md`.
- define source/provenance fields and approval statuses.
- keep real Tenhou, real haifu, external logs, platform data and online account
  access forbidden.
- avoid replay schema code, ingestion, feature extraction, label generation,
  CLI, model-output integration, training, self-play, league, runner behavior
  and P7-P12.
- update governance, evidence, risk, handoff and `10_NEXT`.

That task should not implement replay schema or data ingestion.

## Decision

```text
P6 data-system scope, entry criteria and first task are defined for planning
only.
```

P6 implementation is still not open.

## Verification

Recommended validation for this docs-only task:

```bash
git diff --check
```
