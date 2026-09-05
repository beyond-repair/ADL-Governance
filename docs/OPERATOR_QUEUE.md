# Operator Queue

**Last updated:** 2026-09-05T06:12Z (Sweep-056 — BlockSwarm docs)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.
**Constraint:** Connected GitHub tools cannot create git tags or GitHub Releases.

## Immediate (P0)

| Action | Repo | Exact Commands | Status |
|--------|------|----------------|--------|
| Tag + Release | **BlockSwarm** | See below | **READY** (docs now include GOVERNANCE.md + SECURITY.md) |
| Tag + Release | **forge-aegis** | See Sweep-055 commands | READY (prior) |
| Reconcile CI record | **sovereign-clean-room** | Confirm Actions latest run; do not assume green from Sweep-055 vs red from Sweep-052 | OPEN |
| Archive batch | archive_queue.md | `gh repo archive beyond-repair/<name> --yes` | PENDING |

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
| Wire real supervisor LLM into SUNDER | sunder | Architecture ready | OPEN |
| Bump PyNaCl | sovereign-clean-room | After CI record reconciled | OPEN |
| Classify / consolidate | RealityOS / LegionOS / Sovereign-OS | RESEARCH | OPEN |
| Digital_Double release | Digital_Double_virtual_workforce | Lockfile Dependabot | OPEN |

## Completed this sweep

- **Sweep-056:** BlockSwarm GOVERNANCE.md, SECURITY.md, README footer. No tags created.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
