class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        visit = set()
        q = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
        m = 0
        while q and count>0:

            for i in range(len(q)):
                x,y = q.pop(0)
                
                direct = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr,dc in direct:
                    r = x+dr
                    c = y+dc

                    if r<0 or c<0 or r==row or c==col or (r,c) in visit or grid[r][c] != 1:
                        continue
                    q.append((r,c))
                    visit.add((r,c))
                    count-=1
            m+=1
        return m if count==0 else -1
        