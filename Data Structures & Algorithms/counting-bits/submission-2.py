class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        crr = 1

        while crr <= n:
            for j in range(crr, min(2 * crr, n + 1)):
                dp[j] = 1 + dp[j - crr]
            crr *= 2

        return dp
