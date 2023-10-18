from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = (n + 1) * [0]

        for cite in citations:
            if cite >= n:
                buckets[n] += 1
            else:
                buckets[cite] += 1
        sum = 0
        for j in range(n, -1, -1):
            sum += buckets[j]
            if sum >= j:
                return j


citations = [0]
sol = Solution()
print(sol.hIndex(citations))
