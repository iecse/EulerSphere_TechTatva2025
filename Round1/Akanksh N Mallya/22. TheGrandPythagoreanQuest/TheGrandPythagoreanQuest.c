#include <stdio.h>

#define SUM 5000  // change this to any target sum

int main(void) {
    for (int a = 1; a < SUM; ++a) {
        for (int b = a + 1; b < SUM - a; ++b) {
            int c = SUM - a - b;
            if (a*a + b*b == c*c) {
                long long prod = 1LL * a * b * c;
                printf("Triplet: a=%d, b=%d, c=%d\n", a, b, c);
                printf("Product abc = %lld\n", prod);
                return 0;
            }
        }
    }
    printf("No Pythagorean triplet found for sum = %d\n", SUM);
    return 0;
}

