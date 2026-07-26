class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def find(i, sell):
            if i >= len(prices):
                return 0
            if (i,sell) in dp:
                return dp[(i,sell)]
            if sell:
                res = max(find(i+2,not sell) + prices[i], find(i+1,sell))
            else:
                res = max(find(i+1, not sell) - prices[i], find(i+1, sell))
            dp[(i,sell)] = res
            return res

        return find(0, False)