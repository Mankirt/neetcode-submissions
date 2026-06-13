class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        q = deque([])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i,j)) 
        val = 0
        dr = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] >= val:
                    grid[i][j] = val
                    for dx,dy in dr:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < row and 0 <= y < col and grid[x][y] != -1 and grid[x][y] > val + 1:
                            q.append((x, y))
            val += 1
        
            

