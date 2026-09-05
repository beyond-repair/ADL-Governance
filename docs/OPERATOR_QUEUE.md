# Operator Queue

**Last updated:** 2026-09-05T16:55Z (MAINT-001 maintenance drift scan)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See below | READY (CI green run 33949194624) |
| Tag + Release | **forge-aegis** | RELEASE_GATE checklist then tag | READY (CI green 33904082644) |
| Bump PyNaCl ≥1.6.2 | **sovereign-clean-room** | Pin in requirements.txt; re-run Python tests | OPEN (MEDIUM GHSA-mrfv-m5wm-5w6w) |
| Bump lockfile deps | **Digital_Double_virtual_workforce** | nanoid ≥3.3.12 / 5.1.11; re-run CI | OPEN (HIGH GHSA-xwg4-73v4-xw9w) |
| Archive batch | archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### BlockSwarm — v0.5.0-sagf

```bash
git clone https://github.com/beyond-repair/BlockSwarm.git && cd BlockSwarm
git checkout main && git pull
git tag -a v0.5.0-sagf -m "SAGF production candidate — B1–B2b-3 complete"
git push origin v0.5.0-sagf
gh release create v0.5.0-sagf --title "v0.5.0-sagf" --notes-file docs/CHANGELOG.md
```

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Confirm CI green | sovereign-clean-room | **VERIFIED green** MAINT-001 (33904047312) | DONE |
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-* | `os-family-constitution-map` exists; prefer one surface | OPEN |

## Medium

| Action | Notes |
|--------|-------|
| Register new meta-repos in repository_registry.md | census/matrix/graph/adapters/sunder if not complete |
| Profile README → ACTIVE set only | Hygiene |
| VigilE.S.A. optional archive | RESEARCH claim-capped; archive operator-only |

## Completed (recent)

- sovereign-clean-room VSA Path A restore → CI green (operator; confirmed MAINT-001)
- BlockSwarm GOVERNANCE/SECURITY docs (sweep-056)
- thrust-target-30 unit-identity docs (Sweep-063)
- VigilE.S.A. claim-capped docs (Sweep-062)
- forge-aegis continuous green

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
