class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        count_fresh = 0
        q = deque([]) # queue of rotten -> (i,j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        if count_fresh == 0: return 0
        time = -1
        dr = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for dx, dy in dr:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        grid[x][y] = 2
                        count_fresh -=1
                        q.append((x,y))
            time += 1
        
        return time if count_fresh == 0 else -1
