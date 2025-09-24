---
title: "Smooth Numbers – 50% Version"
difficulty: "Medium"
tags: ["math", "digit dp", "number theory", "smooth numbers"]
id: 8
---

# Smooth Numbers (Difficulty: Medium)

We define a **smooth number** as a positive integer in which the absolute difference between every pair of adjacent digits is at most **1**.

### Examples
- `123454` and `8987` are smooth, because every adjacent pair of digits differs by 1 or less.  
- `135` is not smooth, since the difference between 1 and 3 is 2.  

Clearly, all **single-digit numbers (1–9)** are trivially smooth, because there are no adjacent digits to compare.

---

Let **S(n)** be the number of smooth numbers in the set:

$$
\{1, 2, \dots, n\}
$$

The **proportion of smooth numbers** is given by:

$$
\frac{S(n)}{n}
$$

- For small **n**, this proportion is quite high (for example, up to 9 it is 100%).  
- As **n** grows, the proportion steadily decreases.

---

Find the **least positive integer n** for which the proportion of smooth numbers is **exactly 50%**.

---

## Solution
The least such **n** is **30**, because:

$$
S(30) = 15, \quad \frac{15}{30} = 50\%
$$


