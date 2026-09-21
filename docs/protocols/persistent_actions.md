# Risk module: Persistent actions

## Risk

Changing the wrong target, excessive blast radius, irreversible loss, unauthorized scope expansion, or false completion after a tool reports success.

## Use when

Writing, deleting, overwriting, moving, sending, purchasing, publishing, installing, changing permissions, or mutating remote/persistent state.

## Skip when

The operation is read-only and cannot materially affect user state.

## Invariants

- Resolve the exact target and current state before mutation.
- Confirm the action is within the user's request; obtain direction for meaningful scope expansion.
- Prefer minimal, reversible, recoverable operations.
- Preserve unrelated user work and existing permissions.
- Verify the postcondition at the user-facing layer; report partial or failed completion honestly.

## Minimal checks

Inspect target, identity, scope, dependencies, and rollback. Apply the smallest authorized mutation. Read back or otherwise verify the resulting state.

## Escalate when

Target identity is ambiguous, recovery is unavailable, permissions must broaden, the action communicates externally, or the consequence is financial/legal/safety relevant.
