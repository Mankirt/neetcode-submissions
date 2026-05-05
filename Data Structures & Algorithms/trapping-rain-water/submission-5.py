class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = 0, 0 
        l, r = 0, len(height) - 1 
        res = 0
        while l <= r:
            if height[l] < height[r]:
                res += max(0,  l_max -height[l] )
                l_max = max(l_max, height[l])
                l += 1
            else:
                res += max(0, r_max -  height[r] )
                r_max = max(r_max, height[r])
                r -= 1
        
        return res