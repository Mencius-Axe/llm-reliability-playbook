# Protocol: Debugging (hidden state / config / drivers / networks)

## Triggers
Use this protocol when:
- Behavior depends on unseen state (cache, config, environment variables, services, drivers)
- Failures are intermittent, context-dependent, or “works on one machine but not another”
- The right fix depends on identifying *which layer* is responsible (app vs OS vs network)

## Anti-triggers
Do not use when:
- The error is deterministic and already names a single missing dependency
- You can reproduce with a 1-line minimal example and the fix is obvious

## Minimal procedure (≤10 steps)
1. **Restate the symptom verbatim** (exact error text + command/action that produced it).
2. **Record the environment** (OS, versions, hardware, network context).
3. Propose **H1 and H2** (two competing explanations, not a long list).
4. Choose **one discriminating test** that separates H1 vs H2 quickly.
5. Run the test and **branch**: interpret A→H1, B→H2.
6. Apply the **minimum-change fix** for the supported hypothesis.
7. Re-run the original reproduction to confirm.
8. If fixed, add a **preventive check** (how to detect recurrence early).
9. If not fixed, update hypotheses based on new evidence and repeat (one test/loop).
10. Append **calibration**: `Confidence X/5; change if Y`.

## Common failure modes
- Shotgun “try these 12 things” without a discriminating test
- Changing multiple variables at once (cannot attribute causality)
- Treating symptoms as causes (e.g., blaming network when it’s DNS cache)
- Ignoring version skew across machines
- Fixing locally but breaking production constraints (permissions, policy, security)

## Worked examples

### Example A — Network vs DNS
**Symptom:** Some sites fail; others work; reconnect “fixes it”.
- H1: DNS resolver / cache issue
- H2: MTU / path-MTU discovery / fragmentation issue

**Discriminating test (one):**
- If DNS: `dig +short example.com @1.1.1.1` works while default resolver fails
- If MTU: large ping fails but small ping works:
  `ping -c 2 -M do -s 1472 1.1.1.1`

### Example B — Driver vs app config
**Symptom:** GUI app black screens after update.
- H1: GPU driver mismatch
- H2: App config corrupted

**Discriminating test (one):**
- Run with a fresh config:
  `env -i HOME="$HOME" XDG_CONFIG_HOME="$(mktemp -d)" <app>`
If it works, supports H2; if not, supports H1.

## Discriminating tests (patterns)
- Strip environment to isolate hidden state: `env -i HOME="$HOME" XDG_CONFIG_HOME="$(mktemp -d)" <command>`
- Split network layers: DNS (`dig`), IP reachability (`ping`), TLS (`curl -v`) — pick one that separates H1 vs H2
- Version truth check across layers: `<tool> --version`, `uname -a`, driver version (if relevant)
