# T009 — MA(1) Equivalence, Invertibility, and Fitting

## Metadata

- Category: TimeSeries
- Tags: Autocovariance, Identification, Innovations, Invertibility
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q5

Source and assessment: [2026-10-11 Q5](../../DailyTests/2026-10-11.md#q5--ma1-equivalence-invertibility-and-fitting). The reference material below does not change that attempt’s recorded result.

### Question

Let $`X_t=\varepsilon_t+\theta\varepsilon_{t-1}`$, with iid $`N(0,\sigma^2)`$ innovations. Derive mean and autocovariance at every lag. For $`\theta=2,\sigma^2=1`$, find an equivalent representation with $`|\theta|\lt1`$. Can Gaussian observations distinguish them? Explain invertibility and its practical role.

### Key solution

```math
E[X_t]=0,\qquad
\gamma(h)=\begin{cases}
(1+\theta^2)\sigma^2,&h=0,\\
\theta\sigma^2,&|h|=1,\\
0,&|h|\gt1.
\end{cases}
```

The equivalent parameters are $`\theta'=1/2,\sigma'^2=4`$. Both have $`\gamma(0)=5,\gamma(1)=2`$; Gaussianity makes their full observation distributions identical. Invertibility selects a representation allowing stable reconstruction of innovations from past observations. Stationarity holds for every finite $`\theta`$.

## Assessment history

- [2026-10-11 Q5 — assessment](../../DailyTests/2026-10-11.md#q5--ma1-equivalence-invertibility-and-fitting)

## Related questions and knowledge

- [T011 — Signal Smoothing, Correlation, and Trading Costs](T011_Signal_Smoothing_Correlation_and_Trading_Costs.md) — Lagged signal combinations, autocovariance and representation.
