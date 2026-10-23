# P031 — Exact Uniform Sampling from a Biased Coin

## Metadata

- Category: Probability
- Tags: Rejection Sampling, Fair Bits, Expected Cost
- Date Added: 2026-10-22
- Original drill dates: 2026-10-15
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-15 Q2

Source and assessment: [2026-10-15 Q2](../../DailyTests/2026-10-15.md#q2--exact-uniform-sampling-from-an-unknown-biased-coin). The reference material below does not change that attempt’s recorded result.

### Question

You have independent coin flips with fixed unknown heads probability $`p\in(0,1)`$. Without estimating/querying $`p`$ or using other randomness, design an algorithm returning an exactly uniform integer from $`\{0,1,\ldots,6\}`$. Give precise pseudocode, prove uniformity and almost-sure termination, derive expected raw flips as a function of $`p`$, and discuss both endpoint limits. Repeated calls must produce independent outputs.

### Key solution

User's valid construction: fix seven distinct ordered six-flip patterns containing exactly three heads and three tails; map them one-to-one to outputs 0–6. Toss independent six-flip blocks. Return the matching output for a selected pattern, otherwise discard the entire block and retry. Fresh calls continue with fresh independent flips.

```math
\binom63=20,\qquad
P(\text{one selected pattern})=p^3(1-p)^3,\qquad
q=P(\text{accepted block})=7p^3(1-p)^3.
```

Conditional on acceptance, each output has probability one seventh. Equivalently, summing over rejected blocks gives the unconditional output probability:

```math
P(\text{output}=r)=\sum_{k=0}^{\infty}(1-q)^k p^3(1-p)^3=\frac17.
```

```math
P(\text{no success in }N\text{ blocks})=(1-q)^N\longrightarrow0,
\qquad
E[\text{blocks}]=\frac1q,\qquad
E[\text{raw flips}]=\frac6q=\frac{6}{7p^3(1-p)^3}.
```

The expected raw-flip cost diverges at either endpoint; at a fair coin it is $`384/7\approx54.86`$. Independent blocks and restarting after a successful block yield independent outputs on repeated calls. No efficiency-optimality claim is made.

## Assessment history

- [2026-10-15 Q2 — assessment](../../DailyTests/2026-10-15.md#q2--exact-uniform-sampling-from-an-unknown-biased-coin)

## Related questions and knowledge

- [P024 — Bayesian Coin Selection and Prediction](P024_Bayesian_Coin_Selection_and_Prediction.md) — Unknown-biased-coin sampling versus Bayesian inference.
