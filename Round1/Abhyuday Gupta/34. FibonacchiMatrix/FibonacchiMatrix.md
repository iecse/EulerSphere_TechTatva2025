# Fibonacci Matrix Challenge
## Problem Statement
Consider the Fibonacci sequence defined by $F_0 = 0$, $F_1 = 1$, and $F_n = F_{n-1} + F_{n-2}$ for $n \geq 2$.

The Fibonacci numbers can be computed using the matrix equation:

$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Find $F_{20}$ modulo 1000000007.

## Notes
- Use matrix exponentiation: $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$
- Can be computed by hand using repeated matrix multiplication or fast exponentiation
- For verification: $F_{20}$ should be manageable to compute manually
- Apply modular arithmetic at the final step

## Answer
```
6765
```

