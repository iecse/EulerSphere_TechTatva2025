def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest = 0
second_largest = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if product <= second_largest:
            break
        if is_palindrome(product):
            if product > largest:
                second_largest = largest
                largest = product
            elif product > second_largest:
                second_largest = product

print(largest + second_largest)