# Operator Queue

**Last updated:** 2026-09-06T15:11Z (Sweep-077 — digital-double-mobile re-audit)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`. Agent will not rewrite history.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| **Rotate + remove committed `.env`** | **digital-double-mobile** | 1) Rotate every credential that ever appeared in `.env`. 2) Delete `.env` from `main` after rotation (`gh api` or web UI). 3) `.gitignore` already updated Sweep-077 (`4e33b669`). 4) Do **not** force-push unless separately authorized after rotation. | **OPEN (Sweep-077)** |
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY |
| Confirm Dependabot HIGH closed | **Digital_Double_virtual_workforce** | Open HIGH includes #153 nanoid, #155/#157 browserslist | **OPEN** |
| Merge remaining Dependabot PRs | Digital_Double #5, #6 | Operator merge after review | OPEN |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### Closed this cycle (Sweep-077)

| Action | Notes | Status |
|--------|-------|--------|
| Add `.env` to `.gitignore` on digital-double-mobile | `4e33b66945a285fefa5c114642078fed3a91d925` | **DONE** |
| Re-affirm SUPERSEDED.md | `306571135e94070d32b7254fbdcb95dc72e216b8` | **DONE** |

### Still open from Sweep-067…076

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
| Wire real supervisor LLM into SUNDER | Architecture ready; not implemented | OPEN |
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
