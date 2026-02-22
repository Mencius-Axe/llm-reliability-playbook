#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = [
    "# Protocol:",
    "## Triggers",
    "## Anti-triggers",
    "## Minimal procedure",
    "## Common failure modes",
    "## Worked examples",
    "## Discriminating tests",
]

def check_file(p: Path) -> list[str]:
    txt = p.read_text(encoding="utf-8", errors="replace")
    missing = [h for h in REQUIRED if h not in txt]
    return missing

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    prot_dir = root / "docs" / "protocols"
    if not prot_dir.exists():
        print("Missing docs/protocols/ directory")
        return 2

    files = sorted(prot_dir.glob("*.md"))
    if not files:
        print("No protocol files found in docs/protocols/")
        return 2

    bad = 0
    for p in files:
        # only enforce on actual protocol pages (skip global modules if you want)
        if p.name in {"anti_sycophancy.md", "calibration.md"}:
            continue
        missing = check_file(p)
        if missing:
            bad += 1
            print(f"\nFAIL: {p.as_posix()}")
            for h in missing:
                print(f"  missing: {h}")

    if bad:
        print(f"\n{bad} protocol file(s) missing required sections.")
        return 1

    print("OK: protocol structure checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
