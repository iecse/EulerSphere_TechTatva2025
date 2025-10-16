public class MaximumPathSum {
    public static void main(String[] args) {
        int[][] triangle = {
            {75},
            {95, 64},
            {17, 47, 82},
            {18, 35, 87, 10},
            {20,  4, 82, 47, 65},
            {19,  1, 23, 75,  3, 34},
            {88,  2, 77, 73,  7, 63, 67},
            {99, 65,  4, 28,  6, 16, 70, 92},
            {41, 41, 26, 57, 74, 79, 95, 11, 48},
            {17, 47, 82, 18, 35, 87, 10, 63, 60, 25},
            {20,  4, 82, 47, 65, 19,  4, 23, 76, 41, 39}
        };

        for (int i = triangle.length - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                triangle[i][j] += Math.max(triangle[i+1][j], triangle[i+1][j+1]);
            }
        }

        System.out.println("Maximum Path Sum = " + triangle[0][0]);
    }
}
