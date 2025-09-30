#include <stdio.h>
#include <stdbool.h>

// Function to check for a prime number
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// Zeller’s Congruence to find the day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
int dayOfWeek(int d, int m, int y) {
    int h;
    int J = y / 100;
    int K = y % 100;

    if (m <= 2) {
        m += 12;
        y--;
        J = y / 100;
        K = y % 100;
    }

    h = (d + (13 * (m + 1)) / 5 + K + K / 4 + J / 4 - 2 * J) % 7;
    
    // The original formula gives a value from 0-6 for Sunday-Saturday. 
    // In C, a negative result from the modulo operator can occur, so we ensure a positive result.
    if (h < 0) {
        h += 7;
    }
    return h;
}

int main() {
    int primes[50], count = 0, sum = 0;
    
    // Find primes between 2000 and 2040
    for (int i = 2000; i <= 2040; i++) {
        if (isPrime(i)) {
            primes[count++] = i;
            sum += i;
        }
    }

    // Calculate the average year
    int year = sum / count;
    printf("Average year = %d\n", year);

    // Days in each month (January to December)
    int daysInMonth[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Check for a leap year
    if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {
        daysInMonth[2] = 29;
    }

    int totalSundays = 0;

    // Check January (Month 1)
    for (int d = 1; d <= daysInMonth[1]; d++) {
        if (dayOfWeek(d, 1, year) == 0) totalSundays++;
    }

    // Check December (Month 12)
    for (int d = 1; d <= daysInMonth[12]; d++) {
        if (dayOfWeek(d, 12, year) == 0) totalSundays++;
    }

    printf("Total Sundays in January and December of %d = %d\n", year, totalSundays);

    return 0;
}
