// Returns the count of ways we can
// sum coins[0...n-1] coins to get sum "sum"
int countRecur(int coins[], int n, int sum) {
    // If sum is 0 then there is 1 solution
    // (do not include any coin)
    if (sum == 0)
        return 1;

    // 0 ways in the following two cases
    if (sum < 0 || n == 0)
        return 0;

    // count is sum of solutions (i)
    // including coins[n-1] (ii) excluding coins[n-1]
    return countRecur(coins, n, sum - coins[n - 1]) +
           countRecur(coins, n - 1, sum);
}

int count(int coins[], int n, int sum) {
    return countRecur(coins, n, sum);
}

int main() {
    int coins[] = {5, 50, 100,1000,2500};
    int n = sizeof(coins) / sizeof(coins[0]);
    int sum = 2500;
    printf("%d\n", count(coins, n, sum));
    return 0;
}
