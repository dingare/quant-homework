# P024 — Bayesian Coin Selection and Prediction

## Metadata

- Category: Probability
- Tags: Bayes, Mixture Prior, Posterior Prediction
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08
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

## Assessment history

- [2026-10-08 Q6 — assessment](../../DailyTests/2026-10-08.md#q6--bayesian-coin-posterior-and-prediction)

## Related questions and knowledge

- [P035 — Shared Unknown Win Probability and Predictive Risk](P035_Shared_Unknown_Win_Probability_and_Predictive_Risk.md) — Posterior predictive averaging over a shared latent parameter.
- [P031 — Exact Uniform Sampling from a Biased Coin](P031_Exact_Uniform_Sampling_from_a_Biased_Coin.md) — Unknown-biased-coin sampling versus Bayesian inference.
- [T010 — Deployment Probabilities and Decisions](../TimeSeries/T010_Deployment_Probabilities_and_Decisions.md) — Prior odds, likelihood ratios and posterior prediction.
