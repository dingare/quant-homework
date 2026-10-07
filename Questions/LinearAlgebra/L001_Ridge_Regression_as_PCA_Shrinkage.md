# L001 — Ridge Regression as PCA Shrinkage

## Metadata

- Category: Linear Algebra
- Secondary: Statistics, Machine Learning, Optimization
- Difficulty: ★★★★☆
- Tags: SVD, Ridge Regression, PCA, OLS, Multicollinearity, Eigenvalues, Matrix Algebra
- Review Priority: High
- Personal Note: I am less familiar with SVD and matrix calculation. Review this again.

## Core Question

OLS:

$$
\hat{\beta}_{\mathrm{OLS}} = (X^\top X)^{-1}X^\top y
$$

Ridge:

$$
\hat{\beta}_{\lambda} = (X^\top X + \lambda I)^{-1}X^\top y
$$

Given the SVD:

$$
X = UDV^\top
$$

derive OLS and ridge in the PCA basis. Explain why ridge stabilizes OLS when regressors are highly collinear.

## Key SVD Facts

If

$$
X = UDV^\top
$$

then

$$
X^\top X = VD^2V^\top
$$

and

$$
XX^\top = UD^2U^\top
$$

So:

- columns of $V$ are eigenvectors of $X^\top X$
- columns of $U$ are eigenvectors of $XX^\top$
- eigenvalues are $d_j^2$
- $V$ describes signal / regressor directions
- $U$ describes observation-space directions

In regression, $V$ is usually the more important object because it describes combinations of regressors/signals.

## OLS in PCA Basis

Since

$$
X^\top X = VD^2V^\top
$$

we have

$$
(X^\top X)^{-1} = VD^{-2}V^\top
$$

Also:

$$
X^\top = VDU^\top
$$

so:

$$
X^\top y = VDU^\top y
$$

Therefore:

$$
\hat{\beta}_{\mathrm{OLS}}=
(VD^{-2}V^\top)(VDU^\top y)=
VD^{-1}U^\top y
$$

Equivalently:

$$
\hat{\beta}_{\mathrm{OLS}}=
\sum_j \frac{u_j^\top y}{d_j}v_j
$$

So the OLS coefficient along direction $v_j$ is:

$$
\hat{\theta}_j^{\mathrm{OLS}}=
\frac{u_j^\top y}{d_j}
$$

## Ridge in PCA Basis

$$
X^\top X + \lambda I=
V(D^2 + \lambda I)V^\top
$$

so

$$
(X^\top X + \lambda I)^{-1}=
V(D^2 + \lambda I)^{-1}V^\top
$$

Thus:

$$
\hat{\beta}_{\lambda}=
V(D^2 + \lambda I)^{-1}DU^\top y
$$

The ridge coefficient along $v_j$ is:

$$
\hat{\theta}_j^{\mathrm{ridge}}=
\frac{d_j}{d_j^2 + \lambda}u_j^\top y
$$

Compare with OLS:

$$
\hat{\theta}_j^{\mathrm{OLS}}=
\frac{1}{d_j}u_j^\top y
$$

Therefore:

$$
\boxed{
\hat{\theta}_j^{\mathrm{ridge}}=
\frac{d_j^2}{d_j^2+\lambda}
\hat{\theta}_j^{\mathrm{OLS}}
}
$$

## Intuition

OLS divides by $d_j$.

If $d_j$ is small, that direction is weakly identified. Small noise in $y$ gets amplified.

This is the linear algebra behind multicollinearity.

Ridge avoids dividing too aggressively in weak directions by replacing $d_j^2$ with $d_j^2+\lambda$.

Shrinkage factor:

$$
s_j = \frac{d_j^2}{d_j^2 + \lambda}
$$

If $d_j^2\gg\lambda$, then $s_j\approx1$.
If $d_j^2\ll\lambda$, then $s_j\approx0$.

So ridge mostly shrinks unstable low-eigenvalue directions.

## Market / Rates Application

Rates signals such as carry, roll-down, curve slope, repo specialness, basis, and auction cheapening are often correlated.

OLS may produce unstable coefficients because some signal combinations have very small eigenvalues in $X^\top X$.

Ridge stabilizes prediction by shrinking weak signal directions.

This helps when:

- signals are highly correlated,
- sample size is limited,
- coefficients flip signs across windows,
- prediction matters more than pure attribution.

But ridge introduces bias to reduce variance.

## Common Mistakes

Wrong:

$$
\text{Ridge simply makes all coefficients smaller equally.}
$$

Correct:

$$
\text{Ridge shrinks different PCA directions by different amounts.}
$$

Wrong:

$$
U \text{ and } V \text{ are the same eigenvectors.}
$$

Correct:

$$
V: \text{eigenvectors of } X^\top X
$$

$$
U: \text{eigenvectors of } XX^\top
$$

## What to Remember

$$
\boxed{
V = \text{signal-space eigenvectors of } X^\top X
}
$$

$$
\boxed{
d_j^2 = \text{eigenvalues of } X^\top X
}
$$

$$
\boxed{
\hat{\theta}_j^{\mathrm{ridge}}=
\frac{d_j^2}{d_j^2+\lambda}
\hat{\theta}_j^{\mathrm{OLS}}
}
$$

Ridge is PCA-direction-specific shrinkage.

## Connections

- Multicollinearity
- Eigenvalues of $X^\top X$
- PCA
- Principal Component Regression
- Ridge Regression
- Bias-Variance Tradeoff
- Signal Attribution
- Rates Factor Models

## Interview Drill — Why Ridge Is Invertible

### Question

Why is $A=X^\top X+\lambda I$, $\lambda\gt0$, invertible even if $X^\top X$ is singular?

### Answer

The matrix $X^\top X$ is positive semidefinite, so all its eigenvalues are nonnegative. Adding $\lambda I$ leaves the eigenvectors unchanged and shifts each eigenvalue by the positive number lambda:

$$
\lambda_i(X^\top X+\lambda I)=\lambda_i(X^\top X)+\lambda\gt0.
$$

Thus A is positive definite and invertible. Equivalently, for any nonzero real vector v,

$$
v^\top Av=\|Xv\|^2+\lambda\|v\|^2\gt0.
$$

The crucial claim is that **every** eigenvalue is positive, not merely that one nonzero eigenvalue exists.

### Timed Attempt

[2026-10-06 Q7](../../DailyTests/2026-10-06.md#q7--linear-algebra-and-optimization-lightning-round): Y/G, about 5 minutes for the combined lightning round; stopped at the recommended limit. Concepts were correct, but formulas were not automatic. Continue with the [mean-variance answer](../Optimization/O002_Constrained_Mean_Variance_Optimization_and_the_Meaning_of_Lagrange_Multipliers.md#interview-drill--risk-aversion-and-a-budget-constraint).
