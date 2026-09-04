# Operator Queue

**Last updated:** 2026-09-04T12:52Z EDT (Sweep-051)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0 / Critical)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| **Restore VSA engine for CI** | sovereign-clean-room | **Path A structural step DONE (Sweep-051):** `clean_room_vsa.py` no longer uses `exec(base64…)`. Replaced with static fail-closed module that raises clear ImportError. Leftover `_vsa_b64_*.txt` and `_vsa_part_*.py` remain for operator reference but are unused. **Still required:** supply complete static `CleanRoomVSAEngine` + `CleanRoomGate` + `DEFAULT_PROTECTED_ATOMS` + `jump_start_v01` etc. (full source was never in repo history). Then delete leftover part files. Re-run Actions. Halt maturity claims until green. Do **not** invent engine source. | **CRITICAL — structural Path A applied; full source still missing** |
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` then publish GitHub Release | PENDING (tags=[], releases=[]) |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Confirm CI green on main | forge-aegis | **VERIFIED green** (Sweep-002…051) | DONE |
| Confirm CI green + CLI stable | sovereign-clean-room | **FAILED** — full static engine source still absent | OPEN |
| Decide product canonical | Digital_Double_* family | Public: Digital_Double_virtual_workforce; private 4.2 is newer candidate | DECIDED |
| Confirm public Digital Double CI | Digital_Double_virtual_workforce | Latest “Digital Double CI” **32707099628 success** | DONE (Sweep-010–051) |
| Classify / consolidate | RealityOS, LegionOS, Sovereign-OS, SovereignOS | Registered RESEARCH; prefer one constitutional-OS surface | OPEN |
| Tag forge-aegis v0.1.0 | forge-aegis | After RELEASE_GATE checklist; tags currently empty | OPEN |
| Bump PyNaCl | sovereign-clean-room | Dependabot #1 medium: PyNaCl < 1.6.2 (GHSA-mrfv-m5wm-5w6w / CVE-2025-69277). Pin `>=1.6.2` after VSA restore so CI can prove the bump. | OPEN |
| Claim gate ExoAxis-1 | ExoAxis-1 | README-only RESEARCH. Do not promote ACTIVE until tests+CI exist. Keep claim level ≤1. | OPEN (registered Sweep-041) |
| Claim gate blacksite | blacksite | Private JS prototype created 2026-09-02 (last push 2026-09-03). Zero workflows. Do not promote ACTIVE until tests+CI exist. Keep claim level ≤1. | OPEN (registered Sweep-048) |
| Claim gate Project-Cold-Boot | Project-Cold-Boot | Public GDScript prototype created 2026-09-03; last push 2026-09-04T07:13Z (head `bb564e2a`). Zero workflows. Do not promote ACTIVE until tests+CI exist. Keep claim level ≤1. Optional: add SECURITY.md + governance pointer if it remains. | OPEN (registered Sweep-049; activity Sweep-050) |
| Bump Digital Double lockfile deps | Digital_Double_virtual_workforce | Open Dependabot: high nanoid (GHSA-xwg4-73v4-xw9w / CVE-2026-73086), brace-expansion (GHSA-3jxr-9vmj-r5cp); medium @humanfs/node (GHSA-p498-v437-472g), vite/postcss. Dev/lockfile surface plus nanoid marked runtime in lockfile. Operator npm bump; do not treat as critical runtime CI until product path is shown to invoke vulnerable APIs. | OPEN (noted Sweep-042/050) |

## Medium

| Action | Notes |
|--------|-------|
| Profile README refresh | Point at ACTIVE set only |
| Archive remaining FROZEN/legacy per registry | After markers verified |
| Isolate or merge private Digital_Double_Virtual_Workforce_4.2 | Public smoke CI is green; 4.2 remains a non-canonical sibling |

## Completed (recent)

- **Sweep-051:** Path A structural fix on sovereign-clean-room (`clean_room_vsa.py` → static fail-closed). No engine source invented. Census still 64. Priority CI/tags otherwise unchanged. Governance refresh.
- **Sweep-050:** Live re-audit of 64 repos; no new names. Project-Cold-Boot continued (2026-09-04) but remains RESEARCH / no CI. Priority-target CI/tags unchanged vs Sweep-049. No archives, no tags, no VSA fabrication.
- **Sweep-049:** Live re-audit of 64 repos; registered Project-Cold-Boot RESEARCH. Priority-target CI/tags unchanged vs Sweep-048. No archives, no tags, no VSA fabrication.
- **Sweep-048:** Live re-audit of 63 repos; registered blacksite RESEARCH. Priority-target CI/tags unchanged vs Sweep-047. No archives, no tags, no VSA fabrication.
- **Sweep-039:** ADL-SEEM `docs/LOADER_HARDENING.md` added and accepted (Path A preferred, Path B exception-only with isolation). Linked from this queue.
- BlockSwarm root cleanup, tests, CI workflow, release docs
- Digital Double role assignment + CANONICAL_REPOS entry (Sweep-008)
- SEEM-* classified SUPERSEDED → sovereign-clean-room
- forge-aegis CI live-verified green (Sweep-002…051)
- Sovereign root-cause pinned to missing full engine source (Sweep-003…051)
- New OS family registered RESEARCH (Sweep-007/008)
- Registry census includes potential-garbanzo stub

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
