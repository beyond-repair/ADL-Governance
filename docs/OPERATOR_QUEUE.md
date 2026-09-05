# Operator Queue

**Last updated:** 2026-09-05T21:07Z (Sweep-065 — VigilE.S.A. re-audit)

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

### Security PRs (Sweep-064b; still operator merge)

| PR | URL | Change |
|----|-----|--------|
| sovereign-clean-room#1 | https://github.com/beyond-repair/sovereign-clean-room/pull/1 | `pynacl==1.5.0` → `pynacl>=1.6.2` |
| Digital_Double#4 | https://github.com/beyond-repair/Digital_Double_virtual_workforce/pull/4 | `nanoid: ^5.0.6` → `^5.1.16` |

## Sweep-065 notes

| Action | Notes | Status |
|--------|-------|--------|
| Optional GitHub archive VigilE.S.A.-Enhanced-Security | After confirming no unique production value | PENDING operator |
| Do **not** implement `arp_spoof` / password cracker | Offensive; out of agent safety scope | LOCKED |
| Do **not** add Cargo.toml that implies a product crate | Manifest absence is evidence, not a gap to fake-close | LOCKED this cycle |
| Duplicate `README .md` | History-preserving; operator may delete if desired | PENDING optional |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready; not implemented | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | After lockfile bumps + PR#4 merge | OPEN |
| Harmonize registry claim row for thrust-target-30 to 0 | repository_registry.md | Still lists claim 1 vs Sweep-063 claim 0 | OPEN (docs) |

## Closed this sweep

- **Sweep-065:** Re-audit VigilE.S.A.-Enhanced-Security; README updated `56850e8`; classification RESEARCH claim 0 confirmed. No offensive implementation. No archive.
- **Sweep-064b:** Security PRs opened for both ACTIVE advisory items.
- **Sweep-064:** Live re-verify of four mandatory ACTIVE targets. thrust-target-30 Actions residual closed.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
