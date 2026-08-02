# O002 — Constrained Mean-Variance Optimization and the Meaning of Lagrange Multipliers

## Metadata

- Category: Optimization
- Secondary: Linear Algebra, Portfolio Theory, Rates Research
- Difficulty: ★★★★☆
- Tags: Mean-Variance Optimization, Lagrange Multipliers, Quadratic Optimization, Dollar Neutrality, Projection, Shadow Price
- Review Priority: High
- Date Added: 2026-07-10
- Status: Draft
- Personal Note: The important idea is that a constraint changes the effective signal, not just the feasible set.

## Core Question

Given

$$
\mu=
\begin{pmatrix}
4\\
2\\
1
\end{pmatrix},
$$

and

$$
\Sigma=
\begin{pmatrix}
4&1&0\\
1&2&1\\
0&1&2
\end{pmatrix},
$$

maximize

$$
\mu^\top w-\frac12 w^\top \Sigma w
$$

subject to

$$
1^\top w=0.
$$

How do we:

1. derive the optimal constrained weights,
2. compare them with the unconstrained solution,
3. interpret the Lagrange multiplier?

## Why This Topic Matters

This is one of the cleanest ways to see what constraints actually do in portfolio construction.

The algebra is easy enough to solve by hand, but the real lesson is conceptual:

- constraints change the portfolio,
- constraints change the effective signal,
- Lagrange multipliers measure the value of relaxing a restriction.

That point comes up repeatedly in long-short equity, rates RV, factor neutralization, and constrained regression.

## My Current Understanding

Without constraints, the optimizer wants the raw mean-variance optimum.

With a neutrality constraint, the optimizer cannot use all directions in weight space. It must discard the component of the signal that points into the forbidden direction.

So the constrained problem is not just "same objective, smaller domain." It is equivalently an optimization on a projected signal.

## Unconstrained Solution

Without the constraint, the first-order condition is

$$
\mu-\Sigma w=0,
$$

so

$$
w_{\text{unc}}=\Sigma^{-1}\mu.
$$

Solving

$$
\Sigma w=\mu
$$

gives

$$
\boxed{
w_{\text{unc}}=
\begin{pmatrix}
0.9\\
0.4\\
0.3
\end{pmatrix}
}
$$

with

$$
1^\top w_{\text{unc}}=1.6\gt 0.
$$

So the unconstrained optimizer naturally wants a net long portfolio.

## Constrained Solution

Introduce the Lagrangian

$$
\mathcal L(w,\lambda)
=
\mu^\top w-\frac12 w^\top\Sigma w-\lambda\,1^\top w.
$$

The first-order condition in `w` is

$$
\mu-\Sigma w-\lambda 1=0,
$$

so

$$
w=\Sigma^{-1}(\mu-\lambda 1).
$$

Imposing

$$
1^\top w=0
$$

gives

$$
\lambda=
\frac{1^\top\Sigma^{-1}\mu}{1^\top\Sigma^{-1}1}.
$$

Here,

$$
\Sigma^{-1}\mu=
\begin{pmatrix}
0.9\\
0.4\\
0.3
\end{pmatrix},
\qquad
\Sigma^{-1}1=
\begin{pmatrix}
0.2\\
0.2\\
0.4
\end{pmatrix},
$$

so

$$
1^\top\Sigma^{-1}\mu=1.6,
\qquad
1^\top\Sigma^{-1}1=0.8,
$$

and therefore

$$
\boxed{\lambda=2.}
$$

Thus

$$
w^*
=
\Sigma^{-1}(\mu-2\,1)
=
\begin{pmatrix}
0.5\\
0\\
-0.5
\end{pmatrix}.
$$

So the constrained optimum is

$$
\boxed{
w^*=
\begin{pmatrix}
0.5\\
0\\
-0.5
\end{pmatrix}
}
$$

which is dollar neutral.

## Interpretation of the Constraint

The constraint

$$
1^\top w=0
$$

forbids net long exposure.

That means the optimizer cannot use the part of the signal that points in the all-ones direction. Instead of optimizing the raw vector

$$
\mu,
$$

it optimizes the adjusted signal

$$
\mu-\lambda 1.
$$

So the constraint effectively subtracts the same amount from every expected return until the neutral portfolio condition is satisfied.

## Interpretation of the Lagrange Multiplier

The multiplier

$$
\lambda
$$

has two linked meanings.

First, it is the shadow value of relaxing the neutrality constraint. It tells us how valuable one more unit of net exposure would be.

Second, it is the uniform shift applied to expected returns in order to remove the forbidden direction. Here

$$
\lambda=2
$$

means the optimizer behaves as if the effective alpha vector were

$$
\mu-2\,1=
\begin{pmatrix}
2\\
0\\
-1
\end{pmatrix}.
$$

## Geometry

Without constraints, the optimizer searches the full space.

With

$$
1^\top w=0,
$$

the feasible set becomes a plane. The constrained solution is the covariance-metric projection of the unconstrained optimum onto that plane.

That is the geometric reason Lagrange multipliers are memorable here: they are not just algebraic helpers, they encode projection onto a feasible subspace.

## Common Mistakes

- Treating the multiplier as only a dummy variable with no economic meaning.
- Thinking the constraint merely changes weights instead of changing the effective signal.
- Forgetting that the projection is with respect to the covariance metric, not ordinary Euclidean distance.
- Solving for `w` correctly but not checking the constraint.

## Interview Follow-Ups

- Replace dollar neutrality with beta neutrality.
- Impose several linear constraints at once.
- Add quadratic transaction costs.
- Add long-only or leverage constraints.
- Interpret the KKT system when inequality constraints bind.

## Market / Rates Application

The same mathematics appears whenever a rates or RV portfolio must be neutral to some unwanted exposure:

- DV01 neutrality,
- duration neutrality,
- beta neutrality,
- curve-factor neutrality.

Only the constraint vector or constraint matrix changes.

## Connections

- Mean-variance optimization
- Quadratic forms
- Linear equality constraints
- Lagrange multipliers and shadow prices
- Projection under a covariance metric
- Factor neutralization

## What to Remember

- Unconstrained optimum:

$$
w_{\text{unc}}=\Sigma^{-1}\mu.
$$

- Constrained optimum:

$$
w^*=\Sigma^{-1}(\mu-\lambda 1),
\qquad
\lambda=\frac{1^\top\Sigma^{-1}\mu}{1^\top\Sigma^{-1}1}.
$$

- In this example:

$$
w_{\text{unc}}=(0.9,0.4,0.3)^\top,
\qquad
\lambda=2,
\qquad
w^*=(0.5,0,-0.5)^\top.
$$

- Constraints change the effective signal being optimized.
