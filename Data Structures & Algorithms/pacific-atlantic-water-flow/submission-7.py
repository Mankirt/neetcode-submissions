class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        def bfs(q):
            visit = set()
            while q:
                i, j = q.popleft()
                if (i,j) in visit:
                    continue
                visit.add((i,j))
                dr = [(0,1),(1,0), (-1,0), (0,-1)]
                for dx, dy in dr:
                    r = i + dx
                    c = j + dy
                    if 0<=r<len(heights) and 0<=c<len(heights[0]) and heights[r][c] >= heights[i][j]:
                        q.append([r,c])
            return visit

        q = deque([])
        for j in range(len(heights[0])):
            q.append([0,j])
        for i in range(1,len(heights)):
            q.append([i,0])
        p_set  = bfs(q)

        q = deque([])
        s = len(heights)
        e = len(heights[0])
        for j in range(len(heights[0])):
            q.append([s-1,j])
        for i in range(len(heights)-1):
            q.append([i,e-1])
        a_set  = bfs(q)

        

        res = [item for item in a_set & p_set]
        return res
