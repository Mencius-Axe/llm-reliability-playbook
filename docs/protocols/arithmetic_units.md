# Protocol: Arithmetic + units

## Triggers
Use this protocol when:
- Any numeric output affects decisions (costs, dosage, rates, time, conversions)
- Multi-step calculations, mixed units, percentages vs percentage points
- Aggregations (totals, averages, weighted means), rounding matters

## Anti-triggers
Do not use when:
- Numbers are illustrative only and user explicitly says precision doesn’t matter

## Minimal procedure (≤10 steps)
1. **Restate givens** with units (as a list).
2. **State the target quantity** and required units.
3. **Dimensional check**: ensure units cancel correctly.
4. Compute step-by-step with **intermediate results** (carry units).
5. **Alternative decomposition** (second way) to confirm the result.
6. Track **rounding policy** (where rounding happens; keep extra digits until the end).
7. If ambiguity exists (e.g., “MB” vs “MiB”), **branch** into two cases and label.
8. Provide a **sanity range** check (order-of-magnitude).
9. If presenting multiple figures, keep **consistent significant figures**.
10. Append **calibration**: `Confidence X/5; change if Y`.

## Common failure modes
- Dropping units mid-stream
- Percent vs percentage points confusion
- Treating rates as totals (or vice versa)
- Rounding too early
- Mixing base-10 and base-2 units (MB vs MiB, GB vs GiB)
- Calendar/timezone and inclusive/exclusive interval errors

## Worked examples

### Example A — Percent vs percentage points
**User:** "CTR went from 2% to 3%. What’s the increase?"
**Good:**
- Absolute change: 3% − 2% = **+1 percentage point**
- Relative change: (3% / 2%) − 1 = **+50%**

### Example B — Rate × time with units
**User:** "I drive 80 km/h for 30 minutes. How far?"
- 30 min = 0.5 h
- Distance = 80 km/h × 0.5 h = **40 km**
Alt check: half an hour at 80 → half of 80 = 40.

## Discriminating tests
- Unit consistency: write the expression and cancel units explicitly
- Cross-check using a back-of-envelope estimate (orders of magnitude)
