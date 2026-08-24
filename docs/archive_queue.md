# Archive Queue

Repositories with `ARCHIVED.md` (or superseded) that still need **GitHub Archive** (read-only lock).

Check off when `gh repo archive` succeeds.

**Gate:** Do not archive until Stage-1 extraction rows in sovereign-clean-room/docs/EXTRACTION_LEGACY.md are VERIFIED and tests green.

## Priority batch (extraction complete 2026-08-24 — archive after VERIFIED)

- [ ] beyond-repair/RepoRover-
- [ ] beyond-repair/genieGPT
- [ ] beyond-repair/Agent-Snake
- [ ] beyond-repair/Auto_Legion
- [ ] beyond-repair/AtomicNexusAI
- [ ] beyond-repair/DevelopTool-Unified-Dev-Environment
- [ ] beyond-repair/fantom_trading_bot_2
- [ ] beyond-repair/fantom-smart-contracts-first-bot
- [ ] beyond-repair/ftmA.I.bot
- [ ] beyond-repair/smart_home_BCI
- [ ] beyond-repair/automate_passive_income
- [ ] beyond-repair/Quantumclustering
- [ ] beyond-repair/-Py2APK-main
- [ ] beyond-repair/quantum_A.I._optimization.py
- [ ] beyond-repair/Digital-Double_Mobile
- [ ] beyond-repair/digital-double-mobile
- [ ] beyond-repair/DigitalDoubleVirtualWorkforce3.5
- [ ] beyond-repair/My-mind-A.I. (branch main2) — **patterns extracted**
- [ ] beyond-repair/Gia---General-Intelligence-Assistant — **patterns extracted**
- [ ] beyond-repair/new-program-1.01
- [ ] beyond-repair/FortiTrade_Multi-Strategy
- [ ] beyond-repair/btc-trading
- [ ] beyond-repair/Code_Generation_AI_Program

## After SEEM freeze (already SUPERSEDED → sovereign-clean-room)

- [ ] beyond-repair/SEEM-2.0-Self-Evolving-Emergent-Mind
- [ ] beyond-repair/SEEM-Cognitive-Microservice
- [ ] beyond-repair/SEEM-Cognitive_Microservice
- [ ] beyond-repair/seem-block-system

## Command template

```bash
gh repo archive OWNER/REPO --yes
```

Do not delete. Preserve history.

## Stage-1 note

2026-08-24: TaskAtom / Episode / promote_memskill / CapabilityRegistry landed in
sovereign-clean-room (commit on main). Run tests/test_stage1_extraction.py before
checking boxes above.
