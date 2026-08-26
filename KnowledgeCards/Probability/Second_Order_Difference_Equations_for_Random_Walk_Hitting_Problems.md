# Second-Order Difference Equations for Random-Walk Hitting Problems

## Purpose

Boundary-hitting probabilities, expected stopping times, discounted hitting quantities, and first-hitting-time parity for random walks can usually be reduced to second-order difference equations by first-step analysis. The core workflow is

$$
\text{define the state quantity}
\rightarrow
\text{write the boundary values}
\rightarrow
\text{apply first-step analysis}
\rightarrow
\text{homogenize the recurrence}
\rightarrow
\text{find the characteristic roots}
\rightarrow
\text{use the boundaries to determine the constants}.
$$

## 1. 先分清所求量

在区间 $\{0,1,\ldots,N\}$ 上，公平随机游走每步以 $1/2$ 向左右移动。令 $T$ 为首次到达端点的时间。

不同问题会产生不同递推：

- 右端先命中概率 $h_i$：

$$
h_i=\frac{h_{i-1}+h_{i+1}}2.
$$

- 期望吸收时间 $e_i$：

$$
e_i=1+\frac{e_{i-1}+e_{i+1}}2.
$$

- 吸收时间为奇数的概率 $q_i$：

$$
q_i=1-\frac{q_{i-1}+q_{i+1}}2.
$$

三者只差一个常数或符号，却对应不同的特解和特征根。不要在未定义状态量时套公式。

## 2. 标准齐次递推

对

$$
a_{i+1}+\alpha a_i+\beta a_{i-1}=0,
$$

尝试 $a_i=\lambda^i$，得到特征方程

$$
\lambda^2+\alpha\lambda+\beta=0.
$$

若有两个不同根 $\lambda_1,\lambda_2$，则

$$
a_i=A\lambda_1^i+B\lambda_2^i.
$$

若有二重根 $\lambda$，则必须写成

$$
\boxed{a_i=(A+Bi)\lambda^i}.
$$

漏掉 $Bi\lambda^i$ 会使两个边界条件通常无法同时满足。

## 3. 非齐次项先找特解或做平移

若递推有常数项，可先找常数或多项式特解。

例如奇偶命中递推

$$
q_i=1-\frac{q_{i-1}+q_{i+1}}2
$$

有常数特解 $q_i=1/2$。令

$$
r_i=q_i-\frac12,
$$

便得到

$$
r_{i+1}+2r_i+r_{i-1}=0.
$$

特征方程为 $(\lambda+1)^2=0$，所以

$$
r_i=(A+Bi)(-1)^i.
$$

负根产生交替符号，正是时间奇偶信息在空间递推中的痕迹。

## 4. 边界值是解的一部分

差分方程本身不会决定常数。必须先写清吸收边界代表什么。

例如目标位于区间两端时，若 $q_i$ 表示首次到达目标的时间为奇数，则

$$
q_0=q_N=0,
$$

因为从边界出发的首次到达时间为 $0$，是偶数。

若 $h_i$ 表示先到右端点的概率，则边界应为

$$
h_0=0,
\qquad
h_N=1.
$$

同一随机游走因问题定义不同而有不同边界值。

## 5. 概率母函数统一多个问题

定义带终点事件的母函数

$$
F_i(z)=E_i\left[z^T\mathbf1\{X_T=N\}\right].
$$

首步分析给出

$$
F_i(z)=\frac z2\left(F_{i-1}(z)+F_{i+1}(z)\right).
$$

不同的 $z$ 提取不同信息：

- $z=1$ 给普通右端命中概率；
- 对 $z$ 求导并令 $z=1$ 可关联命中时间矩；
- $z=-1$ 给带符号的奇偶差 $E_i[(-1)^T\mathbf1\{X_T=N\}]$。

所以“奇偶增强”并非独立技巧，而是吸收时间概率母函数在 $z=-1$ 的特例。

## 6. 与鞅方法的关系

对公平随机游走，位置过程 $X_t$ 是鞅。可选停止通常能快速求普通边界命中概率，但它不会自动保留 $T\bmod2$。

若问题涉及奇偶性、折现或路径标记，需要：

- 扩充状态，例如 $(X_t,t\bmod2)$；或
- 构造包含 $(-1)^t$ 或 $z^t$ 的新鞅。

差分方程和鞅并非竞争方法：前者系统地写出边值问题，后者在找到正确状态量或调和函数时给出简洁证明。

## 7. Verification Checklist

1. 边界值是否与事件定义一致？
2. 期望时间递推是否保留了当步的 $+1$？
3. 奇偶事件走一步后是否做了补集翻转？
4. 非齐次方程是否先平移或加入特解？
5. 二重特征根是否包含线性因子 $i$？
6. 解是否落在概率的 $[0,1]$ 范围内？
7. 是否代回递推和两个边界逐项检查？

## 8. Practice Map

- 普通赌徒破产：根 $1$ 的结构与线性命中概率。
- 偏置随机游走：两个不同特征根与几何型命中概率。
- 期望吸收时间：常数非齐次项与二次特解。
- 奇偶首次到达：二重根 $-1$ 与交替线性解。
- 不等步长随机游走：更高阶递推、越界与有限状态线性系统。
- 折现停止问题：用 $z^T$ 把时间价值写入递推。

## Connections

- [P011 — 奇环上首次到达时间的奇偶性与奖金归属](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md)
- [P007 — Unequal-Jump Random Walk and First-Step Analysis](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md)
- [P002 — Optional Stopping, Fair Games, and Why Stop-Loss Does Not Create Alpha](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md)
- [首次命中、奇偶增强、覆盖与轮流归属框架](First_Hitting_Parity_Coverage_and_Alternating_Ownership.md)

## What to Remember

$$
\boxed{
\text{先定义事件与边界，再解递推；负根常对应奇偶交替。}
}
$$
