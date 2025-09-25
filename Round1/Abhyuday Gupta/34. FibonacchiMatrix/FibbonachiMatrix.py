import numpy as np

def matrix_mult_mod(A, B, mod):
    return np.dot(A, B) % mod

def matrix_power_mod(A, n, mod):
    size = A.shape[0]
    result = np.eye(size, dtype=int)
    base = A.copy()
    
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult_mod(result, base, mod)
        base = matrix_mult_mod(base, base, mod)
        n //= 2
    
    return result

MOD = 1000000007

M = np.array([[1, 1], [1, 0]], dtype=int)
result_matrix = matrix_power_mod(M, 20, MOD)
F_20 = result_matrix[0][1] % MOD
print(F_20)