# Sweep History

## Sweep-271 — 2026-10-07 portfolio governance sweep

- Timestamp: 2026-10-07.
- Scope: authenticated search of `user:beyond-repair` plus Phase-3 live verification of `forge-aegis`, `sovereign-clean-room`, `BlockSwarm`, `Digital_Double_virtual_workforce`.
- Repositories reviewed: 83 names in search payload (`incomplete_results` false). Profile `public_repos` 78. Private in payload: 9. Archived flag true: `CFT-v3.0` only.
- Findings: Phase-3 CI on main is success for all four. Releases and tags empty for all four. Code scanning 404 for all four. Dependabot open empty for forge-aegis, sovereign-clean-room, BlockSwarm. Digital Double critical alert 13 still open, plus high lockfile alerts. Readiness FAIL for Digital Double; PASS WITH FINDINGS for the other three.
- Actions performed: updated `docs/PORTFOLIO_STATUS_REPORT.md`, `docs/OPERATOR_QUEUE.md`, `docs/SWEEP_HISTORY.md` only. No repository deletion. No history rewrite. No tag. No archive flag. No claim elevation. No test execution this sweep.
- Residual risks: critical CVE-2025-7783 on Digital Double lockfile; unmerged sovereign-clean-room branches; duplicate canonical lines not archived; count mismatch 83 versus 78; non-Phase-3 trees not re-audited.
- Exit criteria: failed. Sweep stops.

## Sweep-270 — 2026-10-07 random completion sweep (DigitalDoubleVirtualWorkforce3.5)

- Selection: `random.SystemRandom().choice` over the 83-name authenticated search payload (`user:beyond-repair`, `total_count=83`, `incomplete_results=false`, order updated desc). Index 46. Subject: `DigitalDoubleVirtualWorkforce3.5`.
- Discover: default branch `master`, pre-sweep HEAD `1b5f46b7a8ae39dbf46f09813760cdb3b6506090`, tree not truncated, 51 paths. Claim-0 sketch: `main.py`, `src/core`, `src/models/model_quantizer.py` (advice only), `tests/`, `tests_governance/`, `docs/archive_fragments/`. No lockfile. No torch.
- Audit: registry already labels SUPERSEDED with successor `Digital_Double_virtual_workforce`. Archive-queue row present. GitHub archived flag false. Prior CI run 37051311649 success covered banner unittest only.
- Classification: SUPERSEDED. Claim 0. Not changed.
- Local tests before push: `pytest -q` 18 passed; governance unittest 3 OK.
- Actions: extended `.github/workflows/supersede-guard.yml` to install requirements and run `pytest -q`; added `SUPERSEDED.md` and `docs/DISCOVERY.md`; updated README, GOVERNANCE, CLAIM_STATUS, CHANGELOG. Commits `c9158c06`, `23a8ba59`, `50e578b5`, `63daeb47`. No history rewrite. No deletion. No tag. No archive flag. No claim elevation.
- CI observation: supersede-guard run 37633526662 conclusion success on HEAD `63daeb476cf28c1bcda3eac6c2237c9e7f409415` (banner unittest plus Claim-0 pytest). Not a product or CAP claim.
- Working-tree note: Sweep-270 governance commit `144b566b` replaced visible bodies of the three docs with Sweep-270 headers. Prior bodies remain at blobs `d286661bab62308976594fd0d3d4c41c64cbae54`, `540adac46ad50802f0857623c3505865b6bb76e4`, `0980c7b44ea3a8b734fce4ba55571c95fe54e368`. Restore onto HEAD is pending. Not a history rewrite.
- Archive flag remains operator-only. Portfolio exit criteria remain unmet.

Prior sweep bodies before Sweep-270 are retained in git history of this file (pre-sweep blob `0980c7b44ea3a8b734fce4ba55571c95fe54e368`). This commit does not delete those bodies from history.
