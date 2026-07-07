class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[-1]
        b = cost[-2]

        for i in range(len(cost)-3, -1, -1):
            temp = b
            b = cost[i] + min(a,b)
            a = temp
        
        return min(a,b)