# P033 — Gaussian Sign Prediction and Conditional Return

## Metadata

- Category: Probability
- Tags: Gaussian Geometry, Conditional Expectation, Signal Evaluation
- Date Added: 2026-10-22
- Original drill dates: 2026-10-18
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-18 Q2

Source and assessment: [2026-10-18 Q2](../../DailyTests/2026-10-18.md#q2--gaussian-sign-prediction-and-conditional-return). The reference material below does not change that attempt’s recorded result.

### Question

A standardized forecast X and standardized future return Y are jointly Gaussian, both mean zero and variance one, with correlation rho strictly between negative one and one. Predict a positive return when X is positive and a negative return otherwise.

Derive sign accuracy explicitly as a function of rho without quoting a Gaussian sign identity. Derive the mean of Y conditional on X being positive. Evaluate both at rho = 1/2 and briefly explain why sign accuracy and mean return conditional on a positive forecast measure different things.

### Key solution

The requested standardized joint density was supplied:

```math
f_{X,Y}(x,y)=\frac{1}{2\pi\sqrt{1-\rho^2}}
\exp\left[-\frac{x^2-2\rho xy+y^2}{2(1-\rho^2)}\right].
```

A geometric representation avoids double integration:

```math
X=Z_1,\qquad Y=\rho Z_1+\sqrt{1-\rho^2}Z_2,
\qquad Z_1,Z_2\text{ independent }N(0,1).
```

The independent standard-normal plane has a uniform direction. The positive half-planes have unit normals with dot product rho; their normals' angle is arccos(rho). Their intersection has angle pi minus that angle. There are two symmetric same-sign sectors:

```math
P(XY\gt0)
=\frac{2[\pi-\arccos(\rho)]}{2\pi}
=1-\frac{\arccos(\rho)}{\pi}.
```

For rho = 1/2, the positive-positive sector spans direction angles from -30 to 90 degrees, width 120 degrees. Counting both same-sign sectors gives accuracy 2/3.

Independence and the zero mean of the second normal give:

```math
E[Y\mid X\gt0]=\rho E[X\mid X\gt0],
\qquad
E[X\mid X\gt0]
=\frac{\int_0^\infty x\phi(x)\,dx}{1/2}
=\sqrt{\frac2\pi}.
```

```math
E[Y\mid X\gt0]=\rho\sqrt{\frac2\pi},
\qquad
\rho=\frac12:\quad E[Y\mid X\gt0]=\frac1{\sqrt{2\pi}}\approx0.399.
```

Accuracy counts correct signs over all predictions; the conditional mean includes gain/loss magnitudes on positive-forecast observations. A high win rate can coexist with poor expected returns if losses are sufficiently large.

## Assessment history

- [2026-10-18 Q2 — assessment](../../DailyTests/2026-10-18.md#q2--gaussian-sign-prediction-and-conditional-return)

## Related questions and knowledge

- [P004 — Two-Out-of-Three Gaussian Signal Triggers and Correlation](P004_Two_Out_of_Three_Gaussian_Signal_Triggers_and_Correlation.md) — Gaussian geometry, correlation and threshold events.
