# S028 — Exponential Fill Times with Timeout Censoring

## Metadata

- Category: Statistics
- Tags: Likelihood, Censoring, Estimation, Fisher Information
- Date Added: 2026-11-11
- Original drill: November 10, 2026, Q3.
- Status: Pending; original prompt only. No hints or solution supplied.

## Core Question

You study the time required to fill an order. For independent orders, the latent fill times have density

```math
f(t;\lambda)=\lambda e^{-\lambda t},\qquad t\geq0,\quad\lambda\gt0.
```

Every order is canceled at a fixed, known timeout $`c\gt0`$ if it has not filled. For each of n orders you observe only

```math
Y_i=\min(T_i,c),\qquad \delta_i=\mathbf 1\{T_i\leq c\}.
```

Assume this model is correct and orders do not affect one another.

1. Construct the likelihood from the actual observations and derive the maximum-likelihood estimate of lambda. Address the case in which no orders fill.
2. Derive the expected Fisher information and a plug-in large-sample standard error. Explain how the timeout affects precision.
3. A colleague discards canceled orders and estimates lambda as the reciprocal of the average completed fill time. Is this consistent for lambda? If not, determine the direction of the distortion.

Keep the answer interview-length; no code is required.

## Assessment History

- [November 10 Q3](../../DailyTests/2026-11-10.md#q3--fill-times-with-timeout-censoring): Pending; no answer assessed.
