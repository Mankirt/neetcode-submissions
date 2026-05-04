class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] # val, ind
        ans = 0
        last_ind = 0
        for i,h in enumerate(heights):
            ind = i
            while st and h <= st[-1][0]:
                ht, ind = st.pop()
                ans = max(ans, ht * (i-ind) )
            st.append((h,ind))
        print(st)
        for h, i in st:
            ans = max(ans, h * (len(heights) - i ))

        return ans