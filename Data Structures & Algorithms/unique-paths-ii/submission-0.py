class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==row or j==col or obstacleGrid[i][j] == 1:
                return 0
            
            if (i,j) == (row-1,col-1):
                return 1
            
            dp[(i,j)] = dfs(i+1,j) + dfs(i,j+1) 

            return dp[(i,j)]
        
        return dfs(0,0)
        
