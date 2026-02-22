# Contributing

## Scope
This repo is a set of short, testable procedures for common LLM failure modes, plus tiny evals and CI checks.

## Adding a protocol
1. Create or edit a file in `docs/protocols/`.
2. Include these required sections (CI enforces them for protocol pages):
   - `# Protocol: ...`
   - `## Triggers`
   - `## Anti-triggers`
   - `## Minimal procedure (≤10 steps)`
   - `## Common failure modes`
   - `## Worked examples`
   - `## Discriminating tests`

## Adding eval items
- Add JSONL records to `evals/*.jsonl`.
- Each line must be valid JSON with keys:
  - `id`, `task_type`, `prompt`, `must_include` (list), `must_not_include` (list)
- Run: `make check`

## Style rules
- Prefer decision procedures over prose.
- Prefer discriminating tests over checklists.
- If uncertainty affects correctness, require an explicit `UNCLEAR` marker + a request for the missing input.

## Pull requests
- Keep PRs small and single-purpose.
- CI must pass (`make check` locally).
