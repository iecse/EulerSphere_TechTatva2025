def digital_transformation(n):
    digits = str(n)
    total = 0
    for i, digit in enumerate(reversed(digits)):
        position = i + 1
        total += int(digit) * position
    return total

def chain_length(n):
    seen = set()
    current = n
    length = 1
    
    while current >= 10:
        if current in seen:
            return -1
        seen.add(current)
        current = digital_transformation(current)
        length += 1
    
    return length

def digital_transformation(n):
    digits = str(n)
    total = 0
    for i, digit in enumerate(reversed(digits)):
        position = i + 1
        total += int(digit) * position
    return total

def chain_length(n):
    seen = set()
    current = n
    length = 1
    
    while current >= 10:
        if current in seen:
            return -1
        seen.add(current)
        current = digital_transformation(current)
        length += 1
    
    return length

total_sum = 0
for n in range(1, 1000000):
    if chain_length(n) == 7:
        total_sum += n

print(total_sum)