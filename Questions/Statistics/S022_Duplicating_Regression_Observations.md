# S022 — Duplicating Regression Observations

## Metadata

- Category: Statistics
- Tags: OLS, Dependence, Effective Information, Standard Errors
- Date Added: 2026-10-22
- Original drill dates: 2026-10-18
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-18 Q3

Source and assessment: [2026-10-18 Q3](../../DailyTests/2026-10-18.md#q3--duplicating-regression-observations). The reference material below does not change that attempt’s recorded result.

### Question

For n greater than two, fit an OLS intercept and slope to fixed, nonconstant predictors:

```math
y_i=\alpha+\beta x_i+\varepsilon_i,\qquad
\varepsilon_i\text{ independent }N(0,\sigma^2).
```

A colleague duplicates every observed row exactly once and refits using the usual formula treating all 2n rows as independent. Compare coefficients, residual sum of squares and estimated residual variance with exact factors in n. Derive the multiplicative change in reported slope SE and the t-statistic for testing zero slope, assuming a nonzero original slope estimate. Has evidence increased? What should valid inference recognize? Contrast with a genuinely new response at each original predictor with independent noise.

### Key solution

Exact duplication leaves fitted coefficients and R-squared unchanged, doubles RSS and doubles Sxx. The software's residual scale and reported SE obey:

```math
s^2=\frac{RSS}{n-2},\qquad
s_{\rm dup}^2=\frac{2RSS}{2n-2}
=\frac{n-2}{n-1}s^2,
\qquad
S_{xx,\rm dup}=2S_{xx}.
```

```math
\frac{SE_{\rm dup}}{SE_{\rm original}}
=\sqrt{\frac{n-2}{2n-2}},
\qquad
t_{\rm dup}=\sqrt{\frac{2n-2}{n-2}}\ t_{\rm original}.
```

The absolute t-statistic increases; a negative t becomes more negative. Large-sample factors approach one over square root of two for SE and square root of two for absolute t.

Exact copies share the same error and add no information. Treating them as independent understates uncertainty; deduplication restores the original inference.

If each original predictor instead receives a newly sampled independent response, there is genuinely additional information. Under the same model:

```math
\mathrm{Var}(\hat\beta_{\rm independent\ new})
=\frac{\sigma^2}{2S_{xx}}
=\frac12\mathrm{Var}(\hat\beta_{\rm original}).
```

The realized coefficient and estimated SE now vary with new data, so realized absolute t need not increase. For a nonzero true slope, additional independent observations generally improve power.

## Assessment history

- [2026-10-18 Q3 — assessment](../../DailyTests/2026-10-18.md#q3--duplicating-regression-observations)

## Related questions and knowledge

- [S009 — Overlapping Three-Day Returns and Hansen–Hodrick Inference](S009_Overlapping_Three_Day_Returns_and_Hansen_Hodrick_Inference.md) — Reused information invalidates naive independent-observation inference.
