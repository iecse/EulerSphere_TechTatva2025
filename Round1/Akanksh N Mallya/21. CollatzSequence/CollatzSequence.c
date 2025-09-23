#include <stdio.h>

#define LIMIT 10000

long long collatz_cache[LIMIT];

// Function to compute Collatz chain length
long long collatz_length(long long n) {
    if (n < LIMIT && collatz_cache[n] != 0) {
        return collatz_cache[n];
    }

    long long length;
    if (n == 1) {
        length = 1;
    } else if (n % 2 == 0) {
        length = 1 + collatz_length(n / 2);
    } else {
        length = 1 + collatz_length(3 * n + 1);
    }

    if (n < LIMIT) {
        collatz_cache[n] = length;
    }
    return length;
}

int main() {
    long long first_max_length = 0, second_max_length = 0;
    long long first_number = 0, second_number = 0;

    for (long long i = 1; i < LIMIT; i++) {
        long long length = collatz_length(i);

        if (length > first_max_length) {
            // Update both first and second
            second_max_length = first_max_length;
            second_number = first_number;

            first_max_length = length;
            first_number = i;
        } else if (length > second_max_length) {
            second_max_length = length;
            second_number = i;
        }
    }

    printf("Second longest chain under %d:\n", LIMIT);
    printf("Number: %lld\n", second_number);
    printf("Length: %lld\n", second_max_length);

    return 0;
}