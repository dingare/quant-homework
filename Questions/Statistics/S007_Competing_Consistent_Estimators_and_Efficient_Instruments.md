# S007 — Competing Consistent Estimators and Efficient Instruments

## Metadata

- Category: Statistics
- Secondary: Econometrics, GMM, Heteroskedasticity
- Difficulty: ★★★★★
- Tags: Consistency, Asymptotic Variance, Efficiency, Moment Conditions, Optimal Instrument, WLS
- Review Priority: High
- Date Added: 2026-07-26
- Status: Final
- Source: Regression Analysis Exercise 5.6

## Core Question

Consider the scalar regression without an intercept:

$$
y_i=x_i\beta+e_i,
\qquad
E(e_i\mid x_i)=0.
$$

Compare

$$
\widehat\beta
=\frac{\sum_{i=1}^n x_i y_i}
{\sum_{i=1}^n x_i^2}
$$

with

$$
\widetilde\beta
=\frac1n\sum_{i=1}^n\frac{y_i}{x_i}.
$$

1. Under what conditions are both estimators consistent?
2. What are their asymptotic variances?
3. Under what conditional variance structures is each estimator efficient?
4. Where does the general instrument $h(x)$ come from, and why is

$$
h^*(x)=\frac{x}{\sigma^2(x)}
$$

optimal?

Here

$$
\sigma^2(x)=E(e_i^2\mid x_i=x).
$$

## Part I — Consistency

### OLS Estimator

Substitute $y_i=x_i\beta+e_i$:

$$
\widehat\beta-\beta
=\frac{n^{-1}\sum_i x_i e_i}
{n^{-1}\sum_i x_i^2}.
$$

The conditional mean restriction implies

$$
E(x_ie_i)
=E\!\left[x_iE(e_i\mid x_i)\right]
=0.
$$

If $0\lt E(x_i^2)\lt \infty$ and the relevant law of large numbers applies, then

$$
\boxed{\widehat\beta\xrightarrow{p}\beta}.
$$

### Average-Ratio Estimator

Since

$$
\frac{y_i}{x_i}
=\beta+\frac{e_i}{x_i},
$$

we have

$$
\widetilde\beta-\beta
=\frac1n\sum_i\frac{e_i}{x_i}.
$$

Furthermore,

$$
E\!\left(\frac{e_i}{x_i}\right)
=E\!\left[\frac1{x_i}E(e_i\mid x_i)\right]
=0.
$$

Thus, if $P(x_i=0)=0$, $E|e_i/x_i|\lt \infty$, and the relevant law of large numbers applies,

$$
\boxed{\widetilde\beta\xrightarrow{p}\beta}.
$$

The extra conditions matter: observations with $x_i$ close to zero can make $e_i/x_i$ extremely unstable or even destroy the required moments.

## Part II — Asymptotic Variances

### OLS

$$
\sqrt n(\widehat\beta-\beta)
=\left(\frac1n\sum_i x_i^2\right)^{-1}
\frac1{\sqrt n}\sum_i x_ie_i.
$$

Therefore,

$$
\boxed{
\sqrt n(\widehat\beta-\beta)
\xrightarrow{d}N(0,V_{\widehat\beta})
}
$$

with

$$
\boxed{
V_{\widehat\beta}
=\frac{E[x_i^2\sigma^2(x_i)]}
{[E(x_i^2)]^2}
}.
$$

### Average Ratio

$$
\sqrt n(\widetilde\beta-\beta)
=\frac1{\sqrt n}\sum_i\frac{e_i}{x_i}.
$$

Hence, provided the second moment is finite,

$$
\boxed{
\sqrt n(\widetilde\beta-\beta)
\xrightarrow{d}N(0,V_{\widetilde\beta})
}
$$

with

$$
\boxed{
V_{\widetilde\beta}
=E\!\left[\frac{\sigma^2(x_i)}{x_i^2}\right]
}.
$$

Consistency alone does not determine which estimator is more precise.

## Part III — What Efficiency Means

Efficiency here means minimum asymptotic variance within the relevant class of regular estimators that use the conditional moment restriction

$$
E(e_i\mid x_i)=0.
$$

It is not the same as unbiasedness or consistency:

$$
\text{consistency}
=\text{convergence to the true parameter},
$$

whereas

$$
\text{efficiency}
=\text{smallest asymptotic variance among valid competitors}.
$$

The efficient estimator under known conditional variance is weighted least squares:

$$
\widehat\beta_{\mathrm{eff}}
=\frac{\sum_i x_i y_i/\sigma^2(x_i)}
{\sum_i x_i^2/\sigma^2(x_i)},
$$

with efficiency bound

$$
\boxed{
V_{\mathrm{eff}}
=\frac1{E[x_i^2/\sigma^2(x_i)]}
}.
$$

## Part IV — Where $h(x)$ Comes From

The conditional moment restriction generates infinitely many unconditional moments. For every suitable measurable function $h$,

$$
E[h(x_i)e_i]
=E\!\left[h(x_i)E(e_i\mid x_i)\right]
=0.
$$

Thus $h(x)$ is a chosen instrument or weighting function. Solving the sample moment

$$
\frac1n\sum_i h(x_i)(y_i-x_i\beta)=0
$$

gives

$$
\widehat\beta_h
=\frac{\sum_i h(x_i)y_i}
{\sum_i h(x_i)x_i}.
$$

Two special choices recover the estimators above:

$$
h(x)=x
\quad\Longrightarrow\quad
\widehat\beta_h=\widehat\beta,
$$

and

$$
h(x)=\frac1x
\quad\Longrightarrow\quad
\widehat\beta_h=\widetilde\beta.
$$

Under standard conditions,

$$
\sqrt n(\widehat\beta_h-\beta)
\xrightarrow{d}N(0,V(h)),
$$

where

$$
\boxed{
V(h)
=\frac{E[h(x)^2\sigma^2(x)]}
{\{E[h(x)x]\}^2}
}.
$$

## Part V — Deriving the Optimal Instrument

Apply Cauchy–Schwarz to

$$
E[h(x)x]
=E\!\left[
h(x)\sigma(x)\,
\frac{x}{\sigma(x)}
\right].
$$

Then

$$
\{E[h(x)x]\}^2
\le
E[h(x)^2\sigma^2(x)]
E\!\left[\frac{x^2}{\sigma^2(x)}\right].
$$

Rearranging,

$$
V(h)
\ge
\frac1{E[x^2/\sigma^2(x)]}.
$$

Equality in Cauchy–Schwarz holds exactly when

$$
h(x)\sigma(x)
\propto
\frac{x}{\sigma(x)}.
$$

Therefore,

$$
\boxed{
h^*(x)\propto\frac{x}{\sigma^2(x)}
}.
$$

Multiplying an instrument by a nonzero constant does not change the estimator, so the canonical choice is

$$
\boxed{
h^*(x)=\frac{x}{\sigma^2(x)}
}.
$$

This derivation shows that the optimal instrument is not guessed: it solves the asymptotic variance minimization problem.

## Part VI — When Each Estimator Is Efficient

### OLS

OLS uses $h(x)=x$. It matches the optimal instrument when

$$
\frac{x}{\sigma^2(x)}\propto x,
$$

which, for nonzero $x$, requires

$$
\boxed{\sigma^2(x)=\sigma^2}.
$$

Thus OLS is efficient under homoskedasticity.

### Average Ratio

The average-ratio estimator uses $h(x)=1/x$. It matches the optimal instrument when

$$
\frac{x}{\sigma^2(x)}
\propto\frac1x,
$$

which requires

$$
\boxed{\sigma^2(x)=c x^2}
$$

for some $c\gt 0$.

Equivalently, dividing the model by $x_i$ gives

$$
\frac{y_i}{x_i}
=\beta+\frac{e_i}{x_i}.
$$

If $\mathrm{Var}(e_i\mid x_i)=cx_i^2$, then

$$
\mathrm{Var}\!\left(\frac{e_i}{x_i}\,\middle|\,x_i\right)=c.
$$

The transformed model is homoskedastic, so its sample-mean estimator is efficient.

## Key Knowledge Points

- A conditional moment implies many unconditional moments.
- $h(x)$ selects which moment condition—and therefore which estimator—is used.
- Different consistent estimators may have very different asymptotic variances.
- The efficient instrument gives less weight to observations with high conditional noise.
- Optimal weighting depends on $\sigma^2(x)$; robust standard errors alone do not make an inefficient estimator efficient.
- The average-ratio estimator requires stronger inverse-moment conditions than OLS.

## Common Mistakes

- Treating consistency and efficiency as synonyms.
- Claiming $E(e/x)=0$ without checking that $x\neq0$ and the expectation exists.
- Comparing only numerator variances and ignoring the derivative $E[h(x)x]$.
- Saying OLS is always efficient because it is unbiased or consistent.
- Confusing heteroskedasticity-robust inference with efficient estimation.
- Forgetting that an instrument is unchanged, for estimation purposes, by a nonzero scalar multiple.

## Interview Follow-Ups

1. If $\sigma^2(x)$ is unknown, how would feasible GLS estimate it?
2. What happens when $x$ has substantial mass near zero?
3. Generalize the efficient instrument to vector-valued regressors.
4. How does this conditional-moment argument connect to optimal GMM?
5. Why can robust OLS inference be valid even when OLS is inefficient?

## Finance Connection

Market observations often have state-dependent noise: liquidity, bid–ask spreads, and volatility change with signal magnitude or market regime. Efficient estimation weights observations by information content rather than treating every observation as equally precise.

## What to Remember

$$
\boxed{
E(e\mid x)=0
\Longrightarrow
E[h(x)e]=0
\quad\text{for any suitable }h
}
$$

and

$$
\boxed{
h^*(x)=\frac{x}{\mathrm{Var}(e\mid x)}
}.
$$

