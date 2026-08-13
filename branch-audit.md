# Branch audit

This file records the public branch contract for
[`icml26-language-generation-replay`](https://github.com/MachineLearning-Nerd/icml26-language-generation-replay).
The old `orx/` prefixes described internal experiment-tree stages. They have
been replaced with stable `audit/`, `integration/`, and `release/` names.

| Historical branch | Published branch | What it contains |
| --- | --- | --- |
| `main` | `main` | Canonical cumulative six-claim audit, source mapping, reports, and release metadata. |
| `orx/validated-finite-construction-baseline` | `audit/validated-finite-baseline` | Original finite construction baseline and run metadata. |
| `orx/claim-6-cumulative-proof-evidence` | `integration/c6-cumulative-evidence` | Cumulative Claim 6 route before the later claim certificates. |
| `orx/claim-1-exact-reduction-certificate` | `audit/c1-exact-reduction` | Uniform replay-equivalence conversion and checker. |
| `orx/claim-2-arbitrary-threshold-separation` | `audit/c2-threshold-separation` | Symbolic arbitrary-threshold countable separation route. |
| `orx/claim-3-universal-witness-protection-proof` | `audit/c3-witness-protection` | Witness Protection proof obligations and mutation control. |
| `orx/claim-4-infinite-diagonalization-certificate` | `audit/c4-infinite-diagonalization` | Uncountable-class marker and all-phase diagonalization route. |
| `orx/claim-5-universal-mq-lower-bound-certificate` | `audit/c5-mq-lower-bound` | Generator-indexed membership-query lower-bound route. |
| `orx/c6-exact-structural-certificate` | `audit/c6-exact-structural` | Exact four-hypothesis half-line structural certificate. |
| `orx/c6-smt-independent-certificate` | `audit/c6-smt-independent` | Independent Claim 6 cell-partition certificate. |
| `orx/evaluator-visible-release-candidate` | `release/evaluator-visible-candidate` | Claim pages, visible proof excerpts, and release-candidate packaging. |
| `orx/space-relative-evidence-and-release-audit` | `release/space-relative-audit` | Space-relative evidence, manifest, and release audit. |

## Evidence contract

The canonical claim routes are:

- C1: `repro/src/c1_proof.py` + `c1_checker.py`
- C2: `repro/src/c2_proof.py` + `c2_checker.py`
- C3: `repro/src/c3_proof.py` + `c3_checker.py`
- C4: `repro/src/c4_proof.py` + `c4_checker.py`
- C5: `repro/src/c5_proof.py` + `c5_checker.py`
- C6: `repro/src/c6_exact.py`, `c6_cell_solver.py`, and their independent checkers
- Shared universal cores: `repro/formal/ReplayCore.lean` and `check_lean_certificate.py`

Every published branch carries this audit file and a README. Older branches
remain historical snapshots; `main` is the source of truth for the complete
current evidence bundle. No published branch uses an `orx/` name.
