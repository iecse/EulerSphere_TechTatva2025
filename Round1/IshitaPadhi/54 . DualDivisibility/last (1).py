MOD = 1117117717
LCM = 91  # LCM of 7 and 13

# Step 1: Precompute g(n) for n = 1..91
g_table = [0] * (LCM + 1)
for n in range(1, LCM + 1):
    m = n
    count = 0
    while m != 1:
        if m % 7 == 0:
            m //= 7
        elif m % 13 == 0:
            m //= 13
        else:
            m += 1
            count += 1
    g_table[n] = count

# Step 2: Build transition matrix for residues modulo 91
import numpy as np

M = np.zeros((LCM, LCM), dtype=object)  # object dtype for big integers
for i in range(LCM):
    # i corresponds to residue i+1
    next_i = (i + 1) % LCM
    M[next_i, i] = 1  # each state can go to the next by adding 1

# Step 3: Sum over large power using block counting
# For 7^K * 13^K, we can compute total sum as:
# sum_blocks = (number_of_blocks * sum(g_table)) % MOD

def fast_H(K):
    # number of times full 91-block repeats
    N = pow(7, K) * pow(13, K)
    blocks = N // LCM
    remainder = N % LCM
    total = (blocks * sum(g_table)) % MOD
    total = (total + sum(g_table[1:remainder+1])) % MOD
    return total

if __name__ == "__main__":
    K = 10**6
    print("H(10^6) % 1117117717 =", fast_H(K))
