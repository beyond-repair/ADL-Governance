# Operator Queue

**Last updated:** 2026-09-03T12:47Z EDT (Sweep-049)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0 / Critical)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| **Restore VSA engine for CI** | sovereign-clean-room | Missing `core/_vsa_b64_5.txt`, `_vsa_b64_6.txt`, `_vsa_b64_7.txt` (loader uses `range(9)`). Present: 0–4, 8 (1–3 are 12-byte placeholders; 4 and 8 are identical 904B blobs). Leftover `_vsa_part_{0,1,2}.py` unused by current loader. Options: (A) add the three missing base64 chunks so join succeeds, or (B) replace `clean_room_vsa.py` with a single full source module and delete part-loader + partial txts. **Preferred path now formalized in ADL-SEEM `docs/LOADER_HARDENING.md` (Path A = static module).** Re-run Actions after. Halt maturity claims until green. Do **not** invent engine source. | **CRITICAL — reconfirmed Sweep-049** |
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` then publish GitHub Release | PENDING (tags=[], releases=[]) |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Confirm CI green on main | forge-aegis | **VERIFIED green** (Sweep-002…049) | DONE |
| Confirm CI green + CLI stable | sovereign-clean-room | **FAILED** — missing b64 chunks 5–7 | OPEN |
| Decide product canonical | Digital_Double_* family | Public: Digital_Double_virtual_workforce; private 4.2 is newer candidate | DECIDED |
| Confirm public Digital Double CI | Digital_Double_virtual_workforce | Latest “Digital Double CI” **32707099628 success** | DONE (Sweep-010–049) |
| Classify / consolidate | RealityOS, LegionOS, Sovereign-OS, SovereignOS | Registered RESEARCH; prefer one constitutional-OS surface | OPEN |
| Tag forge-aegis v0.1.0 | forge-aegis | After RELEASE_GATE checklist; tags currently empty | OPEN |
| Bump PyNaCl | sovereign-clean-room | Dependabot #1 medium: PyNaCl < 1.6.2 (GHSA-mrfv-m5wm-5w6w / CVE-2025-69277). Pin `>=1.6.2` after VSA restore so CI can prove the bump. | OPEN |
| Claim gate ExoAxis-1 | ExoAxis-1 | README-only RESEARCH. Do not promote ACTIVE until tests+CI exist. Keep claim level ≤1. | OPEN (registered Sweep-041) |
| Claim gate blacksite | blacksite | Private JS prototype created 2026-09-02 (last push 2026-09-03). Zero workflows. Do not promote ACTIVE until tests+CI exist. Keep claim level ≤1. | OPEN (registered Sweep-048) |
| Claim gate Project-Cold-Boot | Project-Cold-Boot | Public GDScript prototype created 2026-09-03. Zero workflows. Do not promote ACTIVE until tests+CI exist. Keep claim level ≤1. Optional: add SECURITY.md + governance pointer if it remains. | OPEN (registered Sweep-049) |
| Bump Digital Double lockfile deps | Digital_Double_virtual_workforce | Open Dependabot: high brace-expansion (GHSA-3jxr-9vmj-r5cp), js-yaml (GHSA-5p4m-2wfm-xmqj), nanoid (GHSA-28wg-ghj8-5hjv); medium vite/postcss. Dev/lockfile surface. Operator npm bump; do not treat as critical runtime CI. | OPEN (noted Sweep-042/049) |

## Medium

| Action | Notes |
|--------|-------|
| Profile README refresh | Point at ACTIVE set only |
| Archive remaining FROZEN/legacy per registry | After markers verified |
| Isolate or merge private Digital_Double_Virtual_Workforce_4.2 | Public smoke CI is green; 4.2 remains a non-canonical sibling |

## Completed (recent)

- **Sweep-049:** Live re-audit of 64 repos; registered Project-Cold-Boot RESEARCH. Priority-target CI/tags unchanged vs Sweep-048. No archives, no tags, no VSA fabrication.
- **Sweep-048:** Live re-audit of 63 repos; registered blacksite RESEARCH. Priority-target CI/tags unchanged vs Sweep-047. No archives, no tags, no VSA fabrication.
- **Sweep-047:** Live re-audit of 62 repos; no new names. Priority-target CI/tags unchanged vs Sweep-046. No archives, no tags, no VSA fabrication.
- **Sweep-046:** Live re-audit of 62 repos; no new names. Priority-target CI/tags unchanged vs Sweep-045. No archives, no tags, no VSA fabrication.
- **Sweep-039:** ADL-SEEM `docs/LOADER_HARDENING.md` added and accepted (Path A preferred, Path B exception-only with isolation). Linked from this queue.
- BlockSwarm root cleanup, tests, CI workflow, release docs
- Digital Double role assignment + CANONICAL_REPOS entry (Sweep-008)
- SEEM-* classified SUPERSEDED → sovereign-clean-room
- forge-aegis CI live-verified green (Sweep-002…049)
- Sovereign root-cause pinned to missing `_vsa_b64_5/6/7` (Sweep-003…049)
- New OS family registered RESEARCH (Sweep-007/008)
- Registry census includes potential-garbanzo stub

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
