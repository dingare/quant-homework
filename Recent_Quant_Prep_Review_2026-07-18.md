# Recent Quant Prep Review — 2026-07-18

This review consolidates the latest six daily topics without duplicating canonical notes already in the knowledge base.

## Six-Topic Rotation

| Category | Topic | Core interview idea | Canonical note |
| --- | --- | --- | --- |
| Linear Algebra | Woodbury identity | Move a large covariance solve into a small factor-space system | [L003](Questions/LinearAlgebra/L003_Woodbury_Identity_for_Low_Rank_Covariance_Inversion.md) |
| Probability | Two-out-of-three Gaussian trigger | Convert exceedance counting to a binomial problem; condition on a common factor under correlation | [P004](Questions/Probability/P004_Two_Out_of_Three_Gaussian_Signal_Triggers_and_Correlation.md) |
| Statistics | HAC / Newey–West inference | Correct the long-run variance of the regression score, not residual autocorrelation alone | [S005](Questions/Statistics/S005_HAC_Newey_West_Inference_for_Persistent_Trading_Signals.md) |
| Optimization | Constrained mean–variance portfolio | Use KKT conditions and solve in low-dimensional constraint space | [O002](Questions/Optimization/O002_Constrained_Mean_Variance_Optimization_and_the_Meaning_of_Lagrange_Multipliers.md) |
| Stochastic Processes | OU first hitting time | Convert a stopping-time expectation into a generator boundary-value ODE | [SC003](Questions/StochasticCalculus/SC003_Ornstein_Uhlenbeck_First_Hitting_Time.md) |
| Coding / Algorithms | Count of range sums | Convert interval sums into ordered prefix-sum pairs and count them in $O(n\log n)$ | [C001](Questions/Coding/C001_Count_of_Range_Sums_with_Prefix_Sums_and_Fenwick_Tree.md) |

## One-Line Memory Hooks

1. **Woodbury:** diagonal/idiosyncratic part is easy; correct only in the low-rank factor subspace.
2. **Gaussian trigger:** independence gives a binomial count; equicorrelation becomes conditionally binomial after conditioning on the common Gaussian factor.
3. **HAC:** dependence matters through $x_tu_t$; residual autocorrelation by itself is not enough.
4. **Constrained optimizer:** start from the unconstrained optimum and remove infeasible exposure under the covariance metric.
5. **OU hitting time:** $E_x[\tau]$ solves $\mathcal Lu=-1$, not $\mathcal Lu=0$.
6. **Range-sum counting:** for each $P_r$, count earlier prefixes in $[P_r-U,P_r-L]$ before inserting $P_r$.

## Shared Structure Across the Six Problems

### Reduce dimension before computing

- Woodbury replaces an $n\times n$ inverse with a $k\times k$ factor-space solve.
- Equality-constrained optimization replaces an $n$-variable correction with an $m\times m$ dual system.
- Equicorrelated Gaussian probabilities become a one-dimensional common-factor integral.
- Prefix sums replace $O(n^2)$ interval enumeration with ordered range queries.

### Identify the correct mathematical object

- HAC uses the long-run variance of the score rather than the residual alone.
- OU holding periods require a first-passage calculation rather than the deterministic half-life.
- Portfolio constraints imply a covariance-metric projection rather than an ordinary Euclidean projection.

## Duplicate Check

- Reused existing canonical notes: **L003**, **P004**, and **O002**.
- Added only missing canonical notes: **S005**, **SC003**, and **C001**.
- Did not create another Kalman, FWL, primal/dual, or generic hyperplane-projection note.

## Suggested Review Order

1. Review **L003** and **O002** together: both exploit a small structured system instead of a large explicit inverse.
2. Review **P004** next: the same dimension-reduction instinct appears through conditioning.
3. Review **S005** to separate coefficient estimation from valid inference.
4. Review **SC003**, focusing on how the generator turns a stochastic problem into an ODE.
5. Finish with **C001**, identifying the naive quadratic object and the ordered structure that removes it.
