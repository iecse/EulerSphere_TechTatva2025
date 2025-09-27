import numpy as np

# Define the matrix M
M = np.array([[3, 1, 2],
              [1, 4, 1],
              [2, 1, 5]])

print("Matrix M:")
print(M)
print()

# Method 1: Using the trace property tr(M^2) = λ₁² + λ₂² + λ₃²
print("Method 1: Using tr(M^2) = λ₁² + λ₂² + λ₃²")
print()

# Calculate M^2
M_squared = np.dot(M, M)
print("M² = M × M:")
print(M_squared)
print()

# Calculate trace of M^2
trace_M_squared = np.trace(M_squared)
print(f"tr(M²) = {trace_M_squared}")
print()

# Method 2: Manual calculation of M^2
print("Method 2: Manual calculation of M²")
print()

print("M² calculation step by step:")
print("M²[0,0] = 3×3 + 1×1 + 2×2 = 9 + 1 + 4 = 14")
print("M²[0,1] = 3×1 + 1×4 + 2×1 = 3 + 4 + 2 = 9") 
print("M²[0,2] = 3×2 + 1×1 + 2×5 = 6 + 1 + 10 = 17")
print("M²[1,0] = 1×3 + 4×1 + 1×2 = 3 + 4 + 2 = 9")
print("M²[1,1] = 1×1 + 4×4 + 1×1 = 1 + 16 + 1 = 18")
print("M²[1,2] = 1×2 + 4×1 + 1×5 = 2 + 4 + 5 = 11")
print("M²[2,0] = 2×3 + 1×1 + 5×2 = 6 + 1 + 10 = 17")
print("M²[2,1] = 2×1 + 1×4 + 5×1 = 2 + 4 + 5 = 11")
print("M²[2,2] = 2×2 + 1×1 + 5×5 = 4 + 1 + 25 = 30")
print()

manual_M_squared = np.array([[14, 9, 17],
                             [9, 18, 11],
                             [17, 11, 30]])

print("Manual M²:")
print(manual_M_squared)
print()

manual_trace = 14 + 18 + 30
print(f"Manual tr(M²) = 14 + 18 + 30 = {manual_trace}")
print()

# Method 3: Verification using actual eigenvalues
print("Method 3: Verification using actual eigenvalues")
eigenvalues = np.linalg.eigvals(M)
print("Actual eigenvalues:")
for i, eigenval in enumerate(eigenvalues):
    print(f"λ_{i+1} = {eigenval:.10f}")

sum_of_eigenvalues = np.sum(eigenvalues)
sum_of_squares = np.sum(eigenvalues**2)

print(f"\nλ₁ + λ₂ + λ₃ = {sum_of_eigenvalues:.10f}")
print(f"λ₁² + λ₂² + λ₃² = {sum_of_squares:.10f}")
print()

# Method 4: Using trace properties
print("Method 4: Using trace properties")
trace_M = np.trace(M)
print(f"tr(M) = 3 + 4 + 5 = {trace_M}")
print(f"This equals λ₁ + λ₂ + λ₃ = {sum_of_eigenvalues:.0f}")
print()

# Verification that all methods agree
print("Verification that all methods agree:")
print(f"Method 1 (tr(M²)): {trace_M_squared}")
print(f"Method 2 (manual): {manual_trace}")
print(f"Method 3 (eigenvalues): {sum_of_squares:.0f}")
print()

print(f"FINAL ANSWER: λ₁² + λ₂² + λ₃² = {trace_M_squared}")

# Additional: Show the relationship between traces and symmetric polynomials
print("\nAdditional Information:")
print("For a 3×3 matrix with eigenvalues λ₁, λ₂, λ₃:")
print("• tr(M) = λ₁ + λ₂ + λ₃")
print("• tr(M²) = λ₁² + λ₂² + λ₃²") 
print("• det(M) = λ₁ × λ₂ × λ₃")
print()

det_M = np.linalg.det(M)
product_eigenvalues = np.prod(eigenvalues)
print(f"det(M) = {det_M:.0f}")
print(f"λ₁ × λ₂ × λ₃ = {product_eigenvalues:.0f}")