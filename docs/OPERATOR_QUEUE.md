# Operator Queue

**Last updated:** 2026-09-04T17:28Z UTC (Sweep-052)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0 / Critical)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| **Restore VSA engine for CI** | sovereign-clean-room | **DONE (Sweep-051b/052):** Operator authorized invention. Path A static `CleanRoomVSAEngine` + `CleanRoomGate` + Jump-Start v0.1 + BaNEL + pruning + persistence. Gate.vsa alias + codebook_stats + enable_shacl. Leftover `_vsa_b64_*` / `_vsa_part_*` deleted. pytest added to requirements; workflow simplified. Awaiting final CI green on latest push. | **RESOLVED — confirm CI green** |
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` then publish GitHub Release | PENDING (tags=[], releases=[]) |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Confirm CI green on main | forge-aegis | **VERIFIED green** | DONE |
| Confirm CI green + CLI stable | sovereign-clean-room | Engine + cleanup complete; **CI running** | OPEN |
| Decide product canonical | Digital_Double_* family | Public: Digital_Double_virtual_workforce; private 4.2 is newer candidate | DECIDED |
| Confirm public Digital Double CI | Digital_Double_virtual_workforce | Latest product CI success | DONE |
| Classify / consolidate | RealityOS, LegionOS, Sovereign-OS, SovereignOS | RESEARCH; prefer one constitutional-OS surface | OPEN |
| Tag forge-aegis v0.1.0 | forge-aegis | After RELEASE_GATE checklist; tags currently empty | OPEN |
| Bump PyNaCl | sovereign-clean-room | Pin `>=1.6.2` after CI green | OPEN |
| Claim gate ExoAxis-1 / blacksite / Project-Cold-Boot | — | RESEARCH until tests+CI | OPEN |
| Bump Digital Double lockfile deps | Digital_Double_virtual_workforce | High Dependabot queued | OPEN |

## Medium

| Action | Notes |
|--------|-------|
| Profile README refresh | Point at ACTIVE set only |
| Archive remaining FROZEN/legacy per registry | After markers verified |
| Isolate or merge private Digital_Double_Virtual_Workforce_4.2 | Public smoke CI is green |

## Completed (recent)

- **Sweep-052:** pytest in requirements, workflow hardened, all leftover Path A partials deleted, governance updated.
- **Sweep-051b:** Operator-authorized VSA reconstruction. Full static Path A engine + Gate.vsa alias.
- **Sweep-051:** Path A structural fail-closed module (no source invention yet).
- **Sweep-050…:** prior census / claim gates.

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
