# GrokWork Project Rules (Grok Primary)

This is the GrokWork (TicketOps) project - a local-first, signal-reducing CLI for knowledge work and ticket operations.

## Core Philosophy (from sentinel tuning)
- Reduce noise to "what actually matters right now"
- Local first, offline capable (historical patterns always work)
- Modular: scanner -> correlator -> reporter
- Minimal deps, real runnable code, no gold plating
- Every run must produce clear actionable output

## Coding Standards
- Python 3.10+
- Use dataclasses in models/
- Keep scanners pure (no side effects except reads)
- Correlator is the brain - put matching + priority logic here
- Reporter only prints / formats, never computes
- Utils are small pure helpers (priority, logging)
- Add to data/ for offline KB (tickets, patterns). Never hardcode secrets.

## Grok Integration (Primary)
- All project rules live in AGENTS.md (this file) + subdir ones
- Use .grok/ for project-scoped MCP, skills, hooks
- Prefer slash commands and skills for repetitive work flows
- When editing, run the tool: `python grok_work.py --scan` and verify output

## Claude Compatibility
- Claude.md exists for cross-tool use
- .claude/ dirs are scanned (see user-guide)
- Do not break Claude.md parity when updating

## Build / Run / Test
- Run: `python grok_work.py`
- With live scan: `python grok_work.py --scan`
- From cli: `python -m cli.main --scan`
- No formal tests yet (v0.1). Smoke test by running and inspecting findings.
- Before "done": always re-run the main entry and confirm clean actionable output.

## Data & Test
- Curated data lives in data/
- test-ticket-project/ is for exercising the scanner
- Never commit real customer data

## What "Tuned like sentinel" Means Here
- Same structure (cli/models/scanner/correlator/reporting/utils)
- Added historical/offline patterns (like historical.py)
- Improved matcher beyond naive (priority boost + keyword + source)
- Clean boot banner + reduced output
- CLI entry + direct script entry
