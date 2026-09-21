import copy
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_evals import validate_record, validate_suite
from check_modules import validate_module, validate_modules, REQUIRED

BASE = {
    "id": "test-1", "task_type": "precision", "prompt": "Return abc exactly.",
    "failure_class": "mutation", "required_behavior": ["preserve abc"],
    "forbidden_behavior": ["mutate abc"], "severity": "high",
    "origin": "synthetic", "case_kind": "trigger",
    "must_include": ["abc"], "must_not_include": ["abd"]
}

class ValidatorTests(unittest.TestCase):
    def check_change(self, **changes):
        obj = copy.deepcopy(BASE)
        obj.update(changes)
        return validate_record(obj, {"precision", "core"})

    def test_valid_record(self):
        self.assertEqual(self.check_change(), [])

    def test_empty_behavior_lists(self):
        for key in ("required_behavior", "forbidden_behavior"):
            with self.subTest(key=key):
                self.assertTrue(self.check_change(**{key: []}))

    def test_unknown_module(self):
        self.assertTrue(self.check_change(task_type="unknown"))

    def test_exact_contradiction_and_substring(self):
        for banned in ("abc", "bc"):
            self.assertTrue(self.check_change(must_not_include=[banned]))

    def test_invalid_severity(self):
        self.assertTrue(self.check_change(severity="nonsense"))

    def test_malformed_types_do_not_crash(self):
        for value in ([], None, 7, "text"):
            with self.subTest(value=value):
                self.assertTrue(validate_record(value, {"precision"}))
        for key in BASE:
            with self.subTest(key=key):
                self.assertTrue(self.check_change(**{key: {}}))

    def test_missing_key(self):
        obj = copy.deepcopy(BASE)
        del obj["prompt"]
        self.assertTrue(validate_record(obj, {"precision"}))

    def test_semantic_bans_are_not_substring_checks(self):
        self.assertTrue(self.check_change(task_type="core"))
        self.assertEqual(self.check_change(task_type="core", must_include=[], must_not_include=[]), [])

    def suite(self, rows):
        module = Path("/fixture/docs/protocols/precision.md")
        eval_file = Path("/fixture/evals/cases.jsonl")
        def glob(path, pattern):
            return [module] if path.name == "protocols" else [eval_file]
        with patch.object(Path, "glob", glob), patch.object(Path, "read_text", return_value="\n".join(json.dumps(x) for x in rows)):
            return validate_suite(Path("/fixture"))[0]

    def test_duplicate_ids(self):
        self.assertTrue(any("duplicate" in e for e in self.suite([BASE, BASE])))

    def test_empty_eval_file(self):
        self.assertTrue(any("empty eval file" in e for e in self.suite([])))

    def test_coverage_missing(self):
        errors = self.suite([BASE])
        self.assertTrue(any("missing anti_trigger" in e for e in errors))

    def test_complete_coverage(self):
        rows = []
        for module in ("precision", "core"):
            for kind in ("trigger", "anti_trigger"):
                row = dict(BASE, id=f"{module}-{kind}", task_type=module, case_kind=kind,
                           must_include=[], must_not_include=[])
                rows.append(row)
        self.assertEqual(self.suite(rows), [])

    def test_no_eval_files(self):
        with patch.object(Path, "glob", return_value=[]):
            self.assertIn("no eval files", validate_suite(Path("/fixture"))[0])

    def test_no_modules(self):
        with patch.object(Path, "glob", return_value=[]), patch.object(Path, "exists", return_value=False):
            self.assertIn("no risk modules", validate_modules(Path("/fixture")))

    def test_heading_only_module(self):
        self.assertEqual(len(validate_module("\n".join("## " + h for h in REQUIRED))), len(REQUIRED))

    def test_valid_module(self):
        self.assertEqual(validate_module("\n".join("## " + h + "\nConcrete content.\n" for h in REQUIRED)), [])

    def test_retired_template_detected(self):
        with patch.object(Path, "glob", return_value=[]), patch.object(Path, "exists", return_value=True):
            self.assertTrue(any("retired template" in e for e in validate_modules(Path("/fixture"))))

    def test_repo_negated_warning_has_no_literal_ban(self):
        rows = [json.loads(line) for line in (ROOT / "evals/system_reliability.jsonl").read_text().splitlines()]
        row = next(r for r in rows if r["id"] == "system-004")
        safe_answer = "Do not delete the project; first locate the only copy."
        self.assertFalse(any(ban in safe_answer for ban in row["must_not_include"]))
        self.assertTrue(row["forbidden_behavior"])  # semantic rubric still required

if __name__ == "__main__":
    unittest.main()
