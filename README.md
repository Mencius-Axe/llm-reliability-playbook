# LLM Reliability Playbook

A versioned collection of known failure hypotheses, minimal countermeasures, and regression tests for deciding whether those countermeasures still earn their cost.

This repository is a selective engineering aid, not a mandatory response format or a second system prompt. Apply the [core invariants](docs/core_invariants.md) broadly and consult a risk module only when its failure mode is plausible and consequential. Do not expose routing, checklists, confidence scores, or protocol markers unless they help the user.

## Architecture

- **Core invariants** — source authority, constraint preservation, read-before-write, limited blast radius, end-state verification, and stopping when done.
- **Risk modules** — small checks for precision, perception/UI, diagnosis, evidence, persistent actions, and long-horizon work.
- **Evals and maintenance** — observed regressions, synthetic variants, anti-trigger pairs, efficiency measures, and rule retirement.

Start with [docs/index.md](docs/index.md). Run `make check` after changes.

## Design objective

Maximize expected avoided error per unit of added intervention. A safeguard that no longer improves outcomes, or costs more than it prevents, should be simplified or retired.
