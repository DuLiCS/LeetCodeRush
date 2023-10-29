from typing import List


class Solution:
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        # 初始化变量
        total_tank, curr_tank = 0, 0
        starting_station = 0

        # 遍历每一个加油站
        for i in range(len(gas)):œ
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # 如果当前油箱为空，设置下一个加油站为起始站，并清空当前油箱
            if curr_tank < 0:
                starting_station = i +œ 1
                curr_tank = 0

        # 如果总的油量 >= 总的花费，返回起始站，否则返回-1
        return starting_station if total_tank >= 0 else -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if cost[i] > gas[i] or gas[i] == 0:
                continue
            else:
                cnt = 0
                tank = gas[i]
                for j in range(n):
                    tank -= cost[(j + i) % n]
                    if tank >= 0:
                        tank += gas[(j + i + 1) % n]
                        cnt += 1
                    else:
                        break
                    if cnt == n:
                        return i
        return -1








gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
solution = Solution()
print(solution.canCompleteCircuit1(gas, cost))