# P040 — Occupied Assets: Moments and Concentration

## Metadata

- Category: Probability
- Tags: Occupancy, Indicators, Inclusion-Exclusion, Negative Covariance, Concentration
- Date Added: 2026-11-07
- Original drill: November 7, Q2
- Status: Discussed; independent contributions and supplied steps are assessed in the dated log.

## Core Question

There are m assets, with m at least 2. Each of n traders, with n at least 1, independently chooses exactly one asset, uniformly at random. Let D be the number of distinct assets chosen.

1. Derive exact expressions for the expectation and variance of D.
2. Are the events “asset A is chosen by at least one trader” and “asset B is chosen by at least one trader” independent for distinct assets? Determine the sign of their covariance and explain it.
3. Suppose m and n tend to infinity with their ratio satisfying the condition below. Does D divided by m converge in probability to a constant? Identify it and justify your answer using your moment calculations.

```math
\frac nm\to\lambda\gt0.
```

An unsimplified but explicit variance expression is sufficient.

## Solution

### 1. Indicators, expectation and variance

Let I_i indicate whether asset i is selected at least once. Define the probabilities that one specified asset is missed and that two specified assets are both missed:

```math
D=\sum_{i=1}^m I_i,\qquad
q=\left(1-\frac1m\right)^n,\qquad
s=\left(1-\frac2m\right)^n.
```

Traders' choices are independent, but asset-occupancy indicators are dependent. Expectation linearity does not require independence:

```math
E[I_i]=1-q,\qquad E[D]=m(1-q),\qquad
\mathrm{Var}(I_i)=q(1-q).
```

For distinct assets, inclusion-exclusion gives:

```math
P(I_i=1\text{ or }I_j=1)=1-s,
\qquad E[I_iI_j]=2(1-q)-(1-s)=1-2q+s.
```

Consequently:

```math
\mathrm{Cov}(I_i,I_j)=1-2q+s-(1-q)^2=s-q^2,
```

```math
\begin{aligned}
\mathrm{Var}(D)
&=\sum_i\mathrm{Var}(I_i)+2\sum_{i\lt j}\mathrm{Cov}(I_i,I_j)\\
&=mq(1-q)+m(m-1)(s-q^2).
\end{aligned}
```

There are m choose 2 unordered pairs; the factor 2 in the variance expansion yields m times m minus one. Each indicator is Bernoulli, equivalently a one-trial binomial. Using q instead of its complement in the single-indicator variance gives the same product, but expectations in the covariance calculation must consistently use the selected-event probability.

### 2. Negative covariance

```math
0\le1-\frac2m\lt\left(1-\frac1m\right)^2,
\qquad s\lt q^2,
\qquad\mathrm{Cov}(I_i,I_j)\lt0.
```

Fixed n creates competition for choices: every choice directed to one asset cannot also select another. Knowing that i was selected means at least one choice was used there. This supports the negative-dependence intuition, but conditioning on at least one selection is not equivalent to leaving exactly n minus one independent choices. With n = 1, selection of i rules out selection of j immediately.

### 3. Concentration of the occupied fraction

```math
n\log\left(1-\frac1m\right)
=-\frac nm+O\left(\frac n{m^2}\right)\to-\lambda,
\qquad
E\left[\frac Dm\right]=1-q\to1-e^{-\lambda}.
```

Mean convergence alone is insufficient. Negative covariances supply a convenient variance bound:

```math
\mathrm{Var}(D)\le mq(1-q)\le\frac m4,
\qquad
\mathrm{Var}\left(\frac Dm\right)\le\frac1{4m}\to0.
```

Chebyshev's inequality makes the occupied fraction concentrate around its own mean; combining this with the mean limit gives:

```math
\boxed{\frac Dm\xrightarrow{P}1-e^{-\lambda}}.
```

直觉：每个资产平均分到约 lambda 次选择，未被选择的比例趋近于指数项。这里不能直接把有依赖的指标当成独立变量套用大数定律；负协方差反而使方差上界更容易得到。

## Connections

- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md): occupancy, joint-event probabilities and covariance counting.
- [P034 — First Repeated Label](P034_First_Repeated_Label.md): related allocation model, but a stopped collision time rather than fixed-sample occupancy moments.

## Assessment History

- [November 7 Q2](../../DailyTests/2026-11-07.md#q2--occupied-assets): Partial / Hinted. Independent indicator, covariance and inclusion-exclusion ideas and negative-sign intuition are preserved; the pair-count correction and full concentration proof were supplied.
