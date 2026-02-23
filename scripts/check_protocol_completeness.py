!/usr/bin/env python3
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROT_DIR = ROOT / "docs" / "protocols"

SKIP = {"anti_sycophancy.md", "calibration.md"}

HEADERS = [
    "## Triggers",
    "## Anti-triggers",
    "## Common failure modes",
    "## Discriminating tests",
]

def section_body(text: str, header: str) -> st
r
    # crude but robust: capture from header to next "## "
    pat = re.compile(re.escape(header) + r"\n(.*?)(?=\n## |\Z)", re.S)
    m = pat.search(text)
    return m.group(1).strip() if m else ""

def has_real_bullet(body: str) -> bool:
    lines = [l.strip() for l in body.splitlines() if l.strip()]
    bullets = [l for l in lines if l.startswith("- ")]
   if not bullets:
        return False
    for b in bullets:
        if "TODO" in b.upper():
            continue
        return True
    return False

def main() -> int:
    if not PROT_DIR.exists():
        print("FAIL: docs/protocols not found")
        return 1

    bad = 0
    for p in sorted(PROT_DIR.glob("*.md")):
        if p.name in SKIP:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
         h in HEADERS:
            body = section_body(text, h)
            if not has_real_bullet(body):
                bad += 1
                print(f"FAIL: {p.as_posix()} incomplete section: {h}")

    if bad:
        print(f"\n{bad} section(s) incomplete (contain only TODO or no bullets).")
        return 1


    print("OK: protocol completeness checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
#
