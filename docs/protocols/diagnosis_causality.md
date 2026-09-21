# Risk module: Diagnosis and causality

## Risk

Premature causal stories, shotgun fixes, or changing several variables before observing hidden state.

## Use when

Failures are intermittent, context-dependent, machine-specific, or could arise at multiple layers; also when observational evidence is being used to infer mechanism.

## Skip when

The error deterministically names the cause and a bounded fix is already verified.

## Invariants

- State before story: inspect the supplied evidence and current environment first.
- Hypotheses are optional tools, not required headings; use competing explanations only when underdetermination is material.
- Choose the smallest reversible test that best separates live explanations.
- Change one load-bearing variable at a time and rerun the original reproduction.
- Stop when the experienced symptom is resolved unless a postmortem is requested.

## Minimal checks

Capture the exact symptom, reproduction, versions, and recent changes. Identify the best separator between plausible layers. Apply the minimum supported fix and verify the original failure path.

## Escalate when

The next step is destructive, evidence conflicts, rollback is unclear, or the failure affects safety or irreplaceable data.
