class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0],0,0)] #wt, i , j
        row = len(grid)
        col = len(grid[0])
        visit = set()
        while q:
            wt, i , j = heapq.heappop(q)    
            if (i,j) == (row-1, col-1):
                return wt
            visit.add((i,j))
            for dx, dy in [(1,0), (0,1)]:
                x = i + dx
                y = j + dy
                if x < row and y < col and (x,y) not in visit:
                    heapq.heappush(q, (wt + grid[x][y], x, y)) 
        