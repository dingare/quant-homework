# P026 — Finite-Horizon Optimal Stopping

## Metadata

- Category: Probability
- Tags: Backward Induction, Continuation Value, Stopping
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q6

Source and assessment: [2026-10-10 Q6](../../DailyTests/2026-10-10.md#q6--finite-horizon-optimal-stopping). The reference material below does not change that attempt’s recorded result.

### Question

Up to three independent $`\mathrm{Uniform}(0,1)`$ draws. First draw free; each redraw costs 0.10 and permanently discards the previous draw. Third draw must be accepted; no recall. Find the optimal policy, expected net payoff and expected draw count.

### Key solution

Work backward. Accept the third draw. Redraw the second below 0.4; the value before seeing the second is:

```math
V_2=0.6(0.7)+0.4(0.5-0.1)=0.58.
```

Redraw the first below $`V_2-0.1=0.48`$:

```math
V_1=0.48(0.58-0.1)+0.52\frac{0.48+1}{2}=0.6152,
\qquad E[N]=1+0.48+0.48(0.4)=1.672.
```

## Assessment history

- [2026-10-10 Q6 — assessment](../../DailyTests/2026-10-10.md#q6--finite-horizon-optimal-stopping)

## Related questions and knowledge

- [P002 — Optional Stopping, Fair Games, and Why Stop-Loss Does Not Create Alpha](P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md) — Stopping policies and the assumptions behind stopping results.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
