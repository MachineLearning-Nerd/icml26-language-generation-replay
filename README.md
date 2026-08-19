# ICML 2026 — Language Generation with Replay

Independent, claim-by-claim reproduction audit for [Language Generation with Replay: A Learning-Theoretic View of Model Collapse](https://arxiv.org/abs/2603.11784).

| Field | Value |
| --- | --- |
| Paper | [arXiv:2603.11784](https://arxiv.org/abs/2603.11784) |
| Authors | Giorgio Racca, Michal Valko, Amartya Sanyal |
| ICML submission | `scnRgI2hhX` |
| Repository | [MachineLearning-Nerd/icml26-language-generation-replay](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay) |
| Local evidence | Six source-anchored audits marked `VERIFIED` |
| Historical live result | `6/12`; no new judge score is claimed here |

## Audit record

- Overall status: `ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_AND_EXACT_AUDITS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE`
- Scope: six source-anchored theorem/construction audits with Lean-checked reusable cores and independent controls
- Current score claim: none; `6/12` is historical external context only
- Publication gate: passed; author endorsement: not claimed
- Standard audit surfaces: [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md), [REPORT.md](REPORT.md), [STATUS.md](STATUS.md), [SOURCE_AUDIT.md](SOURCE_AUDIT.md), and [verify_final.py](verify_final.py)

## What the paper studies

The paper asks what happens when a language generator's earlier outputs can be
replayed as future training examples. Its results compare uniform generation,
non-uniform generation, generation in the limit, and proper generation with and
without replay. The central message is asymmetric: replay preserves the
strongest uniform guarantee, but can separate weaker generation notions and can
make proper generation impossible.

This repository audits the paper's exact constructions. The executable checks
are finite or symbolic evidence for the proof mechanisms; the paper's proofs
remain the authority for their universal quantifiers. A passing audit is not a
claim that a finite run alone proves a universal theorem.

## Claim-to-evidence ledger

| Claim | Paper result and source anchor | How the result is produced here | Evidence and control | Status |
| --- | --- | --- | --- | --- |
| C1 | Uniform generation with replay has the same optimal sample complexity as ordinary uniform generation. Prompt Theorem 3.1; arXiv v2 Theorem 4.1, Algorithm 1. | `repro/src/c1_proof.py` executes the burn-in conversion and `c1_checker.py` independently checks its proof DAG. `ReplayCore.lean` checks the support-closure and same-threshold core. | Replay-tree audit; unsupported pre-burn-in outsider is a rejecting control. See `.openresearch/artifacts/claim_1/`. | `VERIFIED` |
| C2 | A countable class separates non-uniform generation with and without replay. Prompt Theorem 4.1; arXiv v2 Theorem 5.1. | `c2_proof.py` keeps thresholds `d` and `m` symbolic, constructs the `h∞`/`h_d` adversarial trace, and proves the exact intersection obstruction. | `c2_checker.py` rechecks arbitrary-threshold obligations; removing replay or the finite upper bound is rejected. See `.openresearch/artifacts/claim_2/`. | `VERIFIED` |
| C3 | Witness Protection generates every countable UUS class in the limit under replay using membership queries. Prompt Theorem 5.1; arXiv v2 Theorem 6.1, Algorithm 2. | `c3_proof.py` transcribes termination, eventual target criticality, witness protection, and fresh valid output; Lean checks reusable monotonicity and support cores. | Independent proof-DAG checker; allowing a protected witness to be output is rejected. See `.openresearch/artifacts/claim_3/`. | `VERIFIED` |
| C4 | An uncountable class is limit-generatable without replay but not with replay. Prompt Theorem 5.6; arXiv v2 Theorem 6.6. | `c4_proof.py` follows the marker-stabilization and phase construction for every symbolic phase; Lean checks the diagonal and infinitely-often-error implications. | Six-phase construction audit plus independent all-phase checker; removing replayed markers is rejected. See `.openresearch/artifacts/claim_4/`. | `VERIFIED` |
| C5 | No deterministic membership-query-only generator can properly generate every countable class in the limit. Prompt Theorem 6.1; arXiv v2 Theorem 7.1, Algorithm 3. | `c5_proof.py` audits the arbitrary-generator construction and its two exhaustive cases: infinitely many non-`h1` outputs or an eventual `h1` trap. | Independent lower-bound checker; removing the final trap is rejected. See `.openresearch/artifacts/claim_5/`. | `VERIFIED` |
| C6 | A four-member class is properly generatable without replay but impossible to properly generate in the limit with replay. Prompt Theorem 6.3; arXiv v2 Theorem 7.3. | `c6_exact.py`, `c6_cell_solver.py`, and Lean exhaust all four first-output cases over exact half-line predicates and singleton exceptions. | Structural route, seven-cell route, and independent checker agree; removing replayed exceptions is rejected. See `.openresearch/artifacts/claim_6/`. | `VERIFIED` |

## Reproduce the audit

From `main`, the fixed entrypoint is:

```bash
uv sync --frozen --no-dev && \
  uv run --no-sync python repro/src/check_lean_certificate.py && \
  uv run --no-sync python repro/src/verify.py && \
  uv run --no-sync python repro/src/publication_gate.py
```

The repository is deterministic, CPU-only, and uses no seeds, GPU, paid API,
or finite-window inference for the reported symbolic mechanisms. The complete
claim bundles contain the method, source audit, raw result, independent checker,
negative control, command, and limitations files.

Useful entry points:

- [Current results](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/RESULTS.md)
- [Primary-source audit](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/docs/SOURCE_AUDIT.md)
- [Detailed reproduction report](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/reports/replay-reproduction/report.md)
- [Verifier](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/repro/src/verify.py)
- [Lean certificate](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/repro/formal/ReplayCore.lean)
- [Historical judge-facing report](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/pages/historical-rejected-baseline/page.md)

## Branch organization

`main` is the canonical, cumulative audit. The named branches preserve the
research progression and are intentionally descriptive. The complete lineage
and old-to-new mapping are in [`branch-audit.md`](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay/blob/main/branch-audit.md).

| Branch family | Purpose |
| --- | --- |
| `audit/*` | One baseline or one claim-specific proof/evidence route. |
| `integration/*` | Cumulative claim evidence assembled across routes. |
| `release/*` | Evaluator-visible and Space/release checks. |

The old `orx/*` names were implementation-stage labels. They are not part of
the published branch interface. There are 12 clean branches including `main`,
and all reachable commits are attributed to `MachineLearning-Nerd`.

## Citation

```bibtex
@article{racca2026language,
  title         = {Language Generation with Replay: A Learning-Theoretic View of Model Collapse},
  author        = {Racca, Giorgio and Valko, Michal and Sanyal, Amartya},
  journal       = {arXiv preprint arXiv:2603.11784},
  year          = {2026},
  doi           = {10.48550/arXiv.2603.11784}
}
```

## Thank you

Thank you to Giorgio Racca, Michal Valko, and Amartya Sanyal for making the
paper, proof ideas, and source-level theorem structure available. That clarity
made it possible to audit the replay constructions claim by claim and to keep
the evidence boundaries explicit.

This repository is an independent reproduction audit maintained by
**MachineLearning-Nerd**. It is not the authors' official implementation and
does not imply author endorsement.

## Attribution and scope

The paper, theorem statements, and research contribution belong to the cited
authors. The scripts, certificates, evidence packaging, branch cleanup, and
documentation in this repository are the independent work of
**MachineLearning-Nerd**. The historical `6/12` is retained for transparency;
only a future external judge can change it.
