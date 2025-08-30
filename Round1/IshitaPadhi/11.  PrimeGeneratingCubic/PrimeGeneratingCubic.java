public class PrimeGeneratingCubic {
    
    public static void main(String[] args) {
        int bestA = 0;
        int bestB = 0;
        int maxConsecutive = 0;
        
        for (int a = -49; a < 50; a++) {
            for (int b = -50; b <= 50; b++) {
                int n = 0;
                while (true) {
                    int value = n * n * n + a * n + b;
                    if (value < 2 || !isPrime(value)) {
                        break;
                    }
                    n++;
                }
                if (n > maxConsecutive) {
                    maxConsecutive = n;
                    bestA = a;
                    bestB = b;
                }
            }
        }
        
        System.out.println(bestA * bestB);
    }
    
    private static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        if (num == 2) {
            return true;
        }
        if (num % 2 == 0) {
            return false;
        }
        for (int i = 3; i * i <= num; i += 2) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}