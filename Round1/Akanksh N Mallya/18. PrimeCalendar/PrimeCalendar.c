#include <stdio.h>
#include <math.h>
#include <stdbool.h>

typedef unsigned long long ULL;

// Function to check if a number is prime
bool isPrime(ULL n) {
    if (n < 2) return false;
    if (n % 2 == 0) return (n == 2);
    for (ULL i = 3; i <= (ULL)sqrtl(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// Function to get the largest prime factor
ULL largestPrimeFactor(ULL n) {
    ULL largestPrime = 1;

    while (n % 2 == 0) {
        largestPrime = 2;
        n /= 2;
    }

    for (ULL i = 3; i <= (ULL)sqrtl(n); i += 2) {
        while (n % i == 0) {
            largestPrime = i;
            n /= i;
        }
    }

    if (n > 2) {
        largestPrime = n; // Remaining prime factor
    }

    return largestPrime;
}

// Zeller’s Congruence: returns day of week (0=Saturday, 1=Sunday, ..., 6=Friday)
int dayOfWeek(int d, int m, int y) {
    if (m == 1) { m = 13; y--; }  // January -> 13 of previous year
    if (m == 2) { m = 14; y--; }  // February -> 14 of previous year
    int K = y % 100;
    int J = y / 100;
    int h = (d + (13*(m+1))/5 + K + K/4 + J/4 + 5*J) % 7;
    return h;
}

// Function to get days in a month
int daysInMonth(int m, int y) {
    if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) return 31;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    // February
    if ((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)) return 29;
    return 28;
}

// Function to count Sundays in a month
int countSundays(int m, int y) {
    int days = daysInMonth(m, y);
    int count = 0;
    for (int d = 1; d <= days; d++) {
        int w = dayOfWeek(d, m, y);
        if (w == 1) count++; // Sunday
    }
    return count;
}

int main() {
    // Part 1: Largest prime factor of 2^60 - 1
    ULL n = (1ULL << 60) - 1;
    ULL lpf = largestPrimeFactor(n);

    printf("Number: %llu\n", n);
    printf("Largest Prime Factor: %llu\n", lpf);

    // Part 2: Count Sundays in Jan and Dec of that year
    int year = (int)lpf;

    int sundaysJan = countSundays(1, year);
    int sundaysDec = countSundays(12, year);

    printf("Number of Sundays in Jan %d = %d\n", year, sundaysJan);
    printf("Number of Sundays in Dec %d = %d\n", year, sundaysDec);
    printf("Total Sundays in Jan + Dec = %d\n", sundaysJan + sundaysDec);

    return 0;
}