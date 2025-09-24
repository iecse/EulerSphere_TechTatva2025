# Fibonacci Matrix Challenge

## Problem Statement

Consider the Fibonacci sequence defined by $F_0 = 0$, $F_1 = 1$, and $F_n = F_{n-1} + F_{n-2}$ for $n \geq 2$.

The Fibonacci numbers can be computed using the matrix equation:
$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Find $F_{100}$ modulo 1000000007.

## Notes

- Use matrix exponentiation: $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$
- Apply fast exponentiation algorithm to compute the matrix power efficiently
- The problem can be solved by hand for small values but requires computation for $F_{100}$
- Apply modular arithmetic throughout to prevent overflow

## Answer

```
687995182
```
