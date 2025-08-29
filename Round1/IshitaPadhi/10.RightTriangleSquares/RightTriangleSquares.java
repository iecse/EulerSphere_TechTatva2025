public class RightTriangleSquares {
    public static void main(String[] args) {
        int N = 100; // given input
        int count = 0;

        for (int m = 2; m * m < N; m++) {
            for (int n = 1; n < m; n++) {
                if (((m - n) % 2 == 1) && gcd(m, n) == 1) {
                    int a = m * m - n * n;
                    int b = 2 * m * n;
                    int c = m * m + n * n;

                    if (c > N) continue;

                    // scale primitive triples
                    int k = 1;
                    while (k * c <= N) {
                        int A = k * a;
                        int B = k * b;
                        int C = k * c;

                        int big = Math.max(A, B);
                        if ((C - big) > 0 && C % (C - big) == 0) {
                            count++;
                        }
                        k++;
                    }
                }
            }
        }

        System.out.println("Number of valid triples = " + count);
    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
