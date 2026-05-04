class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def bfs(q):
            s = set()
            while q:
                i,j = q.popleft()
                s.add((i,j))
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    x = i + dx
                    y = j + dy
                    if 0<=x<len(heights) and 0<=y<len(heights[0]) and (x,y) not in s and heights[x][y] >= heights[i][j]:
                        q.append((x,y))
            return s

        p_q = deque([])
        a_q = deque([])
        for i in range(len(heights)):
            p_q.append([i,0])
            a_q.append([i,len(heights[0])-1])
        for j in range(len(heights[0])):
            p_q.append([0,j])
            a_q.append([len(heights)-1,j])
        
        p_set = bfs(p_q)
        a_set = bfs(a_q)

        res = [list(i) for i in p_set & a_set]
        return res
        

        