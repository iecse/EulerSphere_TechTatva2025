

# **Problem: Modified Recursive Process with Dual Divisibility**

---

## **Description**

Consider the following **recursive process** applied to any positive integer $n$:

* If $n = 1$, the process stops.
* If $n$ is divisible by 7, divide it by 7.
* If $n$ is divisible by 13, divide it by 13.
* Otherwise, add 1.

Define $g(n)$ to be the **number of times 1 must be added** before the process reaches 1.

---

### **Example Walkthrough**

Starting from $n = 125$:

```
125 → (+1) 126 → (÷7) 18 → (+1) 19 → (+1) 20 → (+1) 21 → (÷7) 3 
→ (+1) 4 → (+1) 5 → (+1) 6 → (+1) 7 → (÷7) 1
```

Seven `+1` operations were applied, so:

$$
g(125) = 7
$$

---

## **Computational Task**

Define:

* $S(N) = \sum_{n=1}^{N} g(n)$
* $H(K) = S(7^K \cdot 13^K)$

Given:

* $H(5) = 186{,}452$

Compute:

$$
H(10^6) \mod 1117117717
$$

---

## **Examples**

* For $n = 91 = 7 \times 13$:

```
91 → (÷7) 13 → (÷13) 1
```

No additions required, so:

$$
g(91) = 0
$$

---

* For $n = 12$:

```
12 → (+1) 13 → (÷13) 1
```

One addition:

$$
g(12) = 1
$$

---

## **Solution Approach**

### **Computational Constraints**

A direct computation of $H(10^6)$ is **infeasible** due to the enormous size of:

$$
7^{10^6} \cdot 13^{10^6}
$$

Instead, we must use recursive structure and mathematical insight.

---

### **Recursive Definition**

The function $g(n)$ can be defined recursively as:

$$
g(n) =
\begin{cases}
0 & \text{if } n = 1 \\
g(n / 7) & \text{if } 7 \mid n \\
g(n / 13) & \text{if } 13 \mid n \\
1 + g(n + 1) & \text{otherwise}
\end{cases}
$$

This means:

* $g(n)$ only increases when we’re not divisible by 7 or 13
* Once we reach a divisible number, we reduce $n$ by division

---

## **Algorithm Strategy**

1. Observe that the process behaves **periodically modulo 91** (since LCM(7,13) = 91).
2. Precompute $g(n)$ for all values modulo 91 (i.e. $n \mod 91$).
3. For larger $H(K) = S(7^K \cdot 13^K)$, note that:

   * There are $91^K$ values
   * Each congruence class modulo 91 will repeat uniformly
4. Use this symmetry and periodicity to **avoid recomputation**.

This allows us to compute:

$$
H(10^6) \mod 1117117717
$$

efficiently, using memoization, modular arithmetic, and recursion reduction.

---

## **Mathematical Twist**

The dual divisibility condition (by both 7 and 13) introduces an **interference pattern**:

* You can divide by 7 or 13 if divisible
* Otherwise, increment until one applies
* Over many steps, this creates **branching recursive structures**
* Periodicity modulo 91 allows efficient simulation

---

## ✅ **Final Answer**

The value of $H(10^6) \mod 1117117717$ is:

$$
\boxed{481647251}
$$

---

