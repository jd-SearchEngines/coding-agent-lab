# Season 1 experiment protocol

Each case is copied to a fresh temporary workspace before a run. The agent
receives the task text and can only observe the workspace through its command
environment. Verification is an external `pytest -q` process run after the
agent stops; the model's `DONE` message is never ground truth.

The default local model is `ScriptedModel`, a deterministic protocol fixture.
It validates agent mechanics, evidence persistence, permissions, and recovery
without pretending to measure an LLM. Provider-backed runs require credentials
and are reported as `BLOCKED_BY_MODEL_RUNTIME` when unavailable.

Metrics:

- `pass`: external verification returned code 0.
- `false_finish`: agent self-reported success while external verification failed.
- `steps`: model turns plus tool actions.
- `latency_ms`: wall clock for the agent run plus external verification.
- `cost_usd`: `null` for local scripted runs; no token price is inferred.

No case is removed because it failed. Every run writes a manifest and preserves
the failing command/output in the report evidence pack.

