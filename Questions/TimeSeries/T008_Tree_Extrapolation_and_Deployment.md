# T008 — Tree Extrapolation and Deployment

## Metadata

- Category: TimeSeries
- Tags: Random Forest, Extrapolation, Distribution Shift
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q5

Source and assessment: [2026-10-10 Q5](../../DailyTests/2026-10-10.md#q5--tree-extrapolation). The reference material below does not change that attempt’s recorded result.

### Question

Train a standard mean-leaf random forest on $`x\in[0,1]`$ with $`Y=2+3x+\varepsilon`$, $`E[\varepsilon\mid x]=0`$. Deploy on $`[1.2,1.5]`$. Describe predictions, whether more trees help, and a model change plus evaluation experiment.

### Key solution

With one feature, all points beyond the training splits enter the same leaf in each tree, so the forest is constant across this deployment interval. More trees do not create linear extrapolation. Fit OLS and the forest on the training range, then compare test MAE on independent labeled deployment-range data. A lower-range/higher-range split is only a stress test if actual deployment labels are unavailable.

## Assessment history

- [2026-10-10 Q5 — assessment](../../DailyTests/2026-10-10.md#q5--tree-extrapolation)

## Related questions and knowledge

- [T007 — Random Forest Rates Signals and Time-Series Validation](T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md) — Match validation to deployment and the model extrapolation limit.
