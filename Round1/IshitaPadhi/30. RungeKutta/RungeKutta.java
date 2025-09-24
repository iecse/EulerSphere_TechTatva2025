public class RungeKutta {
    public static void main(String[] args) {
        double h = 0.1;
        double t = 0;
        double y = 1;
        double tEnd = 0.5;

        while (t < tEnd) {
            double k1 = h * f(t, y);
            double k2 = h * f(t + h / 2.0, y + k1 / 2.0);
            double k3 = h * f(t + h / 2.0, y + k2 / 2.0);
            double k4 = h * f(t + h, y + k3);

            y = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0;
            t = t + h;
        }

        System.out.println((int)Math.round(y));
    }

    static double f(double t, double y) {
        return t + y;
    }
}
