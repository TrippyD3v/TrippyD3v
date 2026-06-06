from typing import List
from models.data_models import WorkFinding
from utils.logger import info


def print_findings(findings: List[WorkFinding]):
    """Pretty print the reduced actionable work signals (like sentinel reporter)."""
    if not findings:
        print("\nNo actionable work items right now. Good job.")
        return

    print("\n=== GROK-WORK / TICKETOPS :: ACTIONABLE FINDINGS ===\n")
    for f in findings:
        pri = f.priority.upper()
        print(f"[{pri}] {f.ticket_id}: {f.title}")
        print(f"    source: {f.source}")
        print(f"    signal: {f.signal}")
        print(f"    => {f.recommended_action}")
        print()

    print("=== end of reduced signal (what actually matters) ===")
