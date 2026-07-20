# P005 — One-Round Random Matching Patterns

## Metadata

- Category: Probability
- Secondary: Combinatorics, Asymptotic Distributions
- Difficulty: ★★★★☆
- Tags: Random Matching, Perfect Matching, Indicator Variables, Covariance, Poisson Approximation
- Review Priority: High
- Date Added: 2026-07-19
- Status: In Progress
- Scope Note: Keep all Probability Part II random-matching patterns in this file rather than creating separate questions.

## Pattern 1 — Couples in a Random Perfect Matching

### Core Question

There are $2n$ people consisting of $n$ couples. The people are paired uniformly at random into $n$ unordered pairs. Let $X$ be the number of couples who are matched to each other.

Find:

1. $E[X]$,
2. $\operatorname{Var}(X)$,
3. the total number of possible pairings,
4. the limiting distribution of $X$ as $n\to\infty$.

### Counting the Sample Space

The number of perfect matchings of $2n$ labeled people is

```math
(2n-1)!!=(2n-1)(2n-3)\cdots3\cdot1
=\frac{(2n)!}{2^n n!}.
```

Sequentially, the first fixed person has $2n-1$ possible partners, the next unmatched fixed person has $2n-3$, and so on.

Alternatively, start with $(2n)!$ permutations, divide by $2^n$ because order within each pair does not matter, and divide by $n!$ because the order of the pairs does not matter.

### Expected Number of Matched Couples

For couple $i$, define

```math
I_i=\mathbf 1\{\text{couple }i\text{ is matched together}\}.
```

Then

```math
X=\sum_{i=1}^n I_i.
```

For either member of a fixed couple, exactly one of the $2n-1$ possible partners is their significant other. Hence

```math
P(I_i=1)=\frac1{2n-1}.
```

By linearity of expectation, which does not require independence,

```math
\boxed{E[X]=\frac{n}{2n-1}}.
```

In particular, $E[X]\to 1/2$.

### Variance and Dependence

For $i\ne j$,

```math
E[I_iI_j]
=P(I_i=1,I_j=1)
=\frac1{(2n-1)(2n-3)}.
```

The first couple must match, after which the second couple is matching within a remaining population of $2n-2$ people. Therefore

```math
\operatorname{Cov}(I_i,I_j)
=\frac1{(2n-1)(2n-3)}-\frac1{(2n-1)^2}>0.
```

The indicators are not independent: one successful couple slightly increases the chance that another couple succeeds.

Using

```math
\operatorname{Var}(X)
=\sum_i\operatorname{Var}(I_i)
+2\sum_{i<j}\operatorname{Cov}(I_i,I_j),
```

and $2\binom n2=n(n-1)$ gives

```math
\boxed{
\operatorname{Var}(X)
=\frac{4n(n-1)^2}{(2n-1)^2(2n-3)}
}.
```

Thus $\operatorname{Var}(X)\to 1/2$ as $n\to\infty$.

### Why the Limit Is Poisson

This is a rare-event counting problem:

- there are $n$ candidate couples,
- each succeeds with probability $1/(2n-1)\approx1/(2n)$,
- the total mean converges to $1/2$,
- dependence between any fixed collection of indicators becomes negligible.

A precise factorial-moment argument uses

```math
(X)_k=X(X-1)\cdots(X-k+1).
```

For fixed $k$,

```math
E[(X)_k]
=\frac{n(n-1)\cdots(n-k+1)}
{(2n-1)(2n-3)\cdots(2n-(2k-1))}
\longrightarrow\left(\frac12\right)^k.
```

These are the factorial moments of a $\operatorname{Poisson}(1/2)$ random variable. Therefore

```math
\boxed{X\xrightarrow{d}\operatorname{Poisson}\left(\frac12\right)}.
```

### Common Mistakes

- Computing the full distribution of $X$ when only its expectation is requested.
- Assuming the indicators must be independent before using linearity of expectation.
- Reversing the covariance formula: it is $E[I_iI_j]-E[I_i]E[I_j]$.
- Using $1/(2n-1)^2$ for the joint probability and missing the reduced denominator $2n-3$ after one couple is removed.
- Counting ordered pairs or ordered groups and forgetting to divide by $2^n n!$.

### What to Remember

- Random perfect matchings of $2n$ labeled objects: $(2n-1)!!=(2n)!/(2^n n!)$.
- For expected counts, define one indicator per target event and use linearity.
- For variance, joint success probabilities reveal the dependence.
- Many weakly dependent rare-event indicators with a finite limiting mean often suggest a Poisson limit.

