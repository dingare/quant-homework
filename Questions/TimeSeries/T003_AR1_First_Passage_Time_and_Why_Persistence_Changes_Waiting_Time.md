# T003 — AR(1) First Passage Time and Why Persistence Changes Waiting Time

## Metadata

- Category: Time Series
- Secondary: Probability, Stochastic Processes, Trading Intuition
- Difficulty: ★★★★☆
- Tags: AR(1), First Passage Time, Hitting Time, Stationary Variance, Persistence, Threshold Crossing
- Review Priority: High
- Date Added: 2026-07-10
- Status: Draft
- Personal Note: The key shift is from predicting the next value to understanding the waiting time for an event.

## Core Question

Consider the AR(1) process

$$
X_{t+1}=0.8X_t+\epsilon_{t+1},
\qquad
\epsilon_t\sim N(0,1),
$$

with

$$
X_0=0.
$$

Define the first hitting time

$$
\tau=\inf\{t:X_t\gt 2\}.
$$

How should we think about:

1. the stationary variance,
2. the approximate probability of exceeding the barrier,
3. the approximate expected hitting time,
4. why the approximation is not exact?

## Why This Topic Matters

Most time-series questions ask for the next observation. This one asks when an event happens.

That distinction matters in practice because many trading problems are naturally first-passage problems:

- stop losses,
- take profits,
- signal entry and exit,
- margin calls,
- liquidation events.

## My Current Understanding

The object of interest is not just

$$
X_t,
$$

but the waiting time

$$
\tau.
$$

That makes this a threshold-crossing problem rather than a standard forecasting problem.

## Stationary Scale

For an AR(1) process

$$
X_{t+1}=\phi X_t+\epsilon_{t+1},
\qquad
\epsilon_t\sim N(0,\sigma^2),
$$

the stationary variance is

$$
\mathrm{Var}(X)=\frac{\sigma^2}{1-\phi^2}.
$$

Here

$$
\phi=0.8,
\qquad
\sigma^2=1,
$$

so

$$
\mathrm{Var}(X)=\frac{1}{1-0.8^2}=\frac{1}{0.36}\approx 2.78.
$$

Hence the stationary standard deviation is

$$
\sqrt{2.78}\approx 1.67.
$$

So the barrier `2` is about `1.2` stationary standard deviations above the mean.

## Approximate Hitting Probability and Waiting Time

Under stationarity,

$$
X_t\sim N(0,2.78),
$$

so

$$
P(X_t\gt 2)\approx P(Z\gt 1.2)\approx 0.115.
$$

A simple approximation is then

$$
E[\tau]\approx \frac{1}{P(X_t\gt 2)}\approx \frac{1}{0.115}\approx 8.7.
$$

This is a geometric-style approximation: if the event happens about 11.5% of the time, then the average waiting time is about 8.7 periods.

## Why The Approximation Is Imperfect

The approximation is useful but not exact for two reasons.

First, the AR(1) process is not independent across time. If

$$
X_t
$$

is already large, then

$$
X_{t+1}
$$

is more likely to remain large. Crossings cluster, so the process does not behave like repeated independent trials.

Second, the approximation assumes stationarity, but the process starts from

$$
X_0=0.
$$

Early on, the variance is smaller than the stationary variance, so the true expected waiting time is generally longer than the stationary geometric estimate.

## Intuition

Two forces matter:

1. how far the threshold is from the mean,
2. how persistent shocks are.

Persistence changes waiting time because it creates runs. Once the process starts moving toward the barrier, memory makes further movement in that direction more likely than under independence.

## Common Mistakes

- Treating first passage as the same problem as one-step prediction.
- Using the stationary exceedance probability as if observations were independent.
- Forgetting that the initial condition matters when the process has not yet mixed.
- Thinking persistence only changes variance, not waiting-time behavior.

## Interview Follow-Ups

- What changes if

$$
\phi=0.95
$$

instead of `0.8`?
- How does the waiting time change if the barrier is `3` instead of `2`?
- How would you estimate

$$
E[\tau]
$$

more accurately than the geometric approximation?
- How does this relate to stop-loss or take-profit timing in trading?

## Market / Rates Application

This matters whenever the timing of a trigger is more important than the next-step forecast. In trading, risk, and execution, many decisions depend on when a spread, signal, or PnL process first reaches a threshold rather than on its unconditional long-run distribution.

## Connections

- AR(1) persistence
- First-passage / hitting-time problems
- Geometric waiting-time approximation
- Stationary distribution versus transient behavior
- Threshold-based trading logic

## What to Remember

- First passage is a waiting-time problem, not just a forecasting problem.
- For AR(1),

$$
\mathrm{Var}(X)=\frac{\sigma^2}{1-\phi^2}.
$$

- A quick approximation is

$$
E[\tau]\approx \frac{1}{P(X\gt a)}.
$$

- That approximation is imperfect because AR(1) observations are dependent and the process may start away from stationarity.
