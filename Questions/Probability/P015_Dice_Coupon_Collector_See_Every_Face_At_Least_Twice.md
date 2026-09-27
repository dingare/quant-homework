# P015 — Dice Coupon Collector: See Every Face at Least Twice

## Problem

Roll a fair six-sided die repeatedly. What is the expected number of rolls required
until every face $1,\ldots,6$ has appeared at least twice?

## Warm-Up: Every Face Appears at Least Once

If $k$ distinct faces have appeared, the probability that the next roll produces a
new face is $(6-k)/6$. The expected waiting time for the next new face is therefore
$6/(6-k)$. Hence the ordinary coupon-collector expectation is

$$
E[T_1]
=1+\frac65+\frac64+\frac63+\frac62+6
=6H_6
=\boxed{14.7}.
$$

## Why the Warm-Up Argument No Longer Suffices

For the twice-seen problem, the number of distinct faces is not a sufficient state.
When all six faces have appeared once, for example, some may already have appeared
two or more times.

Let $E(a,b)$ denote the expected number of additional rolls when

- $a$ faces have appeared zero times;
- $b$ faces have appeared exactly once; and
- the remaining $6-a-b$ faces have appeared at least twice.

The desired expectation is $E(6,0)$, and the terminal condition is

$$
E(0,0)=0.
$$

## First-Step Recurrence

From state $(a,b)$, the next roll has three possible effects:

1. With probability $a/6$, an unseen face is rolled and the state becomes
   $(a-1,b+1)$.
2. With probability $b/6$, a once-seen face is rolled and the state becomes
   $(a,b-1)$.
3. With probability $(6-a-b)/6$, a face already seen at least twice is rolled and
   the state remains $(a,b)$.

First-step analysis therefore gives

$$
E(a,b)
=1+\frac a6E(a-1,b+1)
+\frac b6E(a,b-1)
+\frac{6-a-b}{6}E(a,b).
$$

Moving the self-loop term to the left yields

$$
\frac{a+b}{6}E(a,b)
=1+\frac a6E(a-1,b+1)+\frac b6E(a,b-1),
$$

so, for $a+b\gt0$,

$$
\boxed{
E(a,b)=\frac{6+aE(a-1,b+1)+bE(a,b-1)}{a+b}
}.
$$

Terms multiplied by $a=0$ or $b=0$ are simply omitted. Evaluating the finite set of
states from the boundary condition gives

$$
E(6,0)=\frac{390968681}{16200000}
\approx 24.133869.
$$

Therefore, the expected number of rolls required is

$$
\boxed{E[T_2]\approx24.13\text{ rolls}}.
$$

## Interview Insight

The ordinary coupon collector needs only one state variable: the number of distinct
coupons collected. Requiring two copies makes that summary insufficient. The pair

$$
(\text{number seen zero times},\ \text{number seen exactly once})
$$

retains precisely the information needed for future transitions. Once a face has
appeared twice, its exact count is irrelevant. This compressed state turns a
history-dependent problem into a small Markov-chain dynamic program.
