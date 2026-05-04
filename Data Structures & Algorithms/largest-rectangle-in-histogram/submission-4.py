class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        st = []

        for i, h in enumerate(heights):
            ind = i
            while st and st[-1][0] >=h:
                ht, ind = st.pop()
                ans = max(ans,(i-ind)*ht)
            st.append([h,ind])
        
        print(st)
        for i in range(len(st)):
            ans = max(ans, st[i][0]*(len(heights)-st[i][1]))
        
        return ans