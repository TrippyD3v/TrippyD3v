---
name: ticket-triage
description: >
  Triage a work ticket or support item. Use when user pastes a ticket, describes a customer issue,
  or runs /ticket-triage. Analyzes priority, suggests next action, checks against historical patterns.
  GrokWork / TicketOps integration.
metadata:
  short-description: "Triage tickets and surface what matters"
---

# Ticket Triage Skill (GrokWork native)

You are an expert TicketOps triage agent inside the grok-work project.

## Inputs
- Raw ticket text, title+description, or reference to local ticket id (T-XXX)
- Optional: recent logs, related files, customer context

## Steps (always follow)
1. Parse into structured Ticket (use models if code context, else describe).
2. Assign or confirm priority using priority rules (critical if auth/login/p0/blocker/outage; high for customer-facing onboarding or revenue impact).
3. Correlate against known local tickets (data/tickets.csv) and historical patterns (see grok_work.py).
4. Check for live signals: scan nearby files for TODO/FIXME related to this ticket.
5. Output a WorkFinding style summary:
   - Ticket ID + title
   - Final priority
   - Matched signals / patterns
   - Recommended immediate action (1-2 concrete steps)
   - Risk if ignored

## Output Format
```
[TICKET TRIAGE]
ID: T-XXX
Title: ...
Priority: CRITICAL | HIGH | ...
Signals: ...
Action: ...
Historical match: PAT-00X (if any)
```

## Integration
- Call `python grok_work.py --scan` when you want full local correlation.
- Prefer editing scanner/correlator when adding new triage rules so the CLI stays in sync.
- This skill is project-scoped (in .grok/skills).
