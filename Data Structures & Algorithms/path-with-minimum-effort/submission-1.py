class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        q = [[0,0,0]]
        visit = set()
        
        direct = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            v,r,c = heapq.heappop(q)
            if (r,c) == (row-1,col-1):
                return v
            if (r,c) in visit:
                continue
            visit.add((r,c))

            for dr,dc in direct:
                R = r+dr
                C = c+dc
                if not(R<0 or C<0 or R==row or C==col or (R,C) in visit):
                    heapq.heappush(q,[max(v,abs(heights[r][c]-heights[R][C])),R,C])
        return 0