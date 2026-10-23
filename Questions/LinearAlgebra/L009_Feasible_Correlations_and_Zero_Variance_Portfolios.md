# L009 — Feasible Correlations and Zero-Variance Portfolios

## Metadata

- Category: LinearAlgebra
- Tags: PSD, Correlation Matrix, Null Space
- Date Added: 2026-10-22
- Original drill dates: 2026-10-15
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-15 Q4

Source and assessment: [2026-10-15 Q4](../../DailyTests/2026-10-15.md#q4--feasible-correlations-and-zero-variance-portfolios). The reference material below does not change that attempt’s recorded result.

### Question

Three signals $`X,Y,Z`$ have mean zero and variance one, with correlations:

```math
\mathrm{Corr}(X,Y)=0.8,\qquad
\mathrm{Corr}(X,Z)=0.6,\qquad
\mathrm{Corr}(Y,Z)=r.
```

A colleague proposes $`r=-0.1`$, arguing that every pairwise correlation lies between negative one and one. Determine whether this proposal is coherent. Find the exact admissible range of $`r`$ and justify that every value in your range is attainable. At each endpoint, exhibit nonzero coefficients $`(a,b,c)`$ for which $`aX+bY+cZ`$ has zero variance.

### Key solution

The correlation matrix must be positive semidefinite:

```math
R(r)=\begin{pmatrix}
1&0.8&0.6\\
0.8&1&r\\
0.6&r&1
\end{pmatrix},\qquad
\det R(r)=0.96r-r^2=r(0.96-r).
```

The determinant constraint gives the admissible range below. All smaller principal minors are nonnegative throughout this range, so the constraint is also sufficient for PSD. Every such matrix is attainable as the covariance of a centered random vector, for example a possibly degenerate Gaussian vector. The proposed negative correlation is therefore inadmissible.

```math
\boxed{0\le r\le0.96}.
```

At both endpoints the covariance matrix is singular. The endpoint portfolios lie in its null space:

```math
\begin{aligned}
r=0:&\quad w_0=(-5,4,3)^\top,\qquad R(0)w_0=0,\\
r=0.96:&\quad w_{0.96}=(7,-20,15)^\top,\qquad R(0.96)w_{0.96}=0.
\end{aligned}
```

For portfolio weights in the null space, the variance is zero:

```math
\mathrm{Var}(aX+bY+cZ)=w^\top R(r)w=0.
```

## Assessment history

- [2026-10-15 Q4 — assessment](../../DailyTests/2026-10-15.md#q4--feasible-correlations-and-zero-variance-portfolios)

## Related questions and knowledge

- [L002 — PCA, Covariance Geometry, and Why Butterfly Trades Curvature](L002_PCA_Covariance_Geometry_and_Why_Butterfly_Trades_Curvature.md) — Covariance feasibility, geometry and zero-variance directions.
- [SVD QR Conditioning Least Squares and PCA](../../KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md) — Knowledge card.
