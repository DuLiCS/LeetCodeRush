public class L238 {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            ans[i] = 1;
        }
        int left = 1;
        for (int i = 1; i < n; i++) {
            left = left * nums[i - 1];
            ans[i] *= left;
        }
        int right = 1;
        for (int i = n - 2; i >= -1; i--) {
            right *= nums[i + 1];
            ans[i] *= right;
        }
        return ans;
    }
}
