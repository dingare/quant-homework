# Waiting Time and Competing Risks Cookbook

## Purpose

这张卡片把 Quant 面试中常见的等待时间问题放进同一个框架：先区分“单个时钟的寿命分布”和“多个原因的竞争”，再判断时钟是否无记忆、是否需要记录年龄或阶段。

## Compact Concept Map

$$
\text{Poisson counts}
\longleftrightarrow
\text{exponential interarrival times}
\longrightarrow
\text{competing exponential clocks}
$$

$$
\text{kth arrival}
\longleftrightarrow
Gamma(k,\lambda)
\longleftrightarrow
\text{k sequential exponential phases}
\longrightarrow
\text{phase-type CTMC}
$$

$$
\text{nonconstant hazard}
\longrightarrow
\text{age matters}
\longrightarrow
\text{non-exponential competing risks}
\longrightarrow
\text{queue age / execution risk}
$$

随机时点观察还会引入另一条路径：

$$
\text{random inspection}
\longrightarrow
\text{length bias}
\longrightarrow
\text{inspection paradox}.
$$

## 1. Universal Survival and Hazard Toolkit

对非负等待时间 $T$，定义

$$
S(t)=P(T\gt t),
\qquad
f(t)=-S'(t),
\qquad
h(t)=\frac{f(t)}{S(t)}.
$$

$h(t)dt$ 是在已存活到 $t$ 的条件下，未来极短区间内发生事件的近似概率。累计 hazard 为

$$
H(t)=\int_0^t h(u)\,du,
$$

且

$$
\boxed{S(t)=e^{-H(t)}}.
$$

### Recognition cues

- 题目给 density 或 survival：先计算 hazard。
- 题目说“已经等了 $s$”：检查 residual lifetime 是否依赖 $s$。
- 题目问“下一瞬间哪个事件发生”：比较当前 hazards。
- 题目问“最终哪个原因先发生”：对 cause-specific density 积分，不能只看某一时点的 hazard share。

## 2. Competing Exponentials

若独立时钟

$$
T_i\sim Exp(\lambda_i),
\qquad
T=\min_iT_i,
$$

令 $\Lambda=\sum_i\lambda_i$，则

$$
\boxed{T\sim Exp(\Lambda)},
\qquad
\boxed{P(T_i=T)=\frac{\lambda_i}{\Lambda}}.
$$

首达时间 $T$ 与赢家身份独立。由于无记忆性，给定 $T\gt s$ 后，剩余等待时间仍为 $Exp(\Lambda)$，赢家概率仍为 $\lambda_i/\Lambda$。

### Interview variants

- 多个交易所谁先 fill；fill、cancel、adverse move 谁先发生。
- 已等待一段时间后，剩余期望时间是多少。
- 给定首事件恰在 $t$ 发生，判断事件类型。
- 状态切换后 rates 改变：转为 CTMC first-step analysis。

详见 [SC006 — Competing Exponentials and Time-Dependent Hazards](../../Questions/StochasticCalculus/SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md) 与 [SC004 — Competing Exponential Clocks and CTMC Hitting](../../Questions/StochasticCalculus/SC004_Competing_Exponential_Clocks_and_CTMC_Hitting.md)。

## 3. Non-Exponential Competing Risks

若 $T_1,\ldots,T_m$ 独立但不必为 exponential，则总体 survival 为

$$
S_{\min}(t)=\prod_{j=1}^mS_j(t),
$$

原因 $i$ 在时刻 $t$ 首先发生的 density 为

$$
g_i(t)=f_i(t)\prod_{j\ne i}S_j(t)
=h_i(t)\prod_{j=1}^mS_j(t).
$$

因此最终由原因 $i$ 获胜的概率是

$$
\boxed{P(i\text{ wins})=\int_0^\infty g_i(t)\,dt}.
$$

而给定在时刻 $t$ 附近确有事件发生，其类型为 $i$ 的局部概率为

$$
\boxed{\frac{h_i(t)}{\sum_jh_j(t)}}.
$$

这两个量必须区分：前者是全局累计概率，后者是时刻 $t$ 的局部 hazard share。

## 4. Gamma and Weibull Hazard Behavior

### Gamma / Erlang

若 $T\sim Gamma(k,\lambda)$，其中 $k$ 为正整数，则可理解为 $k$ 个独立 $Exp(\lambda)$ 阶段之和。$k=1$ 才具有无记忆性；当 $k\gt1$ 时，hazard 通常随年龄上升。

例如 $Gamma(2,\lambda)$：

$$
S(t)=e^{-\lambda t}(1+\lambda t),
\qquad
h(t)=\frac{\lambda^2t}{1+\lambda t}.
$$

### Weibull

若 Weibull 的 shape 为 $k$、scale 为 $\eta$，则

$$
h(t)=\frac{k}{\eta}\left(\frac{t}{\eta}\right)^{k-1}.
$$

- $k\gt1$：increasing hazard，等待越久越接近发生。
- $k=1$：constant hazard，即 exponential。
- $k\lt1$：decreasing hazard，能存活到较晚的对象往往更“耐久”。

### Recognition cues

- 多阶段审批、排队推进、累计若干次成交：Gamma / phase-type。
- 设备老化、订单优先级积累：increasing hazard。
- 异质订单混合、早期高淘汰率：decreasing hazard。

## 5. Poisson Process and the Kth-Arrival Link

对 rate 为 $\lambda$ 的 Poisson process $N(t)$，

$$
N(t)\sim Poisson(\lambda t).
$$

相邻到达间隔独立且服从 $Exp(\lambda)$。第 $k$ 次到达时间

$$
T_k=E_1+\cdots+E_k,
\qquad E_i\sim Exp(\lambda),
$$

所以

$$
\boxed{T_k\sim Gamma(k,\lambda)},
\qquad
E[T_k]=\frac{k}{\lambda},
\qquad
Var(T_k)=\frac{k}{\lambda^2}.
$$

等价关系为

$$
\boxed{P(T_k\le t)=P(N(t)\ge k)}.
$$

面试中若题目从“等多久”切换到“时间窗内发生多少次”，这条 duality 通常是最快入口。

## 6. Queue Position and Execution

最简 queue 模型中，若从当前 queue position 到本单完成共需要 $q$ 次队列消耗，且消耗由 rate $\lambda$ 的 Poisson process 驱动，则 fill time 是第 $q$ 次消耗到达时间：

$$
T_{\rm fill}\sim Gamma(q,\lambda).
$$

这解释了为什么排队成交时间通常不是 exponential：订单需要多个阶段完成，queue position 是隐藏状态。

更现实的模型需要加入：

- 前方订单 cancellation；
- 新订单插入或 queue replenishment；
- partial fills 和不同 size；
- market regime 改变 rates；
- adverse move 与 voluntary cancellation 的 competing clocks。

此时状态可取“当前 queue position + market regime”，用 CTMC 或 Markov-modulated queue 做 first-step analysis。执行决策还要平衡等待风险和冲击成本，可连接 [O004 — Optimal Execution with Impact and Inventory Risk](../../Questions/Optimization/O004_Optimal_Execution_with_Impact_and_Inventory_Risk.md)。

## 7. Inspection Paradox and Length Bias

“从事件开始计时”与“随机时点看到一个正在进行的区间”不是同一种抽样。

若 renewal interval 长度为 $X$，随机检查落入长度为 $x$ 的区间的概率与 $x$ 成正比，因此 observed interval 的 length-biased density 为

$$
f_{\rm obs}(x)=\frac{xf_X(x)}{E[X]}.
$$

故

$$
E[X_{\rm obs}]=\frac{E[X^2]}{E[X]}.
$$

在平稳 renewal process 中，随机检查后的平均 residual waiting time 为

$$
\boxed{E[R]=\frac{E[X^2]}{2E[X]}}.
$$

高方差使随机观察更容易命中长区间，这就是 inspection paradox。Exponential 是特殊情形：无记忆性使 $E[R]=E[X]=1/\lambda$，但 length-biased interval 本身仍不同于原始 interval。

## 8. Phase-Type and Markov-Chain Framing

Phase-type distribution 是有限状态 CTMC 到达吸收态的时间分布。设初始 transient-state row vector 为 $\alpha$，transient generator 为 $Q$，$\mathbf1$ 为全 $1$ 向量，则

$$
S(t)=\alpha e^{Qt}\mathbf1,
$$

$$
f(t)=\alpha e^{Qt}(-Q\mathbf1),
$$

$$
\boxed{E[T]=-\alpha Q^{-1}\mathbf1}.
$$

Erlang 是一串顺序阶段；hyperexponential 是初始时随机选择不同 rate 的阶段。Phase-type 的优势是把 non-exponential waiting time 变成更大状态空间中的 Markov problem。

### Recognition cues

- “还差几步完成”是状态：顺序 phase / Erlang。
- “属于哪种隐藏流动性类型”是状态：mixture / hyperexponential。
- 状态和事件 rate 随 market regime 改变：Markov-modulated CTMC。
- 问 eventual absorption probability 或 expected time：写 first-step linear system。

## 9. Common Interview Questions

1. 证明独立 exponential clocks 的最小值与赢家身份独立。
2. 已知订单存活 $s$ 秒，比较 exponential、Gamma 和 Weibull 的 residual lifetime。
3. 求 Gamma fill 与 exponential adverse move 竞争时的全局 fill probability。
4. 从 Poisson count 推导第 $k$ 次到达时间分布。
5. 给定 queue position，求 fill-time mean、variance 和 fill-before-cancel probability。
6. 解释为什么随机观察到的订单寿命比新提交订单的寿命更长。
7. 把 Gamma 或多阶段 execution model 写成有限状态 CTMC。
8. 区分 local hazard share、cumulative incidence 与 unconditional event probability。

## 10. Fast Interview Checklist

1. 明确计时起点：从 inception 开始，还是随机时点检查。
2. 写出每个时钟的 $S_i(t)$、$f_i(t)$、$h_i(t)$。
3. 判断是否 exponential；只有 exponential 才能无条件使用 memorylessness。
4. 问“下一瞬间”用 hazard；问“最终谁赢”对 cause-specific density 积分。
5. 看是否存在 queue position、remaining phases 或 market regime 等隐藏状态。
6. 若是 Poisson counts，尝试切换到 arrival times；反之亦然。
7. 用概率范围、零年龄极限、长期 hazard 和量纲做 sanity check。

## Connections

- [SC006 — Competing Exponentials and Time-Dependent Hazards](../../Questions/StochasticCalculus/SC006_Competing_Exponentials_and_Time_Dependent_Hazards.md) — exponential 与 Gamma hazard 的核心例题。
- [SC004 — Competing Exponential Clocks and CTMC Hitting](../../Questions/StochasticCalculus/SC004_Competing_Exponential_Clocks_and_CTMC_Hitting.md) — 状态依赖 rates 与 CTMC first-step analysis。
- [P009 — Uniform Sum Stopping Time and the Overshooting Draw](../../Questions/Probability/P009_Uniform_Sum_Stopping_Time_and_Overshooting_Draw.md) — threshold stopping、tail-sum identity 与 overshoot。
- [P007 — Unequal-Jump Random Walk and First-Step Analysis](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md) — 离散状态 hitting probability 与 expected time。
- [SC003 — Ornstein–Uhlenbeck First Hitting Time](../../Questions/StochasticCalculus/SC003_Ornstein_Uhlenbeck_First_Hitting_Time.md) — 连续过程的 generator boundary-value method。
- [T003 — AR(1) First Passage Time](../../Questions/TimeSeries/T003_AR1_First_Passage_Time_and_Why_Persistence_Changes_Waiting_Time.md) — persistence 对 threshold-crossing time 的影响。
