# SC001 — Itô's Lemma and Discounted Price Martingale

## Metadata

- Category: Stochastic Calculus
- Secondary: Probability, Derivatives Pricing, Rates
- Difficulty: ★★★★☆
- Tags: Itô's Lemma, Brownian Motion, GBM, Risk-Neutral Measure, Martingale, Discounted Price, Change of Measure
- Review Priority: High
- Personal Note: I am less familiar with Itô's lemma and stochastic calculus. Review this again.

## Core Question

Given

```math
dS_t=\mu S_tdt+\sigma S_tdW_t
```

derive:

1. $d\log S_t$
2. $d(e^{-rt}S_t)$
3. Explain why under risk-neutral measure the martingale object is usually discounted price, not $\log S_t$.

## Itô's Lemma

If

```math
dX_t=\mu_tdt+\sigma_tdW_t
```

and

```math
Y_t=f(t,X_t)
```

then

```math
dY_t
=
f_tdt+f_xdX_t+\frac12 f_{xx}(dX_t)^2
```

Using

```math
(dW_t)^2=dt,\qquad dt\,dW_t=0,\qquad dt^2=0
```

we get

```math
\boxed{
df(t,X_t)
=
\left(f_t+\mu_tf_x+\frac12\sigma_t^2f_{xx}\right)dt
+
\sigma_tf_xdW_t
}
```

## Example 1: Log Price

Let

```math
f(S)=\log S
```

Then

```math
f'(S)=\frac1S,\qquad f''(S)=-\frac1{S^2}
```

Given

```math
dS_t=\mu S_tdt+\sigma S_tdW_t
```

Itô's lemma gives:

```math
\boxed{
d\log S_t
=
\left(\mu-\frac12\sigma^2\right)dt+\sigma dW_t
}
```

The term

```math
-\frac12\sigma^2dt
```

is the Itô correction.

## Example 2: Discounted Price

Let

```math
\tilde S_t=e^{-rt}S_t
```

Since $e^{-rt}$ is deterministic,

```math
d(e^{-rt})=-re^{-rt}dt
```

Using Itô product rule:

```math
d(e^{-rt}S_t)
=
e^{-rt}dS_t+S_td(e^{-rt})+d(e^{-rt})dS_t
```

The cross term is zero because $d(e^{-rt})$ only has $dt$.

Therefore:

```math
d(e^{-rt}S_t)
=
e^{-rt}dS_t-re^{-rt}S_tdt
```

Substitute

```math
dS_t=\mu S_tdt+\sigma S_tdW_t
```

Then:

```math
\boxed{
d(e^{-rt}S_t)
=
e^{-rt}S_t[(\mu-r)dt+\sigma dW_t]
}
```

Under risk-neutral measure $Q$,

```math
dS_t=rS_tdt+\sigma S_tdW_t^Q
```

so

```math
\boxed{
d(e^{-rt}S_t)
=
e^{-rt}S_t\sigma dW_t^Q
}
```

Thus:

```math
\boxed{
e^{-rt}S_t \text{ is a martingale under } Q
}
```

## Important Distinction

Under $Q$,

```math
d\log S_t
=
\left(r-\frac12\sigma^2\right)dt+\sigma dW_t^Q
```

So generally:

```math
\boxed{
\log S_t \text{ is not a martingale}
}
```

The martingale object is:

```math
\boxed{
e^{-rt}S_t
}
```

because $S_t$ is a tradable asset and no-arbitrage pricing requires discounted tradable prices to be martingales.

## Change of Measure Intuition

You can choose a new measure to remove the drift of many processes.

For example, one could choose a measure under which $\log S_t$ has zero drift.

But that measure is generally not the pricing measure.

The risk-neutral measure is chosen to make discounted tradable asset prices martingales, not arbitrary functions like $\log S_t$.

## Equity vs Fixed Income

In equity, people often model:

```math
\log S_t
```

or log returns because GBM keeps prices positive and makes log returns normal.

In fixed income, people often model:

- short rate $r_t$
- yield
- forward rate $f(t,T)$
- swap rate
- level/slope/curvature factors

But in both equity and fixed income, no-arbitrage pricing is based on:

```math
\boxed{
\frac{\text{tradable asset price}}{\text{numeraire}}
\text{ is a martingale under the associated pricing measure}
}
```

For money-market numeraire:

```math
B_t=e^{\int_0^t r_sds}
```

the martingale object is:

```math
\frac{P_t}{B_t}
```

For a $T$-bond numeraire, the martingale object is:

```math
\frac{\text{asset price}}{P(t,T)}
```

under the $T$-forward measure.

## Market / Rates Application

Change of measure is used in:

- option pricing
- caplet/floorlet pricing
- swaption pricing
- HJM drift restriction
- futures vs forwards convexity adjustment
- Treasury futures CTD and delivery option pricing
- SOFR futures convexity
- numeraire changes in rates models

Key distinction:

```math
P: \text{forecasting / alpha / realized expected return}
```

```math
Q: \text{pricing / no-arbitrage / hedge ratios}
```

## Common Mistakes

Wrong:

```math
\log S_t \text{ is martingale under } Q
```

Correct:

```math
e^{-rt}S_t \text{ is martingale under } Q
```

Wrong:

```math
d(e^{-rt}S_t)
```

is just ordinary differentiation.

Correct:

It is Itô product rule, but since $e^{-rt}$ is deterministic, the cross term is zero.

Wrong:

Any measure that removes a drift is the risk-neutral measure.

Correct:

Risk-neutral measure removes drift from discounted tradable asset prices.

## What to Remember

```math
\boxed{
d\log S_t
=
\left(\mu-\frac12\sigma^2\right)dt+\sigma dW_t
}
```

```math
\boxed{
d(e^{-rt}S_t)
=
e^{-rt}S_t[(\mu-r)dt+\sigma dW_t]
}
```

```math
\boxed{
e^{-rt}S_t \text{ is martingale under } Q
}
```

```math
\boxed{
\log S_t \text{ is generally not martingale under } Q
}
```

## Connections

- Brownian Motion
- Itô's Lemma
- GBM
- Martingales
- Risk-Neutral Measure
- Change of Measure
- Numeraire Change
- HJM
- SOFR Convexity
- Treasury Futures CTD Optionality
