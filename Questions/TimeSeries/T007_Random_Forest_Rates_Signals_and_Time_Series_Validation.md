# T007 — Random Forest Rates Signals and Time-Series Validation

## Metadata

- Category: Time Series
- Interview Relevance: High
- Tags: Random Forest, Walk-Forward, Leakage, Regime Shift, Purging
- Date Added: 2026-10-06
- Status: Final
- Source: 2026-10-06 interview drill; worked solution added after the timed attempt at the user's request.

## Core Question

You train a Random Forest rates signal on 3 years of daily data, randomly shuffle observations, and run 5-fold CV. OOS $`R^2`$ looks great. Why might you not trust it? Give at least three distinct mechanisms, and redesign the validation.

## Solution

### Distinct Failure Mechanisms

1. **Temporal dependence and split mismatch:** Random folds mix earlier and later observations and often place highly related neighboring observations in training and validation. This measures interpolation in a mixed historical sample, not the actual past-to-future deployment procedure. Dependence is not by itself proof of feature leakage, but it undermines an iid interpretation of the score.
2. **Regime shift / non-stationarity:** Shuffling spreads regimes across folds. Real deployment may encounter a new regime absent from training; a strong average across mixed regimes need not transfer.
3. **Overlapping future labels:** Multi-day return targets for adjacent dates share future price increments. A training label can extend into the validation period, compromising separation even when row dates differ.
4. **Feature / preprocessing leakage:** Future-looking windows, revised data unavailable at prediction time, or preprocessing and feature selection fitted on the full sample leak information. A correctly constructed trailing feature window is not automatically leakage merely because it uses shared past observations.
5. **Repeated selection on CV:** Trying many settings and reporting the best CV score creates selection optimism, even with sensible chronological splits.

### Validation Redesign

- Specify the prediction timestamp, data availability, target horizon, and realistic trading delay.
- Reserve a final chronological holdout. Tune models on earlier data using nested or otherwise separated chronological validation.
- Use expanding-window or rolling-window walk-forward folds: train on the past, validate on the next block, then advance.
- At each boundary, purge training observations whose label information extends into the validation interval. Add a gap appropriate to the horizon and information availability. If the split design allows training after a validation block, consider an embargo as well; its length should follow the actual dependence / information structure.
- Fit preprocessing, feature selection, and model tuning within each training fold.
- Inspect fold-by-fold and regime-specific performance, rather than only an average. Three years may cover few independent regimes.
- Evaluate metrics aligned with the objective. Prediction $R^2$ can be useful, but also inspect signal quality and, where a trading strategy is defined, costs, turnover, risk, and drawdowns.

## Interview-Short Answer

“Random CV mixes the time direction, spreads regimes across folds, and may share forward-label information across train and test. I would use chronological walk-forward validation, purge overlapping labels, fit preprocessing within each fold, and keep a final untouched future block. I would also inspect regime stability and trading-relevant metrics.”

## Common Mistakes

- Saying only “leakage” without identifying the information path.
- Presenting a criticism of R-squared as a third distinct leakage mechanism.
- Calling every trailing-window overlap leakage.
- Assuming a fixed arbitrary embargo repairs all leakage.
- Forgetting that the user already understood rolling windows; the drill exposed articulation, not absence of that knowledge.

## Connections

- [S009 — Overlapping returns](../Statistics/S009_Overlapping_Three_Day_Returns_and_Hansen_Hodrick_Inference.md)
- [S005 — Serial dependence and inference](../Statistics/S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md)
- [Daily test: Q6](../../DailyTests/2026-10-06.md#q6--rates-signals-and-time-series-validation)

## What to Remember

Name the mechanism, identify the information crossing the boundary, and make validation resemble deployment.

## Interview drill — 2026-10-07 Q6

Source and assessment: [2026-10-07 Q6](../../DailyTests/2026-10-07.md#q6--five-day-labels-and-walk-forward-validation). The reference material below does not change that attempt’s recorded result.

### Question

A rates signal predicts the next five trading days' cumulative return. Train through T and test from T+1; validation looks excellent. Identify two contamination risks despite chronological ordering, give a concrete safeguard for each, and name a trading-oriented metric alongside predictive fit.

### Recorded solution

1. **Boundary leakage:** a label dated t uses returns through t+5. Purge training rows whose label windows overlap the test window and ensure labels are available at training time. Set any gap from exact information intervals; “start at T+5” alone is not a universal boundary rule.
2. **Dependent test observations:** adjacent five-day labels share four return days. Use non-overlapping test blocks or overlap-aware uncertainty estimates such as block bootstrap / appropriate HAC. Dependence alone is not proof of leakage, but treating it as iid can overstate precision.

Maximum drawdown was the user's metric. Sharpe, turnover, and PnL after costs were additional interviewer suggestions.

### Related Notes

- [T007 — Random Forest Rates Signals and Time-Series Validation](T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md): chronological validation and label purging.
- [S009 — Overlapping Three-Day Returns and Hansen–Hodrick Inference](../Statistics/S009_Overlapping_Three_Day_Returns_and_Hansen_Hodrick_Inference.md): related overlap-aware inference, with a different horizon.

## Interview drill — 2026-10-09 Q5

Source and assessment: [2026-10-09 Q5](../../DailyTests/2026-10-09.md#q5--time-series-validation-and-ridge). The reference material below does not change that attempt’s recorded result.

### Question

A next-day Treasury-return model uses 30 highly correlated lagged features. Randomly shuffled five-fold cross-validation looks excellent, but subsequent-month deployment fails. Explain two misleading-validation mechanisms, redesign validation, and choose Ridge or LASSO.

### Recorded answer details

The discussion preferred rolling validation and Ridge. Name concrete information leakage, regime/covariance shift, and serial or label dependence; do not equate dependence alone with leakage. Ridge distributes weight across correlated predictors; LASSO is useful when sparsity or interpretability is central. See the validation protocol in this note and [L001 — Ridge Regression as PCA Shrinkage](../LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md).

## Interview drill — 2026-10-14 Q3

Source and assessment: [2026-10-14 Q3](../../DailyTests/2026-10-14.md#q3--forecast-validation). The reference material below does not change that attempt’s recorded result.

### Question

Using 1,000 consecutive daily observations, compare two configurations for predicting tomorrow's return from today's information. Specify training/validation windows, refitting and selection. Assess standardizing with all 1,000 days and reporting the selected winner on the same validation periods. What would you investigate if the latest 100 days lose money?

### Key solution

Use chronological rolling or expanding training windows, a specified refit schedule, validation for selection, and a later untouched test for final evaluation. Fit preprocessing parameters only on the training data available at each prediction date.

Whether scaling helps is model-dependent: flags need not be standardized, and tree models often do not benefit. Lagged features can be scaled with fixed training-fitted parameters without losing lag alignment; rolling/window transformations may change level information.

Investigate data/pipeline changes, feature and predictive-relationship shifts, overfitting, regime changes and sampling variation. Recent losses alone do not prove model failure.

## Assessment history

- [2026-10-06 Q6 — assessment](../../DailyTests/2026-10-06.md#q6--rates-signals-and-time-series-validation)
- [2026-10-07 Q6 — assessment](../../DailyTests/2026-10-07.md#q6--five-day-labels-and-walk-forward-validation)
- [2026-10-09 Q5 — assessment](../../DailyTests/2026-10-09.md#q5--time-series-validation-and-ridge)
- [2026-10-14 Q3 — assessment](../../DailyTests/2026-10-14.md#q3--forecast-validation)

## Related questions and knowledge

- [T008 — Tree Extrapolation and Deployment](T008_Tree_Extrapolation_and_Deployment.md) — Match validation to deployment and the model extrapolation limit.
- [T012 — Probability Forecasts, Calibration, and Evaluation](T012_Probability_Forecasts_Calibration_and_Evaluation.md) — Probability scoring requires chronological out-of-sample evaluation.
