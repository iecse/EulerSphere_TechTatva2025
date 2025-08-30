#include <stdio.h>

int main(void) {
    const int target = 2500; // 2.5 kg in grams
    const int coins[] = {1, 5, 25, 50, 100, 1000, 2500};
    const int n = sizeof(coins) / sizeof(coins[0]);

    long long dp[target + 1];
    for (int i = 0; i <= target; ++i) dp[i] = 0;
    dp[0] = 1; // one way to make 0

    // Count combinations (order doesn't matter)
    for (int i = 0; i < n; ++i) {
        int c = coins[i];
        for (int a = c; a <= target; ++a) {
            dp[a] += dp[a - c];
        }
    }

    printf("%lld\n", dp[target]); // prints 3444269
    return 0;
}
