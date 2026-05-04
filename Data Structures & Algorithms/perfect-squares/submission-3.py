class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1000001] * (n+1)
        dp[0] = 0
        sq = [i*i for i in range(1,101)]
        for i in range(1,n+1):
            for s in sq:
                if i-s >=0:
                    dp[i] = min(dp[i], 1 + dp[i-s])
        
        return dp[n]