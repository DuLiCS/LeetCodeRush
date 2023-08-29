import java.util.ArrayList;
import java.util.List;

public class L1431 {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        int max = 0;
        for (int i = 0; i < candies.length; i++){
            int[] temp = candies.clone();
            temp[i] += extraCandies;
            max = temp[0];
            for (int j = 1;j < temp.length; j++) {
                if (temp[j] > max) {
                    max = temp[j];
                }
            }
            if (max == temp[i]){
                result.add(true);
            }
            else {
                result.add(false);
            }
        }
        return result;
    }
}
