# P019 — HH vs HTT Pattern Race

## Metadata

- Category: Probability
- Interview Relevance: High
- Tags: First-Step Analysis, Pattern Matching, Absorbing States
- Date Added: 2026-10-06
- Status: Final
- Source: 2026-10-06 interview drill; worked solution added after the timed attempt at the user's request.

## Core Question

Flip a fair coin until HH or HTT first appears. Find $P(HTT\text{ before }HH)$.

## Solution

Track the longest current suffix that is also a prefix of a target: empty, H, or HT. Let their HTT-win probabilities be $p_0,p_H,p_{HT}$. The absorbing values are 1 for HTT and 0 for HH.

$$
\begin{aligned}
p_0 &= \tfrac12p_0+\tfrac12p_H,\\
p_H &= \tfrac12\cdot0+\tfrac12p_{HT},\\
p_{HT} &= \tfrac12p_H+\tfrac12\cdot1.
\end{aligned}
$$

The transition HT followed by H returns to state H: the trailing H can begin either future pattern. Thus $p_0=p_H$ and

$$
p_H=\tfrac14p_H+\tfrac14,
\qquad
\boxed{P(HTT\text{ before }HH)=\tfrac13}.
$$

The complementary HH-win probability is $2/3$. Absorption occurs almost surely; for example, independent blocks of two flips each have probability 1/4 of being HH, so the chance of avoiding HH forever is zero.

## Intuition

Initial tails only delay the race. Once an H occurs, another H loses immediately; a T advances toward HTT, but the next H resets to H rather than to the empty state.

## Common Mistakes

- Resetting HT followed by H to the empty state loses relevant suffix information.
- Comparing only the probabilities of isolated words ignores overlaps and restarts.
- Treating patterns of different lengths as equally likely race winners.

## Connections

- [P007 — First-step analysis](P007_Unequal_Jump_Random_Walk_First_Step_Analysis.md)
- [Waiting Time and Competing Risks Cookbook](../../KnowledgeCards/Probability/Waiting_Time_and_Competing_Risks_Cookbook.md)
- [Daily test: Q5](../../DailyTests/2026-10-06.md#q5--hh-vs-htt-pattern-race)

## What to Remember

Choose suffix states first, then write transitions. HT plus H goes to H. The answer is 1/3.
