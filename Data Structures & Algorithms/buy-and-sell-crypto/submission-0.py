class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        m=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<m:
                m=prices[i]
                continue
            res=max(res,prices[i]-m)
        return res