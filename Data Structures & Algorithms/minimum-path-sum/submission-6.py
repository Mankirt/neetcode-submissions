class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [float('inf')] * col
        dp[-1] = 0
        for i in range(row-1, -1 ,-1):
            for j in range(col-1, -1 ,-1):
                if j!=col-1:
                    dp[j] = min(dp[j],dp[j+1]) + grid[i][j]
                else:
                    dp[j] += grid[i][j]
        
        return dp[0]
        