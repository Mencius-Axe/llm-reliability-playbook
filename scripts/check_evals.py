#!/usr/bin/env python3
"""Validate specifications, not model performance."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "task_type", "prompt", "failure_class", "required_behavior", "forbidden_behavior", "severity", "origin", "case_kind", "must_include", "must_not_include"}
LISTS = {"required_behavior", "forbidden_behavior", "must_include", "must_not_include"}
ENUMS = {"severity": {"low", "medium", "high", "critical"}, "origin": {"observed", "synthetic"}, "case_kind": {"trigger", "anti_trigger"}}

def validate_record(obj, allowed):
    if not isinstance(obj, dict):
        return ["record must be an object"]
    errors = []
    missing = REQUIRED - obj.keys()
    if missing:
        return [f"missing keys: {sorted(missing)}"]
    for key in ("id", "task_type", "prompt", "failure_class"):
        if not isinstance(obj[key], str) or not obj[key].strip():
            errors.append(f"{key} must be a non-empty string")
    for key in LISTS:
        value = obj[key]
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            errors.append(f"{key} must be a list of non-empty strings")
        elif key in {"required_behavior", "forbidden_behavior"} and not value:
            errors.append(f"{key} must not be empty")
    for key, choices in ENUMS.items():
        if not isinstance(obj[key], str) or obj[key] not in choices:
            errors.append(f"invalid {key}")
    if isinstance(obj["task_type"], str) and obj["task_type"] not in allowed:
        errors.append("task_type must reference an existing module or core")
    if errors:
        return errors
    for required in obj["must_include"]:
        for forbidden in obj["must_not_include"]:
            if forbidden in required:
                errors.append("contradictory exact checks")
    if set(obj["required_behavior"]) & set(obj["forbidden_behavior"]):
        errors.append("contradictory behavioral requirements")
    # Interpretation and negation make substring bans unsafe outside exact tasks.
    if obj["task_type"] != "precision" and (obj["must_include"] or obj["must_not_include"]):
        errors.append("non-precision cases must use semantic grading, not substring checks")
    return errors

def validate_suite(root):
    modules = {p.stem for p in (root / "docs/protocols").glob("*.md")}
    allowed = modules | {"core"}
    errors, records, seen = [], [], set()
    files = sorted((root / "evals").glob("*.jsonl"))
    if not files:
        errors.append("no eval files")
    for path in files:
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not lines:
            errors.append(f"{path.name}: empty eval file")
        for number, line in enumerate(lines, 1):
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                errors.append(f"{path.name}:{number}: invalid JSON")
                continue
            issues = validate_record(obj, allowed)
            errors.extend(f"{path.name}:{number}: {issue}" for issue in issues)
            if issues:
                continue
            if obj["id"] in seen:
                errors.append(f"duplicate id: {obj['id']}")
            seen.add(obj["id"])
            records.append(obj)
    for module in sorted(allowed):
        kinds = {r["case_kind"] for r in records if r["task_type"] == module}
        for kind in {"trigger", "anti_trigger"} - kinds:
            errors.append(f"{module}: missing {kind} coverage")
    return errors, records

def main():
    errors, records = validate_suite(ROOT)
    for error in errors:
        print(f"FAIL: {error}")
    if not errors:
        print(f"OK: {len(records)} eval specifications validated; no model responses graded.")
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
