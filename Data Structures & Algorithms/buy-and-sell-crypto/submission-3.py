class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0
        for price in prices[1:]:
            if price > low:
                res = max(res, price - low)
            else:
                low = price
        
        return res