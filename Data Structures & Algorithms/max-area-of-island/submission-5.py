class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        count = 0
        def dfs(i,j):
            if not (0<=i<len(grid)) or  not (0<=j<len(grid[0])) or (i,j) in visit or grid[i][j]==0:
                return 0 
            visit.add((i,j))
            return 1 + dfs(i,j+1) + dfs(i,j-1) + dfs(i+1,j) + dfs(i-1,j)
        

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visit:
                    res = max(res,dfs(i,j))

        
        return res