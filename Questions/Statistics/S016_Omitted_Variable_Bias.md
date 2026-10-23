# S016 — Omitted-Variable Bias

## Metadata

- Category: Statistics
- Tags: Covariance, Identification, Omitted Variables
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q3

Source and assessment: [2026-10-11 Q3](../../DailyTests/2026-10-11.md#q3--omitted-variable-bias). The reference material below does not change that attempt’s recorded result.

### Question

With iid observations and finite second moments, suppose:

```math
Y=\alpha+\beta X+\gamma Z+\varepsilon,\qquad
E[\varepsilon\mid X,Z]=0,\qquad\mathrm{Var}(X)\gt0.
```

Regress on an intercept and $`X`$ only. Derive the slope limit and evaluate $`\beta=1,\gamma=-3,\mathrm{Cov}(X,Z)=0.8,\mathrm{Var}(X)=1`$. Can more data or robust standard errors recover $`\beta`$? Explain a negative fitted slope with positive structural effect.

### Key solution

```math
\widehat\beta_{\mathrm{short}}\xrightarrow{p}
\beta+\gamma\frac{\mathrm{Cov}(X,Z)}{\mathrm{Var}(X)}
=1-2.4=-1.4.
```

More observations and robust SE do not correct inconsistency from an omitted correlated effect.

## Assessment history

- [2026-10-11 Q3 — assessment](../../DailyTests/2026-10-11.md#q3--omitted-variable-bias)

## Related questions and knowledge

- [S001 — OLS Bias vs Variance with Correlated Regressors](S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md) — Projection coefficients, confounding and omitted-variable bias.
- [S023 — Pooled and Within-Sector Signal Evaluation](S023_Pooled_and_Within_Sector_Signal_Evaluation.md) — General omitted-variable formula and the sector-indicator example.
