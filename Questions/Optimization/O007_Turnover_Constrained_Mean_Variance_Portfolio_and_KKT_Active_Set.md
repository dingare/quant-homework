# O007 — Turnover-Constrained Mean-Variance Portfolio and KKT Active Set

## Metadata

- Category: Optimization
- Secondary: Portfolio Optimization, Nonsmooth Optimization
- Difficulty: ★★★★☆
- Tags: Mean-Variance, Turnover, L1 Constraint, KKT, Active Set, Transaction Costs
- Review Priority: High
- Personal Note: Revisit the full KKT subgradient check; a locally best first trade need not remain the optimal allocation of the entire turnover budget.
- Date Added: 2026-08-17
- Status: Final

## Core Question

当前组合为

$$
w^{(0)}=egin{pmatrix}0.4\\0.4\\0.2\end{pmatrix},
$$

预期收益和协方差矩阵为

$$
\mu=egin{pmatrix}0.08\\0.05\\0.02\end{pmatrix},
\qquad
\Sigma=egin{pmatrix}2&1&0\\1&2&0\\0&0&1\end{pmatrix}.
$$

求解

$$
\max_w\quad
\mu^\top w-\frac12w^\top\Sigma w
$$

满足

$$
\mathbf1^\top w=1,
\qquad
\left\|w-w^{(0)}\right\|_1\le0.20.
$$

允许做空。求无 turnover constraint 的解、证明 turnover constraint 是否绑定、求最终组合，并解释 KKT multiplier 与不可微性。

## Unconstrained Turnover Benchmark

只保留 full-investment constraint。Lagrangian 一阶条件为

$$
\Sigma w=\mu-\lambda\mathbf1,
$$

所以

$$
w=\Sigma^{-1}(\mu-\lambda\mathbf1).
$$

这里

$$
\Sigma^{-1}
=\begin{pmatrix}
2/3&-1/3&0\\
-1/3&2/3&0\\
0&0&1
\end{pmatrix}.
$$

由 $\mathbf1^\top w=1$ 得 $\lambda=-0.562$，从而

$$
\boxed{
w^{\rm unc}
=\begin{pmatrix}0.224\\0.194\\0.582\end{pmatrix}
}.
$$

相对当前组合，其 turnover 为

$$
|0.224-0.4|+|0.194-0.4|+|0.582-0.2|=0.764,
$$

远大于 $0.20$，所以 turnover constraint 必然影响最优解。

## Turnover Geometry

由于 $w$ 和 $w^{(0)}$ 的分量和都为 $1$，总买入量等于总卖出量。$L^1$ turnover 上限为 $0.20$ 意味着最多把

$$
\frac{0.20}{2}=0.10
$$

的权重从卖出资产转移到买入资产。

在当前组合，objective gradient 为

$$
\nabla f(w^{(0)})
=\mu-\Sigma w^{(0)}
=\begin{pmatrix}-1.12\\-1.15\\-0.18\end{pmatrix}.
$$

因此最值得买入的是资产 3；资产 2 的初始卖出边际收益最大，但使用完整预算时还必须重新优化资产 1 与资产 2 之间的卖出分配。

令从资产 1 卖出 $a$，从资产 2 卖出 $b$，全部买入资产 3。turnover 绑定时

$$
a+b=0.10,
$$

所以可写

$$
w(a)=
\begin{pmatrix}
0.4-a\\
0.3+a\\
0.3
\end{pmatrix},
\qquad 0\le a\le0.10.
$$

此时

$$
\Sigma w(a)
=\begin{pmatrix}1.1-a\\1+a\\0.3\end{pmatrix},
$$

因此

$$
\nabla_1f=-1.02+a,
\qquad
\nabla_2f=-0.95-a.
$$

沿 $a$ 增大的方向，是少卖资产 2、多卖资产 1，故

$$
\frac{d}{da}f[w(a)]
=-\nabla_1f+\nabla_2f
=0.07-2a.
$$

令其为零，得到

$$
a=0.035,
\qquad
b=0.065.
$$

最终最优组合为

$$
\boxed{
w^\star=
\begin{pmatrix}
0.365\\
0.335\\
0.300
\end{pmatrix}
}.
$$

检查 turnover：

$$
|{-0.035}|+|{-0.065}|+|0.100|=0.20.
$$

## KKT Interpretation

在最优点，三个 gradient components 为

$$
\nabla f(w^\star)
=\begin{pmatrix}-0.985\\-0.985\\-0.280\end{pmatrix}.
$$

资产 1 和 2 都在卖出，因此二者边际收益相等；资产 3 在买入。设 turnover multiplier 为 $\eta\ge0$。把一单位权重从任一卖出资产转到资产 3，objective 的边际改善为

$$
-0.280-(-0.985)=0.705.
$$

但这一转移产生两单位 $L^1$ turnover，所以

$$
2\eta=0.705,
$$

即

$$
\boxed{\eta=0.3525}.
$$

$\eta$ 是放宽 turnover budget 一单位的局部 shadow value。

## Important Correction

只沿“卖资产 2、买资产 3”的初始最佳方向用完整个预算，会得到 $(0.4,0.3,0.3)^\top$。这个点不是全局最优：其资产 1 与资产 2 的卖出边际价值不相等，仍可在不改变总 turnover 的情况下，把一部分卖出量从资产 2 调整到资产 1 并提高 objective。

正确做法是：initial gradient 用来识别候选 active set，但最终必须在该 face 上重新优化，并检查完整 KKT conditions。

## Why the Original Form Is Nondifferentiable

绝对值 $|w_i-w_i^{(0)}|$ 在 $w_i=w_i^{(0)}$ 处不可微。因此应使用 subgradient KKT，或引入辅助变量 $u_i$：

$$
u_i\ge w_i-w_i^{(0)},
\qquad
u_i\ge-[w_i-w_i^{(0)}],
$$

并施加

$$
\sum_i u_i\le0.20.
$$

这样问题变成带线性约束的标准 convex quadratic program。

## Reusable Checklist

1. 先解无交易限制 benchmark。
2. 利用 full investment，把 $L^1$ turnover 转为买入量等于卖出量。
3. 用 current gradient 识别候选买入和卖出资产。
4. 在候选 active face 上重新优化，而不是只走初始 steepest direction。
5. 检查 subgradient stationarity、feasibility 与 complementary slackness。
6. 将 turnover multiplier 解释为额外交易预算的 shadow value。

## Connections

- [O002 — Constrained Mean-Variance Optimization and the Meaning of Lagrange Multipliers](O002_Constrained_Mean_Variance_Optimization_and_the_Meaning_of_Lagrange_Multipliers.md) — equality constraints 与 shadow prices。
- [O004 — Optimal Execution with Impact and Inventory Risk](O004_Optimal_Execution_with_Impact_and_Inventory_Risk.md) — 交易成本与风险之间的动态权衡。
- [O006 — Hedge-Constrained Execution with Position Limits](O006_Hedge_Constrained_Execution_with_Position_Limits.md) — box constraints、active-set 检查和 KKT。

## What to Remember

$$
\boxed{
w^\star=(0.365,0.335,0.300)^\top,
\qquad
\eta=0.3525
}.
$$
