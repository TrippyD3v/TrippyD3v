#!/usr/bin/env python3
"""
GrokWork (TicketOps)
A learning-driven local work signal reducer.

Core question: What work actually matters right now?

Tuned from claude-work skeleton sessions (TICKETOPS-SESSION-20260604-DAY2-CLI-V0.1)
+ patterns proven in sentinel-phase2 (modular scanners, correlators, historical/offline KB,
  clean reporter, minimal deps, actionable output only).

Grok primary. Claude compatible via .claude/ + Claude.md.
"""

import argparse
from scanner.work_scanner import get_work_items, scan_local_work_sources
from correlator.matcher import correlate_work
from reporting.reporter import print_findings
from utils.logger import info
from vulnerability.historical import print_historical_patterns


def main():
    parser = argparse.ArgumentParser(description="GrokWork / TicketOps v0.1 - reduce work noise to what matters")
    parser.add_argument("--no-scan", action="store_true", help="Skip live local file scanner")
    args = parser.parse_args()

    print("grok-work :: boot")
    print("[ ticketops work reducer ]")
    print("----------------------------------------")
    print("> read.work_sources()")
    print("> parse.signals()")
    print("> reduce.noise()")
    print("----------------------------------------")

    info("Scanning curated tickets (data/ + examples)...")
    tickets = get_work_items()
    print(f"Work items loaded: {len(tickets)}")

    signals = []
    if not args.no_scan:
        signals = scan_local_work_sources(".")
        info(f"Live signals discovered: {len(signals)}")

    info("Running correlation (priority + signal boost)...")
    findings = correlate_work(tickets, signals)

    print_findings(findings)

    # Offline "historical" work patterns (classic gotchas that keep recurring)
    # Data transferred / inspired by claude-work side sessions on recurring ticket patterns.
    print_historical_patterns()


if __name__ == "__main__":
    main()
