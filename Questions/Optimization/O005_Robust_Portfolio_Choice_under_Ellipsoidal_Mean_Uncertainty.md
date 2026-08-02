# O005 — Robust Portfolio Choice under Ellipsoidal Mean Uncertainty

## Problem

Let

$$
\widehat\mu=(4,3)^\top,qquad
\Sigma=\begin{pmatrix}2&1\\1&2\end{pmatrix},
$$

and $\mu=\widehat\mu+\delta$, where
$\delta^\top\Sigma^{-1}\delta\le1$. Solve

$$
\max_{w:\,w^\top\Sigma w\le1}
\min_{\delta^\top\Sigma^{-1}\delta\le1}w^\top(\widehat\mu+\delta).
$$

## Worst-Case Mean

Cauchy–Schwarz in the $\Sigma$-geometry gives

$$
\min_\delta w^\top\delta=-\sqrt{w^\top\Sigma w},
$$

attained at $\delta^*=-\Sigma w/\sqrt{w^\top\Sigma w}$. Thus the robust objective is

$$
w^\top\widehat\mu-\sqrt{w^\top\Sigma w}.
$$

## Optimal Portfolio

For risk $r=\sqrt{w^\top\Sigma w}$, generalized Cauchy–Schwarz yields

$$
w^\top\widehat\mu\le r\sqrt{\widehat\mu^\top\Sigma^{-1}\widehat\mu}.
$$

Here

$$
\Sigma^{-1}\widehat\mu=\frac13(5,2)^\top,qquad
\widehat\mu^\top\Sigma^{-1}\widehat\mu=\frac{26}{3}.
$$

Since $\sqrt{26/3}\gt 1$, use the full risk budget in the optimal direction:

$$
\boxed{w^*=\frac{\Sigma^{-1}\widehat\mu}
{\sqrt{\widehat\mu^\top\Sigma^{-1}\widehat\mu}}
=\frac1{\sqrt{78}}(5,2)^\top}.
$$

The optimal worst-case return is

$$
\boxed{V^*=\sqrt{\frac{26}{3}}-1\approx1.944}.
$$

## General Uncertainty Radius

For radius $\rho$, the objective at risk level $r$ is

$$
r\left(\sqrt{\widehat\mu^\top\Sigma^{-1}\widehat\mu}-\rho\right).
$$

The optimizer chooses $w=0$ when $\rho$ exceeds the maximum nominal Sharpe
$\sqrt{\widehat\mu^\top\Sigma^{-1}\widehat\mu}$. At equality, every scale along
the optimal direction, including zero, has value zero.

## Finance Connection

Ellipsoidal alpha uncertainty produces a volatility penalty. A nominally attractive
rates trade is rejected when its maximum Sharpe is not large enough relative to mean-estimation uncertainty.
