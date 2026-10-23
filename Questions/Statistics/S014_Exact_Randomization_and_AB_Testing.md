# S014 — Exact Randomization and A/B Testing

## Metadata

- Category: Statistics
- Tags: Randomization, Sharp Null, Exact p Value
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q3

Source and assessment: [2026-10-10 Q3](../../DailyTests/2026-10-10.md#q3--exact-randomization-and-ab-testing). The reference material below does not change that attempt’s recorded result.

### Question

Exactly three of six units are randomly assigned treatment, with no interference. Outcomes are `[1,2,3,4,7,9]`; the last three units are treated. Under zero effect for every unit, find the exact two-sided p-value for treated-minus-control mean, including ties. Decide at 5%, explain exactness without normality, and assess a zero-average-effect null.

### Key solution

The sharp null fixes every potential outcome under reassignment:

```math
Y_i(1)=Y_i(0),\qquad T_{\mathrm{obs}}=\frac{14}{3},\qquad
N_{\mathrm{assignments}}=\binom63=20.
```

Only treated sets $`\{4,7,9\}`$ and $`\{1,2,3\}`$ are at least as extreme:

```math
p=\frac{2}{20}=0.10.
```

Fail to reject at 5%. Exactness comes from the known random assignment distribution. Zero average effect allows heterogeneous individual effects, so it does not identify all missing potential outcomes; the same fixed-outcome permutation test is not automatically exact for that weaker null.

## Assessment history

- [2026-10-10 Q3 — assessment](../../DailyTests/2026-10-10.md#q3--exact-randomization-and-ab-testing)

## Related questions and knowledge

- [S013 — One-Sided Normal Mean Test](S013_One_Sided_Normal_Mean_Test.md) — Exact randomization null versus a model-based sampling distribution.
