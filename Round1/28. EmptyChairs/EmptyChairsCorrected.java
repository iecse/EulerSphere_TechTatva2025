import java.util.ArrayList;
import java.util.List;

public class EmptyChairsCorrected {
    public static void main(String[] args) {
        int n = 20; // number of people
        int k = 3;  // step size: remove every 3rd person

        // Initialize people 1..n
        List<Integer> people = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            people.add(i);
        }

        int index = 0; // start from the first person

        // Remove every k-th person until only one remains
        while (people.size() > 1) {
            index = (index + k - 1) % people.size(); // move k-1 steps forward
            people.remove(index); // remove that person
        }

        System.out.println(people.get(0)); // last remaining person
    }
}
