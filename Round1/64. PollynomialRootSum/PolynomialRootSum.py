import numpy as np

# Given polynomial: P(x) = x^4 - 10x^3 + 35x^2 - 50x + 24
# Standard form: x^4 + ax^3 + bx^2 + cx + d = 0
# Our polynomial: x^4 + (-10)x^3 + (35)x^2 + (-50)x + 24 = 0

print("Polynomial: P(x) = x^4 - 10x^3 + 35x^2 - 50x + 24")
print("Coefficients: a = -10, b = 35, c = -50, d = 24")
print()

# Method 1: Using Vieta's formulas directly
print("Method 1: Using Vieta's formulas")
print("For polynomial x^4 + ax^3 + bx^2 + cx + d = 0:")
print("- Sum of roots (s1) = -a")
print("- Sum of products taken two at a time (s2) = b") 
print("- Sum of products taken three at a time (s3) = -c")
print("- Product of all roots (s4) = d")
print()

s1 = -(-10)  # Sum of roots
s2 = 35      # Sum of products of pairs
s3 = -(-50)  # Sum of products of triples  
s4 = 24      # Product of all roots

print(f"s1 = r1 + r2 + r3 + r4 = {s1}")
print(f"s2 = r1*r2 + r1*r3 + r1*r4 + r2*r3 + r2*r4 + r3*r4 = {s2}")
print(f"s3 = r1*r2*r3 + r1*r2*r4 + r1*r3*r4 + r2*r3*r4 = {s3}")
print(f"s4 = r1*r2*r3*r4 = {s4}")
print()

# Calculate r1^2 + r2^2 + r3^2 + r4^2 using the identity
# (r1 + r2 + r3 + r4)^2 = r1^2 + r2^2 + r3^2 + r4^2 + 2(r1*r2 + r1*r3 + ... + r3*r4)
# Therefore: r1^2 + r2^2 + r3^2 + r4^2 = (sum of roots)^2 - 2*(sum of pairwise products)

sum_of_squares = s1**2 - 2*s2
print("Method 1 calculation:")
print(f"r1^2 + r2^2 + r3^2 + r4^2 = s1^2 - 2*s2")
print(f"= {s1}^2 - 2*{s2}")
print(f"= {s1**2} - {2*s2}")
print(f"= {sum_of_squares}")
print()

# Method 2: Using Newton's identities
print("Method 2: Using Newton's identities")
print("Let p_k = r1^k + r2^k + r3^k + r4^k (power sums)")
print("Newton's identities relate power sums to elementary symmetric polynomials:")
print()

# For a monic polynomial of degree 4:
# p1 = s1
# p2 = s1*p1 - 2*s2 = s1^2 - 2*s2

p1 = s1
p2 = s1 * p1 - 2 * s2

print(f"p1 = s1 = {p1}")
print(f"p2 = s1*p1 - 2*s2 = {s1}*{p1} - 2*{s2} = {s1*p1} - {2*s2} = {p2}")
print()

# Method 3: Verification by finding actual roots
print("Method 3: Verification by finding actual roots")
coefficients = [1, -10, 35, -50, 24]
roots = np.roots(coefficients)
print("Roots of the polynomial:")
for i, root in enumerate(roots):
    if np.isreal(root):
        print(f"r{i+1} = {root.real:.10f}")
    else:
        print(f"r{i+1} = {root:.10f}")

# Calculate sum of squares directly from roots
actual_sum_squares = sum(root**2 for root in roots)
print(f"\nDirect calculation from roots:")
print(f"r1^2 + r2^2 + r3^2 + r4^2 = {actual_sum_squares.real:.10f}")
print()

# Method 4: Check if polynomial factors nicely
print("Method 4: Checking for integer roots")
print("Testing small integer values...")

def evaluate_polynomial(x):
    return x**4 - 10*x**3 + 35*x**2 - 50*x + 24

# Test integer values from 1 to 10
integer_roots = []
for x in range(1, 11):
    if evaluate_polynomial(x) == 0:
        integer_roots.append(x)
        print(f"P({x}) = {evaluate_polynomial(x)} ✓")

if integer_roots:
    print(f"Integer roots found: {integer_roots}")
    
    # If we found integer roots, calculate sum of squares directly
    if len(integer_roots) == 4:
        direct_sum = sum(r**2 for r in integer_roots)
        print(f"Sum of squares from integer roots: {direct_sum}")

print(f"\nFINAL ANSWER: {sum_of_squares}")

# Additional verification
print(f"\nVerification:")
print(f"Method 1 (Vieta's): {sum_of_squares}")
print(f"Method 2 (Newton's): {p2}")
print(f"Method 3 (Numerical): {actual_sum_squares.real:.0f}")