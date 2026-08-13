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

$$
T_F\sim Exp(4),\qquad T_A\sim Exp(2),\qquad T_C\sim Exp(1).
$$

令 $T=\min(T_F,T_A,T_C)$。已知前 $0.3$ 秒无事件，求 fill 先发生的概率和 $E[T\mid T\gt0.3]$；给定首个事件恰在 $0.8$ 秒发生，求其为 fill 的概率。再将 fill 时钟改为 $Gamma(2,4)$，解释 survival information 如何改变风险竞争。

## Exponential Clocks

总 rate 为 $7$。无记忆性给出

$$
\boxed{P(F\text{ first}\mid T\gt0.3)=\frac47}.
$$

并且

$$
T-0.3\mid T\gt0.3\sim Exp(7),
$$

所以

$$
\boxed{E[T\mid T\gt0.3]=0.3+\frac17\approx0.4429}.
$$

给定首个事件发生于时刻 $t$，fill 的联合密度为 $4e^{-7t}$，任意首事件的密度为 $7e^{-7t}$，故

$$
\boxed{P(F\mid T=t)=\frac47}.
$$

这也说明独立指数时钟中，最短到达时间与赢家身份独立。

## Gamma Fill Clock

若 $T_F\sim Gamma(2,4)$，则

$$
S_F(t)=e^{-4t}(1+4t),
\qquad
f_F(t)=16te^{-4t},
$$

所以 hazard 为

$$
h_F(t)=\frac{16t}{1+4t}.
$$

它从 $h_F(0)=0$ 上升到

$$
h_F(0.3)=\frac{4.8}{2.2}\approx2.182.
$$

在 $0.3$ 时刻刚发生某事件的条件下，该事件为 fill 的局部概率为

$$
\boxed{\frac{h_F(0.3)}{h_F(0.3)+2+1}\approx0.421}.
$$

因此 survival 使 imminent fill 相对初始时刻更可能。这里的比值是局部、条件于短区间内发生事件的概率，并不直接等于“最终 fill 赢得竞争”的全局概率。

## What Breaks

Gamma 分布不满足

$$
P(T_F\gt s+t\mid T_F\gt s)=P(T_F\gt t).
$$

其 residual lifetime 依赖已经存活的年龄，所以不能再用固定 rate 比例描述整个未来。正确对象是随时间变化的 hazard：

$$
P(i\text{ occurs in }[t,t+dt]\mid T\gt t)
\approx h_i(t)dt.
$$

## What to Remember

- 独立 exponentials：最小值 rate 相加，赢家概率为自身 rate 占比。
- non-exponential competing risks：年龄包含信息，应使用 survival function 与 time-dependent hazard。
- inspection paradox 还涉及随机观察时的 length-biased sampling，不能仅靠 memorylessness 一句话代替。

## Connections

- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — 从 exponential race 扩展到 Poisson arrivals、Gamma / Weibull hazards、queue position、inspection paradox 与 phase-type CTMC 的结构化复习卡。
- [SC004 — Competing Exponential Clocks and CTMC Hitting](SC004_Competing_Exponential_Clocks_and_CTMC_Hitting.md) — 状态依赖 rates 和有限状态 first-step analysis。
