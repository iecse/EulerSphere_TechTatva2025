public class NewtonRaphson {
    // Function f(x) = x^3 - 7x^2 + 14x - 6
    static double f(double x) {
        return x*x*x - 7*x*x + 14*x - 6;
    }

    // Derivative f'(x) = 3x^2 - 14x + 14
    static double fPrime(double x) {
        return 3*x*x - 14*x + 14;
    }

    public static void main(String[] args) {
        double x = 3.0;       // Initial guess
        double eps = 0.001;   // Tolerance
        int maxIter = 20;     // Maximum iterations

        for (int i = 0; i < maxIter; i++) {
            double xNew = x - f(x) / fPrime(x);
            if (Math.abs(xNew - x) < eps) {
                x = xNew;
                break;
            }
            x = xNew;
        }

        // Round to nearest integer
        System.out.println(Math.round(x));
    }
}
