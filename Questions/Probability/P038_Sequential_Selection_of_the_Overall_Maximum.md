# P038 — Sequential Selection of the Overall Maximum

## Metadata

- Category: Probability
- Tags: Sequential Selection, Random Order, Stopping Policy
- Date Added: 2026-11-01
- Original drill: November 1, 2026, Q2
- Status: Discussed November 2. Overall Partial / Hinted; the user's independent steps and later supplied derivations are assessed in the dated log.

## Core Question

You observe n distinct candidate scores in uniformly random order. At each arrival, you learn only how that score ranks among those seen so far. You must select exactly one candidate, and rejection is irreversible. Your objective is to select the overall maximum.

Consider this policy:

- Reject the first r candidates.
- Then select the first candidate whose score exceeds every previously observed score, including rejected candidates.
- If none qualifies, select the final candidate.

Assume $`1\le r\lt n`$.

1. Derive the exact success probability as a function of n and r.
2. Explain how to identify the best integer cutoff for a given n, without enumerating arrival orders.
3. For large n, derive the approximately optimal rejected fraction and corresponding success probability.

Justify the reasoning rather than recalling a named rule. A short derivation is sufficient. Original budget: 13 minutes; actual time Not recorded.

## Solution

### Exact success probability

Let $`J`$ be the position of the overall maximum. Uniform random order gives $`P(J=j)=1/n`$. If $`j\le r`$, the policy rejects the maximum and cannot succeed. For $`j\gt r`$, the policy reaches and selects it precisely when the maximum among the preceding $`j-1`$ candidates lies in the rejected first r positions. Its location is uniform among those preceding positions, so:

```math
P(\text{success}\mid J=j)=\frac{r}{j-1},\qquad r+1\le j\le n.
```

Sum over the disjoint positions of the overall maximum:

```math
P_n(r)=\sum_{j=r+1}^{n}\frac1n\frac{r}{j-1}
=\frac rn\sum_{k=r}^{n-1}\frac1k.
```

There are $`n-r`$ possible positions after the rejected prefix. The sum already includes them individually; multiplying it by another count would double count. Equivalently, multiply the probability $`(n-r)/n`$ that the maximum lies after r by the conditional average of $`r/(j-1)`$ over those positions.

### Best integer cutoff

For $`1\le r\le n-2`$, separate the first summand in $`P_n(r)`$:

```math
\begin{aligned}
n\bigl(P_n(r+1)-P_n(r)\bigr)
&=(r+1)\sum_{k=r+1}^{n-1}\frac1k
-r\left(\frac1r+\sum_{k=r+1}^{n-1}\frac1k\right)\\
&=\sum_{k=r+1}^{n-1}\frac1k-1.
\end{aligned}
```

The tail sum strictly decreases with r. Thus the success probability increases while that sum exceeds one and decreases after it falls below one. For $`n\ge3`$, the first integer r for which $`\sum_{k=r+1}^{n-1}1/k\le1`$ maximizes success; equality makes r and r+1 tied. For n = 2, the only allowed cutoff is r = 1. A single scan of the harmonic tails is sufficient; no permutation enumeration or elementary closed form for the finite-n cutoff is required.

### Large-n limit

For a sequence of cutoffs with $`r/n\longrightarrow\alpha`$ in the interval $`(0,1)`$, the harmonic tail is a Riemann-sum approximation:

```math
\sum_{k=r}^{n-1}\frac1k\longrightarrow
\int_{\alpha}^{1}\frac{dx}{x}
=\log\frac1\alpha.
```

Consequently:

```math
P_n(r)\longrightarrow\alpha\log\frac1\alpha.
```

Its derivative is $`\log(1/\alpha)-1`$, which vanishes at the unique maximum $`\alpha=1/e`$. The large-n rejected fraction and success probability both approach $`1/e`$. At a proposed fraction near one half, the harmonic-tail comparison approaches $`\log2\lt1`$, so increasing the cutoff there already reduces success.

## Connections

- [P026 — Finite-Horizon Optimal Stopping](P026_Finite_Horizon_Optimal_Stopping.md): another stop-or-continue setting, but this policy uses relative ranks in random order and maximizes the chance of selecting the single overall maximum.

## Assessment History

- [November 1 Q2, discussed November 2](../../DailyTests/2026-11-01.md#q2--sequential-selection): Partial / Hinted overall. The user supplied the first-r location condition and proposed the neighboring-cutoff comparison; exact weighting, difference simplification and large-n integral were supplied. After the integral hint, the user independently stated $`n/e`$ and then $`1/e`$ as answers. Actual time Not recorded; K/R unresolved.
