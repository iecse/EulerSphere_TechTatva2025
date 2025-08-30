def hanoi(n, source, aux, dest):
    if n == 0:
        return 0
    moves = hanoi(n-1, source, aux, dest)
    moves += 1
    moves += hanoi(n-1, dest, aux, source)
    moves += 1
    moves += hanoi(n-1, source, aux, dest)
    return moves

print(hanoi(15, 'A', 'B', 'C'))
