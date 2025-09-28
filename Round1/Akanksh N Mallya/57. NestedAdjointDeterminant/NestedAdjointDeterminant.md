# Nested Adjoint Determinant
## Question Difficulty – Hard

Let  

```math
A = \begin{bmatrix} 
2 & 2+p & 2+p+q \\ 
4 & 6+2p & 8+3p+2q \\ 
6 & 12+3p & 20+6p+3q 
\end{bmatrix}


If

If

det
⁡
 ⁣
(
adj
⁡
(
adj
⁡
(
3
𝐴
)
)
)
=
2
𝑚
⋅
3
𝑛
,
𝑚
,
𝑛
∈
𝑁
,
det(adj(adj(3A)))=2
m
⋅3
n
,m,n∈N,

then find the value of 
𝑚
+
𝑛
m+n.

Solution:

We start with the determinant of matrix 
𝐴
A:

∣
𝐴
∣
=
∣
2
	
2
+
𝑝
	
2
+
𝑝
+
𝑞


4
	
6
+
2
𝑝
	
8
+
3
𝑝
+
2
𝑞


6
	
12
+
3
𝑝
	
20
+
6
𝑝
+
3
𝑞
∣
∣A∣=
	​

2
4
6
	​

2+p
6+2p
12+3p
	​

2+p+q
8+3p+2q
20+6p+3q
	​

	​


Perform column operations:

𝐶
3
→
𝐶
3
−
𝐶
2
−
𝐶
1
⋅
𝑞
2
C
3
	​

→C
3
	​

−C
2
	​

−C
1
	​

⋅
2
q
	​

𝐶
3
→
𝐶
2
−
𝐶
1
⋅
(
1
+
𝑝
2
)
C
3
	​

→C
2
	​

−C
1
	​

⋅(1+
2
p
	​

)

Thus the matrix reduces to:

∣
𝐴
∣
=
∣
2
	
0
	
0


4
	
2
	
2
+
𝑝


6
	
6
	
8
+
3
𝑝
∣
∣A∣=
	​

2
4
6
	​

0
2
6
	​

0
2+p
8+3p
	​

	​


Expanding determinant:

∣
𝐴
∣
=
2
(
(
16
+
6
𝑝
)
−
(
12
+
6
𝑝
)
)
=
2
⋅
4
=
8
=
2
3
∣A∣=2((16+6p)−(12+6p))=2⋅4=8=2
3

Now,

det
⁡
(
adj
⁡
(
adj
⁡
(
3
𝐴
)
)
)
=
∣
3
𝐴
∣
(
3
−
1
)
2
=
∣
3
𝐴
∣
4
det(adj(adj(3A)))=∣3A∣
(3−1)
2
=∣3A∣
4

Since

∣
3
𝐴
∣
=
3
3
⋅
∣
𝐴
∣
,
∣3A∣=3
3
⋅∣A∣,

we get

det
⁡
(
adj
⁡
(
adj
⁡
(
3
𝐴
)
)
)
=
(
3
3
⋅
2
3
)
4
=
(
2
3
⋅
3
3
)
4
=
2
12
⋅
3
12
det(adj(adj(3A)))=(3
3
⋅2
3
)
4
=(2
3
⋅3
3
)
4
=2
12
⋅3
12
Final Answer:
𝑚
=
12
,
𝑛
=
12
⇒
𝑚
+
𝑛
=
24
m=12,n=12⇒m+n=24