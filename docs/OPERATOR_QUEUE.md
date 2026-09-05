# Operator Queue

**Last updated:** 2026-09-05T07:08Z (Sweep-059 — live re-verify)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See below | READY (CI green run 33949194624) |
| Tag + Release | **forge-aegis** | See Sweep-055 commands | READY (CI green 33904082644) |
| Bump PyNaCl ≥1.6.2 | **sovereign-clean-room** | Pin in requirements.txt; re-run Python tests | OPEN (MEDIUM GHSA-mrfv-m5wm-5w6w) |
| Bump lockfile deps | **Digital_Double_virtual_workforce** | nanoid ≥3.3.12 / 5.1.11; re-run CI | OPEN (HIGH GHSA-xwg4-73v4-xw9w alerts 153/154) |
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
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | After lockfile bumps | OPEN |
| Light-classify census leftovers | optimization-limit-conjecture, The-Origin-Point-Hypothesis., CFT-v3.1, -Entanglement-and-Emergence, -text-informational-fork-protocol- | RESEARCH default until audited | OPEN |

## Closed this sweep

- **Sweep-059:** Live re-verify of four mandatory targets confirmed Sweep-057/058 Actions IDs still current. No new product CI on those four since last recorded success. No contradiction with live API.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
