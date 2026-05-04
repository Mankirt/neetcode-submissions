class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        count = 0
        def dfs(i,j):
            if not (0<=i<len(grid)) or  not (0<=j<len(grid[0])) or (i,j) in visit or grid[i][j]=='0':
                return
            visit.add((i,j))
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visit:
                    dfs(i,j)
                    count+=1
        
        return count