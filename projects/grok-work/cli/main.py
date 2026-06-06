import argparse
from scanner.work_scanner import get_work_items
from correlator.matcher import correlate_work
from reporting.reporter import print_findings
from utils.logger import info


def main():
    parser = argparse.ArgumentParser(description="GrokWork / TicketOps v0.1 - reduce work noise to what matters")
    parser.add_argument("--scan", action="store_true", help="Also run live local file scanner for TODOs/tasks")
    parser.add_argument("--limit", type=int, default=20, help="Max tickets to process")
    args = parser.parse_args()

    info("Booting grok-work (TicketOps mode)...")
    info("Loading curated + live work items...")

    tickets = get_work_items()[: args.limit]
    info(f"Tickets loaded: {len(tickets)}")

    signals = []
    if args.scan:
        from scanner.work_scanner import scan_local_work_sources
        signals = scan_local_work_sources(".")
        info(f"Live signals discovered: {len(signals)}")

    findings = correlate_work(tickets, signals)
    print_findings(findings)

    info("grok-work run complete. Focus here.")


if __name__ == "__main__":
    main()
