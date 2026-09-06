# Operator Queue

**Last updated:** 2026-09-06T22:10Z (Sweep-088 — RepoRover- ARCHIVED lock)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`. Agent will not rewrite history. Agent will not fabricate missing simulation/BCI/v2 intelligence code. Agent will not invent CI green without a workflow run.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| **Rotate + remove committed `.env`** | **digital-double-mobile** | 1) Rotate every credential that ever appeared in `.env`. 2) Delete `.env` from `main` after rotation. 3) `.gitignore` already updated Sweep-077 (`4e33b669`). 4) Do **not** force-push unless separately authorized after rotation. | **OPEN** |
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY |
| Review then merge Dependabot | **Digital_Double_virtual_workforce** | Open PRs **#3 #4 #5 #6**. #5 grouped npm incl. Vite **major** 5.4.14→8.2.2. CI green on #5/#6. Do not squash-merge blindly. | **OPEN** |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |
| GitHub-archive | **smart_home_BCI** | `gh repo archive beyond-repair/smart_home_BCI --yes` after Sweep-087 docs lock `881844c1` | PENDING |
| GitHub-archive | **RepoRover-** | `gh repo archive beyond-repair/RepoRover- --yes` after Sweep-088 docs lock `4aa25674` | PENDING |

### Closed this cycle (Sweep-088)

| Action | Notes | Status |
|--------|-------|--------|
| Re-audit RepoRover- | ARCHIVED lock; product CI absent; commit `4aa25674` | **DONE** |

### Still open from Sweep-067…087

| Action | Notes | Status |
|--------|-------|--------|
| Restore or drop `momentum_closure.convergence.tensor` | `__init__.py` imports missing module; do not invent implementation | OPEN |
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
| GitHub-archive fantom_trading_bot_2 | Sweep-079 ARCHIVED.md + README; `gh repo archive beyond-repair/fantom_trading_bot_2 --yes` | PENDING |
| Do not implement live FrontRunning/SandwichBot | Enum names only; MEV attack surface | DEFERRED |
| Do not implement VigilE arp_spoof / password cracker / MITM | Stubs only; offensive surface | DEFERRED |
| Fix or disable VigilE Security Pipeline | run 33992096428 failure; SAST action is not product CI. Optional: delete duplicate `README .md` | OPEN |
| Consider GitHub-archive VigilE.S.A.-Enhanced-Security | After operator freeze decision; currently RESEARCH documented | PENDING |
| Do not GitHub-archive CFTv3.3-IQG-Unified-Framework | Remains CFT symbol ledger | DEFERRED |
| Do not invent Entanglement figures or simulation tree | Essay-only RESEARCH | DEFERRED |
| Do not invent ExoAxis-1 chemistry / synthesis tree | Essay-only RESEARCH Sweep-085 | DEFERRED |
| Do not promote ADL-Nexus to ACTIVE without CI + tag | Sweep-086 | DEFERRED |
| Optional: add `python-tests.yml` to ADL-Nexus | Operator/product decision; agent did not invent passing CI | OPEN |
| Do not execute smart_home_bci.py against live Hue/door hardware | Sketch unlocks door; undefined imports | DEFERRED |
| Do not resurrect RepoRover v2 dashboard | Mapping already in census/governance | DEFERRED |

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
