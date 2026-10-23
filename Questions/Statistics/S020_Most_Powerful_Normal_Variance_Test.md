# S020 — Most-Powerful Normal Variance Test

## Metadata

- Category: Statistics
- Tags: Likelihood Ratio, Neyman–Pearson, Power
- Date Added: 2026-10-22
- Original drill dates: 2026-10-15
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-15 Q3

Source and assessment: [2026-10-15 Q3](../../DailyTests/2026-10-15.md#q3--most-powerful-testing-for-increased-normal-variance). The reference material below does not change that attempt’s recorded result.

### Question

An anomaly detector observes one real measurement with hypotheses $`H_0:X\sim N(0,1)`$ and $`H_1:X\sim N(0,4)`$, where the second parameter is variance. Construct the most-powerful test with false-positive probability at most 5%, justify optimality and calculate power. Compare with rejecting when $`X\gt1.645`$. For two independent observations with the same distribution under each hypothesis, give the optimal rejection rule and power. Standard normal CDF expressions and named-distribution quantiles are acceptable.

### Key solution

**Logical sequence:** use the likelihood ratio to choose the rejection region's shape; use the null distribution to set its size; use the alternative distribution to calculate power. A rule is fixed before evaluating these two probabilities.

For two fully specified hypotheses, the Neyman–Pearson lemma selects the largest likelihood ratios. For a small region near an observation, alternative probability is the detection benefit, null probability is the false-positive cost, and their ratio gives benefit per unit cost. Swapping equally costly null-probability regions for higher-ratio regions increases power. The ratio compares the same observation under two hypotheses, not the densities of two different observations; it is not itself a probability or power.

```math
\Lambda(x)=\frac{f_1(x)}{f_0(x)}=\frac12e^{3x^2/8}.
```

This increases with absolute value, so the optimal region is two-sided. Let $`c=\Phi^{-1}(0.975)`$:

```math
P_0(|X|\gt c)=0.05,\qquad c\approx1.959964,
\qquad
\text{Power}=P_1(|X|\gt c)=2[1-\Phi(c/2)]\approx0.327095.
```

Under the alternative, standard deviation is 2, so $`Z=X/2\sim N(0,1)`$. Dividing the statistic and cutoff by 2 rewrites the same rejection event; the raw-data cutoff remains unchanged. The comparison rule has approximately 5% size and lower power:

```math
P_1(X\gt1.645)=1-\Phi(1.645/2)\approx0.205396.
```

For two independent observations, multiply the two likelihood ratios:

```math
S=X_1^2+X_2^2,\qquad
\Lambda(x_1,x_2)=\frac14e^{3S/8}.
```

Thus large squared distance from zero supports the higher-variance alternative; signed observations should not cancel. This is one joint test, not two separate 5% tests.

```math
S\mid H_0\sim\chi^2_2,\qquad
S/4\mid H_1\sim\chi^2_2,\qquad
c_2=\chi^2_{2,0.95}=-2\ln0.05\approx5.991465.
```

```math
\text{Reject }H_0\text{ when }S\gt c_2,\qquad
\text{Power}=P(\chi^2_2\gt c_2/4)=e^{-c_2/8}=0.05^{1/4}\approx0.472871.
```

The squared-sum rule is specific to this independent zero-mean normal variance comparison. More generally, reject for a large likelihood ratio; its level set may be one tail, two tails, a central interval or disconnected regions. Composite hypotheses with unknown parameters require additional work and do not automatically admit a test most powerful against every alternative. Boundary randomization can be needed for exact size in discrete models.

## Assessment history

- [2026-10-15 Q3 — assessment](../../DailyTests/2026-10-15.md#q3--most-powerful-testing-for-increased-normal-variance)

## Related questions and knowledge

- [S013 — One-Sided Normal Mean Test](S013_One_Sided_Normal_Mean_Test.md) — Rejection regions, null calibration and power.
