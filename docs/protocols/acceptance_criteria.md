# Protocol: Acceptance criteria (definition of done)

## Triggers
- User needs copy/paste-ready commands, patches, or configs
- “Give me the exact …” / “I will paste this into terminal” / formatting-sensitive outputs
- Multi-constraint tasks (format + content + environment) where “almost right” fails

## Anti-triggers
- Pure ideation/brainstorming where no artifact is executed or pasted
- User explicitly says precision/usability constraints don’t matter

## Minimal procedure (≤10 steps)
1. Write 2–5 **Acceptance Criteria (AC)** as checkable bullets (format, environment, constraints).
2. If any AC is ambiguous, ask ≤1 question; else assume and label assumptions.
3. Produce the output artifact.
4. Verify each AC explicitly (pass/fail); patch until all pass.
5. Run **1 red-team probe**: try to break the artifact with an edge case or copy/paste hazard.
6. Add a **sanity check** command (or “how to verify”) when relevant.
7. If long content must be pasted: use **two blocks** (open/create; paste content) and avoid placeholders like `<paste>`.
8. End with calibration: `Conf X/5; change if Y`.

## Common failure modes
- Placeholder tokens (`<paste>`, `<RUN_ID>`, `...`) shipped as “final”
- Commands missing context (wrong cwd, wrong shell, missing deps)
- Output split across blocks such that copy/paste corrupts it
- Conflicting constraints (e.g., “one code block” but includes nested fences)
- No verification path (user can’t tell if it worked)

## Worked examples

### Example A — Terminal-safe file edit
**AC**
- Two blocks only: (1) open/create; (2) paste full content
- No placeholder tokens
- Works in bash/zsh; uses `python3` not `python`
- Includes a `make check` sanity command

**Good**
- Block 1: `nano path/to/file`
- Block 2: full file text
- Follow-up: `make check`

### Example B — Numeric answer with constraints
**AC**
- Restate givens with units
- Step-by-step calc + alt decomposition
- Final rounded only at end
- Provide `Conf X/5; change if Y`

## Discriminating tests
- Placeholder scan: `rg -n '<paste>|<RUN_ID>|\\.\\.\\.|TODO' <files>`
- Shell safety: ensure commands are complete lines (no dangling quotes / heredocs)
- Artifact verification: include at least one “does it exist / does it run” check (e.g., `make check`, `python3 -m py_compile ...`, `[[ -f ... ]]`)
