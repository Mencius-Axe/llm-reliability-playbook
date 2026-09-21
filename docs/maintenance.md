# Maintenance policy

## Admission threshold

Add or change a rule only when a repeated or material failure suggests a reusable countermeasure. Prefer modifying an existing invariant over adding another rule. Do not encode one-off preferences or preserve obsolete scaffolding.

## Required evidence

For each material intervention, capture:

- failure hypothesis and severity;
- required and forbidden behavior;
- at least one trigger case and, when over-activation is plausible, one anti-trigger;
- origin (`observed` or `synthetic`);
- linked module;
- model, reasoning setting, tools, harness/context, retry policy, and budget when comparing configurations.

## Evaluation

Use deterministic checks for exact properties and semantic rubric/human review for behavioral outcomes. Grade the experienced end state, not a prescribed reasoning path. Track correctness plus avoidable turns, questions, tool calls, repeated retrieval, response size, latency, and cost when available.

Keep some unseen or freshly generated variants outside the public regression set when estimating generalization.

## Retirement

Periodically compare the countermeasure against a no-countermeasure baseline on current model/configuration. Simplify or remove it when it no longer improves substantive outcomes or its intervention cost exceeds avoided error.

Structural changes use a branch and pull request. Keep the repository concise and delete superseded or conflicting rules.
