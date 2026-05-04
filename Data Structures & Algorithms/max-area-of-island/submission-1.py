class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()

        R = len(grid)
        C = len(grid[0])
        ans = 0

        def check(i,j):
            if not (0<=i<R) or not (0<=j<C) or not grid[i][j] or (i,j) in visit:
                return 0 
            visit.add((i,j))
            #grid[i][j] = 0
            return 1+ check(i+1,j) +  check(i-1,j) + check(i,j+1) + check(i,j-1)

        for i in range(R):
            for j in range(C):
               
                if grid[i][j]:
                    ans = max(ans,check(i,j))
                
        
        return ans