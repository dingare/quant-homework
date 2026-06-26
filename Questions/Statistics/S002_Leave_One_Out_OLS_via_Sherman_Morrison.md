# S002 — Leave-One-Out OLS via Sherman-Morrison

## Metadata

- Category: Statistics
- Secondary: Linear Algebra, Econometrics, Machine Learning
- Difficulty: ★★★★☆
- Tags: OLS, Leave-One-Out, Sherman-Morrison, Hat Matrix, Leverage, Influence, Cook's Distance

## Core Question

OLS estimator:

```math
\hat{\beta}=(X^\top X)^{-1}X^\top y
```

Remove one observation $(x_i,y_i)$. Derive $\hat\beta_{(-i)}$ without refitting OLS.

## Key Result

Let

```math
A=X^\top X,\qquad e_i=y_i-x_i^\top\hat{\beta},\qquad h_i=x_i^\top A^{-1}x_i
```

Then:

```math
\boxed{
\hat{\beta}_{(-i)}
=
\hat{\beta}
-
\frac{A^{-1}x_ie_i}{1-h_i}
}
```

Equivalently:

```math
\boxed{
\hat{\beta}-\hat{\beta}_{(-i)}
=
\frac{A^{-1}x_ie_i}{1-h_i}
}
```

## Derivation Sketch

Removing one observation gives:

```math
X_{(-i)}^\top X_{(-i)}=X^\top X-x_ix_i^\top
```

Use Sherman-Morrison:

```math
(A-uu^\top)^{-1}
=
A^{-1}
+
\frac{A^{-1}uu^\top A^{-1}}{1-u^\top A^{-1}u}
```

with $u=x_i$.

## Intuition

An observation is influential when it has both:

1. large residual $e_i$,
2. high leverage $h_i$.

Large residual means it is poorly fitted.  
High leverage means it strongly affects the geometry of the regression.

## Market Application

Useful for diagnosing whether a rates regression is dominated by crisis days, liquidity events, auction dates, March 2020, balance-sheet shocks, or special repo episodes.

## Common Mistake

Large residual alone does not imply high influence.  
High leverage alone does not imply high influence.  
Influence requires both residual and leverage.

## Interview Follow-ups

- Derive leave-one-out prediction error:

```math
e_{(-i),i}=\frac{e_i}{1-h_i}
```

- Connect to Cook's distance.
- Extend to ridge regression.
- Extend to removing $k$ observations.
- Connect recursive least squares to Kalman filtering.

## What to Remember

```math
\boxed{
\hat{\beta}_{(-i)}
=
\hat{\beta}
-
\frac{(X^\top X)^{-1}x_ie_i}{1-h_i}
}
```

```math
\boxed{\text{Influence}=\text{large residual}+\text{high leverage}}
```

## Connections

Sherman-Morrison, Woodbury, Hat Matrix, Leverage, Cook's Distance, Influence Functions, LOOCV, Recursive Least Squares, Kalman Filter
