# P032 — Cycles of a Uniform Random Permutation

## Metadata

- Category: Probability
- Tags: Cycle Counting, Disjoint Events, Harmonic Sums
- Date Added: 2026-10-22
- Original drill dates: 2026-10-17
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-17 Q2

Source and assessment: [2026-10-17 Q2](../../DailyTests/2026-10-17.md#q2--cycles-of-a-uniform-random-permutation). The reference material below does not change that attempt’s recorded result.

### Question

Choose a permutation $`\pi`$ uniformly from all permutations of $`\{1,\ldots,n\}`$, with $`n\ge2`$. Starting at 1, repeatedly apply the same permutation until returning to 1. Let L be the number of distinct labels visited, including 1. Derive the distribution of L. Find the probability that any cycle has length strictly greater than $`n/2`$, and its limit as n tends to infinity. Justify counting; a finite sum is acceptable.

### Key solution

The user's independent chain argument gives:

```math
P(L=\ell)=\left(\prod_{j=1}^{\ell-1}\frac{n-j}{n-j+1}\right)\frac1{n-\ell+1}=\frac1n,
\qquad \ell=1,\ldots,n.
```

Factors are conditional probabilities, not an independence assertion. A long cycle uses more than half the labels, so at most one can exist. For fixed length $`\ell\gt n/2`$, choose its labels, arrange them in one cycle and permute the remainder:

```math
\binom n\ell(\ell-1)!(n-\ell)!=\frac{n!}{\ell}.
```

Each qualifying permutation is counted once. Distinct long-cycle lengths are mutually exclusive, hence:

```math
P(\text{some cycle longer than }n/2)
=\sum_{\ell=\lfloor n/2\rfloor+1}^{n}\frac1\ell
\longrightarrow\int_{1/2}^1\frac{dx}{x}=\ln2.
```

The probability all cycles are at most half the size is one minus this sum. If C counts long cycles, then C is zero or one and $`E[C]=P(C=1)`$.

## Assessment history

- [2026-10-17 Q2 — assessment](../../DailyTests/2026-10-17.md#q2--cycles-of-a-uniform-random-permutation)

## Related questions and knowledge

- [P025 — Permutation Fixed Points and Dependent Indicators](P025_Permutation_Fixed_Points_and_Dependent_Indicators.md) — Uniform permutations; fixed-point indicators versus cycle counting.
- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — Knowledge card.
