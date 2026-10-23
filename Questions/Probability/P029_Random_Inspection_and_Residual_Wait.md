# P029 — Random Inspection and Residual Wait

## Metadata

- Category: Probability
- Tags: Length Bias, Conditional Position, Survival Functions
- Date Added: 2026-10-22
- Original drill dates: 2026-10-13, 2026-10-14
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-13 Q2

Source and assessment: [2026-10-13 Q2](../../DailyTests/2026-10-13.md#q2--random-inspection-and-remaining-wait). The reference material below does not change that attempt’s recorded result.

### Question

A continuous service has iid intervals of 1 or 9 minutes, equally likely. Inspect at an independent uniform time over a long observation window. Find the probability of being in a 9-minute interval, expected residual wait, and probability that residual wait exceeds 4 minutes. Compare with starting immediately after a completion.

### Key solution

First select the interval by time share, then use uniform position within that interval:

```math
P(L=9)=\frac{(1/2)9}{(1/2)1+(1/2)9}=0.9,\qquad
R\mid L=\ell\sim\mathrm{Uniform}(0,\ell).
```

```math
E[R]=0.9\frac92+0.1\frac12=4.1,\qquad
P(R\gt4)=0.9\frac59=0.5.
```

Starting at a completion gives the full next interval, with mean 5 minutes and no length bias.

## Interview drill — 2026-10-14 R2

Source and assessment: [2026-10-14 R2](../../DailyTests/2026-10-14.md#r2--random-time-residual-service). The reference material below does not change that attempt’s recorded result.

### Question

Consecutive iid service durations are 3 or 6 minutes, equally likely. Arrive uniformly over a long operating period, ignoring endpoints. Derive the remaining-time survival function for every nonnegative time and its mean.

### Key solution

```math
P(L=3)=\frac13,\quad P(L=6)=\frac23,\quad
R\mid L=\ell\sim\mathrm{Uniform}(0,\ell).
```

```math
P(R\gt t)=\begin{cases}
1-\frac{2t}{9},&0\le t\lt3,\\
\frac{6-t}{9},&3\le t\lt6,\\
0,&t\ge6,
\end{cases}
\qquad E[R]=\int_0^\infty P(R\gt t)\,dt=\frac52.
```

## Assessment history

- [2026-10-13 Q2 — assessment](../../DailyTests/2026-10-13.md#q2--random-inspection-and-remaining-wait)
- [2026-10-14 R2 — assessment](../../DailyTests/2026-10-14.md#r2--random-time-residual-service)

## Related questions and knowledge

- [P014 — Conditional Expectation Under a Random Stopping Rule](P014_Conditional_Expectation_Under_a_Random_Stopping_Rule.md) — Sampling/inspection rules change conditional distributions.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
