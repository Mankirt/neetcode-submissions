class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [ [1] * col for i in range(row)]
        self.res = 1
        dr = [(1,0),(-1,0), (0,1), (0,-1)]

        def dfs(i,j,prev):
            if not 0<=i<row or not 0<=j<col or matrix[i][j] <= prev:
                return 0
            if dp[i][j] > 1:
                return dp[i][j]
            
            crr = matrix[i][j]
            res = 0
            for dx, dy in dr:
                res = max(res, dfs(i+dx,j+dy,crr))
            dp[i][j] += res
            self.res = max(self.res, dp[i][j])
            return dp[i][j]
        
        for i in range(row):
            for j in range(col):
                dfs(i,j,float('-inf'))
        return self.res
        