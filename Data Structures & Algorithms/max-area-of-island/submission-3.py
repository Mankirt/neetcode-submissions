class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visit = set()
        resF = 0
        def bfs(i,j):
            q = [(i,j)]
            visit.add((i,j))
            res = 0
            while q:
                x,y = q.pop(0)
                res+=1
                print(x,y)
                direct = [(-1,0),(1,0),(0,1),(0,-1)]
                for dr,dc in direct:
                    r = x + dr
                    c = y + dc
                    if r in range(row) and c in range(col) and grid[r][c] and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))

            return res
        for i in range(row):
            for j in range(col):
                if grid[i][j] and (i,j) not in visit:
                    resF = max(resF,bfs(i,j))
        return resF