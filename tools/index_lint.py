"""index_lint.py - validate docs/release-index.md before publishing."""

import re
import sys
from pathlib import Path

ROW = re.compile(r"\| (v[0-9][^|]*) \| ([0-9-]{10}) \| (stable|beta|rc) \| ([^|]+) \|")


def check(path: str) -> list:
    text = Path(path).read_text(encoding="utf-8")
    rows = ROW.findall(text)
    problems = []
    last = ""
    seen = set()
    for version, when, channel, highlights in rows:
        if when < last:
            problems.append(f"row out of order: {version}")
        last = when
        if version in seen:
            problems.append(f"duplicate version: {version}")
        seen.add(version)
        if len(highlights.strip()) > 120:
            problems.append(f"highlights too long: {version}")
    return problems


if __name__ == "__main__":
    issues = check(sys.argv[1] if len(sys.argv) > 1 else "docs/release-index.md")
    for issue in issues:
        print(issue)
    raise SystemExit(1 if issues else 0)
