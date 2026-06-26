class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])


        heap = [(grid[0][0],0,0)]
        ans = grid[0][0]
        visit = set()
        dr = [(0,1), (0,-1), (1,0), (-1,0)]
        while heap:
            val , i ,j = heapq.heappop(heap)
            if (i,j) == (row-1, col-1):
                return val
            if (i,j) in visit:
                continue
            visit.add((i,j))

            for dx, dy in dr:
                r = i + dx
                c = j + dy
                if (0<=r<row) and (0<=c<col) and (r,c) not in visit:
                    heapq.heappush(heap, (max(val,grid[r][c]),r,c))
            