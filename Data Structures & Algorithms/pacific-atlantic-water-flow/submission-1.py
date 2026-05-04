class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.r = len(heights)
        self.c = len(heights[0])

        def check(i,j, val):
            if (i<0 or j<0):
                self.p=1
                return
            if (i==self.r or j ==self.c):
                self.a=1
                return
            if heights[i][j] >  val or (i,j) in s:
                return
            new_val = heights[i][j]
            s.add((i,j))
            check(i+1,j,new_val)
            check(i-1,j,new_val)
            check(i,j-1,new_val)
            check(i,j+1,new_val)
            return
        ans=[]
        for i in range(self.r):
            for j in range(self.c):
                self.p = 0
                self.a = 0
                s=set()
                check(i,j,heights[i][j])
                if self.p and self.a:
                    ans.append([i,j])
        return ans