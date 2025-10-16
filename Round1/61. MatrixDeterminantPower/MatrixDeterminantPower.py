import numpy as np

# Define the matrix C
C = np.array([[2, 1, 3],
              [1, 2, 1],
              [3, 1, 2]])

print("Matrix C:")
print(C)

# Method 1: Using NumPy's determinant function
det_C_numpy = np.linalg.det(C)
print(f"\nDeterminant using NumPy: {det_C_numpy}")

# Method 2: Manual calculation using cofactor expansion
# det(C) = 2*(2*2 - 1*1) - 1*(1*2 - 1*3) + 3*(1*1 - 2*3)
# det(C) = 2*(4 - 1) - 1*(2 - 3) + 3*(1 - 6)
# det(C) = 2*3 - 1*(-1) + 3*(-5)
# det(C) = 6 + 1 - 15 = -8

det_C_manual = 2*(2*2 - 1*1) - 1*(1*2 - 1*3) + 3*(1*1 - 2*3)
print(f"Determinant manual calculation: {det_C_manual}")

# Use the manual calculation for exact integer result
det_C = det_C_manual

# Calculate (det(C))^8
# Since det(C) = -8, we need (-8)^8 = 8^8 (since even power)
det_power_8 = det_C ** 8
print(f"(det(C))^8 = ({det_C})^8 = {det_power_8}")

# Apply modular arithmetic
MOD = 1000000007
result = det_power_8 % MOD
print(f"Result mod {MOD}: {result}")

# Verification using fast exponentiation
def fast_power_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Handle negative base
if det_C < 0:
    # (-8)^8 = 8^8 since 8 is even
    base_for_power = abs(det_C)
else:
    base_for_power = det_C

result_fast = fast_power_mod(base_for_power, 8, MOD)
print(f"Using fast exponentiation: {result_fast}")

print(f"\nFinal answer: {result}")