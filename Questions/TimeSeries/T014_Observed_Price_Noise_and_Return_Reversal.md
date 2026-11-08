# T014 — Observed Price Noise and Return Reversal

## Metadata

- Category: Time Series
- Tags: Observation Noise, Return Autocovariance, Linear Forecasting
- Date Added: 2026-11-07
- Original drill: November 7, Q4
- Status: Pending, unattempted. Original prompt only; no hints or solution supplied. Resume after Q3.

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

## Assessment History

- [November 7 Q4](../../DailyTests/2026-11-07.md#q4--observed-price-noise): Pending, unattempted. Budget 9 minutes; no actual time, hints or solution recorded.
