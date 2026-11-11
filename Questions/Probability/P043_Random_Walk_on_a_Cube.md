# P043 — Random Walk on a Cube

## Metadata

- Category: Probability
- Tags: Random Walk, Conditional Reasoning, Expected Hitting Time
- Date Added: 2026-11-11
- Original drill: November 10, 2026, Q2.
- Status: Discussed. Correct answers and Markov-chain method reported independently; detailed written derivations were not submitted.

## Core Question

An ant starts at vertex A of a cube. At each step, independently of its earlier choices, it chooses uniformly among the three edges incident to its current vertex and traverses that edge. Let B be the vertex diagonally opposite A.

1. What is the expected number of steps until the ant first reaches B?
2. What is the probability that it reaches B before its first return to A after departure?

Derive both answers. You may introduce a small system of equations, but explain why your chosen states contain enough information.

## Answers and Method Record

1. The expected hitting time from A to B is **10 steps**.
2. The probability of reaching B before the first positive-time return to A is **2/5**. Its complement, 3/5, is the probability of returning to A first.

The user reported a Markov-chain derivation for part 1 and explicitly confirmed that both parts were independently derived correctly. The initial 3/5 entry for part 2 was explicitly clarified as a typo for 2/5. Preserve it as a typing correction, not a conceptual error, hint requirement, or failed derivation. No full state equations were submitted; this note does not invent them or claim direct verification of unseen working.

## Assessment History

- [November 10 Q2, continuation November 11](../../DailyTests/2026-11-10.md#q2--random-walk-on-a-cube): Cold Solve by explicit user report; detailed derivations unsubmitted and unverified; part-2 typo corrected without a gap label.
