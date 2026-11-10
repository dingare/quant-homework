# SC006 — Competing Exponentials and Time-Dependent Hazards

## Metadata

- Category: Stochastic Calculus
- Secondary: Survival Analysis, Competing Risks
- Difficulty: ★★★★☆
- Tags: Exponential, Gamma, Memorylessness, Hazard Rate, Competing Risks
- Review Priority: High
- Personal Note: Revisit the distinction between a local hazard share and the global probability of eventually winning a competing-risk race.
- Date Added: 2026-08-13
- Status: Final

## Core Question

三个独立事件时钟分别为 favorable fill、adverse move 和 cancellation：

```math
T_F\sim Exp(4),\qquad T_A\sim Exp(2),\qquad T_C\sim Exp(1).
```

令 $`T=\min(T_F,T_A,T_C)`$。已知前 $`0.3`$ 秒无事件，求 fill 先发生的概率和 $`E[T\mid T\gt0.3]`$；给定首个事件恰在 $`0.8`$ 秒发生，求其为 fill 的概率。再将 fill 时钟改为 $`Gamma(2,4)`$，解释 survival information 如何改变风险竞争。

## Exponential Clocks

总 rate 为 $`7`$。无记忆性给出

```math
\boxed{P(F\text{ first}\mid T\gt0.3)=\frac47}.
```

并且

```math
T-0.3\mid T\gt0.3\sim Exp(7),
```

所以

```math
\boxed{E[T\mid T\gt0.3]=0.3+\frac17\approx0.4429}.
```

给定首个事件发生于时刻 $`t`$，fill 的联合密度为 $`4e^{-7t}`$，任意首事件的密度为 $`7e^{-7t}`$，故

```math
\boxed{P(F\mid T=t)=\frac47}.
```

这也说明独立指数时钟中，最短到达时间与赢家身份独立。

## Gamma Fill Clock

若 $`T_F\sim Gamma(2,4)`$，则

```math
S_F(t)=e^{-4t}(1+4t),
\qquad
f_F(t)=16te^{-4t},
```

所以 hazard 为

```math
h_F(t)=\frac{16t}{1+4t}.
```

它从 $`h_F(0)=0`$ 上升到

```math
h_F(0.3)=\frac{4.8}{2.2}\approx2.182.
```

在 $`0.3`$ 时刻刚发生某事件的条件下，该事件为 fill 的局部概率为

```math
\boxed{\frac{h_F(0.3)}{h_F(0.3)+2+1}\approx0.421}.
```

因此 survival 使 imminent fill 相对初始时刻更可能。这里的比值是局部、条件于短区间内发生事件的概率，并不直接等于“最终 fill 赢得竞争”的全局概率。

## What Breaks

Gamma 分布不满足

```math
P(T_F\gt s+t\mid T_F\gt s)=P(T_F\gt t).
```

其 residual lifetime 依赖已经存活的年龄，所以不能再用固定 rate 比例描述整个未来。正确对象是随时间变化的 hazard：

```math
P(i\text{ occurs in }[t,t+dt]\mid T\gt t)
\approx h_i(t)dt.
```

## What to Remember

- 独立 exponentials：最小值 rate 相加，赢家概率为自身 rate 占比。
- non-exponential competing risks：年龄包含信息，应使用 survival function 与 time-dependent hazard。
- inspection paradox 还涉及随机观察时的 length-biased sampling，不能仅靠 memorylessness 一句话代替。

## Connections

- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — 从 exponential race 扩展到 Poisson arrivals、Gamma / Weibull hazards、queue position、inspection paradox 与 phase-type CTMC 的结构化复习卡。
- [SC004 — Competing Exponential Clocks and CTMC Hitting](SC004_Competing_Exponential_Clocks_and_CTMC_Hitting.md) — 状态依赖 rates 和有限状态 first-step analysis。

## Interview drill — 2026-10-09 Q6

Source and assessment: [2026-10-09 Q6](../../DailyTests/2026-10-09.md#q6--competing-poisson-processes). The reference material below does not change that attempt’s recorded result.

### Question

Independent Poisson processes have rates 2 and 3 per hour. Find (a) the probability the first A event occurs before the second B event and (b) the expected time to the first event of either process.

### Recorded solution

In the merged process, each arrival is labeled A with probability 2/5 and B with probability 3/5. A arrives before the second B if the first label is A, or the first is B and the second is A:

```math
\frac25+\frac35\frac25=\frac{16}{25}.
```

### Recorded answer details

The second B arrival is Erlang/Gamma, not exponential with half the rate. Superposition gives rate 5 and an expected first-arrival wait of 1/5 hour.

## Bus variant — 2026-10-30

Source: Finalized October 30 discussion of two bus routes and the survival-function derivation. This is a guided review reference, not a new timed assessment.

### Question and assumptions

有两条公交线路都可以坐，一条平均每 10 分钟来一辆，另一条平均每 20 分钟来一辆。两条线路独立，并且各自到站遵循泊松过程。你在与公交独立的时刻到达，哪辆先来就坐哪辆，求期望等待时间。

只有平均到站间隔不足以决定答案；这里明确采用独立泊松到站假设，而不是固定时刻表或其他间隔分布。

### 1. 把平均时间换成速率

令 $`T_1,T_2`$ 为你到站后，两条线路分别还要等的时间。指数分布的参数使用 rate convention：

```math
T_1\sim Exp(\lambda_1),\quad \lambda_1=\frac1{10},
\qquad
T_2\sim Exp(\lambda_2),\quad \lambda_2=\frac1{20}.
```

时间单位是分钟，速率单位是每分钟。由于泊松过程的独立增量和指数分布的无记忆性，独立到达后的剩余等待仍具有上述分布。

### 2. 为什么生存概率可以相乘？

实际等待时间为

```math
W=\min(T_1,T_2).
```

“等了 $`t`$ 分钟还没坐上车”意味着“两条线路的车都还没来”，所以事件满足

```math
\{W\gt t\}=\{T_1\gt t\}\cap\{T_2\gt t\}.
```

两条线路独立，因此两个事件同时发生的概率等于概率之积：

```math
P(W\gt t)=P(T_1\gt t)P(T_2\gt t).
```

对指数分布，$`P(T_i\gt t)=e^{-\lambda_i t}`$。逐项代入得到

```math
P(W\gt t)
=e^{-t/10}e^{-t/20}
=e^{-(1/10+1/20)t},\qquad t\ge0.
```

最后一步使用 $`e^a e^b=e^{a+b}`$。所得生存函数仍是指数形式，因此最小值的速率是两条线路的速率之和：

```math
W\sim Exp\left(\frac1{10}+\frac1{20}\right),
\qquad
\boxed{E[W]=\frac{1}{1/10+1/20}
=\frac{20}{3}\text{ minutes}.}
```

即 **6 分 40 秒**。

### 3. “每辆概率相同”要明确选择规则

如果哪辆先来就坐哪辆，两条线路先来的概率并不相同。由指数时钟竞争的速率占比公式：

```math
P(T_1\lt T_2)=\frac{1/10}{1/10+1/20}=\frac23,
\qquad
P(T_2\lt T_1)=\frac{1/20}{1/10+1/20}=\frac13.
```

如果“概率相同”指先各以一半概率选定一条线路，然后只等选中的那条，即使另一条先来也不坐，那么这是先选择再等待的混合模型：

```math
\boxed{E[W_{\rm choose}]
=\frac12\times10+\frac12\times20
=15\text{ minutes}.}
```

这个选择规则与“两个时钟同时竞争，取最小值”不同。

### 4. 与单辆环线公交题对照

| 场景 | 对象与抽样规则 | 期望等待 |
| --- | --- | --- |
| 单辆环线车，每圈 10 或 20 分钟，各一半 | 随机到达，先按长度加权，再取间隔内剩余时间 | 8 分 20 秒 |
| 两条独立泊松线路，平均间隔 10、20 分钟 | 两个指数时钟同时竞争，谁先来就坐谁 | 6 分 40 秒 |
| 同样的泊松线路，先各以一半概率选定一条 | 只等选中的线路，对其均值加权 | 15 分钟 |

第一行的离散间隔、长度偏差及一般停留概率公式见 [P029 — 单辆环线公交的随机到站问题](../Probability/P029_Random_Inspection_and_Residual_Wait.md#bus-variant--2026-10-30)。

## Assessment history

- [2026-10-09 Q6 — assessment](../../DailyTests/2026-10-09.md#q6--competing-poisson-processes)
