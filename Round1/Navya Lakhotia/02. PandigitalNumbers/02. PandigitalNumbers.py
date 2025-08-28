from itertools import permutations

sum=0

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

for p in permutations(range(10)):
    d = list(p)
    if d[0] == 0:
        continue

    even_sum = d[1] + d[3] + d[5] + d[7] + d[9]
    if not is_prime(even_sum):
        continue

    if (d[1]*100 + d[2]*10 + d[3]) % 4 != 0:
        continue
    if (d[2]*100 + d[3]*10 + d[4]) % 6 != 0:
        continue
    if (d[3]*100 + d[4]*10 + d[5]) % 8 != 0:
        continue
    if (d[4]*100 + d[5]*10 + d[6]) % 9 != 0:
        continue
    if (d[5]*100 + d[6]*10 + d[7]) % 10 != 0:
        continue

    sum += int("".join(map(str, d)))
print(sum%1000000)
