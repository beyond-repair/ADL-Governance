# Operator Queue

**Last updated:** 2026-09-05T07:00Z (Sweep-057 — CI reconciliation)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See below | READY (CI green after Sweep-056 docs; run 33949194624) |
| Tag + Release | **forge-aegis** | See Sweep-055 commands | READY (CI green 33904082644) |
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
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | After lockfile bumps | OPEN |

## Closed this sweep

- **Sweep-057:** sovereign-clean-room CI contradiction (Sweep-052 red vs later green) closed against live run 33904047312 success. Registry no longer may say “CI red”.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
