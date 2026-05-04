class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l_h = height[0]
        r_h = height[-1]
        l = 0
        r = len(height) - 1

        while l <= r:
            if height[l] < height[r]:
                ans += max(0,l_h-height[l])
                l_h = max(l_h,height[l])
                l+=1
            else:
                ans += max(0,r_h-height[r])
                r_h = max(r_h, height[r])
                r -= 1
        return ans