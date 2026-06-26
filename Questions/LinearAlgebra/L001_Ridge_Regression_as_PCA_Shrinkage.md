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
\hat\beta_{OLS}=(X'X)^{-1}X'y
$$

Ridge:

$$
\hat\beta_\lambda=(X'X+\lambda I)^{-1}X'y
$$

Given the SVD:

$$
X=UDV'
$$

derive OLS and ridge in the PCA basis. Explain why ridge stabilizes OLS when regressors are highly collinear.

## Key SVD Facts

If

$$
X=UDV'
$$

then

$$
X'X=VD^2V'
$$

and

$$
XX'=UD^2U'
$$

So:

- columns of $V$ are eigenvectors of $X'X$
- columns of $U$ are eigenvectors of $XX'$
- eigenvalues are $d_j^2$
- $V$ describes signal / regressor directions
- $U$ describes observation-space directions

In regression, $V$ is usually the more important object because it describes combinations of regressors/signals.

## OLS in PCA Basis

Since

$$
X'X=VD^2V'
$$

we have

$$
(X'X)^{-1}=VD^{-2}V'
$$

Also:

$$
X'=VDU'
$$

so:

$$
X'y=VDU'y
$$

Therefore:

$$
\hat\beta_{OLS}
=
(VD^{-2}V')(VDU'y)
=
VD^{-1}U'y
$$

Equivalently:

$$
\hat\beta_{OLS}
=
\sum_j \frac{u_j'y}{d_j}v_j
$$

So the OLS coefficient along direction $v_j$ is:

$$
\hat\theta_j^{OLS}
=
\frac{u_j'y}{d_j}
$$

## Ridge in PCA Basis

$$
X'X+\lambda I
=
V(D^2+\lambda I)V'
$$

so

$$
(X'X+\lambda I)^{-1}
=
V(D^2+\lambda I)^{-1}V'
$$

Thus:

$$
\hat\beta_\lambda
=
V(D^2+\lambda I)^{-1}DU'y
$$

The ridge coefficient along $v_j$ is:

$$
\hat\theta_j^{ridge}
=
\frac{d_j}{d_j^2+\lambda}u_j'y
$$

Compare with OLS:

$$
\hat\theta_j^{OLS}
=
\frac{1}{d_j}u_j'y
$$

Therefore:

$$
\boxed{
\hat\theta_j^{ridge}
=
\frac{d_j^2}{d_j^2+\lambda}
\hat\theta_j^{OLS}
}
$$

## Intuition

OLS divides by $d_j$.

If $d_j$ is small, that direction is weakly identified. Small noise in $y$ gets amplified.

This is the linear algebra behind multicollinearity.

Ridge avoids dividing too aggressively in weak directions by replacing $d_j^2$ with $d_j^2+\lambda$.

Shrinkage factor:

$$
s_j=\frac{d_j^2}{d_j^2+\lambda}
$$

If $d_j^2\gg\lambda$, then $s_j\approx1$.  
If $d_j^2\ll\lambda$, then $s_j\approx0$.

So ridge mostly shrinks unstable low-eigenvalue directions.

## Market / Rates Application

Rates signals such as carry, roll-down, curve slope, repo specialness, basis, and auction cheapening are often correlated.

OLS may produce unstable coefficients because some signal combinations have very small eigenvalues in $X'X$.

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
V: \text{eigenvectors of } X'X
$$

$$
U: \text{eigenvectors of } XX'
$$

## What to Remember

$$
\boxed{
V = \text{signal-space eigenvectors of } X'X
}
$$

$$
\boxed{
d_j^2 = \text{eigenvalues of } X'X
}
$$

$$
\boxed{
\hat\theta_j^{ridge}
=
\frac{d_j^2}{d_j^2+\lambda}
\hat\theta_j^{OLS}
}
$$

Ridge is PCA-direction-specific shrinkage.

## Connections

- Multicollinearity
- Eigenvalues of $X'X$
- PCA
- Principal Component Regression
- Ridge Regression
- Bias-Variance Tradeoff
- Signal Attribution
- Rates Factor Models
