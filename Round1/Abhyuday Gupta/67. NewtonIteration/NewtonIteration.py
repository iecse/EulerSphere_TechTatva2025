import math

def f(x):
    """Function f(x) = x^3 - 7x + 3"""
    return x**3 - 7*x + 3

def f_prime(x):
    """Derivative f'(x) = 3x^2 - 7"""
    return 3*x**2 - 7

def newtons_method(x0, tolerance=1e-8, max_iterations=100):
    """
    Apply Newton's method to find root of f(x) = x^3 - 7x + 3
    
    Args:
        x0: Initial guess
        tolerance: Convergence criterion |x_n - x_{n-1}| < tolerance
        max_iterations: Maximum number of iterations
    
    Returns:
        (root, iterations, sequence)
    """
    x_current = x0
    sequence = [x0]
    
    print(f"Newton's Method for f(x) = x³ - 7x + 3")
    print(f"Starting with x₀ = {x0}")
    print(f"Convergence criterion: |xₙ - xₙ₋₁| < {tolerance}")
    print()
    
    print("Iteration | xₙ          | f(xₙ)        | f'(xₙ)       | xₙ₊₁        | |xₙ₊₁ - xₙ|")
    print("-" * 85)
    
    for n in range(max_iterations):
        # Calculate function value and derivative
        fx = f(x_current)
        fpx = f_prime(x_current)
        
        # Check if derivative is zero (would cause division by zero)
        if abs(fpx) < 1e-15:
            print(f"Derivative too close to zero at iteration {n}")
            break
        
        # Apply Newton's formula
        x_next = x_current - fx / fpx
        
        # Calculate difference for convergence check
        diff = abs(x_next - x_current)
        
        print(f"{n:9d} | {x_current:11.8f} | {fx:11.8f} | {fpx:11.8f} | {x_next:11.8f} | {diff:.2e}")
        
        sequence.append(x_next)
        
        # Check convergence
        if diff < tolerance:
            print(f"\nConverged after {n+1} iterations")
            print(f"Root found: x = {x_next:.12f}")
            print(f"Verification: f({x_next:.12f}) = {f(x_next):.2e}")
            return x_next, n+1, sequence
        
        x_current = x_next
    
    print(f"Did not converge within {max_iterations} iterations")
    return x_current, max_iterations, sequence

# Apply Newton's method starting with x₀ = 2
print("NEWTON'S METHOD SOLUTION")
print("=" * 50)

root, iterations, sequence = newtons_method(2.0)

print(f"\nFINAL ANSWER: {iterations} iterations needed")

# Additional verification
print(f"\nAdditional verification:")
print(f"Final root: {root:.12f}")
print(f"f(root) = {f(root):.2e}")
print(f"Last few differences:")
for i in range(max(0, len(sequence)-5), len(sequence)-1):
    diff = abs(sequence[i+1] - sequence[i])
    print(f"|x_{i+1} - x_{i}| = {diff:.2e}")

# Show the convergence graphically
print(f"\nConvergence behavior:")
for i in range(min(10, len(sequence)-1)):
    diff = abs(sequence[i+1] - sequence[i])
    stars = int(-math.log10(diff + 1e-16))
    print(f"Iteration {i+1}: {diff:.2e} " + "*" * min(stars, 20))