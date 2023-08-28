public class L1071 {
    public String gcdOfStrings(String str1, String str2) {
        String lstr;
        String sstr;
        lstr = str1.length() >= str2.length() ? str1 : str2;
        sstr = str1.length() < str2.length() ? str1 : str2;

        if (lstr.length() % sstr.length() == 0) {
            if (lstr.equals(repeat(sstr, lstr.length() / sstr.length()))) {
                return sstr;
            }
        }

        for (int i = 1;i<sstr.length();++i){
            String divisor = sstr.substring(0,sstr.length()-i);
            if (lstr.length() % divisor.length() == 0 && sstr.length() % divisor.length() == 0){
                if (sstr.equals(repeat(divisor, sstr.length()/divisor.length())) && lstr.equals(repeat(divisor, lstr.length() / divisor.length()))){
                    return divisor;
                }
            }
        }

        return "";
    }
    private String repeat(String s, int times) {
        StringBuilder temp = new StringBuilder();
        for (int i = 0;i<times;++i){
            temp.append(s);
        }
        return temp.toString();
    }
}
