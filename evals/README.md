# Evals

These are regression specifications, not a complete automated model harness.

Each JSONL record requires:

- identity: `id`, `task_type`, `failure_class`, `origin`, `case_kind`, `severity`
- task: `prompt`
- semantic rubric: `required_behavior`, `forbidden_behavior`
- optional deterministic checks: `must_include`, `must_not_include`

`case_kind` is `trigger` or `anti_trigger`. Semantic behaviors require rubric/model or human grading; exact strings remain appropriate for symbol and arithmetic cases. Comparative runs should record model/configuration, tools, context, retries, budget, substantive pass/fail, turns, questions, tool calls, tokens, latency, and cost when available.

Public cases are regressions, not holdouts. Use unseen or freshly generated variants to test generalization.

## Validation versus grading

`make check` validates specifications and runs validator regression tests. It never calls a model and cannot establish behavioral improvement. `task_type` links each case to a module filename (without `.md`) or `core`; each module and core require trigger and anti-trigger coverage. This is minimum coverage, not proof that every invariant is tested.

Both behavioral lists must be nonempty. Non-precision cases use empty exact-check lists: substring bans cannot distinguish recommending an action from warning against it. For precision cases, exact checks are supplemental; numeric equivalence and requested formatting still need an appropriate grader. A semantic grader should record pass/fail/uncertain for each rubric item with evidence from the response or action trace, rather than treating a valid schema as a passing answer.
