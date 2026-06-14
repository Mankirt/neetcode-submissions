class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        set_pacific = set()
        set_atlantic = set()
        
        def dfs(i,j,s,prev):
            if not 0<=i<row or not 0<=j<col or (i,j) in s or heights[i][j] < prev:
                return
            s.add((i,j))
            crr = heights[i][j]
            dfs(i+1,j,s,crr)
            dfs(i-1,j,s,crr)
            dfs(i,j-1,s,crr)
            dfs(i,j+1,s,crr)


        for i in range(col):
            dfs(0,i,set_pacific,0)
            dfs(row-1, i , set_atlantic,0)
        for i in range(row):
            dfs(i,0,set_pacific,0)
            dfs(i,col-1, set_atlantic,0)
        
        return [ [i,j] for i,j in set_pacific & set_atlantic]