# 02D_DATA_QUALITY_AUDIT

| Check | Pass? | Notes |
|---|---|---|
| Legal action reconstruction works | | |
| Tile count invariants hold | | |
| Round outcomes match replay | | |
| Train/val/test split avoids leakage | | |
| High-dan subset identifiable | | |
| Rule variants tracked | | |
| Data rights documented | | |

## Failure rule

If legal actions or round outcomes cannot be reconstructed reliably, do not train on the dataset.
