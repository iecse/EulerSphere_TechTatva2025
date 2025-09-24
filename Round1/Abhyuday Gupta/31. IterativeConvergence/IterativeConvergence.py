import math

def solve_iterative_convergence():
    """
    Solve the iterative convergence problem using Newton-Raphson method.
    
    f(x) = ln(x) + x^2 - 3
    f'(x) = 1/x + 2x
    
    Returns the integer N = floor(10^9 * x*)
    """
    
    def f(x):
        """Function f(x) = ln(x) + x^2 - 3"""
        return math.log(x) + x*x - 3
    
    def f_prime(x):
        """Derivative f'(x) = 1/x + 2x"""
        return 1/x + 2*x
    
    # Initial conditions
    x = 1.0  # x_0 = 1
    tolerance = 1e-12
    max_iterations = 100
    
    print("Iteration | x_k | f(x_k) | f'(x_k) | |x_{k+1} - x_k|")
    print("-" * 60)
    
    for iteration in range(max_iterations):
        # Calculate function value and derivative
        fx = f(x)
        fpx = f_prime(x)
        
        # Newton-Raphson step
        x_new = x - fx / fpx
        
        # Check convergence
        diff = abs(x_new - x)
        
        print(f"{iteration:9} | {x:.12f} | {fx:.6e} | {fpx:.6f} | {diff:.6e}")
        
        # Check stopping criterion
        if diff < tolerance:
            print(f"\nConverged! x* = {x_new}")
            print(f"x* with full precision: {x_new:.15f}")
            
            # Calculate N
            N = math.floor(1e9 * x_new)
            print(f"N = floor(10^9 * x*) = {N}")
            
            # Verify the solution
            verification = f(x_new)
            print(f"\nVerification: f(x*) = {verification:.2e}")
            
            return N
        
        x = x_new
    
    raise RuntimeError("Failed to converge within maximum iterations")

# Solve the problem
if __name__ == "__main__":
    result = solve_iterative_convergence()
    print(f"\nFinal Answer: {result}")