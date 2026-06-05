from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ticket:
    """Core work item / ticket model (transferred + tuned from claude-work skeleton)."""
    id: str
    title: str
    description: str
    status: str = "open"  # open, in_progress, blocked, done
    priority: str = "medium"  # low, medium, high, critical
    source: str = "local"
    created: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class WorkSignal:
    """Parsed signal from local work sources (notes, md, csv, code TODOs)."""
    source_file: str
    signal_type: str  # todo, ticket, note, task
    content: str
    urgency_hint: str = "normal"


@dataclass
class WorkFinding:
    """Actionable output after correlation: what actually matters right now."""
    ticket_id: str
    title: str
    priority: str
    signal: str
    recommended_action: str
    source: str