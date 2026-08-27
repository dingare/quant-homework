# P012 — Random-Walk Stopping: Hit +3 Before -2

## Metadata

- Category: Probability
- Secondary: Random Walks, Stopping Times, Martingales
- Difficulty: ★★★☆☆
- Tags: Gambler's Ruin, Optional Stopping, Hitting Probability, Expected Duration
- Review Priority: High
- Date Added: 2026-08-26
- Status: Final

## Core Question

Let

$$
S_n=\sum_{i=1}^n X_i,
\qquad
P(X_i=1)=0.55,
\qquad
P(X_i=-1)=0.45.
$$

Starting from $S_0=0$, stop at

$$
\tau=\inf\{n\ge0:S_n\in\{-2,3\}\}.
$$

Find $P(S_\tau=3)$ and $E[\tau]$. Then solve the fair-walk version.

## Hint

Shift the barriers to $0$ and $5$, so the starting state is $2$. For the biased walk use $r=q/p=9/11$. For the expected time, stop the martingale $S_n-(p-q)n$.

## Solution

### Hitting Probability

Write $h=P(S_\tau=3)$. The barrier distances are asymmetric: the walk starts two steps above the lower barrier and three steps below the upper barrier. After shifting by $2$, this is gambler's ruin on $\{0,1,\ldots,5\}$ starting from $i=2$.

For $p=11/20$, $q=9/20$, and $r=q/p=9/11$,

$$
h=\frac{1-r^2}{1-r^5}
=\frac{1-(9/11)^2}{1-(9/11)^5}
=\frac{26620}{51001}
\approx0.5220.
$$

Thus

$$
\boxed{P(S_\tau=3)\approx0.5220}.
$$

The upward drift makes the probability exceed the fair-walk value, but only slightly because the upper barrier is farther away.

### Expected Stopping Time

At stopping, $S_\tau$ is either $3$ or $-2$, so

$$
E[S_\tau]=3h-2(1-h)=5h-2.
$$

Since $p-q=0.1$, the process

$$
M_n=S_n-0.1n
$$

is a martingale. Optional stopping gives

$$
0=E[M_\tau]=E[S_\tau]-0.1E[\tau].
$$

Therefore

$$
E[\tau]
=\frac{5h-2}{0.1}
=\frac{310980}{51001}
\approx6.10.
$$

Hence

$$
\boxed{E[\tau]\approx6.10}.
$$

The bounded state space makes the stopping time integrable, so the standard optional-stopping calculation is valid.

### Fair-Walk Benchmark

When $p=q=1/2$, the hitting probability is linear in distance:

$$
P(S_\tau=3)=\frac{0-(-2)}{3-(-2)}=\boxed{\frac25}.
$$

For a fair walk between $-a$ and $b$, starting at $0$, $E[\tau]=ab$. Here $a=2$ and $b=3$, so

$$
\boxed{E[\tau]=2\cdot3=6}.
$$

Equivalently, stop the martingale $S_n^2-n$ and use $E[S_\tau^2]=6$.

## Intuition

Barrier geometry matters as much as drift. With no drift, the nearer lower barrier is hit more often, so the upper-hit probability is only $2/5$. A modest positive drift raises it to about $0.522$, while the expected duration remains near six steps.

## Interview Takeaways

- Shift arbitrary barriers to the standard gambler's-ruin interval.
- Use the exponential harmonic function for a biased walk and a linear function for a fair walk.
- The terminal-value identity converts a hit probability into $E[S_\tau]$.
- Use $S_n-(p-q)n$ for biased expected duration and $S_n^2-n$ for the fair case.

## Finance / Market Application

The two barriers can represent a take-profit and a stop-loss around a position. The calculation shows that win probability depends jointly on signal drift and unequal barrier distances; a win rate above one-half does not by itself determine expected profitability.

## What to Remember

$$
\boxed{
P(S_\tau=3)\approx0.5220,
\qquad
E[\tau]\approx6.10
}
$$

and in the fair case,

$$
\boxed{P(S_\tau=3)=\frac25,\qquad E[\tau]=6}.
$$
