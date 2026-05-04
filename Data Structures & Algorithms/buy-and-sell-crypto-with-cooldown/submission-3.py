class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        def sell(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in dp:
                return dp[(i,buy)]
            
            if buy:
                return max( sell(i+1, not buy) - prices[i],
                sell(i+1, buy))
            else:
                return max(sell(i+2, not buy) + prices[i],
                sell(i+1, buy))
        dp = {}
        return sell(0,True)
