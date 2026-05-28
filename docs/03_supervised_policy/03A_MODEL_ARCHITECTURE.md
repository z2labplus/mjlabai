# 03A_MODEL_ARCHITECTURE

| Version | Architecture | Input representation | Heads | Parameters | Latency | Status |
|---|---|---|---|---:|---:|---|

## Design questions

- Does the model represent all visible state needed for Tenhou play?
- Does it support legal action masking?
- Does it expose value estimates for search or RL?
- Can it run at required inference latency?
