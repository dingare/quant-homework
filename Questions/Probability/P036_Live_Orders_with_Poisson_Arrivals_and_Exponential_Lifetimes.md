# P036 — Live Orders with Poisson Arrivals and Exponential Lifetimes

## Metadata

- Category: Probability
- Tags: Poisson Process, Thinning, Exponential Memorylessness, Conditional Distribution, Stationary Distribution
- Date Added: 2026-10-24
- Original drill: October 23, 2026, Q2
- Status: Full worked reference supplied on request; independent derivation unverified.

## Core Question

Orders arrive according to a Poisson process with rate $`\lambda\gt0`$. Each order remains live for an independent exponential lifetime with rate $`\delta\gt0`$, then disappears. Lifetimes are independent of arrivals and of one another. There are no live orders at time zero. Let $`N_t`$ be the number of live orders at time t.

1. For fixed $`T\gt0`$, derive the distribution of $`N_T`$, including its mean and variance.
2. Given only $`N_T=k`$, derive the conditional distribution of $`N_{T+h}`$ for $`h\gt0`$ and calculate its conditional expectation.
3. Does $`N_T`$ approach a limiting distribution as T tends to infinity? Derive it and interpret its mean.

Justify distributional steps rather than quoting a queueing formula.

## Solution

### Representation: arrival versus lifetime

Let S_i be an arrival time and L_i its lifetime. An order is live at T precisely when:

```math
S_i\le T\lt S_i+L_i.
```

For an arrival at t no later than T:

```math
P(L_i\gt T-t)=e^{-\delta(T-t)}.
```

Interarrival gaps are independent exponential variables with rate lambda. Only the first arrival time itself is exponential; subsequent arrival times are sums of interarrival gaps. Arrival time plus lifetime is the departure time. The question counts orders whose live intervals cover T; it is not directly the distribution of a sum of two exponentials.

The user's initial wording was clarified as intending this correct arrival/survival representation. Do not treat the clarification as a confirmed misconception about the survival inequality or every arrival time being exponential.

### 1. Distribution at a fixed time

Let A_T count all arrivals by T:

```math
A_T\sim\mathrm{Poisson}(\lambda T).
```

Given A_T=m, the unordered arrival times, after random labeling, have the distribution of m iid Uniform(0,T) variables. The chronologically sorted arrival times are order statistics, not independent uniforms. Since the live count is symmetric in labels, use the iid unordered representation. Independent lifetimes then give iid retention indicators with common probability:

```math
p_T=\frac1T\int_0^T e^{-\delta(T-t)}\,dt
=\frac{1-e^{-\delta T}}{\delta T},
\qquad
N_T\mid A_T=m\sim\mathrm{Binomial}(m,p_T).
```

Integrating out the random arrival count proves the distribution, not just its mean. For every integer k at least zero, with r=m-k:

```math
\begin{aligned}
P(N_T=k)
&=\sum_{m=k}^{\infty}\binom mk p_T^k(1-p_T)^{m-k}
 e^{-\lambda T}\frac{(\lambda T)^m}{m!}\\
&=e^{-\lambda T}\frac{(\lambda Tp_T)^k}{k!}
 \sum_{r=0}^{\infty}\frac{[\lambda T(1-p_T)]^r}{r!}\\
&=e^{-\lambda Tp_T}\frac{(\lambda Tp_T)^k}{k!}.
\end{aligned}
```

Therefore:

```math
\boxed{N_T\sim\mathrm{Poisson}(m_T)},\qquad
m_T=\frac{\lambda}{\delta}(1-e^{-\delta T}),
\qquad E[N_T]=\mathrm{Var}(N_T)=m_T.
```

### Why Poisson survives the filtering

A fixed number of independently retained objects gives a binomial count. A Poisson number of objects, each independently retained with the same probability, gives another Poisson count: the calculation above is the exact thinning proof.

There is also a useful small-interval intuition. Near time t, the probability of an arrival over a short interval of length dt is approximately lambda dt, and its survival probability is approximately the factor below:

```math
\text{retained-arrival probability}\approx
\lambda e^{-\delta(T-t)}\,dt.
```

Counts contributed by disjoint arrival intervals are independent. Subdividing time gives many independent rare contributions, with total mean:

```math
\int_0^T\lambda e^{-\delta(T-t)}\,dt=m_T.
```

This motivates a Poisson law; the conditional-binomial calculation establishes it exactly. Merely calculating this integral as an expectation does not establish a distribution. The retention probability varies with arrival time; after averaging iid unordered arrival times conditional on A_T, each label has the same marginal retention probability p_T.

### 2. Conditional future distribution

Given N_T=k, split the future count into survivors of current orders and surviving new arrivals. By exponential memorylessness, each current order has remaining survival probability:

```math
p_h=e^{-\delta h},\qquad
S\mid N_T=k\sim\mathrm{Binomial}(k,p_h).
```

Poisson independent increments and independent new lifetimes give:

```math
B\sim\mathrm{Poisson}\left(\frac{\lambda}{\delta}(1-p_h)\right).
```

Conditional on N_T=k, S and B are independent. Thus:

```math
\boxed{N_{T+h}\mid N_T=k\ \overset{d}{=}\ S+B}.
```

This independent binomial-plus-Poisson convolution fully specifies the conditional distribution; it is generally not itself Poisson. Its expectation is:

```math
\boxed{E[N_{T+h}\mid N_T=k]
=kp_h+\frac{\lambda}{\delta}(1-p_h)
=\frac{\lambda}{\delta}+
\left(k-\frac{\lambda}{\delta}\right)e^{-\delta h}}.
```

Existing-count influence decays, and the expected live count approaches the long-run level.

### 3. Long-run distribution

As T tends to infinity, m_T tends to lambda divided by delta, so:

```math
\boxed{N_T\xrightarrow{d}\mathrm{Poisson}\left(\frac{\lambda}{\delta}\right)}.
```

The limiting mean is arrival rate times average lifetime. Equivalently, with n live orders the total departure rate is n delta. In stationarity, mean arrival and departure rates balance:

```math
\lambda=\delta E[N],\qquad E[N]=\frac{\lambda}{\delta}.
```

Flow balance explains the mean; convergence of the complete Poisson law establishes the limiting distribution.

## Assessment History

- [October 23 Q2 — assessment, archived October 24](../../DailyTests/2026-10-23.md#q2--live-orders-with-poisson-arrivals-and-exponential-lifetimes)

## Connections

- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md): Poisson arrival gaps, survival and memorylessness; this problem counts surviving arrivals rather than comparing the first of competing clocks.
- [SC004 — Competing Exponential Clocks and CTMC Hitting](../StochasticCalculus/SC004_Competing_Exponential_Clocks_and_CTMC_Hitting.md): independent lifetimes and state-dependent total exit rates.

## What to Remember

Condition on arrival count, average the retention probability over arrival time, and thin. For future counts, separate old survivors from new arrivals. Exponential memorylessness makes the current count sufficient for this transition law.
