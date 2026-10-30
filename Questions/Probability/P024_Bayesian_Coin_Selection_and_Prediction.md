# P024 — Bayesian Coin Selection and Prediction

## Metadata

- Category: Probability
- Tags: Bayes, Mixture Prior, Posterior Prediction, Beta-Bernoulli, Exact Binomial Confidence Interval
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08
- Discussion added: 2026-10-30; ten heads, confidence intervals, and an unknown coin bias.
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q6

Source and assessment: [2026-10-08 Q6](../../DailyTests/2026-10-08.md#q6--bayesian-coin-posterior-and-prediction). The reference material below does not change that attempt’s recorded result.

### Question

Select coin A or B with equal probability. A has head probability 1/2; B has head probability 3/4. After observing HHH from the selected coin, derive the posterior probability of B and the probability that the next flip is H.

### Recorded solution

```math
P(B\mid HHH)=\frac{(3/4)^3}{(3/4)^3+(1/2)^3}=\frac{27}{35},
\qquad P(H_4\mid HHH)=\frac{27}{35}\frac34+\frac8{35}\frac12=\frac{97}{140}.
```

Update the hidden coin probability first, then average conditional head probabilities using the posterior.

### Related Notes

- [P010 — Bayesian Signal Selection under Multiple Testing](P010_Bayesian_Signal_Selection_under_Multiple_Testing.md): related prior × likelihood normalization, with a different application.

## Discussion — 2026-10-30: Ten Heads and an Unknown Coin Bias

来源：本次对话中已完成的硬币推断讨论。以下是复习笔记，不是一次新的计时测试，也不改变原有测评或掌握程度记录。

### 问题与假设

有一枚公平硬币和一枚不公平硬币。随机选择一枚，连续抛掷 10 次，结果全部为正面。怎样计算选中不公平硬币的概率？如果不公平硬币的正面概率未知、服从均匀先验，又应怎样更新？这和置信区间有什么区别？

设观测事件为 $`D=10H`$，公平硬币模型为 $`F`$，不公平硬币模型为 $`U`$。先假设两种硬币被选中的概率相同：

```math
P(F)=P(U)=\frac12.
```

公平硬币的正面概率为 $`p=1/2`$。在不公平模型中，先为这枚硬币抽取一个正面概率 $`p`$，之后一直固定使用它；给定 $`p`$，各次抛掷独立。不是每次抛掷都重新抽取一个 $`p`$。

### 1. 已知不公平硬币的正面概率

如果不公平硬币的正面概率已知为 $`q`$，两种模型产生观测结果的概率分别为：

```math
P(D\mid F)=\left(\frac12\right)^{10},
\qquad P(D\mid U)=q^{10}.
```

贝叶斯公式给出：

```math
P(U\mid D)
=\frac{P(D\mid U)P(U)}{P(D\mid U)P(U)+P(D\mid F)P(F)}
=\frac{q^{10}}{q^{10}+(1/2)^{10}}.
```

例如，不公平硬币若是双面正面，即 $`q=1`$，则：

```math
P(U\mid D)=\frac{1024}{1025}\approx99.9024\%.
```

这一结果依赖于硬币类型的先验概率和对不公平硬币的具体假设。

### 2. 未知偏置：对所有可能的 p 积分

如果在不公平模型下只有均匀先验：

```math
p\mid U\sim\mathrm{Uniform}(0,1),
\qquad f(p\mid U)=1,\quad 0\lt p\lt1,
```

就需要将给定每个 $`p`$ 的似然，对先验分布加权平均：

```math
P(D\mid U)
=\int_0^1P(D\mid p,U)f(p\mid U)\,dp
=\int_0^1p^{10}\,dp
=\left[\frac{p^{11}}{11}\right]_0^1
=\frac1{11}.
```

把这个边际似然代入模型层面的贝叶斯公式：

```math
\boxed{
P(U\mid D)
=\frac{(1/11)(1/2)}{(1/11)(1/2)+(1/1024)(1/2)}
=\frac{1024}{1035}
\approx98.94\%.
}
```

这里 $`1/11`$ 是不公平模型产生数据的概率，不是观察数据后硬币不公平的概率；后者还要和公平模型比较，并纳入模型先验。

### 3. 为什么后验是 Beta(11, 1)？

以下始终条件于选中了不公平模型 $`U`$，更新的是该模型内部的参数 $`p`$。

均匀分布就是 $`\mathrm{Beta}(1,1)`$。Beta 密度的形式为：

```math
f(p)\propto p^{\alpha-1}(1-p)^{\beta-1},\qquad 0\lt p\lt1.
```

10 个正面、0 个反面的似然为 $`p^{10}(1-p)^0`$。后验正比于先验乘以似然：

```math
\begin{aligned}
f(p\mid D,U)
&\propto p^{1-1}(1-p)^{1-1}\,p^{10}(1-p)^0\\
&=p^{10}(1-p)^0.
\end{aligned}
```

匹配指数：

```math
\alpha-1=10,\qquad\beta-1=0
\quad\Longrightarrow\quad
\boxed{p\mid D,U\sim\mathrm{Beta}(11,1).}
```

归一化常数也可以直接从前面的积分得到：

```math
f(p\mid D,U)=\frac{p^{10}}{\int_0^1u^{10}\,du}=11p^{10},
\qquad 0\lt p\lt1.
```

一般地，Beta 先验的两个参数分别加上正面数和反面数：

```math
p\sim\mathrm{Beta}(\alpha,\beta),
\qquad h\text{ heads},\ t\text{ tails}
\quad\Longrightarrow\quad
p\mid D\sim\mathrm{Beta}(\alpha+h,\beta+t).
```

所以这里是 $`(1+10,1+0)=(11,1)`$，不是把两个参数直接设为正面、反面的观测次数。

### 4. 为什么精确置信下界是 0.025 的 1/10 次方？

如果问题是估计一枚固定硬币的正面概率 $`p`$，10 次全正面后的双侧、等尾 95% 精确二项置信区间为：

```math
\left[(0.025)^{1/10},1\right]\approx[0.6915,1].
```

双侧区间把剩余的 5% 分到两端，每端为 $`(1-0.95)/2=0.025`$。设 $`X`$ 为 10 次抛掷中的正面数。下界 $`p_L`$ 满足：

```math
P(X\ge10\mid p_L)=P(X=10\mid p_L)=p_L^{10}=0.025,
\qquad
\boxed{p_L=(0.025)^{1/10}.}
```

如果 $`p`$ 比这个下界还小，出现 10 次全正面的概率就低于 2.5%。上界为 1，因为 $`p=1`$ 完全符合观察。若只求 95% 单侧置信下界，则不将 5% 除以 2：

```math
p_L=(0.05)^{1/10}\approx0.7411.
```

置信区间不表示“硬币有 95% 的概率不公平”，也不等于参数的贝叶斯后验区间。

### 5. 三个容易混淆的对象

| 对象 | 含义 | 本例结果 |
| --- | --- | --- |
| 硬币类型的后验概率 | 比较公平模型和不公平模型，保留两者的先验概率 | 均匀偏置模型、等模型先验下，不公平概率约 98.94% |
| 不公平模型内部的参数后验 | 已条件于不公平模型，用数据更新正面概率 | Beta(11, 1) |
| 正面概率的频率学置信区间 | 从二项抽样分布反推参数范围 | 双侧 95% 精确区间约 [0.6915, 1] |

如果只设 $`p\sim\mathrm{Uniform}(0,1)`$，而不单独保留公平硬币模型，那么在连续先验下 $`P(p=0.5)=0`$，观察数据前“不完全公平”的概率就已经是 100%。要讨论选中公平硬币还是不公平硬币，需要像本例这样给公平模型单独分配正的先验概率。

## Assessment history

- [2026-10-08 Q6 — assessment](../../DailyTests/2026-10-08.md#q6--bayesian-coin-posterior-and-prediction)

## Related questions and knowledge

- [P035 — Shared Unknown Win Probability and Predictive Risk](P035_Shared_Unknown_Win_Probability_and_Predictive_Risk.md) — Posterior predictive averaging over a shared latent parameter.
- [P031 — Exact Uniform Sampling from a Biased Coin](P031_Exact_Uniform_Sampling_from_a_Biased_Coin.md) — Unknown-biased-coin sampling versus Bayesian inference.
- [T010 — Deployment Probabilities and Decisions](../TimeSeries/T010_Deployment_Probabilities_and_Decisions.md) — Prior odds, likelihood ratios and posterior prediction.
