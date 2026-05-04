class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        # ans = [[0]* col for i in range(row)]

        visit_pac = set()
        visit_at = set()

        def dfs(i,j,s,prev):
            if i<0 or j<0 or i==row or j==col or (i,j) in s or heights[i][j]<prev:
                return
            # ans[i][j]+=1
            prev = heights[i][j]
            s.add((i,j))
            dfs(i+1,j,s,prev)
            dfs(i-1,j,s,prev)
            dfs(i,j-1,s,prev)
            dfs(i,j+1,s,prev)

        for i in range(row):
            dfs(i,0,visit_pac,heights[i][0]) 
        
        for j in range(col):
            dfs(0,j,visit_pac,heights[0][j]) 
        
        for i in range(row):
            dfs(i,col-1,visit_at,heights[i][col-1]) 
        
        for j in range(col):
            dfs(row-1,j,visit_at,heights[row-1][j]) 

        res= [list(i) for i in visit_at & visit_pac]
        # for i in range(row):
        #     for j in range(col):
        #         if ans[i][j]==2:
        #             res.append([i,j])
        # print(ans)
        return res