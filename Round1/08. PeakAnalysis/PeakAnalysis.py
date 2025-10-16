def collatz_analysis(n):
    original = n
    steps = 0
    peak = n
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        steps += 1
        peak = max(peak, n)
    
    return peak, steps

def is_perfect_square(num):
    sqrt_num = int(num ** 0.5)
    return sqrt_num * sqrt_num == num

count = 0
for n in range(1, 1001):
    peak, steps = collatz_analysis(n)
    
    if is_perfect_square(peak):
        count += 1

print(count)
