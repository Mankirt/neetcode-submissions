class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        def find(i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j] == 0 :
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            res = find(i+1,j) + find(i-1,j) + find(i,j-1) + find(i, j+1)
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return find(i,j)
        