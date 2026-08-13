# P009 — Uniform Sum Stopping Time and the Overshooting Draw

## Metadata

- Category: Probability
- Secondary: Stopping Times, Distribution Recursion, Tail-Sum Identity
- Difficulty: ★★★☆☆
- Tags: Uniform Distribution, Partial Sums, Simplex Volume, Tail Sum, Overshoot
- Review Priority: High
- Date Added: 2026-08-13
- Status: Final

## Core Question

设 $X_1,X_2,\ldots$ 独立同分布，且 $X_i\sim U(0,1)$。令

$$
S_n=\sum_{i=1}^nX_i,
\qquad
N=\min\{n:S_n\gt1\}.
$$

求 $E[N]$，并计算使部分和首次越过 $1$ 的最后一次抽样 $X_N$ 的期望。

## Distribution-Function Recursion

记

$$
F_n(t)=P(S_n\le t).
$$

取 $F_0(t)=1$（$t\ge0$）。当 $0\le t\le1$ 时，对最后一个变量 $X_n$ 条件化：

$$
F_n(t)=\int_0^t F_{n-1}(t-x)\,dx.
$$

由归纳法，若 $F_{n-1}(u)=u^{n-1}/(n-1)!$，则

$$
F_n(t)
=\int_0^t\frac{(t-x)^{n-1}}{(n-1)!}\,dx
=\frac{t^n}{n!}.
$$

因此

$$
\boxed{F_n(t)=\frac{t^n}{n!}},
\qquad 0\le t\le1,
$$

特别地，

$$
\boxed{P(S_n\le1)=\frac1{n!}}.
$$

几何上，这也是单位立方体 $[0,1]^n$ 中单纯形
$x_1+\cdots+x_n\le1$ 的体积。

## Expected Stopping Time

因为每个 $X_i\ge0$，所以在前 $n$ 次抽样后仍未停止，当且仅当 $S_n\le1$：

$$
\{N\gt n\}=\{S_n\le1\}.
$$

对取正整数值的随机变量使用尾和公式，

$$
E[N]
=\sum_{n=0}^{\infty}P(N\gt n)
=\sum_{n=0}^{\infty}P(S_n\le1)
=\sum_{n=0}^{\infty}\frac1{n!}.
$$

故

$$
\boxed{E[N]=e}.
$$

这里 $n=0$ 的一项等于 $1$。由于分布连续，把边界处的 $\le$ 换成 $\lt$ 不影响概率。

## Expected Overshooting Draw

需要区分“越界的那次抽样” $X_N$ 和“超过边界的幅度” $S_N-1$。本题先计算 $E[X_N]$。

当 $n\ge2$ 时，$S_{n-1}$ 在 $0\le s\le1$ 上的密度为

$$
f_{n-1}(s)=F_{n-1}'(s)=\frac{s^{n-2}}{(n-2)!}.
$$

给定 $S_{n-1}=s$，第 $n$ 次恰好停止的条件是 $X_n\gt1-s$。因此该次抽样对无条件期望的贡献为

$$
E\left[X_n\mathbf1_{\{N=n\}}\mid S_{n-1}=s\right]
=\int_{1-s}^1x\,dx
=s-\frac{s^2}{2}.
$$

等价地，停止概率为 $s$，而条件均值为

$$
E[X_n\mid N=n,S_{n-1}=s]
=\frac{1+(1-s)}2
=1-\frac s2,
$$

两者相乘仍是 $s-s^2/2$。于是

$$
\begin{aligned}
E[X_N]
&=\sum_{n=2}^{\infty}\int_0^1
\left(s-\frac{s^2}{2}\right)
\frac{s^{n-2}}{(n-2)!}\,ds\\
&=\int_0^1\left(s-\frac{s^2}{2}\right)e^s\,ds\\
&=1-\frac12(e-2).
\end{aligned}
$$

所以

$$
\boxed{E[X_N]=2-\frac e2\approx0.6409}.
$$

作为交叉检查，Wald 等式给出

$$
E[S_N]=E[N]E[X_1]=\frac e2,
$$

因此平均越界幅度为

$$
E[S_N-1]=\frac e2-1.
$$

## Important Correction

$e-\frac52\approx0.2183$ **不是** $E[X_N]$。事实上，仅 $N=2$ 这一项对 $E[X_N]$ 的贡献已经是

$$
\int_0^1\int_{1-s}^1x\,dx\,ds=\frac13,
$$

大于 $e-\frac52$。常见错误是在对 $S_{n-1}$ 积分时漏掉其密度，或把条件期望、联合事件的期望贡献与越界幅度混为一谈。

## Key Knowledge Points

- 单调部分和把生存事件直接化为 $\{N\gt n\}=\{S_n\le1\}$。
- 尾和公式把停止时间期望化为生存概率之和。
- $P(S_n\le1)=1/n!$ 既可由分布函数递推得到，也可解释为单纯形体积。
- 计算随机索引处的 $X_N$ 时，应按停止时刻分解，并保留 $S_{n-1}$ 的密度权重。
- $X_N$、$S_N$ 与越界幅度 $S_N-1$ 是三个不同的随机量。

## Common Mistakes

- 把 $E[N]$ 的尾和从 $n=1$ 开始，漏掉 $P(N\gt0)=1$。
- 忘记只有在 $0\le t\le1$ 时，$F_n(t)=t^n/n!$ 才能直接使用。
- 给定 $S_{n-1}=s$ 后，只写条件均值，却漏乘停止概率 $P(X_n\gt1-s)=s$。
- 把最后一次抽样的期望误写为 $e-5/2$。

## Quant Interview Probability Checklist

遇到概率面试题时，先识别结构，再选择工具；不要一开始就枚举或套公式。

### 1. 停止时间与阈值和

- **识别信号：** “第一次超过”“直到累计值达到”“首次触碰边界”。
- **首选工具：** 定义停止时间，先写生存事件 $\{N\gt n\}$；检查增量是否非负，以及是否存在 overshoot。
- **例题：** 独立 $U(0,1)$ 抽样之和首次超过常数 $a$，求期望抽样次数。

### 2. 条件期望与递推

- **识别信号：** 过程分步发生，下一步之后问题与原问题同型；当前状态足以描述未来。
- **首选工具：** 对第一步或最后一步条件化，写 value function；先明确状态、边界条件和递推范围。
- **例题：** 掷公平骰子，累计点数首次达到或超过 $20$，求期望掷骰次数。

### 3. 尾和公式

- **识别信号：** 求非负整数值随机变量的期望，而 $P(N\gt n)$ 比 $P(N=n)$ 更容易。
- **首选工具：** 使用

$$
E[N]=\sum_{n=0}^{\infty}P(N\gt n),
$$

并把“尚未停止”翻译成原过程的事件。
- **例题：** 不断抛硬币直到首次出现正面，利用生存概率求等待时间期望。

### 4. 几何概率与均匀和

- **识别信号：** 独立均匀变量受到线性不等式约束，如 $X_1+\cdots+X_n\le t$。
- **首选工具：** 把概率看成单位立方体内区域的体积；对单纯形使用缩放，或写分布函数卷积递推。
- **例题：** 三个独立 $U(0,1)$ 变量之和不超过 $1$ 的概率是多少？

### 5. 次序统计量与间距

- **识别信号：** 样本最大值、最小值、第 $k$ 小值，或排序后相邻点之间的距离。
- **首选工具：** 最大值先写 CDF；第 $k$ 个次序统计量用“有多少样本不超过 $x$”；均匀样本的 spacings 联想到 Dirichlet 分布与对称性。
- **例题：** 在 $[0,1]$ 上随机取 $n$ 个点，最靠近 $0$ 的点的期望位置是多少？

### 6. Poisson 与指数过程

- **识别信号：** 固定时间窗内的事件计数、恒定到达率、无记忆等待时间、独立平稳增量。
- **首选工具：** 计数用 Poisson，等待时间用 exponential；多个时钟竞争时用 rates 相加，胜者概率按 rate 占比。
- **例题：** 买单和卖单分别以 rate $\lambda_b$、$\lambda_s$ 到达，下一笔是买单的概率和等待时间期望各是多少？

### 7. 随机游走与赌徒破产

- **识别信号：** 状态按固定跳步变化，问题询问先到哪个边界或到达所需时间。
- **首选工具：** 写 first-step difference equation 和边界条件；只有最近邻 $\pm1$ 情形才直接使用标准 gambler's-ruin 公式，非对称跳跃要处理 overshoot。
- **例题：** 资金每轮以概率 $p$ 增加 $1$、否则减少 $1$，先到 $A$ 而非 $0$ 的概率是多少？

### 8. 模式等待时间与有限状态 Markov 链

- **识别信号：** 等待某个字符串、连续若干次结果，且候选模式可能与自身前后缀重叠。
- **首选工具：** 状态记录“当前后缀与目标模式前缀的最长匹配长度”，再列 first-step 方程；不要假设每个长度为 $m$ 的区块独立。
- **例题：** 连续抛公平硬币，首次出现 HTH 的期望等待时间是多少？

### 面试时的快速执行顺序

1. 定义随机变量、状态与停止事件。
2. 判断求分布、概率还是期望；优先寻找补事件或生存事件。
3. 尝试一次条件化，并检查是否得到闭合递推。
4. 写清边界条件，特别检查 overshoot 与模式重叠。
5. 用极端情形、量纲、上下界或另一种方法做 sanity check。

## What to Remember

$$
\boxed{
P(S_n\le1)=\frac1{n!},
\qquad
E[N]=e,
\qquad
E[X_N]=2-\frac e2
}.
$$
