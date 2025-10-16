count = 0

for n in range(1, 1001):
    if bin(n).count("1") == 2:
        count += 1

print(count)