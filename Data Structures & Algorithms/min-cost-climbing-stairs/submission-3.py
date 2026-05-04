class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0 
        b = 0
        for i in range(len(cost)-1,-1,-1):
            cost[i] = cost[i] + min(a,b)
            a = b
            b = cost[i]
        return min(cost[0],cost[1])