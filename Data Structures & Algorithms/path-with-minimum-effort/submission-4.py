class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        heap = [(0,(0,0))] # (diff, (i,j))
        visit = set()
        while heap:
            diff, coord = heapq.heappop(heap)
            i , j = coord
            if coord == (row-1,col-1):
                return diff
            if (i,j) in visit:
                continue
            visit.add((coord[0],coord[1]))
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                x = coord[0] + dx
                y = coord[1] + dy
                if 0<=x<row and 0<=y<col and (x,y) not in visit:
                    heapq.heappush(heap, ((max(diff, abs(heights[i][j]-heights[x][y]))), (x,y)))