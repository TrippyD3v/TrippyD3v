# GrokWork (TicketOps)

GrokWork is a learning-driven local system focused on **knowledge work + ticket operations**.

**Repository (source of truth):** https://github.com/TrippyD3v/TrippyD3v (inside `projects/grok-work/`)

This project was originally developed as a standalone repo (https://github.com/TrippyD3v/grok-work-project) and later imported into the TrippyD3v monorepo/workspace via `git subtree`. The old `grok-work-project` repo preserves the pre-integration history.

Primary clone (includes grok-work + other projects):
```bash
git clone https://github.com/TrippyD3v/TrippyD3v.git
cd TrippyD3v/projects/grok-work
python3 grok_work.py --scan
```

Standalone history (pre-monorepo):
```bash
git clone https://github.com/TrippyD3v/grok-work-project.git
```

Core question:
**What work actually matters right now?**

---

## Signal

Most tools and inboxes produce noise (endless tickets, TODOs, notes, Slack pings).
GrokWork reduces that into what requires action.

Mode:
* local-first analysis (files, curated data/, markdown tasks)
* knowledge work / ops focus (support, onboarding, roadmap, bugs)
* no cloud dependency for core loop (historical patterns always available)
* Grok primary, Claude compatible

---

## System View

```
grok_work :: boot
[ ticketops work reducer ]
----------------------------------------
> read.work_sources()
> parse.signals()
> reduce.noise()
----------------------------------------
grokwork :: active
purpose:
find what actually matters
method:
curated -> live signals -> priority boost -> actionable
----------------------------------------
signal:
T-002 login failures
urgency: critical
> status: in_progress
> source: data + deploy notes
action: escalate + check recent changes
----------------------------------------
status: focused
mode: learning
----------------------------------------
:: grok_work ::
```

---

## How to Run

```bash
# After cloning the workspace
cd TrippyD3v/projects/grok-work

# Basic curated tickets + correlation
python grok_work.py

# With live local scanner (TODOs, unchecked tasks in md/py etc)
python grok_work.py --scan

# Via CLI module
python -m cli.main --scan
```

(If using the old standalone checkout, adjust the cd path accordingly.)

---

## Structure (Tuned like Sentinel)

Same proven modular layout:

- `grok_work.py` - direct entry + banner + historical patterns
- `cli/` - argparse entrypoint
- `models/` - Ticket, WorkSignal, WorkFinding dataclasses
- `scanner/` - work_scanner (local files + data/ loader)
- `correlator/` - matcher (priority + signal correlation logic)
- `reporting/` - clean reporter only
- `utils/` - logger + priority_utils
- `data/` - offline tickets.csv + future KBs
- `test-ticket-project/` - sample files to exercise scanner
- `.grok/` - native Grok config + project skills (e.g. ticket-triage)
- `AGENTS.md` + `Claude.md` - rules for both

---

## Data Transfer Notes (from Claude-Work-Project sessions)

- Session identifier: TICKETOPS-SESSION-20260604-DAY2-CLI-V0.1
- Core idea transferred: a practical CLI that turns raw work chaos into prioritized, actionable findings with recommended next steps + historical pattern matching.
- Skeleton was minimal (browser sessions); we built full runnable modules + data + tests (exactly like the sentinel expansion).
- Added Grok-native first (.grok/skills, AGENTS.md, config.toml) while keeping full Claude.md + compat for .claude/

This repo was created locally from the claude-work architecture and pushed as the new `grok-work-project`. It was later integrated (full source + history) into the main workspace monorepo at https://github.com/TrippyD3v/TrippyD3v under `projects/grok-work/` using git subtree. The original grok-work-project repo remains as the historical record of the standalone phase.

---

## Extending

- Add new ticket sources in scanner/work_scanner.py (Jira export, Linear, Notion csv, etc.)
- Add richer historical patterns in grok_work.py (or split to historical.py like sentinel)
- Improve matcher with version-like "ticket age" logic or tag correlation
- Drop a new .grok/skills/ for team-specific triage playbooks
- Use the shipped `/ticket-triage` skill when inside this project cwd

---

## Compatibility

- Primary: Grok (TUI, CLI, skills, subagents)
- Compatible: Claude Code / Cowork (via Claude.md + standard file layout)
- The `ticket-triage` skill is auto-loaded when cwd is inside grok-work

Run it. Focus. Ship the important stuff.
