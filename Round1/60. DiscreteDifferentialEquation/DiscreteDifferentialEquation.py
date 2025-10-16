def solve_correctly():
    # y_{n+1} - 2y_n + y_{n-1} = 3^n
    # Rearranged: y_{n+1} = 2y_n - y_{n-1} + 3^n
    
    y = [1, 4]  # y_0 = 1, y_1 = 4
    
    print("y_0 =", y[0])
    print("y_1 =", y[1])
    
    for n in range(1, 10):
        # Calculate y_{n+1} = 2*y_n - y_{n-1} + 3^n
        next_y = 2 * y[n] - y[n-1] + 3**n
        y.append(next_y)
        print(f"y_{n+1} = 2*{y[n]} - {y[n-1]} + 3^{n} = {next_y}")
    
    return y[10]

result = solve_correctly()
print(f"\nFinal answer: y_10 = {result}")