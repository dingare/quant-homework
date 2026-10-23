# T012 — Probability Forecasts, Calibration, and Evaluation

## Metadata

- Category: TimeSeries
- Tags: Brier Score, Calibration, Accuracy, Probability Decisions
- Date Added: 2026-10-22
- Original drill dates: 2026-10-20
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-20 Q4

Source and assessment: [2026-10-20 Q4](../../DailyTests/2026-10-20.md#q4--probability-forecasts-and-classification-accuracy). The reference material below does not change that attempt’s recorded result.

### Question

A model predicts whether tomorrow's return is positive: $`Y\in\{0,1\}`$. Observations belong equally often to two groups:

```math
P(Y=1\mid G=L)=0.3,\qquad P(Y=1\mid G=H)=0.9.
```

Three forecasters report:

| Forecaster | Prediction in L | Prediction in H |
| --- | ---: | ---: |
| A | 0.60 | 0.60 |
| B | 0.30 | 0.90 |
| C | 0.05 | 0.95 |

A probability forecast is calibrated when observations receiving forecast q have positive-return frequency q.

1. Which forecasters are calibrated? Justify each answer.
2. Derive and compare their population losses $`E[(Y-\widehat p)^2]`$.
3. Compare B and C's classification accuracy using cutoff 0.5. What does this comparison establish about evaluating probability forecasts using classification accuracy alone?

### Key solution

**Calibration.** A always predicts 0.6 and the unconditional positive-return frequency is $`(0.3+0.9)/2=0.6`$, so A is calibrated. B's predictions 0.3 and 0.9 separately match their conditional event frequencies. C's 0.05 and 0.95 do not. Thus A and B are calibrated; C is not. The group is known at prediction time, before observing Y; A simply ignores it. Calibration is defined conditional on the reported forecast, not automatically conditional on every available feature. A is calibrated overall without providing B's group-specific information.

**Population probability loss.** For a Bernoulli outcome with true probability p and fixed forecast q, condition on the information defining p:

```math
E[(Y-q)^2]=p(1-q)^2+(1-p)q^2
=p(1-p)+(q-p)^2.
```

The second term is squared probability error. The question asks for a population expectation over one randomly drawn observation's group and outcome; an observed sample average estimates that quantity:

```math
\widehat L=\frac1n\sum_{i=1}^n(Y_i-q_i)^2.
```

The three population losses are:

| Forecaster | Loss in L | Loss in H | Equal-weight population loss |
| --- | ---: | ---: | ---: |
| A | 0.30 | 0.18 | 0.24 |
| B | 0.21 | 0.09 | 0.15 |
| C | 0.2725 | 0.0925 | 0.1825 |

For C specifically:

```math
L_{C,L}=0.3(0.95)^2+0.7(0.05)^2=0.2725,
\qquad
L_{C,H}=0.9(0.05)^2+0.1(0.95)^2=0.0925,
\qquad
L_C=\tfrac12(0.2725+0.0925)=0.1825.
```

**Classification at cutoff 0.5.** B and C both predict zero in L and one in H. Their common accuracy is:

```math
P(\widehat Y=Y)=\tfrac12(1-0.3)+\tfrac12(0.9)=0.8.
```

Accuracy evaluates the thresholded decisions, losing probability magnitude. C is more extreme than the true probabilities and can have the same accuracy as B while having worse probability loss. A versus B shows a different distinction: both are calibrated, but B uses group information and has lower probability loss. Calibration alone does not establish useful discrimination or information content.

### Practical discussion — probability quality and decisions

The user asked how overconfidence matters when probability estimates feed position sizing, trading decisions or expected-loss calculations. In H, a forecast of 0.95 implies a negative-event probability 0.05 even though it is actually 0.10 in this model. Identical threshold decisions need not imply identical decisions under a probability-sensitive policy. Direction probability alone does not determine expected return without outcome magnitudes and costs; a better probability score does not by itself prove better trading performance.

The discussed evaluation approach has three layers:

1. **Probability scoring on the same out-of-sample observations.** Compare Brier score (the sample mean squared probability loss above) and log loss. Log loss strongly penalizes confident incorrect forecasts. These scores reflect more than calibration, so a lower score alone does not prove better calibration.

```math
\widehat L_{\log}
=-\frac1n\sum_{i=1}^n\left[y_i\log q_i+(1-y_i)\log(1-q_i)\right].
```

2. **Calibration diagnostics.** Group observations with similar predicted probabilities; compare each bin's average forecast with its observed positive-event frequency. Report bin sample counts and appropriate uncertainty intervals; also inspect relevant sectors and time periods so an aggregate check does not hide local miscalibration. For calibrated forecasts the population comparison follows the identity line; finite-sample differences require uncertainty assessment.
3. **Decision evaluation.** Fix a common probability-to-position rule, cost assumptions and risk constraints when isolating how forecast differences affect decisions. Compare out-of-sample net performance, risk, drawdowns and turnover. Fit models, any probability recalibration and decision-rule choices using earlier data, then evaluate on untouched subsequent observations; chronological validation must match deployment and information availability.

**Hit-rate curve terminology.** A curve formed by binning predicted probabilities and plotting average forecast against empirical hit rate is a reliability/calibration curve. It directly compares claimed event probabilities with frequencies; the ideal population relation is the identity line. A different curve plots a selection threshold against the hit rate among selected observations. That measures screening behavior and is not directly the same calibration diagnostic. If the horizontal axis is an arbitrary signal score rather than a probability, an identity-line calibration interpretation does not follow.

References consulted for the requested evaluation discussion: [scikit-learn probability calibration](https://scikit-learn.org/stable/modules/calibration.html), [chronological validation](https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split), and [prediction probabilities versus decision thresholds](https://scikit-learn.org/stable/modules/classification_threshold.html).

## Assessment history

- [2026-10-20 Q4 — assessment](../../DailyTests/2026-10-20.md#q4--probability-forecasts-and-classification-accuracy)

## Related questions and knowledge

- [P035 — Shared Unknown Win Probability and Predictive Risk](../Probability/P035_Shared_Unknown_Win_Probability_and_Predictive_Risk.md) — Predictive probability and the evaluation of its quality.
- [T010 — Deployment Probabilities and Decisions](T010_Deployment_Probabilities_and_Decisions.md) — Calibration and decision thresholds answer different questions.
- [T007 — Random Forest Rates Signals and Time-Series Validation](T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md) — Probability scoring requires chronological out-of-sample evaluation.
