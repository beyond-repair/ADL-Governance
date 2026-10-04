# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-217)

- **digital-double-mobile secret scanning alert #1:** open. Type OpenRouter API key. Historical path `.env` (not in current tree). Publicly leaked. Validity unknown. Rotate and revoke. Do not rewrite history. Absence of `.env` is not rotation.
- **digital-double-mobile Dependabot critical #30:** `protobufjs` / GHSA-xq3m-2v4x-88gg / CVE-2026-41242. Manifest `package-lock.json`. Runtime scope. Patched identifiers 7.5.5 or 8.0.1 depending on range. Not bumped (SUPERSEDED; lockfile bump is operator-only here).
- **digital-double-mobile Dependabot critical #8:** `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Runtime scope. Vulnerable range observed `>= 4.0.0, < 4.0.4`, patched identifier 4.0.4. Not bumped.
- **digital-double-mobile archive flag:** classification SUPERSEDED. `archived=true` still false. Archive-queue gate still requires credential rotation first.
- **Digital_Double_virtual_workforce Dependabot alert #13:** re-fetched open in Sweep-216. `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Manifest `digital_double/package-lock.json`. Scope development. Not patched.
- **Digital_Double_virtual_workforce high Dependabot (sample, not exhaustive):** #160 and #159 `js-yaml` GHSA-2883-xcg3-v3hh; #155 `browserslist` GHSA-73wf-gq98-2v4g; #153 `nanoid` GHSA-xwg4-73v4-xw9w. Development scope.
- **sovereign-clean-room `seem-completion-pass`:** PR #3 still open. Head `d6f13042f4f99cd186761ae438b75c3e4e705f11`. Python tests run 37215829476 success. Not merged. VSA completeness still UNVERIFIED.
- **sovereign-clean-room branch `fix/pynacl-1.6.2-cve-2025-69277`:** still present at `f65d7db6`. Not merged.
- **Secret scanning disabled** on `sovereign-clean-room` (API 404). Enabling it is operator-only.
- **DevelopTool-Unified-Dev-Environment archive flag:** classification ARCHIVED. `archived=true` still false.
- Other archive-queue flags remain false. Only `CFT-v3.0` is GitHub-archived.
- Product tags/releases, code scanning enablement, secret rotation, and GitHub archive flags remain operator-only. History rewrite and repository deletion remain forbidden.

## Residual notes from Sweep-218

Subject `digital-double-mobile` post-head `7c65eb04`. superseded-guard run 37230662637 success (job 111519431449, Claim-0 pytest step success). Guard fails if a working-tree `.env` returns. Critical alerts and alert #1 remain open. Archive flag remains false. Sweep-217's unobserved-CI sentence is closed by observation only.

## Residual notes from Sweep-217

Subject `digital-double-mobile` post-head `7c65eb04`. Guard fails if a working-tree `.env` returns. Critical alerts and alert #1 remain open. Sweep stopped. Post-head CI was later observed in Sweep-218.
