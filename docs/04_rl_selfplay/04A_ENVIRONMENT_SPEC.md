# 04A_ENVIRONMENT_SPEC

| Component | Requirement | Status |
|---|---|---|
| Legal action engine | Must exactly enforce rules | Planned |
| Scoring engine | Must match target ruleset | Planned |
| Hidden information | Must not leak unseen tiles | Planned |
| Opponent policies | Support league/self-play opponents | Planned |
| Logging | Full decision trace reproducible | Planned |

## Invalid environment examples

- Hidden tiles leaked to the policy.
- Scoring does not match target Tenhou rules.
- Legal actions differ from real riichi rules.
- Opponents are too weak to expose high-dan mistakes.
