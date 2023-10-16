
public class L55 {
    public boolean canJump(int[] nums) {
        int max_reach = 0;
        int target = nums.length - 1;
        for (int i = 0; i < nums.length; i++) {
            if (i > max_reach){
                return false;
            }
            max_reach = max_reach > (i + nums[i])?max_reach:(i + nums[i]);
            if(max_reach >= target){
                return true;
            }
        }
        return false;
    }
}
