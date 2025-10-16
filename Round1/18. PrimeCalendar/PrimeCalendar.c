#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

// Function to check prime
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// Function to count Sundays in a given month and year
int countSundays(int year, int month) {
    struct tm timeinfo = {0};
    int count = 0;

    // Loop over all days of the given month
    for (int day = 1; day <= 31; day++) {
        timeinfo.tm_year = year - 1900; // years since 1900
        timeinfo.tm_mon = month - 1;    // 0 = Jan, 11 = Dec
        timeinfo.tm_mday = day;

        // mktime will normalize invalid dates (e.g. Feb 30 -> Mar 2)
        if (mktime(&timeinfo) == -1) continue;

        // Check if still the same month (to avoid overflow days)
        if (timeinfo.tm_mon != month - 1) break;

        if (timeinfo.tm_wday == 0) // Sunday
            count++;
    }
    return count;
}

int main() {
    int start = 2000, end = 2100;
    int sum = 0, count = 0;

    // Step 1: Get primes and calculate sum
    for (int i = start; i <= end; i++) {
        if (isPrime(i)) {
            sum += i;
            count++;
        }
    }

    // Step 2: Average year
    int year = sum / count;
    printf("Average year = %d\n", year);

    // Step 3: Count Sundays in January and December
    int sundaysJan = countSundays(year, 1);
    int sundaysDec = countSundays(year, 12);

    printf("Sundays in January %d: %d\n", year, sundaysJan);
    printf("Sundays in December %d: %d\n", year, sundaysDec);
    printf("Total Sundays (Jan + Dec) = %d\n", sundaysJan + sundaysDec);

    return 0;
}
