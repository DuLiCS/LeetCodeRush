from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1

        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= target:
                return True
        return Fasle

nums1 = [2, 3, 1, 1, 4]
sol = Solution()
print(sol.canJump(nums1))