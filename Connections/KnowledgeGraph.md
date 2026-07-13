# Knowledge Graph

Cross-topic relationship map for finalized concepts and interview themes.

## Core Categories

- Linear Algebra
- Probability
- Statistics
- Econometrics
- Time Series
- Optimization
- Coding
- Stochastic Calculus
- Rates Research

## Relationship Notes

- [P001 — Fixed vs Exists Probability Patterns](../Questions/Probability/P001_Fixed_vs_Exists_Probability_Patterns.md): Fixed vs Exists -> Circle Semicircle Problem -> Range -> Boundary Correction -> Complement Counting -> Inclusion-Exclusion
- [L001 — Ridge Regression as PCA Shrinkage](../Questions/LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md): SVD -> PCA -> Eigenvalues of $X^\top X$ -> Multicollinearity -> Ridge Regression -> Bias-Variance Tradeoff -> Rates Factor Models
- [L002 — PCA, Covariance Geometry, and Why Butterfly Trades Curvature](../Questions/LinearAlgebra/L002_PCA_Covariance_Geometry_and_Why_Butterfly_Trades_Curvature.md): Covariance Geometry -> PCA Rotation -> Common vs Spread Direction -> Yield Curve PCA -> Level/Slope/Curvature -> Butterfly Trades -> DV01 Neutrality
- [S001 — OLS Bias vs Variance with Correlated Regressors](../Questions/Statistics/S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md): OLS -> FWL -> Residualization -> Partial Correlation -> Ridge -> PCA -> Factor Attribution
- [S002 — Leave-One-Out OLS via Sherman-Morrison](../Questions/Statistics/S002_Leave_One_Out_OLS_via_Sherman_Morrison.md): Sherman-Morrison -> Leave-One-Out OLS -> Cook's Distance -> Influence Functions -> Recursive Least Squares -> Kalman Filter
- [T001 — Kalman Filter I: Recursive Bayesian Estimation for Noisy Market Signals](../Questions/TimeSeries/T001_Kalman_Filter_I_Recursive_Bayesian_Estimation_for_Noisy_Market_Signals.md): State Space Model -> Recursive Bayesian Estimation -> Innovation -> Kalman Gain -> Precision Weighting -> Market Microstructure Noise -> Yield Curve Factor Extraction
- [T003 — AR(1) First Passage Time and Why Persistence Changes Waiting Time](../Questions/TimeSeries/T003_AR1_First_Passage_Time_and_Why_Persistence_Changes_Waiting_Time.md): AR(1) Persistence -> Stationary Variance -> Threshold Crossing -> First Passage Time -> Geometric Approximation -> Dependence vs Independence -> Stop-Loss Timing
- [T004 — Kalman Filtering II: Covariance-Weighted Bayesian Updating](../Questions/TimeSeries/T004_Kalman_Filtering_II_Covariance_Weighted_Bayesian_Updating.md): Innovation -> Innovation Covariance -> Kalman Gain -> Gaussian Conditioning -> Covariance Weighting -> State Update Geometry
- [O001 — Convex Duality I: No-Arbitrage Pricing through Primal and Dual Optimization](../Questions/Optimization/O001_Convex_Duality_I_No_Arbitrage_Pricing_through_Primal_and_Dual_Optimization.md): Convex Duality -> Super Hedging -> State Prices -> Supporting Hyperplanes -> No-Arbitrage Bands -> Funding Constraints -> FTAP
- [O002 — Constrained Mean-Variance Optimization and the Meaning of Lagrange Multipliers](../Questions/Optimization/O002_Constrained_Mean_Variance_Optimization_and_the_Meaning_of_Lagrange_Multipliers.md): Mean-Variance Optimization -> Equality Constraints -> Lagrange Multipliers -> Shadow Price -> Covariance-Metric Projection -> Factor Neutrality
- [E002 — Efficient IV, Rayleigh Quotient, and Covariance-Weighted Signal Combination](../Questions/Econometrics/E002_Efficient_IV_Rayleigh_Quotient_and_Covariance_Weighted_Signal_Combination.md): Efficient IV -> Rayleigh Quotient -> Inverse Covariance Weighting -> Redundancy Removal -> GMM -> GLS -> Signal Combination
- [SC001 — Itô's Lemma and Discounted Price Martingale](../Questions/StochasticCalculus/SC001_Itos_Lemma_and_Discounted_Price_Martingale.md): Brownian Motion -> Itô's Lemma -> GBM -> Discounted Price -> Martingale -> Risk-Neutral Measure -> Change of Measure -> Numeraire Change

## Update Rule

When a new finalized subject is added:

- Add links to directly related concepts.
- Prefer explicit Markdown links to canonical question files.
- Keep relationships concise and easy to scan.
