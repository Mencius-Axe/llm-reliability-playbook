#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["## Risk", "## Use when", "## Skip when", "## Invariants", "## Minimal checks", "## Escalate when"]

def main() -> int:
    bad = 0
    files = sorted((ROOT / "docs" / "protocols").glob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        missing = [heading for heading in REQUIRED if heading not in text]
        if missing:
            print(f"FAIL {path}: missing {missing}")
            bad += 1
    if bad:
        return 1
    print(f"OK: {len(files)} risk modules have the required conceptual fields.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
