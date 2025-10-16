# Polynomial Determinant Challenge

## Problem Statement

Consider the polynomial matrix:

$$
M = \begin{pmatrix}
x+2 & 3 & 1 \\
2 & x-1 & 4 \\
1 & 2 & x+3
\end{pmatrix}
$$

Let $P(x) = \det(M)$ be the characteristic polynomial.

Find the coefficient $c_2$ of $x^2$ in the polynomial $P(x)$.

Define:
$$N = c_2^3 + 7 \cdot c_2^2 - 15 \cdot c_2 + 100$$

Submit the value of $N$ modulo 1000000007.

## Notes

- Expand the determinant using cofactor expansion or direct calculation
- Extract the coefficient of $x^2$ from the resulting polynomial
- All arithmetic should be exact (no approximations)
- Apply modular arithmetic only at the final step

## Answer

```
216
```
