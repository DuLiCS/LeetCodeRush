public class L169 {
    public int majorityElement(int[] nums) {
        int flag = nums[0];
        int cnt = 0;
        for (int num : nums) {
            if (flag == num) {
                cnt++;
            } else {
                cnt--;
                if (cnt == 0) {
                    flag = num;
                    cnt = 1;
                }
            }
        }
        return flag;
    }
}
