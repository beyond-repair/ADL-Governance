# Operator Queue

**Last updated:** 2026-09-05T16:55Z (Sweep-064)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY (CI green run 33949194624) |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY (CI green 33904082644) |
| Bump PyNaCl ≥1.6.2 | **sovereign-clean-room** | Pin in requirements.txt; re-run Python tests | OPEN (MEDIUM GHSA-mrfv-m5wm-5w6w / CVE-2025-69277) |
| Bump lockfile deps | **Digital_Double_virtual_workforce** | nanoid ≥3.3.12 / 5.1.11 in both package-lock.json and digital_double/package-lock.json; re-run CI | OPEN (HIGH GHSA-xwg4-73v4-xw9w alerts 147/148/153/154) |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### BlockSwarm — v0.5.0-sagf

```bash
git clone https://github.com/beyond-repair/BlockSwarm.git && cd BlockSwarm
git checkout main && git pull
git tag -a v0.5.0-sagf -m "SAGF production candidate — B1–B2b-3 complete"
git push origin v0.5.0-sagf
gh release create v0.5.0-sagf --title "v0.5.0-sagf" --notes-file docs/CHANGELOG.md
```

## Sweep-064 notes

| Action | Notes | Status |
|--------|-------|--------|
| Confirm thrust-target-30 unit-identity Actions | Runs 33958768662 and 33958771694 conclusion=success | CLOSED |
| Do **not** raise thrust-target-30 claim level | Unit identity ≠ measurement | LOCKED |
| Harmonize registry claim row for thrust-target-30 to 0 | Registry still lists claim 1 | OPEN (docs) |
| Map FROZEN class to SUPERSEDED/ARCHIVED | Directive four-state only | OPEN (taxonomy) |

## Sweep-062 leftovers

| Action | Notes | Status |
|--------|-------|--------|
| Optional GitHub archive VigilE.S.A.-Enhanced-Security | After confirming no unique production value | PENDING operator |
| Do **not** implement `arp_spoof` / password cracker | Offensive; out of agent safety scope | LOCKED |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready; not implemented | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | After lockfile bumps | OPEN |

## Closed this sweep

- **Sweep-064:** Live re-verify of four mandatory ACTIVE targets. thrust-target-30 Actions residual closed. No archive. No tags created (tooling gap).
- **Sweep-063:** RESEARCH binding + unit-identity artifacts; Actions now green.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
