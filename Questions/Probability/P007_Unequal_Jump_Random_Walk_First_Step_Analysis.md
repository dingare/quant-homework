# P007 — Unequal-Jump Random Walk and First-Step Analysis

## Metadata

- Category: Probability
- Secondary: Markov Chains, Dynamic Programming, Stopping Times
- Difficulty: ★★★★☆
- Tags: Random Walk, First-Step Analysis, Absorbing States, Hitting Probability, Expected Hitting Time, Overshoot
- Review Priority: High
- Date Added: 2026-07-26
- Status: Final

## Core Question

A random walk starts at $X_0=2$ and evolves by

$$
X_{t+1}=
\begin{cases}
X_t+2,&\text{with probability }0.4,\\
X_t-1,&\text{with probability }0.6.
\end{cases}
$$

Stop at

$$
\tau=\inf\{t\ge0:X_t\le0\text{ or }X_t\ge5\}.
$$

Compute:

1. $P_2(X_\tau\ge5)$;
2. $E_2[\tau]$;
3. why the standard nearest-neighbor gambler's-ruin formula fails.

## State Classification

The state is the current value of $X_t$.

- $X\le0$: lower absorbing region;
- $X\ge5$: upper absorbing region;
- $X\in\{1,2,3,4\}$: transient states.

Only the four transient states require unknown-value equations. Overshoot matters: a move from $4$ to $6$ is an upper exit even though the process never lands on $5$.

## Upper-Exit Probability

Define

$$
h_i=P_i(X_\tau\ge5).
$$

The boundary values are

$$
h_i=0\quad(i\le0),
\qquad
h_i=1\quad(i\ge5).
$$

Conditioning on the first step and using the Markov property gives

$$
\boxed{
h_i=0.4h_{i+2}+0.6h_{i-1}
},
\qquad i=1,2,3,4.
$$

Explicitly,

$$
\begin{aligned}
h_1&=0.4h_3,\\
h_2&=0.4h_4+0.6h_1,\\
h_3&=0.4+0.6h_2,\\
h_4&=0.4+0.6h_3.
\end{aligned}
$$

Substitution gives

$$
h_2=0.16+0.48h_3
$$

and

$$
h_3=0.4+0.6h_2.
$$

Solving,

$$
h_3=\frac{62}{89},
\qquad
\boxed{
h_2=\frac{44}{89}\approx0.4944
}.
$$

The one-step drift is positive:

$$
E[\Delta X]=0.4(2)-0.6(1)=0.2.
$$

Nevertheless, the upper-exit probability from $2$ is slightly below one half. Drift alone does not determine which boundary is reached first; starting position, jump sizes, and overshoot also matter.

## Expected Stopping Time

Define

$$
e_i=E_i[\tau].
$$

The boundary values are $e_i=0$ outside the continuation region. First-step analysis gives

$$
\boxed{
e_i=1+0.4e_{i+2}+0.6e_{i-1}
}.
$$

The $+1$ records the step taken immediately. The four equations are

$$
\begin{aligned}
e_1&=1+0.4e_3,\\
e_2&=1+0.4e_4+0.6e_1,\\
e_3&=1+0.6e_2,\\
e_4&=1+0.6e_3.
\end{aligned}
$$

Substitution produces

$$
e_2=2+0.48e_3,
\qquad
e_3=1+0.6e_2.
$$

Hence

$$
e_3=\frac{275}{89},
\qquad
\boxed{
E_2[\tau]=e_2=\frac{310}{89}\approx3.48
}.
$$

## Why Standard Gambler's Ruin Does Not Apply

The standard formula assumes nearest-neighbor moves $+1$ and $-1$, producing

$$
h_i=ph_{i+1}+qh_{i-1}.
$$

Here the recurrence is

$$
h_i=ph_{i+2}+qh_{i-1},
$$

and the process can overshoot the upper boundary. The state equations, not the nearest-neighbor closed form, are the reliable method.

## General Dynamic-Programming Form

If the jump distribution is $P(J=j)=p_j$, then for $L\lt x\lt U$,

$$
h(x)=\sum_jp_jh(x+j)
$$

with $h(x)=0$ for $x\le L$ and $h(x)=1$ for $x\ge U$.

Expected stopping time satisfies

$$
e(x)=1+\sum_jp_je(x+j),
$$

with $e(x)=0$ outside the continuation region.

For a finite transient-state set, these become

$$
\boxed{
(I-P_T)h=r,
\qquad
(I-P_T)e=\mathbf1
}.
$$

## Reusable Checklist

1. Define the state.
2. Identify absorbing and transient states.
3. Set the boundary values.
4. Condition on the first step.
5. Solve the resulting linear system.
6. Check whether jumps can overshoot a boundary.

## Common Mistakes

- Treating $5$ as the only upper absorbing state and forgetting $6,7,\ldots$.
- Using gambler's-ruin formulas designed for $\pm1$ jumps.
- Forgetting the $+1$ in expected-time recursions.
- Calling all integer values unknown states instead of solving only on the transient region.
- Inferring the exit probability from the sign of the drift alone.

## Interview Follow-Ups

1. Compute $P_2(X_\tau=5)$ and $P_2(X_\tau=6)$ separately.
2. Find $E_2[\tau\mid X_\tau\ge5]$.
3. Allow the up probability to depend on the current state.
4. Use a martingale to relate $E[X_\tau]$ and $E[\tau]$, accounting for overshoot.
5. Explain how sparsity helps for a million-state chain.

## Finance Connection

The walk models asymmetric P&L increments with stop-loss and take-profit regions. Positive expected P&L per step does not imply a high probability of hitting the profit target first.

## What to Remember

$$
\boxed{
\text{state}
\rightarrow
\text{absorbing boundaries}
\rightarrow
\text{first-step recursion}
\rightarrow
\text{linear system}
}.
$$

