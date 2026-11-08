# T014 — Observed Price Noise and Return Reversal

## Metadata

- Category: Time Series
- Tags: Observation Noise, Return Autocovariance, Linear Forecasting
- Date Added: 2026-11-07
- Original drill: November 7, Q4
- Status: Discussed November 8. Overall Partial / Hinted; all part-1 and part-2 coefficients independently correct. Part-3 core judgments correct, execution/cost reasoning supplied. Terminology and target clarification do not count as conceptual errors.

## Core Question

An unobserved efficient price follows:

```math
S_t=S_{t-1}+u_t,
```

where the increments are iid, have mean zero and positive variance sigma squared. You observe:

```math
P_t=S_t+\varepsilon_t,
```

where the observation errors are iid, have mean zero and positive variance eta squared, and are independent of all efficient-price increments. Define the observed return:

```math
r_t=P_t-P_{t-1}.
```

1. Derive the variance of an observed return, its lag-one autocovariance, and its autocovariance at every integer lag k at least 2.
2. Find the best linear forecast below of the next observed return. How do the optimal coefficients change if the target is instead the next efficient-price increment?

```math
a+br_t\quad\text{for target }r_{t+1},
\qquad\text{alternative target }S_{t+1}-S_t.
```

3. A researcher interprets negative observed-return autocorrelation as evidence that the efficient price mean-reverts and that a profitable reversal strategy exists. Assess both claims in a few sentences.

## Solution

### 1. Observed-return moments

Expand the observed price difference:

```math
r_t=u_t+\varepsilon_t-\varepsilon_{t-1}.
```

All three components are independent, giving:

```math
\mathrm{Var}(r_t)=\sigma^2+2\eta^2.
```

Adjacent returns share one observation error with opposite signs:

```math
r_{t-1}=u_{t-1}+\varepsilon_{t-1}-\varepsilon_{t-2},
\qquad\mathrm{Cov}(r_t,r_{t-1})=-\eta^2.
```

Returns at lags at least two share no component, hence:

```math
\mathrm{Cov}(r_t,r_{t-k})=0,\qquad k\ge2.
```

### 2. Best linear forecasts

The target and predictor both have mean zero. The observed-return projection coefficients are:

```math
a=0,\qquad
b=\frac{\mathrm{Cov}(r_{t+1},r_t)}{\mathrm{Var}(r_t)}
=-\frac{\eta^2}{\sigma^2+2\eta^2}.
```

For the alternative target, keep the predictor unchanged and replace only the target:

```math
S_{t+1}-S_t=u_{t+1},\qquad
\mathrm{Cov}(u_{t+1},r_t)=0,\qquad
a=0,\quad b=0.
```

These are best linear forecasts under the stated second-moment assumptions. A full conditional-mean formula would need additional assumptions; joint normality was not stipulated.

### 3. Reversal, efficient prices and trading profits

The efficient price is a random walk with iid zero-mean increments. The negative observed-return autocorrelation comes from differenced observation noise, not an efficient-price tendency to return to a fixed price level.

Observed returns exhibit short-term reversal: the next observed return's best linear forecast has the opposite sign to the current observed return. “Observed returns show short-term mean-reverting behavior” is understandable informal wording; “negative lag-one autocorrelation” or “short-term reversal in observed returns” is more precise. This terminology refinement does not establish an additional conceptual gap.

Predictability does not alone establish net profitability. Check whether the observed prices are executable, whether the noise reversal can be captured by a feasible trade, and whether the edge survives bid-ask spreads, fees and impact. Large variance affects risk and estimation precision; it does not by itself prove or disprove positive expected profit. If execution at the observed prices is allowed without costs, this model can support positive expected gross reversal profits; do not conclude that noise-driven predictability is necessarily untradeable.

Interview-length wording supplied in discussion:

> The efficient price is a random walk. The negative autocorrelation in observed returns comes from observation noise. It implies linear predictability of observed returns, but profitable trading additionally requires executable prices and an edge that survives trading costs.

### Terminology — efficient versus observed returns

本题的 efficient return 是潜在有效价格的变化，而 observed return 还包含观测噪声的变化：

```math
\underbrace{S_t-S_{t-1}}_{\text{efficient return}}=u_t,
\qquad
\underbrace{P_t-P_{t-1}}_{\text{observed return}}
=u_t+\varepsilon_t-\varepsilon_{t-1}.
```

例如有效价格从 100 变到 101，有效价格变化是 1；两次观测噪声不同，实际看到的价格变化不一定是 1。这里的 return 是价格差，未除以前期价格，因此不是百分比收益率。有效增量的 iid 性质来自题目明确假设，不是单凭 efficient 这个名称推出来的。

## Connections

- [T009 — MA(1)](T009_MA1_Equivalence_Invertibility_and_Fitting.md): compare short-lag covariance structure without confusing observed noise reversal with latent-price mean reversion.
- [T013 — Multihorizon Forecast Targets](T013_Multihorizon_AR1_Level_and_Change_Forecasts.md): forecast coefficients depend on the target; changing the target does not redefine the predictor.

## Assessment History

- [November 7 Q4, continued November 8](../../DailyTests/2026-11-07.md#q4--observed-price-noise): all part-1 moments and part-2 coefficients independently correct; efficient-target zero covariance independently justified after target wording was clarified. Core part-3 judgments independently correct, execution/cost reasoning supplied. Overall Partial / Hinted; K/R unresolved, no implementation task, actual time Not recorded. See the log for terminology and clarification evidence.
