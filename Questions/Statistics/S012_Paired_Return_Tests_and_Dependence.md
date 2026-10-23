# S012 — Paired Return Tests and Dependence

## Metadata

- Category: Statistics
- Tags: Paired Tests, Covariance, HAC
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08, 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q8

Source and assessment: [2026-10-08 Q8](../../DailyTests/2026-10-08.md#q8--paired-strategy-return-test). The reference material below does not change that attempt’s recorded result.

### Question

Strategies A and B have returns on the same 50 trading days. Test whether expected returns differ: paired or independent two-sample test? Write the statistic and explain how positive correlation between same-day returns affects its standard error.

### Recorded solution

```math
H_0:E[D_t]=0,\qquad t=\frac{\bar D}{s_D/\sqrt{50}},
\qquad Var(D_t)=Var(A_t)+Var(B_t)-2Cov(A_t,B_t).
```

For iid normal differences, compare to a t distribution with 49 degrees of freedom. Same-day cross-strategy correlation is distinct from serial dependence across dates. If differences are serially dependent, use an appropriate HAC standard error or block-based inference rather than assuming iid days.

### Related Notes

- [S005 — HAC / Newey–West Inference](S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md): related serial-dependence correction.
- [S010 — OLS Significance and Robust Standard Errors](S010_OLS_Significance_Randomness_and_Robust_Standard_Errors.md): related inference assumptions.

## Interview drill — 2026-10-09 Q9

Source and assessment: [2026-10-09 Q9](../../DailyTests/2026-10-09.md#q9--paired-test-with-autocorrelation). The reference material below does not change that attempt’s recorded result.

### Question

The archived prompt summary asked for a one-sided paired mean test on `D_t = A_t - B_t`, why the iid paired-test standard error fails under positive serial correlation, and a HAC / Newey–West-style correction. Exact original wording was not retained.

### Reference

See the related notes below. No additional solution was added during this filing migration.

## Assessment history

- [2026-10-08 Q8 — assessment](../../DailyTests/2026-10-08.md#q8--paired-strategy-return-test)
- [2026-10-09 Q9 — assessment](../../DailyTests/2026-10-09.md#q9--paired-test-with-autocorrelation)

## Related questions and knowledge

- [S005 — HAC / Newey–West Inference for Persistent Trading Signals](S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md) — Within-pair covariance versus serial dependence in mean inference.
