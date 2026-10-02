<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   █████╗ ██████╗ ██╗                                         ║
║  ██╔══██╗██╔══██╗██║                                         ║
║  ███████║██║  ██║██║                                         ║
║  ██╔══██║██║  ██║██║                                         ║
║  ██║  ██║██████╔╝███████╗                                    ║
║  ╚═╝  ╚═╝╚═════╝ ╚══════╝                                    ║
║                                                              ║
║         ＧＯＶＥＲＮＡＮＣＥ  ·  ＣＯＮＳＴＩＴＵＴＩＯＮ       ║
╚══════════════════════════════════════════════════════════════╝
```

# ADL-GOVERNANCE

### The constitution — so code stays honest

**THE CITY WRITES ITS OWN REALITY.**  
**YOU JUST GOVERN IT.**

[![ACTIVE](https://img.shields.io/badge/●_ACTIVE-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Constitution](https://img.shields.io/badge/CONSTITUTION-22d3ee?style=for-the-badge&labelColor=0f0f23)](docs/CONSTITUTION.md)
[![Claims](https://img.shields.io/badge/Claims_0–5-22c55e?style=for-the-badge&labelColor=0f0f23)](docs/CLAIM_VALIDATION.md)

```
STABILITY  ████████████████████████  100%
ALERT      ░░░░░░░░░░░░░░░░░░░░░░░░   0%
```

</div>

---

## ▌ MAIN OBJECTIVE

**REACH THE CORE TOWER**

Classification. Claim levels. Lifecycle. Registry.  
Research cannot pretend to be product.

---

## ▌ TOOLS

| # | Tool | |
|:-:|:----:|:-|
| 1 | **SCAN** | Census |
| 2 | **FORK** | Classify |
| 3 | **SPIKE** | Raise claim |
| 4 | **ANCHOR** | Lock registry |
| 5 | **ESCAPE** | Archive |

---

## ▌ CHECK PASS RECORDS

The runnable tool in this repo is `scripts/check_passes.py`. It checks that every `docs/passes/PASS-*.yaml` file parses and matches one of the two schemas already used here, and that `docs/SWEEP_HISTORY.md` has a `## … / PASS-YYYY-MM-DD-N` heading for every persisted id, including the latest.

It does **not** enforce `docs/CONSTITUTION.md`, raise a claim level, or invent missing historical pass bodies. Markdown files under `docs/passes/` are ignored. Claim levels stay in `docs/CLAIM_VALIDATION.md` as policy.

There is no config file and no compile step. The checker reads the checkout you point at (default: this repository).

### Install

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

`requirements.txt` pins `pyyaml==6.0.2` (the same pin as governance CI) and `pytest==8.3.5` for the tests below. On Windows, activate with `.venv\Scripts\activate`.

### Run

```bash
python scripts/check_passes.py
```

Optional: `python scripts/check_passes.py /path/to/checkout` checks that tree instead of this one.

- Exit `0` prints `PASS: N yaml files parsed; history headings name all ids including PASS-…`.
- Exit `1` is a validation failure (message on stderr).
- Exit `2` means more than one argument was passed.

### Test

```bash
python -m pytest -q
```

### Schemas the checker accepts

Nested (most passes): top-level keys `PASS`, `STATE`, `OBJECTIVE`, `VERIFICATION`, `NEXT`, and `PASS.id` equal to the filename id (`PASS-2026-10-02-205` for `PASS-2026-10-02-205.yaml`; numeric suffix is not zero-padded).

Flat (PASS-168 only in the current tree): `sweep` and `date` match the filename (`sweep: 168`, `date: 2026-10-01`).

A new pass is recorded by adding the YAML file and a sweep heading. This checker only reports whether those two artifacts agree.

---

<div align="center">

```
YOU WERE HERE BEFORE.
VERSION 17 FAILED.
DO NOT TRUST SABLE.
THE CITY REMEMBERS.
```

**REWRITE · BUILD · TRANSCEND**

**Every ACTIVE repo links here.**

</div>
