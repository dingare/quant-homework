# S017 — Confidence and Prediction Intervals

## Metadata

- Category: Statistics
- Tags: Regression, Estimation Uncertainty, Future Noise
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q7

Source and assessment: [2026-10-11 Q7](../../DailyTests/2026-10-11.md#q7--confidence-vs-prediction-intervals). The reference material below does not change that attempt’s recorded result.

### Question

Under fixed-design normal regression,

```math
Y_i=\alpha+\beta x_i+\varepsilon_i,\quad
\varepsilon_i\overset{\mathrm{iid}}{\sim}N(0,\sigma^2),\quad
S_{xx}=\sum_i(x_i-\bar x)^2\gt0,\quad s^2=\frac{\mathrm{RSS}}{n-2},\quad n\gt2.
```

At $`x_0`$, derive 95% intervals for the conditional mean and one independent new observation. Explain their widths, behavior away from $`\bar x`$, and omitted extrapolation risks.

### Key solution

Set $`d=x_0-\bar x`$ and $`h_0=1/n+d^2/S_{xx}`$. The error representation shows why the covariance vanishes:

```math
\hat\beta-\beta=\frac{\sum_i(x_i-\bar x)\varepsilon_i}{S_{xx}},\qquad
\hat\mu(x_0)=\bar Y+d\hat\beta,\qquad
\mathrm{Cov}(\bar Y,\hat\beta)=\frac{\sigma^2}{nS_{xx}}\sum_i(x_i-\bar x)=0.
```

```math
\mathrm{Var}(\hat\mu(x_0))=\sigma^2h_0,\qquad
\frac{\hat\mu(x_0)-\mu(x_0)}{s\sqrt{h_0}}\sim t_{n-2}.
```

Normality gives independent residual scale estimation. New-observation noise adds an independent variance term:

```math
\begin{aligned}
\text{Mean CI:}&\quad\hat\mu(x_0)\pm t_{n-2,0.975}s\sqrt{h_0},\\
\text{Prediction interval:}&\quad\hat\mu(x_0)\pm t_{n-2,0.975}s\sqrt{1+h_0}.
\end{aligned}
```

The conditional response variance remains $`\sigma^2`$; estimator uncertainty increases away from the design center. Neither interval protects against a wrong model or a changed regime.

## Assessment history

- [2026-10-11 Q7 — assessment](../../DailyTests/2026-10-11.md#q7--confidence-vs-prediction-intervals)

## Related questions and knowledge

- [S010 — OLS Significance, Randomness, and Robust Standard Errors](S010_OLS_Significance_Randomness_and_Robust_Standard_Errors.md) — Sampling uncertainty and the target of an interval.
