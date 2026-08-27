# O008 — Risk Budgeting with a Binding Factor Constraint

## Metadata

- Category: Optimization
- Secondary: Portfolio Optimization, Convex Optimization, KKT Conditions
- Difficulty: ★★★★☆
- Tags: Risk Budget, Factor Constraint, KKT, Shadow Price, Active Constraint
- Review Priority: High
- Date Added: 2026-08-26
- Status: Final

## Core Question

Solve

$$
\max_w\quad \mu^\top w
$$

subject to

$$
w^\top\Sigma w\le1,
\qquad
w_1+w_2\le0.2,
$$

where shorting is allowed and

$$
\Sigma=
\begin{pmatrix}
4&1&0\\
1&2&0\\
0&0&1
\end{pmatrix},
\qquad
\mu=
\begin{pmatrix}
6\\4\\3
\end{pmatrix}.
$$

Find the unrestricted risk-budget solution, determine whether the factor cap binds, solve the constrained problem, and interpret the KKT multipliers.

## Hint

Without the factor cap, the maximizing direction is $\Sigma^{-1}\mu$. With a binding cap, the KKT stationarity condition is

$$
\mu-2\lambda\Sigma w-\nu a=0,
\qquad
a=(1,1,0)^\top.
$$

## Solution

### Unrestricted Risk-Budget Benchmark

By Cauchy–Schwarz in the $\Sigma$ inner product,

$$
w^{\mathrm{unc}}
=\frac{\Sigma^{-1}\mu}{\sqrt{\mu^\top\Sigma^{-1}\mu}},
$$

and the maximum expected return is

$$
\sqrt{\mu^\top\Sigma^{-1}\mu}.
$$

Here

$$
\Sigma^{-1}
=\begin{pmatrix}
2/7&-1/7&0\\
-1/7&4/7&0\\
0&0&1
\end{pmatrix},
$$

so

$$
\mu^\top\Sigma^{-1}\mu=\frac{151}{7}.
$$

Therefore

$$
\boxed{
\max\mu^\top w
=\sqrt{\frac{151}{7}}
\approx4.65
}.
$$

The unrestricted portfolio has

$$
w_1^{\mathrm{unc}}+w_2^{\mathrm{unc}}
=\frac{18/7}{\sqrt{151/7}}
\approx0.553\gt0.2.
$$

Hence the factor constraint binds at the constrained optimum.

### Constrained Solution

Let $a=(1,1,0)^\top$. The Lagrangian is

$$
\mathcal L(w,\lambda,\nu)
=\mu^\top w
-\lambda(w^\top\Sigma w-1)
-\nu(a^\top w-0.2),
$$

with $\lambda,\nu\ge0$. Stationarity gives

$$
w=\frac{1}{2\lambda}\Sigma^{-1}(\mu-\nu a).
$$

Impose the two active constraints

$$
w^\top\Sigma w=1,
\qquad
a^\top w=0.2.
$$

Solving yields

$$
\nu\approx3.3523
$$

and

$$
\boxed{
w^\star\approx
\begin{pmatrix}
0.20248\\
-0.00248\\
0.91488
\end{pmatrix}
}.
$$

The small short position in asset 2 is permitted. Direct checks give

$$
w_1^\star+w_2^\star=0.2,
\qquad
(w^\star)^\top\Sigma w^\star=1.
$$

The optimal expected return is

$$
\boxed{
\mu^\top w^\star\approx3.9496
}.
$$

### KKT and Shadow-Price Interpretation

The multiplier $\lambda$ is the marginal value of relaxing the variance budget in its squared-risk units. The factor multiplier $\nu$ is the local increase in optimal expected return from raising the cap $0.2$ by one unit:

$$
\frac{\partial V(c)}{\partial c}=\nu
\approx3.3523.
$$

Thus a small relaxation $dc$ of the factor limit improves the optimized objective by approximately $3.3523\,dc$. Complementary slackness explains why $\nu\gt0$: the unrestricted portfolio violates the factor cap, so scarce factor exposure has positive shadow value.

Economically, the cap forces the portfolio away from the unconstrained return-per-unit-risk direction. Most risk is allocated to asset 3, which has zero exposure to the constrained factor, while assets 1 and 2 nearly offset each other.

## Interview Takeaways

- A linear objective over an ellipsoid is solved by the covariance-weighted direction $\Sigma^{-1}\mu$.
- Test a candidate inequality constraint against the unrestricted solution before declaring it active.
- With an active linear cap, replace $\mu$ by the shadow-adjusted return vector $\mu-\nu a$.
- Shorting can make one component slightly negative even when all expected returns are positive.

## Finance / Market Application

A portfolio may have a strict budget for duration, market beta, sector exposure, or another common factor. The shadow price quantifies how much forecast return the risk team sacrifices by tightening that exposure limit.

## What to Remember

$$
\boxed{
w^\star\approx(0.203,-0.003,0.915)^\top,
\qquad
\mu^\top w^\star\approx3.95
}.
$$
