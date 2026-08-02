# P001 — Fixed vs Exists Probability Patterns

## Metadata

- Category: Probability
- Difficulty:
- Interview Relevance:
- Tags: Fixed vs Exists, Circle Semicircle Problem, Range, Streaks, Inclusion-Exclusion
- Date Added: 2026-06-25
- Status: Finalized

## Core Question

This note collects four probability problems with the same core idea:

$$
\text{fixed object/event} \neq \text{there exists some object/event}
$$

The main interview lesson is to avoid fixing a candidate too early. If the problem says "some", "at least one", "exists", or "anywhere", we need to consider all possible candidates and handle overlap carefully.

## Hint

When a problem asks whether something happens somewhere, first ask:

1. What is the probability for one fixed candidate?
2. How many candidates are there?
3. Are those candidate events disjoint or overlapping?

## Solution

### 1. Random Points on a Circle: All Points in Some Semicircle

#### Problem

Pick $N$ random points independently and uniformly on a circle. What is the probability that all points lie in some semicircle?

#### Answer

$$
\boxed{P=\frac{N}{2^{N-1}}}
$$

#### Key Idea

Do not fix the semicircle first.

If a particular semicircle is fixed, then the probability all $N$ points lie in it is:

$$
\left(\frac12\right)^N
$$

But the problem asks whether there exists some semicircle. The semicircle can be chosen after seeing the points.

#### Solution Sketch

Choose one point as the boundary point of the semicircle.

For a fixed boundary point, the other $N-1$ points must fall within the next half-circle:

$$
\left(\frac12\right)^{N-1}
$$

There are $N$ possible boundary points. These events are effectively non-overlapping, ignoring probability-zero ties at exactly opposite points.

Therefore:

$$
P=N\left(\frac12\right)^{N-1}=\frac{N}{2^{N-1}}
$$

### 2. Linear Version: Random Points on $[0,1]$ Covered by a Moving Interval

#### Problem

Let

$$
X_1,\dots,X_N \overset{iid}{\sim} U(0,1)
$$

What is the probability that all points can be covered by some interval of length $a$?

Equivalently:

$$
P(\max X_i-\min X_i\leq a)
$$

#### Answer

$$
\boxed{P(\text{range}\leq a)=Na^{N-1}-(N-1)a^N}
$$

For $a=1/2$:

$$
\boxed{P(\text{range}\leq 1/2)=\frac{N+1}{2^N}}
$$

#### Key Idea

This is the line-segment version of the circle problem, but now there is a boundary effect.

On the circle, intervals can wrap around. On $[0,1]$, they cannot.

#### Solution Sketch

Pick one point $X_i=x$ as the leftmost point.

Then the other $N-1$ points need to lie in:

$$
[x,x+a]
$$

If $x\leq 1-a$, the full length $a$ is available, so the contribution is:

$$
\int_0^{1-a} a^{N-1}\,dx=(1-a)a^{N-1}
$$

If $x\gt 1-a$, the interval hits the right boundary. The available length is only:

$$
1-x
$$

So the contribution is:

$$
\int_{1-a}^{1}(1-x)^{N-1}\,dx=\frac{a^N}{N}
$$

For one chosen leftmost point:

$$
(1-a)a^{N-1}+\frac{a^N}{N}
$$

There are $N$ choices for the leftmost point:

$$
P=N\left[(1-a)a^{N-1}+\frac{a^N}{N}\right]
$$

Simplifying gives:

$$
P=Na^{N-1}-(N-1)a^N
$$

### 3. Coin Toss Streak: At Least One Run of Three Heads

#### Problem

Toss a fair coin 10 times. What is the probability of seeing at least one run of three consecutive heads?

That is:

$$
P(\text{at least one HHH in 10 tosses})
$$

#### Answer

$$
\boxed{\frac{65}{128}\approx 50.78\%}
$$

#### Key Idea

Fixed window is not the same as exists somewhere.

The probability that the first three tosses are HHH is:

$$
\frac18
$$

But the probability that HHH occurs somewhere in 10 tosses is much larger.

We cannot simply multiply by 8 because overlapping windows are not disjoint.

#### Solution Sketch

Use the complement:

$$
P(\text{at least one HHH})=1-P(\text{no HHH})
$$

Let $a_n$ be the number of length-$n$ binary sequences with no HHH.

A valid sequence can end in:

- $T$
- $TH$
- $THH$

So:

$$
a_n=a_{n-1}+a_{n-2}+a_{n-3}
$$

Initial values:

$$
a_0=1,\quad a_1=2,\quad a_2=4
$$

Then:

$$
a_{10}=504
$$

Total sequences:

$$
2^{10}=1024
$$

Therefore:

$$
P(\text{at least one HHH})=1-\frac{504}{1024}=\frac{520}{1024}=\frac{65}{128}
$$

### 4. Occupancy / Empty Box Problem

#### Problem

Throw $n$ balls independently and uniformly into $m$ boxes. What is the probability that at least one box is empty?

$$
P(\exists \text{ empty box})
$$

#### Answer

$$
\boxed{
P(\exists \text{ empty box})=
\sum_{k=1}^{m}
(-1)^{k+1}
\binom{m}{k}
\left(\frac{m-k}{m}\right)^n
}
$$

#### Key Idea

Fixed empty box is not the same as exists some empty box.

For a fixed box:

$$
P(\text{box 1 empty})=\left(1-\frac1m\right)^n
$$

But the problem asks whether any box is empty.

The events overlap: box 1 and box 2 can be empty at the same time.

Therefore, we need inclusion-exclusion.

#### Solution Sketch

Let:

$$
A_i=\{\text{box }i\text{ is empty}\}
$$

We want:

$$
P(A_1\cup A_2\cup\cdots\cup A_m)
$$

If a fixed set of $k$ boxes is empty, then each ball must avoid those $k$ boxes.

For one ball, the probability of avoiding those $k$ boxes is:

$$
\frac{m-k}{m}
$$

For $n$ balls:

$$
\left(\frac{m-k}{m}\right)^n
$$

There are:

$$
\binom{m}{k}
$$

ways to choose the $k$ empty boxes.

By inclusion-exclusion:

$$
P(\exists \text{ empty box})=
\sum_{k=1}^{m}
(-1)^{k+1}
\binom{m}{k}
\left(\frac{m-k}{m}\right)^n
$$

## Key Knowledge Points

- Fixed candidate probability is usually easier than existence probability, but they are not the same object.
- When candidate events are disjoint, symmetry and multiplication can work.
- When candidate events overlap, use complement, recurrence, or inclusion-exclusion.
- Range problems on $[0,1]$ introduce boundary correction that does not appear on the circle.

## Intuition

All four problems share the same warning:

$$
\boxed{
\text{fixed candidate} \neq \text{exists some candidate}
}
$$

The right tool depends on how candidate events interact:

| Problem | Fixed version | Exists version | Main tool |
| --- | --- | --- | --- |
| Circle semicircle | Fixed semicircle | Some semicircle | Symmetry |
| Line interval | Fixed interval | Some interval | Range + boundary correction |
| Coin streak | Fixed window HHH | HHH somewhere | Complement + recurrence |
| Empty boxes | Fixed box empty | Some box empty | Inclusion-exclusion |

## Geometry

$$
\boxed{
\text{circle has no boundary, so no boundary correction is needed}
}
$$

$$
\boxed{
\text{line answer}=\text{circle-style answer}-\text{boundary correction}
}
$$

## Common Mistakes

- Fixing one candidate event and forgetting the problem asks whether some candidate works.
- Multiplying by the number of candidates when the events overlap.
- Missing the boundary effect in interval-coverage problems on $[0,1]$.
- Treating streak problems as disjoint-window problems.
- Forgetting inclusion-exclusion in occupancy questions.

## Interview Follow-ups

When a problem says "some", "exists", "at least one", or "anywhere", ask:

1. What happens if I fix one candidate?
2. How many candidates are there?
3. Do candidate events overlap?
4. If no overlap, can I use symmetry or multiply directly?
5. If overlap, should I use complement, recurrence, or inclusion-exclusion?

## Market / Rates Application

The practical interview value is pattern recognition: many probability questions become easier once we distinguish a fixed event from an existence event and then choose the right counting or conditioning tool.

## Connections

- Circle semicircle problem
- Range and order statistics
- Boundary correction
- Complement counting
- Dynamic programming recurrences
- Inclusion-exclusion

## What to Remember

- "Fixed" and "exists" are often different probability questions.
- Circle versions may avoid boundary effects that appear on line segments.
- Overlap structure determines the method.
- For interview speed, classify the event structure before doing algebra.
