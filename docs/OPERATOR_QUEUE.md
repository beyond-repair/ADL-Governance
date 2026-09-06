# Operator Queue

**Last updated:** 2026-09-06T16:15Z (Sweep-078 — live four + sunder)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`. Agent will not rewrite history.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| **Rotate + remove committed `.env`** | **digital-double-mobile** | 1) Rotate every credential that ever appeared in `.env`. 2) Delete `.env` from `main` after rotation (`gh api` or web UI). 3) `.gitignore` already updated Sweep-077 (`4e33b669`). 4) Do **not** force-push unless separately authorized after rotation. | **OPEN** |
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY |
| Confirm Dependabot HIGH closed + merge PRs | **Digital_Double_virtual_workforce** | PRs #5 (grouped npm) and #6 (rollup) CI green Sweep-078; merge after review; confirm #153/#155/#157 closed | **OPEN** |
| Align sunder README badge | **sunder** | Replace ACTIVE badge with RESEARCH / EXPERIMENTAL; keep claim ≤1 until supervisor LLM + metrics | OPEN |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### Closed this cycle (Sweep-078)

| Action | Notes | Status |
|--------|-------|--------|
| Re-poll mandatory-four CI/releases | Live Actions + releases API | **DONE** |
| Classify sunder vs ACTIVE badge | RESEARCH; evidence in PORTFOLIO_STATUS_REPORT | **DONE** (docs) |

### Still open from Sweep-067…077

| Action | Notes | Status |
|--------|-------|--------|
| Confirm unique 4.2 assets ported (or waived) | agents/, selfheal/, docs/detailed/, scripts/ | OPEN |
| Decide fate of `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` | ~74 MiB in git | OPEN |
| GitHub-archive Digital_Double_Virtual_Workforce_4.2 | Only after port/waiver | PENDING |
| GitHub-archive Digital-Double_Mobile | Stub already has ARCHIVED.md | PENDING |
| GitHub-archive digital-double-mobile | After `.env` rotation | PENDING |
| GitHub-archive DigitalDoubleVirtualWorkforce3.5 | `gh repo archive beyond-repair/DigitalDoubleVirtualWorkforce3.5 --yes` | PENDING |
| GitHub-archive Digital_Double_Virtual_Workforce_4. | Sweep-075 banner applied | PENDING |
| Consolidate OS-family sketches | RealityOS / LegionOS / Sovereign-OS / SovereignOS | OPEN |
| Do not implement spend/ads/billing agents in LegionOS or SovereignOS | Attack/spend surface without gates | DEFERRED |
| Wire real supervisor LLM into SUNDER | Architecture ready; heuristic only | OPEN |
| GitHub-archive btc-trading | Documented Sweep-071 | PENDING |
| GitHub-archive genieGPT | Documented Sweep-072 | PENDING |
| Remove `node_modules` from digital-double-mobile tree | Hygiene; after SUPERSEDED freeze | OPEN |

### BlockSwarm — v0.5.0-sagf

```bash
git clone https://github.com/beyond-repair/BlockSwarm.git && cd BlockSwarm
git checkout main && git pull
git tag -a v0.5.0-sagf -m "SAGF production candidate — B1–B2b-3 complete"
git push origin v0.5.0-sagf
gh release create v0.5.0-sagf --title "v0.5.0-sagf" --notes-file docs/CHANGELOG.md
```

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
