# L003 — Woodbury Identity for Low-Rank Covariance Inversion

## Metadata

- Category: Linear Algebra
- Secondary: Optimization, Statistics, Numerical Linear Algebra
- Difficulty: ★★★★☆
- Tags: Woodbury Identity, Low-Rank Update, Matrix Inversion Lemma, Factor Models, Covariance Inversion
- Review Priority: High
- Date Added: 2026-07-15
- Status: Finalized
- Personal Note: The key idea is to invert a small factor-space matrix rather than the full covariance matrix.

## Core Question

Let

$$
\Sigma = D + UU^\top,
$$

where

$$
D=\mathrm{diag}(1,2,3,4),
\qquad
U=
\begin{pmatrix}
1&0\\
1&1\\
0&1\\
1&-1
\end{pmatrix}.
$$

A portfolio optimizer needs to repeatedly compute

$$
x=\Sigma^{-1}b
$$

for many vectors $b$, but should not explicitly invert the full $4\times 4$ matrix.

For

$$
b=
\begin{pmatrix}
1\\2\\0\\1
\end{pmatrix},
$$

compute $x$ using the Woodbury identity.

Then answer:

1. What matrix must actually be inverted?
2. How does the computational advantage scale when $D\in\mathbb R^{n\times n}$ is diagonal and $U\in\mathbb R^{n\times k}$, with $k\ll n$?
3. Under what conditions is $\Sigma$ positive definite?

## Hint

Use

$$
(D+UU^\top)^{-1}
=
D^{-1}
-
D^{-1}U
\left(I+U^\top D^{-1}U\right)^{-1}
U^\top D^{-1}.
$$

First calculate

$$
y=D^{-1}b,
\qquad
V=D^{-1}U.
$$

You only need to solve a $2\times 2$ system.

## Solution

We have

$$
D^{-1}
=
\mathrm{diag}
\left(1,\frac12,\frac13,\frac14\right).
$$

Therefore

$$
y=D^{-1}b
=
\begin{pmatrix}
1\\1\\0\\1/4
\end{pmatrix}.
$$

Also,

$$
V=D^{-1}U
=
\begin{pmatrix}
1&0\\
1/2&1/2\\
0&1/3\\
1/4&-1/4
\end{pmatrix}.
$$

Now compute the small matrix

$$
M=I+U^\top D^{-1}U
=I+U^\top V.
$$

Its entries are

$$
U^\top V
=
\begin{pmatrix}
7/4&1/4\\
1/4&13/12
\end{pmatrix},
$$

so

$$
M=
\begin{pmatrix}
11/4&1/4\\
1/4&25/12
\end{pmatrix}.
$$

Next,

$$
U^\top y
=
\begin{pmatrix}
9/4\\
3/4
\end{pmatrix}.
$$

Solve

$$
Mz=U^\top y.
$$

That is,

$$
\begin{pmatrix}
11/4&1/4\\
1/4&25/12
\end{pmatrix}
z
=
\begin{pmatrix}
9/4\\
3/4
\end{pmatrix}.
$$

The solution is

$$
z=
\begin{pmatrix}
27/34\\
9/34
\end{pmatrix}.
$$

Woodbury gives

$$
x=y-Vz.
$$

Now

$$
Vz=
\begin{pmatrix}
27/34\\
18/34\\
3/34\\
9/68
\end{pmatrix},
$$

and therefore

$$
\boxed{
x=
\begin{pmatrix}
7/34\\
8/17\\
-3/34\\
2/17
\end{pmatrix}
}.
$$

## Key Knowledge Points

- Woodbury replaces inversion of a large matrix by inversion of a low-dimensional correction.
- When the covariance has diagonal plus low-rank structure, the expensive work happens in factor space.
- Repeated solves become cheap once the reduced matrix is built and factorized.

## Intuition

The matrix $D$ is the easy part because it is diagonal.

The term $UU^\top$ is a low-rank adjustment, so it only changes the inverse inside a small subspace.

Woodbury says:

> Start from the easy diagonal inverse and correct it only within the low-dimensional factor subspace.

That is why the hard part depends on the number of factors $k$, not directly on the ambient dimension $n$.

## Geometry

The update $UU^\top$ only acts along the column space of $U$.

Outside that subspace, the matrix still behaves like $D$.

So Woodbury is a geometric decomposition into:

- a simple diagonal background metric,
- plus a correction inside a low-dimensional factor subspace.

## Common Mistakes

- Explicitly inverting the full $n\times n$ matrix when only a $k\times k$ inverse is needed.
- Forgetting that the reduced matrix is $I+U^\top D^{-1}U$.
- Thinking Woodbury is only an algebra trick rather than a computational strategy.
- Forming $\Sigma^{-1}$ explicitly instead of factorizing the reduced system and solving.

## Interview Follow-Ups

- Derive the determinant identity

$$
\det(D+UU^\top)
=
\det(D)\det(I+U^\top D^{-1}U).
$$

- Suppose

$$
\Sigma=D+UCU^\top
$$

with nonsingular $C$. Derive the corresponding inverse.
- Explain why explicitly forming $\Sigma^{-1}$ is still usually inferior to factorizing the reduced matrix and solving systems.
- How would your approach change if some diagonal entries of $D$ were extremely small?

## Market / Rates Application

Large covariance matrices are frequently modeled as

$$
\Sigma=D+BFB^\top,
$$

where $D$ is idiosyncratic variance, $B$ contains factor exposures, and $F$ is a small factor covariance matrix.

This structure appears in:

- mean-variance portfolio optimization,
- factor-neutral portfolio construction,
- risk attribution,
- GLS estimation,
- multi-asset and rates risk models.

In a rates setting, thousands of instruments may be driven by a much smaller collection of curve-level, slope, curvature, spread, and volatility factors.

## Connections

- [S002 — Leave-One-Out OLS via Sherman-Morrison](../Statistics/S002_Leave_One_Out_OLS_via_Sherman_Morrison.md)
- [L001 — Ridge Regression as PCA Shrinkage](L001_Ridge_Regression_as_PCA_Shrinkage.md)
- [O003 — Primal vs Dual Optimization and When the Dual Is Easier](../Optimization/O003_Primal_vs_Dual_Optimization_and_When_the_Dual_Is_Easier.md)

## What to Remember

- Invert the small factor-space matrix, not the full covariance matrix.
- The reduced inverse is

$$
\left(I+U^\top D^{-1}U\right)^{-1}.
$$

- With diagonal-plus-low-rank structure, complexity scales with $k$, not $n$.
- This is one of the core computational ideas behind factor risk models.
