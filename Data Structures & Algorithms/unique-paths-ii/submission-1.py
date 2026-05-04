class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[-1][-1]:
            return 0

        row = len(grid)
        col = len(grid[0])
        dp = [0]*(col+1)

        for i in range(col-1,-1,-1):
            if grid[-1][i] == 1:
                break
            dp[i] = 1
    

        for i in range(row-2,-1,-1):
            for j in range(col-1,-1,-1):
                if grid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j+1]
        
        return dp[0]
        
        
