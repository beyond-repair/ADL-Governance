# Operator Queue

**Last updated:** 2026-09-04T20:32Z UTC (Sweep-054 — SUNDER born)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0 / Critical)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` then publish GitHub Release | PENDING |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready; next vertical slice | OPEN |
| Tag forge-aegis v0.1.0 | forge-aegis | After RELEASE_GATE checklist | OPEN |
| Bump PyNaCl | sovereign-clean-room | Optional `>=1.6.2` | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |

## ACTIVE Set — Launch Status

| Repo | CI | Launch Ready |
|------|----|--------------|
| sovereign-clean-room | GREEN | YES |
| forge-aegis | GREEN | YES |
| BlockSwarm | GREEN | YES — needs tag |
| Digital_Double_virtual_workforce | GREEN | YES |
| **sunder** | pending first CI | **YES (v0.1 runtime live)** |
| ADL-Governance | docs | YES |

## Completed (recent)

- **Sweep-054:** Created **sunder** — local-first autonomous coding agent with VSA memory, Constitutional Gate, and Version Forking. SCAN → SNAP → SUNDER loop is runnable.
- **Sweep-053:** ACTIVE accuracy + CI green confirmed.

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
**Truth rule:** No false information. Claim levels enforced.
