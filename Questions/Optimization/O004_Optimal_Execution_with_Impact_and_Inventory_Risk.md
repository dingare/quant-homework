# O004 — Optimal Execution with Impact and Inventory Risk

## Metadata

- Category: Optimization
- Secondary: Market Microstructure, Dynamic Optimization, Numerical Linear Algebra
- Difficulty: ★★★★☆
- Tags: Optimal Execution, Market Impact, Inventory Risk, Quadratic Optimization, Tridiagonal System
- Review Priority: High
- Date Added: 2026-07-26
- Status: Final

## Core Question

Buy $Q=6$ units over three periods. Let $q_t$ be the quantity executed in period $t$, and let

$$
R_t=6-\sum_{s=1}^t q_s
$$

be the remaining inventory after period $t$. Minimize

$$
\frac12\sum_{t=1}^3q_t^2
+\frac12(R_1^2+R_2^2)
$$

subject to

$$
q_1+q_2+q_3=6.
$$

Find the optimal schedule, minimized cost, and the general $T$-period first-order condition.

## Three-Period Solution

The execution constraint implies

$$
q_1=6-q_2-q_3,
\qquad
R_1=q_2+q_3,
\qquad
R_2=q_3.
$$

Thus

$$
\begin{aligned}
J(q_2,q_3)
={}&\frac12\left[(6-q_2-q_3)^2+q_2^2+q_3^2\right]\\
&+\frac12\left[(q_2+q_3)^2+q_3^2\right].
\end{aligned}
$$

The first-order conditions are

$$
3q_2+2q_3=6,
$$

and

$$
2q_2+4q_3=6.
$$

Solving gives

$$
q_2=\frac32,
\qquad
q_3=\frac34,
\qquad
q_1=\frac{15}{4}.
$$

Therefore

$$
\boxed{
(q_1^*,q_2^*,q_3^*)
=\left(\frac{15}{4},\frac32,\frac34\right)
=(3.75,1.50,0.75)
}.
$$

The remaining inventories are

$$
R_1=\frac94,
\qquad
R_2=\frac34.
$$

Impact cost is

$$
\frac12\sum_{t=1}^3(q_t^*)^2
=\frac{135}{16},
$$

and inventory-risk cost is

$$
\frac12\left[(R_1^*)^2+(R_2^*)^2\right]
=\frac{45}{16}.
$$

Hence

$$
\boxed{
J^*=\frac{180}{16}=\frac{45}{4}=11.25
}.
$$

## Why the Schedule Front-Loads

With no inventory-risk penalty, convex impact alone would produce the uniform schedule

$$
q_t=\frac QT.
$$

Inventory risk penalizes unfinished quantity at every intermediate date. An early trade reduces several future inventory penalties, while a late trade reduces few or none. The optimum balances

$$
\text{execute slowly to reduce impact}
$$

against

$$
\text{execute quickly to reduce inventory risk}.
$$

This produces $q_1^*\gt q_2^*\gt q_3^*$.

## General $T$-Period Problem

Consider

$$
\min_{\{q_t\}}
\frac{\eta}{2}\sum_{t=1}^Tq_t^2
+\frac{\lambda}{2}\sum_{t=1}^{T-1}R_t^2,
$$

with

$$
R_0=Q,\qquad R_T=0,\qquad q_t=R_{t-1}-R_t.
$$

In inventory coordinates, the objective is

$$
\frac{\eta}{2}\sum_{t=1}^T(R_{t-1}-R_t)^2
+\frac{\lambda}{2}\sum_{t=1}^{T-1}R_t^2.
$$

For each interior $t=1,\ldots,T-1$, the first-order condition is

$$
\boxed{
-\eta R_{t-1}
+(2\eta+\lambda)R_t
-\eta R_{t+1}=0
}.
$$

Equivalently,

$$
\boxed{
R_{t+1}
-\left(2+\frac{\lambda}{\eta}\right)R_t
+R_{t-1}=0
}.
$$

This is a second-order linear difference equation with boundary conditions $R_0=Q$ and $R_T=0$.

## Computational Structure

The Hessian in inventory coordinates is symmetric positive definite and tridiagonal. A specialized tridiagonal solver computes the schedule in

$$
\boxed{O(T)}
$$

time and $O(T)$ storage, rather than treating the system as a generic dense $O(T^3)$ problem.

## Limiting Cases

- As $\lambda\to0$, inventory risk disappears and $q_t\to Q/T$.
- As $\lambda/\eta\to\infty$, the optimizer increasingly executes near the beginning.
- Larger $\eta$ favors smoother execution.
- Larger $\lambda$ favors faster execution.

## Common Mistakes

- Penalizing $R_T$ even though full execution already forces $R_T=0$.
- Forgetting that an early trade reduces more than one future inventory term.
- Solving a dense system and missing the tridiagonal structure.
- Assuming front-loading always holds after adding alpha forecasts or time-varying liquidity.
- Confusing temporary impact with permanent impact.

## Interview Follow-Ups

1. Add participation constraints $0\le q_t\le c_t$ and state the KKT conditions.
2. Add time-varying impact coefficients $\eta_t$.
3. Add expected alpha from delaying or accelerating execution.
4. Solve the recurrence in hyperbolic-function form.
5. Explain how this connects to Almgren–Chriss.

## Finance Connection

For a Treasury or futures trade, $q_t^2$ approximates temporary liquidity cost and $R_t^2$ approximates mark-to-market risk from remaining DV01. Event risk raises $\lambda$; poor liquidity raises $\eta$.

## What to Remember

$$
\boxed{
\text{Optimal execution}
=\text{market-impact smoothing}
+\text{inventory-risk urgency}
}.
$$

