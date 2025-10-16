from itertools import product

count = 0
valid_sequences = []

for seq in product(range(1, 7), repeat=3):
    if all(abs(seq[i] - seq[i+1]) != 1 for i in range(2)):
        count += 1

print(count)
