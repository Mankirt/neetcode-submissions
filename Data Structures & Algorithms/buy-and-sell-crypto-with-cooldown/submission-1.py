class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def check(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            cool = check(i+1,buy)

            if buy:
                profit = -prices[i] + check(i+1,not buy)
            else:
                profit = prices[i] + check(i+2, not buy)
            
            res = max(profit,cool)
            dp[(i,buy)] = res
            return res
        
        return check(0,True)
