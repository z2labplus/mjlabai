# 07J_AKOCHAN_F2_INTERFACE_TASK

## Scope

Date: 2026-05-29.

Stage:

```text
P3 / baseline reproducibility audit
Akochan = F2 interface/legal-action adapter task definition
```

North-star link:

```text
This task supports the LuckyJ 10.68 target by defining a controlled baseline/reviewer interface before any training, league evaluation or Tenhou-like strength claim.
```

This document first defined the F2 task boundary. It now also records the result of the first minimal wrapper-skeleton implementation.

## A. F2 Goal

Akochan's project role:

1. Legal-action checker.
2. mjai/log reviewer.
3. Baseline/reviewer candidate.

Non-goals:

- Not a strength proof.
- Not a training route.
- Not a self-play route.
- Not a real Tenhou integration.
- Not platform automation.
- Not a claim that Akochan is stronger than any baseline.

F2 exists to make Akochan callable through a narrow, auditable wrapper boundary so future evaluation work can compare legal-action behavior and reviewer outputs without copying Akochan into this repository.

## B. F2 Minimal Scope

Allowed future F2 implementation scope:

- Define and implement a minimal wrapper skeleton only.
- Call fixed non-training commands against a temporary external Akochan build.
- Use fixed samples only:
  - Minimal `legal_action` JSON.
  - Fixed `haifu_log_sample.json` / mjai-log sample.
- Record command metadata and short output summaries.

Inputs:

- mjai-compatible JSON.
- Fixed sample log.
- Decision state derived from audited test fixtures.

Outputs:

- Legal actions JSON.
- Parsed `mjai_log` result.
- Command status.
- stdout summary.
- stderr summary.
- Latency.
- Reproducibility metadata.

Forbidden in F2:

- No real Tenhou connection.
- No self-play.
- No match league.
- No training.
- No hyperparameter tuning.
- No unknown model weights.
- No platform automation, scraping, account tooling, evasion or anti-detection logic.
- No third-party source vendoring.
- No third-party binary or build-artifact upload.

## C. Interface Boundary

Akochan source and `system.exe` must not enter this repository.

Allowed boundary:

- The wrapper may call an external Akochan path supplied by configuration or environment variable.
- The wrapper may run in GitHub Actions after building Akochan in the runner temporary directory.
- The wrapper may consume fixture JSON and logs stored in this repository only if those fixtures are original project fixtures or minimal synthetic samples, not copied third-party source or large third-party logs.
- The wrapper may write small audit logs produced by this project.

Repository may store:

- Wrapper code in a future implementation task.
- Schema definitions.
- Small synthetic test samples.
- Smoke tests.
- Audit-log examples produced by this project.
- Documentation.

Repository must not store:

- Akochan source.
- Akochan `system.exe`.
- `libai.so`.
- Akochan `params/` copies.
- Third-party binaries.
- Unknown model artifacts.
- Large raw logs.

Expected future configuration keys:

```text
AKOCHAN_ROOT
AKOCHAN_SYSTEM_EXE
AKOCHAN_COMMIT
AKOCHAN_BUILD_ENV
```

These names are a draft for the next implementation task, not code.

## D. State / Action Mapping Draft

Future wrapper must accept or preserve these mjai event types:

| Event type | Purpose in mapping |
|---|---|
| `start_game` | Initialize names, red-five flag and game metadata. |
| `start_kyoku` | Initialize round wind, hand tiles, scores, honba, kyotaku, oya and dora marker. |
| `tsumo` | Add draw event and identify acting player. |
| `dahai` | Record discard action and tsumogiri flag. |
| `chi` | Record call action and consumed tiles. |
| `pon` | Record call action and consumed tiles. |
| `kan` | Record kan action, actor and tile group. |
| `reach` | Record riichi declaration and step if present. |
| `hora` | Record win result, actor, target and score deltas if present. |
| `ryukyoku` | Record drawn hand result and tenpai/no-ten status if present. |
| `end_kyoku` | Mark round boundary. |

Draft internal action schema:

```json
{
  "source": "akochan",
  "action_type": "dahai",
  "actor": 0,
  "tile": "1s",
  "tsumogiri": true,
  "raw": {
    "actor": 0,
    "pai": "1s",
    "tsumogiri": true,
    "type": "dahai"
  }
}
```

Draft legal-action list schema:

```json
{
  "tool": "akochan_legal_action",
  "actions": [
    {
      "source": "akochan",
      "action_type": "dahai",
      "actor": 0,
      "tile": "1s",
      "tsumogiri": true,
      "raw": {
        "actor": 0,
        "pai": "1s",
        "tsumogiri": true,
        "type": "dahai"
      }
    }
  ]
}
```

Mapping rules for next implementation:

- Preserve the raw Akochan action in `raw`.
- Normalize mjai `pai` to internal `tile`.
- Normalize mjai `type` to internal `action_type`.
- Reject outputs that are not parseable JSON.
- Do not infer hidden information.
- Do not evaluate move strength.

## E. Audit Log Schema

Every future wrapper call must record:

| Field | Required | Notes |
|---|---|---|
| `tool_name` | Yes | Example: `akochan_legal_action` or `akochan_mjai_log`. |
| `external_repo` | Yes | `https://github.com/critter-mj/akochan.git`. |
| `external_commit` | Yes | Current F1 commit: `53188a0b926fbab38177f88c3cd87d554cf412af`. |
| `build_environment` | Yes | Example: `github-actions ubuntu-latest`. |
| `command` | Yes | Full command without secrets. |
| `input_hash` | Yes | SHA256 of wrapper input. |
| `output_hash` | Yes | SHA256 of raw stdout or normalized output. |
| `exit_code` | Yes | Process exit code. |
| `stdout_summary` | Yes | Short bounded summary only. |
| `stderr_summary` | Yes | Short bounded summary only. |
| `elapsed_ms` | Yes | Wall-clock elapsed time in milliseconds. |
| `training_related` | Yes | Must be `false`. |
| `self_play_related` | Yes | Must be `false`. |
| `tenhou_related` | Yes | Must be `false`. |
| `license_note` | Yes | Must mention custom license and private/internal audit boundary. |
| `reproducibility_note` | Yes | Must include commit, runner/toolchain and artifact handling. |

Draft audit log object:

```json
{
  "tool_name": "akochan_legal_action",
  "external_repo": "https://github.com/critter-mj/akochan.git",
  "external_commit": "53188a0b926fbab38177f88c3cd87d554cf412af",
  "build_environment": "github-actions ubuntu-latest",
  "command": "./system.exe legal_action <json>",
  "input_hash": "<sha256>",
  "output_hash": "<sha256>",
  "exit_code": 0,
  "stdout_summary": "<bounded summary>",
  "stderr_summary": "<bounded summary>",
  "elapsed_ms": 0,
  "training_related": false,
  "self_play_related": false,
  "tenhou_related": false,
  "license_note": "Akochan custom license; private/internal audit only.",
  "reproducibility_note": "Akochan built outside this repository at fixed commit; no third-party source or binary stored."
}
```

## F. License Guardrails

Akochan custom-license restrictions remain active.

Current allowed project use:

```text
Private research / internal audit only.
```

Before any broader use, require license review or author permission for:

- Source modification.
- AI-part modification.
- Redistribution.
- Binary publication.
- Commercial use.
- Public release.

F2 implementation guardrails:

- Do not vendor Akochan source.
- Do not publish Akochan binaries.
- Do not upload `system.exe`, `libai.so` or `params/`.
- Do not present Akochan as a mjlabai-owned component.
- Prefer wrapper code that shells out to an externally provided path.
- Keep attribution and license notes in audit logs and documentation.

## G. F2 Acceptance Criteria

This task definition is complete when:

- This document exists.
- The F2 goal, boundary, schema, logging and license guardrails are documented.
- `docs/10_next/10_NEXT.md` points to the minimal F2 implementation task.
- No adapter code was written in this task.

Future F2 implementation acceptance criteria:

- Akochan can be rebuilt on GitHub Actions Ubuntu runner, or called from a temporary external build path produced in the runner.
- Fixed `legal_action` JSON returns a parseable legal action list.
- Fixed `mjai_log` sample returns parseable output.
- Wrapper has a unit test or smoke test.
- Audit log schema is written by the wrapper.
- No training command is executed.
- No self-play or match command is executed.
- No real Tenhou connection is opened.
- No third-party source, binary, weight or unknown artifact is stored in this repository.
- No build artifact is uploaded.

Implementation status on 2026-05-29:

- Minimal wrapper skeleton implemented in `src/mjlabai/adapters/akochan_wrapper.py`.
- Supported wrapper methods:
  - `run_legal_action(input_json)`.
  - `run_mjai_log(log_path, actor=0, mode=2)`.
- Wrapper executable path must be explicit through constructor argument or `AKOCHAN_SYSTEM_EXE`.
- Wrapper exposes no free-form command execution API.
- Synthetic fixtures and a fake executable were added under `tests/fixtures/akochan/`.
- The fake executable is a test substitute only; it is not Akochan and is not strength evidence.
- Local test command `python3 -m unittest tests/adapters/test_akochan_wrapper.py` passed 4 tests.
- No Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary, unknown model artifact or build artifact was stored in this repository.

## H. F2 Failure Conditions

F2 implementation must fail or stop if:

- It requires vendoring Akochan source into this repository.
- It requires saving third-party binaries in this repository.
- License boundary is unclear for the intended use.
- It triggers training.
- It triggers self-play or match execution.
- It connects to real Tenhou.
- It creates platform automation, scraping, account tooling, evasion or anti-detection logic.
- Output is not parseable.
- The build or command path is not reproducible.
- It relies on unknown model weights or artifacts.

## I. Next-Step Recommendation

Recommended next `docs/10_next/10_NEXT.md` first task:

```text
Run Akochan F2 wrapper against real GitHub Actions Ubuntu-built system.exe for fixed legal_action/mjai_log samples, without uploading third-party binaries or artifacts.
```

Reason:

- F1 has Conditional Pass evidence from Ubuntu GitHub Actions run `26617347785`.
- The F2 interface boundary, state/action mapping, audit log schema and license guardrails are now defined.
- The minimal wrapper skeleton passed fake-executable smoke tests.
- The next evidence gap is real external `system.exe` compatibility for fixed samples, still under no-vendor, no-training and no-Tenhou constraints.

Review note:

```text
Web ChatGPT Pro / legal review is not required to write the private/internal wrapper skeleton,
but is required before modification, redistribution, commercial use, public release or treating Akochan as a public product component.
```
