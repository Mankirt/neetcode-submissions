class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        st = [] #val, ind

        for i, heigh in enumerate(heights):
            ind = i
            while st and st[-1][0] >= heigh:
                val, ind = st.pop()
                res = max(res, val * (i-ind))
            st.append([heigh, ind])

        length = len(heights)
       
        for heigh, ind in st:
            res = max(res, heigh * (length  - ind))
        
        return res
