# S005 — HAC / Newey–West Inference for Persistent Trading Signals

## Metadata

- Category: Statistics
- Secondary: Econometrics, Time Series, Rates Research
- Difficulty: ★★★★☆
- Tags: HAC, Newey–West, Serial Correlation, Long-Run Variance, Predictive Regression
- Review Priority: High
- Date Added: 2026-07-18
- Status: Finalized
- Personal Note: HAC corrects the long-run variance of the regression score, not residual autocorrelation in isolation.

## Core Question

For $T=500$, consider

$$
\Delta y_t=\alpha+\beta s_{t-1}+u_t,
$$

with $\hat\beta=-0.80$ bp and $\mathrm{SE}_{\mathrm{iid}}(\hat\beta)=0.25$ bp. Assume

$$
\mathrm{Var}(u_t)=4,
\quad \mathrm{Corr}(u_t,u_{t-1})=0.60,
$$

$$
T^{-1}\sum s_{t-1}^2=1,
\quad T^{-1}\sum s_{t-1}s_{t-2}=0.40,
$$

with negligible dependence beyond lag 1. Compute the iid and lag-1 Bartlett HAC $t$-statistics, using weight $w_1=1/2$.

## Hint

Ignoring the intercept,

$$
\hat\beta-\beta\approx
\frac{\sum_t s_{t-1}u_t}{\sum_t s_{t-1}^2}.
$$

The relevant process is the score $s_{t-1}u_t$, whose long-run variance is

$$
\Omega=\Gamma_0+2w_1\Gamma_1.
$$

## Solution

The conventional statistic is

$$
t_{\mathrm{iid}}=\frac{-0.80}{0.25}=-3.20.
$$

Assuming the signal and residual process are independent,

$$
\Gamma_0=E[s_{t-1}^2]E[u_t^2]=1\cdot4=4.
$$

The lag-1 residual covariance is $0.60\times2\times2=2.4$, so

$$
\Gamma_1
=E[s_{t-1}s_{t-2}]E[u_tu_{t-1}]
=0.40\times2.4=0.96.
$$

Therefore,

$$
\Omega=4+2\left(\frac12\right)(0.96)=4.96.
$$

The variance inflation factor relative to the iid calculation is

$$
\frac{4.96}{4}=1.24.
$$

Using the supplied iid standard error as the baseline,

$$
\mathrm{SE}_{\mathrm{HAC}}
=0.25\sqrt{1.24}
\approx0.278,
$$

and

$$
t_{\mathrm{HAC}}
=\frac{-0.80}{0.278}
\approx-2.88.
$$

The simplified moments alone imply an iid standard error $\sqrt{4/500}\approx0.0894$, which differs from the supplied $0.25$. The internally consistent comparison is therefore the inflation-factor calculation above.

## Key Knowledge Points

- HAC estimates the long-run variance of $s_{t-1}u_t$.
- Positive residual autocorrelation does not by itself imply that iid standard errors are too small.
- The sign and size of the correction depend on both regressor and residual serial dependence.
- HAC repairs inference under suitable assumptions; it does not repair endogeneity or coefficient bias.

## Intuition

Here the signal and residual are both positively persistent, so adjacent score contributions move together. The sample contains less independent information than an iid calculation assumes, increasing the standard error.

If the signal were nearly serially uncorrelated, $E[s_{t-1}s_{t-2}]\approx0$, hence $\Gamma_1\approx0$ even with autocorrelated residuals. The HAC correction would then be small.

## Common Mistakes

- Looking only at residual autocorrelation instead of score autocorrelation.
- Treating HAC as a cure for $E[s_{t-1}u_t]\ne0$.
- Mixing a model-implied iid standard error with a reported one without reconciling their scale.
- Using independent-observation inference for overlapping forward returns.

## Interview Follow-ups

1. What happens if the signal's lag-1 autocorrelation is $-0.40$?
2. Why do overlapping $k$-day returns induce dependence?
3. How do Newey–West and clustered standard errors differ?
4. How should the bandwidth be selected?
5. Why does HAC not fix endogeneity?

## Market / Rates Application

Rates signals based on carry, rolldown, momentum, or overlapping forward returns are often persistent. Yield changes may also exhibit volatility clustering, stale-price effects, or short-horizon serial dependence. A naive backtest can therefore overstate the effective number of independent observations.

## Connections

- Predictive regressions and long-run variance estimation
- Overlapping returns and effective sample size
- Signal persistence, residual persistence, and backtest inference
- [S001 — OLS Bias vs Variance with Correlated Regressors](S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md)

## What to Remember

> HAC is about dependence in the regression score $x_tu_t$, not the residual $u_t$ alone.
