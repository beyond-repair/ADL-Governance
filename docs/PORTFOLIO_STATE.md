# Portfolio State (Locked)

**As of:** 2026-10-20 (post Sweep-435, PASS-2026-10-20-435)

## Priority queue

1. **Digital_Double_virtual_workforce** — ACTIVE (CI green; prior critical Dependabot residual closed via issues API)
2. sovereign-clean-room — ACTIVE (stabilize; VSA completeness UNVERIFIED)
3. BlockSwarm — ACTIVE (operator release tag v0.5.0-sagf)
4. forge-aegis — ACTIVE / RELEASE_BLOCKED_BY_OPERATOR (implementation FROZEN; wait for remote v0.1.0; no FLS expansion)
5. Governance / research / archive — maintenance (registry + claim discipline)
6. Unaudited / private remainder — blacksite (RESEARCH, CI green verified Sweep-435), atomicdreamlabs (private), mendthegame (private)

## System status

| System | Status | Notes |
|--------|--------|-------|
| forge-aegis | RELEASE_BLOCKED_BY_OPERATOR | Slice+CI+gate done; wait for remote `v0.1.0`; **no FLS expansion**. Live CI success (Sweep-400) |
| AEGIS-Project-Nehemiah- | CONTRACT CONSUMER / ACTIVE | Must not redefine validation semantics |
| Digital_Double_virtual_workforce | ACTIVE | Public canonical; CI green (Sweep-400); prior Dependabot critical residual now no open issues observed; evidence PR residuals (operator) |
| sovereign-clean-room | ACTIVE | Canonical SEEM substrate; CI green (Sweep-400); VSA completeness UNVERIFIED |
| BlockSwarm | ACTIVE | SAGF; CI success (Sweep-400); tag PENDING operator |
| ADL-Governance | ACTIVE / MAINTAIN | Registry + constitution (this repo); live census 83; PASS-2026-10-20-435 |
| ADL-SEEM | ACTIVE | SEEM-specific constitution |
| blacksite | RESEARCH | Sweep-435: CI green verified (run 39453722349 success); experimental isometric stealth prototype; claim-capped |
| coherence-drive + satellites | RESEARCH | Claim discipline; no lab thrust claim |
| bloch-coherence-factor2 | RESEARCH | Sweep-173; local pytest 11 passed; main Actions success; loop branch not promoted |
| topological-pinch | RESEARCH | Sweep-172; proxy not 0.92; CI success |
| mend | RESEARCH | Sweep-170; formula witness local PASS; playable product NOT verified |
| informational-flux-identity | RESEARCH | Sweep-168; local witness signed net 0 |
| finite-gasket-spectral-derivatives | RESEARCH | Sweep-167; kernel locally tested; mult(6) CLAIMED not machine-verified here |
| momentum-closure | RESEARCH | Claim-cap refreshed Sweep-158; pytest CI success |
| ADL-Nexus | RESEARCH | Re-confirmed; CI green; not product-canonical |
| CFTv3.3-IQG-Unified-Framework | RESEARCH | Re-confirmed; docs-ci success |
| m2-renormalization-law | RESEARCH | Re-confirmed; parameter-free + pytest CI success |
| SEEM-Cognitive-Microservice | SUPERSEDED | Archive flag PENDING |
| SEEM / legacy bots / CFT-v3.1 / Digital Double predecessors | SUPERSEDED / ARCHIVED targets | archive_queue.md; GitHub flags mostly PENDING operator |

## Live census

- GitHub `user:beyond-repair` search total_count: **83** (confirmed stable)
- Prior locked inventory: 67 rows (expansion OPEN / operator-gated)

## Rules

- Automated completion sweeps **skip** forge-aegis implementation while status is RELEASE_BLOCKED_BY_OPERATOR.
- CHANGE → IMPLEMENT → TEST → CI → DOCUMENT → REGISTRY → RELEASE/ARCHIVE
- Claim levels strictly enforced; documentation ≠ implementation; never fabricate verification.
- Operator-only: GitHub archive flags, release tags, Dependabot merges, secret rotation, claim elevation.
- Random selection cycles document RESEARCH state without promotion. blacksite CI now green.
