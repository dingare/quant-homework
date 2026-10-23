# S015 — Interaction and Recentering

## Metadata

- Category: Statistics
- Tags: Regression, Interaction, Parameterization, Hypothesis Testing
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q7

Source and assessment: [2026-10-10 Q7](../../DailyTests/2026-10-10.md#q7--interaction-and-recentering). The reference material below does not change that attempt’s recorded result.

### Question

A full-rank unpenalized fit is $`\widehat Y=2+0.8X+0.3Z-0.04XZ`$. Does increasing $`X`$ always raise predictions? Set $`W=Z-10`$; rewrite the fit, assess fitted values/RSS, and compare old/new tests of the main $`X`$ coefficient against zero.

### Key solution

```math
\frac{\partial\widehat Y}{\partial X}=0.8-0.04Z,\qquad
\widehat Y=5+0.4X+0.3W-0.04XW.
```

Fitted values and RSS are unchanged, but main effects refer to different reference levels:

```math
H_{0,\mathrm{old}}:\beta_X=0,\qquad
H_{0,\mathrm{new}}:\beta_X+10\beta_{XZ}=0.
```

```math
\mathrm{Var}(\hat\beta_X+10\hat\beta_{XZ})
=\mathrm{Var}(\hat\beta_X)+100\mathrm{Var}(\hat\beta_{XZ})
+20\mathrm{Cov}(\hat\beta_X,\hat\beta_{XZ}).
```

## Assessment history

- [2026-10-10 Q7 — assessment](../../DailyTests/2026-10-10.md#q7--interaction-and-recentering)

## Related questions and knowledge

- [S023 — Pooled and Within-Sector Signal Evaluation](S023_Pooled_and_Within_Sector_Signal_Evaluation.md) — Regression parameter interpretation depends on controls and centering.
