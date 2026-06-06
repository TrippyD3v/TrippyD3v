import os
import re
from typing import List
from models.data_models import WorkSignal, Ticket


def scan_local_work_sources(root: str = ".") -> List[WorkSignal]:
    """Scan local dir for work signals: TODOs in md/py, ticket-like lines."""
    signals: List[WorkSignal] = []
    exts = {".md", ".txt", ".py", ".rst"}

    for dirpath, _, filenames in os.walk(root):
        # skip obvious noise
        if any(skip in dirpath for skip in (".git", "venv", "__pycache__", "node_modules", ".grok")):
            continue
        for fn in filenames:
            if not any(fn.endswith(e) for e in exts):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, "r", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        line = line.strip()
                        if not line:
                            continue
                        # simple TODO / ticket patterns
                        if re.search(r"\b(TODO|FIXME|TICKET|WORK|BUG)\b", line, re.I):
                            signals.append(
                                WorkSignal(
                                    source_file=f"{path}:{i}",
                                    signal_type="todo",
                                    content=line[:200],
                                    urgency_hint="high" if "FIXME" in line.upper() or "CRITICAL" in line.upper() else "normal",
                                )
                            )
                        elif re.search(r"^\s*-\s*\[\s*\]\s*", line):  # unchecked markdown task
                            signals.append(
                                WorkSignal(
                                    source_file=f"{path}:{i}",
                                    signal_type="task",
                                    content=line[:200],
                                    urgency_hint="normal",
                                )
                            )
            except Exception:
                pass
    return signals


def load_tickets_from_data(data_dir: str = "data") -> List[Ticket]:
    """Load curated tickets from local data/ (csv or simple md simulation for v0.1)."""
    tickets: List[Ticket] = []
    # For skeleton v0.1 we hardcode a few "transferred" example tickets.
    # In real: parse data/tickets.csv or data/*.ticket.md
    example_tickets = [
        {
            "id": "T-001",
            "title": "Onboard new customer AcmeCorp to portal",
            "description": "Provision accounts, send welcome kit, schedule kickoff call.",
            "status": "open",
            "priority": "high",
            "source": "data/tickets.csv",
            "tags": ["onboarding", "customer"],
        },
        {
            "id": "T-002",
            "title": "Investigate login failures after last deploy",
            "description": "Auth service returning 5xx for ~8% of sessions. Check recent changes.",
            "status": "in_progress",
            "priority": "critical",
            "source": "data/tickets.csv",
            "tags": ["bug", "auth", "p0"],
        },
        {
            "id": "T-003",
            "title": "Update Q2 roadmap slide deck",
            "description": "Incorporate new OKRs and competitive notes from last sync.",
            "status": "open",
            "priority": "medium",
            "source": "notes/roadmap.md",
            "tags": ["docs", "planning"],
        },
    ]
    for t in example_tickets:
        tickets.append(
            Ticket(
                id=t["id"],
                title=t["title"],
                description=t["description"],
                status=t["status"],
                priority=t["priority"],
                source=t["source"],
                tags=t.get("tags", []),
            )
        )
    return tickets


def get_work_items() -> List[Ticket]:
    """Primary entry: combine live signals + curated tickets."""
    curated = load_tickets_from_data()
    # signals = scan_local_work_sources(".")  # can be merged later
    return curated
