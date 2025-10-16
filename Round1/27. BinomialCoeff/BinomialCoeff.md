

# Counting Factors of 2 in a Binomial Coefficient 

## Problem Statement

You are tasked with finding **the number of factors of 2 in a specific binomial coefficient**.

Consider:

$$
n = 25, \quad r = 12
$$

Compute the binomial coefficient:

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

Your goal is to determine the **largest integer $k$** such that:

$$
2^k \, \big| \, \binom{n}{r}
$$

---

## Input

* No input is required from the user; the values of $n$ and $r$ are fixed as above.

---

## Output

* Print a **single integer**, which is the **number of factors of 2** in $\binom{25}{12}$.

---

## Task

Write a program to:

1. Compute the number of times 2 divides the factorials involved (using an efficient method like Legendre’s formula).
2. Calculate the number of factors of 2 in $\binom{25}{12}$.
3. Print the **integer result**.

---

## Solution (For Reference)

**Step 1:** Count factors of 2 in each factorial using **Legendre’s formula**:

$$
\text{Factors of 2 in } n! = \sum_{i=1}^{\infty} \left\lfloor \frac{n}{2^i} \right\rfloor
$$

* For $n = 25$:

$$
\lfloor 25/2 \rfloor + \lfloor 25/4 \rfloor + \lfloor 25/8 \rfloor + \lfloor 25/16 \rfloor = 12 + 6 + 3 + 1 = 22
$$

* For $r = 12$:

$$
\lfloor 12/2 \rfloor + \lfloor 12/4 \rfloor + \lfloor 12/8 \rfloor = 6 + 3 + 1 = 10
$$

* For $n-r = 13$:

$$
\lfloor 13/2 \rfloor + \lfloor 13/4 \rfloor + \lfloor 13/8 \rfloor = 6 + 3 + 1 = 10
$$

**Step 2:** Factors of 2 in $\binom{25}{12}$:

$$
22 - 10 - 10 = 2
$$

---

### Answer

$$
\boxed{2}
$$

---
