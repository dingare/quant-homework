# S004 — Efficient IV, Rayleigh Quotient, and Covariance-Weighted Signal Combination

## Metadata

- Category: Statistics
- Secondary: Linear Algebra, Statistics, Optimization
- Difficulty: ★★★★★
- Tags: Instrumental Variables, Efficient IV, GMM, Rayleigh Quotient, Covariance Weighting, Signal Combination
- Review Priority: High
- Date Added: 2026-07-12
- Status: Draft
- Personal Note: The real lesson is that efficient IV is another covariance-adjusted signal-combination problem.

## Core Question

Suppose

```math
z=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix}
```

are two correlated instruments, and we want to construct a single instrument

```math
h=a^\top z.
```

How should we choose the weights `a`?

## Why This Topic Matters

This problem is useful because it exposes a common structure that appears in many places:

- efficient IV,
- GMM,
- GLS,
- mean-variance optimization,
- Kalman filtering,
- Mahalanobis distance,
- correlated signal combination.

The principle is always the same:

```math
\text{use covariance to remove redundancy before combining information.}
```

## My Current Understanding

A good instrument should have:

1. high correlation with the endogenous regressor,
2. low variance.

So the relevant objective is not "large raw covariance" alone. It is predictive power after penalizing redundancy.

## Objective

Let

```math
h=a^\top z.
```

Define

```math
q=E[zx],
\qquad
Q=E[zz^\top].
```

Then

```math
\operatorname{Cov}(h,x)=a^\top q,
\qquad
\operatorname{Var}(h)=a^\top Q a.
```

So the problem becomes

```math
\boxed{
\max_a \frac{(a^\top q)^2}{a^\top Q a}
}
```

which is a generalized Rayleigh quotient.

## Solution

Because scaling does not matter, impose

```math
a^\top Q a=1.
```

Then maximize

```math
a^\top q
```

subject to that normalization.

The Lagrangian is

```math
L=a^\top q-\lambda(a^\top Q a-1).
```

The first-order condition is

```math
q=2\lambda Q a.
```

Hence

```math
\boxed{
a=c\,Q^{-1}q
}
```

for an irrelevant scaling constant `c`.

So the direction of the optimal instrument is

```math
Q^{-1}q.
```

## Main Intuition

If the instruments are independent, then

```math
Q=I,
```

so

```math
a\propto q.
```

Weights are just proportional to predictive covariance.

But if the instruments are highly correlated, then `Q` has large off-diagonal terms. Inverting `Q` removes duplicate information.

So

```math
Q^{-1}
```

does not reward correlation by itself. It rewards incremental predictive power after removing redundancy.

## Why This Is a Rayleigh Quotient Problem

The expression

```math
\frac{(a^\top q)^2}{a^\top Qa}
```

is the same kind of structure that appears in many optimization problems:

- PCA maximizes variance in one direction,
- mean-variance optimization maximizes return relative to covariance risk,
- efficient IV maximizes predictive content relative to covariance redundancy.

The geometry is different in each application, but the mathematical skeleton is the same.

## Connection to GMM and GLS

Efficient IV is closely related to efficient GMM.

In both cases, inverse covariance weighting appears because correlated moments should not be double counted.

That is also why GLS uses inverse error covariance and why Mahalanobis distance rescales directions by covariance rather than Euclidean length.

## Connection to Kalman Filtering

Kalman filtering also combines correlated information using covariance weighting.

The gain matrix effectively says: take the observation surprise, then downweight components that are noisy or redundant.

So efficient IV and Kalman filtering look very different on the surface, but they share the same mathematical principle.

## Common Mistakes

- Thinking the best instrument is the one with the largest raw covariance alone.
- Ignoring correlation across instruments.
- Treating `Q^{-1}` as a technical trick instead of a redundancy-removal operator.
- Missing that only the direction of `a` matters.

## Interview Follow-Ups

- How does this connect to efficient GMM weighting?
- Why is the objective scale invariant?
- What happens if the instruments are nearly collinear?
- How does this relate to GLS?
- How does the Rayleigh quotient connect to PCA or mean-variance optimization?

## Market / Rates Application

In practice, quants often combine multiple correlated signals that all try to forecast the same latent object:

- carry, roll, and value signals,
- multiple curve dislocations,
- related macro instruments,
- basis signals across nearby maturities.

The correct combination is not equal weighting and not raw-correlation weighting. It is covariance-adjusted weighting.

## Connections

- Efficient IV
- GMM weighting
- Generalized Rayleigh quotient
- GLS and Mahalanobis geometry
- Mean-variance optimization
- Kalman gain and covariance weighting

## What to Remember

- Objective:

```math
\max_a \frac{(a^\top q)^2}{a^\top Q a}
```

- Solution direction:

```math
a\propto Q^{-1}q
```

- Interpretation:

```math
Q^{-1}
```

removes redundancy, so the optimal instrument loads on incremental predictive content rather than duplicated correlation.
