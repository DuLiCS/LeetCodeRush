from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            temp = candies.copy()
            temp[i] += extraCandies
            if max(temp) == temp[i]:
                result.append(True)
            else:
                result.append(False)

        return result

candies = [2,3,5,1,3]
extraCandies = 3
sol = Solution()
result = sol.kidsWithCandies(candies, extraCandies)

print(result)
