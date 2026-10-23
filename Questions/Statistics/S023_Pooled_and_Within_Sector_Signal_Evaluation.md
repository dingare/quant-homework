# S023 — Pooled and Within-Sector Signal Evaluation

## Metadata

- Category: Statistics
- Tags: Total Covariance, Demeaning, FWL, Omitted-Variable Bias
- Date Added: 2026-10-22
- Original drill dates: 2026-10-20
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-20 Q3

Source and assessment: [2026-10-20 Q3](../../DailyTests/2026-10-20.md#q3--pooled-and-within-sector-signal-evaluation). The reference material below does not change that attempt’s recorded result.

### Question

You evaluate a stock-selection signal X against next-period return Y. Each observation belongs to sector A or B, with equal probability. Treat these as population facts:

| Quantity | Sector A | Sector B |
| --- | ---: | ---: |
| $`E[X\mid G]`$ | 2 | -2 |
| $`E[Y\mid G]`$ | 1 | -1 |
| $`\mathrm{Var}(X\mid G)`$ | 1 | 1 |
| $`\mathrm{Var}(Y\mid G)`$ | 1 | 1 |
| $`\mathrm{Cov}(X,Y\mid G)`$ | -1/2 | -1/2 |

1. Find the slope and R-squared of the population regression of Y on an intercept and X, pooling both sectors.
2. Find the coefficient on X when the regression also includes a sector indicator. Justify your calculation.
3. Explain the relationship between the two slopes. Does the pooled result establish that buying high-X stocks and selling low-X stocks within each sector has positive predictive value?

Keep the interpretation to a few interview-length sentences.

### Key solution

The pooled variables have means zero. Total variance and total covariance give:

```math
\mathrm{Var}(X)=1+4=5,\qquad
\mathrm{Var}(Y)=1+1=2,\qquad
\mathrm{Cov}(X,Y)=-\frac12+2=\frac32.
```

Thus the user's independently correct part-1 answers are:

```math
\beta_{\rm pooled}=\frac{3/2}{5}=\frac3{10},
\qquad
R^2=\frac{(3/2)^2}{5\cdot2}=\frac9{40}.
```

Let $`d=\mathbf1\{G=B\}`$ and $`z=(1,X,d)^\top`$. For $`\theta=(\alpha,\beta,\gamma)^\top`$, minimizing expected squared error yields the population normal equations:

```math
L(\theta)=E[(Y-z^\top\theta)^2],\qquad
\nabla L=-2E[z(Y-z^\top\theta)]=0,
\qquad
E[zz^\top]\theta=E[zY].
```

The residual is orthogonal to each regressor. Because $`d^2=d`$, $`E[d]=1/2`$, $`E[Xd]=-1`$ and $`E[dY]=-1/2`$, the numeric system is:

```math
\begin{pmatrix}1&0&1/2\\0&5&-1\\1/2&-1&1/2\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\\\gamma\end{pmatrix}
=\begin{pmatrix}0\\3/2\\-1/2\end{pmatrix},
\qquad
(\alpha,\beta,\gamma)=(2,-1/2,-4).
```

A simpler route allows a separate sector intercept. For fixed beta, the best intercept in sector g is $`a_g=E[Y\mid G=g]-\beta E[X\mid G=g]`$. Substituting it into the residual gives a regression of sector-demeaned Y on sector-demeaned X:

```math
\widetilde X=X-E[X\mid G],\qquad
\widetilde Y=Y-E[Y\mid G],\qquad
\beta=\frac{E[\widetilde X\widetilde Y]}{E[\widetilde X^2]}
=\frac{E[\mathrm{Cov}(X,Y\mid G)]}{E[\mathrm{Var}(X\mid G)]}
=-\frac12.
```

The dummy absorbs sector mean differences, leaving the common within-sector slope. If within-sector slopes differ, a dummy alone still imposes one common slope; an X-by-sector interaction permits separate slopes.

The covariance decomposition was derived on request by taking expectations of the conditional covariance definition and subtracting $`E[X]E[Y]`$:

```math
\mathrm{Cov}(X,Y)
=E[\mathrm{Cov}(X,Y\mid G)]
+\mathrm{Cov}(E[X\mid G],E[Y\mid G]).
```

The second term treats each sector as its center point: (2,1) or (-2,-1), each with probability one half. Their mean coordinates are zero, so between-sector covariance is $`(2\cdot1)/2+((-2)(-1))/2=2`$. This positive between-sector relationship outweighs within-sector covariance -1/2. Pooled positive association therefore does not establish positive within-sector stock-selection value. Distinguish selecting sectors from selecting stocks within a sector: sector exposure can itself be useful for a mandate that allows it, but it is a different predictive claim requiring evaluation.

The requested omitted-variable calculation uses the full population regression $`Y=2-X/2-4d+\varepsilon`$, with residual orthogonal to X and d. Omitting d shifts the X coefficient by:

```math
\mathrm{Cov}(X,d)=E[Xd]-E[X]E[d]=\frac12(-2)=-1,
\qquad
\beta_{\rm pooled}-\beta
=\gamma\frac{\mathrm{Cov}(X,d)}{\mathrm{Var}(X)}
=(-4)\frac{-1}{5}=\frac45.
```

Hence $`-1/2+4/5=3/10`$. Correlation between X and an omitted regressor is only one ingredient; the omitted variable's coefficient also matters. Bias here is relative to the within-sector target: 0.3 is the correct pooled linear-projection coefficient. An error term absorbing the omitted sector effect can correlate with X, while the pooled regression's own fitted residual remains orthogonal to X. These two residual/error meanings must not be conflated; no causal conclusion follows from adding a control alone.

## Assessment history

- [2026-10-20 Q3 — assessment](../../DailyTests/2026-10-20.md#q3--pooled-and-within-sector-signal-evaluation)

## Related questions and knowledge

- [S015 — Interaction and Recentering](S015_Interaction_and_Recentering.md) — Regression parameter interpretation depends on controls and centering.
- [S016 — Omitted-Variable Bias](S016_Omitted_Variable_Bias.md) — General omitted-variable formula and the sector-indicator example.
- [SVD QR Conditioning Least Squares and PCA](../../KnowledgeCards/LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md) — Knowledge card.
