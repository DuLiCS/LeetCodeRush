from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        p2 = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[p2 - 2]:
                nums[p2] = nums[i]
                p2 += 1

        return p2


sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums))

