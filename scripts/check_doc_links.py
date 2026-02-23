#!/usr/bin/env python3
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "index.md"

# Matches backticked relative paths like `protocols/foo.md` in the index
PATH_RE = re.compile(r"`([^`]+\.md)`")

def main() -> int:
    if not INDEX.exists():
        print("FAIL: docs/index.md not found")
        return 1

    text = INDEX.read_text(encoding="utf-8", errors="replace")
    # Deduplicate file references to avoid redundant checks
    paths = set(PATH_RE.findall(text))
    if not paths:
        print("WARN: no backticked .md paths found in docs/index.md")
        return 0

    missing: list[str] = []
    # Resolve each referenced path relative to docs/index.md and record any that do not exist.
    for rel in paths:
        p = (INDEX.parent / rel).resolve()
        if not p.exists():
            missing.append(rel)

    if missing:
        print("FAIL: docs/index.md references missing files:")
        for rel in missing:
            print(f" - {rel}")
        return 1

    print("OK: docs/index.md link targets exist.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
