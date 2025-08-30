public class DoublePalindrome { 
    public static boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    public static void main(String[] args) {
        int limit = 1000;
        int sum = 0;
        for (int i = 1; i < limit; i++){
            if (isPalindrome(Integer.toString(i))) {
                if (isPalindrome(Integer.toBinaryString(i))) {
                    sum += i;
                }
            }
        }
        System.out.println("The sum is:" + sum);
    }
}