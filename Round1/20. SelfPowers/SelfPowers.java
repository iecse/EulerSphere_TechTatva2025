
  public class SelfPowers { 
    public static void main(String[] args) {
        long sum = 0;
        int N = 10;

        for (int i = 1; i <= N; i++) {
            long term = 1;
            for (int j = 1; j <= i; j++) {
                term *= i; // compute i^i
            }
            sum += term;
        }

        String result = String.valueOf(sum);
        int digitSum = 0;
        for (int i = 0; i < 3 && i < result.length(); i++) {
            digitSum += result.charAt(i) - '0';
        }

        System.out.println(digitSum);
    }
}