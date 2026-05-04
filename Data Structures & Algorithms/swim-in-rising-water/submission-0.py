class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [(grid[0][0],0,0)]
        l = len(grid)
        visit = set((0,0))
        direc = [(0,1),(1,0),(-1,0),(0,-1)]
        while minheap:
            node, r ,c = heapq.heappop(minheap)
            if r == l-1 and c == l-1:
                return node
            for dr,dc in direc:
                new_r = r+dr
                new_c = c+dc
                if 0<=new_r<l and 0<=new_c<l and (new_r,new_c) not in visit:
                    visit.add((new_r,new_c))
                    heapq.heappush(minheap, (max(node,grid[new_r][new_c]), new_r , new_c)) 
                    