class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])

        def check(i,j,val):
            if not(0<=i<r) or not(0<=j<c) or grid[i][j]==-1 or grid[i][j] < val:
                return
            if val < grid[i][j] :
                grid[i][j] = val 
            else:
                val = grid[i][j]
            check(i+1,j,val+1)
            check(i,j+1,val+1)
            check(i,j-1,val+1)
            check(i-1,j,val+1)

            return


        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    
                    check(i,j,0)
        
        