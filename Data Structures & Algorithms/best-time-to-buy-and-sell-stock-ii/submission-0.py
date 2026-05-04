class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = mx = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i]>=mx:
                mx = prices[i]
            else:
                ans+=(mx-mn)
                mn = mx = prices[i]
        ans+= (mx-mn)
        return ans