# 09_PLATFORM_COMPLIANCE

## Purpose

Document what the project may and may not do around Tenhou or any third-party platform.

## Default allowed path

1. Offline replay analysis.
2. Self-contained simulator.
3. Self-play evaluation.
4. Human-reviewed strategy analysis.
5. Compliance-reviewed external testing only after explicit approval.

## Default prohibited path

- Unauthorized automated play.
- Anti-detection, account evasion or captcha/rate-limit bypass.
- Credential storage in repo.
- Unauthorized scraping or redistribution.
- Any instruction whose purpose is to bypass platform rules.

## Before any platform integration

| Check | Pass? | Evidence |
|---|---|---|
| Platform rules reviewed | | |
| Allowed use documented | | |
| No evasion logic included | | |
| No secrets committed | | |
| Human approval recorded | | |
