class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(i,j):
            if not(0<=i<row) or not (0<=j<col) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        
        for i in range(row):
            for j in range(col):
                ans = max(dfs(i,j), ans)
            
        return ans