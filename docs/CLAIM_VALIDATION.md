# Claim Validation Policy

## Levels

| Level | Name | Meaning |
|-------|------|---------|
| 0 | Idea | Informal concept |
| 1 | Mathematical framework | Equations/structure only |
| 2 | Numerical fit | Fits data under stated assumptions |
| 3 | Independent reproduction | Third-party recompute |
| 4 | Experimental evidence | Controlled experiment |
| 5 | Engineering validation | Deployed, measured system |

## Mandatory rules

1. Default for Ware/CFT/IQG/Coherence Drive content: **Level 1** unless higher is evidenced.
2. SPARC-style fits are at most **Level 2**.
3. A green CI, ledger signature, or Merkle proof does **not** raise physics claim level.
4. Energy extraction / thrust / propulsion claims require Level 4+ and explicit measurement protocol.
5. Software readiness (tests, CI) is tracked separately from claim level.

## Canonical Ware law (software + research alignment)

$$
W(n) = 0.08 \, e^{0.23(n-3)}
$$

Conflicting forms (e.g. \(n-1\) indexing without re-normalization) are non-canonical.
