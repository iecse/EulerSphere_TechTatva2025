# Modular Matrix Power

## Problem Statement

Consider the matrix:

$$
A = \begin{pmatrix}
7 & 3 & 2 \\
1 & 5 & 4 \\
6 & 2 & 9
\end{pmatrix}
$$

Define the sequence $S_n = \text{tr}(A^n)$ where $\text{tr}$ denotes the trace (sum of diagonal elements).

Let $F(k) = S_k \bmod 97$ for $k \geq 1$.

Find the smallest positive integer $m$ such that $F(m) = F(1)$.

Define:
$$N = \sum_{i=1}^{m} F(i)^2$$

Submit the value of $N$ modulo 1000000007.

## Notes

- Compute matrix powers $A^n$ using fast exponentiation
- Calculate traces $S_n = \text{tr}(A^n)$ for each power
- Find the period where $F(m) = F(1)$ (the cycle length)
- Sum the squares of all $F(i)$ values in one complete cycle
- Apply modular arithmetic only at the final step

## Answer

```
80898
```
