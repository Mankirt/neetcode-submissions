class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        t = 0
        while q and fresh > 0:
            for x in range(len(q)):
                i, j = q.popleft()
                
                dr = [(0,1),(1,0),(-1,0),(0,-1)]
                for dx,dy in dr:
                    r = i + dx
                    c = j + dy
                    if (0<=r<len(grid)) and (0<=c<len(grid[0])) and grid[r][c]==1:
                        q.append([r,c])
                        grid[r][c] = 2
                        fresh-=1
            t+=1
        
        return t if fresh == 0 else -1
        

                