# Operator Queue

**Last updated:** 2026-09-06T19:10Z (Sweep-083 — -Entanglement-and-Emergence)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`. Agent will not rewrite history.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| **Rotate + remove committed `.env`** | **digital-double-mobile** | 1) Rotate every credential that ever appeared in `.env`. 2) Delete `.env` from `main` after rotation. 3) `.gitignore` already updated Sweep-077 (`4e33b669`). 4) Do **not** force-push unless separately authorized after rotation. | **OPEN** |
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY |
| Review then merge Dependabot | **Digital_Double_virtual_workforce** | PRs #5 and #6. After merge, confirm alerts #153/#155/#157 close. | **OPEN** |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### Closed this cycle (Sweep-083)

| Action | Notes | Status |
|--------|-------|--------|
| Claim-cap -Entanglement-and-Emergence | RESEARCH; workflows=0; commit `17d1b7c6` | **DONE** |

### New / still open from Sweep-067…083

| Action | Notes | Status |
|--------|-------|--------|
| Optionally add real 1D spin-chain scripts + missing `figures/metric_entanglement.png` | Only if operator wants Level-2 numerics; do not invent data | OPEN |
| Confirm unique 4.2 assets ported (or waived) | agents/, selfheal/, docs/detailed/, scripts/ | OPEN |
| Decide fate of `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` | ~74 MiB in git | OPEN |
| GitHub-archive Digital Double lineage + fantom_trading_bot_2 + btc-trading + genieGPT | After P0 rotation where applicable | PENDING |
| Consolidate OS-family sketches | RealityOS / LegionOS / Sovereign-OS / SovereignOS | OPEN |
| Do not implement spend/ads/billing agents in LegionOS or SovereignOS | Attack/spend surface without gates | DEFERRED |
| Do not implement live FrontRunning/SandwichBot | MEV attack surface | DEFERRED |
| Do not implement VigilE arp_spoof / password cracker / MITM | Offensive surface | DEFERRED |
| Fix or disable VigilE Security Pipeline | run 33992096428 failure | OPEN |
| Do not GitHub-archive CFTv3.3-IQG-Unified-Framework | Remains CFT symbol ledger | DEFERRED |

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
