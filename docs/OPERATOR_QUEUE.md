# Operator Queue

**Last updated:** 2026-09-07T04:00Z (Sweep-100 — adl-capability-matrix)

Destructive or account-level actions that require a human operator. Agent records; does not execute.

## Immediate (P0)

| Action | Repo | Status |
|--------|------|--------|
| Rotate + remove committed `.env` | digital-double-mobile | **OPEN** |
| Tag + Release v0.5.0-sagf | BlockSwarm | READY |
| Tag + Release v0.1.0 | forge-aegis | READY |
| Review merge/reject Dependabot #5 / #6 | Digital_Double_virtual_workforce | **OPEN** |
| `gh repo archive beyond-repair/smart_home_BCI --yes` | smart_home_BCI | **PENDING** |
| `gh repo archive` remainder of archive_queue | archive_queue | PENDING |

## Medium (documentation / census)

| Action | Repo | Status |
|--------|------|--------|
| Refresh capability_matrix.json to live census (75) with verified cluster/cap per new row | adl-capability-matrix | **OPEN** (Sweep-100 documented drift; do not invent rows) |
| Optional tag v0.1.0 after green CI | adl-capability-matrix | PENDING |
| Optional tag v0.1.0 | aegis-repo-graph | PENDING |

## High-risk / do-not-implement

| Item | Reason |
|------|--------|
| Fabricate matrix rows for unenumerated repos | Unsupported metadata claim |
| Implement missing `bci` / `SmartHome` in smart_home_BCI | ARCHIVED |
| Execute smart_home_BCI against live LAN | Hard-coded unlock path |
| Elevate Coherence Drive / physics novelty claims | Claim level ≤1 |
| Delete any repository / rewrite history | Immutable |
| Treat RESEARCH census tools as ACTIVE products | Wrong lifecycle |

## Closed this cycle (Sweep-100)

| Action | Notes | Status |
|--------|-------|--------|
| Random select + audit adl-capability-matrix | RESEARCH; CLAIM_STATUS + README drift | **DONE** |
| Governance docs update | SWEEP_HISTORY, PORTFOLIO_STATUS_REPORT, this file | **DONE** |

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes. Never invent inventory rows without a fresh enumeration.
