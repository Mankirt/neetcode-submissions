class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()

        R = len(grid)
        C = len(grid[0])
        count = 0

        def check(i,j):
            if not (0<=i<R) or not (0<=j<C) or grid[i][j] == '0' or (i,j) in visit:
                return
            visit.add((i,j))
            
            check(i+1,j)
            check(i-1,j)
            check(i,j+1)
            check(i,j-1)
            return

        for i in range(R):
            for j in range(C):
               
                if grid[i][j]=='1' and (i,j) not in visit:
                    check(i,j)
                    count+=1
        
        return count