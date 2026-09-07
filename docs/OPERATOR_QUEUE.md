# Operator Queue

**Last updated:** 2026-09-07T22:20Z (Sweep-114 — Phase-3 + residual close)

Destructive or account-level actions that require a human operator. Agent records; does not execute.

## Immediate (P0)

| Action | Repo | Status |
|--------|------|--------|
| Rotate + remove committed `.env` | digital-double-mobile | **OPEN** |
| Review / patch Dependabot HIGH (browserslist #85, nanoid #83, …) | digital-double-mobile | **OPEN** |
| Tag + Release v0.5.0-sagf | BlockSwarm | READY (CI 33986287866 success) |
| Tag + Release v0.1.0 | forge-aegis | READY (CI 33904082644 success) |
| Review merge/reject Dependabot #5 / #6 | Digital_Double_virtual_workforce | **OPEN** |
| Review merge/reject PR #7 workforce evidence | Digital_Double_virtual_workforce | **OPEN** (CI 34084870372 success on PR) |
| Diagnose / fix pytest job `test (3.11)` | ADL-Nexus | **OPEN** (run 34158629167 failure) |
| `gh repo archive beyond-repair/smart_home_BCI --yes` | smart_home_BCI | **PENDING** |
| `gh repo archive beyond-repair/genieGPT --yes` | genieGPT | **PENDING** (Sweep-111 docs lock done) |
| `gh repo archive` remainder of archive_queue | archive_queue | PENDING |

## Medium (documentation / census)

| Action | Repo | Status |
|--------|------|--------|
| Confirm Sweep-113 docs-presence conclusion | momentum-closure | **CLOSED** (34162475153 success) |
| Implement tensor.py + tests before product pytest | momentum-closure | OPEN (do not invent) |
| Confirm first Sweep-112 Actions conclusion | ADL-Nexus | **CLOSED as FAIL** (34158629167) |
| Confirm pytest after Sweep-110 docs push | acoustic-token-modem | PENDING (prior 34068585607 success) |
| Refresh capability_matrix.json to live census (75) | adl-capability-matrix | **OPEN** |
| Optional tag after green tests | sovereign-clean-room | READY (CI 33979476402) |
| Confirm docs-presence success after Sweep-109 repair | The-Origin-Point-Hypothesis. | PENDING |
| Confirm first docs-presence Actions run | ware-constant-phenomenology | PENDING |

## High-risk / do-not-implement

| Item | Reason |
|------|--------|
| Invent `tensor.py` or claim pytest-21 | ABSENT; would fabricate implementation |
| Promote momentum-closure to ACTIVE | Broken import; no tests; no product CI |
| Promote ADL-Nexus to ACTIVE | Product pytest FAILED 34158629167 |
| Treat Gia as ACTIVE agent runtime | SUPERSEDED; successor is sovereign-clean-room |
| Treat acoustic FSK CI as speaker/mic validation | M10 absent |
| Elevate Coherence Drive / physics novelty claims | Claim level ≤1 |
| Delete any repository / rewrite history | Immutable |
| Claim VSA completeness from unit-test CI alone | Insufficient evidence |

## Closed this cycle (Sweep-114)

| Action | Notes | Status |
|--------|-------|--------|
| Close Sweep-113 docs-presence pending | momentum-closure 34162475153 success | **DONE** |
| Confirm Gia SUPERSEDED lock | head 50d30cf8; no product CI; no releases | **DONE** |
| Record Nexus pytest failure | test (3.11) failed; docs-presence passed | **DONE** |

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes. Never invent inventory rows without a fresh enumeration.
