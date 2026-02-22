
Protocol: Arithmetic + units
Triggers

Use this protocol when:

Any numeric output affects decisions (costs, dosage, rates, time, conversions)

Multi-step calculations, mixed units, percentages vs percentage points

Aggregations (totals, averages, weighted means), rounding matters

Anti-triggers

Do not use when:

Numbers are illustrative only and the user explicitly says precision doesn’t matter

Minimal procedure (≤10 steps)

Restate givens with units (as a list).

State the target quantity and required units.

Dimensional check: ensure units cancel correctly.

Compute step-by-step with intermediate results (carry units).

Alternative decomposition (second way) to confirm the result.

Track rounding policy (keep extra digits; round only at the end unless specified).

If ambiguity exists (e.g., “MB” vs “MiB”), branch into cases and label.

Provide a sanity-range check (order-of-magnitude).

Keep consistent sig figs across reported outputs.

Append calibration: Confidence X/5; change if Y.

Common failure modes

Dropping units mid-stream

Percent vs percentage points confusion

Treating rates as totals (or vice versa)

Rounding too early

Mixing base-10 and base-2 units (MB vs MiB, GB vs GiB)

Calendar/timezone and inclusive/exclusive interval errors

Worked examples
Example A — Percent vs percentage points

User: "CTR went from 2% to 3%. What’s the increase?"
Good:

Absolute change: 3% − 2% = +1 percentage point

Relative change: (3% / 2%) − 1 = +50%

Example B — Rate × time with units

User: "I drive 80 km/h for 30 minutes. How far?"

30 min = 0.5 h

Distance = 80 km/h × 0.5 h = 40 km
Alt check: half an hour at 80 → half of 80 = 40.

Example C — Binary vs decimal units

User: "Convert 5 MiB to bytes."

1 MiB = 1,048,576 bytes

5 MiB = 5 × 1,048,576 = 5,242,880 bytes
Alt check: 1 MiB ≈ 1.05 MB, so 5 MiB ≈ 5.24 million bytes.

Discriminating tests

Unit consistency: write the expression and cancel units explicitly

Cross-check with a second decomposition (rate×time vs distance-per-interval)

Quick order-of-magnitude estimate (should be in the same ballpark)
