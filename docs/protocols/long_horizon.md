# Risk module: Long-horizon continuity

## Risk

Constraint loss, rebuilding instead of patching, partial-state confusion, compaction drift, and declaring a project complete before end-to-end verification.

## Use when

Work spans many files, tools, turns, sessions, or handoffs; an existing artifact is being revised; or canonical requirements and current implementation may differ.

## Skip when

The task is small, stateless, and fully represented in the current request.

## Invariants

- Inspect the complete current state and authoritative sources before changing it.
- Preserve approved wording, decisions, interfaces, and unrelated work.
- Maintain a compact ledger of constraints, decisions, unresolved risks, and definition of done.
- Work in bounded increments: inspect → change → verify → record state.
- Treat summaries and memory as indexes, not substitutes for current artifacts.
- Verify end-to-end behavior before claiming completion.

## Minimal checks

Identify authoritative inputs and current implementation, diff them, choose the smallest coherent increment, run relevant checks, and leave a durable progress record that distinguishes done, pending, and blocked.

## Escalate when

Authoritative sources conflict, the workspace is dirty in overlapping areas, compaction lost a load-bearing decision, or the next increment would require redesign rather than patching.
