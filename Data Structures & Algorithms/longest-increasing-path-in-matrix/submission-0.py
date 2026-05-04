class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = {}
        direct = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            visit.add((i,j))
            res= 1
            for dr,dc in direct:
                x = i+dr
                y = j+dc
                if not(x<0 or y<0 or x==row or y == col or (x,y) in visit or matrix[x][y]<=matrix[i][j]):
                    res  = max(res, 1+ dfs(x,y))
            dp[(i,j)] = res
            return res
        ans = 1
        for i in range(row):
            for j in range(col):
                visit = set()
                ans = max(ans,dfs(i,j))
        print(dp)
        return ans