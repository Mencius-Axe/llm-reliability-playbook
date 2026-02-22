# Protocol: Recency + facts (time-sensitive)

## Triggers
Use this protocol when:
- The answer could have changed recently (policies, prices, schedules, product specs, roles)
- The user asks for “latest/current/now/today/this week”
- High-stakes domains: medical, legal, financial, safety, compliance
- Precise attribution is required (quotes, claims with provenance)

## Anti-triggers
Do not use when:
- The question is stable background knowledge (history, math, basic science)
- The user explicitly asks you not to browse and the risk is acceptable

## Minimal procedure (≤10 steps)
1. Identify the **load-bearing claims** (what must be true for your answer to hold).
2. Convert each claim into a **targeted query** (include location/date constraints).
3. Prefer **primary sources** (official docs, standards, vendor docs) over summaries.
4. Open **2–4 sources** and extract only what supports the load-bearing claims.
5. Answer with **inline citations per claim** (not just a link dump).
6. If sources disagree, present **both** and state what would resolve the conflict.
7. If information is missing, say so and provide the **best next retrieval step**.
8. Avoid quoting long passages; quote only what is necessary.
9. Distinguish **facts** from **inference** explicitly.
10. Append **calibration**: `Confidence X/5; change if Y`.

## Common failure modes
- Answering from memory when the fact could have changed
- Using one secondary article when primary docs exist
- Citing irrelevant sources that don’t support the specific claim
- Treating “published date” as “effective date” without checking
- Overconfident synthesis when sources conflict

## Worked examples

### Example A — “Who is the current CEO of X?”
- Load-bearing claim: identity of current CEO
- Primary sources: company investor relations, SEC filings, official press release
- Output: one sentence + citation; note effective date if leadership change announced

### Example B — “What are the rules for Y this year?”
- Load-bearing claim: current rule text and effective date
- Sources: official regulator/agency page; the text of the rule; reputable summary if needed
- Output: rule summary + link to the operative text + effective date

## Discriminating tests
- Verify with a primary source that has an **effective date**
- Cross-check with a second independent authoritative source
- For disputed claims: locate the **original document** (policy text, spec sheet, statute)
