#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// Function to check if a number is prime
bool isPrime(int n) {
    if (n < 2) return false;
    if (n % 2 == 0 && n != 2) return false;
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// Function to check if number is Right-Rolling Prime
bool isRightRolling(int n) {
    while (n > 0) {
        if (!isPrime(n)) return false;
        n /= 10;  // remove rightmost digit
    }
    return true;
}

int main() {
    int count = 0, sum = 0;
    for (int i = 11; count < 15; i++) {
        if (isRightRolling(i) && i > 7) {
            printf("%d\n", i);
            sum += i;
            count++;
        }
    }
    printf("Sum = %d\n", sum);
    return 0;
}
