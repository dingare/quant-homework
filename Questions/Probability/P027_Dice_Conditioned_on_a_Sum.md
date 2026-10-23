# P027 — Dice Conditioned on a Sum

## Metadata

- Category: Probability
- Tags: Conditional Sample Space, Bounded Compositions
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q2

Source and assessment: [2026-10-11 Q2](../../DailyTests/2026-10-11.md#q2--four-dice-conditioned-on-a-sum). The reference material below does not change that attempt’s recorded result.

### Question

Four independent fair six-sided dice have total 10. Without simulation, find $`P(D_1=1\mid\sum D_i=10)`$ and $`P(\max_iD_i\le4\mid\sum D_i=10)`$. Explain the ordered conditional sample space.

### Key solution

Count ordered bounded compositions; all admissible outcomes are equally likely:

```math
N=\binom93-4=80,\qquad
N_{D_1=1}=\binom82-3=25.
```

```math
P(D_1=1\mid\textstyle\sum D_i=10)=\frac{25}{80}=\frac5{16},\qquad
P(\max_iD_i\le4\mid\textstyle\sum D_i=10)=\frac{44}{80}=\frac{11}{20}.
```

## Assessment history

- [2026-10-11 Q2 — assessment](../../DailyTests/2026-10-11.md#q2--four-dice-conditioned-on-a-sum)

## Related questions and knowledge

- [P021 — Conditional Red-Ball Positions](P021_Conditional_Red_Ball_Positions.md) — Conditioning first to identify the correct finite sample space.
