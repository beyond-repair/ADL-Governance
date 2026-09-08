# Operator Queue

**Last updated:** 2026-09-07T00:10Z (Sweep-117 — BlockSwarm)

Destructive or account-level actions that require a human operator. Agent records; does not execute.

## Immediate (P0)

| Action | Repo | Status |
|--------|------|--------|
| Rotate + remove committed `.env` | digital-double-mobile | **OPEN** |
| Review / patch Dependabot HIGH (browserslist #85, nanoid #83, …) | digital-double-mobile | **OPEN** |
| Tag + Release v0.5.0-sagf | BlockSwarm | READY (last verified CI 33986287866 success; Sweep-117 Foundry re-run PENDING) |
| Tag + Release v0.1.0 | forge-aegis | READY (CI 33904082644 success) |
| Review merge/reject Dependabot #5 / #6 | Digital_Double_virtual_workforce | **OPEN** |
| Review merge/reject PR #7 workforce evidence | Digital_Double_virtual_workforce | **OPEN** (CI 34084870372 success on PR) |
| `gh repo archive beyond-repair/smart_home_BCI --yes` | smart_home_BCI | **PENDING** |
| `gh repo archive beyond-repair/genieGPT --yes` | genieGPT | **PENDING** |
| `gh repo archive` remainder of archive_queue | archive_queue | PENDING |
| Refresh capability_matrix.json to live census (75) with evidence-backed caps | adl-capability-matrix | **OPEN** (do not invent rows) |

## Medium (documentation / census)

| Action | Repo | Status |
|--------|------|--------|
| Confirm Sweep-117 Foundry conclusion | BlockSwarm | **PENDING** |
| Confirm Sweep-116 docs-presence re-run | ware-constant-phenomenology | **PENDING** |
| Confirm Sweep-115 pytest conclusion | adl-capability-matrix | **PENDING** |
| Confirm Sweep-114 pytest conclusion | sierpinski-geometry-045 | **PENDING** |
| Confirm Sweep-113 docs-presence conclusion | momentum-closure | **PENDING** |
| Implement tensor.py + tests before product pytest | momentum-closure | OPEN (do not invent) |
| Confirm first Sweep-112 Actions conclusion | ADL-Nexus | **PENDING** |
| Optional tag after green tests | sovereign-clean-room | READY (CI 33979476402) |

## High-risk / do-not-implement

| Item | Reason |
|------|--------|
| Invent 8 new matrix rows + cluster/cap | Would fabricate metadata claims |
| Invent `tensor.py` or claim pytest-21 | ABSENT |
| Promote ware-constant-phenomenology to ACTIVE | Phenomenology only; no experimental artifacts |
| Promote adl-capability-matrix to ACTIVE | Dated 67-row snapshot; live drift |
| Promote momentum-closure / ADL-Nexus / sierpinski to ACTIVE | Evidence incomplete |
| Delete any repository / rewrite history | Immutable |
| Claim VSA completeness from unit-test CI alone | Insufficient evidence |
| Tag releases without operator review | Operator-gated |
| Treat docs-presence CI as SPARC/χ²/thrust validation | File presence ≠ physics |
| Claim BlockSwarm mainnet / audit / economic security | Claim-capped |

## Closed this cycle (Sweep-117)

| Action | Notes | Status |
|--------|-------|--------|
| Re-audit BlockSwarm | ACTIVE; docs lock; no tag executed | **DONE** (Foundry re-run PENDING) |

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes. Never invent inventory rows without a fresh enumeration.
