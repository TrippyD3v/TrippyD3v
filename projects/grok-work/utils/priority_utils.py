from typing import Dict, Any


PRIORITY_ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def extract_priority(item: Dict[str, Any]) -> str:
    """Extract or infer priority from a raw work item dict (tags, title keywords, etc)."""
    text = (item.get("title", "") + " " + item.get("description", "")).lower()
    tags = [t.lower() for t in item.get("tags", [])]

    if "critical" in tags or "p0" in tags or "blocker" in text or "urgent" in text:
        return "critical"
    if "high" in tags or "p1" in tags or "asap" in text or "broken" in text:
        return "high"
    if "low" in tags or "p3" in tags or "nice to have" in text:
        return "low"
    return "medium"


def sort_by_priority(findings: list) -> list:
    """Sort findings by priority desc (critical first)."""
    return sorted(
        findings,
        key=lambda f: PRIORITY_ORDER.get(getattr(f, "priority", "medium").lower(), 2),
        reverse=True,
    )
