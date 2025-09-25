
# Indefinite Integration 
## Problem Statement

You are tasked with **computing an indefinite integral** of a more advanced function. Consider:

$$
f(x) = 2e^x - 3\sin(x) + 4\cos(x)
$$

Your goal is to compute its **indefinite integral** $F(x)$, i.e.,

$$
F(x) = \int f(x) \, dx
$$

with the constant of integration $C = 0$.

---

## Input

* No input is required from the user; all values are fixed.
* After finding $F(x)$, **evaluate it at $x = \pi/4$** to get a numerical value.

---

## Output

* Print a **single integer**, which is the **integer part of $F(\pi/4)$** (truncate any decimal part).
* For example, if $F(\pi/4) = 3.87$, the output should be `3`.

---

## Task

Write a program to:

1. Compute the **indefinite integral** of $f(x)$.
2. Evaluate the integral at $x = \pi/4$.
3. Print the **integer part** of the result.

---

## Solution (For Reference)

The indefinite integral of

$$
f(x) = 2e^x - 3\sin(x) + 4\cos(x)
$$

is:

$$
F(x) = 2e^x + 3\cos(x) + 4\sin(x) + C
$$

Evaluate at $x = \pi/4$ ($C = 0$):

$$
F(\pi/4) = 2e^{\pi/4} + 3\cos(\pi/4) + 4\sin(\pi/4)
$$

$$
\approx 2 \cdot 2.193 + 3 \cdot 0.707 + 4 \cdot 0.707
$$

$$
\approx 4.386 + 2.121 + 2.828 = 9.335
$$

**Integer part (truncate):**

$$
\boxed{9}
$$

---

