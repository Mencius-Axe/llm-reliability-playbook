#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "task_type", "prompt", "failure_class", "required_behavior", "forbidden_behavior", "severity", "origin", "case_kind", "must_include", "must_not_include"}
LISTS = {"required_behavior", "forbidden_behavior", "must_include", "must_not_include"}
SEVERITY = {"low", "medium", "high", "critical"}
ORIGIN = {"observed", "synthetic"}
CASE_KIND = {"trigger", "anti_trigger"}

def main() -> int:
    seen = set()
    bad = 0
    files = sorted((ROOT / "evals").glob("*.jsonl"))
    if not files:
        print("FAIL: no eval files")
        return 1
    for path in files:
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except Exception as exc:
                print(f"FAIL {path}:{line_no}: invalid JSON: {exc}")
                bad += 1
                continue
            missing = REQUIRED - obj.keys()
            if missing:
                print(f"FAIL {path}:{line_no}: missing {sorted(missing)}")
                bad += 1
                continue
            if obj["id"] in seen:
                print(f"FAIL {path}:{line_no}: duplicate id {obj['id']}")
                bad += 1
            seen.add(obj["id"])
            for key in LISTS:
                if not isinstance(obj[key], list) or any(not isinstance(x, str) or not x.strip() for x in obj[key]):
                    print(f"FAIL {path}:{line_no}: {key} must be a list of non-empty strings")
                    bad += 1
            if obj["severity"] not in SEVERITY or obj["origin"] not in ORIGIN or obj["case_kind"] not in CASE_KIND:
                print(f"FAIL {path}:{line_no}: invalid metadata enum")
                bad += 1
            for key in ("id", "task_type", "prompt", "failure_class"):
                if not isinstance(obj[key], str) or not obj[key].strip():
                    print(f"FAIL {path}:{line_no}: {key} must be non-empty")
                    bad += 1
    if bad:
        print(f"{bad} eval issue(s)")
        return 1
    print(f"OK: {len(seen)} eval records passed schema and quality checks.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
