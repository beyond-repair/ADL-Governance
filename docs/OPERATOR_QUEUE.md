# Operator Queue

**Last updated:** 2026-09-05T23:10Z (Sweep-067 — Digital_Double_Virtual_Workforce_4.2)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY (CI green run 33949194624) |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY (CI green 33904082644) |
| Bump PyNaCl ≥1.6.2 | **sovereign-clean-room** | PR **#1** open | **PR OPEN** — merge after CI green |
| Bump nanoid ≥5.1.11 | **Digital_Double_virtual_workforce** | PR **#4** open; run `npm install` to refresh lockfile | **PR OPEN** — merge after lockfile + CI |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### Sweep-067 new operator items

| Action | Notes | Status |
|--------|-------|--------|
| Confirm unique 4.2 assets ported (or waived) | agents/, selfheal/, docs/detailed/, scripts/ | OPEN |
| Decide fate of `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` | ~74 MiB in git; consider Git LFS or omit from successor | OPEN |
| GitHub-archive Digital_Double_Virtual_Workforce_4.2 | Only after port/waiver | PENDING |
| Apply same SUPERSEDED banner to 3.5 / 4. / mobile pair | Same successor | OPEN |

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

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready; not implemented | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |
| Classify new repo | Sovereign-Epistemic-Reality-Engine | Appeared in Sweep-066 census | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | After lockfile bumps + PR#4 merge | OPEN |
| Harmonize registry claim row for thrust-target-30 to 0 | repository_registry.md | Still lists claim 1 vs Sweep-063 claim 0 | OPEN (docs) |

## Closed this sweep

- **Sweep-067:** Digital_Double_Virtual_Workforce_4.2 classified SUPERSEDED; README + SUPERSEDED.md + CANONICAL_NOTE on `c3375cb`. No archive. No delete. No history rewrite.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
