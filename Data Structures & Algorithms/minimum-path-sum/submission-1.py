class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],0,0)]
        m = len(grid)
        n = len(grid[0])
        visit = set()
        while True:
            val, i ,j = heapq.heappop(heap)
            if (i,j) == (m-1,n-1):
                return val
            visit.add((i,j))
            if i+1 < m and (i+1,j) not in visit:
                heapq.heappush(heap,(val+grid[i+1][j],i+1,j))
            if j+1 < n and (i,j+1) not in visit:
                heapq.heappush(heap,(val+grid[i][j+1],i,j+1))