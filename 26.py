from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        k = 0
        j = 100000

        for i in range(len(nums)):
            if nums[i] != j:
                j = nums[i]
                nums[p1] = nums[i]
                k += 1
                p1 += 1
            else:
                continue
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
result = sol.removeDuplicates(nums)
print(result)


