# Operator Queue

**Last updated:** 2026-08-27T02:05Z (autonomous Sweep-008)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0 / Critical)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| **Restore VSA engine for CI** | sovereign-clean-room | Missing `core/_vsa_b64_5.txt`, `_vsa_b64_6.txt`, `_vsa_b64_7.txt` (loader uses `range(9)`). Present: 0–4, 8 (some 12-byte placeholders). Options: (A) add the three missing base64 chunks so join succeeds, or (B) replace `clean_room_vsa.py` with a single full source module and delete part-loader + partial txts. Re-run Actions after. Halt maturity claims until green. Do **not** invent engine source. | **CRITICAL — reconfirmed Sweep-008** |
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` then publish GitHub Release | PENDING (tags=[], releases=[]) |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Confirm CI green on main | forge-aegis | **VERIFIED green** (Sweep-002…08) | DONE |
| Confirm CI green + CLI stable | sovereign-clean-room | **FAILED** — missing b64 chunks 5–7 | OPEN |
| Decide product canonical | Digital_Double_* family | Public: Digital_Double_virtual_workforce; private 4.2 is newer candidate | DECIDED (see STATUS) |
| Classify / consolidate | RealityOS, LegionOS, Sovereign-OS, SovereignOS | Registered RESEARCH; prefer one constitutional-OS surface | OPEN |

## Medium

| Action | Notes |
|--------|-------|
| Profile README refresh | Point at ACTIVE set only |
| Archive remaining FROZEN/legacy per registry | After markers verified |
| forge-aegis v0.1.0 release | After RELEASE_GATE_v0.1.md checklist complete |
| Digital Double test/CI on canonical | Verify before maturity 3 |

## Completed (recent)

- BlockSwarm root cleanup, tests, CI workflow, release docs
- Digital Double role assignment + CANONICAL_REPOS entry (Sweep-008)
- SEEM-* classified SUPERSEDED → sovereign-clean-room
- forge-aegis CI live-verified green (Sweep-002…08)
- Sovereign root-cause pinned to missing `_vsa_b64_5/6/7` (Sweep-003…08)
- New OS family registered RESEARCH (Sweep-007/008)
- Registry census 60 repos including potential-garbanzo stub (Sweep-008)

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
