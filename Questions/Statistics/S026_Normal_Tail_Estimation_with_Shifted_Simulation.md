# S026 — Normal Tail Estimation with Shifted Simulation

## Metadata

- Category: Statistics
- Tags: Monte Carlo, Estimator Unbiasedness, Variance, Shifted Sampling
- Date Added: 2026-11-01
- Original drill: November 1, 2026, Q3
- Status: Pending, unattempted. Original prompt only; no hints or solution supplied.

## Core Question

You want to estimate the following probability by simulation:

```math
p=P(Z\gt3),\qquad Z\sim N(0,1).
```

A colleague instead generates independent draws $`X_1,\ldots,X_N\sim N(m,1)`$, where $`m\gt0`$, and reports the fraction exceeding 3.

1. What quantity does that fraction estimate? Construct an estimator of p using these same draws that is unbiased for every fixed m. Derive any weighting explicitly.
2. Derive your estimator's variance and compare its expression with the variance of direct simulation from N(0,1). You may express the answer using the standard normal CDF Phi.
3. Does moving m farther to the right necessarily improve precision? Explain why the observed number of threshold exceedances is insufficient to decide.

No code or numerical normal-tail evaluation is required. Original budget: 14 minutes; actual time Not recorded.

## Assessment History

- [November 1 Q3](../../DailyTests/2026-11-01.md#q3--shifted-simulation): unattempted; deferred to November 2 at the user's request. No solution or hint filed.
