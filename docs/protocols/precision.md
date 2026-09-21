# Risk module: Precision

## Risk

Silent mutation of exact strings, incorrect arithmetic or units, and loss of strict output constraints.

## Use when

Exact characters, identifiers, paths, commands, quotations, calculations, rates, percentages, units, rounding, or paste-ready formats affect correctness.

## Skip when

Variation is harmless and numbers are illustrative.

## Invariants

- Preserve authoritative strings verbatim; mark ambiguity `UNCLEAR` rather than normalizing it.
- Carry units through consequential calculations; distinguish percentage points from relative percent change.
- Respect the user's shell, environment, container, and output limits.
- Do not ship placeholders as completed output.

## Minimal checks

Extract exact inputs before transforming them. Calculate with units and round at the end. Use a second decomposition or order-of-magnitude check only for nontrivial or consequential results. Validate paste safety or run the artifact when practical.

## Escalate when

The source glyph is ambiguous, a unit definition changes the answer, or an exact value cannot be verified.
