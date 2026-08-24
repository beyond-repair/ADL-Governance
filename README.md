<div align="center">

# ADL-Governance

### The **constitution** of Atomic Dream Labs — so code stays honest

[![ACTIVE](https://img.shields.io/badge/status-ACTIVE-22c55e?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)

</div>

---

## Why it is unique

Most orgs grow 50 repos and zero rules.  
This repo forces **classification, claim levels, lifecycle, and a registry** — research cannot quietly pretend to be a product.

---

## Visual workflow

```text
  ┌──────────────────┐
  │ 1. IDEA / REPO   │  something lands under beyond-repair
  └────────┬─────────┘
           ▼
  ┌──────────────────┐
  │ 2. CLASSIFY      │  ACTIVE · RESEARCH · FROZEN · SUPERSEDED · ARCHIVED
  └────────┬─────────┘
           ▼
  ┌──────────────────┐
  │ 3. CLAIM LEVEL   │  0–5  (physics defaults ≤2 without evidence)
  └────────┬─────────┘
           ▼
  ┌──────────────────┐
  │ 4. REGISTER      │  repository_registry.md + canonical map
  └────────┬─────────┘
           ▼
  ┌──────────────────┐
  │ 5. BUILD LOOP    │  implement → test → CI → document → release/archive
  └────────┬─────────┘
           ▼
  ┌──────────────────┐
  │ 6. AUDIT         │  portfolio state · archive queue · final audit docs
  └──────────────────┘
```

### Step-by-step — how & why

| Step | How | Why |
|-----:|-----|-----|
| **1** | New work appears | Without a gate, duplicates explode |
| **2** | Assign lifecycle class | Readers know if it is product or history |
| **3** | Assign claim 0–5 | Stops “hypothesis” reading as “proven engine” |
| **4** | Enter registry | One source of truth for the org |
| **5** | Standard eng loop | No repo bypasses test/docs |
| **6** | Periodic audit | Drift is visible |

---

## How the portfolio fits together

```text
                    ┌─ ADL-Governance ─┐
                    │  rules · claims  │
                    └────────┬─────────┘
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                 ▼
    ENGINEERING          SECURITY           RESEARCH
    clean-room           forge-aegis        coherence-drive
    BlockSwarm           Nehemiah           Ware satellites
    Digital Double
```

| Doc | Purpose |
|-----|---------|
| [repository_registry.md](docs/repository_registry.md) | Census |
| [CLAIM_VALIDATION.md](docs/CLAIM_VALIDATION.md) | Levels 0–5 |
| [LIFECYCLE.md](docs/LIFECYCLE.md) | ACTIVE → ARCHIVED |
| [CONSTITUTION.md](docs/CONSTITUTION.md) | Principles |

---

<div align="center">

**Every ACTIVE repo should link here.**

</div>
