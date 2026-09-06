# Operator Queue

**Last updated:** 2026-09-06T13:40Z (Sweep-073 — random select LegionOS)

Destructive or account-level actions that require a human operator. Agent records; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases. Agent will not implement offensive security modules. Agent will not `gh repo archive`.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See v0.5.0-sagf block | READY |
| Tag + Release | **forge-aegis** | `git tag -a v0.1.0` + `gh release create` | READY |
| Confirm Dependabot HIGH closed | **Digital_Double_virtual_workforce** | Open HIGH includes #153 nanoid, #155/#157 browserslist | **OPEN** |
| Merge remaining Dependabot PRs | Digital_Double #5, #6 | Operator merge after review | OPEN |
| Archive batch | docs/archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

### Closed this cycle (Sweep-073)

| Action | Notes | Status |
|--------|-------|--------|
| Re-audit LegionOS | RESEARCH claim 0 confirmed; head `5d471c16` | **DONE (docs)** |

### Still open from Sweep-067/068/069/070/071/072

| Action | Notes | Status |
|--------|-------|--------|
| Confirm unique 4.2 assets ported (or waived) | agents/, selfheal/, docs/detailed/, scripts/ | OPEN |
| Decide fate of `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` | ~74 MiB in git | OPEN |
| GitHub-archive Digital_Double_Virtual_Workforce_4.2 | Only after port/waiver | PENDING |
| Apply SUPERSEDED banner to 3.5 / 4. / mobile pair | Same successor | OPEN |
| Consolidate OS-family sketches | RealityOS / LegionOS / Sovereign-OS / SovereignOS | OPEN |
| Do not implement spend/ads/billing agents in LegionOS or SovereignOS | Attack/spend surface without gates | DEFERRED |
| Wire real supervisor LLM into SUNDER | Architecture ready; not implemented | OPEN |
| GitHub-archive btc-trading | Documented Sweep-071; execute `gh repo archive` | PENDING |
| GitHub-archive genieGPT | Documented Sweep-072; execute `gh repo archive beyond-repair/genieGPT --yes` | PENDING |

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
| ADL-Nexus claim-cap / CI | ADL-Nexus | Do not treat as second canonical owner | OPEN |
| Harmonize registry claim row for thrust-target-30 to 0 | repository_registry.md | OPEN (docs) |

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
