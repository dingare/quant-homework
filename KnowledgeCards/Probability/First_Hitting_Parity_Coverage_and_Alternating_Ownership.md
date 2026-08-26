# 首次命中、奇偶增强、覆盖与轮流归属框架

## Purpose

这张卡用于识别一类共同骨架：随机游走首次访问位置，访问时刻的奇偶性决定轮到谁，最终收益又是各目标归属的总和。[P011 — 奇环上首次到达时间的奇偶性与奖金归属](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md) 是代表题，但方法也覆盖普通赌徒破产、路径或环的覆盖，以及二阶差分方程。

核心分流是：

$$
\text{只问总数期望}\Rightarrow\text{指示变量与线性期望};
$$

$$
\text{只问边界或平均时间}\Rightarrow\text{首步递推或鞅};
$$

$$
\text{问到达时刻奇偶或轮流归属}\Rightarrow\text{扩充状态或奇偶翻转递推}.
$$

## 1. 基础模板：赌徒破产

在 $\{0,1,\ldots,N\}$ 上令 $X_0=i$，每步以概率 $p$ 右移、概率 $q=1-p$ 左移；$0,N$ 为吸收边界，

$$
T=\inf\{t\ge0:X_t\in\{0,N\}\}.
$$

### 边界命中概率

令 $h_i=P_i(X_T=N)$。首步递推及边界为

$$
h_i=ph_{i+1}+qh_{i-1},
\qquad h_0=0,\quad h_N=1.
$$

公平情形 $p=q=1/2$：

$$
h_i=\frac{i}{N},
\qquad P_i(X_T=0)=1-\frac{i}{N}.
$$

有偏情形 $p\ne q$：

$$
h_i=\frac{1-(q/p)^i}{1-(q/p)^N},
\qquad P_i(X_T=0)=1-h_i.
$$

公平时用鞅 $X_t$；有偏时用指数鞅 $(q/p)^{X_t}$。在有限区间先对 $T\wedge n$ 停止，再利用有界性取极限，是最稳妥的可选停止论证。

### 平均吸收时间

令 $e_i=E_i[T]$。首步递推为

$$
e_i=1+pe_{i+1}+qe_{i-1},
\qquad e_0=e_N=0.
$$

公平情形：

$$
e_i=i(N-i).
$$

这也可由 $X_t^2-t$ 的鞅和可选停止得到。有偏情形令 $\mu=p-q$，则 $X_t-\mu t$ 是鞅；结合 $E_i[X_T]=Nh_i$ 得

$$
e_i=\frac{Nh_i-i}{p-q}
=\frac{i-Nh_i}{q-p}.
$$

这里有限状态、吸收几乎必然且 $E[T]\lt\infty$，因而上述停止可严格化。对无界区域、无界跳跃或可能无限等待的停时，不能只写“由可选停止”；必须检查有界停时、一致可积性或可积支配等条件。参见 [P002](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md)。

### 这套基础模板遗漏什么

$h_i$ 告诉你从哪个边界退出，$e_i$ 告诉你平均多久退出；两者都不告诉你 $T$ 是奇数还是偶数。若轮流行动使归属由 $T\bmod2$ 决定，必须保留时间奇偶状态。

## 2. 四个相连的题型家族

### A. 首次命中与赌徒破产

- **识别信号：** “先到哪条边界”“破产前达到目标”“止盈与止损谁先触发”。
- **标准工具：** $h_i=ph_{i+1}+qh_{i-1}$；平均时间用 $e_i=1+pe_{i+1}+qe_{i-1}$；简单边界优先考虑鞅和可选停止。
- **能捕捉：** 出口身份、命中概率、平均停止时间；处理不等步长和越界时改用有限状态方程，见 [P007](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md)。
- **不能捕捉：** 裸位置状态不记录到达时刻奇偶、访问顺序或完整路径。
- **面试变式：** 偏置硬币、非对称边界、条件命中时间、不等跳步与 overshoot、带漂移布朗运动。

### B. 奇偶增强的命中时间与轮流行动

- **识别信号：** “奇数步或偶数步首次到达”“两人轮流移动”“第几位玩家拿到首次访问奖励”。
- **标准工具：** 状态扩充为 $(X_t,t\bmod2)$；或令 $q_i=P_i(T\text{ 为奇数})$，公平游走时

$$
q_i=1-\frac{q_{i-1}+q_{i+1}}2.
$$

- **鞅角色：** 普通 $X_t$ 不够；需把 $(-1)^t$ 或概率母函数 $z^T$ 加入构造。$z=-1$ 提取奇偶差。
- **能捕捉：** 首次到达的奇偶与交替归属。
- **不能捕捉：** 单个目标的边际归属通常不足以给出各目标间依赖或最终胜率；胜率还需结构约束。
- **面试变式：** 偏置游走的两层奇偶状态、每 $k$ 步轮换、不同玩家权重、给定边界与奇偶的联合概率。

### C. 路径与环上的覆盖或已访问集合

- **识别信号：** “每个点第一次访问时领奖”“直到覆盖全部顶点”“圆环可以剪开或提升到整数线”。
- **标准结构：** 一维游走的已访问集合始终是区间 $[\min X_t,\max X_t]$；环可剪成以目标为两个端点的区间，或提升到整数线研究极差。
- **线性期望角色：** 对目标 $v$ 定义 $I_v=\mathbf1\{v\text{ 归某玩家}\}$，则 $E[\sum_v I_v]=\sum_vP(I_v=1)$，不要求独立。
- **能捕捉：** 期望覆盖收益、最后未访问点、路径的二分颜色约束；在 P011 中，去掉最后一点后得到偶数长度路径，从而最终比分只能相差一。
- **不能捕捉：** 线性期望本身不给方差、联合归属或胜率；必须另证可能比分的支持集，或计算联合概率。
- **面试变式：** 偶环与奇环、加权顶点、非均匀起点、路径 cover time、最后访问点分布、一般图上是否仍能用二分结构。

### D. 二阶差分方程

- **识别信号：** 最近邻首步分析只连接 $i-1,i,i+1$；有两个边界条件。
- **标准工具：** 齐次递推尝试 $a_i=\lambda^i$；非齐次项先找特解或平移。不同根给 $A\lambda_1^i+B\lambda_2^i$；二重根给

$$
a_i=(A+Bi)\lambda^i.
$$

- **在奇偶题中的角色：** 平移 $r_i=q_i-1/2$ 后特征方程为 $(\lambda+1)^2=0$，所以必须保留 $(A+Bi)(-1)^i$。负根对应交替，二重根产生线性包络。
- **能捕捉：** 边界命中、平均时间、折现量、奇偶母函数等边值问题。
- **不能捕捉：** 方程不会替你决定正确的状态、事件和边界；状态漏掉奇偶，解得再漂亮也回答错问题。
- **面试变式：** 偏置游走的几何根、常数非齐次项、重复根、$z^T$ 母函数、更高阶跳步递推。详见 [二阶差分方程卡](Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md)。

## 3. 识别与选法决策树

1. **结果是若干目标奖励之和吗？** 是：先为每个目标设归属指示变量，用线性期望；不要先追联合分布。
2. **单个目标只依赖先到哪个边界吗？** 是：剪图成区间，写普通命中递推；边界简单时用鞅更短。
3. **行动者随步数轮换，或题目问奇偶时刻吗？** 是：立即把 $t\bmod2$ 加入状态，或写“走一步后奇偶翻转”的递推。
4. **问平均停止时间吗？** 在概率递推上加当步的 $+1$；公平时考虑 $X_t^2-t$，有偏时考虑 $X_t-(p-q)t$。
5. **问覆盖路径或环吗？** 检查已访问集是否为区间、能否剪环、是否存在二分颜色或最后顶点结构。
6. **得到最近邻线性递推吗？** 解二阶差分方程；先找特解，再检查重根和两个边界。
7. **想由期望推出胜率吗？** 只有先证明最终取值只有两个可能时才可；否则期望不决定胜率。

## 4. 从简单到复杂的复习路线

| 顺序 | 要掌握的问题 | 为什么是下一步 | 新增要素 | 对应条目 |
| --- | --- | --- | --- | --- |
| 1 | **先掌握：公平赌徒破产。** 从 $i$ 出发先到 $N$ 的概率与平均吸收时间 | 建立边界值、首步递推和可选停止的共同语言 | 调和递推；$X_t$ 与 $X_t^2-t$ | [P002](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md) |
| 2 | 偏置赌徒破产 | 在同一状态空间中看线性解变为几何解 | $(q/p)^{X_t}$；中心化鞅；两个不同特征根 | 本卡第 1 节 |
| 3 | 不等步长的有限区间退出 | 防止机械套用最近邻公式 | overshoot；有限状态线性系统 | [P007](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md) |
| 4 | 区间吸收时间为奇数的概率 | 第一次强制承认“位置状态不够” | 奇偶翻转；$(X_t,t\bmod2)$；二重根 $-1$ | [二阶差分方程卡](Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md) |
| 5 | 路径上首次访问奖励的期望 | 从一个目标推广到许多相关目标 | 指示变量；无需独立的线性期望 | [Indicator Cookbook](Indicator_Random_Variables_Cookbook.md) |
| 6 | **P011 奇环轮流归属** | 合并命中奇偶、剪环、覆盖区间和胜率结构 | 整数线提升；最后顶点；二分路径；期望转胜率 | [P011](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md) |
| 7 | 偏置、加权或偶环版本 | 检验哪些结论依赖公平性、均匀性与奇环 | 两层递推；加权线性期望；二分图例外 | P011 Practice Variants |

每一步复习时都同时回答四问：状态是什么、边界是什么、一步后递推怎样、该状态遗漏了什么。

## 5. P011 的框架定位

P011 同时使用四个家族：普通赌徒破产证明整数线最终覆盖区间的端点参数均匀；坐标与时间同奇偶把首次访问映射为玩家归属；指示变量与线性期望汇总每块砖；奇偶翻转递推产生二重根 $-1$；最后删除一个顶点所得的二分路径，再把期望差转成胜率。

因此最重要的诊断不是“会不会某个闭式公式”，而是：

$$
\boxed{
\text{普通命中只需位置；交替归属必须保留时间相位。}
}
$$

## Connections

- [P011 — 奇环上首次到达时间的奇偶性与奖金归属](../../Questions/Probability/P011_Parity_of_First_Hitting_Times_on_an_Odd_Cycle.md)
- [P002 — Optional Stopping](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md)
- [P007 — Unequal-Jump Random Walk](../../Questions/Probability/P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md)
- [Indicator Random Variables Cookbook](Indicator_Random_Variables_Cookbook.md)
- [Second-Order Difference Equations for Random-Walk Hitting Problems](Second_Order_Difference_Equations_for_Random_Walk_Hitting_Problems.md)

## What to Remember

$$
\boxed{
\text{先问状态是否足够，再选线性期望、鞅或奇偶增强递推。}
}
$$
