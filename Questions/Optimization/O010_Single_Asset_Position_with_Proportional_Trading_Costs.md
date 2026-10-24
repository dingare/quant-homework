# O010 — Single-Asset Position with Proportional Trading Costs

## Metadata

- Category: Optimization
- Tags: Position Choice, Risk Penalty, Proportional Trading Costs
- Date Added: 2026-10-24
- Original drill: October 23, 2026, Q4
- Status: Pending; unattempted. No hints or solution supplied.

## Core Question

You currently hold position $`q_0\in\mathbb R`$ in one asset. Choose a new position $`q\in\mathbb R`$ to maximize:

```math
J(q)=\mu q-\frac a2q^2-c|q-q_0|,
```

where mu is forecast P&L per unit position, $`a\gt0`$ is a quadratic risk-penalty coefficient, and $`c\ge0`$ is the cost per unit traded.

1. Derive the optimal position for every value of mu, including boundary cases.
2. Identify exactly when retaining $`q_0`$ is optimal.
3. Justify global optimality, including what happens at $`q=q_0`$. Briefly interpret how increasing c changes the decision.

## Assessment History

- [October 23 Q4 — Pending](../../DailyTests/2026-10-23.md#q4--single-asset-position-with-proportional-trading-costs)

No solution is filed. Archival filing does not count as an attempt or completion.
