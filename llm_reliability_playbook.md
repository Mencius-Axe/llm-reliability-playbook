# LLM Reliability Playbook (seed)

This file is the compact index for the repo. Use it when you want a fast, repeatable way to reduce common LLM failure modes.

## Failure-Point Index
Route the task to a protocol:

- **Symbol-level** (strings/IDs/paths/commands): `docs/protocols/symbol_level.md`
- **Arithmetic + units** (numbers/percent/units/time): `docs/protocols/arithmetic_units.md`
- **Perceptual / OCR / UI / PDF** (screenshots, glyphs, tables): `docs/protocols/perceptual_ocr.md`
- **Debugging** (hidden state/config/drivers/network): `docs/protocols/debugging_hidden_state.md`
- **Recency + facts** (time-sensitive claims): `docs/protocols/recency_facts.md`
- **Speculation** (underdetermined “why”): `docs/protocols/speculative_theory.md`
- **Acceptance criteria (definition of done)**: `docs/protocols/acceptance_criteria.md`

## Global modules
- Anti-sycophancy guardrails: `docs/protocols/anti_sycophancy.md`
- Calibration format: `docs/protocols/calibration.md`

## Default output requirements
- If exact strings matter: extract + index verbatim; mark `UNCLEAR` instead of guessing.
- If numbers matter: step-by-step with units + alternate decomposition.
- If images/UI/PDF: transcribe verbatim first; mark unclear glyphs; request crop/zoom.
- If debugging: H1 vs H2 + one discriminating test (iterate).
- If recency-sensitive: browse + cite load-bearing claims.
- Always end with: `Confidence X/5; would change if Y.`
