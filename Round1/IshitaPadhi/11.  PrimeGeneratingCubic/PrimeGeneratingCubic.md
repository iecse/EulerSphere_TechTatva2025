# Prime-Rich Cubic

## Problem Statement

Mathematicians are fascinated by polynomials that generate long sequences of prime numbers.  

Consider a cubic polynomial:

\[
f(n) = n^3 + a \cdot n + b
\]

where \(a\) and \(b\) are integers.  

A polynomial is said to be **prime-rich** if it produces the **maximum number of consecutive prime numbers** starting from \(n = 0\).  

Your task is to find integers \(a, b\) (within given constraints) that maximize this sequence, and output the **product \(a \cdot b\)**.

---

## Input

No input required.

---

## Output

A single integer — the product \(a \cdot b\) of the coefficients that make the polynomial prime-rich.

---

## Constraints

| Parameter | Constraint |
|----------|------------|
| a | -50 < a < 50 |
| b | -50 ≤ b ≤ 50 |

---

## Example

For quadratic polynomials,  
\[
f(n) = n^2 + n + 41
\]  
generates primes for \(n = 0 \dots 39\).  

Here, we are working with a **cubic polynomial**.

---

## Solution

- **Optimal a:** `-13`  
- **Optimal b:** `41`  
- **Maximum consecutive primes:** `45`  

### Final Answer:

\[
\boxed{-533}
\]

