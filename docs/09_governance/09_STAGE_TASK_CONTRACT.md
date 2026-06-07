# 09_STAGE_TASK_CONTRACT

## Current stage

Post-full-P6 transition review before defining any P7 task after `02AA`
final full P6 closure review. P5 evaluation foundation is
closed for the current synthetic/local scope; general P6 implementation is not open, and the exact
minimal replay schema / project-authored synthetic fixture task approved by
`02N` is implemented, reviewed with no blocker and accepted as current-scope
complete in `02P`; `02Q` selected a docs-only current-scope closure-criteria
task, `02R` defined those criteria, `02S` reviewed them with no blocker and
`02T` closed the accepted current-scope P6 synthetic/local minimal replay
schema and project-authored synthetic fixture scope only. `12C` completes the
post-current-scope P6 transition review, confirms full P6 remains open and
selects a docs-only full P6 closure roadmap / remaining-scope inventory as the
next task. `02U` defines that roadmap / inventory and selects a docs-only
review gate as the next task. `02V` reviews that roadmap / inventory with no
blocker and selects a docs-only full P6 closure criteria definition as the next
task. `02X` reviews the `02W` criteria with no blocker, and `02Y` finalizes
the full P6 handoff / evidence index. P7-P12 entry remains unapproved.

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
P6 synthetic/local replay fixture boundary = defined before schema implementation; fixture implementation remains closed
P6 synthetic/local replay fixture boundary review = complete; no blocker found; fixture implementation remains closed
P6 replay schema and fixture implementation readiness checklist = defined before code; implementation remains closed
P6 replay schema and fixture implementation readiness checklist review = complete; no blocker found; implementation remains closed
P6 replay schema and synthetic fixture implementation proposal boundary = defined before code; implementation remains closed
P6 replay schema and synthetic fixture implementation proposal boundary review = complete; no blocker found; implementation remains closed
P6 minimal replay schema and synthetic fixture implementation proposal = prepared for review before code; implementation remains closed
P6 minimal replay schema and synthetic fixture implementation proposal review = complete; no blocker found; implementation remains closed
P6 minimal replay schema and synthetic fixture implementation approval decision = complete
P6 minimal replay schema and project-authored synthetic fixture implementation = complete in exact approved files only
P6 minimal replay schema and project-authored synthetic fixture implementation review = complete; no blocker found
P6 minimal replay schema and project-authored synthetic fixture current-scope acceptance decision = complete; accepted as current-scope complete
P6 next current-scope data-system task definition = complete; selected a docs-only closure-criteria task
P6 current-scope data-system closure criteria = defined after minimal replay schema acceptance
P6 current-scope data-system closure criteria review = complete; no blocker found
P6 final current-scope data-system closure review = complete; accepted current-scope closed
P6 post-current-scope transition review = complete; full P6 remains open and P7-P12 entry remains unapproved
P6 full closure roadmap and remaining scope inventory = defined in `02U`; full P6 remains open and P7-P12 entry remains unapproved
P6 full closure roadmap and remaining scope inventory review = complete in `02V`; review can close with no blocker
P6 full closure criteria after roadmap and remaining scope review = defined in `02W`; full P6 remains open and P7-P12 entry remains unapproved
P6 full closure criteria review after roadmap and remaining scope review = complete in `02X`; review can close with no blocker
P6 full handoff and evidence index finalization after closure criteria review = complete in `02Y`; full P6 remains open and P7-P12 remains unapproved
P6 full risk register and source-rights inventory consistency review before final closure = complete in `02Z`; review can close with no blocker for final full P6 closure review
P6 final full closure review = complete in `02AA`; Full P6 can close for the documented P6 data-system scope only
Full P6 = closed for documented P6 data-system scope only
P7-P12 entry = not approved
P6 implementation = closed except for separately approved future tasks
Next = run post-full-P6 transition review before defining any P7 task
```

## AI role

Local Codex engineer + evidence keeper + scope controller.

## Stage goal

Bridge from the closed documented P6 data-system scope into a safe
post-full-P6 transition review by keeping P7-P12 unapproved until separate
scope, entry criteria, risk review and first-task approval exist.

This supports the north-star target by ensuring that any future supervised
learning, RL, search, league or LuckyJ validation work starts only after the
data-system closure state is understood and the next stage has explicit scope,
entry criteria, provenance guardrails, rights/compliance requirements and
first-task boundaries.

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

The stable-dan evaluation groundwork subtrack is complete for current P5 scope. The offline result envelope schema and synthetic stable-dan envelope smoke test are implemented. The legal-action / invalid-action metric specification and action canonicalization schema are defined, the synthetic legal-action metric fixture schema smoke test is implemented, the synthetic evaluator boundary is defined, the first synthetic evaluator is implemented for the project-authored fixture only, synthetic parse-failure fixture coverage is implemented, the legal-action synthetic evaluator coverage review is complete for the current synthetic-only `dahai` + strict scope, the P5 tiny benchmark harness boundary is defined before implementation, the P5 tiny benchmark harness synthetic fixture schema smoke test is implemented, the fixture schema coverage review confirms it is sufficient as a front-door input boundary for a future P5-only harness implementation, the P5 tiny benchmark harness is implemented only for the project-authored synthetic fixture, the implementation review is complete for the current fixture scope, the offline envelope coverage review confirms the current synthetic tiny benchmark diagnostic can be represented with the existing envelope, the metric registry consistency review confirms current names, units, directions, statuses and evidence grades are consistent, the evidence taxonomy / promotion guardrails review confirms current P5 synthetic/local evidence labels and non-evidence warnings remain conservative, the P5 closure criteria / exit readiness checklist is defined, the closure criteria review found no blocker, the P5 handoff/evidence index finalization found no blocker, and the final P5 closure review gate records that P5 can close for the current synthetic/local evaluation groundwork scope. P5 closure is not P6-P12 entry approval. The post-P5 transition review records that the project may define P6 scope before implementation. `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P6 data-system scope, entry criteria, future implementation entry criteria, future exit criteria, provenance/rights/compliance requirements, evidence requirements, risks, P7-P12 non-entry boundaries and the first next task. `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source provenance and rights inventory before replay schema implementation, and `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` reviews it with no blocker. `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema documentation boundary after source inventory review, including allowed/forbidden scope, source dependencies, field families, validation expectations, future implementation entry criteria and replay-schema risks. `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` reviews that boundary with no blocker. `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md` defines the P6 synthetic/local replay fixture boundary before schema implementation. `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md` reviews that boundary with no blocker. `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md` defines the replay schema and fixture implementation readiness checklist before code. `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md` reviews that checklist with no blocker. `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md` defines the replay schema and synthetic fixture implementation proposal boundary before code. `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md` reviews that proposal boundary with no blocker. `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md` prepares the minimal implementation proposal for review before code. `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md` reviews that proposal with no blocker. `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` approves only the next exact minimal implementation task. General P6 implementation, real data, parser / reader / ingestion work, feature extraction, label generation and P7-P12 remain closed beyond that exact task.

`docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md` reviews the `02L` proposal with no blocker. `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` approved only the exact minimal implementation task. That task is now implemented in `src/mjlabai/data/replay_schema.py`, `tests/fixtures/data/synthetic_replay_smoke.json`, `tests/data/test_replay_schema.py` and `tests/data/test_synthetic_replay_fixture_schema.py`, plus directly related docs/governance synchronization. `docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md` reviews that exact implementation with no blocker. `docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md` accepts that exact minimal implementation as current-scope complete. `docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` selects a docs-only closure-criteria definition as the next bounded P6 data-system task. `docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` defines those criteria and sets the next task to a docs-only review gate. `docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` reviews those criteria with no blocker. `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md` closes only the accepted current-scope P6 synthetic/local minimal replay schema and project-authored synthetic fixture scope. It must not be used as full P6 closure, P7-P12 entry, parser, dataset-reader, ingestion, feature extraction, label generation, real-data, model-output, CLI, training, self-play, league or strength evidence.

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

Run post-full-P6 transition review before defining any P7 task.
