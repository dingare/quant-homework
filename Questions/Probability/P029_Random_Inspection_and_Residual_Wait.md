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

## Bus variant — 2026-10-30

Source: User-supplied bus question and the finalized explanation in the October 30 discussion. This is a guided review reference, not a new timed assessment.

### Question

一辆公交车沿环线持续运行，不停留时每圈恰好 10 分钟。每次经过冰淇淋店，司机独立抛一次公平硬币：正面额外停留 10 分钟，反面直接继续。你在一个固定站点独立、随机到达，求等到下一次公交经过的期望时间。如果额外停留的概率改为 $`p`$，答案如何变化？

“随机到达”指从很长的运行时段中均匀抽取到达时刻，忽略观察窗口两端的影响。

### 1. 先区分离散间隔与指数分布

设相邻两次公交经过站点的间隔为 $`T`$。按运行圈数抽样时：

```math
P(T=10)=1-p,\qquad P(T=20)=p.
```

公平硬币对应 $`p=1/2`$。这里是一个两点离散分布：每一圈的间隔只能是 10 或 20 分钟。它不是两个指数分布的混合，也不能把 10、20 当成指数分布的速率。

### 2. 随机时点抽中间隔的概率按长度加权

令 $`L`$ 为你到达时所在的完整间隔长度。较长间隔占据更多时间，因此

```math
E[T]=10(1-p)+20p=10(1+p),
```

```math
P(L=10)=\frac{10(1-p)}{10(1-p)+20p}
=\frac{1-p}{1+p},
\qquad
P(L=20)=\frac{20p}{10(1-p)+20p}
=\frac{2p}{1+p}.
```

对于公平硬币，这两个概率分别是 $`1/3`$ 和 $`2/3`$，不是各一半。要区分“随机抽一圈”和“随机抽一个时刻”。

### 3. 给定间隔长度，剩余等待均匀分布

你在该间隔内的位置均匀，所以剩余等待时间 $`W`$ 满足

```math
W\mid L=\ell\sim\mathrm{Uniform}(0,\ell),
\qquad E[W\mid L=\ell]=\frac\ell2.
```

于是公平硬币情形给出

```math
\boxed{E[W]=\frac13\times5+\frac23\times10
=\frac{25}{3}\text{ minutes}.}
```

即 **8 分 20 秒**。直接用两个间隔各一半加权会漏掉随机观察造成的长度偏差。

一般 $`0\le p\le1`$ 时：

```math
\boxed{E[W]
=\frac{1-p}{1+p}\times5+\frac{2p}{1+p}\times10
=\frac{5(1+3p)}{1+p}\text{ minutes}.}
```

也可以使用平稳更新过程的剩余等待公式：

```math
E[T^2]=100(1-p)+400p=100(1+3p),
\qquad
E[W]=\frac{E[T^2]}{2E[T]}
=\frac{5(1+3p)}{1+p}.
```

### 4. 怎样改成指数分布题？

把公交到站机制改为“到站遵循泊松过程，平均每 10 分钟来一辆；你独立到达”，则

```math
W\sim Exp(\lambda),\qquad
\lambda=\frac1{10}\text{ per minute},\qquad
E[W]=\frac1\lambda=10\text{ minutes}.
```

均值 10 分钟对应速率 $`1/10`$，不是速率 10。指数分布具有无记忆性：不论已经等了多久，接下来一小段时间内来车的条件概率都一样。

仅把额外停留时间改成指数分布仍不够：若每圈必定先运行 10 分钟，再增加指数停留时间 $`S`$，总间隔是 $`T=10+S`$，至少为 10 分钟，因此不是指数分布。

两条独立泊松线路“谁先来就坐谁”的问题见 [SC006 — 两条公交线路的指数时钟竞争](../StochasticCalculus/SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md#bus-variant--2026-10-30)。

## Assessment history

- [2026-10-13 Q2 — assessment](../../DailyTests/2026-10-13.md#q2--random-inspection-and-remaining-wait)
- [2026-10-14 R2 — assessment](../../DailyTests/2026-10-14.md#r2--random-time-residual-service)

## Related questions and knowledge

- [P014 — Conditional Expectation Under a Random Stopping Rule](P014_Conditional_Expectation_Under_a_Random_Stopping_Rule.md) — Sampling/inspection rules change conditional distributions.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
