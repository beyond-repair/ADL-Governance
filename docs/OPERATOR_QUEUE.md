# Operator Queue

**Last updated:** 2026-09-05T01:48Z EDT (Sweep-055 — release readiness)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Operator must run the commands below on a machine with push rights.

## Immediate (P0) — Ready for Operator Release

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See below | **READY** |
| Tag + Release | **forge-aegis** | See below | **READY** (CI green; RELEASE_GATE functional boxes complete) |
| Tag (optional) | **sovereign-clean-room** | See below | **READY** (CI green) |
| Archive batch | See archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### BlockSwarm — v0.5.0-sagf (highest priority)

```bash
git clone https://github.com/beyond-repair/BlockSwarm.git && cd BlockSwarm
git checkout main && git pull
git tag -a v0.5.0-sagf -m "SAGF production candidate — B1–B2b-3 complete"
git push origin v0.5.0-sagf
gh release create v0.5.0-sagf --title "v0.5.0-sagf" --notes-file docs/CHANGELOG.md
```

### forge-aegis — v0.1.0

```bash
git clone https://github.com/beyond-repair/forge-aegis.git && cd forge-aegis
git checkout main && git pull
# confirm latest CI green on Actions
git tag -a v0.1.0 -m "forge-aegis v0.1.0 deterministic validation vertical slice"
git push origin v0.1.0
gh release create v0.1.0 --title "v0.1.0" --notes "Deterministic offline validation vertical slice. See docs/RELEASE_GATE_v0.1.md and docs/V0_1_VERTICAL_SLICE.md."
```

### sovereign-clean-room — optional first tag

```bash
git clone https://github.com/beyond-repair/sovereign-clean-room.git && cd sovereign-clean-room
git checkout main && git pull
git tag -a v1.3.0 -m "Sovereign Clean-Room VSA Core v1.3 Hyperspherical — CI green"
git push origin v1.3.0
gh release create v1.3.0 --title "v1.3.0" --notes "CI green. FHRR engine + gated skills. See README."
```

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready; next vertical slice | OPEN |
| Bump PyNaCl | sovereign-clean-room | Optional `>=1.6.2` after tag | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH; partially mapped by os-family-constitution-map | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | CI green; prepare CHANGELOG + tag when product lockfile stable | OPEN |

## ACTIVE Set — Launch Status (Sweep-055)

| Repo | CI | Tags | Launch Ready | Notes |
|------|----|------|--------------|-------|
| BlockSwarm | GREEN | none | **YES — tag now** | Release notes present |
| forge-aegis | GREEN | none | **YES — tag now** | Vertical slice complete |
| sovereign-clean-room | GREEN | none | **YES** | Optional first tag |
| Digital_Double_virtual_workforce | GREEN | none | Near | Lockfile Dependabot still open |
| sunder | pending first CI | none | Runtime live | Claim-capped; not product release |
| ADL-Governance | docs | n/a | YES | Governing source |
| Mapping / Census layer (9) | n/a | none | **NO** | Claim-capped metadata only — do not product-release |

## Explicit Non-Release

- All RESEARCH / claim-capped mapping adapters (aegis-repo-graph, adl-*, seem-*, os-family-*, sunder-cleanroom-vsa-adapter)
- Game prototypes (Project-Cold-Boot, blacksite)
- Physics satellites (coherence-drive lineage)
- SUPERSEDED / FROZEN / archive-queue targets

## Completed (recent)

- **Sweep-055:** Release readiness matrix + precise operator commands. Confirmed CI green on BlockSwarm, forge-aegis, sovereign-clean-room. API cannot create tags.
- **Sweep-052:** Profile master-pro cover; census 73; mapping layer registered.
- **Sweep-054:** Created sunder.
- **Sweep-053:** ACTIVE accuracy + CI green confirmed.

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
**Truth rule:** No false information. Claim levels enforced.
**Tooling limit:** GitHub connected tools lack create_tag / create_release. Operator executes the commands above.
