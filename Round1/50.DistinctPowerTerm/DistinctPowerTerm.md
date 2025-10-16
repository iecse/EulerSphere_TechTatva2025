
# Problem: Distinct Power Terms with Larger Bases

## Description

Consider all integer combinations of $a^b$ for $10 \leq a \leq 100$ and $10 \leq b \leq 100$. When these values are placed in numerical order with duplicates removed, we obtain a sequence of distinct terms. The challenge is to determine how many such distinct terms exist **without explicitly computing all $91 \times 91 = 8,281$ exponential values**.

## Computational Task

Count the number of distinct values in the set:

$$
\{ a^b \mid 10 \leq a \leq 100,\ 10 \leq b \leq 100 \}.
$$

## Example

For the smaller case $2 \leq a \leq 5$ and $2 \leq b \leq 5$, the distinct terms are:

$$
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
$$

giving **15 distinct terms**. Note that $4^2 = 2^4 = 16$ appears only once.

## Solution Approach

### Computational Approach

A direct computation of all $91^2 = 8,281$ exponentiations is feasible but requires handling very large integers ($100^{100}$ has 201 digits). However, a smarter approach uses the mathematical insight that **duplicates occur when different base-exponent pairs yield the same numerical value**.

### Mathematical Analysis

The key observation is that $a^b = c^d$ can occur when both sides represent the same **perfect power**. Let

$$
a = m^x \quad \text{and} \quad c = m^y
$$

where $m$ is not a perfect power itself (a "primitive" base). Then:

$$
a^b = m^{xb} = m^{yd} = c^d \iff xb = yd
$$

This occurs when the fractions:

$$
\frac{x}{y} = \frac{d}{b}
$$

are equal.

For $10 \leq a \leq 100$, we first identify all numbers that are perfect powers of some primitive base.

### Algorithm

1. Identify all **primitive bases** $m$ in the range $10 \leq m \leq 100$ that are **not perfect powers** themselves.
2. For each primitive base $m$, find the maximum exponent $k_{\max}$ such that $m^k \leq 100$.
3. For each primitive base $m$ and each exponent $k \geq 2$, the values $m^k$ will generate duplicates when raised to different powers.
4. Count distinct values using **inclusion-exclusion principle** to avoid overcounting.

## Final Answer

For $10 \leq a \leq 100$ and $10 \leq b \leq 100$, the number of distinct terms is:

$$
\boxed{8162}
$$


---
