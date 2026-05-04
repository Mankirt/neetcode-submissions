class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visit = set()

        def bfs(i,j):
            q = deque([(i,j)])
            result = 0
            while q:
                for x in range(len(q)):
                    r,c = q.popleft()
                    if not (0<=r<len(grid)) or not (0<=c<len(grid[0])) or (r,c) in visit or not grid[r][c]:
                        continue
                    result += 1
                    visit.add((r,c))
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c+1))
                    q.append((r,c-1))
            
            return result


        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = max(ans,bfs(i,j))
        
        return ans