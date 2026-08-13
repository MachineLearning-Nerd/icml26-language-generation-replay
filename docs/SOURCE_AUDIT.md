# Primary-source audit

## Paper identity

- Title: [Language Generation with Replay: A Learning-Theoretic View of Model Collapse](https://arxiv.org/abs/2603.11784)
- Authors: Giorgio Racca, Michal Valko, and Amartya Sanyal
- Source used for theorem labels: arXiv v2, [HTML](https://arxiv.org/html/2603.11784v2), [abstract and metadata](https://arxiv.org/abs/2603.11784)
- ICML submission identifier: `scnRgI2hhX`
- Retrieved source records: TeX SHA-256 `1014bb49b0b75137488266a641fa179fcd2885c6ea4217501c9e7683758cb1c4`; HTML cross-check SHA-256 `b3220f5cfa110088b01df476f2fdd366fbe6e5088507be9a1f15cfe1c9ebba2b`.

No unreleased code, data, model weights, proprietary API, stochastic sampling,
or GPU is required. The six judged claims are theorem/construction claims.

## Exact source anchors and quantifiers

| Claim | Prompt / arXiv v2 anchor | Domain and exact quantifier audited |
| --- | --- | --- |
| C1 | Prompt Theorem 3.1; `sections/04-uniform-with-replay.tex`, arXiv v2 Theorem 4.1 and Algorithm `alg:uniform_to_uniform_replay` | Every binary class, target, replay sequence, and finite standard complexity `d`; equality of optimal complexities. |
| C2 | Prompt Theorem 4.1; `sections/05-nonuniform-with-replay.tex`, arXiv v2 Theorem 5.1 | Constructed countable class over all integers; every replay generator and arbitrary finite target thresholds `d,m`. |
| C3 | Prompt Theorem 5.1; `sections/06-limit-with-replay.tex`, arXiv v2 Theorem 6.1 and Witness Protection Algorithm 2 | Every countable uniformly unbounded-support class, target index, replay enumeration, and round. |
| C4 | Prompt Theorem 5.6; `sections/06-limit-with-replay.tex`, arXiv v2 Theorem 6.6 and uncountable separation lemmas | Constructed uncountable class; every deterministic generator and every natural adversarial phase. |
| C5 | Prompt Theorem 6.1; `sections/07-proper-generation.tex`, arXiv v2 Theorem 7.1 and Algorithm 3 | Every deterministic computable membership-query-only proper generator. |
| C6 | Prompt Theorem 6.3; `sections/07-proper-generation.tex`, arXiv v2 Theorem 7.3 | Every deterministic proper generator on the exact four-member class over all integers. |

The judge-facing numbering refers to the prompt/earlier paper version. The
current arXiv v2 numbering is recorded above so that a reader can follow both
the evaluator contract and the current source.

## Evidence boundary

`repro/src/verify.py` executes the six constructions and writes the committed
machine-readable results. The independent `c*_checker.py` programs re-check
the emitted certificate schemas. `repro/formal/ReplayCore.lean` checks reusable
universal mechanisms and mutation rejection. These checks support the cited
paper proofs; they do not replace the proofs or turn a finite trace into a
universal theorem.
