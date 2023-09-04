public class L80 {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 3){
            return nums.length;
        }
        int p = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[p-2]){
                nums[p] = nums[i];
                p++;
            }
        }
        return p;
    }
}
