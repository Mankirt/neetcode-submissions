class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = cost[-1]

        for i in range(len(cost)-2,-1,-1):
            temp = b
            b = cost[i] + min(a,b)
            a = temp

        return min(a,b) 