# S024 — Multiple Testing and Independent Confirmation

## Metadata

- Category: Statistics
- Tags: Multiple Testing, Research Selection, Independent Confirmation
- Date Added: 2026-10-24
- Original drill: October 23, 2026, Q3
- Status: Discussed through October 25; full worked reference. Overall Partial / Hinted; independent subparts and assistance are recorded in the dated assessment.

## Core Question

A researcher tests 100 candidate strategies on the same discovery period. Under the global null, every strategy has zero alpha, and each test produces a valid continuous p-value.

1. First assume the 100 p-values are independent and Uniform(0,1). The smallest observed p-value is 0.01. Derive the probability, under the global null, of observing a minimum at least this small. Does this support a 5% claim that at least one strategy has alpha? An exact expression is sufficient.
2. Now remove independence while retaining valid marginal p-values. Give a common rejection threshold that guarantees the probability of any false rejection is at most 5%, regardless of dependence. Justify the guarantee.
3. The researcher freezes exactly one strategy using only discovery data, then conducts one prespecified test on fresh data independent of the entire discovery period. Its p-value is 0.03. Can this be a valid 5% confirmatory rejection without adjusting for the original 100 candidates? Explain the conditioning argument and the essential conditions.

Keep the discussion interview-length.

## Solution

### 1. Independent discovery tests

Under the global null, the minimum p-value is at most the observed 0.01 exactly when at least one test reports a p-value no larger than 0.01. Independence gives:

```math
P\left(\min_{1\le i\le100}p_i\le0.01\right)
=1-P(p_1\gt0.01,\ldots,p_{100}\gt0.01)
=1-0.99^{100}\approx0.634.
```

The user's independently stated decision not to reject was correct. The submitted value 0.99 to the power 100, approximately 0.366, is the probability that every p-value exceeds 0.01, the complementary event. The assistant supplied the complement calculation. Subsequent discussion of “at least this small” clarified English wording: as small as 0.01 or smaller. Do not infer a general conceptual gap from that wording question alone.

Even when all 100 strategies have zero alpha, a minimum this small or smaller occurs about 63.4% of the time. The selected minimum therefore does not establish significance at the 5% familywise level.

### 2. Unknown dependence

Independence is no longer available for multiplying probabilities, but each marginal null p-value still satisfies the uniform assumption. Let A_i denote rejection of test i at threshold t. The union bound requires no independence:

```math
P\left(\bigcup_{i=1}^{100}A_i\right)
\le\sum_{i=1}^{100}P(A_i)=100t.
```

Choose:

```math
\boxed{t=\frac{0.05}{100}=0.0005}.
```

Reject a strategy's null only when its p-value is at most 0.0005. This Bonferroni correction guarantees that the chance of at least one false rejection is no more than 5%, under any dependence structure. The actual familywise error may be smaller; this is a bound, not an independence-based exact probability.

More generally, a valid null p-value need only satisfy the inequality below, which also suffices for this bound; exact equality is the stated uniform-null setting:

```math
P(p_i\le t)\le t.
```

The user confirmed the marginal-uniform versus joint-independence distinction, then requested how to proceed without independence. The union bound, threshold and justification were supplied rather than independently derived.

### 3. Independent confirmation after discovery selection

Let D be all discovery data. Conditional on D, the selected strategy and prespecified test are fixed. If that strategy's null is true, independence of the new data and a correctly calibrated confirmation test give:

```math
P(p_{\mathrm{new}}\le0.05\mid D)\le0.05.
```

Averaging over discovery data preserves the bound in the global-null setting:

```math
P(p_{\mathrm{new}}\le0.05)
=E\left[P(p_{\mathrm{new}}\le0.05\mid D)\right]\le0.05.
```

Thus the fresh p-value 0.03 can reject at 5% for this one confirmatory test without dividing the threshold by the original 100 candidates. Selection occurred on discovery data; the confirmation data were not used to choose the strategy or test.

Essential conditions: freeze the strategy and testing protocol before examining the new data; use data independent of the entire discovery process; conduct the one prespecified valid test. Continuing to tune strategies, select results or repeatedly test on the supposed holdout changes the procedure and requires reassessing the error guarantee.

The user's “yes” was independently correct before the assistant supplied the conditional argument and conditions. The complete proof is assisted work, not an independently verified derivation.

## Assessment History

- [October 23 drill Q3 — continued through October 25](../../DailyTests/2026-10-23.md#q3--multiple-testing-and-independent-confirmation)

## Connections

- [P010 — Bayesian Signal Selection under Multiple Testing](../Probability/P010_Bayesian_Signal_Selection_under_Multiple_Testing.md): Bayesian posterior evidence versus the familywise frequentist error guarantee here; the two questions use different inferential targets.
- [T007 — Random Forest Rates Signals and Time-Series Validation](../TimeSeries/T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md): information separation between selection and final evaluation. The independence assumption in this question is explicit and should not be assumed automatically for market time-series data.
