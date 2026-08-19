# Audit report

## Executive result

All six source-anchored construction audits pass their scoped evidence
contracts. The package combines exact symbolic proof routes, independent
checkers, negative controls, and a Lean 4.32.0 reusable core. It does not claim
that finite traces replace the paper’s proofs.

Overall status:

`ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_AND_EXACT_AUDITS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE`

## Claim matrix

| Claim | Result | Primary route | Main boundary |
| --- | --- | --- | --- |
| C1 | `VERIFIED_SCOPED` | Replay burn-in conversion and support-closure proof | Finite route supports the universal source proof |
| C2 | `VERIFIED_SCOPED` | Symbolic arbitrary-threshold adversarial trace | Source proof supplies unrestricted threshold quantifier |
| C3 | `VERIFIED_SCOPED` | Witness Protection termination/criticality/protection audit | Lean checks reusable cores, not every paper definition |
| C4 | `VERIFIED_SCOPED` | Marker stabilization and all-phase diagonalization | No finite phase prefix is treated as universal |
| C5 | `VERIFIED_SCOPED` | Generator-indexed MQ lower-bound dichotomy | Source-level temporal invariants remain explicit |
| C6 | `VERIFIED_SCOPED` | Exact four-branch half-line and cell-partition routes | Exact integer domain and proper/no-replay sides are scoped |

Open the [claim ledger](CLAIM_EVIDENCE.md) for production paths and controls,
the [source audit](SOURCE_AUDIT.md) for version mapping, and the
[detailed report](reports/replay-reproduction/report.md) for the full evidence
ladder.

## Score and publication boundary

The external judge’s **6/12** result is historical and remains the only score
claimed. The current local publication gate passed, but no score increase has
been observed:

- `current_score_claim`: `false`
- `publication_allowed`: `false`
- `official_author_endorsement`: `false`

This repository is an independent reproduction audit and does not imply
endorsement by the paper’s authors.
