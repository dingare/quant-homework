# T013 — Multihorizon AR(1): Level and Change Forecasts

## Metadata

- Category: Time Series
- Tags: Forecasting, Prediction Targets, Population R-squared
- Date Added: 2026-11-01
- Original drill: October 31, 2026, Q4
- Status: Discussed November 1. Overall Partial / Hinted; independently correct final limits and interpretation are preserved in the dated assessment.

## Core Question

A spread follows the stationary process:

```math
X_{t+1}=\phi X_t+\varepsilon_{t+1},\qquad
0\lt\phi\lt1,\qquad
\varepsilon_t\overset{\mathrm{iid}}{\sim}N(0,\sigma^2).
```

Innovations are independent of past observations. Treat phi and the positive innovation variance as known. For integer horizon h at least one, consider two prediction targets:

```math
A=X_{t+h},\qquad B=X_{t+h}-X_t.
```

1. Derive the optimal squared-error forecast of each target using observations through time t, and its conditional mean squared prediction error.
2. For each target, derive the population out-of-sample score below, using its unconditional mean as the benchmark.

```math
R^2=1-\frac{E[(\text{target}-\text{forecast})^2]}
{\mathrm{Var}(\text{target})}.
```

3. Compare the scores as h tends to infinity. Would the difference establish that one forecasting task contains more economically useful information? Explain briefly.

Original budget: 9 minutes; actual time not recorded.

## Solution

### 1. Forecasts and conditional mean squared error

Let F_t denote all observations available through time t. Iterating the recursion gives:

```math
X_{t+h}=\phi^hX_t+\sum_{j=1}^{h}\phi^{h-j}\varepsilon_{t+j}.
```

The future innovations are independent of current information and have zero mean. Therefore the conditional-mean forecasts are:

```math
\widehat A=E[X_{t+h}\mid\mathcal F_t]=\phi^hX_t,
\qquad
\widehat B=E[X_{t+h}-X_t\mid\mathcal F_t]=(\phi^h-1)X_t.
```

Both prediction errors equal the same sum of future innovations:

```math
A-\widehat A=B-\widehat B=\sum_{j=1}^{h}\phi^{h-j}\varepsilon_{t+j}.
```

Independence eliminates cross-covariances, so square the coefficients before summing the innovation variances:

```math
E[(A-\widehat A)^2\mid\mathcal F_t]
=E[(B-\widehat B)^2\mid\mathcal F_t]
=\sigma^2\sum_{r=0}^{h-1}\phi^{2r}
=\sigma^2\frac{1-\phi^{2h}}{1-\phi^2}.
```

### Why is the conditional mean optimal under squared error?

For any square-integrable target Y, set m = E[Y | F_t]. For any forecast a based on the same information, expand Y - a = (Y - m) + (m - a). The conditional cross term vanishes because the conditional mean of Y - m is zero:

```math
\begin{aligned}
E[(Y-a)^2\mid\mathcal F_t]
&=E[(Y-m)^2\mid\mathcal F_t]
+2(m-a)E[Y-m\mid\mathcal F_t]+(m-a)^2\\
&=\mathrm{Var}(Y\mid\mathcal F_t)+(m-a)^2.
\end{aligned}
```

The conditional variance is unaffected by the forecast choice. The added squared term is minimized at a = m. This argument requires a finite second moment, not normality.

### 2. Stationary variance, covariance and population R-squared

Stationarity makes the variance equal across dates. Writing that variance as V:

```math
\mathrm{Var}(X_{t+1})=\phi^2\mathrm{Var}(X_t)+\sigma^2,
\qquad V=\phi^2V+\sigma^2,
\qquad V=\frac{\sigma^2}{1-\phi^2}.
```

Each period retains phi squared times the previous variance and adds the innovation variance. The stationary value solves that balance equation.

The conditional prediction MSE is constant across current observations, so averaging it gives the same unconditional MSE:

```math
\mathrm{MSE}=V(1-\phi^{2h}).
```

For the level target, stationarity gives variance V. Thus:

```math
R_A^2=1-\frac{V(1-\phi^{2h})}{V}=\phi^{2h}.
```

The expansion separates a multiple of the current value from independent future noise, giving:

```math
\mathrm{Cov}(X_{t+h},X_t)=\phi^hV,
\qquad
\mathrm{Var}(B)=V+V-2\phi^hV=2V(1-\phi^h).
```

Consequently:

```math
R_B^2=1-\frac{V(1-\phi^{2h})}{2V(1-\phi^h)}
=1-\frac{1+\phi^h}{2}
=\frac{1-\phi^h}{2}.
```

The denominator is the unconditional variance of the prediction target. Equal prediction errors need not give equal R-squared values when the targets differ.

### 3. Long-horizon limits and interpretation

Because phi is strictly between zero and one:

```math
\phi^h\longrightarrow0,\qquad
R_A^2\longrightarrow0,\qquad
R_B^2\longrightarrow\frac12.
```

The forecasts approach zero for the future level and minus the current value for the change. The change target contains an already observed component. At long horizons the covariance of the two levels vanishes, so the change's total variance approaches 2V, while the remaining prediction MSE approaches V.

The user independently identified both limits and correctly explained that knowing the current value accounts for half the change variance in this limit. The assistant supplied the detailed variance decomposition afterward. The two targets have identical prediction errors at every horizon; the different scores reflect their definitions and benchmark variances. The higher change-target score does not by itself establish additional forecasting information or a trading advantage.

## Reading recommendations and study priorities

The user reports that time series has not yet been reviewed and that many foundations are unfamiliar. For the next 1–2 weeks, prioritize stationarity and autocovariance, AR(1) and MA(1), conditional forecasts and forecast-error variance, then chronological evaluation and residual diagnostics. This is a preparation recommendation, not a new assessment or a compulsory review block.

- [Hyndman and Athanasopoulos, Forecasting: Principles and Practice, third edition — Chapter 9](https://otexts.com/fpp3/arima.html): use Sections 9.1, 9.3, 9.4 and 9.8 for stationarity/differencing, AR models, MA models and forecasts. This is the suggested accessible first reading.
- [The same book — Chapter 5](https://otexts.com/fpp3/toolbox.html): Sections 5.4, 5.8 and 5.10 cover residual diagnostics, forecast accuracy and time-series cross-validation. Focus on the reasoning; its R examples do not require changing the user's Python interview workflow.
- [Brockwell and Davis, Introduction to Time Series and Forecasting, third edition](https://link.springer.com/book/10.1007/978-3-319-29854-2): use Chapters 2, 3 and 5 as a more mathematical reference for stationary processes, ARMA models, and modeling/forecasting with ARMA processes. Select relevant sections rather than committing to a full cover-to-cover reading before imminent interviews.

## Assessment History

- [October 31 drill, continued through November 1 — Q4](../../DailyTests/2026-10-31.md#q4--multihorizon-ar1-forecasts).

## Connections

- [T003 — AR(1) First Passage Time](T003_AR1_First_Passage_Time_and_Why_Persistence_Changes_Waiting_Time.md): a fixed-horizon forecasting task rather than a stopping-time question.
- [T012 — Probability Forecasts and Evaluation](T012_Probability_Forecasts_Calibration_and_Evaluation.md): a different forecast-evaluation task; target and benchmark definitions matter in both questions.
