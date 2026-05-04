class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = 0
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                x = dx + i
                y = dy + j
                if 0<=x<len(matrix) and 0<=y < len(matrix[0]) and matrix[x][y]>matrix[i][j]:
                    res = max(res, dfs(x,y))
            
            dp[(i,j)] = 1 + res
            return 1 + res
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               
                ans = max(ans, dfs(i,j))
        
        return ans
