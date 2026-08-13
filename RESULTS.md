# Results

This repository audits [Language Generation with Replay: A Learning-Theoretic
View of Model Collapse](https://arxiv.org/abs/2603.11784) by Giorgio Racca,
Michal Valko, and Amartya Sanyal. The six claim bundles are marked
`VERIFIED` by the committed source-anchored audits and independent controls.

| Claim | Paper construction | Executable evidence | Rejecting control |
| --- | --- | --- | --- |
| C1 | Prompt Theorem 3.1; arXiv v2 Theorem 4.1, Algorithm 1 | Exhaustive replay-tree audit of the burn-in conversion plus Lean support-closure core | Unsupported pre-burn-in outsider can be replayed forever |
| C2 | Prompt Theorem 4.1; arXiv v2 Theorem 5.1 | Symbolic `h∞`/`h_d` trace with arbitrary thresholds and exact support intersection | Shared trace is illegal for `h_d` without replay; removing the finite bound breaks the exact obstruction |
| C3 | Prompt Theorem 5.1; arXiv v2 Theorem 6.1, Algorithm 2 | Witness Protection transcription, proof-DAG checker, and checked criticality/validity cores | Emitting a protected witness prevents the required eviction |
| C4 | Prompt Theorem 5.6; arXiv v2 Theorem 6.6 | Marker stabilization and source-faithful phase audit with Lean diagonalization core | Removing marker replay makes the alternative history illegal |
| C5 | Prompt Theorem 6.1; arXiv v2 Theorem 7.1, Algorithm 3 | Arbitrary-generator two-case diagonalization audit and independent checker | Removing the final trap removes the eventual-error branch |
| C6 | Prompt Theorem 6.3; arXiv v2 Theorem 7.3 | Exact half-line, seven-cell, Lean, and independent four-way first-output routes | Removing replayed exceptions invalidates the common adversarial sequence |

## Interpretation

These are proof-level construction audits, not proxy empirical experiments. The
finite executions and symbolic certificates check the stated mechanisms and
controls; the paper's proof supplies the full universal quantifiers. Claim 6
is additionally reconstructed over exact integer predicates rather than the
historical `[-40,40]` window.

The external/judged result remains **6/12** until a judge evaluates a newly
published revision. This repository makes no new score claim.

## Re-run

```bash
uv sync --frozen --no-dev && \
  uv run --no-sync python repro/src/check_lean_certificate.py && \
  uv run --no-sync python repro/src/verify.py && \
  uv run --no-sync python repro/src/publication_gate.py
```

See [docs/SOURCE_AUDIT.md](docs/SOURCE_AUDIT.md),
[reports/replay-reproduction/report.md](reports/replay-reproduction/report.md),
and the per-claim directories under `.openresearch/artifacts/` for the exact
source labels, commands, raw outputs, checkers, controls, and limitations.
