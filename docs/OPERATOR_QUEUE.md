# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Sweep-237 additions (2026-10-07)

- **Digital_Double_virtual_workforce Dependabot alert #13:** re-fetched open. `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Manifest `digital_double/package-lock.json`. Scope development. Vulnerable range observed `>= 4.0.0, < 4.0.4`. Patched identifier 4.0.4. Lockfile edit remains operator-owned. Do not mark the workforce product security-clean.
- **sovereign-clean-room branch `fix/pynacl-1.6.2-cve-2025-69277`:** head `f65d7db6c4f7d98ed3f5ded3defd5d1886c21cc4`, not merged. Do not merge from this sweep. Do not claim the CVE is fixed on main. Dependabot high filter on that repo returned empty. Secret scanning is disabled (API 404).
- **sovereign-clean-room branch `seem-completion-pass`:** head `d6f13042f4f99cd186761ae438b75c3e4e705f11`. CI run 37215829476 success. Not merged.
- **digital-double-mobile secret scanning alert #1:** not re-fetched. Prior record stands: OpenRouter API key, historical path `.env`, publicly leaked, validity unknown. Rotate and revoke. Do not rewrite history.
- **digital-double-mobile Dependabot critical #30 and #8:** not re-fetched. Archive-queue gate still requires credential rotation first.
- **Archive flags still false:** `potential-garbanzo`, `RepoRover-`, `Code_Generation_AI_Program`, `test`, Digital Double version repos, OS-family duplicates. Classification in the status report is not a GitHub archive action. Do not delete.
- **BlockSwarm README tag sentence:** tags API empty this cycle. Do not create `v0.5.0-sagf` to match the README.
- **forge-aegis license:** `License TBD` remains operator-only. Code scanning still returns 404 no analysis.
- Product tags, code scanning enablement, secret rotation, and GitHub archive flags remain operator-only. History rewrite and repository deletion remain forbidden.
- Accounting: search `total_count` 83. Profile `public_repos` 78. Do not delete repositories to force equality.
- Digital Double branch list succeeded on retry: `main`; `finish/repair-python-core-ui`; `nex-int-workforce-evidence`; three `dependabot/npm_and_yarn/*` branches; `fix/nanoid-5.1.11-ghsa-xwg4` at `2e8a810e162fa81a60e7c725cb86477836e56fd9`. Do not merge those branches from this sweep. Do not claim the nanoid advisory is fixed on main.

## Residual notes from Sweep-236

`potential-garbanzo` governance class ARCHIVED. Tree `72399fa4e8d304cfa09c0f10f9fe6f12737b9887` not re-fetched. GitHub archive flag not set.

## Residual notes from Sweep-235

Four-pillar heads were unchanged at that fetch. No archive flag. No tag. No lockfile edit.

## Residual notes from Sweep-234

Transcription only. PASS yaml for sweeps 225, 226, and 227. PASS-230, PASS-232, and PASS-233 remain abbreviated stubs.

## Residual notes from Sweep-233

`sunder` RESEARCH, claim ≤1. Do not remove unused declared dependencies unless a later sweep proves no importer. Do not tag. Do not archive.
