#!/usr/bin/env python3
import json
from pathlib import Path
import sys

REQUIRED_KEYS = {"id","task_type","prompt","must_include","must_not_include"}

def main():
    root = Path(__file__).resolve().parents[1]
    evals = root / "evals"
    bad = 0
    for p in sorted(evals.glob("*.jsonl")):
        for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except Exception as e:
                bad += 1
                print(f"FAIL {p}:{i} invalid JSON: {e}")
                continue
            missing = REQUIRED_KEYS - set(obj.keys())
            if missing:
                bad += 1
                print(f"FAIL {p}:{i} missing keys: {sorted(missing)}")
                continue
            if not isinstance(obj["must_include"], list) or not isinstance(obj["must_not_include"], list):
                bad += 1
                print(f"FAIL {p}:{i} must_include/must_not_include must be lists")
    if bad:
        print(f"\n{bad} eval record(s) failed schema checks.")
        return 1
    print("OK: eval schema checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
