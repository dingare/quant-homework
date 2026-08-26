# P011 — 奇环上首次到达时间的奇偶性与奖金归属

## Metadata

- Category: Probability
- Secondary: Random Walks, Hitting Times, Difference Equations, Martingales
- Difficulty: ★★★★☆
- Tags: First-Hitting Parity, Linearity of Expectation, Odd Cycle, First-Step Analysis, Optional Stopping
- Review Priority: High
- Date Added: 2026-08-20
- Status: Final

## Core Question

45 块砖围成一圈，每块有 100 美元。先手从均匀随机选出的砖开始，立即拿走该砖的钱。随后后手先掷公平硬币，令棋子顺时针或逆时针走一步；两人轮流操作。棋子第一次落到尚有钱的砖时，当前玩家拿走钱。直到所有钱被拿完。

求：

1. 两人的期望收益；
2. 先手最终拿得比后手多的概率。

约定初始时刻为 $t=0$。后手走第 1 步，先手走第 2 步，依此类推。

## Answer

先手和后手拿到的砖块数期望分别为

$$
E[N_F]=\frac{1013}{45},
\qquad
E[N_S]=\frac{1012}{45}.
$$

因此期望收益为

$$
\boxed{
E[W_F]=\frac{101300}{45}\text{ 美元}
\approx2251.11\text{ 美元}
}
$$

和

$$
\boxed{
E[W_S]=\frac{101200}{45}\text{ 美元}
\approx2248.89\text{ 美元}
}.
$$

先手严格获胜的概率为

$$
\boxed{P(N_F\gt N_S)=\frac{23}{45}\approx0.5111}.
$$

## Method 1: 整数线提升与均匀覆盖区间

这是本题最短、最适合面试现场的解法。

### 1. 把圆周随机游走提升到整数线

把初始砖记为 $0$，顺时针一步记为 $+1$，逆时针一步记为 $-1$。暂时不对坐标取模，而是在整数线上记录随机游走 $X_t$。

整数线上的已访问点始终构成一个连续区间。覆盖完 45 个圆周位置的时刻，整数线上的极差第一次达到 44。因此终止时访问区间必可唯一写成

$$
\boxed{[-K,\,44-K]},
\qquad
K\in\{0,1,\ldots,44\}.
$$

这里 $K$ 是从起点向逆时针方向达到的最远距离。区间中的 45 个整数模 45 后恰好对应圆周上的 45 块砖。

### 2. 严格证明 $K$ 是均匀分布

固定 $K=k$，记

$$
a=-k,
\qquad
b=44-k.
$$

最终覆盖区间为 $[a,b]$ 有两种互斥方式。

第一种是先到 $a$，再从 $a$ 出发先到 $b$ 而不是 $a-1$。普通赌徒破产概率给出

$$
P_0(T_a\lt T_b)\cdot
P_a(T_b\lt T_{a-1})=
\frac{b}{44}\cdot\frac1{45}.
$$

第二种是先到 $b$，再从 $b$ 出发先到 $a$ 而不是 $b+1$：

$$
P_0(T_b\lt T_a)\cdot
P_b(T_a\lt T_{b+1})=
\frac{k}{44}\cdot\frac1{45}.
$$

两种情况相加，并使用 $b+k=44$，得到

$$
\boxed{
P(K=k)
=\frac{b+k}{44\cdot45}
=\frac1{45}
}.
$$

所以 $K$ 在 $0,1,\ldots,44$ 上严格均匀。这里的均匀性不是仅凭圆周对称性猜出的，而是由两次边界命中概率直接证明的。

### 3. 坐标奇偶性直接决定归属

整数线随机游走每走一步都切换坐标奇偶性，因此从 $X_0=0$ 出发，首次到达整数 $j$ 的时间满足

$$
\boxed{T_j\equiv j\pmod2}.
$$

先手拥有偶数时刻首次访问的砖，所以先手得到区间 $[-K,44-K]$ 中的偶数整数。

- 若 $K$ 为偶数，区间两端均为偶数，45 个连续整数中有 23 个偶数，先手拿 23 块；
- 若 $K$ 为奇数，区间两端均为奇数，其中有 22 个偶数，先手拿 22 块。

在 $0,1,\ldots,44$ 中有 23 个偶数、22 个奇数，故

$$
\boxed{
P(N_F\gt N_S)
=P(K\text{ 为偶数})
=\frac{23}{45}
}.
$$

同时

$$
\begin{aligned}
E[N_F]
&=23\cdot\frac{23}{45}
+22\cdot\frac{22}{45}\\
&=\boxed{\frac{1013}{45}},
\end{aligned}
$$

从而

$$
E[N_S]=45-E[N_F]=\boxed{\frac{1012}{45}}.
$$

这条解法将整题压缩成三步：

$$
\boxed{
\text{提升到整数线}
\rightarrow
K\text{ 均匀}
\rightarrow
\text{坐标奇偶性决定归属}
}.
$$

## Method 2: 逐个目标砖的首次到达奇偶性

下面的方法更长，但能直接推广到非均匀起点、不同目标权重和其他边界条件。

### Step 1: 用首次到达时间的奇偶性编码归属

记随机游走为 $X_t$，目标砖 $v$ 的首次到达时间为

$$
T_v=\inf\{t\ge0:X_t=v\}.
$$

由于初始砖在 $t=0$ 被先手拿走，之后后手走奇数步、先手走偶数步，所以

$$
\boxed{
v\text{ 属于后手}
\iff
T_v\text{ 为奇数}
}.
$$

同理，$T_v$ 为偶数时该砖属于先手。这一步把一个双人收集游戏变成了首次到达时间的奇偶性问题。

### Step 2: 固定目标砖，并把环剪成区间

先固定一块目标砖 $v$。把环在 $v$ 处剪开，目标砖的两个副本成为区间端点 $0$ 和 $45$。如果初始砖在剪开后的坐标为 $i$，则

$$
i\in\{0,1,\ldots,44\}.
$$

记

$$
q_i=P_i(T_v\text{ 为奇数}).
$$

从任一端点开始时已经在目标砖上，首次到达时间是 $0$，所以

$$
\boxed{q_0=q_{45}=0}.
$$

这里把同一目标的两个副本放在边界，是将环上的首次到达问题化为有限区间吸收问题的关键。

### Step 3: 首步分析必须翻转奇偶性

从内部点 $i$ 走一步后，剩余首次到达时间若为偶数，总时间才是奇数。因此

$$
q_i
=\frac12(1-q_{i-1})+\frac12(1-q_{i+1}),
$$

即

$$
\boxed{
q_i=1-\frac{q_{i-1}+q_{i+1}}2
},
\qquad 1\le i\le44.
$$

常见错误是写成调和方程 $q_i=(q_{i-1}+q_{i+1})/2$。那个方程追踪的是不随一步而翻转的事件；这里追踪奇偶性，每走一步都要在“奇”和“偶”之间切换。

### Step 4: 平移后解二阶差分方程

令

$$
r_i=q_i-\frac12.
$$

代入递推式得

$$
r_{i+1}+2r_i+r_{i-1}=0.
$$

特征方程为

$$
\lambda^2+2\lambda+1=(\lambda+1)^2=0.
$$

特征根 $-1$ 是二重根，因此通解不是只有 $A(-1)^i$，而是

$$
\boxed{r_i=(A+Bi)(-1)^i}.
$$

由 $q_0=q_{45}=0$，即 $r_0=r_{45}=-1/2$，得到

$$
A=-\frac12,
\qquad
B=\frac1{45}.
$$

所以

$$
\boxed{
q_i=\frac12+(-1)^i\left(\frac{i}{45}-\frac12\right)
}.
$$

等价地，

$$
q_i=
\begin{cases}
\dfrac{i}{45},&i\text{ 为偶数},\\
1-\dfrac{i}{45},&i\text{ 为奇数}.
\end{cases}
$$

### Step 5: 线性期望，不需要砖块之间独立

对每块砖 $v$ 定义后手归属指示变量

$$
I_v=\mathbf1\{T_v\text{ 为奇数}\}.
$$

后手拿到的砖块总数为

$$
N_S=\sum_v I_v.
$$

由于起点均匀随机，对固定目标砖，剪开后的 $i$ 在 $0,1,\ldots,44$ 上均匀。因此

$$
P(v\text{ 属于后手})
=\frac1{45}\sum_{i=0}^{44}q_i.
$$

偶数 $i=2,4,\ldots,44$ 的贡献为

$$
\sum_{j=1}^{22}\frac{2j}{45}=\frac{506}{45},
$$

奇数 $i=1,3,\ldots,43$ 的贡献也为

$$
\sum_{j=1}^{22}\left(1-\frac{2j-1}{45}\right)=\frac{506}{45}.
$$

故

$$
P(v\text{ 属于后手})=\frac{1012}{2025}.
$$

由线性期望，完全不需要各砖归属独立：

$$
E[N_S]
=45\cdot\frac{1012}{2025}
=\frac{1012}{45}.
$$

总砖数为 45，所以

$$
E[N_F]=45-E[N_S]=\frac{1013}{45}.
$$

### Step 6: 为什么最终只可能是 23 比 22

设最后一块被访问的砖为 $L$。在它被访问前，其余 44 块构成一条路径，而路径是二分图。

随机游走在二分图上每走一步必定切换颜色。因此，从初始砖出发，路径上每个顶点的首次到达时间奇偶性完全由其二分颜色决定。44 个顶点的路径两种颜色各有 22 个，所以在最后一块被拿走前，双方恰好各有 22 块。

最后一块必然让其中一人得到第 23 块。因此

$$
N_F\in\{22,23\},
$$

且先手获胜等价于 $N_F=23$。令 $p=P(N_F=23)$，则

$$
E[N_F]=22(1-p)+23p=22+p.
$$

结合 $E[N_F]=1013/45$，得到

$$
p=\frac{1013}{45}-22=\boxed{\frac{23}{45}}.
$$

这也提供了强力校验：后手获胜概率为 $22/45$，而双方不可能平局。

## Martingale / Optional Stopping: 能做什么，不能做什么

对公平随机游走，$X_t$ 是鞅；在有限区间吸收时，可选停止能给出普通的赌徒破产边界命中概率。例如从 $i$ 出发先到 $45$ 而不是 $0$ 的概率是 $i/45$。鞅也能帮助计算期望吸收时间。

但“从哪个边界退出”与“在奇数还是偶数时退出”是两个不同的问题。裸用 $X_t$ 或标准赌徒破产公式会把时间奇偶性丢掉，因而不能直接决定砖块归属。

正确补救有两种等价观点：

1. 扩充状态为 $(X_t,t\bmod2)$，在位置之外保留奇偶状态；
2. 使用带符号的量，例如 $(-1)^t$ 乘以适当的空间函数，再做首步分析或构造鞅。

因此本题的准确结论是：

$$
\boxed{
\text{普通赌徒破产鞅解决边界命中；归属问题还需要奇偶状态。}
}
$$

可选停止不是无效，而是原始状态描述不够丰富。扩充状态后，鞅方法与上面的差分方程方法会给出同一答案。

## General Odd Cycle: $n=2m+1$

把 45 换成任意奇数 $n=2m+1$。相同推导给出

$$
q_i=\frac12+(-1)^i\left(\frac{i}{n}-\frac12\right),
\qquad 0\le i\le n.
$$

固定目标砖属于后手的概率为

$$
\frac1n\sum_{i=0}^{n-1}q_i
=\frac{2m(m+1)}{n^2}
=\frac{n^2-1}{2n^2}.
$$

因此

$$
\boxed{
E[N_F]=\frac n2+\frac1{2n},
\qquad
E[N_S]=\frac n2-\frac1{2n}
}.
$$

去掉最后访问的顶点后，剩余 $2m$ 个顶点构成一条路径，双方各拿 $m$ 块；最后一块决定胜负。所以

$$
\boxed{
P(N_F\gt N_S)=\frac{m+1}{2m+1}=\frac{n+1}{2n}
}.
$$

先手优势只有 $1/n$ 块的期望差，随环变大而消失，但在有限奇环上严格为正。

## Common Mistakes

- 忽略初始砖对应 $t=0$，把先后手奇偶性倒置。
- 对 $q_i$ 写普通调和方程，忘记一步之后奇偶性翻转。
- 剪环后只设一个吸收端点；目标砖应同时对应 $0$ 和 $45$。
- 二重根 $-1$ 只写 $A(-1)^i$，漏掉 $Bi(-1)^i$。
- 为使用线性期望而错误地假设各砖归属独立。
- 仅用 $X_t$ 的可选停止，误以为普通边界命中概率已经回答奇偶归属。
- 只算期望就猜胜率；还必须先证明最终块数只可能是 22 和 23。

## Practice Variants

1. 在长度为 $N$ 的区间上，分别求从 $i$ 出发在奇数时刻和偶数时刻先到右端点的概率。
2. 把硬币改成偏置概率 $p$；写出含奇偶状态的两组首步方程，并比较普通赌徒破产概率。
3. 对偶环 $n=2m$ 重做分析，说明二分结构为何使所有顶点归属由起点颜色决定，并检查是否可能平局。
4. 求公平随机游走吸收时间的概率母函数 $E_i[z^T]$；令 $z=-1$ 提取时间奇偶信息。
5. 构造位置与奇偶性的乘积鞅，并说明应用可选停止所需的有界性或可积性条件。
6. 将每块奖金改成不同权重 $w_v$，用指示变量和线性期望求双方期望收益。

## Connections

- [P002 — Optional Stopping, Fair Games, and Why Stop-Loss Does Not Create Alpha](P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md)
- [P007 — Unequal-Jump Random Walk and First-Step Analysis](P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md)
- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md)
- [Second-Order Difference Equations for Random-Walk Hitting Problems](../../KnowledgeCards/Probability/Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md)
- [首次命中、奇偶增强、覆盖与轮流归属框架](../../KnowledgeCards/Probability/First_Hitting_Parity_Coverage_and_Alternating_Ownership.md)

## What to Remember

$$
\boxed{
\text{首选：整数线覆盖区间与 }K\text{ 的均匀性}
}
$$

$$
\boxed{
\text{通用：归属}=\text{首次到达时间奇偶性}
\rightarrow
\text{剪环成区间}
\rightarrow
\text{奇偶翻转递推}
\rightarrow
\text{线性期望}
}
$$

普通边界命中只需要位置；谁拿到奖金还需要时间奇偶性。
