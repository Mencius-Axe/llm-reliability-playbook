# Evals

Each `.jsonl` file contains one JSON object per line:

Required keys:
- `id` (string, unique across all evals)
- `task_type` (one of: symbol_level, arithmetic_units, perceptual_ocr, debugging_hidden_state, recency_facts, speculative_theory)
- `prompt` (string)
- `must_include` (list of strings)
- `must_not_include` (list of strings)

Intended use:
- These are *tiny regression tripwires* for common failure modes.
- They are checked in CI for schema + basic quality (unique IDs, known task types, non-empty patterns).
- They are not an automated LLM harness; they’re meant to be run manually (copy prompt → model → verify includes/excludes) or integrated into a harness later.
