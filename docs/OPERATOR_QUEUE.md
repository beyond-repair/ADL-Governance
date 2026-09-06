# Operator Queue

**Last updated:** 2026-09-06T02:00Z (Sweep-069 — live re-verify ACTIVE four)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY (Foundry green 33986287866) |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY (CI green 33904082644) |
| Confirm Dependabot HIGH closed | **Digital_Double_virtual_workforce** | Alerts 153 (nanoid) and 155 (browserslist) still OPEN after lockfile `c69ba6f6` | **OPEN** |
| Merge remaining Dependabot PRs | Digital_Double #5 (group bump), #6 (rollup) | CI success on both PR heads; operator merge after review | OPEN |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### Closed since Sweep-068

| Action | Notes | Status |
|--------|-------|--------|
| Bump PyNaCl ≥1.6.2 | sovereign-clean-room main `33a1caca`; Python tests 33979476402 success; Dependabot open=0 | **DONE on main** |
| LegionOS docs-ci observation | run 34003175517 success on `89486578` | **DONE** |
| Classify ADL-Nexus | RESEARCH / UNVERIFIED integration sketch (layer0–8 tree; no ACTIVE promotion) | **DONE (docs)** |
| Classify Sovereign-Epistemic-Reality-Engine | RESEARCH | **DONE (docs)** |

### Still open from Sweep-067/068

| Action | Notes | Status |
|--------|-------|--------|
| Confirm unique 4.2 assets ported (or waived) | agents/, selfheal/, docs/detailed/, scripts/ | OPEN |
| Decide fate of `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` | ~74 MiB in git; consider Git LFS or omit from successor | OPEN |
| GitHub-archive Digital_Double_Virtual_Workforce_4.2 | Only after port/waiver | PENDING |
| Apply SUPERSEDED banner to 3.5 / 4. / mobile pair | Same successor | OPEN |
| Consolidate OS-family sketches | RealityOS / LegionOS / Sovereign-OS / SovereignOS | OPEN |
| Do not implement spend/ads/billing agents in LegionOS | Attack/spend surface without gates | DEFERRED |
| Wire real supervisor LLM into SUNDER | Architecture ready; not implemented | OPEN |

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
| Digital_Double release | Digital_Double_virtual_workforce | After Dependabot HIGH clear + PR merge | OPEN |
| ADL-Nexus claim-cap / CI | ADL-Nexus | Tree looks like multi-layer facade; do not treat as second canonical owner | OPEN |
| Harmonize registry claim row for thrust-target-30 to 0 | repository_registry.md | Still lists claim 1 vs Sweep-063 claim 0 | OPEN (docs) |

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
