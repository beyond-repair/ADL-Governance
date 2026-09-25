# Portfolio State (Locked)

**As of:** 2026-09-24 (post Sweep-163 / Sweep-164 discovery)

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
| Digital_Double_virtual_workforce | ACTIVE | Public canonical; CI green; Dependabot HIGH + evidence PR #7 open (operator) |
| sovereign-clean-room | ACTIVE | Canonical SEEM substrate; CI green; VSA completeness UNVERIFIED |
| BlockSwarm | ACTIVE | SAGF; Foundry success; tag PENDING operator |
| ADL-Governance | ACTIVE / MAINTAIN | Registry + constitution (this repo); census refreshed Sweep-164 |
| ADL-SEEM | ACTIVE | SEEM-specific constitution |
| coherence-drive + satellites | RESEARCH | Claim discipline; Stage-1 symbolic INPUT-COMPLETE; no lab thrust claim |
| momentum-closure | RESEARCH | Claim-cap refreshed Sweep-158; pytest CI success |
| ADL-Nexus | RESEARCH | Re-confirmed Sweep-163; CI green |
| CFTv3.3-IQG-Unified-Framework | RESEARCH | Re-confirmed Sweep-162; docs-ci success |
| m2-renormalization-law | RESEARCH | Re-confirmed Sweep-161; parameter-free + pytest CI success |
| SEEM / legacy bots / CFT-v3.1 / Digital Double predecessors | SUPERSEDED / ARCHIVED targets | archive_queue.md; GitHub flags mostly PENDING operator |

## Live census

- GitHub `user:beyond-repair` search total_count: **77** (2026-09-24)
- adl-capability-matrix locked inventory: 67 rows (expansion OPEN / operator-gated)

## Rules

- Automated completion sweeps **skip** forge-aegis implementation while status is RELEASE_BLOCKED_BY_OPERATOR.
- CHANGE → IMPLEMENT → TEST → CI → DOCUMENT → REGISTRY → RELEASE/ARCHIVE
- Claim levels strictly enforced; documentation ≠ implementation; never fabricate verification.
- Operator-only: GitHub archive flags, release tags, Dependabot merges, secret rotation, claim elevation.
