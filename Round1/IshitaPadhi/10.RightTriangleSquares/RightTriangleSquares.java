public class RightTriangleSquares {
    public static void main(String[] args) {
        int N = 100; // given input
        int count = 0;

        for (int a = 1; a < N; a++) {
            for (int b = a + 1; b < N; b++) {
                int c2 = a * a + b * b;
                int c = (int) Math.sqrt(c2);

                if (c > N) continue;
                if (c * c != c2) continue; // must be perfect square hypotenuse

                if ((c - b) > 0 && c % (c - b) == 0) {
                    count++;
                }
            }
        }

        System.out.println("Number of valid triples = " + count);
    }
}
