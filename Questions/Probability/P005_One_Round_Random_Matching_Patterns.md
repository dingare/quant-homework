# P005 — One-Round Random Matching Patterns

## Metadata

- Category: Probability
- Secondary: Combinatorics, Asymptotic Distributions
- Difficulty: ★★★★☆
- Tags: Random Matching, Perfect Matching, Indicator Variables, Covariance, Poisson Approximation
- Review Priority: High
- Date Added: 2026-07-19
- Status: Completed
- Scope Note: Keep all Probability Part II random-matching patterns in this file rather than creating separate questions.

## Pattern 1 — Couples in a Random Perfect Matching

### Core Question

There are $2n$ people consisting of $n$ couples. The people are paired uniformly at random into $n$ unordered pairs. Let $X$ be the number of couples who are matched to each other.

Find:

1. $E[X]$,
2. $\mathrm{Var}(X)$,
3. the total number of possible pairings,
4. the limiting distribution of $X$ as $n\to\infty$.

### Counting the Sample Space

The number of perfect matchings of $2n$ labeled people is

$$
(2n-1)!!=(2n-1)(2n-3)\cdots3\cdot1
=\frac{(2n)!}{2^n n!}.
$$

Sequentially, the first fixed person has $2n-1$ possible partners, the next unmatched fixed person has $2n-3$, and so on.

Alternatively, start with $(2n)!$ permutations, divide by $2^n$ because order within each pair does not matter, and divide by $n!$ because the order of the pairs does not matter.

### Expected Number of Matched Couples

For couple $i$, define

$$
I_i=\mathbf 1\{\text{couple }i\text{ is matched together}\}.
$$

Then

$$
X=\sum_{i=1}^n I_i.
$$

For either member of a fixed couple, exactly one of the $2n-1$ possible partners is their significant other. Hence

$$
P(I_i=1)=\frac1{2n-1}.
$$

By linearity of expectation, which does not require independence,

$$
\boxed{E[X]=\frac{n}{2n-1}}.
$$

In particular, $E[X]\to 1/2$.

### Variance and Dependence

For $i\ne j$,

$$
E[I_iI_j]
=P(I_i=1,I_j=1)
=\frac1{(2n-1)(2n-3)}.
$$

The first couple must match, after which the second couple is matching within a remaining population of $2n-2$ people. Therefore

$$
\mathrm{Cov}(I_i,I_j)
=\frac1{(2n-1)(2n-3)}-\frac1{(2n-1)^2}\gt 0.
$$

The indicators are not independent: one successful couple slightly increases the chance that another couple succeeds.

Using

$$
\mathrm{Var}(X)
=\sum_i\mathrm{Var}(I_i)
+2\sum_{i\lt j}\mathrm{Cov}(I_i,I_j),
$$

and $2\binom n2=n(n-1)$ gives

$$
\boxed{
\mathrm{Var}(X)
=\frac{4n(n-1)^2}{(2n-1)^2(2n-3)}
}.
$$

Thus $\mathrm{Var}(X)\to 1/2$ as $n\to\infty$.

### Why the Limit Is Poisson

This is a rare-event counting problem:

- there are $n$ candidate couples,
- each succeeds with probability $1/(2n-1)\approx1/(2n)$,
- the total mean converges to $1/2$,
- dependence between any fixed collection of indicators becomes negligible.

A precise factorial-moment argument uses

$$
(X)_k=X(X-1)\cdots(X-k+1).
$$

For fixed $k$,

$$
E[(X)_k]
=\frac{n(n-1)\cdots(n-k+1)}
{(2n-1)(2n-3)\cdots(2n-(2k-1))}
\longrightarrow\left(\frac12\right)^k.
$$

These are the factorial moments of a $\mathrm{Poisson}(1/2)$ random variable. Therefore

$$
\boxed{X\xrightarrow{d}\mathrm{Poisson}\left(\frac12\right)}.
$$

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

## Pattern 2 — No Matches and Exactly $k$ Matches

Let $A_i$ be the event that couple $i$ is matched together. For $r$ couples, define $D_r$ as the number of perfect matchings in which no couple is matched together.

### Inclusion-Exclusion Count

If a specified set of $j$ couples is forced to match, the remaining $2r-2j$ people can be paired in

$$
(2r-2j-1)!!
$$

ways. There are $\binom rj$ choices of the specified couples. Inclusion-exclusion therefore gives

$$
\boxed{
D_r=\sum_{j=0}^r(-1)^j\binom rj(2r-2j-1)!!
}.
$$

The convention $(-1)!!=1$ represents the single empty matching after everyone has already been paired.

Consequently,

$$
\boxed{
P(X=0)=\frac{D_n}{(2n-1)!!}
}.
$$

Because $X\Rightarrow\mathrm{Poisson}(1/2)$,

$$
P(X=0)\longrightarrow e^{-1/2}\approx0.6065.
$$

### Exact Distribution

For exactly $k$ couples to match, first choose those couples and then require zero matches among the remaining $n-k$ couples:

$$
\boxed{
P(X=k)=\frac{\binom nkD_{n-k}}{(2n-1)!!}
}.
$$

Equivalently,

$$
P(X=k)
=\frac{\binom nk}{(2n-1)!!}
\sum_{j=0}^{n-k}(-1)^j\binom{n-k}{j}
\big(2(n-k-j)-1\big)!!.
$$

A useful feasibility check is

$$
P(X=n-1)=0:
$$

if $n-1$ couples match, the final two people are also a couple and must match.

## Pattern 3 — Two Types and Cross-Type Matches

There are $n$ members of type M and $n$ members of type F. All $2n$ people are paired uniformly at random. Let $X$ be the number of mixed M-F pairs.

### Probability Every Pair Is Mixed

Match each of the $n$ M members bijectively to the $n$ F members. There are $n!$ favorable matchings, so

$$
\boxed{
P(X=n)=\frac{n!}{(2n-1)!!}
=\frac{2^n(n!)^2}{(2n)!}
=\frac{2^n}{\binom{2n}{n}}
}.
$$

### Expected Number of Mixed Pairs

For each M member, let $I_i$ indicate that their partner is type F. Every mixed pair contains exactly one M member, so $X=\sum_{i=1}^n I_i$ without double counting. Since

$$
P(I_i=1)=\frac{n}{2n-1},
$$

linearity gives

$$
\boxed{E[X]=\frac{n^2}{2n-1}}.
$$

### Exact Distribution and the Parity Constraint

If there are $k$ mixed pairs, then $n-k$ M members and $n-k$ F members remain to be paired within their own types. Hence $n-k$ must be even. For a feasible $k$:

1. choose the $k$ M members and $k$ F members;
2. match those selected members across types in $k!$ ways;
3. match the remaining members internally within each type.

Thus

$$
\boxed{
P(X=k)=
\frac{\binom nk^2k!\big((n-k-1)!!\big)^2}{(2n-1)!!}
}
$$

when $n-k$ is even, and $P(X=k)=0$ otherwise. In particular, $X$ has the same parity as $n$.

### Variance

For two distinct M members,

$$
E[I_iI_j]
=\frac{n}{2n-1}\frac{n-1}{2n-3}.
$$

Therefore

$$
\mathrm{Cov}(I_i,I_j)
=\frac{n}{(2n-1)^2(2n-3)}\gt 0,
$$

and

$$
\boxed{
\mathrm{Var}(X)
=\frac{2n^2(n-1)^2}{(2n-1)^2(2n-3)}
}.
$$

Here $E[X]\sim n/2$ and $\mathrm{Var}(X)\sim n/4$. Unlike the matched-couples count, this is not a fixed-mean rare-event problem.

## Pattern 4 — Matches Internal to a Specified Subset

Among $2n$ people, suppose a specified subset contains $m$ people. Let $X$ be the number of pairs having both endpoints in that subset.

### Expected Internal Pairs

Define one indicator $I_{ij}$ for each potential pair inside the subset. There are $\binom m2$ potential pairs and

$$
P(I_{ij}=1)=\frac1{2n-1}.
$$

Hence

$$
\boxed{
E[X]=\frac{\binom m2}{2n-1}
=\frac{m(m-1)}{2(2n-1)}
}.
$$

The indicator should be attached to each potential pair, not to each person; otherwise an actual internal pair may be counted twice.

### Variance: Classify Overlap Structure

For two potential internal pairs, there are two covariance types.

If they share a person, they are mutually exclusive:

$$
E[I_{ij}I_{ik}]=0,
\qquad
\mathrm{Cov}(I_{ij},I_{ik})=-\frac1{(2n-1)^2}.
$$

If their four endpoints are distinct:

$$
E[I_{ij}I_{kl}]
=\frac1{(2n-1)(2n-3)},
$$

so

$$
\mathrm{Cov}(I_{ij},I_{kl})
=\frac1{(2n-1)(2n-3)}-\frac1{(2n-1)^2}\gt 0.
$$

There are $3\binom m3$ unordered pairs of potential edges that share one endpoint and $3\binom m4$ unordered pairs of disjoint potential edges. Therefore

$$
\boxed{
\begin{aligned}
\mathrm{Var}(X)
={}&\binom m2\frac1{2n-1}\left(1-\frac1{2n-1}\right)\\
&-\frac{6\binom m3}{(2n-1)^2}\\
&+6\binom m4\left[
\frac1{(2n-1)(2n-3)}-\frac1{(2n-1)^2}
\right].
\end{aligned}
}
$$

The factors $3$ come from the three two-edge configurations on a selected triple or quadruple; the additional factor $2$ comes from the covariance expansion.

### A Specified Even Subset Is Closed

For a specified subset of $2k$ people to pair entirely within itself, both the subset and its complement must form perfect matchings. Thus

$$
\boxed{
P(\text{the specified }2k\text{ people form a closed matching})
=\frac{(2k-1)!!(2n-2k-1)!!}{(2n-1)!!}
}.
$$

For four specified people this becomes

$$
\frac{3}{(2n-1)(2n-3)},
$$

corresponding to their three internal matchings.

### Asymptotic Regimes for Internal Pairs

Since

$$
E[X]\sim\frac{m^2}{4n},
$$

the scale of $m$ determines the limit:

- if $m=o(\sqrt n)$, then $X\xrightarrow{p}0$;
- if $m/\sqrt n\to c$, then $X\Rightarrow\mathrm{Poisson}(c^2/4)$;
- if $m/(2n)\to\rho\in(0,1)$, then $X/n\xrightarrow{p}\rho^2$, with a normal limit after centering and variance normalization.

This is the general rare-event principle: a finite limiting mean suggests Poisson; a growing count with many small contributions suggests concentration and a Gaussian fluctuation scale.

## Pattern 5 — Conditional Symmetry

Return to $n$ couples and condition on no couple being matched together. Fix a person A, their partner A', and another person B who is not A'. Then

$$
\boxed{
P(\text{A is paired with B}\mid X=0)=\frac1{2n-2}
}.
$$

The condition removes A' from A's candidate set. All remaining $2n-2$ candidates are still symmetric under relabeling that preserves the couple structure and the event $X=0$.

The partner B' of B does affect the dependence structure of the remaining matching, but does not change A's marginal probability of selecting B. Comparing A-B with A-B' merely swaps the labels B and B' in structurally identical remaining problems.

## Master Pattern Checklist

When facing a one-round random-matching problem:

1. **Identify the sample space.** For $2n$ labeled objects, use $(2n-1)!!$.
2. **Try sequential exposure.** A fixed unmatched person has $2n-1$, then $2n-3$, and so on, possible partners.
3. **For an expected count, choose the correct indicator unit.** Use one indicator per target couple, potential edge, or uniquely represented mixed pair.
4. **Use linearity immediately.** Independence is unnecessary for expectation.
5. **For variance, classify pairs of indicators by overlap.** Shared endpoints often imply negative covariance; disjoint target edges often have positive covariance.
6. **For zero or exactly $k$ forbidden matches, use inclusion-exclusion.** First force a selected set of target edges, then freely match the remainder.
7. **Check feasibility and parity.** Some counts are structurally impossible even when a formula initially appears to allow them.
8. **Use symmetry only after conditioning carefully.** Verify that the conditioning event preserves symmetry among the remaining candidates.
9. **Inspect the limiting mean.** Vanishing mean gives degeneration, finite mean often gives Poisson, and a growing mean often leads to concentration and a normal approximation.

## Consolidated Common Mistakes

- Confusing the number of potential pairs, $\binom m2$, with the number of complete matchings, $(m-1)!!$.
- Writing $m!/(2^m(m/2)!)$ instead of $m!/(2^{m/2}(m/2)!)$ for a perfect matching of $m$ even objects.
- Using $2n-4$ rather than $2n-1$ as the first denominator when exposing the partner of one fixed person.
- Forgetting the factor $3$ when two potential edges are constructed from a chosen triple or quadruple.
- Forgetting the factor $2$ in $2\sum_{\alpha\lt \beta}\mathrm{Cov}(I_\alpha,I_\beta)$.
- Treating weak dependence as exact independence.
- Forgetting that a conditioned matching may remain marginally symmetric even though its edges are globally dependent.

## Final Takeaways

$$
\boxed{N_{\text{matchings}}(2n)=(2n-1)!!}
$$

The reusable toolkit is:

$$
\boxed{
\text{sequential exposure}
+\text{ indicators}
+\text{ overlap-based covariance}
+\text{ inclusion-exclusion}
+\text{ symmetry}
}
$$

Choose the method based on what is requested: indicators for moments, counting for exact probabilities, inclusion-exclusion for forbidden edges, and asymptotics for the large-system shape.

## Connections

- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — the general framework behind the indicator expectations, covariance classifications, factorial moments, and Poisson approximations used throughout this note.
