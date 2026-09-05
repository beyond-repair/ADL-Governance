# Operator Queue

**Last updated:** 2026-09-05T16:58Z (Sweep-064b — security PR open)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY (CI green run 33949194624) |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY (CI green 33904082644) |
| Bump PyNaCl ≥1.6.2 | **sovereign-clean-room** | PR **#1** open (`fix/pynacl-1.6.2-cve-2025-69277`) | **PR OPEN** — merge after CI green |
| Bump nanoid ≥5.1.11 | **Digital_Double_virtual_workforce** | PR **#4** open (`fix/nanoid-5.1.11-ghsa-xwg4`); run `npm install` to refresh lockfile | **PR OPEN** — merge after lockfile + CI |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### BlockSwarm — v0.5.0-sagf

```bash
git clone https://github.com/beyond-repair/BlockSwarm.git && cd BlockSwarm
git checkout main && git pull
git tag -a v0.5.0-sagf -m "SAGF production candidate — B1–B2b-3 complete"
git push origin v0.5.0-sagf
gh release create v0.5.0-sagf --title "v0.5.0-sagf" --notes-file docs/CHANGELOG.md
```

### Security PRs opened this cycle

| PR | URL | Change |
|----|-----|--------|
| sovereign-clean-room#1 | https://github.com/beyond-repair/sovereign-clean-room/pull/1 | `pynacl==1.5.0` → `pynacl>=1.6.2` (CVE-2025-69277) |
| Digital_Double#4 | https://github.com/beyond-repair/Digital_Double_virtual_workforce/pull/4 | `nanoid: ^5.0.6` → `^5.1.16` (GHSA-xwg4-73v4-xw9w) |

## Sweep-064 notes

| Action | Notes | Status |
|--------|-------|--------|
| Confirm thrust-target-30 unit-identity Actions | Runs 33958768662 and 33958771694 conclusion=success | CLOSED |
| Do **not** raise thrust-target-30 claim level | Unit identity ≠ measurement | LOCKED |
| Harmonize registry claim row for thrust-target-30 to 0 | Registry still lists claim 1 | OPEN (docs) |
| Map FROZEN class to SUPERSEDED/ARCHIVED | Directive four-state only | OPEN (taxonomy) |
| Open PyNaCl / nanoid security PRs | Agent-executed; merge is operator/CI | **DONE (PRs open)** |

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
| Digital_Double release | Digital_Double_virtual_workforce | After lockfile bumps + PR#4 merge | OPEN |

## Closed this sweep

- **Sweep-064b:** Security PRs opened for both ACTIVE advisory items.
- **Sweep-064:** Live re-verify of four mandatory ACTIVE targets. thrust-target-30 Actions residual closed. No archive. No tags created (tooling gap).
- **Sweep-063:** RESEARCH binding + unit-identity artifacts; Actions now green.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
