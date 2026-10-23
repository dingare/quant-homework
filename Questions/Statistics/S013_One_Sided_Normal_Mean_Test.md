# S013 — One-Sided Normal Mean Test

## Metadata

- Category: Statistics
- Tags: Sampling Distribution, z Test, Power
- Date Added: 2026-10-22
- Original drill dates: 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-09 Q3

Source and assessment: [2026-10-09 Q3](../../DailyTests/2026-10-09.md#q3--one-sided-z-test-with-known-variance). The reference material below does not change that attempt’s recorded result.

### Question

For iid `N(mu, sigma^2)` observations with known variance, test `H0: mu = 0` against `H1: mu > 0`. Give the statistic, null distribution, 5% rejection region, effect of larger n on power, and Type I / II errors.

### Recorded solution

Interview checklist: estimator → sampling distribution → null distribution → standardize → choose one- or two-sided tail → rejection region / p-value → power and error interpretation.

### Recorded answer details

The recorded sampling distribution is $`\bar X\sim N(\mu,\sigma^2/n)`$. With known variance use a z test; the recorded right-tail 5% rejection threshold is $`Z\gt1.645`$. Use “fail to reject” rather than “accept” the null.

## Assessment history

- [2026-10-09 Q3 — assessment](../../DailyTests/2026-10-09.md#q3--one-sided-z-test-with-known-variance)

## Related questions and knowledge

- [S020 — Most-Powerful Normal Variance Test](S020_Most_Powerful_Normal_Variance_Test.md) — Rejection regions, null calibration and power.
- [S014 — Exact Randomization and A/B Testing](S014_Exact_Randomization_and_AB_Testing.md) — Exact randomization null versus a model-based sampling distribution.
