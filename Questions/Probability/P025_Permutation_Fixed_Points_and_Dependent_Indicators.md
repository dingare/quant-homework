# P025 — Permutation Fixed Points and Dependent Indicators

## Metadata

- Category: Probability
- Tags: Indicators, Covariance, Derangements
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10, 2026-10-14
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q2

Source and assessment: [2026-10-10 Q2](../../DailyTests/2026-10-10.md#q2--random-permutation-fixed-points). The reference material below does not change that attempt’s recorded result.

### Question

Six labeled envelopes are assigned uniformly to six owners. Let $`F`$ count correct returns. Derive $`P(F=0)`$, $`E[F]`$, $`\mathrm{Var}(F)`$ and $`E[F\mid F\gt0]`$ without enumeration code.

### Key solution

Inclusion-exclusion counts assignments fixing a specified subset; indicators give the moments:

```math
P(F=0)=\sum_{k=0}^6\frac{(-1)^k}{k!}=\frac{53}{144},\qquad
F=\sum_{i=1}^6 I_i.
```

```math
P(I_i=1)=\frac16,\quad P(I_i=I_j=1)=\frac1{30},\quad
\mathrm{Cov}(I_i,I_j)=\frac1{180}\quad(i\ne j).
```

```math
E[F]=1,\qquad
\mathrm{Var}(F)=6\frac16\frac56+2\binom62\frac1{180}=1,\qquad
E[F\mid F\gt0]=\frac{E[F]}{P(F\gt0)}=\frac{144}{91}.
```

## Interview drill — 2026-10-14 R1

Source and assessment: [2026-10-14 R1](../../DailyTests/2026-10-14.md#r1--fixed-points). The reference material below does not change that attempt’s recorded result.

### Question

For a uniform permutation of $`n\ge2`$ objects, let $`F`$ count fixed points. Derive its mean and variance, and discuss independence of the fixed-point indicators.

### Key solution

```math
I_i=\mathbf1\{\pi(i)=i\},\quad F=\sum_iI_i,\quad
P(I_i=1)=\frac1n,\quad P(I_i=I_j=1)=\frac1{n(n-1)}\quad(i\ne j).
```

```math
\begin{aligned}
E[F]&=1,\\
\mathrm{Cov}(I_i,I_j)&=\frac1{n(n-1)}-\frac1{n^2}=\frac1{n^2(n-1)},\\
\mathrm{Var}(F)&=n\frac1n\left(1-\frac1n\right)+n(n-1)\frac1{n^2(n-1)}=1.
\end{aligned}
```

## Assessment history

- [2026-10-10 Q2 — assessment](../../DailyTests/2026-10-10.md#q2--random-permutation-fixed-points)
- [2026-10-14 R1 — assessment](../../DailyTests/2026-10-14.md#r1--fixed-points)

## Related questions and knowledge

- [P032 — Cycles of a Uniform Random Permutation](P032_Cycles_of_a_Uniform_Random_Permutation.md) — Uniform permutations; fixed-point indicators versus cycle counting.
- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — Knowledge card.
