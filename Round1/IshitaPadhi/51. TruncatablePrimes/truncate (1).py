import math

# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

# Check if a prime is truncatable from both left and right
def is_truncatable_prime(n):
    s = str(n)
    if len(s) == 1:   # exclude single-digit primes
        return False
    
    # Left truncations
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    
    # Right truncations
    for i in range(len(s)):
        if not is_prime(int(s[:len(s) - i])):
            return False
    
    return True

def find_truncatable_primes():
    trunc_primes = []
    n = 11   # start from two-digit primes
    while len(trunc_primes) < 11:
        if is_prime(n) and is_truncatable_prime(n):
            trunc_primes.append(n)
        n += 2  # only odd numbers need checking
    return trunc_primes

if __name__ == "__main__":
    truncatable_primes = find_truncatable_primes()
    print("Truncatable primes:", truncatable_primes)
    print("Count:", len(truncatable_primes))
    print("Sum:", sum(truncatable_primes))
