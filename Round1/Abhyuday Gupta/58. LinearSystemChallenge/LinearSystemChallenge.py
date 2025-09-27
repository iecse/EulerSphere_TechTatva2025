import numpy as np

# Coefficient matrix A and constant vector b
A = np.array([[3, 2, 1], 
              [1, 4, 2], 
              [2, 1, 5]], dtype=float)

b = np.array([7, 11, 13], dtype=float)

# Solve the system Ax = b
solution = np.linalg.solve(A, b)

x, y, z = solution
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# Calculate sum
sum_xyz = x + y + z
print(f"x + y + z = {sum_xyz}")

# Calculate floor(1000 * sum)
result = int(1000 * sum_xyz)
print(f"floor(1000 * (x + y + z)) = {result}")

# Apply modulo
final_answer = result % 1000000007
print(f"Answer mod 1000000007 = {final_answer}")