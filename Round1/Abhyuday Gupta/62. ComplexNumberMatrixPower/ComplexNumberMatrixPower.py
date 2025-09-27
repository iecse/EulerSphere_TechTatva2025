import numpy as np

# Define the complex matrix A
A = np.array([[1+1j, 2+0j], 
              [0-1j, 1-1j]], dtype=complex)

print("Matrix A:")
print(A)
print()

# Method 1: Direct matrix exponentiation using NumPy
A_power_10 = np.linalg.matrix_power(A, 10)
print("A^10 using NumPy matrix_power:")
print(A_power_10)
print()

# Calculate trace of A^10
trace_A10 = np.trace(A_power_10)
print(f"Trace of A^10: {trace_A10}")

# Extract real part of the trace
real_part_trace = trace_A10.real
print(f"Real part of trace: {real_part_trace}")
print(f"Real part as integer: {int(round(real_part_trace))}")
print()

# Method 2: Manual matrix exponentiation using repeated squaring
def matrix_power_complex(matrix, n):
    """Compute matrix^n using repeated squaring"""
    if n == 0:
        return np.eye(matrix.shape[0], dtype=complex)
    if n == 1:
        return matrix.copy()
    
    result = np.eye(matrix.shape[0], dtype=complex)
    base = matrix.copy()
    
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, base)
        base = np.dot(base, base)
        n //= 2
    
    return result

print("Verification using manual exponentiation:")
A_manual_10 = matrix_power_complex(A, 10)
print("A^10 manual calculation:")
print(A_manual_10)
print()

trace_manual = np.trace(A_manual_10)
print(f"Manual trace: {trace_manual}")
print(f"Manual real part: {trace_manual.real}")
print(f"Manual real part as integer: {int(round(trace_manual.real))}")
print()

# Method 3: Step by step for smaller powers to verify
print("Step by step verification:")
powers = {}
powers[1] = A
print("A^1:")
print(powers[1])
print(f"Trace A^1: {np.trace(powers[1])}")
print()

for i in [2, 4, 8]:
    if i == 2:
        powers[i] = np.dot(A, A)
    elif i == 4:
        powers[i] = np.dot(powers[2], powers[2])
    elif i == 8:
        powers[i] = np.dot(powers[4], powers[4])
    
    print(f"A^{i}:")
    print(powers[i])
    print(f"Trace A^{i}: {np.trace(powers[i])}")
    print(f"Real part of trace A^{i}: {np.trace(powers[i]).real}")
    print()

# A^10 = A^8 * A^2
A10_check = np.dot(powers[8], powers[2])
print("A^10 = A^8 * A^2:")
print(A10_check)
print(f"Trace: {np.trace(A10_check)}")
print(f"Real part: {np.trace(A10_check).real}")

print(f"\nFINAL ANSWER: {int(round(real_part_trace))}")