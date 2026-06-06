# Claude.md - Compatibility Layer for Claude Code / Cowork

This project is **Grok primary** (see AGENTS.md) but fully compatible with Claude.

## Project
GrokWork / TicketOps v0.1
A CLI that reduces ticket and work noise to the signals that require action now.
Local-first, modular (scanner / correlator / reporter), offline historical patterns included.

## Run
python grok_work.py
python grok_work.py --scan   # also pulls TODOs/tasks from local files

## Structure (same as sentinel for easy navigation)
- grok_work.py : main entry + boot banner
- cli/main.py : argparse CLI
- models/data_models.py : Ticket, WorkSignal, WorkFinding
- scanner/work_scanner.py : local file scan + curated ticket loader
- correlator/matcher.py : priority + signal correlation (the important logic)
- reporting/reporter.py : clean output only
- utils/ : logger, priority_utils
- data/ : tickets.csv + other offline sources
- test-ticket-project/ : sample files with tasks/TODOs for testing scanner

## Key Differences from Pure Claude Workflow
- We use real Python modules and dataclasses (not just prompts)
- Correlation logic is code, not just LLM reasoning (repeatable + auditable)
- Historical patterns live in code (see grok_work.py and future historical.py)
- Designed to be called from Grok skills / subagents / TUI

## Adding New Work Sources
1. Extend scanner/work_scanner.py (or add new scanner module)
2. Update models if new fields
3. Enhance correlator/matcher.py for new matching rules
4. Update reporter only for format
5. Add example data under data/ or test-*/

## For Claude Users
Treat this like any other Claude Code project. The Claude.md + .claude/ dirs will be picked up.
All instructions in AGENTS.md also apply (Grok will read both).

Keep changes minimal and focused. Run the tool after edits to verify.
