from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0
        k = 0

        while p1 <= len(nums) - 1 and p2 <= len(nums) - 1:
            if nums[p1] != val:
                nums[p2] = nums[p1]
                p2 += 1
                p1 += 1
                k += 1
            else:
                p1 += 1

        return k





nums = [3, 2, 2, 3]
val = 3
sol = Solution()
print(sol.removeElement(nums, val))
