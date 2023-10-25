class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCnt = 0
        result = []
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCnt += 1
        for i in nums:
            if zeroCnt > 1:
                return [0] * len(nums)
            if zeroCnt == 1:
                if i != 0:
                    result.append(0)
                else:
                    result.append(product)
            else:
                result.append(product//i)

        return result

    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)

            # 输出数组，初始化为1
            ans = [1] * n

            # 构造左边乘积
            left = 1
            for i in range(1, n):
                left = left * nums[i - 1]
                ans[i] *= left

            # 构造右边乘积
            right = 1
            for i in range(n - 2, -1, -1):
                right = right * nums[i + 1]
                ans[i] *= right

            return ans







