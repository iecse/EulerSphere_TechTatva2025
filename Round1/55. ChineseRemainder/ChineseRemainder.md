# Chinese Remainder Construction
## Difficulty – Hard

Find the **smallest positive integer** \(N\) such that  

$$
N \equiv 2 \pmod{5}, \quad
N \equiv 3 \pmod{7}, \quad
N \equiv 4 \pmod{9}.
$$

## Solution:

Since 5, 7, and 9 are pairwise coprime, a unique solution exists modulo  

$$
M = 5 \cdot 7 \cdot 9 = 315.
$$


### Step 1: Use first congruence
From the first congruence:

$$
N \equiv 2 \pmod{5}
\;\;\Longrightarrow\;\;
N = 2 + 5t.
$$


### Step 2: Impose second congruence
Now require:

$$
N \equiv 3 \pmod{7}.
$$

Substitute:

$$
2 + 5t \equiv 3 \pmod{7},
$$

which simplifies to:

$$
5t \equiv 1 \pmod{7}.
$$

The inverse of 5 modulo 7 is 3, since  

$$
5 \cdot 3 = 15 \equiv 1 \pmod{7}.
$$

So:

$$
t \equiv 3 \pmod{7} \quad \Longrightarrow \quad t = 3 + 7k.
$$

Thus:

$$
N = 2 + 5(3+7k) = 17 + 35k.
$$

So:

$$
N \equiv 17 \pmod{35}.
$$


### Step 3: Impose third congruence
Now require:

$$
N \equiv 4 \pmod{9}.
$$

Substitute:

$$
17 + 35k \equiv 4 \pmod{9}.
$$

Reduce terms:

$$
17 \equiv 8 \pmod{9}, \quad 35 \equiv 8 \pmod{9}.
$$

So:

$$
8 + 8k \equiv 4 \pmod{9}
\;\;\Longrightarrow\;\;
8k \equiv -4 \equiv 5 \pmod{9}.
$$

The inverse of 8 modulo 9 is 8, since  

$$
8 \cdot 8 = 64 \equiv 1 \pmod{9}.
$$


Thus:

$$
k \equiv 5 \cdot 8 \equiv 40 \equiv 4 \pmod{9}.
$$

So:

$$
k = 4 + 9m.
$$


### Step 4: General solution
Substitute back:

$$
N = 17 + 35(4+9m) = 157 + 315m.
$$

Therefore:  

- The **smallest positive solution** is  

$$
\boxed{157}
$$  

### Step 5: Verification
Check with \(N=157\):  

$$
157 \equiv 2 \pmod{5}, \quad
157 \equiv 3 \pmod{7}, \quad
157 \equiv 4 \pmod{9}.
$$

All congruences hold.
