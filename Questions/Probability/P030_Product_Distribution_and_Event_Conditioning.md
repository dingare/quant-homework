# P030 — Product Distribution and Event Conditioning

## Metadata

- Category: Probability
- Tags: Support, Integration, Conditional Dependence
- Date Added: 2026-10-22
- Original drill dates: 2026-10-13
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-13 Q3

Source and assessment: [2026-10-13 Q3](../../DailyTests/2026-10-13.md#q3--product-distribution-and-event-conditioning). The reference material below does not change that attempt’s recorded result.

### Question

Let $`U,V`$ be independent $`\mathrm{Uniform}(0,1)`$ variables and $`Z=UV`$. Derive the CDF and density, including domains. Find $`E[U\mid UV\gt1/2]`$ without simulation and decide whether $`U,V`$ remain independent after conditioning.

### Key solution

Clip the integration region at the unit-square boundary:

```math
F_Z(z)=\begin{cases}
0,&z\le0,\\
z-z\ln z,&0\lt z\lt1,\\
1,&z\ge1,
\end{cases}
\qquad
f_Z(z)=-\ln z\quad(0\lt z\lt1).
```

The density is zero outside this interval. For $`A=\{UV\gt1/2\}`$:

```math
P(A)=\frac{1-\ln2}{2},\qquad
E[U\mathbf1_A]=\int_{1/2}^1\int_{1/(2u)}^1u\,dv\,du=\frac18,
\qquad E[U\mid A]=\frac{1}{4(1-\ln2)}.
```

Either integration order is valid with matching bounds. Under $`A`$, the conditional support of $`V`$ given $`U=u`$ is $`(1/(2u),1)`$, so dependence follows. The requested covariance check is:

```math
E[UV\mid A]=\frac{3-2\ln2}{8(1-\ln2)},\qquad
\mathrm{Cov}(U,V\mid A)=\frac{3-2\ln2}{8(1-\ln2)}-\frac{1}{16(1-\ln2)^2}\approx-0.006412.
```

## Assessment history

- [2026-10-13 Q3 — assessment](../../DailyTests/2026-10-13.md#q3--product-distribution-and-event-conditioning)

## Related questions and knowledge

- [P035 — Shared Unknown Win Probability and Predictive Risk](P035_Shared_Unknown_Win_Probability_and_Predictive_Risk.md) — Conditioning and independence depend on the information retained.
