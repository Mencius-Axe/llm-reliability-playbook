#!/usr/bin/env python3
from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]

TARGET_GLOBS = [
    "README.md",
    "llm_reliability_playbook.md",
    "docs/**/*.md",
    "templates/**/*.md",
]

# Keep patterns conservative to avoid false positives.
BAD_PATTERNS = [
    r"^EOF$",
    r"^git (add|commit|push)\b",
    r"^make\b",
    r"::contentReference",
    r"oaicite",
    r"^To github\.com:",
    r"^Enumerating objects:",
    r"^Counting objects:",
    r"^Compressing objects:",
    r"^Writing objects:",
    r"^remote:",
]

BAD_RE = [re.compile(p) for p in BAD_PATTERNS]

def is_bad(line: str) -> bool:
    s = line.strip()
    return any(rx.search(s) for rx in BAD_RE)

def main() -> int:
    files = []
    for g in TARGET_GLOBS:
        files.extend(ROOT.glob(g))

    bad = []
    for p in sorted(set(files)):
        if not p.is_file():
            continue
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception as e:
            bad.append((p.as_posix(), 0, f"<read error: {e}>"))
            continue

        for i, line in enumerate(lines, 1):
            if is_bad(line):
                bad.append((p.as_posix(), i, line.strip()[:200]))

    if bad:
        print("FAIL: pasted-terminal junk detected in markdown:")
        for f, i, l in bad:
            print(f"  {f}:{i}: {l}")
        return 1

    print("OK: no pasted-terminal junk detected.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
