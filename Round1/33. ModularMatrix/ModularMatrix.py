import numpy as np

def matrix_mult_mod(A, B, mod):
    return np.dot(A, B) % mod

def matrix_power_mod(A, n, mod):
    size = A.shape[0]
    result = np.eye(size, dtype=int)
    base = A % mod
    
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult_mod(result, base, mod)
        base = matrix_mult_mod(base, base, mod)
        n //= 2
    
    return result

A = np.array([[7, 3, 2], [1, 5, 4], [6, 2, 9]], dtype=int)
MOD_97 = 97
MOD_FINAL = 1000000007

F_values = []
F1 = np.trace(A) % MOD_97
F_values.append(F1)

n = 1
while True:
    n += 1
    An = matrix_power_mod(A, n, MOD_97)
    trace_n = np.trace(An) % MOD_97
    F_n = trace_n
    
    if F_n == F1:
        m = n
        break
    
    F_values.append(F_n)

N = sum(f**2 for f in F_values) % MOD_FINAL
print(N)