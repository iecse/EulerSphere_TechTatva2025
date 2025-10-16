
# Empty Chairs 

## Problem Statement

A group of **people are sitting in a circle**, numbered sequentially from 1 to $n$. Starting from person 1, a counting-out game is played: every **third person** is removed from the circle until only one person remains.

Your task is to determine **the position of the last remaining person**.

For this problem, use the fixed number of people:

$$
n = 20
$$

---

## Input

* No input is required; $n = 20$ and step size $k = 3$ are fixed.

---

## Output

* Print a **single integer**, the position of the last remaining person in the circle.

---

## Task

Write a program to:

1. Simulate the elimination process (every third person removed).
2. Determine the **position of the last remaining person**.
3. Print the **integer position**.

---

## Solution (For Reference)

This is a **Josephus problem** with step size $k = 3$.

**Recursive formula:**

$$
J(n, k) =
\begin{cases} 
1 & \text{if } n = 1 \\
((J(n-1, k) + k - 1) \mod n) + 1 & \text{if } n > 1
\end{cases}
$$

**Step 1:** Apply iteratively for $n = 20$, $k = 3$:

* Last person standing = 20

---

### Answer

$$
\boxed{20}
$$

---

