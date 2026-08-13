# L006 — Factor-Neutral Alpha in Eigenfactor Space

## Metadata

- Category: Linear Algebra
- Secondary: Portfolio Optimization, PCA
- Difficulty: ★★★☆☆
- Tags: Eigenbasis, Factor Neutrality, Maximum Sharpe, Inverse Variance
- Review Priority: High
- Personal Note: Revisit why Euclidean alpha projection differs from covariance-weighted maximum-Sharpe allocation.
- Date Added: 2026-08-13
- Status: Final

## Core Question

协方差矩阵有正交特征向量 $q_1,\ldots,q_4$，对应特征值 $(16,9,4,1)$。预期收益为

$$
\mu=2q_1+3q_2+4q_3+2q_4.
$$

要求 $q_1^\top w=q_2^\top w=0$，求最大化 Sharpe ratio 的组合方向、单位方差归一化和最大 Sharpe ratio。

## Solution

在特征基中写

$$
w=a_1q_1+a_2q_2+a_3q_3+a_4q_4.
$$

中性约束立即给出 $a_1=a_2=0$。于是

$$
w^\top\mu=4a_3+2a_4,
\qquad
w^\top\Sigma w=4a_3^2+a_4^2.
$$

可行子空间内的最大 Sharpe 方向是 inverse variance times alpha：

$$
\begin{pmatrix}a_3\\a_4\end{pmatrix}
\propto
\begin{pmatrix}1/4&0\\0&1\end{pmatrix}
\begin{pmatrix}4\\2\end{pmatrix}
=\begin{pmatrix}1\\2\end{pmatrix}.
$$

因此 $w_0=q_3+2q_4$。其方差为 $4+4=8$，故单位方差组合为

$$
\boxed{w^\star=\frac{q_3+2q_4}{\sqrt8}}.
$$

同时 $w_0^\top\mu=8$，所以

$$
\boxed{SR_{\max}=\frac8{\sqrt8}=\sqrt8}.
$$

仅把 $\mu$ 做欧氏投影会得到 $4q_3+2q_4$，但这没有按各方向风险缩放。除非可行子空间内协方差与单位阵成比例，否则最大 Sharpe 组合必须使用 covariance-metric weighting。

## Key Knowledge Points

- PCA 基使协方差对角化，也使 factor-neutrality 直接变成坐标为零。
- alpha projection 决定可交易信号；inverse eigenvalue weighting 决定风险调整后的仓位。
- 无需构造或求逆完整协方差矩阵。

## What to Remember

在可行特征因子集合 $J$ 上，

$$
\boxed{a_j\propto\frac{\mu_j}{\lambda_j},\qquad j\in J.}
$$
