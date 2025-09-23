# Prime-Rich Cubic

### Description:
Mathematicians are intrigued by polynomials that generate unusually long sequences of prime numbers.

Consider the cubic polynomial:

\[
f(n) = n^{3} + a n + b
\]

where \(a\) and \(b\) are integers.

A polynomial is said to be **prime-rich** if it produces the **maximum number of consecutive primes** starting from \(n = 0\).

Your task is to find integers \(a, b\) within the given constraints that maximize this sequence and output the product \(a \cdot b\).

---

### Constraints:

| Parameter | Constraint |
|----------|-------------|
| \(a\) | \(-50 < a < 50\) |
| \(b\) | \(-50 \leq b \leq 50\) |

---

### Example:
For quadratic polynomials:

\[
f(n) = n^{2} + n + 41
\]

produces primes for \(n = 0, 1, \dots, 39\).

In this problem, we focus on **cubic polynomials**.

---

### Solution Approach (Algorithm):
1. Iterate over all values of \(a, b\) within the given range.
2. For each pair \((a, b)\):
   - Start from \(n = 0\) and keep computing \(f(n)\).
   - Check if \(f(n)\) is prime.  
   - Stop when \(f(n)\) is not prime and count the consecutive primes generated.
3. Track the pair \((a, b)\) that gives the **longest prime run**.
4. Output the product \(a \cdot b\).

---

### Solution:
The optimal coefficients are:

\[
a = -13, \quad b = 41
\]

which generate \(45\) consecutive primes.

---

### Answer:
