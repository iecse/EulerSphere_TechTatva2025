public class MaximumPathSum {
    public static void main(String[] args) {
        int[][] tri = {
            {7},
            {3, 8},
            {8, 1, 0},
            {2, 7, 4, 4},
            {4, 5, 2, 6, 5}
        };

        // dp array initialized to the bottom row
        int[] dp = new int[tri[tri.length - 1].length];
        for (int j = 0; j < dp.length; j++) {
            dp[j] = tri[tri.length - 1][j];
        }

        // bottom-up collapse
        for (int i = tri.length - 2; i >= 0; i--) {
            for (int j = 0; j < tri[i].length; j++) {
                dp[j] = tri[i][j] + Math.max(dp[j], dp[j + 1]);
            }
        }

        // dp[0] now contains the maximum total
        System.out.println(dp[0]); // prints: 30
    }
}
