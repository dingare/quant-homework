# P044 — Uniform Sampling on the Unit Sphere

## Metadata

- Category: Probability
- Tags: Uniform Sampling, Surface Area, Spherical Coordinates, Rotational Symmetry
- Date Added: 2026-11-13
- Status: Partial / Hinted discussion; the two-stage trigonometric construction was proposed independently, while uniform height sampling was supplied.
- Source: User-provided question outside the scheduled daily drill; elapsed time not recorded.

## Core Question

Generate a random point $`(X,Y,Z)`$ uniformly with respect to surface area on the unit sphere:

```math
X^2+Y^2+Z^2=1.
```

The user clarified that the intended radius is one. The target is the sphere's surface.

## Hint

Equal height intervals on the unit sphere have equal surface areas. Sample the height first, then sample uniformly around its horizontal circle.

## Solution

### 1. User's construction: two trigonometric stages

The user proposed first choosing height and horizontal radius so that $`z^2+r^2=1`$, then using sine and cosine to choose $`x,y`$ with $`x^2+y^2=r^2`$. One such parametrization is:

```math
z=\cos\theta,\qquad r=\sin\theta,
\qquad x=r\cos\phi,\qquad y=r\sin\phi.
```

This guarantees that the point lies on the sphere, but does not by itself specify a uniform distribution. Choosing both angles uniformly, with $`\theta\in[0,\pi]`$ and $`\phi\in[0,2\pi)`$, places too much probability near the poles. The user did not specify an angle distribution; this explains the issue with the naive uniform-angle completion, rather than attributing that choice to the user.

### 2. Correct completion: uniform height and azimuth

Draw independently:

```math
Z\sim U[-1,1],\qquad \Phi\sim U[0,2\pi).
```

Then set:

```math
r=\sqrt{1-Z^2},\qquad
X=r\cos\Phi,\qquad Y=r\sin\Phi.
```

These equations retain the user's two-stage construction and produce a point uniformly distributed over the sphere's surface.

### 3. Why uniform height works

A thin horizontal spherical band of height $`dz`$ has area:

```math
dS=2\pi\,dz.
```

Thus equal height intervals correspond to equal surface areas. Uniform height chooses these bands in proportion to their area; an independent uniform azimuth distributes points uniformly around each band.

### 4. Alternative already discussed: normalize a Gaussian vector

Draw three independent standard normal variables and normalize:

```math
A,B,C\overset{\mathrm{iid}}{\sim}N(0,1),
\qquad
(X,Y,Z)=\frac{(A,B,C)}{\sqrt{A^2+B^2+C^2}}.
```

The zero vector has probability zero. Rotational symmetry of the joint Gaussian distribution makes its direction uniform. This was an assistant-provided alternative, not an independently submitted user solution.

## Key Knowledge Points

- Satisfying the sphere equation establishes the support, not the distribution.
- Uniform surface area does not mean uniform polar angle.
- Uniform height and independent uniform azimuth give the correct surface distribution.
- Normalizing a rotationally symmetric Gaussian vector gives another valid construction.

## Intuition

Preserve the user's horizontal-circle construction. The essential choice is how much probability to assign to each height, which is determined by spherical band area.

## Geometry

Near a pole, a horizontal circle is shorter, but the sphere's slant compensates when measuring area per unit height. Consequently the band area per unit height is constant.

## Common Mistakes

- Checking only the identity $`X^2+Y^2+Z^2=1`$ and concluding that the distribution is uniform.
- Choosing the polar angle uniformly, which concentrates points near the poles.
- Confusing uniform sampling on the surface with uniform sampling inside the solid ball.

## Connections

- [P041 — Uniform Extremes: Ratio and Maximum Independence](P041_Uniform_Extremes_Ratio_and_Maximum_Independence.md): both questions require checking the induced distribution under a transformation; a valid change of coordinates alone does not establish the desired density.
- [P031 — Exact Uniform Sampling from a Biased Coin](P031_Exact_Uniform_Sampling_from_a_Biased_Coin.md): both distinguish constructing legal outcomes from producing a specified uniform law.

## Assessment History

Discussion on 2026-11-13, outside the scheduled daily drill. The user independently proposed the two-stage sine/cosine construction. The assistant explained the uniform-angle pitfall and supplied uniform height sampling, the surface-band justification, and the Gaussian-normalization alternative. The user explicitly reported that they had not independently found the step of sampling the height uniformly. Record **Partial / Hinted**, preserving the independent parametrization. No independent full uniformity proof or final implementation was submitted; prior familiarity versus retrieval remains unresolved. No elapsed time or implementation error is inferred, and the filed reference does not establish independent mastery.

## What to Remember

**Uniform surface sampling: choose height uniformly, then choose an independent uniform angle around the horizontal circle.**
