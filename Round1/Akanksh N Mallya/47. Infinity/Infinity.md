## Infinity (Difficulty: Medium)

If the system of linear equations

$$
\begin{align*}
3x + y + \beta z &= 3 \\
2x + \alpha y - z &= -3 \\
x + 2y + z &= 4
\end{align*}
$$

has infinitely many solutions, then what is the value of $22\beta - 9\alpha$?

***

## Solution

### Step 1: Condition for Infinitely Many Solutions

For a non-homogeneous system of linear equations to have **infinitely many solutions**, two conditions must be met:

1.  The determinant of the coefficient matrix ($\Delta$) must be zero.
2.  The determinants formed by replacing each column with the constant vector ($\Delta_x, \Delta_y, \Delta_z$) must also be zero.

Let's set up the required determinants. The coefficient matrix `A` and the constant vector `B` are:

$$
A = \begin{vmatrix}
3 & 1 & \beta \\
2 & \alpha & -1 \\
1 & 2 & 1
\end{vmatrix}, \quad B = \begin{vmatrix} 3 \\ -3 \\ 4 \end{vmatrix}
$$

### Step 2: Calculate the Determinants

First, we set the determinant of the coefficient matrix to zero ($\Delta = 0$).

$$
\begin{align*}
\Delta &= \begin{vmatrix}
3 & 1 & \beta \\
2 & \alpha & -1 \\
1 & 2 & 1
\end{vmatrix} = 0 \\
&\implies 3(\alpha \cdot 1 - (-1) \cdot 2) - 1(2 \cdot 1 - (-1) \cdot 1) + \beta(2 \cdot 2 - \alpha \cdot 1) = 0 \\
&\implies 3(\alpha + 2) - 1(2 + 1) + \beta(4 - \alpha) = 0 \\
&\implies 3\alpha + 6 - 3 + 4\beta - \alpha\beta = 0 \\
&\implies \boldsymbol{3\alpha + 4\beta - \alpha\beta + 3 = 0} \quad \cdots(1)
\end{align*}
$$

Next, we set $\Delta_z = 0$. We choose $\Delta_z$ because it will eliminate $\beta$ from the calculation, allowing us to solve for $\alpha$ directly.

$$
\begin{align*}
\Delta_z &= \begin{vmatrix}
3 & 1 & 3 \\
2 & \alpha & -3 \\
1 & 2 & 4
\end{vmatrix} = 0 \\
&\implies 3(\alpha \cdot 4 - (-3) \cdot 2) - 1(2 \cdot 4 - (-3) \cdot 1) + 3(2 \cdot 2 - \alpha \cdot 1) = 0 \\
&\implies 3(4\alpha + 6) - 1(8 + 3) + 3(4 - \alpha) = 0 \\
&\implies 12\alpha + 18 - 11 + 12 - 3\alpha = 0 \\
&\implies 9\alpha + 19 = 0 \\
&\implies \boldsymbol{9\alpha = -19}
\end{align*}
$$

### Step 3: Solve for $\beta$ and the Final Expression

From the $\Delta_z$ calculation, we have $\alpha = -\frac{19}{9}$. Now, substitute this into equation (1):

$$
\begin{align*}
3\left(-\frac{19}{9}\right) + 4\beta - \left(-\frac{19}{9}\right)\beta + 3 &= 0 \\
-\frac{19}{3} + 4\beta + \frac{19}{9}\beta + 3 &= 0 \\
\left(\frac{36}{9} + \frac{19}{9}\right)\beta &= \frac{19}{3} - 3 \\
\frac{55}{9}\beta &= \frac{19-9}{3} \\
\frac{55}{9}\beta &= \frac{10}{3} \\
\beta &= \frac{10}{3} \times \frac{9}{55} = \frac{2 \times 5 \times 3 \times 3}{3 \times 5 \times 11} = \frac{6}{11}
\end{align*}
$$

Now we can calculate the value of the final expression, $22\beta - 9\alpha$.
* $22\beta = 22 \times \frac{6}{11} = 2 \times 6 = 12$
* $9\alpha = -19$

Therefore:

$$22\beta - 9\alpha = 12 - (-19) = 12 + 19 = 31$$