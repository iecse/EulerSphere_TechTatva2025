## DeterminantBlast (Difficulty: Easy)

Find the value of the following determinant:

$$
\Delta = \begin{vmatrix}
a-b-c & 2a & 2a \\
2b & b-c-a & 2b \\
2c & 2c & c-a-b
\end{vmatrix}
$$

**Input Sets:**
1.  $a = 1, b = 1, c = 1$
2.  $a = 1, b = 2, c = 3$
3.  $a = 2, b = 0, c = -1$
4.  $a = 5, b = -2, c = -3$
5.  $a = 10, b = 5, c = -5$

### Then find the sum of all the answers with respect to each set

***

## Solution

The key to solving this is to simplify the matrix using row and column operations.

### Step 1: Simplify the First Row

A good first step is to see if adding rows or columns together creates a common term. Let's apply the row operation $R_1 \to R_1 + R_2 + R_3$.

* **First element:** $(a-b-c) + 2b + 2c = a+b+c$
* **Second element:** $2a + (b-c-a) + 2c = a+b+c$
* **Third element:** $2a + 2b + (c-a-b) = a+b+c$

This simplifies the determinant to:
$$
\Delta = \begin{vmatrix}
a+b+c & a+b+c & a+b+c \\
2b & b-c-a & 2b \\
2c & 2c & c-a-b
\end{vmatrix}
$$

### Step 2: Factor Out the Common Term

Now, we can factor out the common term $(a+b+c)$ from the first row ($R_1$).

$$
\Delta = (a+b+c) \begin{vmatrix}
1 & 1 & 1 \\
2b & b-c-a & 2b \\
2c & 2c & c-a-b
\end{vmatrix}
$$

### Step 3: Create Zeros in the First Row

Having a row of 1s makes it easy to create zeros, which simplifies the final calculation. We'll use column operations:
1.  $C_2 \to C_2 - C_1$
2.  $C_3 \to C_3 - C_1$

Applying these operations gives us:
$$
\Delta = (a+b+c) \begin{vmatrix}
1 & 1-1 & 1-1 \\
2b & (b-c-a) - 2b & 2b - 2b \\
2c & 2c - 2c & (c-a-b) - 2c
\end{vmatrix}
$$

This results in the much simpler matrix:
$$
\Delta = (a+b+c) \begin{vmatrix}
1 & 0 & 0 \\
2b & -(a+b+c) & 0 \\
2c & 0 & -(a+b+c)
\end{vmatrix}
$$

### Step 4: Calculate the Final Value

The determinant is now in a **lower triangular form**. The determinant of a triangular matrix is simply the product of its diagonal elements.

$$\begin{aligned}
\Delta &= (a+b+c) \times [1 \times (-(a+b+c)) \times (-(a+b+c))] \\
\Delta &= (a+b+c) \times (a+b+c)^2 \\
\Delta &= (a+b+c)^3
\end{aligned}$$

The corresponding solutions are presented in the table below:

| Set | Values (a, b, c) | Calculation (a+b+c) | Determinant Value (a+b+c)³ |
|:---:|:------------------:|:---------------------:|:----------------------------:|
| 1   | (1, 1, 1)          | (1 + 1 + 1) = 3       | $3^3 = 27$                   |
| 2   | (1, 2, 3)          | (1 + 2 + 3) = 6       | $6^3 = 216$                  |
| 3   | (2, 0, -1)         | (2 + 0 - 1) = 1       | $1^3 = 1$                    |
| 4   | (5, -2, -3)        | (5 - 2 - 3) = 0       | $0^3 = 0$                    |
| 5   | (10, 5, -5)        | (10 + 5 - 5) = 10     | $10^3 = 1000$                |

### Final ans = 1244