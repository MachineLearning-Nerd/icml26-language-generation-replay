# Status — ICML 2026 language generation with replay

**State: VERIFIED — six source-anchored construction audits are published; the historical live judge result remains 6/12.**

- Paper: [arXiv:2603.11784](https://arxiv.org/abs/2603.11784), by Giorgio Racca, Michal Valko, and Amartya Sanyal.
- Submission identifier: `scnRgI2hhX`.
- Claims C1–C6 each have a source anchor, executable audit, independent checker, negative control, and stated scope limitation.
- The Lean certificate checks reusable quantified mechanisms and requires theorem-breaking mutations to fail; it is not presented as a complete formalization of every paper definition.
- The fixed cumulative command is recorded in [README.md](README.md) and each claim artifact's `commands.txt`.
- All reported runs are deterministic and CPU-only; no GPU is required.
- `6/12` is the preserved external/judged baseline. No score increase or forecast is claimed.
