class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j])
                    
        
        t = 1
        while q:   
            for x in range(len(q)):
                i, j  = q.popleft()
                dr = [(0,1),(1,0), (0,-1), (-1,0)]
                for dx, dy in dr:
                    r = i + dx
                    c = j + dy
                    if  (0<=r<len(grid)) and (0<=c<len(grid[0])) and  grid[r][c] == 2147483647:
                        grid[r][c] = t
                       
                        q.append([r,c])
            t+=1
        
                