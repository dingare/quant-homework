# S001 — OLS Bias vs Variance with Correlated Regressors

## Metadata

- Category: Statistics
- Secondary: Econometrics, Linear Algebra, Quant Research
- Difficulty: ★★★★☆
- Tags: OLS, Multicollinearity, OVB, FWL, Bias vs Variance, Factor Attribution

## Core Question

True model:

$$
y=\beta_1x_1+\beta_2x_2+\epsilon,\qquad E[\epsilon|x_1,x_2]=0
$$

with

$$
Var(x_1)=Var(x_2)=1,\qquad Corr(x_1,x_2)=\rho
$$

where $\rho\approx 1$.

Compare:

$$
y\sim x_1+x_2
$$

versus

$$
y\sim x_1
$$

When is beta biased, and when is it only high variance?

## Key Result

Full regression:

$$
E[\hat\beta|X]=\beta
$$

so multicollinearity alone does not create bias.

Single-variable regression omitting $x_2$:

$$
\tilde\beta_1=\beta_1+\beta_2\rho
$$

so omitted variable bias is:

$$
\tilde\beta_1-\beta_1=\beta_2\rho
$$

Variance inflation in full regression:

$$
Var(\hat\beta_1)\propto \frac{1}{1-\rho^2}
$$

so as $\rho\to1$, coefficient estimates become unstable.

## Intuition

- Bias comes from misspecification/endogeneity.
- High variance comes from ill-conditioned $X'X$.
- Including correlated signals may create unstable attribution.
- Omitting correlated relevant signals creates bias.

## FWL View

The coefficient on $x_2$ is based on residualized $x_2$:

$$
\tilde x_2=M_{x_1}x_2
$$

If $x_2$ is almost explained by $x_1$, then $\tilde x_2$ is tiny, making the coefficient noisy.

## Common Mistake

Wrong:

$$
Corr(x_1,x_2)\approx1 \Rightarrow \text{bias}
$$

Correct:

$$
Corr(x_1,x_2)\approx1 \Rightarrow \text{high variance}
$$

Bias requires omitted variables or $E[\epsilon|X]\neq0$.

## Market Application

In rates factor models, carry and roll-down may be highly correlated. Including both can make attribution unstable, while omitting one may bias the other. This motivates residualization, PCA, ridge, or economically combining signals.

## What to Remember

$$
\boxed{\text{Omitting correlated signals creates bias; including them creates variance.}}
$$

$$
\boxed{\text{Multicollinearity hurts attribution more than prediction.}}
$$

## Connections

FWL, Residualization, Partial Correlation, Ridge, PCA, Factor Models, Signal Attribution, Rates RV
