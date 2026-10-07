# S010 — OLS Significance, Randomness, and Robust Standard Errors

## Metadata

- Category: Statistics
- Interview Relevance: High
- Tags: OLS, Inference, Heteroskedasticity, Endogeneity
- Date Added: 2026-10-06
- Status: Final
- Source: 2026-10-06 interview drill; worked solution added after the timed attempt at the user's request.

## Core Question

Given $y_t=\alpha+\beta x_t+\epsilon_t$, $\hat\beta=0.30$ and $SE(\hat\beta)=0.10$: Is beta significant? What is random? Does heteroskedasticity bias OLS? What does it break? Do robust standard errors fix endogeneity, and why?

## Solution

1. **Significance:** For a two-sided test of $H_0:\beta=0$, the statistic is $t=0.30/0.10=3$. With a valid standard error and a large-sample normal approximation, the two-sided p-value is about 0.0027 and the 95% interval is $0.30\pm1.96(0.10)=[0.104,0.496]$. This rejects at 5% and 1% under that approximation. Exact finite-sample significance requires degrees of freedom and the relevant assumptions; the prompt alone does not specify them.
2. **What is random:** In frequentist inference, the population parameter beta is fixed but unknown. Across repeated samples, the estimator, estimated standard error, test statistic, and confidence interval are random. Conditional on fixed regressors, the response varies through the errors; with random design, regressors vary too. The observed estimate is one realization.
3. **Bias:** Heteroskedasticity alone does not bias OLS. Conditional mean-zero errors, $E[\epsilon\mid X]=0$, plus full rank yield conditional unbiasedness. Changing conditional variance does not violate that mean restriction.
4. **What breaks:** The usual homoskedastic variance formula and its standard errors are generally wrong; tests and confidence intervals based on them can be misleading. OLS also loses its general efficiency guarantee among linear unbiased estimators.
5. **Robust standard errors:** They change estimated uncertainty, not the OLS coefficient. They do not fix endogeneity.
6. **Why:** With an intercept, the population slope under suitable laws of large numbers is

$$
\text{plim}\hat\beta
=\beta+\frac{Cov(x,\epsilon)}{Var(x)}.
$$

A nonzero covariance shifts the probability limit. Adjusting the estimated variance does not remove that shift. Appropriate identification methods, such as valid instruments, require additional assumptions.

For time-series data, heteroskedasticity-only robust standard errors need not handle serial correlation. Use an appropriate dependence-robust estimator when warranted.

## Common Mistakes

- Saying beta itself is random in the frequentist sampling statement.
- Claiming significance without specifying the null or validity of the standard error.
- Confusing heteroskedasticity with endogeneity.
- Expecting robust standard errors to repair bias or serial dependence automatically.

## Connections

- [S001 — OLS bias vs variance](S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md)
- [S005 — HAC inference](S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md)
- [Daily test: Q3](../../DailyTests/2026-10-06.md#q3--ols-and-inference-oral)

## What to Remember

Separate the parameter from its estimator, and separate coefficient identification from uncertainty estimation.
