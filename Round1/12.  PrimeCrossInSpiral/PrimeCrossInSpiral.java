public class PrimeCrossInSpiral {

    public static void main(String[] args) {
        int primesCount = 0;
        int totalDiagonals = 1; // Start with the center (1)
        int currentNumber = 1;
        int sideLength = 1;

        // We start with sideLength=1 (only center) and expand in layers
        while (true) {
            sideLength += 2; // Next odd side length
            int step = sideLength - 1; // Step to next corner

            // Generate the 4 corners of the current layer
            for (int corner = 0; corner < 4; corner++) {
                currentNumber += step;
                if (isPrime(currentNumber)) {
                    primesCount++;
                }
            }

            totalDiagonals += 4; // Each layer adds 4 diagonal numbers

            double ratio = (double) primesCount / totalDiagonals;

            // Check if ratio drops below 20%
            if (ratio < 0.20) {
                System.out.println(sideLength);
                break;
            }
        }
    }

    // Helper method to check if a number is prime
    private static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}