#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ALLOWED_TASK_TYPES = {
    "symbol_level",
    "arithmetic_units",
    "perceptual_ocr",
    "debugging_hidden_state",
    "recency_facts",
    "speculative_theory",
    "acceptance_criteria",
}

REQUIRED_KEYS = {"id", "task_type", "prompt", "must_include", "must_not_include"}

def fail(msg: str) -> None:
    print(msg)
    raise SystemExit(1)

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    evals_dir = root / "evals"
    files = sorted(evals_dir.glob("*.jsonl"))
    if not files:
        print("FAIL: no evals/*.jsonl files found")
        return 1

    seen_ids = {}
    bad = 0

    for p in files:
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

            _id = obj["id"]
            tt = obj["task_type"]

            if not isinstance(_id, str) or not _id.strip():
                bad += 1
                print(f"FAIL {p}:{i} id must be a non-empty string")
            else:
                if _id in seen_ids:
                    bad += 1
                    prev = seen_ids[_id]
                    print(f"FAIL {p}:{i} duplicate id '{_id}' (already in {prev})")
                else:
                    seen_ids[_id] = f"{p}:{i}"

            if tt not in ALLOWED_TASK_TYPES:
                bad += 1
                print(f"FAIL {p}:{i} unknown task_type '{tt}' (allowed: {sorted(ALLOWED_TASK_TYPES)})")

            for k in ("must_include", "must_not_include"):
                v = obj[k]
                if not isinstance(v, list) or any((not isinstance(x, str)) or (not x.strip()) for x in v):
                    bad += 1
                    print(f"FAIL {p}:{i} {k} must be a list of non-empty strings")

            if not isinstance(obj["prompt"], str) or not obj["prompt"].strip():
                bad += 1
                print(f"FAIL {p}:{i} prompt must be a non-empty string")

    if bad:
        print(f"\n{bad} eval record(s) failed quality checks.")
        return 1

    print("OK: eval quality checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
