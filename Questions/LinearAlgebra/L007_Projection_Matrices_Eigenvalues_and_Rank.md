# L007 — Projection Matrices, Eigenvalues, and Rank

## Metadata

- Category: LinearAlgebra
- Tags: Idempotence, PSD, Image, Rank
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08, 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q7

Source and assessment: [2026-10-08 Q7](../../DailyTests/2026-10-08.md#q7--projection-matrices-and-psd). The reference material below does not change that attempt’s recorded result.

### Question

A real symmetric matrix P satisfies $`P^2=P`$. What are its possible eigenvalues? Must $`x^\top Px\ge0`$ hold for every x? Justify both conclusions.

### Recorded solution

```math
\lambda^2=\lambda\Rightarrow\lambda\in\{0,1\},
\qquad x^\top Px=x^\top P^\top Px=\|Px\|^2\ge0.
```

The identity uses both symmetry and idempotence. Such P is an orthogonal projection; idempotence alone does not justify this quadratic-form identity.

### Related Notes

- [L001 — Ridge Regression as PCA Shrinkage](L001_Ridge_Regression_as_PCA_Shrinkage.md#interview-drill--why-ridge-is-invertible): related PSD / squared-norm argument, not the same projection question.
- [New projection-matrix gap](../../Backlog.md#october-8-interview-knowledge-gaps).

## Interview drill — 2026-10-09 Q7

Source and assessment: [2026-10-09 Q7](../../DailyTests/2026-10-09.md#q7--projection-matrix). The reference material below does not change that attempt’s recorded result.

### Question

For full-column-rank A of size 5 by 2, let $`P=A(A^\top A)^{-1}A^\top`$. Determine its rank, possible eigenvalues, and whether it is PSD.

### Recorded answer details

The projection image is the two-dimensional column space of A: rank 2, two eigenvalues equal to 1, three equal to 0, and positive semidefinite.

## Assessment history

- [2026-10-08 Q7 — assessment](../../DailyTests/2026-10-08.md#q7--projection-matrices-and-psd)
- [2026-10-09 Q7 — assessment](../../DailyTests/2026-10-09.md#q7--projection-matrix)

## Related questions and knowledge

- [L008 — Conditioning and Least Squares](L008_Conditioning_and_Least_Squares.md) — Projection geometry, column space and stable least squares.
- [SVD QR Conditioning Least Squares and PCA](../../KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md) — Knowledge card.
