# L002 — PCA, Covariance Geometry, and Why Butterfly Trades Curvature

## Metadata

- Category: Linear Algebra
- Secondary: Rates Research, Statistics
- Difficulty: ★★★☆☆
- Tags: PCA, Covariance Matrix, Eigenvectors, Eigenvalues, Yield Curve, Level, Slope, Curvature, Butterfly Trade

## Core Question

Given the covariance matrix

$$
\Sigma=
\begin{pmatrix}
4 & 3\\
3 & 4
\end{pmatrix}
$$

with eigenvectors

$$
v_1=\frac{1}{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
v_2=\frac{1}{\sqrt2}
\begin{pmatrix}
1\\
-1
\end{pmatrix}
$$

and eigenvalues

$$
\lambda_1=7,
\qquad
\lambda_2=1,
$$

what do these principal components mean geometrically, and how does the same idea connect to yield-curve curvature and butterfly trades?

## Key Result

For

$$
\Sigma=
\begin{pmatrix}
4 & 3\\
3 & 4
\end{pmatrix},
$$

the high-variance direction is

$$
(1,1)
$$

and the low-variance direction is

$$
(1,-1).
$$

If the covariance flips sign so that

$$
\Sigma=
\begin{pmatrix}
4 & -3\\
-3 & 4
\end{pmatrix},
$$

then the roles reverse:

- dominant direction becomes $(1,-1)$
- low-variance direction becomes $(1,1)$

So PCA directions are not fixed labels. They depend on the covariance structure.

## Intuition

PCA rotates coordinates into risk-factor directions.

- Positive covariance means the two variables usually move together, so $(1,1)$ is the common factor.
- Negative covariance means the typical joint move is opposite-signed, so $(1,-1)$ becomes the dominant factor.
- The low-variance direction is often the relative-value or spread direction because deviations there are smaller historically.

The important point is that "common movement" means the statistically dominant joint pattern, not necessarily same-sign movement.

## Geometry

The covariance matrix defines an ellipse.

- The long axis points in the highest-variance direction.
- The short axis points in the lowest-variance direction.

For positive covariance, the ellipse is stretched along $(1,1)$.

For negative covariance, the ellipse is stretched along $(1,-1)$.

This is why PCA is best read as geometry plus risk decomposition, not just eigenvalue algebra.

## Yield Curve Connection

In rates PCA, the empirical principal directions are usually interpreted as:

$$
PC1 \approx \text{level},\qquad
PC2 \approx \text{slope},\qquad
PC3 \approx \text{curvature}.
$$

These are orthogonal directions of historical yield-curve variation.

- Level: yields move up or down together.
- Slope: short and long maturities move differently.
- Curvature: the belly moves differently from the wings.

So the two-dimensional covariance example is the small version of the same idea used in rates factor decomposition.

## Why Butterfly Trades Curvature

A simple 2s5s10s butterfly is

$$
\text{Fly}=y_2-2y_5+y_{10}.
$$

This is a second-difference operator. It asks whether the 5y point is high or low relative to the line connecting 2y and 10y.

If

$$
y_5 \gt  \frac{y_2+y_{10}}{2},
$$

then the 5y yield is high relative to the wings, so 5y is cheap.

If

$$
y_5 \lt  \frac{y_2+y_{10}}{2},
$$

then the 5y yield is low relative to the wings, so 5y is rich.

## Why Level and Slope Cancel

A parallel level shift

$$
y_2 \to y_2+c,\qquad
y_5 \to y_5+c,\qquad
y_{10}\to y_{10}+c
$$

gives

$$
(y_2+c)-2(y_5+c)+(y_{10}+c)=y_2-2y_5+y_{10},
$$

so level cancels because

$$
c-2c+c=0.
$$

A linear slope move also approximately cancels because if 5y lies on the line between 2y and 10y, then

$$
y_5 \approx \frac{y_2+y_{10}}{2}
\quad\Rightarrow\quad
y_2-2y_5+y_{10}\approx 0.
$$

That is why the butterfly primarily isolates curvature rather than level or slope.

## Trading Interpretation

Conceptually:

- If 5y is cheap, buy 5y and short the 2y and 10y wings.
- If 5y is rich, short 5y and buy the 2y and 10y wings.

In practice, real trades are not equal-notional. They should be DV01-adjusted and often slope-neutralized.

## Market / Rates Application

A practical butterfly is chosen so that

$$
w_2DV01_2+w_5DV01_5+w_{10}DV01_{10}=0
$$

to make the position approximately level-neutral. Traders may also choose weights to reduce slope exposure, leaving mainly curvature exposure.

So there is a difference between:

- PCA curvature: an empirical orthogonal factor from historical covariance
- trader butterfly: a constructed portfolio designed to load mostly on belly-versus-wings shape

They are related, but not identical.

## Common Mistakes

Wrong:

$$
(1,1)\text{ is always the common factor.}
$$

Correct:

$$
\text{The dominant factor depends on the covariance structure.}
$$

Wrong:

$$
\text{Low variance means a good trade.}
$$

Correct:

$$
\text{Low variance only means that direction was historically stable.}
$$

It does not imply mean reversion or positive expected return.

## Interview Follow-ups

1. Why does changing the sign of covariance rotate the first principal component?
2. Why is $(1,-1)$ a spread direction when covariance is positive?
3. Why is PCA useful for yield-curve factor extraction?
4. What is the difference between PCA curvature and a butterfly trade?
5. Why does a butterfly cancel level exposure?
6. Why does a butterfly approximately cancel slope exposure?
7. Why do real butterfly weights need DV01 adjustment?

## What to Remember

$$
\boxed{\text{PCA rotates covariance into orthogonal risk directions.}}
$$

$$
\boxed{\text{Butterfly trades curvature because they largely cancel level and linear slope.}}
$$

$$
\boxed{\text{In rates, curvature means the belly moves differently from the wings.}}
$$
