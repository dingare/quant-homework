# P004 — Two-Out-of-Three Gaussian Signal Triggers and Correlation

## Metadata

- Category: Probability
- Secondary: Statistics, Gaussian Models, Trading Signals
- Difficulty: ★★★★★
- Tags: Gaussian Signals, Binomial Counting, Threshold Calibration, Conditional Expectation, Equicorrelation
- Review Priority: High
- Date Added: 2026-07-15
- Status: Finalized
- Personal Note: The useful trick is to condition on the common Gaussian factor so the correlated problem becomes binomial again.

## Core Question

A market maker observes three independent signals:

$$
X_1,X_2,X_3 \sim N(0,1).
$$

A trade is triggered when at least two signals exceed the same threshold $a$. The desk chooses $a$ so that the unconditional trade probability is exactly $5\%$:

$$
\mathbb P\!\left(\left|\{i:X_i\gt a\}\right|\ge 2\right)=0.05.
$$

1. Find $p=\mathbb P(X_i\gt a)$, and approximate $a$.
2. Conditional on a trade occurring, compute the probability that all three signals exceed $a$.
3. Let

$$
M=\max(X_1,X_2,X_3).
$$

Write an exact one-dimensional integral for

$$
\mathbb E[M\mid \left|\{i:X_i\gt a\}\right|\ge 2].
$$

4. The signals are now equicorrelated:

$$
\mathrm{Corr}(X_i,X_j)=\rho,\qquad i\neq j,
$$

with $0\lt \rho\lt 1$. Give a one-dimensional integral representation for the trade probability.

## Hint

For the independent case, if

$$
N=\left|\{i:X_i\gt a\}\right|,
$$

then

$$
N\sim\mathrm{Binomial}(3,p).
$$

For the correlated case, use the common-factor representation

$$
X_i=\sqrt{\rho}\,Z+\sqrt{1-\rho}\,\varepsilon_i,
$$

where $Z,\varepsilon_1,\varepsilon_2,\varepsilon_3$ are independent standard normals.

## Solution

### 1. Calibrating the Threshold

With

$$
N\sim\mathrm{Binomial}(3,p),
$$

we have

$$
\mathbb P(N\ge2)
=
3p^2(1-p)+p^3.
$$

Therefore

$$
3p^2-2p^3=0.05.
$$

Solving

$$
2p^3-3p^2+0.05=0
$$

for the root in $(0,1)$ gives approximately

$$
\boxed{p\approx0.13535}.
$$

Hence

$$
a=\Phi^{-1}(1-p),
$$

so

$$
\boxed{a\approx1.10}.
$$

### 2. Probability That All Three Exceed

We need

$$
\mathbb P(N=3\mid N\ge2)
=
\frac{p^3}{3p^2(1-p)+p^3}.
$$

Since the denominator is $0.05$,

$$
\mathbb P(N=3\mid N\ge2)
=
\frac{p^3}{0.05}.
$$

Using $p\approx0.13535$,

$$
p^3\approx0.00248.
$$

Thus

$$
\boxed{
\mathbb P(N=3\mid N\ge2)\approx0.0496
}.
$$

Only about $5\%$ of triggered trades have all three signals above threshold.

### 3. Conditional Expected Maximum

Let

$$
A=\{N\ge2\}.
$$

On $A$, at least two variables exceed $a$, so necessarily

$$
M\gt a.
$$

Therefore

$$
\mathbb E[M\mid A]
=
a+\int_a^\infty \mathbb P(M\gt t\mid A)\,dt.
$$

For $t\ge a$, define

$$
q(t)=\Phi(t)-\Phi(a).
$$

Then

$$
\mathbb P(M\le t,A)
=
3q(t)^2\Phi(a)+q(t)^3.
$$

Hence

$$
\mathbb P(M\gt t\mid A)
=
1-
\frac{
3[\Phi(t)-\Phi(a)]^2\Phi(a)
+
[\Phi(t)-\Phi(a)]^3
}{0.05}.
$$

Thus an exact one-dimensional integral is

$$
\boxed{
\mathbb E[M\mid A]
=
a+
\int_a^\infty
\left[
1-
\frac{
3[\Phi(t)-\Phi(a)]^2\Phi(a)
+
[\Phi(t)-\Phi(a)]^3
}{0.05}
\right]dt
}.
$$

### 4. Equicorrelated Signals

Write

$$
X_i=\sqrt{\rho}\,Z+\sqrt{1-\rho}\,\varepsilon_i.
$$

Conditional on $Z=z$, the $X_i$ are independent and

$$
\mathbb P(X_i\gt a\mid Z=z)
=
\bar\Phi\left(
\frac{a-\sqrt{\rho}\,z}{\sqrt{1-\rho}}
\right).
$$

Define

$$
p(z)
=
\bar\Phi\left(
\frac{a-\sqrt{\rho}\,z}{\sqrt{1-\rho}}
\right).
$$

Then

$$
N\mid Z=z\sim\mathrm{Binomial}(3,p(z)),
$$

so

$$
\mathbb P(N\ge2\mid Z=z)
=
3p(z)^2[1-p(z)]+p(z)^3.
$$

Integrating over $Z$,

$$
\boxed{
\mathbb P(N\ge2)
=
\int_{-\infty}^{\infty}
\left[
3p(z)^2(1-p(z))+p(z)^3
\right]\phi(z)\,dz
}.
$$

## Key Knowledge Points

- A two-out-of-three trigger under independence reduces to a binomial exceedance count.
- Correlated Gaussian threshold problems often become tractable by conditioning on a common factor.
- Conditional expectations can often be written as one-dimensional tail integrals even when closed forms are messy.

## Intuition

The trigger is a nonlinear aggregation rule.

Even though each individual signal crosses only about $13.5\%$ of the time, requiring two out of three reduces the overall trade frequency to $5\%$.

Positive correlation changes the clustering of exceedances:

- it increases the probability of many signals crossing together,
- it also increases the probability that none cross,
- it changes the calibration needed to keep trade frequency fixed.

## Geometry

The independence case is a counting problem in exceedance space.

The correlated case becomes a one-factor mixture: conditional on the common factor $Z$, the problem reduces back to a binomial count.

That is the geometric simplification behind the one-dimensional integral.

## Common Mistakes

- Treating the independent and correlated cases as if they had the same threshold calibration.
- Forgetting that conditional on the common factor, the signals become independent.
- Assuming a closed-form answer is required when an exact one-dimensional integral is already the right endpoint.
- Ignoring that a trigger based on multiple signals can hide correlation concentration.

## Interview Follow-Ups

- As $\rho\to1$, what does the trade probability converge to?
- For fixed $a$, is the trade probability monotone in $\rho$?
- Derive

$$
\mathbb P(N=3\mid N\ge2)
$$

under equicorrelation as a ratio of one-dimensional integrals.
- Generalize the trigger to at least $k$ exceedances among $n$ signals.
- Approximate the threshold $a$ when $n$ is large and the trigger requires at least $k$ exceedances.

## Market / Rates Application

A rates desk may combine signals such as:

- curve dislocation,
- order-flow imbalance,
- futures-cash basis,
- relative-value residuals.

A two-out-of-three trigger reduces reliance on a single noisy feature.

But correlated signals can create hidden concentration: several apparently distinct indicators may fire simultaneously because they share the same underlying duration, liquidity, or macro factor.

## Connections

- [P001 — Fixed vs Exists Probability Patterns](P001_Fixed_vs_Exists_Probability_Patterns.md)
- [S004 — Efficient IV, Rayleigh Quotient, and Covariance-Weighted Signal Combination](../Statistics/S004_Efficient_IV_Rayleigh_Quotient_and_Covariance_Weighted_Signal_Combination.md)
- [T004 — Kalman Filtering II: Covariance-Weighted Bayesian Updating](../TimeSeries/T004_Kalman_Filtering_II_Covariance_Weighted_Bayesian_Updating.md)

## What to Remember

- Independence gives a binomial exceedance count.
- Correlation can be handled by conditioning on a common Gaussian factor.
- Multi-signal trigger rules are really joint-tail probability problems.
- In practice, correlation matters as much as marginal thresholding.
