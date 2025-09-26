Perfect — this is Project Euler **Problem 247** (Squares under a hyperbola).
We can absolutely convert this into a **medium-hard hackathon question** by:

* Using a **smaller region** (so that brute-force or simulation is feasible in under a minute).
* Asking participants to find **the largest $n$** for a given fixed index $(a, b)$.
* Keeping **fixed inputs** and **one fixed output** so that it’s checkable.

Here’s a hackathon-ready version for you:

---

# Hackathon Challenge – Squares Under a Curve

## Problem Statement

Consider the region in the coordinate plane defined by:

$$
1 \leq x, \quad 0 \leq y \leq \frac{1}{x}
$$

We fill this region with **non-overlapping squares** in the following way:

* $S_1$ is the largest square that can fit entirely under the curve.
* $S_2$ is the largest square that fits in the remaining area, and so on.
* This process continues until no more squares can fit.

---

### Index Definition

Each square $S_n$ is assigned an **index** $(L, B)$, where:

* $L$ = number of squares to the **left** of $S_n$
* $B$ = number of squares **below** $S_n$

For example:

* $S_2$ has index $(1, 0)$ (one square to its left, none below).
* $S_{32}$ and $S_{50}$ both have index $(1, 1)$.
* $S_{50}$ is the largest $n$ with index $(1, 1)$.

---

## Task

**Find the largest $n$ such that the index of $S_n$ is $(2, 2)$.**

---

## Input

No input is required — the region and the index $(2, 2)$ are fixed.

---

## Output

Print a **single integer**, the **largest $n$** for which $S_n$ has index $(2, 2)$.

---

## Example (for a smaller region)

If we considered a smaller region and only filled squares until $n=10$,
and if $S_4$ and $S_6$ both had index $(1, 0)$,
the answer would be $6$ (the largest $n$ with that index).

---


