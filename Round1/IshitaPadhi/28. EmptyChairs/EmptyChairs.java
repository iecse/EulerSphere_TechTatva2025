public class EmptyChairs {
    
    // Function to compute the Josephus position iteratively
    public static int josephus(int n, int k) {
        int result = 0; // Base case: J(1, k) = 0 (0-indexed)
        for (int i = 2; i <= n; i++) {
            result = (result + k) % i;
        }
        return result + 1; // Convert to 1-indexed
    }

    public static void main(String[] args) {
        int n = 20; // Number of people
        int k = 3;  // Step size (every 3rd person removed)

        // Compute the last remaining person's position
        int lastPerson = josephus(n, k);

        // Print the result
        System.out.println(lastPerson);
    }
}
