class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        heap = [(grid[0][0],0,0)] #time, i,j
        visit = set()
        while heap:
            time, i , j = heapq.heappop(heap)
            if (i,j) == (row-1, col-1):
                return time
            visit.add((i,j))
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                x = dx + i
                y = dy + j
                if 0<=x<row and 0 <= y < col and (x,y) not in visit:
                    heapq.heappush(heap, (max(grid[x][y], time), x,y))
                