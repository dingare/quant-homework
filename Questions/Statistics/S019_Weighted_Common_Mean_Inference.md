# S019 — Weighted Common-Mean Inference

## Metadata

- Category: Statistics
- Tags: Inverse-Variance Weights, GLS, Residual Scale, t Pivot
- Date Added: 2026-10-22
- Original drill dates: 2026-10-14
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-14 Q2

Source and assessment: [2026-10-14 Q2](../../DailyTests/2026-10-14.md#q2--weighted-common-mean-inference). The reference material below does not change that attempt’s recorded result.

### Question

Independent measurements satisfy $`E[X_i]=\mu`$, $`\mathrm{Var}(X_i)=\sigma^2v_i`$, with known $`v_i\gt0`$, unknown $`\sigma^2\gt0`$ and $`n\ge2`$. Among deterministic unbiased linear estimators, derive and prove minimum-variance weights. Under normality, construct an exact 95% CI with an estimated scale and justify degrees of freedom. Evaluate the estimate and SE for $`v=(1,4,9)`$, $`X=(2,4,8)`$.

### Key solution

With $`A=\sum_i1/v_i`$, the inverse-variance estimator has:

```math
w_i=\frac{1/v_i}{A},\qquad
\hat\mu=\sum_iw_iX_i,\qquad
\mathrm{Var}(\hat\mu)=\frac{\sigma^2}{A}.
```

Estimate the common noise scale, then use it in the estimator variance:

```math
s^2=\frac1{n-1}\sum_i\frac{(X_i-\hat\mu)^2}{v_i},\qquad
\mathrm{SE}(\hat\mu)=\sqrt{\frac{s^2}{A}}.
```

Under independent normal observations, the weighted mean and residual scale are independent:

```math
\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1},\qquad
\frac{\hat\mu-\mu}{\sqrt{s^2/A}}\sim t_{n-1},\qquad
\mathrm{CI}_{0.95}:\ \hat\mu\pm t_{n-1,0.975}\sqrt{\frac{s^2}{A}}.
```

For the numerical example:

```math
A=\frac{49}{36},\quad w=\frac1{49}(36,9,4),\quad
\hat\mu=\frac{20}{7},\quad
\sum_i\frac{(X_i-\hat\mu)^2}{v_i}=4,\quad
s^2=2,\quad\mathrm{SE}(\hat\mu)=\frac{6\sqrt2}{7}.
```

## Assessment history

- [2026-10-14 Q2 — assessment](../../DailyTests/2026-10-14.md#q2--weighted-common-mean-inference)

## Related questions and knowledge

- [S006 — Two Noisy Proxies and Errors-in-Variables](S006_Two_Noisy_Proxies_and_Errors_in_Variables.md) — Precision weighting of noisy observations.
- [S004 — Efficient IV, Rayleigh Quotient, and Covariance-Weighted Signal Combination](S004_Efficient_IV_Rayleigh_Quotient_and_Covariance_Weighted_Signal_Combination.md) — Covariance-weighted estimators and efficiency.
