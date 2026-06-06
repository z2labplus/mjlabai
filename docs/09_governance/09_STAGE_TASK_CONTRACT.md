# 09_STAGE_TASK_CONTRACT

## Current stage

P6 data-system docs-only planning. P5 evaluation foundation is closed for the
current synthetic/local scope; P6 implementation is not yet open.

Current focus:

```text
Mortal = F1 paused as runnable baseline / ReferenceOnly
Akochan = F1 Conditional Pass; F2 fixed-sample real-exe wrapper validation passed in workflow run `26629344590`; not strength evidence
Stable-dan calculator = deterministic point estimate implemented and tested
Stable-dan bootstrap CI = percentile empirical multinomial bootstrap implemented and tested
Stable-dan threshold helper = LuckyJ 10.68 lower-bound comparison implemented and tested
Stable-dan reporting schema = minimum sample-size guardrails and report schema implemented and tested
Stable-dan placement aggregation = offline placement-count helper implemented and tested
Stable-dan report smoke fixture = CLI-free synthetic placement fixture implemented and tested
Stable-dan evaluation API docs = synthetic placement example added
Stable-dan evaluation groundwork = complete for current P5 scope
Offline evaluation result envelope = metric registry and schema implemented/tested
Offline envelope smoke fixture = synthetic stable-dan envelope smoke test implemented
Legal-action metric specification = defined
Action canonicalization schema = defined
Synthetic legal-action metric fixture schema smoke test = implemented
Synthetic legal-action metric evaluator boundary = defined
Synthetic legal-action metric evaluator = implemented for project-authored fixture only
Synthetic legal-action parse-failure fixture coverage = implemented
Synthetic legal-action evaluator coverage review = complete for current synthetic-only dahai + strict scope
P5 tiny benchmark harness boundary = defined before implementation
P5 tiny benchmark harness synthetic fixture schema smoke test = implemented
P5 tiny benchmark fixture schema coverage review = complete
P5 tiny benchmark harness = implemented for project-authored synthetic fixture only
P5 tiny benchmark harness implementation review = complete
P5 offline envelope coverage review for synthetic tiny benchmark diagnostics = complete
P5 metric registry consistency review across stable-dan, legal-action and tiny benchmark diagnostics = complete
P5 synthetic/local evidence taxonomy and promotion guardrails review = complete
P5 evaluation groundwork closure criteria and exit readiness checklist = defined
P5 evaluation groundwork closure criteria and exit readiness checklist review = complete; no blocker found
P5 handoff and evidence index finalization = complete; no blocker found
Final P5 closure review gate = complete; P5 can close for current synthetic/local evaluation groundwork scope
P5 overall = closed for current synthetic/local evaluation groundwork scope
Post-P5 transition review = complete
P6 data-system scope / entry criteria / first task definition = complete as docs-only planning
P6 data-source provenance and rights inventory = defined and reviewed before replay schema implementation; no blocker found
P6 replay schema documentation boundary = defined after source inventory review; implementation remains closed
P6 replay schema documentation boundary review = complete; no blocker found; implementation remains closed
Next = define P6 synthetic/local replay fixture boundary before schema implementation
```

## AI role

Local Codex engineer + evidence keeper + scope controller.

## Stage goal

Bridge from the closed P5 evaluation foundation into safe P6 data-system
planning without executing P6 implementation.

This supports the north-star target by ensuring that future replay, feature,
label and dataset work has explicit scope, entry criteria, provenance
guardrails, rights/compliance requirements and first-task boundaries before any
supervised learning, RL, search or LuckyJ validation work begins.

## Inputs

- `AGENTS.md`
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/04_rl_selfplay/04G_ALGORITHM_RACING_FUNNEL.md`
- `docs/05_evaluation/05G_RACING_FUNNEL_EVALUATION.md`
- `docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md`

## Do

- Execute only the first unchecked task in `docs/10_next/10_NEXT.md`.
- Check repository accessibility, license, dependencies, build path, model artifacts, minimal sample run, input/output schema and logging ability.
- Record commit/version, local environment results and blockers.
- Keep candidate promotion tied to documented evidence.

## Do not

- Do not train models.
- Do not tune hyperparameters.
- Do not start self-play.
- Do not connect to real Tenhou.
- Do not create platform automation, scraping, evasion or account tooling.
- Do not claim strength improvement from reproducibility checks.
- Do not use unknown model weights, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Do not vendor or copy third-party source into this repository.
- Do not exceed the documented Akochan F2 wrapper boundary: fixed `legal_action` / `mjai_log` samples only until later evidence justifies more.
- Treat fake-executable wrapper tests as implementation smoke tests only, not real Akochan compatibility or strength evidence.
- Treat Akochan run `26629344590` as fixed-sample wrapper/integration evidence only, not strength evidence.
- Treat workflow run `26621536548` as partial F2 evidence: real `legal_action` passed, but real `mjai_log` remained blocked by `setup_mjai.json` working-directory handling.
- Treat workflow run `26623247276` as partial F2 evidence: cwd handling is improved and real `legal_action` passed, but real `mjai_log` remained blocked by stdout parsing.
- Treat workflow run `26628128871` as partial F2 evidence: strict JSON stream parsing improved diagnostics, but real `mjai_log` exposed mixed stdout with the known status line `calculating review`.
- Treat workflow run `26629344590` as closing the fixed-sample real-exe wrapper validation task: fake tests passed 14 tests, real `legal_action` passed and real `mjai_log` passed.
- Do not vendor or store Akochan source, `system.exe`, `libai.so`, `params/`, third-party binaries or unknown artifacts in this repository.
- Do not promote Mortal to F2 unless a lawful, verifiable and usable trained model artifact is provided and Mortal F1 is re-opened with source, version/tag, usage constraints and checksum.

## Task boundary

F1 is an audit stage only. It may inspect external source repositories and local dependencies, but it must not create project source code or training scripts.

F2 may create only the documented minimal wrapper skeleton for fixed `legal_action` / `mjai_log` samples. F2 must keep Akochan source and binaries outside this repository and must not become training, self-play, Tenhou integration or platform automation.

The Tenhou stable-dan calculator is an offline metric utility. It must remain separate from training, self-play, league execution and real Tenhou integration.

The stable-dan bootstrap CI is an offline statistical reporting utility. It must remain separate from training, self-play, league execution and real Tenhou integration.

The stable-dan threshold helper is an offline statistical reporting utility. It must remain separate from training, self-play, league execution and real Tenhou integration.

The stable-dan reporting schema is an offline statistics reporting utility. It must remain separate from training, self-play, league execution and real Tenhou integration.

The stable-dan placement aggregation helper is an offline evaluation input utility. It accepts only explicit placement values and whitelisted aliases; it must not become a league harness, real Tenhou ingestion path or model-strength claim by itself.

The CLI-free stable-dan report smoke fixture is a synthetic-only code-path test. It must not be interpreted as model-strength evidence, Tenhou evidence, a league result or a LuckyJ comparison claim.

The stable-dan evaluation API documentation is an API-only guide. It must not become a CLI, league harness, file ingestion system, training path, self-play path or real Tenhou integration.

The stable-dan evaluation groundwork subtrack is complete for current P5 scope. The offline result envelope schema and synthetic stable-dan envelope smoke test are implemented. The legal-action / invalid-action metric specification and action canonicalization schema are defined, the synthetic legal-action metric fixture schema smoke test is implemented, the synthetic evaluator boundary is defined, the first synthetic evaluator is implemented for the project-authored fixture only, synthetic parse-failure fixture coverage is implemented, the legal-action synthetic evaluator coverage review is complete for the current synthetic-only `dahai` + strict scope, the P5 tiny benchmark harness boundary is defined before implementation, the P5 tiny benchmark harness synthetic fixture schema smoke test is implemented, the fixture schema coverage review confirms it is sufficient as a front-door input boundary for a future P5-only harness implementation, the P5 tiny benchmark harness is implemented only for the project-authored synthetic fixture, the implementation review is complete for the current fixture scope, the offline envelope coverage review confirms the current synthetic tiny benchmark diagnostic can be represented with the existing envelope, the metric registry consistency review confirms current names, units, directions, statuses and evidence grades are consistent, the evidence taxonomy / promotion guardrails review confirms current P5 synthetic/local evidence labels and non-evidence warnings remain conservative, the P5 closure criteria / exit readiness checklist is defined, the closure criteria review found no blocker, the P5 handoff/evidence index finalization found no blocker, and the final P5 closure review gate records that P5 can close for the current synthetic/local evaluation groundwork scope. P5 closure is not P6-P12 entry approval. The post-P5 transition review records that the project may define P6 scope before implementation. `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P6 data-system scope, entry criteria, future implementation entry criteria, future exit criteria, provenance/rights/compliance requirements, evidence requirements, risks, P7-P12 non-entry boundaries and the first next task. `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source provenance and rights inventory before replay schema implementation, and `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` reviews it with no blocker. `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema documentation boundary after source inventory review, including allowed/forbidden scope, source dependencies, field families, validation expectations, future implementation entry criteria and replay-schema risks. `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` reviews that boundary with no blocker and records that the review can close while replay schema implementation remains closed. P6 implementation, replay schema implementation and data ingestion remain closed. The next task must define the P6 synthetic/local replay fixture boundary before schema implementation, remain docs-only and must not implement replay schema code, data ingestion, dataset readers, feature extraction, label generation, CLI, broad file ingestion, model-output integration, real Tenhou, real haifu, external logs, platform data, training, self-play, league, runner behavior, P7-P12 or model-strength claims.

## Output files

After a real P3/F1/F2 task, update:

- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/00_HANDOFF.md`

If the task changes candidate status or records audit evidence, update:

- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`

If a blocker or project risk is discovered, update:

- `docs/09_governance/09_RISK_REGISTER.md`

## Acceptance criteria

- The current stage and candidate funnel stage are explicit.
- License and dependency notes are recorded.
- Minimal run result is recorded as pass/fail/blocked.
- Input/output and logging viability are noted.
- The next lowest-cost action is recorded in `docs/10_next/10_NEXT.md`.

## Only next step

Define P6 synthetic/local replay fixture boundary before schema implementation.
