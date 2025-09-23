public class NewtonRaphson {
    // Function f(x)
    public static double f(double x) {
        return x*x*x - 7*x*x + 14*x - 6;
    }

    // Derivative f'(x)
    public static double fPrime(double x) {
        return 3*x*x - 14*x + 14;
    }

    public static void main(String[] args) {
        double x = 3.0;       // Initial guess
        double tolerance = 0.001;
        int maxIter = 20;

        for (int i = 0; i < maxIter; i++) {
            double xNew = x - f(x)/fPrime(x);
            if (Math.abs(xNew - x) < tolerance) {
                x = xNew;
                break;
            }
            x = xNew;
        }

        System.out.println(Math.round(x)); // Output nearest integer
    }
}
