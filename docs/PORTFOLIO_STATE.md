# Portfolio State (Locked)

**As of:** 2026-08-23

## Priority queue

1. **Digital Double** — NEXT BUILD (consolidate / run path / CI)
2. sovereign-clean-room — stabilize
3. BlockSwarm — operator release tag
4. forge-aegis — **RELEASE_BLOCKED_BY_OPERATOR** (implementation FROZEN)
5. Governance / research / archive — maintenance

## System status

| System | Status | Notes |
|--------|--------|-------|
| forge-aegis | RELEASE_BLOCKED_BY_OPERATOR | Slice+CI+gate done; wait for remote `v0.1.0`; **no FLS expansion** |
| AEGIS-Nehemiah | CONTRACT CONSUMER | Must not redefine validation semantics |
| Digital_Double_virtual_workforce | NEXT BUILD | Canonical public target |
| sovereign-clean-room | STABILIZE | CI / docs |
| BlockSwarm | RELEASE / MAINTAIN | Tag `v0.5.0-sagf` operator |
| ADL-Governance | MAINTAIN | Registry |
| coherence-drive + satellites | RESEARCH | Claim discipline |
| SEEM / legacy bots | SUPERSEDED / ARCHIVE | archive_queue.md |

## Rules

- Automated completion sweeps **skip** forge-aegis implementation while status is RELEASE_BLOCKED_BY_OPERATOR.
- CHANGE → IMPLEMENT → TEST → CI → DOCUMENT → REGISTRY → RELEASE/ARCHIVE
