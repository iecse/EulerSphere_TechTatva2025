public class BinomialCoeff {
    
    // Function to count the number of times 2 divides n!
    public static int countFactorsOfTwo(int n) {
        int count = 0;
        int powerOfTwo = 2;
        while (powerOfTwo <= n) {
            count += n / powerOfTwo;
            powerOfTwo *= 2;
        }
        return count;
    }

    public static void main(String[] args) {
        int n = 25;
        int r = 12;

        // Count factors of 2 in n!, r!, and (n-r)!
        int factorsN = countFactorsOfTwo(n);
        int factorsR = countFactorsOfTwo(r);
        int factorsNR = countFactorsOfTwo(n - r);

        // Number of factors of 2 in binomial coefficient
        int factorsBinomial = factorsN - factorsR - factorsNR;

        // Print the result
        System.out.println(factorsBinomial);
    }
}
