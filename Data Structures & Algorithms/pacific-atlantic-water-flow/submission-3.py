class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        # ans = [[0]* col for i in range(row)]

        visit_pac = set()
        visit_at = set()

        def dfs(i,j,s):
            if i<0 or j<0 or i==row or j==col or (i,j) in s:
                return
            # ans[i][j]+=1
            s.add((i,j))
            if i+1<row and heights[i+1][j]>=heights[i][j]: dfs(i+1,j,s)
            if i-1>=0 and heights[i-1][j]>=heights[i][j]:dfs(i-1,j,s)
            if j-1 >=0 and heights[i][j-1]>=heights[i][j]:dfs(i,j-1,s)
            if j+1<col and heights[i][j+1]>=heights[i][j]:dfs(i,j+1,s)

        for i in range(row):
            dfs(i,0,visit_pac) 
        
        for j in range(col):
            dfs(0,j,visit_pac) 
        
        for i in range(row):
            dfs(i,col-1,visit_at) 
        
        for j in range(col):
            dfs(row-1,j,visit_at) 

        res= [list(i) for i in visit_at & visit_pac]
        # for i in range(row):
        #     for j in range(col):
        #         if ans[i][j]==2:
        #             res.append([i,j])
        # print(ans)
        return res