import java.util.Stack;

public class L345 {
    public String reverseVowels(String s) {
        int left = 0;
        int right = s.length() - 1;
        String vowels = "aeiouAEIOU";
        char[] charArray = s.toCharArray();

        while(left < right){
            while (left < right && !vowels.contains(String.valueOf(charArray[left]))){
                left ++;
            }
            while (left < right && !vowels.contains(String.valueOf(charArray[right]))){
                right --;
            }
            char temp = charArray[left];
            charArray[left] = charArray[right];
            charArray[right] = temp;
            left ++;
            right --;
        }
        return new String(charArray);
    }
    public String reverseVowels_stack(String s) {
        String vowels = "aeiouAEIOU";

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()){
            if (vowels.contains(String.valueOf(c))){
                stack.push(c);
            }
        }

        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()){
            if (vowels.contains(String.valueOf(c))){
                result.append(stack.pop());
            }
            else {
                result.append(c);
            }
        }
        return result.toString();
    }

}
