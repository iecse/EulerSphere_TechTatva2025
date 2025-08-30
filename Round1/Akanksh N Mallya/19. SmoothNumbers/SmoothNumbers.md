### Question (Difficulty: Medium–High)

Working from left to right, if the absolute difference between every pair of adjacent digits is at most **1**, we call the number a **smooth number**.

**Examples:**
- `123454` and `8987` are smooth (all adjacent differences ≤ 1).
- `135` is not smooth (difference between 1 and 3 is 2).

Clearly, all **single-digit numbers (1–9)** are trivially smooth, since there are no adjacent digits to compare.

We shall call any number that is not smooth a **rough number**.

Define **S(n)** as the count of smooth numbers from 1 to n.

The **proportion** of smooth numbers is therefore:

$$
\frac{S(n)}{n}
$$

- For small n, this proportion is large (for example, up to 9 it is 100%).
- As n grows, the proportion steadily decreases, since random digits are unlikely to remain close together.
