from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 1
        flag = nums[0]
        n = (len(nums) / 2) if len(nums) % 2 == 0 else (len(nums) + 1) / 2
        for i in range(1, len(nums)):
            if flag == nums[i]:
                cnt += 1
            else:
                cnt = 0
                flag = nums[i]
                cnt += 1
            if cnt >= n:
                return flag

    def majorityElement_1(self, nums: List[int]) -> int:
        cnt = 0
        flag = nums[0]
        for i in range(len(nums)):
            if flag == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    flag = nums[i]
                    cnt = 1

        return flag


sol = Solution()
nums = [2,2]
print(sol.majorityElement_1(nums))