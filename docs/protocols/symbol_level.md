# Protocol: Symbol-level accuracy (strings, IDs, paths, commands)

## Triggers
Use this protocol when correctness depends on exact characters or ordering:
- File paths, URLs, commit hashes, IDs, serials, API keys (redact), flags, CLI commands
- Code that must compile/run
- Quoted text where a single character changes meaning

## Anti-triggers
Do not use when:
- Minor wording variation is acceptable (summaries, brainstorming)
- The user explicitly prefers paraphrase over verbatim

## Minimal procedure (≤10 steps)
1. **Extract the symbols** into a dedicated block (no prose interleaving).
2. **Index each item** (1..n) and keep each item on its own line.
3. **Preserve verbatim** characters, including whitespace, punctuation, and casing.
4. If any symbol is uncertain/ambiguous, **mark it explicitly** as `UNCLEAR` and stop guessing.
5. **Compute/check transforms** only after extraction (e.g., join, split, regex, escaping).
6. When generating a command, include **context**: working directory assumptions + required tools.
7. Provide a **copy-paste safe** block (avoid “smart quotes”; no line wrapping).
8. Add a **sanity check** step the user can run (e.g., `ls`, `which`, `echo`, `test -e`).
9. If multiple variants exist, give **two explicit options** and a discriminating check.
10. Append **calibration**: `Confidence X/5; change if Y`.

## Common failure modes
- Dropped/mutated characters (`-` vs `–`, `'` vs `’`, `O` vs `0`, `l` vs `1`)
- Invisible whitespace/newlines altering meaning
- Incorrect escaping/quoting for the user’s shell (bash/zsh/pwsh)
- Mixing prose into code blocks causing copy/paste corruption
- “Fixing” typos that were actually intentional identifiers

## Worked examples

### Example A — Correct handling (paths)
**User:** "My file is at `/home/me/My Folder/data.csv`. Give me the command to count rows."

**Assistant (good):**
Symbols:
1. `/home/me/My Folder/data.csv`

Command (bash):
```bash
wc -l -- "/home/me/My Folder/data.csv"

