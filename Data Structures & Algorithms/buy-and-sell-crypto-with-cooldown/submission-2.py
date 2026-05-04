class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def find(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            if buy:
                # buy or skip
                res = max(
                    -prices[i] + find(i+1, False),
                    find(i+1, True)
                )
            else:
                # sell (cooldown) or skip
                res = max(
                    prices[i] + find(i+2, True),
                    find(i+1, False)
                )
            
            dp[(i, buy)] = res
            return res
        
        return find(0, True)
