def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def generate_decimal_palindromes(limit: int):
    """Generate all base-10 palindromes up to limit"""
    palindromes = []
    for length in range(1, 7):  # up to 6 digits (since < 1,000,000)
        half_len = (length + 1) // 2
        start = 10**(half_len - 1) if half_len > 1 else 0
        end = 10**half_len
        for first_half in range(start, end):
            s = str(first_half)
            if length % 2 == 0:
                p = int(s + s[::-1])
            else:
                p = int(s + s[-2::-1])
            if p < limit:
                palindromes.append(p)
    return palindromes

def double_base_palindrome_sum(limit=1_000_000):
    total = 0
    palindromes = generate_decimal_palindromes(limit)
    for n in palindromes:
        hex_str = format(n, "x")  # base-16 representation (lowercase)
        if is_palindrome(hex_str):
            total += n
    return total

if __name__ == "__main__":
    result = double_base_palindrome_sum()
    print("Sum of double-base palindromes under 1,000,000:", result)