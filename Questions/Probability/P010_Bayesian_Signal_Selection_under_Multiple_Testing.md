# P010 — Bayesian Signal Selection under Multiple Testing

## Metadata

- Category: Probability
- Secondary: Bayesian Inference, Multiple Testing, Selection Bias
- Difficulty: ★★★★☆
- Tags: Bayes Rule, Mixture Model, Maximum, False Discovery, Backtest Selection
- Review Priority: High
- Personal Note: Revisit posterior-odds calculations and explain exactly when maximum selection cancels after conditioning on the observed score.
- Date Added: 2026-08-13
- Status: Final

## Core Question

独立检验 $100$ 个信号。每个信号以概率 $0.05$ 有真实 alpha，且

$$
Z\mid H=0\sim N(0,1),
\qquad
Z\mid H=1\sim N(2,1).
$$

选取 $Z$ 最大的信号，观察到最大值 $M=3$。求赢家有真实 alpha 的后验概率，并讨论它与预先指定且观测到 $Z=3$ 的信号有何不同。再求所有 $Z_i\gt2$ 中真实信号的期望数量，以及使 $P(H=0\mid Z\gt c)\le0.1$ 的阈值。

## Solution

单个得分的混合分布函数为

$$
F(z)=0.95\Phi(z)+0.05\Phi(z-2).
$$

指定信号在状态 $h$ 下以 $m$ 成为最大值的联合密度正比于

$$
P(H=h)f_h(m)F(m)^{99}.
$$

两种状态共有的 $F(m)^{99}$ 抵消，因此

$$
P(H_{\rm winner}=1\mid M=m)
=\frac{0.05\phi(m-2)}{0.95\phi(m)+0.05\phi(m-2)}.
$$

在 $m=3$ 时，$\phi(1)/\phi(3)=e^4$，故

$$
\boxed{P(H_{\rm winner}=1\mid M=3)=\frac{0.05e^4}{0.95+0.05e^4}\approx0.742}.
$$

这恰好等于预先指定信号在 $Z=3$ 时的后验。选择最大值改变了观测值的分布，但给定精确得分后，“其余 $99$ 个都较小”对赢家所属 mixture component 不再提供额外信息。

对阈值 $2$，单个信号同时为真且被选中的概率是 $0.05\times0.5=0.025$，所以

$$
\boxed{E\left[\left|\{i:H_i=1,Z_i\gt2\}\right|\right]=2.5}.
$$

Bayesian false-discovery probability 为

$$
\frac{0.95\bar\Phi(c)}{0.95\bar\Phi(c)+0.05\bar\Phi(c-2)}.
$$

令其不超过 $0.1$，等价于

$$
\frac{\bar\Phi(c-2)}{\bar\Phi(c)}\ge171,
$$

数值解约为

$$
\boxed{c\approx3.21}.
$$

## Key Knowledge Points

- 后验由 likelihood ratio 与 prior odds 共同决定。
- 给定赢家的精确得分时，独立同分布候选者的最大值选择项会抵消。
- “被选为赢家”仍会影响 effect-size estimation、只条件于入选而不条件于得分的推断，以及未知层级先验下的推断。
- 多重回测中，$3\sigma$ 结果也必须结合真实信号的先验稀缺度解释。

## What to Remember

$$
\boxed{\text{Posterior odds}=\text{prior odds}\times\text{likelihood ratio}.}
$$
