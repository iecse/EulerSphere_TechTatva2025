public class CubeSumDiff{
    public static void main(String[] args) {
        int n=100;
        long sum=0;
        long sumcubes=0;
        for(int i=1;i<=n;i++) {
            sum += i;
            sumcubes += (long) i*i*i;
        }
        long cube =sum*sum*sum;
        long difference = cube - sumcubes;
        System.out.println("Difference=" + difference);
    }
}
