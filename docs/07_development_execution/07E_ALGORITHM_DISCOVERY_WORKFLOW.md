# 07E_ALGORITHM_DISCOVERY_WORKFLOW

## Purpose

定义“如何找算法、筛算法、变成 Codex 本地任务”。

## Workflow

### Step 1: Ask a target question

不要问：

```text
有没有更好的麻将 AI 算法？
```

要问：

```text
有哪些算法最可能提升 Tenhou 稳定段位、降低四位率、提升 rank EV，并且可在本项目复现？
```

### Step 2: Build candidate list

每个候选必须记录：

```text
名称
来源
核心方法
已有强度证据
是否适合 Tenhou
可复现程度
需要数据
需要环境
需要算力
主要风险
第一步最小实验
```

### Step 3: Score candidates

使用 `01G_ALGORITHM_SELECTION_PRINCIPLES.md` 的 100 分评分表。

### Step 4: Convert to experiment

候选算法不能直接进入代码。

必须先生成：

```text
实验卡
成功标准
失败标准
评测方法
回滚方法
```

### Step 5: Convert to local Codex task

Codex 任务必须小到可以本地完成。

正确格式：

```text
只实现一个最小模块。
只改明确文件。
必须运行测试。
必须更新文档。
不得跨阶段推进。
```

### Step 6: Evidence update

每次算法讨论后更新：

```text
09_EVIDENCE_LOG.md
09_CHANGELOG.md
10_NEXT.md
```

## Current algorithm discovery backlog

```text
1. 建立算法候选表：Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer。
2. 给每个候选打分。
3. 选出一个最小 baseline 路线。
4. 把 baseline 路线拆成 Codex 可执行任务。
```
