class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [0] * col
        for i in range(col-1, -1 ,-1):
            if obstacleGrid[-1][i] == 1:
                break
            dp[i] = 1
        
        for i in range(row-2,-1,-1):
            for j in range(col-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j == col - 1:
                    continue
                else:
                    dp[j] += dp[j+1]
        
        return dp[0]
