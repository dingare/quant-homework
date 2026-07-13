# S003 — Cointegration: Trading Equilibrium Rather Than Correlation

## Metadata

- Category: Statistics
- Secondary: Time Series, Statistical Arbitrage, Mean Reversion
- Difficulty: ★★★★☆
- Tags: Cointegration, Stationarity, Relative Value, Engle-Granger, Mean Reversion
- Review Priority: High
- Date Added: 2026-07-05
- Status: Draft
- Personal Note: Always frame cointegration as an equilibrium concept, not just a test statistic.

## Core Question

Suppose $X_t$ and $Y_t$ are both non-stationary random walks, but there exists some $\beta$ such that

```math
Z_t=Y_t-\beta X_t
```

is stationary.

Why is this much stronger than high correlation, and why is it the foundation of relative value trading?

## Why This Topic Matters

Pairs and RV trading do not really bet on two assets moving together day by day. They bet that a spread has a stable long-run anchor and tends to revert toward it after dislocations.

That is exactly the distinction between:

- correlation,
- equilibrium.

## My Current Understanding

Correlation measures contemporaneous co-movement.

Cointegration says that although each series may wander on its own, a particular linear combination remains stable over time.

So the real traded object is not "Asset A versus Asset B." It is the residual:

```math
Y_t-\beta X_t.
```

## Why High Correlation Is Not Enough

Two random walks can be highly correlated and still drift apart forever. Correlation does not stop the spread from wandering.

That means a highly correlated pair can still be a terrible mean-reversion trade, because "rich" and "cheap" are not defined relative to any stable benchmark.

## Why Stationarity Changes Everything

If

```math
Z_t=Y_t-\beta X_t
```

is stationary, then the spread has:

- a stable center,
- finite dispersion,
- a meaningful notion of deviation,
- a plausible tendency to revert.

Only then does it make sense to say the spread is unusually wide or unusually tight.

## Intuition

Correlation asks:

```math
\text{Do these series move together?}
```

Cointegration asks:

```math
\text{Are these series tied to a long-run equilibrium?}
```

For trading, the second question is the important one.

## Econometric Form

A common representation is

```math
Y_t=\alpha+\beta X_t+e_t
```

where:

- $X_t$ and $Y_t$ are individually non-stationary,
- $e_t$ is stationary.

Then $e_t$ is the equilibrium error or spread we try to trade.

## Why Buy-Side Researchers Care About Economics

A passing test statistic is not enough. A spread is more credible when the equilibrium has an economic reason to exist:

- same issuer capital structure,
- ETF versus basket,
- cash versus futures,
- related points on the same curve,
- substitutable instruments constrained by arbitrage capital.

Without a real mechanism, the relationship can disappear just when the position is on.

## Common Mistakes

- Equating high correlation with cointegration.
- Forgetting that non-stationary series can look tightly linked in-sample.
- Treating the hedge ratio as static without economic justification.
- Believing statistical significance alone is enough for a live trade.

## Interview Follow-Ups

- Why can regressing one random walk on another create spurious relationships?
- How does Engle-Granger work conceptually?
- What is the error-correction interpretation of cointegration?
- Why might a cointegrated relationship break in production?

## Market / Rates Application

Rates relative value often relies on equilibrium spreads:

- swap spread relationships,
- curve butterflies,
- cash-futures basis,
- on-the-run versus off-the-run relationships.

The point is not raw correlation. The point is whether the residual has a stable economic anchor.

## What to Remember

Correlation is about co-movement.

Cointegration is about equilibrium.

Relative value trading needs the second one, because the tradable object is the stationary residual, not the two raw price series.
