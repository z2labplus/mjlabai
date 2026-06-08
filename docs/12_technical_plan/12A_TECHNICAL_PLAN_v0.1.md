# 12A_TECHNICAL_PLAN_v0.1

## Purpose

本文件是当前项目执行总纲。

项目从这一版开始采用：

```text
技术方案优先，论文未来总结。
```

含义：

- 技术方案用于指导当前阶段、任务拆分、实验选择、代码落地和评测闭环。
- 论文不是当前执行主线；论文是未来当路线、证据、评测和结论足够稳定之后的成果总结。
- 任何代码、实验、baseline、训练或评测都必须先能说明它如何服务北极星目标。

North-star target:

```text
Train a Japanese riichi mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum benchmark: above Tenhou 10 dan and stable dan > 10.68.
```

## Current Stage

当前项目处于：

```text
P7 docs-only scope / entry criteria / first-task review gate after P7 scope
definition in `03E` and post-full-P6 transition review in `12D`.
P5 evaluation foundation is closed for the current synthetic/local scope.
General P6 data-system implementation is not open; the exact minimal replay
schema and project-authored synthetic fixture task approved by `02N` is
implemented, reviewed with no blocker and accepted as current-scope complete in
`02P`; `02Q` selected a docs-only current-scope closure-criteria task, `02R`
defined those criteria, `02S` reviewed them with no blocker and `02T` closed
the accepted current-scope P6 synthetic/local minimal replay schema and
project-authored synthetic fixture scope only. `02AA` closes full P6 only for
the documented P6 data-system scope: docs/governance/source-rights planning,
accepted synthetic/local minimal replay schema and project-authored synthetic
fixture smoke implementation, and deferred/blocked/later-stage inventory.
P7-P12 entry remains unapproved.
Mortal = F1 paused as runnable baseline / ReferenceOnly.
Akochan = F1 Conditional Pass; F2 fixed-sample real-exe wrapper validation passed in workflow run `26629344590`; not strength evidence.
Tenhou stable-dan calculator = deterministic point estimate implemented and tested.
Tenhou stable-dan bootstrap CI = percentile empirical multinomial bootstrap implemented and tested.
Tenhou stable-dan threshold helper = LuckyJ 10.68 lower-bound comparison implemented and tested.
Tenhou stable-dan reporting schema = minimum sample-size guardrails and report schema implemented and tested.
Tenhou stable-dan placement aggregation = offline placement-count helper implemented and tested.
Tenhou stable-dan report smoke fixture = CLI-free synthetic placement fixture implemented and tested.
Tenhou stable-dan evaluation API docs = synthetic placement example added.
Tenhou stable-dan evaluation groundwork = complete for current P5 scope.
P5 offline evaluation metric registry and result envelope schema = implemented/tested.
Offline evaluation envelope smoke fixture = synthetic stable-dan envelope smoke test implemented.
P5 legal-action / invalid-action metric specification = defined.
P5 action canonicalization schema for legal-action metric fixtures = defined.
Synthetic legal-action metric fixture schema smoke test = implemented.
P5 legal-action metric synthetic evaluator boundary = defined.
P5 overall = closed for the current synthetic/local evaluation groundwork scope.
P5 synthetic legal-action evaluator = implemented for project-authored fixture only.
P5 synthetic parse-failure fixture coverage = implemented.
P5 legal-action synthetic evaluator coverage review = complete for current synthetic-only dahai + strict scope.
P5 tiny benchmark harness boundary = defined before implementation.
P5 tiny benchmark harness synthetic fixture schema smoke test = implemented.
P5 tiny benchmark fixture schema coverage review = complete.
P5 tiny benchmark harness = implemented for project-authored synthetic fixture only.
P5 tiny benchmark harness implementation review = complete.
P5 offline envelope coverage review for synthetic tiny benchmark diagnostics = complete.
P5 metric registry consistency review across stable-dan, legal-action and tiny benchmark diagnostics = complete.
P5 synthetic/local evidence taxonomy and promotion guardrails review = complete.
P5 evaluation groundwork closure criteria and exit readiness checklist = defined.
P5 evaluation groundwork closure criteria and exit readiness checklist review = complete; no blocker found.
P5 handoff and evidence index finalization = complete; no blocker found.
P5 final closure review gate = complete; P5 can close for current synthetic/local evaluation groundwork scope.
Post-P5 transition review = complete.
P6 data-system scope / entry criteria / first task definition = complete as docs-only planning.
P6 data-source provenance and rights inventory = defined and reviewed before replay schema implementation; no blocker found.
P6 replay schema documentation boundary = defined after source inventory review; implementation remains closed.
P6 replay schema documentation boundary review = complete; no blocker found; implementation remains closed.
P6 synthetic/local replay fixture boundary = defined before schema implementation; fixture implementation remains closed.
P6 synthetic/local replay fixture boundary review = complete; no blocker found; fixture implementation remains closed.
P6 replay schema and fixture implementation readiness checklist = defined before code; implementation remains closed.
P6 replay schema and fixture implementation readiness checklist review = complete; no blocker found; implementation remains closed.
P6 replay schema and synthetic fixture implementation proposal boundary = defined before code; implementation remains closed.
P6 replay schema and synthetic fixture implementation proposal boundary review = complete; no blocker found; implementation remains closed.
P6 minimal replay schema and synthetic fixture implementation proposal = prepared for review before code; implementation remains closed.
P6 minimal replay schema and synthetic fixture implementation proposal review = complete; no blocker found; implementation remains closed.
P6 minimal replay schema and synthetic fixture implementation approval decision = complete.
P6 minimal replay schema and project-authored synthetic fixture implementation = complete in exact approved files only.
P6 minimal replay schema and project-authored synthetic fixture implementation review = complete; no blocker found.
P6 minimal replay schema and project-authored synthetic fixture current-scope acceptance decision = complete; accepted as current-scope complete.
P6 next current-scope data-system task definition = complete; selected a docs-only closure-criteria task.
P6 current-scope data-system closure criteria = defined after minimal replay schema acceptance.
P6 current-scope data-system closure criteria review = complete; no blocker found.
P6 final current-scope data-system closure review = complete; accepted current-scope closed.
P6 post-current-scope transition review = complete; full P6 remains open and
P7-P12 remains unapproved.
P6 full closure roadmap and remaining scope inventory = defined in `02U`;
full P6 remains open and P7-P12 remains unapproved.
P6 full closure roadmap and remaining scope inventory review = complete in
`02V`; review can close with no blocker.
P6 full closure criteria after roadmap and remaining scope review = defined in
`02W`; full P6 remains open and P7-P12 remains unapproved.
P6 full closure criteria review after roadmap and remaining scope review =
complete in `02X`; review can close with no blocker.
P6 full handoff and evidence index finalization after closure criteria review =
complete in `02Y`; full P6 remains open and P7-P12 remains unapproved.
P6 full risk register and source-rights inventory consistency review before
final closure = complete in `02Z`; review can close with no blocker for final
full P6 closure review.
Final full P6 closure review = complete in `02AA`; Full P6 can close for the
documented P6 data-system scope only.
Post-full-P6 transition review = complete in `12D`; the next task may define
P7 scope, entry criteria and first task as docs-only planning before
implementation.
P7 scope, entry criteria and first task = defined in
`docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` as
docs-only planning before implementation.
P7-P12 entry = not approved.
P7 implementation = not approved.
P6 implementation = closed except for separately approved future tasks.
Next = review P7 scope, entry criteria and first task before implementation.
```

本技术方案不改变当前阶段，不允许跳过 Mortal/Akochan/Archer 等 baseline 的 F1/F2 复现与接口审计。

## Role Split

### Web ChatGPT Pro

网页端 ChatGPT Pro 负责高层方案与研究判断：

- 技术方案设计。
- 外部资料调研。
- 候选算法评审。
- 实验路线评审。
- 风险与合规判断。
- 关键技术决策。
- 论文结构和未来成果总结。

网页端输出不能直接替代项目事实。任何网页端结论都必须落到 Git + docs 后，才成为项目事实来源。

### Local Codex App

本地 Codex App 负责本地执行与落地：

- 读取项目规则。
- 执行 `docs/10_next/10_NEXT.md` 的第一项任务。
- 修改代码。
- 运行测试。
- 做本地可复现审计。
- 更新文档。
- 记录 evidence、risk、changelog 和 next。

Codex 不负责跳阶段，不负责无证据声称模型更强，不负责绕过平台规则。

## Source of Truth

唯一事实来源是：

```text
Git + docs
```

具体规则：

- Git worktree 中的文档和代码是当前项目状态。
- 网页端 ChatGPT Pro 的结论只有被 Codex 写入 docs 后才生效。
- 口头讨论、聊天记录、外部网页摘要不能单独作为项目事实。
- 每个技术决策必须写入对应 primary doc，并同步 handoff / changelog / next。
- 外部证据必须进入 `docs/09_governance/09_EVIDENCE_LOG.md`。
- 新风险必须进入 `docs/09_governance/09_RISK_REGISTER.md`。

## Main Technical Route

当前主路线是组合路线，不是单论文完整复现路线：

```text
Suphx-style SL + RL
+ Tenhou stable dan / pt EV reward
+ ACH-inspired policy improvement
+ risk model / search
+ baseline racing funnel
```

解释：

- Suphx-style SL + RL: 使用监督学习建立基础策略，再用自我对弈强化学习提升长期 Tenhou-like 指标。
- Tenhou stable dan / pt EV reward: 奖励与评测必须围绕稳定段位、Tenhou pt EV、平均顺位和四位率控制。
- ACH-inspired policy improvement: 借鉴 Actor-Critic Hedge / regret-minimization-inspired policy improvement 思路，但不得假设可直接迁移到四人 Tenhou。
- risk model / search: 把押引、危险牌、南场避四、Oorasu 排名判断作为后续增强重点。
- baseline racing funnel: Mortal / Archer / Akochan / Kanachan 等候选必须按 F0-F7 漏斗逐级验证。

## LuckyJ Position

LuckyJ 是目标基准，不是直接完整复现对象。

项目对 LuckyJ 的使用方式：

- 固定最低目标线：Tenhou stable dan > 10.68。
- 收集公开指标，定义验收条件。
- 不假设能得到 LuckyJ 实现细节、训练数据、权重或平台流程。
- 不为了复现 LuckyJ 而跳过本地评测、baseline、数据系统和合规边界。

## Execution Rule

Codex 每次只执行：

```text
docs/10_next/10_NEXT.md 的第一项未完成任务。
```

如果网页端或用户提出新方向，先判断它属于哪个阶段、哪个 primary doc、是否应成为新的 `10_NEXT`。不能把新想法直接变成训练、平台接入或大规模实验。

## Update Rule

每次真实任务完成后必须更新：

- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

如果任务产生技术决策，还必须更新：

- `docs/09_governance/09_DECISION_RECORD.md`

如果任务产生代码或实验结果，还必须记录：

- 使用的 commit / version / config。
- 数据来源与许可。
- 模型权重来源、版本、usage constraints 和 checksum。
- 评测规则、样本量、指标和失败案例。

## Current Non-Goals

当前不做：

- 不写训练代码。
- 不下载模型。
- 不接入真实 Tenhou。
- 不创建平台自动化、抓取、账号工具、规避或反检测逻辑。
- 不声称模型超过任何 baseline。
- 不把 LuckyJ 当作可直接复现对象。
- 不跳过 baseline racing funnel。
- 不使用来路不明的 model weights、`*.pth`、`*.pt`、`checkpoint` 或 `snapshot` 文件。
- 不把第三方源码 vendor/copy 进本仓库。
- 不超过 Akochan F2 fixed-sample wrapper 边界；不保存第三方源码、二进制、`params/` 或未知 artifact。

## Current Next Task

当前 `10_NEXT` 的下一步是：

```text
Review P7 scope, entry criteria and first task before implementation.
```

`docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
defines P7 supervised-learning scope, entry criteria and the first task
candidate before implementation after the `12D` post-full-P6 transition review.
Full P6 is closed only for the documented P6 data-system scope, and the next
step may be only a docs-only review of that P7 scope definition. This is not
P7 implementation, not P7 first-task execution and not P8-P12 entry approval.
The next task must not add production code, tests, fixtures, parser, dataset
reader, ingestion, feature extraction, label generation, real Tenhou, real
haifu, external logs, platform data, model-output integration, CLI, broad file
ingestion, training, tuning, self-play, league, runner behavior or
model-strength claims.

The exact P6 implementation approved by `02N` is complete and reviewed in
`docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md`
with no blocker and accepted as current-scope complete in
`docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md`.
`docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
selected a docs-only closure-criteria definition as the next bounded P6
data-system task. `docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
now defines those criteria and selects a docs-only review gate as the next
task. `docs/02_data_system/02S_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md`
reviews those criteria with no blocker and selects a docs-only final
current-scope closure review gate as the next task. It does not close full P6,
close current-scope P6 or approve real Tenhou, real haifu, external logs,
platform data, parser, dataset reader, data ingestion, feature extraction,
label generation, CLI, model-output integration, training, self-play, league
or P7-P12. `docs/02_data_system/02T_FINAL_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_REVIEW.md`
now records that current-scope P6 can close for the accepted synthetic/local
minimal replay schema and project-authored synthetic fixture scope only. Full
P6 remains open; P7-P12, real data, parser, dataset reader, ingestion, feature
extraction, label generation, model-output integration, CLI, training,
self-play and league remain unapproved.

`docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`
records that the post-current-scope P6 transition review is complete. It
selects a docs-only full P6 closure roadmap and remaining scope inventory as
the next task; `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
now defines that roadmap / inventory and selects a docs-only review gate as the
next task. `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
reviews that roadmap / inventory with no blocker and selects a docs-only full
P6 closure criteria definition as the next task. This does not approve
implementation, real data, parser, dataset reader, ingestion, feature
extraction, label generation or P7-P12.
`docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
defines the full P6 closure criteria, exit readiness checklist, required
remaining full-P6 closure items, deferred / blocked / later-stage /
out-of-scope classifications and P7-P12 non-entry conditions. It does not
close full P6, approve P7-P12, approve implementation, real data, parser,
dataset reader, ingestion, feature extraction or label generation. The next
task is a docs-only review of those criteria.
`docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
reviews those criteria with no blocker and selects full P6 handoff / evidence
index finalization as the next docs-only task. It does not close full P6,
approve P7-P12, approve implementation, real data, parser, dataset reader,
ingestion, feature extraction or label generation.
`docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
finalizes the full P6 handoff and evidence index after the criteria review. It
records the handoff summary, P6 evidence index, evidence grade consistency,
remaining required full-P6 items and next risk / source-rights review scope.
It does not close full P6, approve P7-P12, approve implementation, real data,
parser, dataset reader, ingestion, feature extraction or label generation.
`docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
reviews the risk register and source-rights inventory consistency before final
closure review. It finds no risk/source-rights blocker for the final full P6
closure review gate. It does not close full P6, approve P7-P12, approve source
ingestion, approve real data, approve parser, dataset reader, ingestion,
feature extraction or label generation.
`docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
records that full P6 can close for the documented P6 data-system scope only:
docs/governance/source-rights planning, accepted synthetic/local minimal
replay schema and project-authored synthetic fixture smoke implementation, and
deferred/blocked/later-stage inventory. It is not P7-P12 entry approval, not
P7 first-task approval and not new implementation approval.
`docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md` records that the
post-full-P6 transition review is complete and selected the docs-only P7 scope
definition task. `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
now defines P7 scope, entry criteria and the first task candidate before
implementation. This is not P7 implementation, not P7 first-task execution and
not P8-P12 entry approval.

 The stable-dan calculator now supports four-player general/ippan, upper/joukyu, expert/tokujou and phoenix/houou room formulas, records placement counts/rates and raises `StableDanUndefinedError` when `fourth_count == 0`. The bootstrap CI uses percentile empirical multinomial resampling, reports successful/undefined resamples and refuses to fabricate infinite stable dan. The threshold helper uses LuckyJ stable dan `10.68` by default and only returns `clear_pass` when bootstrap lower bound exceeds the threshold with acceptable undefined rate. The reporting schema separates `clears_threshold` from `can_enter_threshold_review` so low-sample reports cannot become project-level LuckyJ claims. The placement aggregation helper converts only explicit offline placement values and whitelisted aliases into first/second/third/fourth counts; it rejects zero-based, ambiguous, bool, float and unknown inputs. The smoke fixture verifies the CLI-free path from synthetic placements through report serialization without Tenhou data or model-strength claims. The API documentation explains this usage path and its guardrails. `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md` records stable-dan evaluation groundwork as complete for current P5 scope while keeping P5 overall open at that time. `src/mjlabai/eval/offline_result.py` and `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md` define the P5 offline metric registry and result envelope schema. `tests/eval/test_offline_envelope_smoke.py` verifies that a synthetic stable-dan report can be represented in the envelope. `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md` defines legal-action and invalid-action metric denominators, parse/missing/skipped handling, canonical matching principles, envelope mapping and the synthetic evaluator boundary before implementation. `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md` defines canonical action fields, current minimum `dahai` fixture scope, strict matching, future relaxed matching boundary and legal-action fixture shape. `tests/fixtures/eval/legal_action_metric_smoke.json` and `tests/eval/test_legal_action_fixture_schema_smoke.py` validate a synthetic-only legal-action fixture shape, now including `parse_failure` coverage. `src/mjlabai/eval/legal_action_metric.py` and `tests/eval/test_legal_action_metric.py` implement and test a narrow synthetic-only evaluator for that fixture, producing counts/rates and an offline envelope without CLI, broad ingestion, canonicalizer, rule engine, model code, training, self-play, league or Tenhou integration. `docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md` records that the current fixture covers `legal`, `invalid`, `missing_action`, `parse_failure` and `skipped_no_legal_actions`, and that the legal-action synthetic evaluator minimum outcome coverage is complete only for the current P5 synthetic-only `dahai` + strict scope. `docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md` defines the future tiny benchmark harness boundary for legal-action rate, latency and fixed-position diagnostics before implementation. `tests/fixtures/eval/tiny_benchmark_harness_smoke.json` and `tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py` validate the synthetic/local fixture shape for that boundary without implementing a harness, measuring latency, calculating fixed-position exact-match or reading real data. `docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md` records that the fixture schema is sufficient as the front-door input boundary for a future P5-only tiny benchmark harness implementation. `src/mjlabai/eval/tiny_benchmark_harness.py` now implements only that project-authored synthetic/local harness boundary and can emit an offline envelope without latency measurement, fixed-position exact-match, model-output integration, CLI, real data or strength claims. `docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md` records that this implementation review can close for the current fixture scope with no blocker. `docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md` records that the existing offline envelope coverage is sufficient for the synthetic tiny benchmark diagnostic scope with `wrapper_smoke_success`, `sample_size = 1`, `latency_ms = None`, all-false safety flags, synthetic/local warnings and evidence references. `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md` records that current P5 metric registry names, units, directions, statuses and evidence grades are consistent across stable-dan, legal-action and tiny benchmark diagnostics with no blocker. `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md` records that current P5 synthetic/local evidence labels, non-evidence warnings, promotion/ranking guardrails and stage-boundary wording are consistent with no blocker. `docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md` defines P5 closure criteria and an exit readiness checklist. `docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md` reviews those criteria and finds no blocker. `docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md` finalizes the P5 handoff and evidence index for final closure review and finds no blocker. `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md` records that all closure criteria pass, no blocker remains, and P5 can close for the current synthetic/local evaluation groundwork scope. `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` records that the project may start a docs-only task to define P6 data-system scope, entry criteria and first task before implementation. `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P6 data-system purpose, allowed/forbidden inputs, entry criteria, future implementation entry criteria, future exit criteria, provenance/rights/compliance requirements, evidence requirements, risks, P7-P12 non-entry boundaries and the first next task. `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 source provenance/rights inventory, source categories, approval vocabulary, pre-ingestion checklist, future evidence requirements and rights/provenance risks before replay schema implementation. `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` reviews that inventory and finds no blocker, while keeping broad P6 implementation and data ingestion closed. `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema documentation boundary after source inventory review, and `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` reviews it with no blocker. `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md` defines the P6 synthetic/local replay fixture boundary before schema implementation. `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md` reviews that boundary with no blocker. `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md` defines the replay schema and fixture implementation readiness checklist before code. `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md` reviews that checklist with no blocker. These remain metric infrastructure, specification, implementation, review, finalization, closure-review, transition-review and P6 planning evidence only, not strength evidence. `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md` defines the proposal boundary that any future replay schema or synthetic fixture implementation proposal must satisfy before code. `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md` reviews that proposal boundary with no blocker. `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md` prepares the minimal implementation proposal for review before code. `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md` reviews it with no blocker. `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` approved only the exact minimal implementation task. That task is now implemented in the approved files and reviewed in `02O` with no blocker before any further P6 work. It does not approve broad P6 implementation, real data, parser / reader / ingestion work, feature extraction, label generation, CLI, model-output integration, training, self-play, league, P7-P12 or model-strength claims.

`docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
prepares the current minimal proposal, and
`docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
reviews it with no blocker while keeping implementation closed.
`docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
approved only the exact minimal implementation task. That implementation is
now complete, reviewed and accepted as current-scope complete in the named
minimal replay schema module, project-authored synthetic/local fixture and two
minimal tests; `02Q` selects current-scope closure criteria as the next docs-only
P6 task, `02R` defines those criteria, `02S` reviews them with no blocker and
`02T` closes the accepted current-scope only. All parser, dataset reader, ingestion, feature
extraction, label generation, real-data, CLI, model-output, training,
self-play, league and P7-P12 work remains unapproved.

Mortal runnable baseline 已暂停，因为当前没有合法、可校验、可使用的 trained model artifact。Mortal 仍保留为源码、mjai 接口、方法论和工程参考。除非未来先补齐 artifact 来源、version/tag、usage constraints 和 checksum 并重新打开 F1，否则不进入 Mortal F2 adapter。

Akochan F1 审计已完成，当前结论为 Conditional Pass：仓库公开且 JSON/mjai/log/legal-action 入口有价值，未发现外部神经网络权重需求；修正后的 GitHub Actions Ubuntu workflow run `26617347785` 成功生成 `libai.so` 和 `system.exe`，并跑通最小 `legal_action` 与 `mjai_log haifu_log_sample.json 0 2` 样例。

Conditional 的原因：Akochan license 是 custom Japanese usage agreement，修改、再分发、商业或公开发布仍需要复审/许可；本机 macOS build 仍未通过，当前可复现证据来自 Ubuntu GitHub Actions runner。

F2 task definition 已写入 `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`。最小 wrapper skeleton 已实现，并通过 fake executable smoke tests；该 fake executable 只是测试替身，不是真实 Akochan，也不是强度证据。

真实 external `system.exe` 验证路径已新增：`.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` 会在临时 Ubuntu runner 中构建 Akochan，并用 `tests/adapters/test_akochan_wrapper_real_exe.py` 调用真实 runner-temp `system.exe`。

首个 workflow run `26621536548` 已复审：构建、fake wrapper tests 和真实 `legal_action` wrapper test 通过；真实 `mjai_log` wrapper test 失败，因为 Akochan 运行时需要从 process working directory 读取 `setup_mjai.json`。

本地 wrapper cwd 边界已修复：`AkochanWrapper` 支持显式 `working_dir`、`AKOCHAN_WORKING_DIR` 和默认 `Path(system_exe).resolve().parent`；`subprocess.run` 使用 `cwd=self.working_dir`；audit log 记录 `working_dir`。workflow run `26623247276` 证明 `setup_mjai.json` blocker 已消失，真实 `legal_action` 继续通过，但真实 `mjai_log` stdout 触发 `JSONDecodeError: Extra data`。workflow run `26628128871` 进一步证明 strict JSON stream parser 能解析前段 JSON records，但真实 stdout 还包含白名单状态行 `calculating review` 和后续 JSON review output。本地 parser 已支持 single JSON、JSON Lines、concatenated JSON values、pretty-printed multi-record JSON stream，以及只跳过 exactly `calculating review` 的 allowlisted mixed stdout；unknown non-JSON line 和 partial parse 仍必须失败。workflow run `26629344590` 已成功验证该路径：Ubuntu runner 成功构建 `ai_src/libai.so`、root `libai.so` 和 `system.exe`，fake wrapper tests 14 tests passed，real `legal_action` 和 real `mjai_log` 均通过。该证据只说明 fixed-sample wrapper/integration 可行，不是 Akochan 或 mjlabai 强度证据。下一步只允许 implement P5 synthetic legal-action metric evaluator for project-authored fixture only；仍然不训练、不调参、不自我对弈、不跑 league、不接入 Tenhou、不 vendor 或上传第三方源码、二进制、`params/` 或未知 artifact。
