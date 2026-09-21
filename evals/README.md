# Evals

These are regression specifications, not a complete automated model harness.

Each JSONL record requires:

- identity: `id`, `task_type`, `failure_class`, `origin`, `case_kind`, `severity`
- task: `prompt`
- semantic rubric: `required_behavior`, `forbidden_behavior`
- optional deterministic checks: `must_include`, `must_not_include`

`case_kind` is `trigger` or `anti_trigger`. Semantic behaviors require rubric/model or human grading; exact strings remain appropriate for symbol and arithmetic cases. Comparative runs should record model/configuration, tools, context, retries, budget, substantive pass/fail, turns, questions, tool calls, tokens, latency, and cost when available.

Public cases are regressions, not holdouts. Use unseen or freshly generated variants to test generalization.
