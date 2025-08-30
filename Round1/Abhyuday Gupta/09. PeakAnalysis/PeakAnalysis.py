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

def contains_digit_2(num):
    return '2' in str(num)

total_sum = 0
for n in range(1, 50001, 2):  # Only odd numbers
    peak, steps = collatz_analysis(n)
    
    if (peak > 3 * n and 
        steps % 4 == 0 and 
        contains_digit_2(peak)):
        total_sum += n

print(total_sum)