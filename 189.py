from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1

    def rotate1(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, start, end):
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums, k)