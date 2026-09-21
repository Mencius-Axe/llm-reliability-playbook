# Contributing

Read `docs/maintenance.md` before changing a rule.

## Modules

Each risk module states:

- **Risk** — failure being prevented.
- **Use when / Skip when** — trigger and anti-trigger.
- **Invariants** — outcomes that must hold.
- **Minimal checks** — smallest useful intervention.
- **Escalate when** — conditions requiring more evidence or caution.

## Evals

JSONL records require `id`, `task_type`, `prompt`, `failure_class`, `required_behavior`, `forbidden_behavior`, `severity`, `origin`, `case_kind`, `must_include`, and `must_not_include`. Include/exclude strings may be empty; they are for genuinely deterministic properties, not proxies for reasoning quality.

Pair trigger cases with anti-triggers when a safeguard could over-activate. Run `make check` before opening a pull request.
