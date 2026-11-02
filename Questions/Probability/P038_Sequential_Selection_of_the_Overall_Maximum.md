# P038 — Sequential Selection of the Overall Maximum

## Metadata

- Category: Probability
- Tags: Sequential Selection, Random Order, Stopping Policy
- Date Added: 2026-11-01
- Original drill: November 1, 2026, Q2
- Status: Pending, unattempted. Original prompt only; no hints or solution supplied.

## Core Question

You observe n distinct candidate scores in uniformly random order. At each arrival, you learn only how that score ranks among those seen so far. You must select exactly one candidate, and rejection is irreversible. Your objective is to select the overall maximum.

Consider this policy:

- Reject the first r candidates.
- Then select the first candidate whose score exceeds every previously observed score, including rejected candidates.
- If none qualifies, select the final candidate.

Assume $`1\le r\lt n`$.

1. Derive the exact success probability as a function of n and r.
2. Explain how to identify the best integer cutoff for a given n, without enumerating arrival orders.
3. For large n, derive the approximately optimal rejected fraction and corresponding success probability.

Justify the reasoning rather than recalling a named rule. A short derivation is sufficient. Original budget: 13 minutes; actual time Not recorded.

## Assessment History

- [November 1 Q2](../../DailyTests/2026-11-01.md#q2--sequential-selection): prompt presented again after Q1; no answer or solving hint. Deferred with Q3–Q4 to November 2 at the user's request. Pending is not Miss.
