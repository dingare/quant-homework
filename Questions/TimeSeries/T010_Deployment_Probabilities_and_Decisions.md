# T010 — Deployment Probabilities and Decisions

## Metadata

- Category: TimeSeries
- Tags: Prior Shift, Bayes Odds, Calibration, Decision Thresholds
- Date Added: 2026-10-22
- Original drill dates: 2026-10-13
- Status: Archived interview material; original follow-up remains Pending; performance is recorded separately below.

## Interview drill — 2026-10-13 Q5

Source and assessment: [2026-10-13 Q5](../../DailyTests/2026-10-13.md#q5--deployment-probabilities-and-decisions). The reference material below does not change that attempt’s recorded result.

### Question

A binary classifier returns the exact calibrated training posterior $`p_{\mathrm{train}}(x)=P_{\mathrm{train}}(Y=1\mid X=x)`$. Training prevalence is 0.5, deployment prevalence 0.1, and class-conditional feature distributions $`P(X\mid Y)`$ remain unchanged. Derive the deployment probability and evaluate training output 0.8.

**Pending follow-up:** false positives cost 1, false negatives cost 9, correct decisions cost zero. Derive the optimal rule in terms of the training output and explain why threshold adjustment alone does not recalibrate reported probabilities.

### Key solution

For class prevalence $`\pi`$ and unchanged class-conditional densities $`f_1,f_0`$:

```math
\frac{P(Y=1\mid x)}{P(Y=0\mid x)}=\frac{f_1(x)}{f_0(x)}\frac{\pi}{1-\pi}.
```

Only the prior-odds factor changes:

```math
\frac{p_{\mathrm{deploy}}}{1-p_{\mathrm{deploy}}}
=\frac{0.1/0.9}{0.5/0.5}\frac{p_{\mathrm{train}}}{1-p_{\mathrm{train}}}
=\frac19\frac{p_{\mathrm{train}}}{1-p_{\mathrm{train}}},\qquad
p_{\mathrm{deploy}}=\frac{p_{\mathrm{train}}}{9-8p_{\mathrm{train}}}.
```

At training output 0.8, the deployment probability is $`4/13\approx0.307692`$. The multiplier applies to odds, not directly to probability. The decision follow-up has no published solution yet.

## Assessment history

- [2026-10-13 Q5 — assessment](../../DailyTests/2026-10-13.md#q5--deployment-probabilities-and-decisions)

## Related questions and knowledge

- [P024 — Bayesian Coin Selection and Prediction](../Probability/P024_Bayesian_Coin_Selection_and_Prediction.md) — Prior odds, likelihood ratios and posterior prediction.
- [T012 — Probability Forecasts, Calibration, and Evaluation](T012_Probability_Forecasts_Calibration_and_Evaluation.md) — Calibration and decision thresholds answer different questions.
