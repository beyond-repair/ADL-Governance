# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-220)

- **digital-double-mobile secret scanning alert #1:** open as of Sweep-219. Type OpenRouter API key. Historical path `.env` (not in current tree). Publicly leaked. Validity unknown. Rotate and revoke. Do not rewrite history. Absence of `.env` is not rotation. Not re-fetched in Sweep-220.
- **digital-double-mobile Dependabot critical #30:** `protobufjs` / GHSA-xq3m-2v4x-88gg / CVE-2026-41242. Manifest `package-lock.json`. Runtime scope. Not bumped. Not re-fetched in Sweep-220.
- **digital-double-mobile Dependabot critical #8:** `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Runtime scope. Not bumped. Not re-fetched in Sweep-220.
- **digital-double-mobile archive flag:** classification SUPERSEDED. `archived=true` still false. Archive-queue gate still requires credential rotation first.
- **Digital_Double_virtual_workforce Dependabot alert #13:** re-fetched open in Sweep-220. `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Manifest `digital_double/package-lock.json`. Scope development. Matched range `>= 4.0.0, < 4.0.4`. Patched identifier 4.0.4. Not patched.
- **Digital_Double_virtual_workforce high Dependabot (sample from Sweep-217, not re-listed):** #160 and #159 `js-yaml`; #155 `browserslist`; #153 `nanoid`. Development scope.
- **sovereign-clean-room `seem-completion-pass`:** branch still at `d6f13042f4f99cd186761ae438b75c3e4e705f11`. Python tests run 37215829476 success. Not merged. VSA completeness still UNVERIFIED.
- **sovereign-clean-room branch `fix/pynacl-1.6.2-cve-2025-69277`:** still present at `f65d7db6c4f7d98ed3f5ded3defd5d1886c21cc4`. Not merged.
- **Secret scanning disabled** on `sovereign-clean-room` (API 404, Sweep-220). Enabling it is operator-only.
- **DevelopTool-Unified-Dev-Environment archive flag:** classification ARCHIVED. `archived=true` still false.
- Other archive-queue flags remain false. Only `CFT-v3.0` is GitHub-archived.
- Product tags/releases, code scanning enablement, secret rotation, and GitHub archive flags remain operator-only. History rewrite and repository deletion remain forbidden.
- Accounting: user `public_repos` 78 vs search total 83. Do not delete repositories to force equality.

## Residual notes from Sweep-220

Live re-fetch of the four mandated subjects. Main CI success retained (runs 37065566958, 37064696194, 36859452185, 36861489156). Releases API empty. Digital Double alert #13 still open. Secret scanning disabled on sovereign-clean-room. No archive, no merge, no lockfile bump.

## Residual notes from Sweep-219

Subject `Digital_Double_virtual_workforce` main head `24e6a29fd26c03900a8d98634d6683996eabdac4`. Dependabot alert #13 re-fetched open. digital-double-mobile secret scanning alert #1 still open (value not copied). sovereign-clean-room PR #3 and PR #1 still open. Not merged.

## Residual notes from Sweep-218

Subject `digital-double-mobile` post-head `7c65eb04`. superseded-guard run 37230662637 success. Critical alerts and alert #1 remain open. Archive flag remains false.
