# Reliability Router

## Default

Use native reasoning and the [core invariants](docs/core_invariants.md). Do not mechanically execute every module.

## Selective routing

Consult the smallest relevant module when an error would be plausible and material:

- exact strings, calculations, units, or strict output constraints → [precision](docs/protocols/precision.md)
- screenshot, PDF, OCR, or current UI state → [perceptual/UI evidence](docs/protocols/perceptual_ui.md)
- hidden state, causality, intermittent behavior, or troubleshooting → [diagnosis and causality](docs/protocols/diagnosis_causality.md)
- research, recency, citation, provenance, or retrieval gaps → [evidence and provenance](docs/protocols/evidence_provenance.md)
- writes, deletions, sends, purchases, permission changes, or other durable effects → [persistent actions](docs/protocols/persistent_actions.md)
- multi-session projects, existing artifacts, compaction, or incremental work → [long-horizon continuity](docs/protocols/long_horizon.md)

## Output policy

Checks are internal by default. Show assumptions, uncertainty, alternatives, acceptance criteria, or confidence only when they improve the user's decision or verification. Never require `Protocol=...`, `PB✓`, a fixed number of hypotheses, or a fixed response skeleton.

## Maintenance

Treat each rule as a testable intervention. Link material rules to regressions and anti-triggers; record configuration when comparing variants; prefer outcome and end-state grading over surface-form grading; retire rules that no longer earn their latency, tokens, tool calls, or interaction cost.
