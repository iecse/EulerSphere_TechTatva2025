public class FibonacciNuggets {
    public static void main(String[] args) {
        int N = 20;  // You can take input here if needed
        System.out.println("Nuggets up to " + N + ":");

        int sum = 0; // store sum of nuggets

        for (int k = 1; k <= N; k++) {
            if (isNugget(k)) {
                System.out.print(k + " ");
                sum += k; // add to sum
            }
        }

        System.out.println("\nSum of nuggets up to " + N + ": " + sum);
    }

    /**
     * Check if k is a nugget.
     * A nugget occurs when the quadratic equation:
     *     kx^2 + (k+1)x - k = 0
     * has a rational root between 0 and 1.
     */
    public static boolean isNugget(int k) {
        long a = k;
        long b = k + 1;
        long c = -k;

        // Discriminant = b^2 - 4ac
        long D = b * b - 4 * a * c;

        // Must be a perfect square for rational roots
        long sqrtD = (long) Math.sqrt(D);
        if (sqrtD * sqrtD != D) return false;

        // Roots: (-b ± sqrtD) / (2a)
        double root1 = (-b + sqrtD) / (2.0 * a);
        double root2 = (-b - sqrtD) / (2.0 * a);

        // Check if any root lies strictly between 0 and 1
        return (root1 > 0 && root1 < 1) || (root2 > 0 && root2 < 1);
    }
}
