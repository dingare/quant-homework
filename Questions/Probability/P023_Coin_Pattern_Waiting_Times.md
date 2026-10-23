# P023 — Coin Pattern Waiting Times

## Metadata

- Category: Probability
- Tags: Suffix States, First-Step Recursion, Absorbing Chains
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08, 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q2

Source and assessment: [2026-10-08 Q2](../../DailyTests/2026-10-08.md#q2--hh-versus-ht-waiting-times). The reference material below does not change that attempt’s recorded result.

### Question

Flip a fair coin until HH first appears. Find the expected number of flips. Repeat for HT and explain why the expectations differ, without simulation.

### Recorded solution

Let $`E_0`$ denote no useful suffix and $`E_H`$ a trailing H. Both satisfy $`E_0=1+E_0/2+E_H/2`$. For HH, $`E_H=1+E_0/2`$; for HT, $`E_H=1+E_H/2`$. In the HT problem, another H preserves progress; in HH, T resets it.

With transient states ordered as (empty, H):

```math
Q_{HH}=\begin{pmatrix}1/2&1/2\\1/2&0\end{pmatrix},
\qquad Q_{HT}=\begin{pmatrix}1/2&1/2\\0&1/2\end{pmatrix},
\qquad t=\mathbf{1}+Qt=(I-Q)^{-1}\mathbf{1}.
```

### Recorded answer details

The recorded expectations are 6 flips for HH and 4 for HT.

### Related Notes

- [P019 — HH vs HTT Pattern Race](P019_HH_vs_HTT_Pattern_Race.md): same suffix-state representation; a race probability rather than this waiting-time question.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md).

## Interview drill — 2026-10-09 Q2

Source and assessment: [2026-10-09 Q2](../../DailyTests/2026-10-09.md#q2--expected-waiting-time-for-hth). The reference material below does not change that attempt’s recorded result.

### Question

Repeatedly flip a fair coin until HTH first appears. Derive the expected number of flips.

### Recorded solution

Use states for the longest suffix that is also a prefix of HTH: empty, H, and HT. Self-overlap matters because after `H + H`, the useful suffix remains H.

### Recorded answer details

The corrected transition from HT on T returns to the empty state: $`E_{HT}=1+E_0/2`$. The recorded expected waiting time is 10 flips.

## Assessment history

- [2026-10-08 Q2 — assessment](../../DailyTests/2026-10-08.md#q2--hh-versus-ht-waiting-times)
- [2026-10-09 Q2 — assessment](../../DailyTests/2026-10-09.md#q2--expected-waiting-time-for-hth)

## Related questions and knowledge

- [P019 — HH vs HTT Pattern Race](P019_HH_vs_HTT_Pattern_Race.md) — Suffix states; waiting time versus competing-pattern probability.
- [P028 — Branching Process Extinction](P028_Branching_Process_Extinction.md) — First-step recursion and boundary/root selection.
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md) — Knowledge card.
