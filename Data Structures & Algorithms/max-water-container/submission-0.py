class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        while l<r:
            dif=r-l
            if heights[l]<heights[r]:
                h=heights[l]
                l+=1
            else:
                h=heights[r]
                r-=1
            
            res=max(res,dif*h)
        return res