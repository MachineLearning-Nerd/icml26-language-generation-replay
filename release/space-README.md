---
title: "Repro - Language Generation with Replay"
emoji: 🎯
colorFrom: yellow
colorTo: red
sdk: static
pinned: false
tags:
 - trackio
 - trackio-logbook
 - open-experiment
 - icml2026-repro
 - paper-scnRgI2hhX
 - theory
 - replay
---

# Repro — Language Generation with Replay

An open experiment logbook for [Language Generation with Replay: A Learning-Theoretic View of Model Collapse](https://arxiv.org/abs/2603.11784) by Giorgio Racca, Michal Valko, and Amartya Sanyal, published with [Trackio](https://github.com/gradio-app/trackio).

## Current candidate evidence

The live judged score remains **6/12**. Six source-anchored proof audits now expose their code directly, with Lean-checked universal cores and fail-closed mutations. This is candidate evidence, not a new judge result.

- [Start with the pinned executive summary](#/executive-summary)
- [Read Claim 1](#/claim-1-current) through [Claim 6](#/claim-6-current)
- [Inspect the retained evidence matrix](#/visibility-matrix)
- [Open the illustrated technical report](reports/replay-reproduction/report.md)
- [Inspect the self-contained marimo notebook](notebooks/replay_reproduction.py)

The new Lean route ran on local CPU; the retained Python evidence ran on Hugging Face `cpu-upgrade`. No GPU was used. Historical evidence remains preserved and is explicitly labeled **Historical rejected baseline**.

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

Thank you to the authors for making the theorem structure and source available
for independent, claim-by-claim auditing.
