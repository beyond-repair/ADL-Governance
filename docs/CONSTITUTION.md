# Repository Constitution

## Article 1 — Purpose

Repositories under `beyond-repair` exist to advance sovereign software, auditable cognition substrates, and honestly labeled research. No repository may blur engineering validation with unvalidated physical claims.

## Article 2 — Classification

Every repository MUST carry exactly one primary class:

| Class | Meaning |
|-------|---------|
| ACTIVE | Engineering maintained; CI required |
| RESEARCH | Hypothesis-grade; no product claims |
| FROZEN | Complete as reference; no feature work |
| SUPERSEDED | Replaced by a named successor |
| ARCHIVED | Historical only; no new commits expected |

## Article 3 — Canonical authority

Where multiple repos overlap, **CANONICAL_REPOS.md** names the authoritative implementation. Non-canonical repos MUST point to the successor.

## Article 4 — Claim integrity

Physical and cognitive performance claims MUST be tagged Level 0–5 per CLAIM_VALIDATION.md. Cryptographic or CI success does **not** imply experimental physics validation.

## Article 5 — Boundaries

| Boundary | Rule |
|----------|------|
| Clean-Room vs physics | Physics modules are hypothesis-grade; offline only |
| BlockSwarm Chain-3 | Advisory only; no arbitrary execution |
| Secrets | Never commit keys; rotate on exposure |

## Article 6 — Lifecycle

Creation, promotion, supersession, and archive follow LIFECYCLE.md.

## Article 7 — Amendments

Governance changes land in this repository via reviewed commits on `main`.
