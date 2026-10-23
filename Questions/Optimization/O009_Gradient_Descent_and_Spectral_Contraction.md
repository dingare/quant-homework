# O009 — Gradient Descent and Spectral Contraction

## Metadata

- Category: Optimization
- Tags: Eigenvalues, Step Size, Quadratic Optimization
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q8

Source and assessment: [2026-10-10 Q8](../../DailyTests/2026-10-10.md#q8--gradient-descent-and-spectral-contraction). The reference material below does not change that attempt’s recorded result.

### Question

For $`f(w)=\tfrac12w^\top Hw`$, let $`H`$ be symmetric positive definite with extreme eigenvalues 2 and 18. Find constant gradient-descent steps guaranteeing convergence from every start, assess $`\eta=0.12`$, and minimize worst-direction Euclidean contraction.

### Key solution

```math
\nabla f(w)=Hw,\quad w_{k+1}=(I-\eta H)w_k,\quad
\left|1-\eta\lambda_i\right|\lt1\iff 0\lt\eta\lt\frac{2}{18}.
```

The proposed step fails in the largest-eigenvalue direction. Balance the endpoint magnitudes for the optimal step:

```math
1-2\eta=18\eta-1\quad\Longrightarrow\quad
\eta^*=0.1,\qquad q^*=0.8.
```

## Assessment history

- [2026-10-10 Q8 — assessment](../../DailyTests/2026-10-10.md#q8--gradient-descent-and-spectral-contraction)

## Related questions and knowledge

- [L008 — Conditioning and Least Squares](../LinearAlgebra/L008_Conditioning_and_Least_Squares.md) — Extreme eigenvalues govern numerical sensitivity and convergence.
- [SVD QR Conditioning Least Squares and PCA](../../KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md) — Knowledge card.
