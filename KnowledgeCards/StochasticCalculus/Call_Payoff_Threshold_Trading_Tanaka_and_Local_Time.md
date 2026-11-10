# Call Payoff vs Threshold Trading: Review Map

## Metadata

- Category: Stochastic Calculus
- Tags: Call Replication, Self-Financing, Tanaka Formula, Local Time
- Date Added: 2026-10-30
- Status: Companion review card; understanding remains provisional. Reorganization does not establish an independent solve.

## Core Question and Solution

The full prompt, intuition, worked examples, and mathematical solution now have one canonical home:

**[SC007 — Call Replication, Threshold Trading, and Local Time](../../Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md).**

## Intuition and Reading Order

1. [Intuition](../../Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md#intuition): why a drawn path supports the proposed strategy and why discrete crossings create a discrepancy.
2. [Solution](../../Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md#solution): define the cash account, work through the numerical example, then introduce Brownian roughness, Tanaka's formula, and local time.
3. [Common Mistakes](../../Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md#common-mistakes): distinguish intrinsic value, funded wealth, option premium, and pre-expiry delta.
4. [What to Remember](../../Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md#what-to-remember): short interview answer and independent-review checklist.

## Interview assessment — 2026-10-30

[Preserved assessment and answer boundary](../../Questions/StochasticCalculus/SC007_Call_Replication_Threshold_Trading_and_Local_Time.md#interview-assessment--2026-10-30).

Latest completion self-report remains **at most about 20%**. The recorded answer was a short near-expiry downward crossing through 100. Hint usage and actual time were not recorded; the full continuous-time explanation remains unverified. This was a real interview, not a DailyTests session.

## Connections

- [SC001 — Itô's Lemma](../../Questions/StochasticCalculus/SC001_Itos_Lemma_and_Discounted_Price_Martingale.md): the smooth chain rule and its quadratic-variation correction.
- [SC002 — Change of Measure](../../Questions/StochasticCalculus/SC002_Change_of_Measure_I_Understanding_P_Q_and_the_Radon_Nikodym_Derivative.md): risk-neutral expectation versus physical-measure dynamics.
- [P002 — Fair Games and Stop-Loss](../../Questions/Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md): martingale reasoning for trading and stopping rules.

## What to Remember

Matching the slope of intrinsic value is only the beginning. Check the financing condition and the path model. In a continuous Brownian model, the intrinsic-value change exceeds the self-financing threshold gain by half the local time at the strike.
