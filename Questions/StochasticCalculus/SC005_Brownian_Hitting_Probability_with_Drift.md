# SC005 — Brownian Hitting Probability with Drift

## Metadata

- Category: Stochastic Calculus
- Secondary: First Passage, Generator Equations
- Difficulty: ★★★★☆
- Tags: Brownian Motion, Drift, Hitting Probability, Expected Exit Time, Optional Stopping
- Review Priority: High
- Personal Note: Revisit both generator ODEs and verify the zero-drift limit without memorizing the closed forms.
- Date Added: 2026-08-13
- Status: Final

## Core Question

令

$$
X_t=0.2t+W_t,
\qquad X_0=0,
$$

并在首次到达 $2$ 或 $-1$ 时停止。求先到 $2$ 的概率、期望停止时间与期望终值，并考察 drift 趋于零时的极限。

## Hitting Probability

令 $p(x)$ 为从 $x$ 出发先到上界的概率。生成元方程为

$$
0.2p'(x)+\frac12p''(x)=0,
\qquad p(-1)=0,\quad p(2)=1.
$$

一般地，若 $k=2\mu/\sigma^2$，下界为 $L$、上界为 $U$，则

$$
p(x)=\frac{1-e^{-k(x-L)}}{1-e^{-k(U-L)}}.
$$

代入 $x=0,L=-1,U=2,k=0.4$：

$$
\boxed{p(0)=\frac{1-e^{-0.4}}{1-e^{-1.2}}\approx0.472}.
$$

正 drift 并不保证胜率超过一半，因为下界距离只有 $1$，上界距离为 $2$。

## Expected Exit Time and Terminal P&L

由于终值只能是 $2$ 或 $-1$，

$$
E[X_\tau]=2p(0)-[1-p(0)]=3p(0)-1\approx0.416.
$$

对有界区间首次退出可使用停止后的 martingale $X_t-\mu t$，得到

$$
E[X_\tau]=\mu E[\tau].
$$

因此

$$
\boxed{E[\tau]=\frac{3p(0)-1}{0.2}\approx2.08}.
$$

$E[X_\tau]$ 不等于零，因为 $X_t$ 本身不是 martingale；$X_t-0.2t$ 才是。

## Zero-Drift Limit

当 $\mu\to0$ 时，用 $1-e^{-z}\sim z$：

$$
p(0)\to\frac{0-L}{U-L}=\frac13.
$$

零 drift Brownian motion 在距离为 $a=2,b=1$ 的两边界之间有

$$
\boxed{E[\tau]\to\frac{ab}{\sigma^2}=2},
\qquad
\boxed{E[X_\tau]\to0}.
$$

## What to Remember

- hitting probability 解齐次 generator ODE。
- expected exit time 解右端为 $-1$ 的 Poisson equation。
- 非零 drift 时应对 $X_t-\mu t$，而非 $X_t$，使用 optional stopping。
