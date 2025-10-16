
import java.lang.Math;

public class MinimalReciprocals {

    // Helper function to count the number of divisors (tau) of an integer N
    public static int countDivisors(int N) {
        if (N <= 0) return 0;
        int count = 0;
        for (int i = 1; i * i <= N; i++) {
            if (N % i == 0) {
                // If the divisors are equal (i is the square root), count once
                if (i * i == N) {
                    count++;
                } 
                // Otherwise, count both i and N/i
                else {
                    count += 2;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Fixed Input
        int m = 4;   // required number of solutions

        int n = 1; 
        while (true) {
            // Check the standard formula for the number of solutions for 1/x + 1/y = 1/n
            // Number of solutions = (tau(n^2) - 1) / 2
            int tau_n_squared = countDivisors(n * n);
            
            // The required number of divisors for n^2 is 2*m + 1
            if (tau_n_squared >= (2 * m + 1)) {
                System.out.println(n);
                break;
            }
            n++;
        }
    }
}
