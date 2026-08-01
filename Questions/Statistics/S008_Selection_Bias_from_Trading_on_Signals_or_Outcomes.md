# S008 — Selection Bias from Trading on Signals or Outcomes

## Problem

Let \(X\sim N(0,1)\) and

\[
Y=2X+\varepsilon,qquad \varepsilon\sim N(0,4),\quad \varepsilon\perp X.
\]

Find the population regression of \(Y\) on \(X\), including an intercept, when the
sample is selected first by \(X>0\), and then instead by \(Y>0\).

## Selection on the Regressor

Conditioning on \(X>0\) preserves \(E[\varepsilon\mid X]=0\). Thus

\[
\boxed{\alpha_{X>0}=0,qquad \beta_{X>0}=2}.
\]

Truncating the regressor changes its distribution but does not break exogeneity.

## Selection on the Outcome

Now low-\(X\) observations survive only when \(\varepsilon\) is unusually positive,
inducing negative selected-sample covariance between \(X\) and \(\varepsilon\).

Because \(\operatorname{Var}(Y)=8\) and \(\operatorname{Cov}(X,Y)=2\), write

\[
X=\frac14Y+\eta,qquad \eta\perp Y,qquad \operatorname{Var}(\eta)=\frac12.
\]

For a half-normal truncation,

\[
\operatorname{Var}(Y\mid Y>0)=8\left(1-\frac2\pi\right).
\]

Therefore,

\[
\operatorname{Cov}(X,Y\mid Y>0)=2\left(1-\frac2\pi\right),
\]

\[
\operatorname{Var}(X\mid Y>0)=1-\frac1\pi,
\]

and

\[
\boxed{\beta_{Y>0}=\frac{2(\pi-2)}{\pi-1}\approx1.066}.
\]

Also \(E[Y\mid Y>0]=4/\sqrt\pi\) and \(E[X\mid Y>0]=1/\sqrt\pi\), so

\[
\alpha_{Y>0}=\frac{4-\beta_{Y>0}}{\sqrt\pi}.
\]

## Interview Takeaways

- Selection on a regressor can preserve the conditional model.
- Selection on an outcome generally correlates regressors with regression errors.
- HAC standard errors cannot repair this identification bias.

## Finance Connection

Filtering trades by an ex-ante signal threshold differs fundamentally from retaining
only profitable trades or high realized-Sharpe strategies. The latter is post-selection bias.
