## TrigoBlast (Difficulty: Easy)

Find the value of the following determinant:

$$
\begin{vmatrix}
\sin \alpha & \cos \alpha & \sin(\alpha + \delta) \\
\sin \beta & \cos \beta & \sin(\beta + \delta) \\
\sin \gamma & \cos \gamma & \sin(\gamma + \delta)
\end{vmatrix}
$$

***

## Solution

Let the given determinant be $\Delta$.

$$
\Delta = \begin{vmatrix}
\sin \alpha & \cos \alpha & \sin(\alpha + \delta) \\
\sin \beta & \cos \beta & \sin(\beta + \delta) \\
\sin \gamma & \cos \gamma & \sin(\gamma + \delta)
\end{vmatrix}
$$

First, we'll use the trigonometric angle addition formula on the third column ($C_3$):
$\sin(A + B) = \sin A \cos B + \cos A \sin B$.

Applying this, the determinant becomes: 
$$
\Delta = \begin{vmatrix}
\sin \alpha & \cos \alpha & \sin \alpha \cos \delta + \cos \alpha \sin \delta \\
\sin \beta & \cos \beta & \sin \beta \cos \delta + \cos \beta \sin \delta \\
\sin \gamma & \cos \gamma & \sin \gamma \cos \delta + \cos \gamma \sin \delta
\end{vmatrix}
$$

***

Using the property that a determinant can be split into a sum of two determinants if one of its columns (or rows) is a sum of two terms, we get:

$$
\Delta = \begin{vmatrix}
\sin \alpha & \cos \alpha & \sin \alpha \cos \delta \\
\sin \beta & \cos \beta & \sin \beta \cos \delta \\
\sin \gamma & \cos \gamma & \sin \gamma \cos \delta
\end{vmatrix} + \begin{vmatrix}
\sin \alpha & \cos \alpha & \cos \alpha \sin \delta \\
\sin \beta & \cos \beta & \cos \beta \sin \delta \\
\sin \gamma & \cos \gamma & \cos \gamma \sin \delta
\end{vmatrix}
$$

***

Now, we can take the common factors $\cos \delta$ from the third column of the first determinant and $\sin \delta$ from the third column of the second determinant.

$$
\Delta = \cos \delta \begin{vmatrix}
\sin \alpha & \cos \alpha & \sin \alpha \\
\sin \beta & \cos \beta & \sin \beta \\
\sin \gamma & \cos \gamma & \sin \gamma
\end{vmatrix} + \sin \delta \begin{vmatrix}
\sin \alpha & \cos \alpha & \cos \alpha \\
\sin \beta & \cos \beta & \cos \beta \\
\sin \gamma & \cos \gamma & \cos \gamma
\end{vmatrix}
$$

***

A fundamental property of determinants is that if any two columns (or rows) are identical, the value of the determinant is **zero**.
* In the first determinant, Column 1 ($C_1$) is identical to Column 3 ($C_3$).
* In the second determinant, Column 2 ($C_2$) is identical to Column 3 ($C_3$).

Therefore, both determinants evaluate to zero.

$$\Delta = (\cos \delta \times 0) + (\sin \delta \times 0)$$
$$\Delta = 0 + 0 = 0$$

Thus, the value of the determinant is **0**.