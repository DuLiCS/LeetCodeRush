public class L1768 {

    public String mergeAlternately(String word1, String word2) {


        StringBuilder result = new StringBuilder();
        int i;
        for(i = 0 ; i<Math.min(word1.length(),word2.length());i++){
            result.append(word1.charAt(i));
            result.append(word2.charAt(i));
        }
        if (word1.length()>word2.length()){
            result.append(word1.substring(i));
        }
        if (word1.length()<word2.length()){
            result.append(word2.substring(i));
        }

        return result.toString();
    }

}
