class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3: return n-1
        dp = [i for i in range(n+1)]

        for i in range(4,n+1):
            for j in range(1,i//2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
        print(dp)
        return dp[n]