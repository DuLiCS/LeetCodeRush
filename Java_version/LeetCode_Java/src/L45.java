public class L45 {
    public int jump(int[] nums) {
        int farthest = 0;
        int end = 0;
        int steps = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = farthest > i + nums[i] ? farthest : i + nums[i];
            if (i == end){
                steps += 1;
                end = farthest;
            }
        }
        return steps;
    }
}
