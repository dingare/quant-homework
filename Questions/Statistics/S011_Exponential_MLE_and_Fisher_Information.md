# S011 — Exponential MLE and Fisher Information

## Metadata

- Category: Statistics
- Tags: Likelihood, Score, Fisher Information, Asymptotic SE
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q3

Source and assessment: [2026-10-08 Q3](../../DailyTests/2026-10-08.md#q3--exponential-mle-and-fisher-information). The reference material below does not change that attempt’s recorded result.

### Question

For n independent positive interarrival times from an exponential distribution with unknown rate lambda, derive the MLE from the density and then derive its asymptotic standard error.

### Recorded solution

```math
f(x;\lambda)=\lambda e^{-\lambda x},\quad x\gt0,\quad\lambda\gt0,
\qquad \ell(\lambda)=n\log\lambda-\lambda\sum_iX_i.
```

```math
s_n(\lambda)=\ell'(\lambda)=\frac n\lambda-\sum_iX_i,
\qquad \hat\lambda=\frac n{\sum_iX_i}=\frac1{\bar X}.
```

The score is the slope of log-likelihood. Under regularity conditions, $`I_1(\lambda)=E[s_1^2]=-E[\ell_1'']=1/\lambda^2`$ and $`I_n=nI_1`$. Thus:

```math
\sqrt n(\hat\lambda-\lambda)\xrightarrow{d}N(0,\lambda^2),
\qquad \widehat{SE}(\hat\lambda)=\frac{\hat\lambda}{\sqrt n}.
```

Inverse information gives asymptotic variance, not an exact finite-sample variance. The curvature identity requires regularity; parameter-dependent support can invalidate the usual argument.

### Related Notes

- [New MLE / Fisher-information / asymptotic-SE gap](../../Backlog.md#october-8-interview-knowledge-gaps): historical gap record from before this canonical note was filed.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md): related exponential waiting-time model, not an MLE reference.

## Assessment history

- [2026-10-08 Q3 — assessment](../../DailyTests/2026-10-08.md#q3--exponential-mle-and-fisher-information)

## Related questions and knowledge

- [S021 — Uniform Endpoint Estimation and Exact Bounds](S021_Uniform_Endpoint_Estimation_and_Exact_Bounds.md) — Estimator inference; regular likelihood versus parameter-dependent support.
- [S018 — Ratio-of-Means Inference](S018_Ratio_of_Means_Inference.md) — Asymptotic distribution, plug-in standard error and conditions.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
