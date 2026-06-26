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

```math
\hat{\beta}_{\mathrm{OLS}} = (X^\top X)^{-1}X^\top y
```

Ridge:

```math
\hat{\beta}_{\lambda} = (X^\top X + \lambda I)^{-1}X^\top y
```

Given the SVD:

```math
X = UDV^\top
```

derive OLS and ridge in the PCA basis. Explain why ridge stabilizes OLS when regressors are highly collinear.

## Key SVD Facts

If

```math
X = UDV^\top
```

then

```math
X^\top X = VD^2V^\top
```

and

```math
XX^\top = UD^2U^\top
```

So:

- columns of $V$ are eigenvectors of $X^\top X$
- columns of $U$ are eigenvectors of $XX^\top$
- eigenvalues are $d_j^2$
- $V$ describes signal / regressor directions
- $U$ describes observation-space directions

In regression, $V$ is usually the more important object because it describes combinations of regressors/signals.

## OLS in PCA Basis

Since

```math
X^\top X = VD^2V^\top
```

we have

```math
(X^\top X)^{-1} = VD^{-2}V^\top
```

Also:

```math
X^\top = VDU^\top
```

so:

```math
X^\top y = VDU^\top y
```

Therefore:

```math
\hat{\beta}_{\mathrm{OLS}}
=
(VD^{-2}V^\top)(VDU^\top y)
=
VD^{-1}U^\top y
```

Equivalently:

```math
\hat{\beta}_{\mathrm{OLS}}
=
\sum_j \frac{u_j^\top y}{d_j}v_j
```

So the OLS coefficient along direction $v_j$ is:

```math
\hat{\theta}_j^{\mathrm{OLS}}
=
\frac{u_j^\top y}{d_j}
```

## Ridge in PCA Basis

```math
X^\top X + \lambda I
=
V(D^2 + \lambda I)V^\top
```

so

```math
(X^\top X + \lambda I)^{-1}
=
V(D^2 + \lambda I)^{-1}V^\top
```

Thus:

```math
\hat{\beta}_{\lambda}
=
V(D^2 + \lambda I)^{-1}DU^\top y
```

The ridge coefficient along $v_j$ is:

```math
\hat{\theta}_j^{\mathrm{ridge}}
=
\frac{d_j}{d_j^2 + \lambda}u_j^\top y
```

Compare with OLS:

```math
\hat{\theta}_j^{\mathrm{OLS}}
=
\frac{1}{d_j}u_j^\top y
```

Therefore:

```math
\boxed{
\hat{\theta}_j^{\mathrm{ridge}}
=
\frac{d_j^2}{d_j^2+\lambda}
\hat{\theta}_j^{\mathrm{OLS}}
}
```

## Intuition

OLS divides by $d_j$.

If $d_j$ is small, that direction is weakly identified. Small noise in $y$ gets amplified.

This is the linear algebra behind multicollinearity.

Ridge avoids dividing too aggressively in weak directions by replacing $d_j^2$ with $d_j^2+\lambda$.

Shrinkage factor:

```math
s_j = \frac{d_j^2}{d_j^2 + \lambda}
```

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

```math
\text{Ridge simply makes all coefficients smaller equally.}
```

Correct:

```math
\text{Ridge shrinks different PCA directions by different amounts.}
```

Wrong:

```math
U \text{ and } V \text{ are the same eigenvectors.}
```

Correct:

```math
V: \text{eigenvectors of } X^\top X
```

```math
U: \text{eigenvectors of } XX^\top
```

## What to Remember

```math
\boxed{
V = \text{signal-space eigenvectors of } X^\top X
}
```

```math
\boxed{
d_j^2 = \text{eigenvalues of } X^\top X
}
```

```math
\boxed{
\hat{\theta}_j^{\mathrm{ridge}}
=
\frac{d_j^2}{d_j^2+\lambda}
\hat{\theta}_j^{\mathrm{OLS}}
}
```

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
