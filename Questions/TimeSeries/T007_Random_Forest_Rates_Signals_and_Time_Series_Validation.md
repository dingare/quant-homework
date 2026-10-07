# T007 — Random Forest Rates Signals and Time-Series Validation

## Metadata

- Category: Time Series
- Interview Relevance: High
- Tags: Random Forest, Walk-Forward, Leakage, Regime Shift, Purging
- Date Added: 2026-10-06
- Status: Final
- Source: 2026-10-06 interview drill; worked solution added after the timed attempt at the user's request.

## Core Question

Train a Random Forest rates signal on three years of daily observations. Randomly shuffle the data and run five-fold cross-validation. OOS $R^2$ looks great. Give at least three distinct reasons for skepticism and redesign validation.

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
