# Protocol: Speculation (competing models required)

## Triggers
Use this protocol when:
- The question is underdetermined and invites theorizing
- Mechanisms are unclear, data is sparse, or multiple explanations fit
- The user asks for “why” beyond available evidence
- Stakes are non-trivial and wrong narratives could mislead decisions

## Anti-triggers
Do not use when:
- The user wants a direct factual answer and the evidence is available
- The question is purely creative and correctness is not the objective

## Minimal procedure (≤10 steps)
1. State what is **observed/assumed** vs what is **unknown**.
2. Propose **≥2 plausible models** (M1, M2) that explain the observations.
3. For each model, list **distinct predictions** (what should be true if the model is right).
4. Identify **separating evidence/tests** (one or two that best discriminate).
5. Note **confounders** that could make the tests ambiguous.
6. Provide the **most decision-relevant** model ranking (if any) and why.
7. If the user must act now, give a **robust action** that is safe under both models.
8. Avoid narrative certainty; keep claims tied to evidence/predictions.
9. Cite sources if you rely on external facts; otherwise label as inference.
10. Append **calibration**: `Confidence X/5; change if Y`.

## Common failure modes
- Presenting one story as “the explanation” when alternatives exist
- Using plausibility as proof (good narrative ≠ true)
- No discriminating predictions (models become unfalsifiable)
- Confusing correlation with mechanism
- Overfitting to a single anecdote

## Worked examples

### Example A — Intermittent symptom with multiple causes
**Observation:** Random disconnects on two PCs, not on two other devices.
- M1: Router/AP band steering or client Wi-Fi driver issue
- M2: ISP/modem instability affecting specific traffic patterns

**Separating tests:**
- Ethernet vs Wi-Fi comparison on same PC
- Same PC on different network
- Router logs correlated with disconnect timestamps

### Example B — Cognitive performance intervention
**Observation:** Performance improved after intervention.
- M1: True causal effect
- M2: Practice/placebo/expectancy or regression to mean

**Separating tests:**
- Counterbalanced sham condition
- Blinded assessment + pre-registered analysis

## Discriminating tests
- Identify a prediction that differs in sign/direction between models (not just magnitude)
- Run a swap test (A/B): change one component/context variable at a time to see which model survives
- Add a negative control (condition where the effect should disappear under M1 but persist under M2, or vice versa)
