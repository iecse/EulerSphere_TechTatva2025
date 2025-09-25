public class IndefiniteIntegrals {
    public static void main(String[] args) {
        // x = pi/4
        double x = Math.PI / 4;

        // Compute the indefinite integral F(x) = 2*e^x + 3*cos(x) + 4*sin(x)
        double Fx = 2 * Math.exp(x) + 3 * Math.cos(x) + 4 * Math.sin(x);

        // Print the integer part (truncate decimal)
        System.out.println((int) Fx);
    }
}
