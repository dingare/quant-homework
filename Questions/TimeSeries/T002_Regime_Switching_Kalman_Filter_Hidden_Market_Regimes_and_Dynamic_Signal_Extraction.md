# T002 — Regime-Switching Kalman Filter: Hidden Market Regimes and Dynamic Signal Extraction

## Metadata

- Category: Time Series
- Secondary: Bayesian Inference, State Space Models, Market Regimes
- Difficulty: ★★★★★
- Tags: Kalman Filter, Hidden Markov Model, Regime Switching, Bayesian Updating, Latent State
- Review Priority: High
- Date Added: 2026-07-05
- Status: Draft
- Personal Note: Position this as "multiple competing state-space models updated online," not just a more complicated Kalman filter.

## Core Question

Suppose the hidden state evolves as

```math
x_t=A_{s_t}x_{t-1}+w_t
```

where

```math
s_t\in\{0,1\}
```

is an unobserved Markov regime, and observations satisfy

```math
y_t=Hx_t+v_t.
```

How do we estimate both the latent factor $x_t$ and the hidden regime $s_t$ at the same time?

## Why This Topic Matters

A standard Kalman filter assumes one stable linear system. Real markets often switch between different dynamics:

- normal liquidity versus stressed liquidity,
- trend versus mean reversion,
- risk-on versus risk-off,
- stable funding versus balance-sheet stress.

The same observed move can mean different things in different regimes.

## Relationship to T001

`T001` covers one state-space model with one set of dynamics.

This note extends that idea by allowing several candidate models and continuously updating belief over which one is active.

## My Current Understanding

There are now two hidden objects:

- a continuous latent state $x_t$,
- a discrete hidden regime $s_t$.

Each regime has its own dynamics, such as:

- transition matrix,
- process covariance,
- possibly observation covariance.

So filtering means both:

1. estimating the latent factor within each regime,
2. updating the probability of each regime after seeing new data.

## Intuition

Instead of saying "there is one hidden market state," say:

"there are several possible hidden worlds, and each new observation changes which one I believe."

That is why this feels like Bayesian model selection running in real time.

## Conceptual Filtering Loop

At time $t-1$, carry forward:

- the posterior state estimate for each regime path,
- the posterior probability of each regime.

At time $t$:

1. Use the regime transition matrix to predict regime probabilities.
2. For each candidate regime, run the corresponding Kalman prediction and update.
3. Compute the likelihood of the new observation under each regime.
4. Reweight regime probabilities using Bayes' rule.
5. Combine or collapse the regime-specific state estimates if needed.

## Why One Kalman Filter Is Not Enough

Ordinary Kalman filtering handles uncertainty within one model.

Regime shifts are different: they are structural changes in the governing dynamics. If the data-generating process itself changes, one fixed transition matrix can systematically misread the signal.

## Common Mistakes

- Treating the hidden regime as just another continuous latent factor.
- Ignoring the explosion of possible regime paths over time.
- Forgetting that regime inference depends on both transition probabilities and observation likelihoods.
- Assuming more regimes automatically produce better forecasts.

## Interview Follow-Ups

- How does this relate to Hidden Markov Models?
- Why do practical implementations need approximation or collapsing steps?
- When would you prefer a switching linear dynamical system over a single Kalman filter?
- How do you diagnose whether detected regimes are real or overfit?

## Market / Rates Application

This framework is useful when the same market variable behaves differently across environments, for example:

- yield curve moves during calm macro periods,
- basis behavior during dealer balance-sheet stress,
- liquidity-sensitive spreads near quarter-end,
- macro signals whose persistence changes across policy regimes.

## What to Remember

A regime-switching Kalman filter is not just a noisier Kalman filter.

It is a joint inference problem over:

- hidden continuous state,
- hidden discrete regime,
- regime-dependent dynamics.
