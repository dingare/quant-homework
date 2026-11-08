# S027 — Estimating a Squared Mean

## Metadata

- Category: Statistics
- Tags: Estimator Bias, Nonlinear Targets, Finite-Sample Variance
- Date Added: 2026-11-07
- Original drill: November 7, Q3
- Status: Discussed November 8. Overall Partial / Hinted; part 1 independently correct, fourth-moment / MGF route proposed independently, subsequent calculation and negative-estimate interpretation supplied.

## Core Question

A strategy's daily returns are independent:

```math
X_1,\ldots,X_n\sim N(\mu,\sigma^2),
```

where the positive variance is known and the mean is unknown. A researcher wants to estimate the strategy's squared population mean return:

```math
\theta=\mu^2.
```

1. The researcher proposes the square of the sample mean. Derive its bias and construct an unbiased estimator of theta.
2. Derive the exact finite-sample variance of your unbiased estimator as a function of the mean, known variance and sample size.
3. Your estimator is negative on the observed sample. Is that a mathematical contradiction? If you replace negative estimates by zero, does unbiasedness survive? Explain briefly.

No code or numerical integration is required.

## Solution

### Bias correction

Write the sample-mean variance as tau squared. Then:

```math
\tau^2=\frac{\sigma^2}{n},\qquad
\bar X\sim N(\mu,\tau^2),\qquad
E[\bar X^2]=\mu^2+\tau^2.
```

The proposed estimator's bias is tau squared, so the corrected estimator is:

```math
\widehat\theta=\bar X^2-\frac{\sigma^2}{n},\qquad
E[\widehat\theta]=\mu^2.
```

### Exact finite-sample variance

Subtracting a known constant does not change variance. The fourth-moment route is:

```math
\mathrm{Var}(\widehat\theta)
=E[\bar X^4]-\left(E[\bar X^2]\right)^2.
```

The user proposed an MGF calculation. That is valid; the supplied calculation instead separates the mean and standard-normal component:

```math
\bar X=\mu+\tau Z,\qquad Z\sim N(0,1),
```

```math
E[Z]=E[Z^3]=0,\qquad E[Z^2]=1,\qquad E[Z^4]=3.
```

Expand the fourth power and discard the odd-moment terms:

```math
E[\bar X^4]=\mu^4+6\mu^2\tau^2+3\tau^4,
```

```math
\begin{aligned}
\mathrm{Var}(\widehat\theta)
&=\mu^4+6\mu^2\tau^2+3\tau^4-(\mu^2+\tau^2)^2\\
&=4\mu^2\tau^2+2\tau^4\\
&=\boxed{\frac{4\mu^2\sigma^2}{n}+\frac{2\sigma^4}{n^2}}.
\end{aligned}
```

This is exact, not an asymptotic approximation. Distinguish the raw fourth moment of the sample mean from its centered fourth moment.

### Negative estimates and clipping

Unbiasedness is a statement about the expectation across samples, not a requirement that every estimate lie in the parameter space. A negative estimate occurs precisely when:

```math
|\bar X|\lt\frac{\sigma}{\sqrt n}.
```

It is not a contradiction and does not by itself establish that the estimator's variance is large. Clipping all negative values to zero raises some estimates and lowers none. With the positive-part notation:

```math
x_+=\max(x,0),\qquad
E[\max(\widehat\theta,0)]
=\mu^2+E[(-\widehat\theta)_+]\gt\mu^2.
```

The inequality is strict for finite n and positive sigma squared because the normal sample mean has positive probability of lying in the negative-estimate interval. Clipping therefore introduces upward bias.

Increasing n shrinks estimation error but does not guarantee a nonnegative estimate. At zero mean:

```math
\widehat\theta=\frac{\sigma^2}{n}(Z^2-1),\qquad
P(\widehat\theta\lt0)=P(|Z|\lt1)\approx0.6827.
```

This probability does not change with n even as the magnitude of the error shrinks. 区分“误差幅度变小”和“负值出现得更少”；增大样本不是消除每次负估计值的保证。

## Connections

- [S021 — Uniform Endpoint Estimation](S021_Uniform_Endpoint_Estimation_and_Exact_Bounds.md): compare estimator properties under finite-sample sampling laws; bias correction is target-specific.

## Assessment History

- [November 7 Q3, continued November 8](../../DailyTests/2026-11-07.md#q3--estimating-a-squared-mean): part 1 independently correct; fourth-moment and MGF route proposed, full calculation supplied on request. Negative-estimate and clipping interpretation explained. Overall Partial / Hinted; K/R unresolved, no implementation task, actual time Not recorded.
