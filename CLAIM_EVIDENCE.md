# Claim-to-evidence ledger

This repository audits six source-anchored constructions from *Language
Generation with Replay: A Learning-Theoretic View of Model Collapse*. The
paper-version mapping is explicit in [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md):
the judge-facing prompt numbering is paired with the current arXiv v2
numbering. Lean checks reusable quantified mechanisms; the Python routes and
independent checkers audit the exact constructions and controls.

| Claim | Paper anchor | How the result is produced | Evidence and control | Scope and status |
| --- | --- | --- | --- | --- |
| C1 — uniform replay equivalence | Prompt Theorem 3.1; arXiv v2 Theorem 4.1; Algorithm 1 | `repro/src/c1_proof.py` audits burn-in conversion and same-threshold complexity; `c1_checker.py` independently checks the proof DAG; `ReplayCore.lean` checks support closure. | An unsupported pre-burn-in outsider is a rejecting control; raw result records both complexity directions. | Arbitrary replay support/core plus finite execution support. **VERIFIED_SCOPED** |
| C2 — countable non-uniform separation | Prompt Theorem 4.1; arXiv v2 Theorem 5.1 | `c2_proof.py` keeps thresholds `d` and `m` symbolic, constructs the adversarial `h∞`/`h_d` trace, and checks the exact intersection obstruction. | `c2_checker.py` rechecks arbitrary-threshold obligations; removing replay or the finite upper bound is rejected. | Symbolic arbitrary-threshold construction; source proof supplies the universal quantifier. **VERIFIED_SCOPED** |
| C3 — Witness Protection limit generation | Prompt Theorem 5.1; arXiv v2 Theorem 6.1; Algorithm 2 | `c3_proof.py` audits termination, target criticality, witness protection, and fresh valid output; Lean checks monotonicity and support cores. | The independent proof-DAG checker rejects a protected witness being output. | Countable UUS/replay construction with universal source lemmas. **VERIFIED_SCOPED** |
| C4 — uncountable separation | Prompt Theorem 5.6; arXiv v2 Theorem 6.6 | `c4_proof.py` follows marker stabilization and every symbolic phase; Lean checks Cantor diagonalization and infinitely-often-error implications. | The all-phase checker rejects removal of replayed markers. | Every natural adversarial phase, not a finite phase cutoff. **VERIFIED_SCOPED** |
| C5 — deterministic MQ proper-generation lower bound | Prompt Theorem 6.1; arXiv v2 Theorem 7.1; Algorithm 3 | `c5_proof.py` audits the arbitrary-generator construction and both exhaustive cases; `c5_checker.py` checks the dichotomy. | Removing the final trap is rejected; the two cases are generator-indexed. | Every deterministic computable MQ-only proper generator. **VERIFIED_SCOPED** |
| C6 — four-member replay hardness | Prompt Theorem 6.3; arXiv v2 Theorem 7.3 | `c6_exact.py`, `c6_cell_solver.py`, and `c6_independent.py` exhaust all first-output cases over exact half-line predicates and singleton exceptions. | Removing replayed exceptions is rejected; structural, seven-cell, and independent routes agree. | All integers and all four branches, with proper/no-replay side documented. **VERIFIED_SCOPED** |

## Reading the evidence

- `repro/formal/ReplayCore.lean` and
  `.openresearch/artifacts/formal/lean_certificate.json` are the reusable
  universal proof core. The certificate reports Lean 4.32.0 and 27 checked
  theorem statements; two premise-changing mutations fail compilation.
- `.openresearch/artifacts/claim_1/` through `claim_6/` contain each claim’s
  method, source audit, raw result, checker, negative control, commands, and
  limitations.
- `pages/*-current/` and `release/` are the evaluator-visible package; the
  historical baseline pages remain preserved separately.
- `outputs/verdict.json` and `outputs/publication_gate.json` are the committed
  six-claim machine-readable records.

## Overall result

`ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_AND_EXACT_AUDITS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE`

The historical external judge result remains `6/12`. Internal verification is
not a new score, and this repository does not imply author endorsement.
