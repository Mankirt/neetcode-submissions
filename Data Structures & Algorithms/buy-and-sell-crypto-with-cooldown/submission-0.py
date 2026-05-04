class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            cool = dfs(i+1, buying)
            if buying:
                x = dfs(i+1, not buying) - prices[i]
            else:
                x = dfs(i+2, not buying) + prices[i]
            
            dp[(i,buying)] = max(cool,x)
            return dp [(i,buying)]
        
        return dfs(0,True)