# O003 — Primal vs Dual Optimization and When the Dual Is Easier

## Metadata

- Category: Optimization
- Secondary: Linear Algebra, Convex Analysis, Portfolio Construction
- Difficulty: ★★★★☆
- Tags: Primal Optimization, Dual Optimization, Lagrangian, KKT Conditions, Strong Duality, Shadow Price, Constrained Least Squares
- Review Priority: High
- Date Added: 2026-07-13
- Status: Finalized
- Personal Note: The key interview edge is to distinguish "eliminate $x$" from the formal dual problem and then talk about dimensions, structure, and sensitivity.

## Core Question

What is the difference between a primal and dual optimization problem, when is the dual easier to solve, and what do Lagrange multipliers mean in practice?

## Why This Topic Matters

This comes up constantly in quantitative finance because many portfolio and regression problems are constrained.

Interviewers often use this topic to test whether I can:

- write a Lagrangian cleanly,
- eliminate primal variables correctly,
- recognize when the dual dimension is much smaller,
- explain why we solve linear systems rather than form explicit inverses,
- interpret multipliers economically.

## My Current Understanding

The primal problem is the original optimization over the decision variables.

The dual problem is built from the Lagrangian by minimizing over the primal variable first and then maximizing the resulting dual function over the multipliers.

In many quadratic finance problems, the algebra lets us solve for $x$ as a function of $\lambda$, so the dual reduces the problem to constraint space.

That is especially attractive when the number of constraints is far smaller than the number of variables.

## Primal Setup

Consider the equality-constrained problem

$$
\min_x \frac12\|x-a\|^2
\quad\text{subject to}\quad
Bx=c,
$$

with

$$
x\in\mathbb R^n,
\qquad
B\in\mathbb R^{m\times n},
\qquad
c\in\mathbb R^m.
$$

Here:

- $x$ is the primal variable,
- $n$ is the number of decision variables,
- $m$ is the number of equality constraints.

In finance, the primal variables could be:

- portfolio weights,
- asset holdings,
- factor exposures,
- regression coefficients.

## Lagrangian and Dual Variables

Introduce one multiplier for each equality constraint:

$$
\lambda\in\mathbb R^m.
$$

Using the convention

$$
\mathcal L(x,\lambda)=
\frac12(x-a)^\top(x-a)+\lambda^\top(Bx-c),
$$

the first-order condition in $x$ is

$$
\nabla_x \mathcal L=
x-a+B^\top\lambda=
0.
$$

So

$$
x(\lambda)=a-B^\top\lambda.
$$

## The Formal Dual Problem

The dual function is

$$
g(\lambda)=\inf_x \mathcal L(x,\lambda).
$$

The dual problem is therefore

$$
\max_\lambda g(\lambda).
$$

This matters in interviews because the dual is not merely "substitute $x(\lambda)$ back somewhere." Formally, we minimize the Lagrangian over $x$ first and then maximize over $\lambda$.

For this quadratic problem, substituting $x(\lambda)$ back into the constraint gives

$$
B(a-B^\top\lambda)=c,
$$

so

$$
BB^\top\lambda=Ba-c.
$$

If $B$ has full row rank, then $BB^\top$ is invertible and

$$
\lambda=(BB^\top)^{-1}(Ba-c).
$$

Then

$$
x^*=a-B^\top\lambda.
$$

If $B$ does not have full row rank, we should not write an inverse blindly. We instead solve the linear system in a least-norm or pseudoinverse sense.

## Dimension Comparison

The dimensions are:

| Quantity | Dimension |
| --- | --- |
| Primal variable | $x\in\mathbb R^n$ |
| Dual variable | $\lambda\in\mathbb R^m$ |
| Constraint matrix | $B\in\mathbb R^{m\times n}$ |

The practical question is:

> Which dimension is smaller and better structured?

If $m\ll n$, the dual can be dramatically cheaper because it works in constraint space rather than variable space.

## When the Dual Is Easier

The dual is often attractive when:

- there are very few constraints relative to variables,
- the primal variables can be eliminated analytically,
- the reduced system in $\lambda$ has favorable structure,
- the multipliers themselves are economically meaningful.

Example:

- $n=10^7$ variables,
- $m=10$ constraints.

Then the primal lives in a 10 million dimensional space, while the dual only has 10 unknown multipliers.

This is common in:

- constrained portfolio optimization,
- factor neutrality,
- constrained least squares,
- projection problems.

If instead $m\approx n$ or $m\gt n$, the dual may not be smaller and we often solve the primal directly or use iterative methods.

## KKT and Convexity

For interview purposes, it is good to mention the Karush-Kuhn-Tucker conditions rather than only derivatives.

For equality-constrained convex problems, the key conditions are:

- primal feasibility,
- stationarity,
- and, under standard conditions, strong duality.

For inequality constraints such as

$$
h(x)\le 0,
$$

the multipliers also satisfy

$$
\lambda\ge 0,
$$

and complementary slackness enters the picture.

That is why duality is especially clean and powerful in convex optimization.

## Weak vs Strong Duality

Weak duality always says:

> the dual objective provides a lower bound on the primal objective for a minimization problem.

Strong duality says:

> under suitable regularity conditions, the primal optimum equals the dual optimum.

In convex finance problems, strong duality is often what justifies solving the dual instead of the primal.

## Shadow Price Interpretation

The multiplier also gives sensitivity information.

Suppose the constraint right-hand side changes from

$$
c
\to
c+\Delta c.
$$

Then the optimal objective changes at first order according to the multiplier.

With the convention

$$
\mathcal L(x,\lambda)=f(x)+\lambda^\top(Bx-c),
$$

the sensitivity of the optimal value with respect to $c$ is

$$
-\lambda^*.
$$

So the sign depends on the Lagrangian convention. That is an easy place to lose points if I state the shadow-price rule too casually.

Economically, the multiplier measures how valuable it would be to relax or tighten a constraint marginally.

## Why We Do Not Compute Explicit Inverses

Interviewers usually want to hear this point clearly.

If $n=10^7$, then a dense $n\times n$ matrix has

$$
10^{14}
$$

entries, which is computationally absurd to store and invert directly.

Even when the inverse exists mathematically, numerical work almost never forms it explicitly.

Instead we solve systems such as

$$
Qx=b
$$

using factorization or iterative methods.

## Large-Scale Numerical Methods

Useful methods to mention:

- Cholesky factorization for symmetric positive definite systems,
- Conjugate Gradient for large SPD problems,
- sparse direct solvers for structured sparse systems,
- projected gradient methods for simple constraints,
- interior-point methods for general constrained convex programs,
- ADMM when the problem splits naturally.

The interview answer should always connect the formulation to structure:

- dense vs sparse,
- few constraints vs many constraints,
- direct solve vs iterative solve.

## Common Mistakes

- Saying the dual is always smaller.
- Writing $(BB^\top)^{-1}$ without checking rank conditions.
- Claiming the dual variable is always the derivative with the same sign regardless of convention.
- Talking only about algebra and never mentioning KKT, weak duality, or strong duality.
- Saying "compute the inverse" instead of "solve the linear system."

## Interview Follow-Ups

Good follow-up points to volunteer:

- If $m\ll n$, solve in dual space when possible.
- If $n\ll m$, primal space may be preferable.
- In convex problems, KKT conditions often characterize the optimum.
- Dual variables are useful both computationally and economically.
- Numerical linear algebra is about solves, sparsity, and structure, not symbolic inversion.

## Market / Rates Application

This shows up directly in:

- factor-neutral portfolio construction,
- duration- or DV01-neutral hedging,
- regression with linear restrictions,
- cheapest hedge construction under balance-sheet constraints,
- constrained relative-value optimization.

In rates, the dual variables can often be interpreted as the marginal value of relaxing neutrality, funding, or risk-budget constraints.

## Connections

- [O001 — Convex Duality I: No-Arbitrage Pricing through Primal and Dual Optimization](O001_Convex_Duality_I_No_Arbitrage_Pricing_through_Primal_and_Dual_Optimization.md)
- [O002 — Constrained Mean-Variance Optimization and the Meaning of Lagrange Multipliers](O002_Constrained_Mean_Variance_Optimization_and_the_Meaning_of_Lagrange_Multipliers.md)
- [S004 — Efficient IV, Rayleigh Quotient, and Covariance-Weighted Signal Combination](../Statistics/S004_Efficient_IV_Rayleigh_Quotient_and_Covariance_Weighted_Signal_Combination.md)
- [L001 — Ridge Regression as PCA Shrinkage](../LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md)

## What to Remember

- Primal means optimize over the original variables.
- Dual means optimize over the constraint multipliers after minimizing the Lagrangian over the primal variable.
- The dual is often easier when the number of constraints is much smaller than the number of variables.
- KKT conditions and strong duality are the right theoretical language for interviews.
- Never form large explicit inverses when a solve or iterative method will do.
- Lagrange multipliers are shadow prices, but the sign depends on the Lagrangian convention.
