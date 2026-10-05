# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-223)

- **RepoRover- archive flag:** classification ARCHIVED. `archived=true` still false. Operator may run `gh repo archive beyond-repair/RepoRover- --yes`. Not executed. Do not delete. Do not rewrite history.
- **RepoRover- tags:** none. Do not tag an archive candidate as a product release.

## Residual notes from Sweep-222

forge-aegis post-head CI run 37257747973 success on `8083425d`. Job test 111598348161 success. License, product tag, code scanning, and stale branches remain operator-only. Not closed by CI success.

## Open items (as of Sweep-221)

- **forge-aegis license:** `pyproject.toml` still says `License TBD`. Do not assign a license in an autonomous sweep.
- **forge-aegis product tag:** version `0.1.0` is in pyproject; tags and releases API empty. Product tags remain operator-only. Not tagged in Sweep-221.
- **forge-aegis code scanning:** enabling remains operator-only (API 404 on prior sweeps; not re-enabled).
- **forge-aegis stale branches:** `finish/forge-aegis-v0.1-runnable`, `repair/docs-python3-venv`, `repair/v0.1-installable-slice` still present. Not deleted.

## Open items (as of Sweep-220)

- **digital-double-mobile secret scanning alert #1:** open as of Sweep-219. Type OpenRouter API key. Historical path `.env` (not in current tree). Publicly leaked. Validity unknown. Rotate and revoke. Do not rewrite history. Absence of `.env` is not rotation. Not re-fetched in Sweep-223.
- **digital-double-mobile Dependabot critical #30:** `protobufjs` / GHSA-xq3m-2v4x-88gg / CVE-2026-41242. Manifest `package-lock.json`. Runtime scope. Not bumped. Not re-fetched in Sweep-223.
- **digital-double-mobile Dependabot critical #8:** `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Runtime scope. Not bumped. Not re-fetched in Sweep-223.
- **digital-double-mobile archive flag:** classification SUPERSEDED. `archived=true` still false. Archive-queue gate still requires credential rotation first.
- **Digital_Double_virtual_workforce Dependabot alert #13:** re-fetched open in Sweep-220. `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Manifest `digital_double/package-lock.json`. Scope development. Matched range `>= 4.0.0, < 4.0.4`. Patched identifier 4.0.4. Not patched.
- **sovereign-clean-room `seem-completion-pass`:** branch still at `d6f13042f4f99cd186761ae438b75c3e4e705f11`. Python tests run 37215829476 success. Not merged. VSA completeness still UNVERIFIED.
- **sovereign-clean-room branch `fix/pynacl-1.6.2-cve-2025-69277`:** still present at `f65d7db6c4f7d98ed3f5ded3defd5d1886c21cc4`. Not merged.
- **Secret scanning disabled** on `sovereign-clean-room` (API 404, Sweep-220). Enabling it is operator-only.
- **DevelopTool-Unified-Dev-Environment archive flag:** classification ARCHIVED. `archived=true` still false.
- Other archive-queue flags remain false. Only `CFT-v3.0` is GitHub-archived.
- Product tags/releases, code scanning enablement, secret rotation, and GitHub archive flags remain operator-only. History rewrite and repository deletion remain forbidden.
- Accounting: user `public_repos` 78 vs search total 83. Do not delete repositories to force equality.
