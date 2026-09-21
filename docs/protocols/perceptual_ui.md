# Risk module: Perceptual and UI evidence

## Risk

Inventing unseen labels or state, over-trusting OCR, or detaching extracted content from its layout.

## Use when

Screenshots, photos, scanned PDFs, dense tables, small glyphs, toggles, or current interface navigation are load-bearing.

## Skip when

The image is decorative or a high-level description is enough.

## Invariants

- Anchor claims and instructions to what is actually visible.
- Separate observed content from interpretation.
- Preserve exact text and table relationships when they matter.
- Never invent a menu, button, state, or path from remembered UI.

## Minimal checks

Inspect directly before using OCR. Zoom or crop only the ambiguous region. Use selectable text or a second capture when exactness matters. Map the next instruction to a visible label or ask one discriminating question.

## Escalate when

Resolution prevents a consequential reading, the current screen conflicts with documentation, or navigation would require guessing.
