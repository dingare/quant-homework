# S021 — Uniform Endpoint Estimation and Exact Bounds

## Metadata

- Category: Statistics
- Tags: Order Statistics, MSE, Pivots, Confidence Bounds
- Date Added: 2026-10-22
- Original drill dates: 2026-10-17
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-17 Q3

Source and assessment: [2026-10-17 Q3](../../DailyTests/2026-10-17.md#q3--uniform-endpoint-estimation-and-exact-upper-bounds). The reference material below does not change that attempt’s recorded result.

### Question

Observe iid samples from $`\mathrm{Uniform}(0,\theta)`$, with unknown $`\theta\gt0`$ and $`n\ge2`$. Compare $`A=2\bar X`$ and $`B=c_nM`$, where $`M=\max_iX_i`$. Choose $`c_n`$ for unbiasedness, derive both MSEs and determine whether one is smaller for every positive parameter. Construct an exact one-sided 95% upper confidence bound U with $`P_\theta(\theta\le U)=0.95`$ for every positive parameter. Derive distributional results used.

### Key solution

The user's independent maximum CDF and mean integration give:

```math
F_M(m)=\left(\frac m\theta\right)^n\quad(0\le m\le\theta),\qquad
E[M]=\frac{n\theta}{n+1},\qquad c_n=\frac{n+1}{n}.
```

The CDF is zero below zero and one above the endpoint. Both estimators are unbiased, so MSE equals variance:

```math
\mathrm{MSE}(A)=\frac4{n^2}\sum_{i=1}^n\frac{\theta^2}{12}=\frac{\theta^2}{3n},
\qquad
\mathrm{Var}(M)=\frac{n\theta^2}{(n+1)^2(n+2)},
\qquad
\mathrm{MSE}(B)=\left(\frac{n+1}{n}\right)^2\mathrm{Var}(M)=\frac{\theta^2}{n(n+2)}.
```

Thus B has strictly smaller MSE for all stated n and positive parameters. For an upper bound, set $`U=aM`$ and calibrate coverage:

```math
P_\theta(\theta\le aM)=P_\theta(M\ge\theta/a)=1-a^{-n}=0.95,
\qquad
\boxed{U=\frac{M}{0.05^{1/n}}}.
```

The rule uses only sample data and n. Repeated-sampling coverage is exactly 95% for each fixed parameter, not merely an asymptotic approximation or a posterior probability statement.

The sample mean can also give an exact one-sided bound. Let $`Z=\bar X/\theta`$ and let its fifth percentile be $`q_{0.05}`$. Its distribution depends only on n, since it is the average of iid standard uniforms:

```math
U_{\mathrm{mean}}=\frac{\bar X}{q_{0.05}},\qquad
P_\theta(\theta\le U_{\mathrm{mean}})=P(Z\ge q_{0.05})=0.95.
```

The mean is not intrinsically two-sided; its exact quantile is less simple. Maximum-based inference is convenient and uses a sufficient statistic: for nonnegative observations, the likelihood is $`\theta^{-n}\mathbf1\{\theta\ge M\}`$. B is a one-to-one scaling of M, so it contains the same information. Smaller estimator MSE alone does not establish confidence-bound coverage.

## Assessment history

- [2026-10-17 Q3 — assessment](../../DailyTests/2026-10-17.md#q3--uniform-endpoint-estimation-and-exact-upper-bounds)

## Related questions and knowledge

- [S011 — Exponential MLE and Fisher Information](S011_Exponential_MLE_and_Fisher_Information.md) — Estimator inference; regular likelihood versus parameter-dependent support.
- [Random Points Order Statistics and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md) — Knowledge card.
