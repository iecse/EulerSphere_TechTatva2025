import math

def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

def gcd_euclidean(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

print("Fibonacci GCD Problem")
print("Find gcd(F_24, F_18)")
print()

# Method 1: Using the property gcd(F_m, F_n) = F_gcd(m,n)
print("Method 1: Using the Fibonacci GCD property")
print("Property: gcd(F_m, F_n) = F_gcd(m,n)")
print()

# Step 1: Find gcd(24, 18)
gcd_indices = gcd_euclidean(24, 18)
print(f"Step 1: gcd(24, 18) = {gcd_indices}")
print("Calculation using Euclidean algorithm:")
print("24 = 18 × 1 + 6")
print("18 = 6 × 3 + 0")
print("Therefore gcd(24, 18) = 6")
print()

# Step 2: Calculate F_6
F_6 = fibonacci(6)
print(f"Step 2: Calculate F_6")
print("F_1 = 1")
print("F_2 = 1")
print("F_3 = F_2 + F_1 = 1 + 1 = 2")
print("F_4 = F_3 + F_2 = 2 + 1 = 3")
print("F_5 = F_4 + F_3 = 3 + 2 = 5")
print("F_6 = F_5 + F_4 = 5 + 3 = 8")
print(f"Therefore F_6 = {F_6}")
print()

result_property = F_6
print(f"Using the property: gcd(F_24, F_18) = F_6 = {result_property}")
print()

# Method 2: Verification by calculating actual values
print("Method 2: Verification by calculating F_24 and F_18 directly")

F_18 = fibonacci(18)
F_24 = fibonacci(24)

print(f"F_18 = {F_18}")
print(f"F_24 = {F_24}")

actual_gcd = gcd_euclidean(F_24, F_18)
print(f"gcd(F_24, F_18) = gcd({F_24}, {F_18}) = {actual_gcd}")
print()

# Method 3: Show step-by-step Fibonacci calculation
print("Method 3: Step-by-step Fibonacci sequence")
print("First 24 Fibonacci numbers:")
fib_sequence = []
for i in range(1, 25):
    fib_val = fibonacci(i)
    fib_sequence.append(fib_val)
    print(f"F_{i} = {fib_val}")

print()
print(f"From the sequence:")
print(f"F_18 = {fib_sequence[17]}")  # 18th element (0-indexed)
print(f"F_24 = {fib_sequence[23]}")  # 24th element (0-indexed)
print()

# Verification that both methods give same result
print("Verification:")
print(f"Method 1 (using property): {result_property}")
print(f"Method 2 (direct calculation): {actual_gcd}")
print(f"Results match: {result_property == actual_gcd}")
print()

print(f"FINAL ANSWER: {result_property}")

# Additional: Show the GCD calculation step by step
print("\nAdditional verification - GCD calculation:")
print(f"gcd({F_24}, {F_18}) using Euclidean algorithm:")
a, b = F_24, F_18
steps = []
while b:
    quotient = a // b
    remainder = a % b
    steps.append(f"{a} = {b} × {quotient} + {remainder}")
    a, b = b, remainder

for step in steps:
    print(step)
print(f"Therefore gcd({F_24}, {F_18}) = {a}")