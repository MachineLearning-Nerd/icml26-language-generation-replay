# Environment and reproduction boundary

## Locked inputs and command

- Python: `3.12`
- Package manager: `uv`
- Lockfile: [`uv.lock`](uv.lock)
- Lean: `4.32.0` in the formal certificate

Run the cumulative audit from `main` with:

```bash
uv sync --frozen --no-dev
uv run --no-sync python repro/src/check_lean_certificate.py
uv run --no-sync python repro/src/verify.py
uv run --no-sync python repro/src/publication_gate.py
```

The reported mechanisms are deterministic and CPU-only: no GPU, paid API,
random seed, or finite-window inference is required for the symbolic routes.

## Scope

The Lean certificate has no `sorry`, `admit`, `axiom`, or `unsafe` escape in the
audited file and records two premise-changing compile failures. The Python
proof-DAG and independent checkers validate construction details and controls.
The paper’s proofs remain authoritative for universal quantifiers; these
artifacts are not a claim that finite runs replace them.
