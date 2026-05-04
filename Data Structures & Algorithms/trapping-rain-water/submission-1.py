class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        m = height[0]
        for i in range(1,len(height)):
            left[i] = m
            m = max(height[i],m)
        m = height[-1]
        for i in range(len(height)-2,-1,-1):
            right[i] = m
            m = max(height[i],m)
        res = 0
        for i in range(len(height)):
            if height[i] < min(left[i],right[i]):
                res += min(left[i],right[i]) - height[i]
        return res
