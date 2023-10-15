from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        if len(prices) == 2:
            if prices[0]<prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
        for i in range(2, len(prices)):
            if prices[i-1] < min:
                min = prices[i-1]
            if prices[i-1] > min and prices[i] < prices[i-1]:
                profit += (prices[i-1] - min)
                min = prices[i]
            if i == len(prices)-1 and prices[-1] > min:
                profit += (prices[-1] - min)
        return profit


    def maxProfit1(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


prices = [1, 2]
sol = Solution()
print(sol.maxProfit(prices))
print(sol.maxProfit1(prices))