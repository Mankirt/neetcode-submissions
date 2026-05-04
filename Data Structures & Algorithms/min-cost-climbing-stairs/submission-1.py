class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = cost[-1]
        for i in range(len(cost)-2,-1,-1):
            temp = cost[i] + min(a,b)
            a= b
            b = temp
        return min(a,b)