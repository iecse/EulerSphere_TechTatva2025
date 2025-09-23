

# Mini Self-Power Sum

**Problem Statement**

### Description:

The series:

$$
1^1 + 2^2 + 3^3 + \cdots + N^N
$$

is called the **self-power series**.

Your task is simple:

* Given $N = 10$, compute

$$
S = 1^1 + 2^2 + 3^3 + \cdots + 10^{10}
$$

* Then **print the sum of the first 3 digits of $S$**.

---

### Example:

For $N = 3$:

$$
1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32
$$

First 3 digits of `32` are `0 3 2` (pad left with zeros if needed)

$$
\text{Sum} = 0 + 3 + 2 = 5
$$

---

### Input:

No input required. Take $N = 10$ inside your code.

---

### Output:

A single integer – the sum of the first 3 digits of $S$.

---

### Expected Output:

**5**

---

### Explanation:

$$
1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317
$$


### Solution:

First 3 digits: $1, 0, 4$

$$
\text{Sum} = 1 + 0 + 4 = 5
$$

---
