public class SquareFree {
    public static void main(String[] args) {
        int N=1000000;
        int count=0;
        for (int i=1;i<=N;i++) {
            if (isSqDiv(i)) {
                count++;
            }
        }
        System.out.println("N "+count);
    }
    static boolean isSqDiv(int num) {
        for (int i=2;i*i<=num;i++) {
            if (num%(i*i)==0) {
                return false; 
            }
        }
        return true;
    }
}
