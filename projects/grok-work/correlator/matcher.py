from typing import List
from models.data_models import Ticket, WorkSignal, WorkFinding
from utils.priority_utils import extract_priority, sort_by_priority
from utils.logger import info


def correlate_work(tickets: List[Ticket], signals: List[WorkSignal] = None) -> List[WorkFinding]:
    """
    Core correlation: reduce noise to what requires action now.
    - Boost priority from live signals (TODOs near ticket titles)
    - Produce WorkFinding with recommended_action.
    Tuned from sentinel matcher patterns + claude-work ticketops ideas.
    """
    if signals is None:
        signals = []
    findings: List[WorkFinding] = []
    signal_text = " ".join(s.content.lower() for s in signals)

    for t in tickets:
        pri = t.priority
        action = "review and update status"

        title_lower = t.title.lower()
        desc_lower = t.description.lower()
        self_text = f"{title_lower} {desc_lower}"

        # Primary rules from ticket itself (title/desc) - data transfer from claude-work + sentinel style primary match
        if any(kw in self_text for kw in ["login", "auth", "5xx", "token"]) and ("login" in title_lower or "auth" in title_lower or "deploy" in self_text):
            pri = "critical"
            action = "escalate immediately - check recent deploys and auth logs"
        elif "onboard" in self_text and "acme" in self_text:
            action = "run onboarding playbook (see docs/onboarding.md)"
        elif "roadmap" in title_lower:
            action = "pull latest OKRs from notion/notion-export and regenerate slides"

        # keyword urgency from the ticket own text
        if "critical" in self_text or "p0" in self_text or "blocker" in self_text:
            pri = "critical"

        # Secondary: live signal boost (only if signals provided). Match signal content against this ticket.
        if signals:
            for sig in signals:
                sig_l = sig.content.lower()
                if ("login" in title_lower or "auth" in title_lower or "deploy" in self_text) and any(k in sig_l for k in ["login", "auth", "fixme", "hotfix", "deploy"]):
                    pri = "critical"
                    action = "escalate immediately - check recent deploys and auth logs (live signal match)"
                    break

        findings.append(
            WorkFinding(
                ticket_id=t.id,
                title=t.title,
                priority=pri,
                signal="live+curated" if signals else "curated",
                recommended_action=action,
                source=t.source,
            )
        )

    return sort_by_priority(findings)
