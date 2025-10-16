def sum_alternating_series():
    """
    Calculates the sum: 1*1^2 - 2*3^2 + 3*5^2 - ... + 15*29^2
    The general term is T_n = (-1)^(n+1) * n * (2n-1)^2
    """
    total_sum = 0
    
    num_terms = 15
    
    for n in range(1, num_terms + 1):
        sign = (-1)**(n + 1)
        term = sign * n * (2*n - 1)**2
        total_sum += term
        
    print(f"The sum of the series is: {total_sum}")

sum_alternating_series()