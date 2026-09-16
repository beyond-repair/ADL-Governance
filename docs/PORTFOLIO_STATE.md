# Portfolio State (Locked)

**As of:** 2026-09-16 (post Sweep-148)

## Priority queue

1. **Digital_Double_virtual_workforce** — ACTIVE (docs/CI/SECURITY terminal; release tags + Dependabot/evidence PRs operator)
2. sovereign-clean-room — ACTIVE (stabilize; VSA completeness UNVERIFIED)
3. BlockSwarm — ACTIVE (operator release tag v0.5.0-sagf)
4. forge-aegis — ACTIVE / RELEASE_BLOCKED_BY_OPERATOR (implementation FROZEN; wait for remote v0.1.0; no FLS expansion)
5. Governance / research / archive — maintenance (registry + claim discipline)

## System status

| System | Status | Notes |
|--------|--------|-------|
| forge-aegis | RELEASE_BLOCKED_BY_OPERATOR | Slice+CI+gate done; wait for remote `v0.1.0`; **no FLS expansion** |
| AEGIS-Project-Nehemiah- | CONTRACT CONSUMER / ACTIVE | Must not redefine validation semantics |
| Digital_Double_virtual_workforce | ACTIVE | Public canonical; CI green; Dependabot HIGH + evidence PR open (operator) |
| sovereign-clean-room | ACTIVE | Canonical SEEM substrate; CI green; VSA completeness UNVERIFIED |
| BlockSwarm | ACTIVE | SAGF; Foundry success; tag PENDING operator |
| ADL-Governance | ACTIVE / MAINTAIN | Registry + constitution (this repo) |
| ADL-SEEM | ACTIVE | SEEM-specific constitution |
| coherence-drive + satellites | RESEARCH | Claim discipline; Stage-1 symbolic INPUT-COMPLETE; no lab thrust claim |
| SEEM / legacy bots / CFT-v3.1 / Digital Double predecessors | SUPERSEDED / ARCHIVED targets | archive_queue.md; GitHub flags mostly PENDING operator |

## Rules

- Automated completion sweeps **skip** forge-aegis implementation while status is RELEASE_BLOCKED_BY_OPERATOR.
- CHANGE → IMPLEMENT → TEST → CI → DOCUMENT → REGISTRY → RELEASE/ARCHIVE
- Claim levels strictly enforced; documentation ≠ implementation; never fabricate verification.
- Operator-only: GitHub archive flags, release tags, Dependabot merges, secret rotation, claim elevation.
