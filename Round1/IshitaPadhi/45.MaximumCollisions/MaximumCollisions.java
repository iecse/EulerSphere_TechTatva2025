public class MaximumCollisions {

    public static int findMaxCollisions() {
        int p = 103;
        int m = 20;
        int maxCollisions = 0;

        for (int a = 1; a < p; a++) {
            for (int b = 1; b < p; b++) {
                int[] buckets = new int[m];

                for (int n = 0; n < p; n++) {
                    long hashVal = ((long) a * n * n + (long) b * n) % p; // use long
                    int bucket = (int) (hashVal % m);
                    buckets[bucket]++;
                }

                int currentMax = 0;
                for (int count : buckets) {
                    if (count > currentMax) {
                        currentMax = count;
                    }
                }

                if (currentMax > maxCollisions) {
                    maxCollisions = currentMax;
                    // Uncomment to debug:
                    // System.out.println("New Max Found: " + maxCollisions + " at (a=" + a + ", b=" + b + ")");
                }
            }
        }

        return maxCollisions;
    }

    public static void main(String[] args) {
        int result = findMaxCollisions();
        System.out.println("Maximum Collisions: " + result);
    }
}
