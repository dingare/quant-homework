# S018 — Ratio-of-Means Inference

## Metadata

- Category: Statistics
- Tags: CLT, Delta Method, Plug-in SE, Denominator Uncertainty
- Date Added: 2026-10-22
- Original drill dates: 2026-10-13
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-13 Q4

Source and assessment: [2026-10-13 Q4](../../DailyTests/2026-10-13.md#q4--ratio-of-means-inference). The reference material below does not change that attempt’s recorded result.

### Question

Observe iid pairs $`(X_i,Y_i)`$ with $`Y_i\gt0`$, finite second moments and $`\mu_Y=E[Y_i]\gt0`$:

```math
r=\frac{E[X_i]}{E[Y_i]},\qquad\hat r=\frac{\bar X}{\bar Y}.
```

Derive the limiting distribution of $`\sqrt n(\hat r-r)`$, an implementable approximate 95% CI and a nondegeneracy condition. Does averaging individual ratios estimate the same target? Give a counterexample with finite targets, and explain why denominator uncertainty can undermine the interval.

### Key solution

Center before applying CLT; use denominator convergence and Slutsky:

```math
W_i=X_i-rY_i,\quad E[W_i]=0,\quad
\hat r-r=\frac{\bar W}{\bar Y},\quad
\sqrt n(\hat r-r)\xrightarrow{d}N\!\left(0,\frac{\sigma_W^2}{\mu_Y^2}\right).
```

Require $`\sigma_W^2\gt0`$ and retain within-pair covariance:

```math
\sigma_W^2=\mathrm{Var}(X_i)+r^2\mathrm{Var}(Y_i)-2r\,\mathrm{Cov}(X_i,Y_i).
```

```math
s_W^2=\frac1{n-1}\sum_i(X_i-\hat rY_i)^2,\qquad
\widehat{\mathrm{SE}}(\hat r)=\frac{s_W}{\sqrt n\,\bar Y},\qquad
\mathrm{CI}_{0.95}:\ \hat r\pm z_{0.975}\frac{s_W}{\sqrt n\,\bar Y}.
```

This is asymptotic, not an exact t interval. A denominator small relative to its sampling uncertainty can create asymmetric ratio behavior and poor Wald coverage; small units alone are not the issue.

With integrable individual ratios, their average targets $`E[X/Y]`$. For $`X\equiv1`$ and $`Y\sim\mathrm{Uniform}(1,3)`$:

```math
E[X/Y]=\frac12\int_1^3\frac1y\,dy=\frac{\ln3}{2}
\ne\frac{E[X]}{E[Y]}=\frac12.
```

The original second-moment assumptions alone do not guarantee integrability of individual ratios.

## Assessment history

- [2026-10-13 Q4 — assessment](../../DailyTests/2026-10-13.md#q4--ratio-of-means-inference)

## Related questions and knowledge

- [S011 — Exponential MLE and Fisher Information](S011_Exponential_MLE_and_Fisher_Information.md) — Asymptotic distribution, plug-in standard error and conditions.
