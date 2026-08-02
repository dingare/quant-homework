# SC003 — Ornstein–Uhlenbeck First Hitting Time

## Metadata

- Category: Stochastic Calculus
- Secondary: Stochastic Processes, Time Series, Rates Research
- Difficulty: ★★★★★
- Tags: Ornstein–Uhlenbeck, First Passage Time, Infinitesimal Generator, Boundary Value Problem, Mean Reversion
- Review Priority: High
- Date Added: 2026-07-18
- Status: Finalized
- Personal Note: Expected hitting times turn a stochastic stopping problem into a generator ODE.

## Core Question

Let

$$
dX_t=-\kappa X_t\,dt+\sigma\,dW_t,
\qquad \kappa=2,\quad\sigma=3,\quad X_0=1,
$$

and define

$$
\tau=\inf\{t\ge0:X_t=0\}.
$$

Find the conditional mean and variance of $X_t$, explain why $\tau\lt \infty$ almost surely, derive the ODE for $u(x)=E_x[\tau]$, give an integral representation, and obtain its small-$x$ approximation.

## Hint

The generator is

$$
\mathcal Lf(x)=-\kappa xf'(x)+\frac{\sigma^2}{2}f''(x),
$$

and expected hitting times solve $\mathcal Lu=-1$ with an absorbing boundary at zero.

## Solution

The OU solution is

$$
X_t=X_0e^{-\kappa t}
+\sigma\int_0^te^{-\kappa(t-s)}\,dW_s.
$$

Thus, conditional on $X_0=1$,

$$
E[X_t]=e^{-2t},
\qquad
\mathrm{Var}(X_t)=\frac94(1-e^{-4t}).
$$

The OU process is a regular recurrent one-dimensional diffusion with stationary distribution $N(0,\sigma^2/(2\kappa))$. It visits both sides of zero and therefore hits zero almost surely.

For $x\gt 0$, $u(x)=E_x[\tau]$ satisfies

$$
\frac{\sigma^2}{2}u''(x)-\kappa xu'(x)=-1,
\qquad u(0)=0,
$$

together with a non-explosive growth condition at infinity. With $v=u'$, the integrating factor $e^{-\kappa x^2/\sigma^2}$ gives

$$
u'(x)=\frac{2}{\sigma^2}e^{\kappa x^2/\sigma^2}
\int_x^\infty e^{-\kappa y^2/\sigma^2}\,dy.
$$

Therefore,

$$
u(x)=\frac{2}{\sigma^2}
\int_0^x e^{\kappa z^2/\sigma^2}
\left[\int_z^\infty e^{-\kappa y^2/\sigma^2}\,dy\right]dz.
$$

For $\kappa=2$ and $\sigma=3$,

$$
u(x)=\frac29
\int_0^x e^{2z^2/9}
\left[\int_z^\infty e^{-2y^2/9}\,dy\right]dz.
$$

Near zero,

$$
u(x)\approx u'(0)x
=\frac{\sqrt\pi}{\sigma\sqrt\kappa}x
=\frac{\sqrt\pi}{3\sqrt2}x
\approx0.418x.
$$

## Key Knowledge Points

- The OU transition distribution is Gaussian.
- Hitting probabilities and expected hitting times are boundary-value problems for the generator.
- The drift-only OU path approaches zero asymptotically; diffusion noise creates finite crossings.
- Boundary and growth conditions select the economically relevant ODE solution.

## Intuition

Mean reversion pulls the state toward zero, while Brownian noise pushes it across. Close to the boundary, the expected waiting time is approximately linear in the starting distance.

## Common Mistakes

- Assuming deterministic mean reversion alone reaches zero in finite time.
- Writing $\mathcal Lu=0$ rather than $\mathcal Lu=-1$ for an expected hitting time.
- Forgetting the absorbing boundary $u(0)=0$.
- Solving the ODE without a condition at infinity.

## Interview Follow-ups

1. Replace the exit level zero by $-a$.
2. Derive the probability of hitting $+b$ before $-a$.
3. Find the ODE for $E_x[e^{-q\tau}]$.
4. Study how $u(x)$ changes with $\kappa$ and $\sigma$.
5. Add transaction costs and discuss optimal entry and exit bands.

## Market / Rates Application

OU dynamics are a first approximation for curve-spread residuals, swap-spread dislocations, cash–futures basis deviations, and relative-value z-scores. The hitting-time distribution describes how long capital may remain tied up before normalization.

## Connections

- [T003 — AR(1) First Passage Time](../TimeSeries/T003_AR1_First_Passage_Time_and_Why_Persistence_Changes_Waiting_Time.md)
- Infinitesimal generators and Dynkin's formula
- Free-boundary problems and optimal stopping
- Mean-reversion half-life versus actual first-passage time

## What to Remember

> For a diffusion, the expected time to hit a boundary solves $\mathcal Lu=-1$.
