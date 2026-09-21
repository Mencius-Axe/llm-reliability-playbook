#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["Risk", "Use when", "Skip when", "Invariants", "Minimal checks", "Escalate when"]

def validate_module(text):
    sections = {}
    parts = re.split(r"(?m)^## +(.+?)\s*$", text)
    for index in range(1, len(parts), 2):
        sections[parts[index]] = parts[index + 1].strip()
    return [f"missing or empty section: {name}" for name in REQUIRED if not sections.get(name)]

def validate_modules(root):
    files = sorted((root / "docs/protocols").glob("*.md"))
    errors = [] if files else ["no risk modules"]
    for path in files:
        errors.extend(f"{path.name}: {e}" for e in validate_module(path.read_text(encoding="utf-8")))
    # The v1 response templates contradict the selective v2 architecture.
    for name in ("response_skeleton.md", "prompt_header_ac_rt_al.md", "acceptance_contract.md", "dbg_protocol.md", "recency_check.md"):
        if (root / "templates" / name).exists():
            errors.append(f"retired template remains: {name}")
    return errors

def main():
    errors = validate_modules(ROOT)
    for error in errors:
        print(f"FAIL: {error}")
    if not errors:
        print("OK: risk modules have non-empty sections; retired templates absent.")
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
