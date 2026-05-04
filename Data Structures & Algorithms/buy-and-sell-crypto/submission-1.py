class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) <=1:
            return res
        mx = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i] < mx:
                res = max(res,(mx-prices[i]))
            else:
                mx = prices[i]
        return res
        