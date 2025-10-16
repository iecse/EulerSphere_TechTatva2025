import math

# Method 1: Using the given formula directly
# f(x) = 1/(1-x)^3 = sum_{n=0}^∞ C(n+2,2) * x^n
# So coefficient of x^8 is C(8+2,2) = C(10,2)

def binomial_coefficient(n, k):
    """Calculate binomial coefficient C(n,k) = n! / (k! * (n-k)!)"""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

coeff_method1 = binomial_coefficient(10, 2)
print("Method 1: Using given formula")
print(f"Coefficient of x^8 = C(10,2) = {coeff_method1}")
print()

# Method 2: Using derivatives to find Taylor series coefficients
# f(x) = (1-x)^(-3)
# f^(n)(0) / n! gives coefficient of x^n

def factorial(n):
    return math.factorial(n)

def coefficient_from_derivative(n):
    """
    For f(x) = (1-x)^(-3), the nth derivative at x=0 is:
    f^(n)(0) = (-3)(-4)(-5)...(-3-n+1) * (-1)^n
             = 3*4*5*...*(n+2) * (-1)^n * (-1)^n
             = 3*4*5*...*(n+2)
             = (n+2)! / 2!
    So coefficient = f^(n)(0) / n! = (n+2)! / (2! * n!) = C(n+2,2)
    """
    # Direct calculation: coefficient = (n+2)(n+1)/2
    return (n + 2) * (n + 1) // 2

coeff_method2 = coefficient_from_derivative(8)
print("Method 2: Using derivative formula")
print(f"Coefficient of x^8 = (8+2)(8+1)/2 = 10*9/2 = {coeff_method2}")
print()

# Method 3: Manual calculation of C(10,2)
coeff_method3 = (10 * 9) // (2 * 1)
print("Method 3: Manual calculation")
print(f"C(10,2) = 10*9/(2*1) = {coeff_method3}")
print()

# Method 4: Verification using the general binomial series
# (1-x)^(-3) = sum_{n=0}^∞ C(-3,n) * (-x)^n
# where C(-3,n) = (-3)(-4)...(-3-n+1) / n!

def generalized_binomial_coefficient(r, n):
    """Calculate generalized binomial coefficient C(r,n) for negative r"""
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= (r - i) / (i + 1)
    return result

# For (1-x)^(-3), we have C(-3,n) * (-1)^n
gen_binom_coeff = generalized_binomial_coefficient(-3, 8)
coeff_method4 = gen_binom_coeff * ((-1) ** 8)
print("Method 4: Using generalized binomial coefficient")
print(f"C(-3,8) * (-1)^8 = {gen_binom_coeff} * 1 = {coeff_method4}")
print()

# Verify all methods give the same result
print("Verification:")
print(f"Method 1 result: {coeff_method1}")
print(f"Method 2 result: {coeff_method2}")
print(f"Method 3 result: {coeff_method3}")
print(f"Method 4 result: {int(coeff_method4)}")

print(f"\nFINAL ANSWER: {coeff_method1}")

# Additional verification: Generate first few terms of the series
print("\nFirst few terms of the series for verification:")
for n in range(10):
    coeff = binomial_coefficient(n + 2, 2)
    print(f"Coefficient of x^{n}: {coeff}")