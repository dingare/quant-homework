# S009 — Overlapping Three-Day Returns and Hansen–Hodrick Inference

## Metadata

- Category: Statistics
- Secondary: Econometrics, Time Series, Predictive Regressions
- Difficulty: ★★★★☆
- Tags: Overlapping Returns, Hansen–Hodrick, HAC, Long-Run Variance, Predictive Regression
- Review Priority: High
- Date Added: 2026-08-26
- Status: Final
- Personal Note: Overlap creates residual autocorrelation, but inference depends on autocorrelation of the regression score.

## Core Question

Suppose the one-day predictive-return model is

$$
r_{t+1}=0.2x_t+\varepsilon_{t+1},
$$

where $x_t$ and $\varepsilon_t$ are iid, mutually independent, mean zero, and appropriately normalized. A researcher runs a predictive regression using overlapping three-day forward returns. Explain:

1. why OLS consistently estimates the predictive coefficient $0.2$;
2. why the overlapping regression residual has autocovariances $3,2,1,0$ at lags $0,1,2,3$ under unit innovation variance;
3. which HAC bandwidth is required;
4. when overlap does and does not inflate the standard error.

## Setup

Index the three-day forecast so that its conditional mean is $0.2x_t$ and write its unpredictable component as

$$
u_t=e_{t+1}+e_{t+2}+e_{t+3},
$$

where $e_t$ is the normalized one-day innovation, with $E[e_t]=0$ and $E[e_t^2]=1$. Any future iid signal terms in the literal sum of one-day returns can be absorbed into $e_t$; the coefficient on the currently observed $x_t$ remains $0.2$.

Thus the overlapping regression is

$$
R^{(3)}_{t,t+3}=0.2x_t+u_t.
$$

## Solution

### Consistency of OLS

Because $x_t$ is independent of current and future innovations,

$$
E[x_tu_t]=0.
$$

Therefore the population regression coefficient is $0.2$, and

$$
\boxed{\hat\beta_{\mathrm{OLS}}\xrightarrow{p}0.2}.
$$

Overlap changes the sampling variance, not this exogeneity argument.

### Residual Autocovariances

Adjacent three-day residuals share innovations:

$$
u_t=e_{t+1}+e_{t+2}+e_{t+3},
$$

$$
u_{t-1}=e_t+e_{t+1}+e_{t+2}.
$$

Counting common unit-variance terms gives

$$
\gamma_u(0)=3,
\qquad
\gamma_u(1)=2,
\qquad
\gamma_u(2)=1,
\qquad
\gamma_u(k)=0\quad\text{for }k\ge3.
$$

This is an MA(2) dependence pattern. Hansen–Hodrick inference, or a HAC estimator, must therefore include lags through $2$:

$$
\boxed{L=2}.
$$

The original Hansen–Hodrick estimator uses the overlap-implied autocovariances without Bartlett downweighting; Newey–West is a positive-semidefinite weighted alternative.

### Score Long-Run Variance

The asymptotic variance of $\hat\beta$ depends on the score

$$
g_t=x_tu_t,
$$

not on $u_t$ alone. Its long-run variance is

$$
\Omega_g
=\Gamma_g(0)+2\Gamma_g(1)+2\Gamma_g(2),
$$

where

$$
\Gamma_g(k)=E[x_tx_{t-k}u_tu_{t-k}].
$$

If $x_t$ is iid and mean zero, then $E[x_tx_{t-k}]=0$ for $k\ne0$. Under independence from the residual process,

$$
\Gamma_g(1)=\Gamma_g(2)=0
$$

even though $u_t$ is autocorrelated. This is the iid-score special case: overlap alone need not inflate the coefficient standard error.

If instead the predictor is highly persistent, adjacent $x_t$ values are nearly equal. Then the score inherits the full overlap pattern. Relative to the lag-zero variance,

$$
\frac{3+2(2)+2(1)}{3}=3.
$$

Hence the standard-error inflation approaches

$$
\boxed{\sqrt3\approx1.73}.
$$

## Intuition

Three adjacent overlapping returns reuse the same daily shocks. But a slope estimate averages products $x_tu_t$. If the signs of iid predictors change independently across dates, those products do not remain correlated. A persistent predictor keeps nearly the same exposure attached to reused shocks, reducing the effective amount of independent information.

## Common Mistakes

- Concluding from residual autocorrelation alone that the slope standard error must rise.
- Using an HAC cutoff of $1$ for a three-day overlapping return; the induced residual is MA(2).
- Treating HAC as a correction for endogeneity or coefficient bias.
- Confusing Hansen–Hodrick's unweighted overlap correction with Bartlett-weighted Newey–West.

## Interview Follow-ups

1. What changes for a $k$-day overlapping return?
2. Why can an iid predictor eliminate nonzero score autocovariances?
3. How would predictor autocorrelation between zero and one affect the inflation factor?
4. Why does a correct HAC estimator not repair $E[x_tu_t]\ne0$?

## Finance / Market Application

Overlapping weekly or monthly forward returns are common in signal research because they create more labeled observations. They do not create more independent information. Correct inference must reflect both return overlap and signal persistence.

## Connections

- [S005 — HAC / Newey–West Inference for Persistent Trading Signals](S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md)

## What to Remember

> Three-day overlap produces residual autocovariances $3,2,1,0$ and requires HAC lag $2$, but standard errors are governed by the score $x_tu_t$. With a highly persistent predictor, the limiting inflation is $\sqrt3\approx1.73$.
