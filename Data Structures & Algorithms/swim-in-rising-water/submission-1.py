class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = [[grid[0][0],0,0]]
        direct = [(1,0),(-1,0),(0,1),(0,-1)]
        visit = set()
        while q:
            val, i, j = heapq.heappop(q)
            if (i,j) == (row-1,col-1):
                return val
            visit.add((i,j))
            for dr,dc in direct:
                r = i+dr
                c = j+dc
                if not(r<0 or c<0 or r==row or c==col or (r,c) in visit):
                    heapq.heappush(q,[max(val,grid[r][c]),r,c])
