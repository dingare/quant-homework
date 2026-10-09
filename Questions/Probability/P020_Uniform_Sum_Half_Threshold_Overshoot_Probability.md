# P020 — Uniform Sum: Half-Threshold Overshoot Probability

## Metadata

- Category: Probability
- Difficulty: ★★★☆☆
- Interview Relevance: Stopping Times, Conditional Probability, Geometric Probability
- Tags: Uniform Distribution, Convolution, Simplex Volume, Mixed Distribution, Overshoot
- Date Added: 2026-10-09
- Status: Final

## Core Question

设无限序列 $X_1,X_2,\ldots$ 独立同分布，且 $X_i\sim U(0,1)$。定义

$$
S_0=0,\qquad S_k=\sum_{i=1}^kX_i,\qquad
T=\min\{k\ge1:S_k\gt1/2\}.
$$

求首次越过 $1/2$ 时，部分和已经超过 $1$ 的概率 $P(S_T\gt1)$。

**范围说明：** 本文采用无限序列、持续抽样直到越界的设定。如果原题只给出有限个 $X_1,\ldots,X_n$，需要另外说明未在第 $n$ 步前越界时如何处理，以及是否条件于 $T\le n$；不能直接沿用无限序列的答案。

## Hint

先看停止前的位置 $Y=S_{T-1}$。分别求它的分布，以及给定这个位置、已经知道下一步停止时，越过 $1$ 的条件概率。

## Solution

### 1. 从两个均匀变量之和开始

对 $0\lt y\lt1$，给定 $X_1=x$，要使 $X_1+X_2\le y$，必须有 $0\le x\le y$，并且 $X_2\le y-x$。由于 $X_1$ 的密度为 $1$，

$$
\begin{aligned}
P(S_2\le y)
&=\int_0^y P(X_2\le y-x)f_{X_1}(x)\,dx\\
&=\int_0^y(y-x)\,dx\\
&=\frac{y^2}{2}.
\end{aligned}
$$

所以 CDF 是 $y^2/2$，而密度是其导数：

$$
f_{S_2}(y)=y.
$$

这里 $f_{S_2}(y)=y$ **不是** $P(S_2=y)=y$。连续随机变量在单点的概率为零；密度描述的是小区间概率：

$$
P(y\lt S_2\le y+h)=f_{S_2}(y)h+o(h).
$$

### 2. 用卷积归纳得到一般密度

从 $f_{S_1}(y)=1$ 开始。对 $0\lt y\lt1$，若

$$
f_{S_k}(y)=\frac{y^{k-1}}{(k-1)!},
$$

则由 $S_k$ 与 $X_{k+1}$ 独立，

$$
\begin{aligned}
f_{S_{k+1}}(y)
&=\int_0^y f_{S_k}(t)f_{X_{k+1}}(y-t)\,dt\\
&=\int_0^y\frac{t^{k-1}}{(k-1)!}\,dt\\
&=\frac{y^k}{k!}.
\end{aligned}
$$

积分上下限来自 $t\ge0$ 与 $y-t\ge0$；在这个范围内 $y-t\lt1$，均匀密度等于 $1$。因此

$$
\boxed{f_{S_k}(y)=\frac{y^{k-1}}{(k-1)!}},
\qquad k\ge1,\quad 0\lt y\lt1.
$$

相应地，$P(S_k\le y)=y^k/k!$。因为增量非负，

$$
P(T\gt k)=P(S_k\le1/2)=\frac{(1/2)^k}{k!}\longrightarrow0.
$$

所以 $T$ 几乎必然有限。

### 3. 停止前的位置是混合分布

令 $Y=S_{T-1}$。当第一步就停止时，$Y=S_0=0$，故

$$
P(Y=0)=P(T=1)=P(X_1\gt1/2)=\frac12.
$$

这是 $Y$ 在零点的原子质量（atom）。

再看 $0\lt y\lt1/2$。对固定的 $k\ge1$，若 $S_k=y$，由于部分和单调，前 $k$ 步都没有越过 $1/2$。恰好在下一步停止的条件是

$$
X_{k+1}\gt\frac12-y,
$$

其概率为 $1/2+y$。因此，对足够小且留在区间内的 $dy$，联合事件的概率密度贡献为

$$
P(Y\in[y,y+dy],T=k+1)
=f_{S_k}(y)\left(\frac12+y\right)dy+o(dy).
$$

按互斥的停止时刻求和，得到连续部分的密度：

$$
\begin{aligned}
f_Y(y)
&=\sum_{k=1}^{\infty}\frac{y^{k-1}}{(k-1)!}
\left(\frac12+y\right)\\
&=e^y\left(\frac12+y\right),
\qquad 0\lt y\lt\frac12.
\end{aligned}
$$

非负项允许交换求和与积分。注意这里只给出了连续部分；它的积分等于 $1/2$：

$$
\int_0^{1/2}e^y\left(\frac12+y\right)\,dy
=\left[e^y\left(y-\frac12\right)\right]_0^{1/2}
=\frac12.
$$

加上 $P(Y=0)=1/2$，总质量才是 $1$。

### 4. 给定停止前位置后的条件概率

给定 $Y=y$ 已经包含了“下一次抽样使过程停止”的信息。因此被选中的 $X_T$ 服从截断均匀分布：

$$
X_T\mid Y=y\sim U\left(\frac12-y,1\right).
$$

严格说，在连续部分使用的是正则条件分布；上述规律也可以先对每个 $T=k+1$ 条件化，再混合，因为各个 $k$ 给出相同的截断区间。

停止要求 $X_T\gt1/2-y$，而 $S_T\gt1$ 要求 $X_T\gt1-y$。均匀分布下，条件概率等于区间长度之比：

$$
\begin{aligned}
P(S_T\gt1\mid Y=y)
&=\frac{\text{length of }(1-y,1)}
{\text{length of }(1/2-y,1)}\\
&=\frac{y}{1/2+y}.
\end{aligned}
$$

当 $y=0$ 时，该概率为 $0$：第一步抽样不会超过 $1$。

### 5. 对停止前位置取平均

零点原子的贡献为零，因此

$$
\begin{aligned}
P(S_T\gt1)
&=\frac12\cdot0+
\int_0^{1/2}\frac{y}{1/2+y}
e^y\left(\frac12+y\right)\,dy\\
&=\int_0^{1/2}ye^y\,dy\\
&=\left[(y-1)e^y\right]_0^{1/2}\\
&=\boxed{1-\frac{\sqrt e}{2}}
\approx0.175639.
\end{aligned}
$$

### 6. 用联合事件直接核对

也可以不显式引入 $Y$ 的条件分布。对 $k\ge1$，$S_k=y\lt1/2$ 且 $X_{k+1}\gt1-y$ 已经保证下一步停止，并且超过 $1$。后一个事件的概率为 $y$，所以

$$
\begin{aligned}
P(S_T\gt1)
&=\sum_{k=1}^{\infty}\int_0^{1/2}
\frac{y^{k-1}}{(k-1)!}\,y\,dy\\
&=\int_0^{1/2}ye^y\,dy.
\end{aligned}
$$

这说明上一种方法中的停止概率因子 $1/2+y$，为什么恰好与条件概率的分母抵消。

## Key Knowledge Points

- 非负增量保证：当前部分和未越界，就意味着过去所有部分和都未越界。
- 固定时刻的 $S_k$ 与随机时刻前的位置 $Y$ 不是同一个分布；后者必须乘上下一步停止的概率，再按时刻求和。
- $Y$ 同时包含零点原子与连续部分。
- 原始抽样独立，不代表由停止规则选出的 $X_T$ 与 $Y$ 独立。
- 概率密度必须乘区间宽度后才能解释为局部概率。

## Intuition

$Y=y$ 越大，越过 $1$ 所需的最后一步就越短。但我们已经知道最后一步足以越过 $1/2$，因此比较的样本空间只剩 $(1/2-y,1)$。

例如 $y=1/4$ 时，停止要求最后一步大于 $1/4$，成功要求大于 $3/4$。可行区间长度为 $3/4$，成功区间长度为 $1/4$，条件成功概率为 $1/3$。

## Geometry

### 从三角形到单纯形

由于联合密度为 $1$，独立均匀抽样的概率就是单位立方体内相应区域的体积。

| 变量数 | 区域 | 几何量 |
| --- | --- | --- |
| $1$ | $0\le x_1\le y$ | 线段长度 $y$ |
| $2$ | $x_1,x_2\ge0,\ x_1+x_2\le y$ | 直角三角形面积 $y^2/2$ |
| $3$ | $x_1,x_2,x_3\ge0,\ x_1+x_2+x_3\le y$ | 四面体体积 $y^3/6$ |
| $k$ | $x_i\ge0,\ \sum_{i=1}^kx_i\le y$ | $k$ 维单纯形体积 $y^k/k!$ |

二维中，三角形顶点是 $(0,0),(y,0),(0,y)$，两条直角边长度均为 $y$。这直接给出 CDF $y^2/2$，对 $y$ 求导就得到密度 $y$。

当 $y\lt1$ 时，和不超过 $y$ 自动保证每个坐标都小于 $1$，所以整个单纯形都在单位立方体内部。标准单纯形的体积为 $1/k!$；把每条坐标轴缩放到原来的 $y$ 倍，体积乘上 $y^k$：

$$
P(S_k\le y)=\frac{y^k}{k!},
\qquad
f_{S_k}(y)=\frac{d}{dy}\frac{y^k}{k!}
=\frac{y^{k-1}}{(k-1)!}.
$$

### 切片就是卷积

固定最后一个坐标 $x_{k+1}=x$，其余坐标允许的区域是一个阈值为 $y-x$ 的 $k$ 维单纯形。把这些切片叠起来：

$$
P(S_{k+1}\le y)
=\int_0^y\frac{(y-x)^k}{k!}\,dx
=\frac{y^{k+1}}{(k+1)!}.
$$

这就是 CDF 递推的几何版本；对阈值求导便与密度卷积一致。

密度也可以理解为两层相邻单纯形之间的“薄壳体积除以阈值增量”。不要直接把斜截面的欧氏面积当成密度：阈值增加 $dy$ 时，平面 $\sum x_i=y$ 的法向位移是 $dy/\sqrt{k}$，还需要这个几何因子。

## Common Mistakes

- **漏掉原子：** 把连续密度的积分误认为必须等于 $1$，忽略第一步停止时 $Y=0$ 的概率 $1/2$。
- **忽略选择条件：** 直接写 $X_T\mid Y=y\sim U(0,1)$，从而把条件成功概率写成 $y$。
- **混淆联合与条件：** 固定 $S_k=y$ 时，下一步超过 $1-y$ 的概率确实是 $y$；但给定 $Y=y$ 已经条件于停止，要除以 $1/2+y$。
- **密度当概率：** 把 $f_{S_k}(y)$ 当作 $P(S_k=y)$。
- **公式超范围：** 把 $y^k/k!$ 用于 $y\gt1$，忽略单纯形被单位立方体的边界截断。
- **有限与无限混用：** 有限抽样次数下存在尚未停止的事件，须明确问题的定义。

## Interview Follow-ups

- 为什么 $T$ 几乎必然有限？使用上面的生存概率趋于零。
- 为什么第一步停止不贡献成功概率？因为 $X_1\le1$ 几乎必然成立。
- 如何不求 $Y$ 的分布就算出答案？使用按 $T=k+1$ 分解的联合事件积分。

## Market / Rates Application

这里的均匀正增量是数学模型。对任何按阈值筛选的观测，使用原始抽样分布前都应检查停止或选择条件；不能把本题的具体概率直接用于市场收益。

## Connections

- [P009 — Uniform Sum Stopping Time and the Overshooting Draw](P009_Uniform_Sum_Stopping_Time_and_Overshooting_Draw.md)：相同的单纯形与卷积工具，求停止时间和越界抽样的期望。
- [P014 — Conditional Expectation Under a Random Stopping Rule](P014_Conditional_Expectation_Under_a_Random_Stopping_Rule.md)：随机停止时刻下的条件化与选择效应。

## What to Remember

$$
P(Y=0)=\frac12,\qquad
f_Y(y)=e^y\left(\frac12+y\right),\quad 0\lt y\lt\frac12.
$$

$$
\boxed{
P(S_T\gt1)=
\int_0^{1/2}\frac{y}{1/2+y}
e^y\left(\frac12+y\right)\,dy
=1-\frac{\sqrt e}{2}
}.
$$
