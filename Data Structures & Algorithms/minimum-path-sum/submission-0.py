class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [400000] * (col+1)
        dp[-2] = 0

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                dp[j] = grid[i][j]+ min(dp[j],dp[j+1])
            

        return dp[0]

