def count_partitions(n, max_part):
    if n == 0:
        return 1
    if n < 0 or max_part == 0:
        return 0
    return count_partitions(n - max_part, max_part) + count_partitions(n, max_part - 1)

print(count_partitions(16, 16))