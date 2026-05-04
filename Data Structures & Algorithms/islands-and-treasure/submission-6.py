class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        q=[]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        while q:
            
            for i in range(len(q)):
                x,y,v = q.pop(0)
                direct = [(1,0),(-1,0),(0,1),(0,-1)]

                for dr,dc in direct:
                    r = x+dr
                    c = y+dc
                    if r in range(row) and c in range(col) and grid[r][c]==2147483647:
                        q.append((r,c,v+1))
                        grid[r][c] = v+1