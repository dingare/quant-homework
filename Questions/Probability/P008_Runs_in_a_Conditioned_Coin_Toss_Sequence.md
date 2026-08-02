# P008 — Runs in a Conditioned Coin-Toss Sequence

## Problem

A fair coin is tossed 100 times conditional on exactly 50 heads and 50 tails. Let

\[
C=\sum_{i=1}^{99}I_i,qquad I_i=\mathbf1_{\{X_i\ne X_{i+1}\}},
\]

be the number of changes. Find \(E[C]\), \(\operatorname{Var}(C)\), and a normal
approximation to \(P(C\ge60)\).

## Expectation

For each adjacent pair,

\[
p=P(I_i=1)=2\frac{50}{100}\frac{50}{99}=\frac{50}{99}.
\]

Therefore,

\[
\boxed{E[C]=99p=50}.
\]

## Variance by Indicator Covariances

Use

\[
\operatorname{Var}(C)=\sum_i\operatorname{Var}(I_i)
+2\sum_{i<j}\operatorname{Cov}(I_i,I_j).
\]

Adjacent indicators both equal one only for \(HTH\) or \(THT\), so

\[
E[I_iI_{i+1}]=\frac{25}{99},qquad
\operatorname{Cov}_{\rm adj}=-\frac{25}{9801}.
\]

Nonadjacent indicators use four distinct positions. Both pairs must contain one head
and one tail, giving

\[
E[I_iI_j]=\frac{2450}{99\cdot97},qquad
\operatorname{Cov}_{\rm nonadj}=\frac{50}{950697}.
\]

There are 98 adjacent indicator pairs and

\[
\binom{99}{2}-98=4753=49\cdot97
\]

nonadjacent pairs. Their aggregate covariances cancel:

\[
98\left(-\frac{25}{9801}\right)
+4753\left(\frac{50}{950697}\right)=0.
\]

Hence

\[
\boxed{\operatorname{Var}(C)=99p(1-p)=\frac{2450}{99}\approx24.75}.
\]

The indicators are not independent; the cancellation is a feature of this symmetric
50/50 case.

## Normal Approximation

With continuity correction and \(\sigma_C=\sqrt{2450/99}\approx4.975\),

\[
P(C\ge60)\approx
1-\Phi\left(\frac{59.5-50}{4.975}\right)
\approx\boxed{0.028}.
\]

## Runs Interpretation

If \(R\) is the number of runs, then \(R=C+1\). For a random ordering of \(m\)
heads and \(n\) tails,

\[
E[R]=1+\frac{2mn}{m+n},qquad
\operatorname{Var}(R)=
\frac{2mn(2mn-m-n)}{(m+n)^2(m+n-1)}.
\]

This classical runs-test formula is itself obtained by the indicator expansion above.

## Finance Connection

Applied to return signs, unusually few runs suggest persistence and unusually many
runs suggest mean reversion. Conditioning on the counts of positive and negative days
removes unconditional directional bias.

## Connections

- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — the reusable indicator, joint-probability, and covariance framework behind the runs formula.
