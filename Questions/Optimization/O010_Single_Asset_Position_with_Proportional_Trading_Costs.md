# O010 — Single-Asset Position with Proportional Trading Costs

## Metadata

- Category: Optimization
- Tags: Position Choice, Risk Penalty, Proportional Trading Costs
- Date Added: 2026-10-24
- Original drill: October 23, 2026, Q4
- Status: Discussed October 25. User reports independently obtaining the same answer before the displayed reference; exact written working was not submitted or verified. Do not classify as Partial / Hinted merely because the reference was later shown.

## Core Question

You currently hold position $`q_0\in\mathbb R`$ in one asset. Choose a new position $`q\in\mathbb R`$ to maximize:

```math
J(q)=\mu q-\frac a2q^2-c|q-q_0|,
```

where mu is forecast P&L per unit position, $`a\gt0`$ is a quadratic risk-penalty coefficient, and $`c\ge0`$ is the cost per unit traded.

1. Derive the optimal position for every value of mu, including boundary cases.
2. Identify exactly when retaining $`q_0`$ is optimal.
3. Justify global optimality, including what happens at $`q=q_0`$. Briefly interpret how increasing c changes the decision.

## Solution

### Piecewise first-order conditions

For a position above the current holding:

```math
q\gt q_0:\qquad J'(q)=\mu-aq-c,
\qquad q=\frac{\mu-c}{a}.
```

This stationary point belongs to that region when mu exceeds the upper threshold below. For a position below the current holding:

```math
q\lt q_0:\qquad J'(q)=\mu-aq+c,
\qquad q=\frac{\mu+c}{a}.
```

The unique optimum, including equality boundaries, is:

```math
\boxed{
q^*=\begin{cases}
\dfrac{\mu+c}{a},&\mu\lt aq_0-c,\\[6pt]
q_0,&aq_0-c\le\mu\le aq_0+c,\\[6pt]
\dfrac{\mu-c}{a},&\mu\gt aq_0+c.
\end{cases}}
```

### No-trade interval and the kink

The one-sided derivatives at the current holding are:

```math
J'_-(q_0)=\mu-aq_0+c,\qquad
J'_+(q_0)=\mu-aq_0-c.
```

Keeping the current position is optimal when the left derivative is nonnegative and the right derivative is nonpositive. Equivalently:

```math
\boxed{|\mu-aq_0|\le c}.
```

The risk-adjusted marginal gain from changing the current holding has magnitude no greater than the trading cost. Both equality boundaries are included in the no-trade case.

### Global optimality and economic interpretation

The quadratic part is strictly concave because a is positive. The negative absolute-cost term is concave, so the entire objective is strictly concave. The interior stationary points or the stated one-sided condition therefore identify the unique global maximum, including at the kink.

Increasing c widens the no-trade interval and makes the optimum closer to the current position. With zero cost:

```math
c=0:\qquad q^*=\frac\mu a.
```

## Assessment History and Clarification

- [October 23 drill Q4 — October 25 continuation](../../DailyTests/2026-10-23.md#q4--single-asset-position-with-proportional-trading-costs)

The user initially requested the answer because writing it out was cumbersome. After the assistant displayed the reference and initially labeled the item Partial / Hinted, the user clarified: they had already written the same answer and meant that typing the answer was inconvenient. The assistant accepted that clarification. The final assessment is **Cold Solve, user-reported; exact written derivation unverified**, not a directly verified cold derivation. The displayed derivation above is the assistant reference, not a transcription of the user's unsubmitted working. Do not infer inability to solve, a K/R gap, or assisted solving merely from the request to display the answer. Actual time is not recorded.

## Connections

- [O007 — Turnover-Constrained Mean-Variance Portfolio and KKT Active Set](O007_Turnover_Constrained_Mean_Variance_Portfolio_and_KKT_Active_Set.md): proportional absolute trading cost versus an L1 turnover constraint; scalar no-trade boundaries versus a multi-asset active set.
- [T011 — Signal Smoothing, Correlation, and Trading Costs](../TimeSeries/T011_Signal_Smoothing_Correlation_and_Trading_Costs.md): position choice with proportional costs here versus comparing two fixed signal rules under quadratic turnover costs.
