public class UniversalHashing {

    public static void main(String[] args) {
        int p = 107;  // prime number
        int m = 12;   // number of buckets
        int totalPairs = 106 * 107;

        int x = 5;  // any distinct x, y
        int y = 10;

        int collisionCount = 0;

        for (int a = 1; a < p; a++) {
            for (int b = 0; b < p; b++) {
                int hx = ((a * x + b) % p) % m;
                int hy = ((a * y + b) % p) % m;

                if (hx == hy) {
                    collisionCount++;
                }
            }
        }

        double probability = (double) collisionCount / totalPairs;
        int percentage = (int) Math.round(probability * 100);

        // Print a single integer (percentage)
        System.out.println(percentage);
    }
}
