# O006 — Hedge-Constrained Execution with Position Limits

## Metadata

- Category: Optimization
- Secondary: Quadratic Programming, KKT Conditions
- Difficulty: ★★★☆☆
- Tags: Execution, Quadratic Cost, Hedge Constraint, Box Constraint, KKT
- Review Priority: High
- Personal Note: Revisit the equality-constrained closed form, then practice one variant in which a box constraint actually binds.
- Date Added: 2026-08-13
- Status: Final

## Core Question

给定

$$
\mu=(4,3,2)^\top,
\qquad
H=\begin{pmatrix}4&1&0\\1&2&0\\0&0&1\end{pmatrix},
$$

求

$$
\max_x\ \mu^\top x-\frac12x^\top Hx
$$

满足 $x_1+x_2+x_3=0$ 和 $|x_i|\le2$。求无约束解、仅含 hedge constraint 的解、最终最优值及活跃约束的 KKT multiplier。

## Solution

无约束一阶条件 $Hx=\mu$ 给出

$$
x^{\rm unc}=H^{-1}\mu=\left(\frac57,\frac87,2\right)^\top.
$$

它不满足净头寸为零。令 $a=(1,1,1)^\top$，Lagrangian 为

$$
L=\mu^\top x-\frac12x^\top Hx-\lambda a^\top x.
$$

于是

$$
x=H^{-1}(\mu-\lambda a),
\qquad
\lambda=\frac{a^\top H^{-1}\mu}{a^\top H^{-1}a}.
$$

由

$$
H^{-1}\mu=\left(\frac57,\frac87,2\right)^\top,
\qquad
H^{-1}a=\left(\frac17,\frac37,1\right)^\top,
$$

得到 $\lambda=27/11$，从而

$$
\boxed{x^\star=\left(\frac4{11},\frac1{11},-\frac5{11}\right)^\top}.
$$

三个分量都严格位于 $(-2,2)$，所以 box constraints 均不活跃，其 multiplier 全为零。由 $Hx^\star=\mu-\lambda a$ 和 $a^\top x^\star=0$，有

$$
(x^\star)^\top Hx^\star=(x^\star)^\top\mu.
$$

因此最优值为

$$
\boxed{\frac12\mu^\top x^\star=\frac9{22}}.
$$

## Reusable Checklist

1. 先解无约束问题。
2. 用 equality-constrained closed form 加入线性 hedge。
3. 检查 box constraints，而不是预先假设其是否活跃。
4. 若有越界，固定候选活跃坐标并重解 reduced KKT system。
5. 检查 primal feasibility、dual feasibility 与 complementary slackness。

## What to Remember

$$
\boxed{x^\star=H^{-1}\mu-H^{-1}a\frac{a^\top H^{-1}\mu}{a^\top H^{-1}a}}
$$

只在该解满足其余不等式约束时才是最终答案。
