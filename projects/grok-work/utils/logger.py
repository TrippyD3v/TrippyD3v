import sys
from datetime import datetime


def log(msg: str, level: str = "INFO"):
    ts = datetime.now().isoformat(timespec="seconds")
    print(f"[{ts}] [{level}] {msg}", file=sys.stderr if level in ("ERROR", "WARN") else sys.stdout)


def info(msg: str):
    log(msg, "INFO")


def warn(msg: str):
    log(msg, "WARN")


def error(msg: str):
    log(msg, "ERROR")
