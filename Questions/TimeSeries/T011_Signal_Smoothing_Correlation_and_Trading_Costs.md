# T011 — Signal Smoothing, Correlation, and Trading Costs

## Metadata

- Category: TimeSeries
- Tags: Autocovariance, Signal Evaluation, Turnover
- Date Added: 2026-10-22
- Original drill dates: 2026-10-17
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-17 Q4

Source and assessment: [2026-10-17 Q4](../../DailyTests/2026-10-17.md#q4--signal-smoothing-correlation-and-trading-costs). The reference material below does not change that attempt’s recorded result.

### Question

The daily signal $`x_t`$ is iid standard normal and next-day return satisfies $`r_{t+1}=\beta x_t+\varepsilon_{t+1}`$, with $`\beta\gt0`$. Errors are iid, mean zero, variance $`\sigma^2\gt0`$, independent of the entire signal sequence. At time t, strategies take positions:

```math
q_t^A=x_t,\qquad q_t^B=\frac{x_t+x_{t-1}}{\sqrt2},\qquad
J(q)=E[q_tr_{t+1}]-\kappa E[(q_t-q_{t-1})^2],\quad\kappa\ge0.
```

Compare position variances and population correlations with next-day return. Calculate both objectives and determine exactly when each strategy is preferred. Can ranking by forecast correlation disagree with ranking by J? Explain the economic reason.

### Key solution

Both position variances are one. Return variance and forecast correlations are:

```math
\mathrm{Var}(r_{t+1})=\beta^2+\sigma^2,\quad
\mathrm{Cov}(q_t^A,r_{t+1})=\beta,\quad
\mathrm{Cov}(q_t^B,r_{t+1})=\frac\beta{\sqrt2},
\quad
\rho_A=\frac\beta{\sqrt{\beta^2+\sigma^2}},\quad
\rho_B=\frac{\rho_A}{\sqrt2}.
```

Adjacent B positions share a signal, despite the raw signals being iid:

```math
q_t^A-q_{t-1}^A=x_t-x_{t-1},\qquad
q_t^B-q_{t-1}^B=\frac{x_t-x_{t-2}}{\sqrt2}.
```

Thus the expected squared position changes are two and one respectively, giving:

```math
J(A)=\beta-2\kappa,\qquad J(B)=\frac\beta{\sqrt2}-\kappa,
\qquad
J(A)-J(B)=\beta\left(1-\frac1{\sqrt2}\right)-\kappa.
```

A is preferred below that cost threshold, B above it, and both tie at equality. Correlation always favors A.

**Economic interpretation discussed after the drill:** A responds entirely to today's predictive signal; B smooths it with yesterday's signal, which has no incremental predictive value for tomorrow in this model. B sacrifices expected gross return but reduces squared turnover. The square-root normalization equalizes position variance; it does not establish equal P&L variance. Smoothing is worthwhile when saved cost exceeds lost gross return. The quadratic cost penalizes large adjustments disproportionately. J is expected return net of this modeled cost, not Sharpe or a complete portfolio-risk objective. Research should evaluate the positions and costs induced by a forecast, as well as predictive correlation.

Related: [forecast validation](T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md) and [execution impact / inventory risk](../Optimization/O004_Optimal_Execution_with_Impact_and_Inventory_Risk.md).

## Assessment history

- [2026-10-17 Q4 — assessment](../../DailyTests/2026-10-17.md#q4--signal-smoothing-correlation-and-trading-costs)

## Related questions and knowledge

- [T009 — MA(1) Equivalence, Invertibility, and Fitting](T009_MA1_Equivalence_Invertibility_and_Fitting.md) — Lagged signal combinations, autocovariance and representation.
- [O004 — Optimal Execution with Impact and Inventory Risk](../Optimization/O004_Optimal_Execution_with_Impact_and_Inventory_Risk.md) — Predictive fit versus turnover and execution costs.
