# P002 — Optional Stopping, Fair Games, and Why Stop-Loss Does Not Create Alpha

## Metadata

- Category: Probability
- Secondary: Stochastic Processes, Trading Intuition, Risk Management
- Difficulty: ★★★★☆
- Tags: Martingale, Optional Stopping, Hitting Probability, Stop-Loss, Fair Game
- Review Priority: High
- Date Added: 2026-07-05
- Status: Draft
- Personal Note: Emphasize that stopping rules reshape the payoff distribution but do not create edge when the underlying process is a martingale.

## Core Question

Suppose $X_t$ is a martingale with $X_0=0$, and define the stopping time

$$
\tau=\inf\{t: X_t\in\{a,-b\}\}
$$

for $a,b\gt 0$.

Show that

$$
P(X_\tau=a)=\frac{b}{a+b}
$$

and explain why changing stopping rules cannot generate alpha in a fair game.

## Why This Topic Matters

This is one of the cleanest ways to separate:

- alpha generation,
- risk management,
- path management.

Many trading rules look appealing because they improve win rate or truncate losses. Optional stopping clarifies that if the underlying process has zero edge, changing the exit rule alone does not manufacture positive expectancy.

## My Current Understanding

A martingale is a fair game in conditional expectation:

$$
E[X_t\mid\mathcal F_s]=X_s.
$$

So the stopping rule can change:

- how often I win,
- how large wins are,
- how large losses are,
- how long the trade lasts,

but not the expected value, provided the stopping argument is valid.

## Hitting Probability Calculation

At the stopping time, the process ends at either $a$ or $-b$, so

$$
X_\tau\in\{a,-b\}.
$$

Let

$$
p=P(X_\tau=a).
$$

Then

$$
P(X_\tau=-b)=1-p.
$$

If optional stopping applies, then

$$
E[X_\tau]=E[X_0]=0.
$$

Therefore

$$
ap+(-b)(1-p)=0.
$$

Solve:

$$
ap-b+bp=0
\quad\Longrightarrow\quad
p(a+b)=b
\quad\Longrightarrow\quad
\boxed{P(X_\tau=a)=\frac{b}{a+b}}.
$$

Similarly,

$$
\boxed{P(X_\tau=-b)=\frac{a}{a+b}}.
$$

## Intuition

The winning probability is higher when the loss barrier is farther away.

That sounds favorable, but the gain size and loss size adjust against each other. A closer profit target raises hit rate only because the upside is smaller. The expectation stays pinned at zero.

## Why Stop-Loss Does Not Create Alpha

Suppose a strategy exits at:

- a small gain very often,
- a large loss occasionally.

This can create an impressive win rate without creating positive expected value. What matters is:

$$
E[\text{PnL}]
=
\sum \text{probability}\times \text{payoff}.
$$

Optional stopping says that in a fair game, exit engineering alone changes the shape of outcomes, not the mean.

## Common Mistakes

- Confusing high win rate with positive expectancy.
- Thinking smaller losses automatically imply positive edge.
- Forgetting that optional stopping needs conditions; it is not a free pass for every unbounded stopping rule.
- Mistaking risk control for signal generation.

## Interview Follow-Ups

- What conditions are needed for the Optional Stopping Theorem?
- How does the conclusion change if the process has drift?
- How do stop-loss and take-profit rules affect skewness and drawdowns even if they do not create alpha?
- Why can a backtest look better after changing exits without the underlying signal improving?

## Market / Rates Application

In practice, stop-loss rules still matter. They can improve:

- tail control,
- capital usage,
- liquidity management,
- drawdown behavior.

But those are risk-management benefits, not proof of alpha. This distinction matters a lot in discretionary macro and systematic rates trading.

## What to Remember

Stopping Rule $\neq$ Alpha.

If the underlying process is a martingale, clever exits can change distribution, hit rate, and path behavior, but not expected profit.
