import numpy as np
import math

# Define the matrix B
B = np.array([[1, 3, 2],
              [2, 1, 4],
              [3, 2, 1]])

print("Matrix B:")
print(B)

# Calculate Frobenius norm manually
# ||B||_F = sqrt(sum of squares of all elements)
sum_of_squares = np.sum(B**2)
print(f"Sum of squares of all elements: {sum_of_squares}")

frobenius_norm = math.sqrt(sum_of_squares)
print(f"Frobenius norm ||B||_F: {frobenius_norm}")

# Calculate floor(10000 * ||B||_F)
result = math.floor(10000 * frobenius_norm)
print(f"floor(10000 * ||B||_F): {result}")

# Apply modular arithmetic
final_answer = result % 1000000007
print(f"Answer mod 1000000007: {final_answer}")

# Verification using NumPy's built-in function
frobenius_norm_numpy = np.linalg.norm(B, 'fro')
print(f"\nVerification with NumPy: {frobenius_norm_numpy}")
print(f"floor(10000 * numpy result): {math.floor(10000 * frobenius_norm_numpy)}")