## Problem: Multiplicative Cipher Sums

A multiplicative cipher encrypts each letter x (A = 0, B = 1, …, Z = 25) using
E(x)=(k⋅x)mod26

where k is the encryption key. The key k must be coprime with 26 to be valid.

Let V(k, w) be the numeric value of the ciphertext obtained by encrypting the word w with key k, where the ciphertext is read as a base-26 number (e.g. "CAT" → 2·26² + 0·26 + 19).

For example, with w = "MATH" and k = 3:

"MATH" → (12, 0, 19, 7)

Encrypted → (10, 0, 5, 21) → "KAFV"

V(3, "MATH") = 10·26³ + 0·26² + 5·26 + 21 = 177079.

$$
S(N) = \sum_{\substack{1 \leq k \leq N \\ \gcd(k,26)=1}} V(k, \text{"PRIME"}).
$$

For example:

S(10) = 2 165 561.

Find S(1000).
Report the last 12 digits of your answer.
