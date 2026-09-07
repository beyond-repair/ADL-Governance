# Operator Queue

**Last updated:** 2026-09-07T14:10Z (Sweep-102 — census + Phase-3 re-verify)

Destructive or account-level actions that require a human operator. Agent records; does not execute.

## Immediate (P0)

| Action | Repo | Status |
|--------|------|--------|
| Rotate + remove committed `.env` | digital-double-mobile | **OPEN** |
| Tag + Release v0.5.0-sagf | BlockSwarm | READY (CI 33986287866 success) |
| Tag + Release v0.1.0 | forge-aegis | READY (CI 33904082644 success) |
| Review merge/reject Dependabot #5 / #6 | Digital_Double_virtual_workforce | **OPEN** |
| Review merge/reject PR #7 workforce evidence | Digital_Double_virtual_workforce | **OPEN** (CI 34084870372 success on PR) |
| `gh repo archive beyond-repair/smart_home_BCI --yes` | smart_home_BCI | **PENDING** |
| `gh repo archive` remainder of archive_queue | archive_queue | PENDING |

## Medium (documentation / census)

| Action | Repo | Status |
|--------|------|--------|
| Refresh capability_matrix.json to live census (75) with verified cluster/cap per new row | adl-capability-matrix | **OPEN** (do not invent rows) |
| Optional tag v0.1.0 after green CI | adl-capability-matrix | PENDING |
| Optional tag v0.1.0 | aegis-repo-graph | PENDING |
| Optional tag after green tests | sovereign-clean-room | READY (CI 33979476402) |
| Add docs CI to ADL-Governance | ADL-Governance | OPTIONAL |

## High-risk / do-not-implement

| Item | Reason |
|------|--------|
| Fabricate matrix rows for unenumerated repos | Unsupported metadata claim |
| Implement missing `bci` / `SmartHome` in smart_home_BCI | ARCHIVED |
| Execute smart_home_BCI against live LAN | Hard-coded unlock path |
| Elevate Coherence Drive / physics novelty claims | Claim level ≤1 |
| Delete any repository / rewrite history | Immutable |
| Treat RESEARCH census tools as ACTIVE products | Wrong lifecycle |
| Claim VSA completeness from unit-test CI alone | Insufficient evidence |

## Closed this cycle (Sweep-102)

| Action | Notes | Status |
|--------|-------|--------|
| Live re-verify four ACTIVE product repos | CI green; releases empty; advisories empty | **DONE** |
| Re-enumerate public census | search total_count 75; names published in PORTFOLIO_STATUS_REPORT | **DONE** |
| Governance docs update | PORTFOLIO_STATUS_REPORT, SWEEP_HISTORY, this file | **DONE** |

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes. Never invent inventory rows without a fresh enumeration.
