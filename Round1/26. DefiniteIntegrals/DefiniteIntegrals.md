
# Definite Integration 

## Problem Statement

Compute the definite integral of the function

$$
f(x) = 2e^{x^2} - 3\sin(x) + 4\cos(2x)
$$

over the interval

$$
[0,\ \tfrac{\pi}{4}]
$$

That is, evaluate

$$
I = \int_{0}^{\pi/4} \big(2e^{x^2} - 3\sin x + 4\cos 2x\big)\,dx.
$$

> **Note:** $e^{x^2}$ does **not** have an elementary antiderivative, so an analytical closed-form is not expected — you must use a **numerical integration method** (composite Simpson, adaptive Simpson, Gauss–Legendre, etc.) to compute $I$ accurately.

---

## Input

* No input — all values are fixed.

---

## Output

round off your answer and print the nearest integer 
---

## Reference Result

Using a reliable numerical integration I get:

$$
I \approx 3.0848156539861051
$$

Integer part (truncate) =

$$
\boxed{3}
$$

---

 