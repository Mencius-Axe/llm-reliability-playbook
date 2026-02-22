# Protocol: Perceptual / OCR / UI / PDF

## Triggers
Use this protocol when:
- Reading from screenshots, UI, PDFs, scanned docs, photos
- Small glyph differences matter (0/O, 1/l/I, punctuation, diacritics)
- The output will be used verbatim (IDs, codes, commands, settings)

## Anti-triggers
Do not use when:
- The user only wants a high-level description and exact text is non-critical
- The image is decorative (no semantic extraction needed)

## Minimal procedure (≤10 steps)
1. **Transcribe verbatim first** (no interpretation). Keep line breaks.
2. **Mark uncertainty explicitly** with `UNCLEAR` for any glyph/word you can’t read.
3. **Do not “correct”** typos; preserve exactly what is visible.
4. If any `UNCLEAR` remains, request a **crop/zoom** or higher-resolution capture of the specific region.
5. Separate **what is seen** (verbatim) from **what is inferred** (interpretation).
6. For tables, preserve **row/column structure**; keep headers.
7. For settings/UIs, capture **paths** (menu → submenu → option) as displayed.
8. Provide a **copy-paste safe** block for extracted text.
9. If needed, offer a **verification step** (e.g., user re-checks a highlighted region).
10. Append **calibration**: `Confidence X/5; change if Y`.

## Common failure modes
- Guessing unclear glyphs and “filling in” missing text
- Normalizing punctuation/quotes and changing meaning
- Losing layout (table rows collapse; labels detach from values)
- Confusing similar icons/states (toggle on/off, enabled/disabled)
- Over-trusting OCR output without cross-checking

## Worked examples

### Example A — Ambiguous glyph
**Input:** “WAN IP: 209.195.???.???”
**Good:**
- “WAN IP: 209.195.UNCLEAR.UNCLEAR”
- Request: crop the last octets; avoid guessing

### Example B — UI path
**Input:** A screenshot showing a setting nested in menus
**Good:**
- `Settings → Network → Advanced → DNS → Manual`
- Transcribe the on-screen labels exactly

## Discriminating tests
- Ask for a **tight crop** (2–4× zoom) of the ambiguous region
- Ask for a **second capture** with different zoom/contrast
- If text is selectable, request the user to **copy/paste** it instead of OCR
