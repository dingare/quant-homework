# L005 — Low-Rank Covariance Update and Portfolio Risk

## Problem

Let

$$
\Sigma=\begin{pmatrix}4&1&0\\1&3&1\\0&1&2\end{pmatrix},\quad
u=\begin{pmatrix}1\\1\\0\end{pmatrix},\quad
\widetilde\Sigma=\Sigma+2uu^\top,
\quad w=\begin{pmatrix}1\\-1\\1\end{pmatrix}.
$$

Without directly inverting $\widetilde\Sigma$, compute $\widetilde\Sigma^{-1}w$,
$w^\top\widetilde\Sigma^{-1}w$, and
$\det(\widetilde\Sigma)/\det(\Sigma)$. When does the update have no effect?

## Solution

Solve the two systems

$$
x=\Sigma^{-1}w=\frac1{9}(4,-7,8)^\top,\qquad
z=\Sigma^{-1}u=\frac1{6}(1,2,-1)^\top.
$$

Thus $u^\top z=1/2$ and $u^\top x=-1/3$. Sherman–Morrison gives

$$
\widetilde\Sigma^{-1}w
=x-\frac{2z(u^\top x)}{1+2u^\top z}
=x+\frac13z
=\boxed{\begin{pmatrix}1/2\\-2/3\\5/6\end{pmatrix}}.
$$

Also,

$$
w^\top\widetilde\Sigma^{-1}w
=w^\top x-\frac{2(w^\top z)^2}{1+2u^\top z}
=\frac{19}{9}-\frac1{9}
=\boxed{2}.
$$

The determinant lemma yields

$$
\boxed{\frac{\det(\widetilde\Sigma)}{\det(\Sigma)}
=1+2u^\top\Sigma^{-1}u=2}.
$$

The correction vanishes exactly when

$$
\boxed{u^\top\Sigma^{-1}w=0},
$$

which is orthogonality in inverse-covariance geometry, not necessarily ordinary Euclidean orthogonality.

## Interview Takeaways

- Solve linear systems; do not explicitly form a large inverse.
- A rank-one update changes the solution only along $\Sigma^{-1}u$.
- Low rank means low-dimensional, not necessarily small in magnitude.

## Finance Connection

This efficiently updates hedge ratios, Mahalanobis risk, and Gaussian likelihoods when a covariance model gains a new common risk factor.
