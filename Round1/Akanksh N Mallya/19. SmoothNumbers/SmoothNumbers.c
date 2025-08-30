#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// Function to check if a number is smooth
bool is_smooth(int n) {
    int prev = n % 10;
    n /= 10;
    while (n > 0) {
        int d = n % 10;
        if (abs(d - prev) > 1) return false;
        prev = d;
        n /= 10;
    }
    return true;
}

int main() {
    int n = 0, smooth_count = 0;

    while (1) {
        n++;
        if (is_smooth(n)) {
            smooth_count++;
        }
        if (smooth_count * 100 == 25 * n) {  // smooth numbers exactly 25%
            printf("The least number for which smooth numbers are exactly 25%% is: %d\n", n);
            break;
        }
    }

    return 0;
}
