class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0 , len(heights) - 1
        res = 0
        while p1 < p2:
            if heights[p1] < heights[p2]:
                res = max(res, (p2-p1) * heights[p1])
                p1 += 1
            else:
                res = max(res, (p2-p1) * ( heights[p2]))
                p2 -= 1
        
        return res