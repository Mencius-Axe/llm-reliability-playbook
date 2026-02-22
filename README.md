# LLM Reliability Playbook

A compact set of *procedures* for reducing predictable LLM failure modes (symbol-level errors, arithmetic/units slips, OCR/perception mistakes, debugging ambiguity, recency drift, and speculative overreach).

## How to use (fast)
1. Identify the task type using the **Failure-Point Index**.
2. Apply the corresponding **protocol** (minimal steps, then a discriminating test if needed).
3. For factual/recency-sensitive claims: **browse + cite** sources.
4. Append **Calibration**: `Confidence X/5; would change if Y`.

## What’s inside
- `llm_reliability_playbook.md` — original seed/index
- `docs/` — expanded protocols with triggers, steps, failure modes, and worked examples
- `templates/` — copy/paste snippets for prompts and reviews
- `evals/` — tiny test sets to catch regressions
- `.github/workflows/` — CI checks (structure + schemas)

## Repository map (planned)
