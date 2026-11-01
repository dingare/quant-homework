# T013 — Multihorizon AR(1): Level and Change Forecasts

## Metadata

- Category: Time Series
- Tags: Forecasting, Prediction Targets, Population R-squared
- Date Added: 2026-11-01
- Original drill: October 31, 2026, Q4
- Status: Pending, unattempted. Prompt only; no hints or solution supplied.

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

## Assessment History

- [October 31 drill, continued through November 1 — Q4](../../DailyTests/2026-10-31.md#q4--multihorizon-ar1-forecasts).

## Connections

- [T003 — AR(1) First Passage Time](T003_AR1_First_Passage_Time_and_Why_Persistence_Changes_Waiting_Time.md): a fixed-horizon forecasting task rather than a stopping-time question.
- [T012 — Probability Forecasts and Evaluation](T012_Probability_Forecasts_Calibration_and_Evaluation.md): a separate forecast-evaluation question; this Pending prompt has no solution filed.
