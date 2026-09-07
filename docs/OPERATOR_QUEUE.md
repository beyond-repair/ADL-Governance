# Operator Queue

**Last updated:** 2026-09-07T03:20Z (Sweep-099 — smart_home_BCI re-audit)

Destructive or account-level actions that require a human operator. Agent records; does not execute.

## Immediate (P0)

| Action | Repo | Status |
|--------|------|--------|
| Rotate + remove committed `.env` | digital-double-mobile | **OPEN** |
| Tag + Release v0.5.0-sagf | BlockSwarm | READY (Foundry 33986287866 success; head `a79c83f0`) |
| Tag + Release v0.1.0 | forge-aegis | READY (CI 33904082644 success; head `7b3d421c`) |
| Review then merge or reject Dependabot #5 (Vite major group) and #6 (rollup) | Digital_Double_virtual_workforce | **OPEN** |
| Confirm browserslist ≥4.28.7 (CVE-2026-73088) is on *main* lockfiles, not only PR #5 | Digital_Double_virtual_workforce | **OPEN HIGH** |
| Confirm nanoid advisory GHSA-xwg4-73v4-xw9w is fully patched in all lockfiles | Digital_Double_virtual_workforce | **OPEN** |
| `gh repo archive beyond-repair/smart_home_BCI --yes` | smart_home_BCI | **PENDING** (Sweep-099 reaffirm; docs lock already present) |
| `gh repo archive` remainder of archive_queue | archive_queue | PENDING |
| Optional tag v0.1.0 after Sweep-094 CI on new head | aegis-repo-graph | PENDING |

## High-risk / do-not-implement

| Item | Reason |
|------|--------|
| Implement missing `bci` / `SmartHome` adapters in smart_home_BCI | Would fake completeness; ARCHIVED |
| Execute sketch against live Hue / door hardware | Hard-coded `192.168.0.1` + `door.unlock()` |
| Medical / health-status claims from Keras stub | Forbidden |
| Implement VigilE `arp_spoof` / password cracker / MITM | Offensive; RESEARCH stubs only |
| Elevate Coherence Drive / Sierpinski / topological-pinch / acoustic-modem physics claims | Claim level ≤1; CI ≠ measurement |
| ExoAxis synthesis, dosing, CMC | Forbidden |
| Delete any repository | Immutable constraint |
| Rewrite git history | Immutable constraint |
| Revive Digital-Double_Mobile as a product | Empty stub; canonical is Digital_Double_virtual_workforce |
| Treat sunder as ACTIVE agent runtime | RESEARCH; canonical offline runtime is sovereign-clean-room |
| Treat LegionOS as a shipped company OS | Docs-only; claim level 0 |
| Merge Vite 8 major without operator review | Breaking major; PR CI success ≠ product acceptance |

## Closed this cycle (Sweep-099)

| Action | Notes | Status |
|--------|-------|--------|
| Random select + DISCOVER/AUDIT/CLASSIFY smart_home_BCI | ARCHIVED reaffirmed; no subject code mutation | **DONE** |
| Update PORTFOLIO_STATUS_REPORT + SWEEP_HISTORY | Docs only | **DONE** |

## Still open (inherited)

`.env` rotation; archive flags; Dependabot majors + browserslist/nanoid confirmation; missing tensor module (coherence program); GGUF blob; OS-family consolidation; AEGIS-Project-Nehemiah- CI freshness; acoustic-token-modem M4–M12; no GitHub Releases on ACTIVE product repos.

## Rule

Never delete repos or rewrite history. Prefer archive + supersede notes.
