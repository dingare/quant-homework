# P006 — Inversion Count in a Random Permutation

## Metadata

- Category: Probability
- Secondary: Random Permutations, Combinatorics, Algorithms
- Difficulty: ★★★★★
- Tags: Inversions, Indicator Variables, Covariance, Random Permutation, Asymptotic Normality
- Review Priority: High
- Date Added: 2026-07-23
- Status: Final

## Core Question

For a uniformly random permutation \(\pi\) of \(\{1,\ldots,n\}\), define

$$
X=\#\{(i,j):i<j,\ \pi_i>\pi_j\}.
$$

Compute \(E[X]\) and \(\mathrm{Var}(X)\) without enumerating all \(n!\) permutations.

## Expected Value

For each \(i<j\), define

$$
I_{ij}=\mathbf1\{\pi_i>\pi_j\}.
$$

By symmetry,

$$
P(I_{ij}=1)=\frac12.
$$

Since \(X=\sum_{i<j}I_{ij}\),

$$
\boxed{
E[X]=\binom n2\frac12=\frac{n(n-1)}4
}.
$$

Independence is not needed for this step.

## Variance: Dependence Lives on Triples

Each indicator has variance \(1/4\). Indicators involving four distinct positions are independent, so only comparisons sharing an index contribute covariance.

For \(i<j<k\), inspect the six relative orderings of \(\pi_i,\pi_j,\pi_k\):

$$
\mathrm{Cov}(I_{ij},I_{ik})
=\frac13-\frac14=\frac1{12},
$$

because both are one exactly when \(\pi_i\) is the largest;

$$
\mathrm{Cov}(I_{ik},I_{jk})
=\frac13-\frac14=\frac1{12},
$$

because both are one exactly when \(\pi_k\) is the smallest; and

$$
\mathrm{Cov}(I_{ij},I_{jk})
=\frac16-\frac14=-\frac1{12},
$$

because both are one only in the descending ordering.

Thus the sum of the three unordered covariance terms for each triple is \(1/12\). The variance expansion doubles this contribution:

$$
\mathrm{Var}(X)
=\binom n2\frac14+\binom n3\frac16.
$$

Therefore

$$
\boxed{
\mathrm{Var}(X)
=\frac{n(n-1)(2n+5)}{72}
}.
$$

For \(n=5\),

$$
\boxed{E[X]=5,\qquad\mathrm{Var}(X)=\frac{25}{6}}.
$$

## Symmetry of the Distribution

Reversing every comparison maps a permutation with \(X\) inversions to one with

$$
\binom n2-X
$$

inversions. Hence

$$
X\overset d=\binom n2-X.
$$

The distribution is symmetric around

$$
\frac12\binom n2=\frac{n(n-1)}4.
$$

## Why Independence Gives the Wrong Answer

If all indicators were incorrectly treated as independent, the variance would be only

$$
\binom n2\frac14=O(n^2).
$$

The correct variance is \(O(n^3)\), because there are \(\binom n3\) overlapping triples whose net covariance contribution does not vanish.

The inversion count is asymptotically normal after centering and scaling:

$$
\frac{X-E[X]}{\sqrt{\mathrm{Var}(X)}}
\xrightarrow{d}N(0,1).
$$

## Algorithmic Connection

For a realized array, inversions can be counted in \(O(n\log n)\) time using merge sort or a Fenwick tree. During merge sort, whenever a right-half element precedes the remaining left-half elements, it creates as many inversions as the number of those remaining elements.

## Important Knowledge Points

- Pairwise symmetry makes the expectation immediate.
- Pairwise independence of some indicators is not mutual independence of the full family.
- For variance, classify indicator pairs by overlap structure.
- Local dependence can accumulate: \(O(n^3)\) overlapping triples dominate the variance.
- Distributional symmetry is often easier to see through a bijection than through a PMF.

## Common Mistakes

- Assuming every pair of inversion indicators is independent.
- Forgetting the factor \(2\) in the covariance expansion.
- Assigning the same sign to all three covariance types on a triple.
- Enumerating \(n!\) permutations when relative-order symmetry suffices.

## Finance Connection

Inversion count is the Kendall-tau distance between rankings. Comparing asset rankings across dates provides a measure of signal instability, cross-sectional rank decay, and potential turnover.

## Connections

- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — the general expectation, covariance, and overlap-classification method used in this problem.

## What to Remember

$$
\boxed{
E[X]=\frac{n(n-1)}4,
\qquad
\mathrm{Var}(X)=\frac{n(n-1)(2n+5)}{72}
}.
$$
