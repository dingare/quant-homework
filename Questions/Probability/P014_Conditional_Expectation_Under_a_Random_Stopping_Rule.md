# P014 — Conditional Expectation Under a Random Stopping Rule

## Metadata

- Category: Probability
- Secondary: Martingales, Stopping Times, Conditional Expectation
- Difficulty: ★★★☆☆
- Tags: Predictable Processes, Martingale Transform, Optional Stopping, Random Walk
- Review Priority: High
- Date Added: 2026-08-26
- Status: Final

## Core Question

Let $X_1,X_2,\ldots$ be iid with

$$
P(X_i=1)=P(X_i=-1)=\frac12,
\qquad
S_n=\sum_{i=1}^n X_i.
$$

Stop at

$$
\tau=\inf\{n\ge0:S_n\in\{-1,2\}\}.
$$

Define

$$
Y=\sum_{i=1}^{\tau}iX_i.
$$

Find the probability of hitting $+2$ first, $E[\tau]$, and $E[Y]$. Generalize the last result to $Y_f=\sum_{i=1}^{\tau}f(i)X_i$ for deterministic $f$ under suitable integrability.

## Hint

Rewrite

$$
Y=\sum_{i\ge1}iX_i\mathbf1_{\{\tau\ge i\}}.
$$

The event $\{\tau\ge i\}$ is known before observing $X_i$.

## Solution

### Hitting Probability

Let $h=P(S_\tau=2)$. Since $S_n$ is a martingale and the stopped walk is bounded,

$$
0=E[S_\tau]=2h-1(1-h).
$$

Therefore

$$
\boxed{h=\frac13}.
$$

This also follows from the fair gambler's-ruin formula: the start is one step above the lower barrier in an interval of width three.

### Expected Stopping Time

For a symmetric random walk,

$$
S_n^2-n
$$

is a martingale. Optional stopping gives

$$
E[\tau]=E[S_\tau^2].
$$

Using the terminal probabilities,

$$
E[S_\tau^2]
=4\left(\frac13\right)
+1\left(\frac23\right)
=2.
$$

Hence

$$
\boxed{E[\tau]=2}.
$$

### Expected Weighted Sum

Write

$$
Y=\sum_{i\ge1}iX_i\mathbf1_{\{\tau\ge i\}}.
$$

Crucially, $\mathbf1_{\{\tau\ge i\}}$ is measurable with respect to $\mathcal F_{i-1}$: immediately before step $i$, we know whether the walk has already stopped. Therefore

$$
\begin{aligned}
E\left[iX_i\mathbf1_{\{\tau\ge i\}}\right]
&=E\left[
i\mathbf1_{\{\tau\ge i\}}
E[X_i\mid\mathcal F_{i-1}]
\right]\\
&=0.
\end{aligned}
$$

Summing under the required integrability condition gives

$$
\boxed{E[Y]=0}.
$$

This is a martingale-transform argument: the weight $i\mathbf1_{\{\tau\ge i\}}$ is predictable.

### Generalization

For any deterministic function $f$ such that the stopped sum is integrable and expectation may be interchanged with summation,

$$
Y_f=\sum_{i=1}^{\tau}f(i)X_i
=\sum_{i\ge1}f(i)X_i\mathbf1_{\{\tau\ge i\}}.
$$

The same predictable-weight calculation yields

$$
\boxed{E[Y_f]=0}.
$$

A sufficient condition is

$$
E\left[\sum_{i=1}^{\tau}|f(i)|\right]\lt\infty.
$$

## Why Substituting $E[\tau]$ Is Invalid

It is generally wrong to replace the random upper limit by its mean and write

$$
E\left[\sum_{i=1}^{\tau}iX_i\right]
\stackrel{\text{wrong}}{=}
E\left[\sum_{i=1}^{E[\tau]}iX_i\right].
$$

Here $E[\tau]=2$, but $\tau$ is not identically $2$, and it depends on the realized increments. Nonlinear functions and randomly stopped sums are not determined by the mean stopping time. The answer is zero because the inclusion decision for $X_i$ is predictable, not because $\tau$ can be replaced by $2$.

## Intuition

Stopping decides whether the next fair increment will be included before that increment is observed. It may select how many bets are placed, but it cannot create a positive expected gain from the next unseen fair bet. Predictability is the key distinction between a valid stopping rule and a rule that looks into the future.

## Interview Takeaways

- Use $S_n$ for hitting probabilities and $S_n^2-n$ for expected duration in a fair walk.
- Expand a stopped sum with survival indicators $\mathbf1_{\{\tau\ge i\}}$.
- Check that each multiplier is measurable before the increment it multiplies.
- State an integrability condition before exchanging an infinite sum and expectation.

## Finance / Market Application

A trading strategy may choose whether to hold a position at time $i$ using information available at time $i-1$. Multiplying a martingale return by such a predictable exposure still has zero expected gain, provided the strategy is integrable. Adaptive timing alone does not manufacture alpha.

## What to Remember

$$
\boxed{
P(S_\tau=2)=\frac13,
\qquad
E[\tau]=2,
\qquad
E[Y]=0
}.
$$
