# Fibonacci Matrix Challenge

## Problem Statement

Consider the Fibonacci sequence defined by F₀ = 0, F₁ = 1, and Fₙ = Fₙ₋₁ + Fₙ₋₂ for n ≥ 2.

The Fibonacci numbers can be computed using the matrix equation:

$$\begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Find F₂₀ modulo 1000000007.

## Notes

- Use matrix exponentiation
- Can be computed by hand using repeated matrix multiplication or fast exponentiation
- For verification: F₂₀ should be manageable to compute manually
- Apply modular arithmetic at the final step

## Answer
```
6725
```
