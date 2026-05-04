class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        r=len(grid)
        c=len(grid[0])
        count = 0
        visit = set()
        q=[]
        def add_banana(i,j):
            if not (0<=i<r) or not(0<=j<c) or (i,j) in visit or grid[i][j]!=1:
                return
            nonlocal count
            count-=1
            visit.add((i,j))
            q.append((i,j))
            return

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
        while q and count>0:
            for i in range(len(q)):
                R,C = q.pop(0)
                add_banana(R+1,C)
                add_banana(R-1,C)
                add_banana(R,C+1)
                add_banana(R,C-1)
            time+=1
        return time if count==0 else -1
