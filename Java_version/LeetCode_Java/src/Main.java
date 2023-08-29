import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 8, 7};
        int extra = 1;
        L1431 sol = new L1431();
        List<Boolean> result = new ArrayList<>();
        result = sol.kidsWithCandies(arr, extra);
        System.out.println(result);
    }
}