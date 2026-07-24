# L004 — Rank-One Covariance Update and Eigenvalue Interlacing

## Metadata

- Category: Linear Algebra
- Secondary: PCA, Matrix Perturbation, Covariance Estimation
- Difficulty: ★★★★★
- Tags: Rank-One Update, Eigenvalue Interlacing, Secular Equation, Matrix Determinant Lemma, PCA
- Review Priority: High
- Date Added: 2026-07-23
- Status: Final

## Core Question

Let

```math
\Sigma=\operatorname{diag}(4,2,1),
\qquad
u=(1,1,1)^\top,
```

and

```math
\widetilde\Sigma=\Sigma+uu^\top
=\begin{pmatrix}
5&1&1\\
1&3&1\\
1&1&2
\end{pmatrix}.
```

Derive the secular equation, locate and approximate the eigenvalues without solving a cubic symbolically, explain the PCA effect, and compute the determinant efficiently.

## Secular Equation

For \(\lambda\notin\{4,2,1\}\), the matrix determinant lemma gives

```math
\det(\widetilde\Sigma-\lambda I)
=\det(\Sigma-\lambda I)
\left[1+u^\top(\Sigma-\lambda I)^{-1}u\right].
```

Hence the new eigenvalues solve

```math
\boxed{
1+\frac1{4-\lambda}
+\frac1{2-\lambda}
+\frac1{1-\lambda}=0
}.
```

After clearing denominators, the correct characteristic polynomial is

```math
\boxed{
\lambda^3-10\lambda^2+28\lambda-22=0
}.
```

## Interlacing

Define

```math
f(\lambda)
=1+\frac1{4-\lambda}
+\frac1{2-\lambda}
+\frac1{1-\lambda}.
```

On every interval away from the poles,

```math
f'(\lambda)
=\frac1{(4-\lambda)^2}
+\frac1{(2-\lambda)^2}
+\frac1{(1-\lambda)^2}>0.
```

The one-sided limits at \(1,2,4\) show that there is exactly one root in each of

```math
(1,2),\qquad(2,4),\qquad(4,\infty).
```

Therefore

```math
\boxed{
\widetilde\lambda_1>4>
\widetilde\lambda_2>2>
\widetilde\lambda_3>1
}.
```

Numerically,

```math
\boxed{
\widetilde\lambda_1\approx5.88,\qquad
\widetilde\lambda_2\approx2.65,\qquad
\widetilde\lambda_3\approx1.47
}.
```

Useful checks are

```math
\sum_i\widetilde\lambda_i
=\operatorname{tr}(\widetilde\Sigma)=10
```

and

```math
\prod_i\widetilde\lambda_i
=\det(\widetilde\Sigma)=22.
```

## Determinant Without Expansion

Using the determinant lemma at \(\lambda=0\),

```math
\det(\Sigma+uu^\top)
=\det(\Sigma)\left(1+u^\top\Sigma^{-1}u\right).
```

Since

```math
\det(\Sigma)=8,
\qquad
u^\top\Sigma^{-1}u
=\frac14+\frac12+1=\frac74,
```

we get

```math
\boxed{\det(\widetilde\Sigma)=8\left(1+\frac74\right)=22}.
```

## Why Rank One Can Strongly Change PCA

Rank one means the update acts only along one direction:

```math
uu^\top x=u(u^\top x).
```

It does not mean the update is small. Here \(\|u\|^2=3\), and \(u\) overlaps with every original eigenvector. The leading eigenvector can rotate strongly toward the new common-factor direction, especially when the original eigengap is small.

For

```math
\Sigma(\alpha)=\Sigma+\alpha uu^\top,
```

first-order eigenvalue sensitivity is

```math
\frac{d\lambda_i}{d\alpha}=(v_i^\top u)^2.
```

This makes the role of alignment explicit.

## Important Knowledge Points

- A positive-semidefinite rank-one update cannot decrease any ordered eigenvalue.
- Secular equations locate roots between poles without requiring a closed-form polynomial solution.
- Low rank is a statement about dimension, not magnitude.
- Trace, determinant, and interlacing are fast consistency checks.
- Closely spaced eigenvalues imply potentially unstable eigenvectors.

## Common Mistakes

- Treating the old diagonal entries as roots after applying the determinant lemma.
- Losing the constant term when clearing denominators; here it is \(22\), not \(17\).
- Assuming a rank-one update only affects one eigenvalue.
- Confusing eigenvalue stability with eigenvector stability.

## Finance Connection

A new duration, liquidity, or policy factor may enter a covariance model as a low-rank update. Even though the update is low-dimensional, it can materially rotate PCA factors and change hedge ratios when the existing eigengaps are small.

## What to Remember

```math
\boxed{
\det(A+uu^\top)
=\det(A)(1+u^\top A^{-1}u)
}
```

and the same identity applied to \(A-\lambda I\) produces the secular equation.

