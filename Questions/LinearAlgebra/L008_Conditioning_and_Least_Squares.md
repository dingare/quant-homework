# L008 — Conditioning and Least Squares

## Metadata

- Category: LinearAlgebra
- Tags: SVD, QR, Condition Number, Normal Equations
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q8

Source and assessment: [2026-10-11 Q8](../../DailyTests/2026-10-11.md#q8--conditioning-and-least-squares). The reference material below does not change that attempt’s recorded result.

### Question

A real full-column-rank matrix $`A`$ has singular values 10, 1, 0.01. Find the 2-norm condition numbers of $`A`$ and $`A^\top A`$. Compare normal equations with QR and assess whether a large condition number implies faulty implementation. Full column rank makes explicit the original question's intended setting.

### Key solution

```math
\kappa_2(A)=\frac{\sigma_{\max}}{\sigma_{\min}}=1000,\qquad
\kappa_2(A^\top A)=\kappa_2(A)^2=10^6.
```

Normal equations square conditioning; QR/SVD avoid explicitly forming the Gram matrix. Ill-conditioning measures problem sensitivity, even for a stable correct algorithm. For a wide matrix with input nullspace, the Gram matrix would be singular instead.

## Assessment history

- [2026-10-11 Q8 — assessment](../../DailyTests/2026-10-11.md#q8--conditioning-and-least-squares)

## Related questions and knowledge

- [L007 — Projection Matrices, Eigenvalues, and Rank](L007_Projection_Matrices_Eigenvalues_and_Rank.md) — Projection geometry, column space and stable least squares.
- [L001 — Ridge Regression as PCA Shrinkage](L001_Ridge_Regression_as_PCA_Shrinkage.md) — Singular values, conditioning and ridge regularization.
- [O009 — Gradient Descent and Spectral Contraction](../Optimization/O009_Gradient_Descent_and_Spectral_Contraction.md) — Extreme eigenvalues govern numerical sensitivity and convergence.
- [SVD QR Conditioning Least Squares and PCA](../../KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md) — Knowledge card.
