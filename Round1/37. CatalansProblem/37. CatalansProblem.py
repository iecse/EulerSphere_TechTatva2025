def count_paths(i, j, n):
    if i > n or j > n:
        return 0 
    if j > i:
        return 0 
    if i == n and j == n:
        return 1 
    return count_paths(i+1, j, n) + count_paths(i, j+1, n)

result = count_paths(0, 0, 3)
print(result)  