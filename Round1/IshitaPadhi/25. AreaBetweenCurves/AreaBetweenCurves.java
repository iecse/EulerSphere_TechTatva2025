public class AreaBetweenCurves {
    public static double f(double x) {
        return x*x*x - 2*x*x + x + 1;
    }

    public static double g(double x) {
        return x*x + 1;
    }

    public static void main(String[] args) {
        int n = 1000;          // Number of intervals
        double a = 0.0, b = 2.0;
        double dx = (b - a) / n;
        double area = 0.0;

        for (int i = 0; i <= n; i++) {
            double x = a + i * dx;
            double hx = Math.abs(f(x) - g(x));
            if (i == 0 || i == n)
                area += hx / 2.0;
            else
                area += hx;
        }

        area *= dx;

        System.out.println(Math.round(area)); // Output nearest integer
    }
}
