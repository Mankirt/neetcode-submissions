class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * (n)
        dp[-1] = grid[m-1][n-1]
        for i in range(n-2,-1,-1):
            dp[i] = grid[m-1][i] + dp[i+1]
        
        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                if j != n-1:
                    dp[j] = grid[i][j] + min(dp[j],dp[j+1])
                else:
                    dp[j] += grid[i][j] 
        
        return dp[0]
        