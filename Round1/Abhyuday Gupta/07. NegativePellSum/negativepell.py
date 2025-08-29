#!/usr/bin/env python3
"""
Solution to: The Negative Pell Sum Challenge

Problem: Find all D ≤ 100 (non-perfect squares) where x² - Dy² = -1 has solutions.
For each such D, find the fundamental solution (x,y) and compute x×y.
Return the sum of all these products.

Mathematical approach:
- Generate continued fraction representation of √D
- Check if period length is odd (necessary and sufficient condition for solutions)
- If odd, extract the appropriate convergent to get the fundamental solution
- Sum all products x×y
"""

import math
from fractions import Fraction

def is_perfect_square(n):
    """Check if n is a perfect square"""
    root = int(math.sqrt(n))
    return root * root == n

def continued_fraction_sqrt(n):
    """
    Returns the continued fraction representation of √n
    Returns (a0, period) where:
    - a0 is the integer part 
    - period is the minimal repeating sequence
    
    Uses the standard algorithm for square root continued fractions
    """
    if is_perfect_square(n):
        return (int(math.sqrt(n)), [])
    
    a0 = int(math.sqrt(n))
    
    # Initialize the algorithm
    m, d, a = 0, 1, a0
    period = []
    seen = {}
    
    while True:
        # Update m, d, a according to the algorithm
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        
        # Check if we've seen this state before (period detection)
        state = (m, d)
        if state in seen:
            break
            
        seen[state] = len(period)
        period.append(a)
    
    return (a0, period)

def compute_convergent(a0, period, k):
    """
    Compute the k-th convergent of continued fraction [a0; period[0], period[1], ...]
    Returns a Fraction object representing p_k/q_k
    """
    if k < 0:
        return Fraction(1, 0)  # Convention: p_{-1}/q_{-1} = 1/0
    if k == 0:
        return Fraction(a0, 1)
    
    # Build the continued fraction terms up to position k
    terms = [a0]
    for i in range(k):
        terms.append(period[i % len(period)])
    
    # Use recurrence relation: p_k = a_k * p_{k-1} + p_{k-2}
    #                         q_k = a_k * q_{k-1} + q_{k-2}
    p_prev, p_curr = 1, terms[0]
    q_prev, q_curr = 0, 1
    
    for i in range(1, len(terms)):
        p_next = terms[i] * p_curr + p_prev
        q_next = terms[i] * q_curr + q_prev
        p_prev, p_curr = p_curr, p_next
        q_prev, q_curr = q_curr, q_next
    
    return Fraction(p_curr, q_curr)

def solve_negative_pell(d):
    """
    Find the fundamental solution to x² - dy² = -1
    
    Returns (x, y) if solution exists, None otherwise
    
    Theory: Solutions exist iff the period length of √d is odd.
    If solutions exist, the fundamental solution is given by 
    the convergent p_r/q_r where r = period_length - 1.
    """
    if is_perfect_square(d):
        return None
    
    a0, period = continued_fraction_sqrt(d)
    
    # Check if solutions exist (period length must be odd)
    if len(period) == 0 or len(period) % 2 == 0:
        return None
    
    # For negative Pell equation with odd period length,
    # the fundamental solution is at convergent index = period_length - 1
    convergent_index = len(period) - 1
    convergent = compute_convergent(a0, period, convergent_index)
    
    x, y = convergent.numerator, convergent.denominator
    
    # Verify the solution
    if x * x - d * y * y == -1:
        return (x, y)
    else:
        # This shouldn't happen if our theory and implementation are correct
        print(f"Warning: Verification failed for D={d}")
        return None

def main():
    """Solve the Negative Pell Sum Challenge"""
    print("The Negative Pell Sum Challenge")
    print("=" * 40)
    print("Finding all D ≤ 100 where x² - Dy² = -1 has solutions\n")
    
    total_sum = 0
    valid_solutions = []
    
    for d in range(2, 101):
        if is_perfect_square(d):
            continue  # Skip perfect squares
        
        solution = solve_negative_pell(d)
        if solution:
            x, y = solution
            product = x * y
            total_sum += product
            valid_solutions.append((d, x, y, product))
            
            # Show continued fraction info for verification
            a0, period = continued_fraction_sqrt(d)
            period_str = ', '.join(map(str, period))
            print(f"D={d:2d}: √{d} = [{a0}; {period_str}] (period length: {len(period)})")
            print(f"      Solution: x={x}, y={y} → x×y = {product}")
            print(f"      Verification: {x}² - {d}×{y}² = {x*x - d*y*y}")
            print()
    
    print("=" * 50)
    print(f"Total number of valid D values: {len(valid_solutions)}")
    print(f"Sum of all products (x×y): {total_sum}")
    print("=" * 50)
    
    # Additional verification: show a few examples
    print("\nDetailed verification for first few solutions:")
    for i, (d, x, y, product) in enumerate(valid_solutions[:3]):
        result = x*x - d*y*y
        print(f"D={d}: {x}² - {d}×{y}² = {x*x} - {d*y*y} = {result}")
    
    return total_sum

if __name__ == "__main__":
    answer = main()
    print(f"\n Final Answer: {answer}")