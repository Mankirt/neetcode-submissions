class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        row = len(grid)
        col = len(grid[0])

        def dfs(i,j):
            if not(0<=i<row) or not (0<=j<col) or grid[i][j] == '0' or (i,j) in visit:
                return
            
            visit.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visit:
                    dfs(i,j)
                    count+=1
        return count