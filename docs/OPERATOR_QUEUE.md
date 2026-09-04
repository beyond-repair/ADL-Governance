# Operator Queue

**Last updated:** 2026-09-04T18:15Z UTC (Sweep-053 — Accuracy + Launch Readiness)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0 / Critical)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` then publish GitHub Release | PENDING |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Tag forge-aegis v0.1.0 | forge-aegis | After RELEASE_GATE checklist; CI green | OPEN |
| Bump PyNaCl | sovereign-clean-room | Pin `>=1.6.2` (current 1.5.0 works; optional) | OPEN |
| Classify / consolidate | RealityOS, LegionOS, Sovereign-OS, SovereignOS | RESEARCH; prefer one constitutional-OS surface | OPEN |
| Claim gate ExoAxis-1 / blacksite / Project-Cold-Boot | — | RESEARCH until tests+CI | OPEN |
| Bump Digital Double lockfile deps | Digital_Double_virtual_workforce | Dependabot queued | OPEN |

## ACTIVE Set — Accuracy & Launch Status (Sweep-053)

| Repo | CI | Code Review | Truth-to-Source | Launch Ready |
|------|----|-------------|-----------------|--------------|
| sovereign-clean-room | **GREEN** | Path A static engine verified; no leftover partials; Gate.vsa + codebook_stats present | Accurate (operator-authorized reconstruction) | **YES** (runnable) |
| forge-aegis | **GREEN** | Deterministic pipeline intact | Accurate | **YES** (v0.1 slice) |
| BlockSwarm | **GREEN** | Foundry tests pass; SAGF invariants documented | Accurate | **YES** — needs tag/release |
| Digital_Double_virtual_workforce | **GREEN** | Canonical product line | Accurate | **YES** |
| ADL-Governance | N/A (docs) | Registry + claim rules current | Accurate | **YES** |

## Medium

| Action | Notes |
|--------|-------|
| Profile README refresh | Point at ACTIVE set only |
| Archive remaining FROZEN/legacy per registry | After markers verified |
| Isolate or merge private Digital_Double_Virtual_Workforce_4.2 | Public smoke CI is green |

## Completed (recent)

- **Sweep-053:** Full ACTIVE accuracy review. All four engineering surfaces CI-green. VSA engine, Gate, Jump-Start, BaNEL, pruning confirmed present and tested. No false claims introduced by aesthetic READMEs. Leftover loader files confirmed deleted.
- **Sweep-052:** pytest in requirements, workflow hardened, leftovers deleted.
- **Sweep-051b:** Operator-authorized VSA reconstruction.

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
**Truth rule:** No false information. Claim levels enforced. Research stays RESEARCH.
