import java.util.HashMap;
import java.util.Map;

public class L13 {
    public int romanToInt(String s) {
        Map<Character, Integer> romanDict = new HashMap<>();
        romanDict.put('I', 1);
        romanDict.put('V', 5);
        romanDict.put('X', 10);
        romanDict.put('L', 50);
        romanDict.put('C', 100);
        romanDict.put('D', 500);
        romanDict.put('M', 1000);

        int total = 0;
        int preNum = 0;
        int value = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            value = romanDict.get(s.charAt(i));
            if (value < preNum){
                total -= value;
            }else {
                total += value;
            }
            preNum = value;
        }
    return total;
    }
}
