class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        minH = [(0,0,0)] # Val, i ,j
        visit = set()
        # visit.add((0,0))
        dr = [(0,1), (1,0), (-1,0), (0,-1)]
        while minH:

            val, i , j = heapq.heappop(minH)
            if (i,j) == (row-1,col-1):
                return val
            if (i,j) in visit:
                continue
            visit.add((i,j))
            
            for dx, dy in dr:
                r = i + dx
                c = j + dy

                if (0<=r<row) and (0<=c<col) and (r,c) not in visit:
                    #visit.add((r,c))
                    heapq.heappush(minH,(max(val, abs(heights[i][j]-heights[r][c])),r,c))
        
        return 0
